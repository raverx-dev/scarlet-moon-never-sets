import fs from 'node:fs/promises';
import fsSync from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn, spawnSync} from 'node:child_process';
import {CANONICAL_REPOSITORY, GAME_PATH, GAME_SHA256, PINNED_COMMIT} from './constants.mjs';
import {QaInfrastructureError} from './errors.mjs';

const REQUIRED_QA_FILES = ['qa/build.py', 'qa/regression.js', 'qa/inspection.js', 'qa/cases.json'];
const BLOCKED_PROTOCOLS = ['https', 'http', 'git', 'ssh', 'file'];

function keptEnvironment(base, keys) {
  const env = {};
  for (const key of keys) if (base[key]) env[key] = base[key];
  return env;
}

export function requestGitEnvironment(base = process.env) {
  const env = {
    ...keptEnvironment(base, ['PATH', 'LANG', 'LC_ALL']),
    GIT_CONFIG_GLOBAL: '/dev/null',
    GIT_CONFIG_SYSTEM: '/dev/null',
    GIT_TERMINAL_PROMPT: '0',
    GIT_ASKPASS: '/bin/false',
    GIT_CONFIG_COUNT: String(BLOCKED_PROTOCOLS.length + 1)
  };
  BLOCKED_PROTOCOLS.forEach((protocol, index) => {
    env[`GIT_CONFIG_KEY_${index}`] = `protocol.${protocol}.allow`;
    env[`GIT_CONFIG_VALUE_${index}`] = 'never';
  });
  const safeDirectory = BLOCKED_PROTOCOLS.length;
  env[`GIT_CONFIG_KEY_${safeDirectory}`] = 'safe.directory';
  env[`GIT_CONFIG_VALUE_${safeDirectory}`] = '*';
  return env;
}

function provisioningGitEnvironment(base = process.env) {
  return {
    ...keptEnvironment(base, ['PATH', 'LANG', 'LC_ALL', 'HTTPS_PROXY', 'HTTP_PROXY', 'NO_PROXY', 'https_proxy', 'http_proxy', 'no_proxy']),
    GIT_CONFIG_GLOBAL: '/dev/null',
    GIT_CONFIG_SYSTEM: '/dev/null',
    GIT_TERMINAL_PROMPT: '0',
    GIT_ASKPASS: '/bin/false'
  };
}

function runGit(args, {cwd, env, code, timeoutMs = 45_000}) {
  return new Promise((resolve, reject) => {
    const child = spawn('git', args, {cwd, env, stdio: ['ignore', 'pipe', 'pipe']});
    let stdout = '';
    let stderr = '';
    const timer = setTimeout(() => {
      child.kill('SIGKILL');
      reject(new QaInfrastructureError(`${code}_timeout`, `${code} timed out`));
    }, timeoutMs);
    child.stdout.on('data', chunk => { stdout += chunk.toString('utf8'); });
    child.stderr.on('data', chunk => { stderr += chunk.toString('utf8'); });
    child.once('error', error => {
      clearTimeout(timer);
      reject(new QaInfrastructureError(code, `${code}: ${error.code || 'spawn error'}`));
    });
    child.once('close', status => {
      clearTimeout(timer);
      if (status !== 0) reject(new QaInfrastructureError(code, `${code} exited with status ${status}`));
      else resolve({stdout, stderr});
    });
  });
}

function isInside(parent, child) {
  const relative = path.relative(parent, child);
  return relative === '' || (!relative.startsWith('..') && !path.isAbsolute(relative));
}

async function hashFile(file) {
  const data = await fs.readFile(file);
  return crypto.createHash('sha256').update(data).digest('hex');
}

async function validateTrackedSymlinks(sourceDir, env) {
  const {stdout} = await runGit(['ls-files', '-s', '-z'], {cwd: sourceDir, env, code: 'source_symlink_scan'});
  for (const entry of stdout.split('\0').filter(Boolean)) {
    const match = entry.match(/^(\d+) [0-9a-f]+ \d+\t(.+)$/s);
    if (!match) throw new QaInfrastructureError('source_index_invalid', 'source index entry was invalid');
    if (match[1] !== '120000') continue;
    const link = path.resolve(sourceDir, match[2]);
    let target;
    try { target = await fs.realpath(link); }
    catch { throw new QaInfrastructureError('source_symlink_invalid', 'source contains a dangling symlink'); }
    if (!isInside(sourceDir, target)) throw new QaInfrastructureError('source_symlink_escape', 'source contains an escaping symlink');
  }
}

export async function validatePinnedSource(pinnedSource, {runRoot} = {}) {
  if (!pinnedSource || !path.isAbsolute(pinnedSource)) {
    throw new QaInfrastructureError('pinned_source_missing', 'QA_PINNED_SOURCE must be an absolute prepared source directory');
  }
  let sourceDir;
  try { sourceDir = await fs.realpath(pinnedSource); }
  catch { throw new QaInfrastructureError('pinned_source_missing', 'prepared source directory is absent'); }
  if (runRoot) {
    const runRootReal = await fs.realpath(runRoot);
    if (isInside(runRootReal, sourceDir) || isInside(sourceDir, runRootReal)) {
      throw new QaInfrastructureError('pinned_source_overlap', 'prepared source must stay outside the writable run directory');
    }
  }
  const env = requestGitEnvironment();
  let head;
  try {
    head = (await runGit(['rev-parse', 'HEAD'], {cwd: sourceDir, env, code: 'source_revision'})).stdout.trim();
  } catch {
    throw new QaInfrastructureError('pinned_source_invalid', 'prepared source is not a Git checkout');
  }
  if (head !== PINNED_COMMIT) throw new QaInfrastructureError('pinned_source_wrong_commit', 'prepared source is not the approved game commit');
  const branch = await runGit(['symbolic-ref', '--quiet', 'HEAD'], {cwd: sourceDir, env, code: 'source_branch'}).then(() => true, () => false);
  if (branch) throw new QaInfrastructureError('pinned_source_not_detached', 'prepared source must be a detached checkout of the approved commit');
  const remote = (await runGit(['remote', 'get-url', 'origin'], {cwd: sourceDir, env, code: 'source_remote'})).stdout.trim();
  if (remote !== CANONICAL_REPOSITORY) throw new QaInfrastructureError('pinned_source_wrong_remote', 'prepared source origin is not the canonical repository');
  const status = (await runGit(['status', '--porcelain=v1', '--untracked-files=all'], {cwd: sourceDir, env, code: 'source_status'})).stdout;
  if (status.trim()) throw new QaInfrastructureError('pinned_source_dirty', 'prepared source has uncommitted or untracked changes');
  await validateTrackedSymlinks(sourceDir, env);
  for (const relative of [GAME_PATH, ...REQUIRED_QA_FILES]) {
    const file = path.join(sourceDir, relative);
    let real;
    try { real = await fs.realpath(file); }
    catch { throw new QaInfrastructureError('pinned_source_incomplete', 'prepared source is missing a required file'); }
    const info = await fs.lstat(file);
    if (!info.isFile() || !isInside(sourceDir, real)) throw new QaInfrastructureError('pinned_source_incomplete', 'prepared source file failed containment validation');
  }
  const toolRevision = (await runGit(['log', '-1', '--format=%H', '--', ...REQUIRED_QA_FILES], {cwd: sourceDir, env, code: 'qa_tool_revision'})).stdout.trim();
  if (toolRevision !== PINNED_COMMIT) throw new QaInfrastructureError('pinned_source_wrong_tool_revision', 'prepared QA tooling revision is not the approved commit');
  const gameHash = await hashFile(path.join(sourceDir, GAME_PATH));
  if (gameHash !== GAME_SHA256) throw new QaInfrastructureError('game_hash_mismatch', 'pinned game HTML failed identity validation');
  return {sourceDir, head, toolRevision, gameSha256: gameHash, acquisition: 'prepared-offline'};
}

export async function materializePinnedSource(runDir, pinnedSource, runRoot) {
  const prepared = await validatePinnedSource(pinnedSource, {runRoot});
  const sourceDir = path.join(runDir, 'source');
  await fs.cp(prepared.sourceDir, sourceDir, {recursive: true, verbatimSymlinks: true});
  await fs.chmod(sourceDir, 0o700);
  return validatePinnedSource(sourceDir);
}

function assertStageDestination(destination) {
  if (!destination || !path.isAbsolute(destination)) throw new QaInfrastructureError('stage_destination_invalid', 'stage destination must be absolute');
  const resolved = path.resolve(destination);
  const base = path.basename(resolved);
  if (resolved === path.parse(resolved).root || base === '.' || base === '..' || resolved.split(path.sep).length < 3) {
    throw new QaInfrastructureError('stage_destination_invalid', 'stage destination is too broad');
  }
  let existing;
  try { existing = fsSync.lstatSync(resolved); }
  catch (error) {
    if (error.code !== 'ENOENT') throw new QaInfrastructureError('stage_destination_invalid', 'stage destination could not be inspected');
  }
  if (existing) throw new QaInfrastructureError('stage_destination_exists', 'refusing to replace an existing staging destination');
  const parent = path.dirname(resolved);
  let parentStat;
  try { parentStat = fsSync.lstatSync(parent); }
  catch { throw new QaInfrastructureError('stage_destination_invalid', 'stage destination parent is missing'); }
  if (!parentStat.isDirectory() || parentStat.isSymbolicLink()) {
    throw new QaInfrastructureError('stage_destination_invalid', 'stage destination parent must be a real directory');
  }
  return {resolved, parent, base};
}

function publishNewDirectory(source, destination) {
  const script = `
import ctypes, errno, os, sys
libc = ctypes.CDLL(None, use_errno=True)
if not hasattr(libc, "renameat2"):
    sys.exit(2)
AT_FDCWD = -100
RENAME_NOREPLACE = 1
libc.renameat2.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
rc = libc.renameat2(AT_FDCWD, os.fsencode(sys.argv[1]), AT_FDCWD, os.fsencode(sys.argv[2]), RENAME_NOREPLACE)
if rc != 0:
    sys.exit(17 if ctypes.get_errno() == errno.EEXIST else 1)
`;
  const result = spawnSync(process.env.PYTHON || '/usr/bin/python3', ['-c', script, source, destination], {encoding: 'utf8'});
  if (result.status === 0) return;
  if (result.status === 17) throw new QaInfrastructureError('stage_destination_exists', 'staging destination appeared before publication');
  throw new QaInfrastructureError('stage_publish_failed', 'prepared source could not be published without replacement');
}

function isAttemptTemp(parent, candidate, base) {
  const name = path.basename(candidate);
  const prefix = `.${base}.staging-${process.pid}-`;
  if (!name.startsWith(prefix)) return false;
  return path.resolve(path.dirname(candidate)) === path.resolve(parent);
}

export async function stagePinnedSource(destination, {env = process.env} = {}) {
  const {resolved, parent, base} = assertStageDestination(destination);
  const temporary = path.join(parent, `.${base}.staging-${process.pid}-${crypto.randomBytes(6).toString('hex')}`);
  const gitEnv = provisioningGitEnvironment(env);
  let created = false;
  try {
    await fs.mkdir(temporary, {mode: 0o755});
    created = true;
    await runGit(['init', '--quiet'], {cwd: temporary, env: gitEnv, code: 'stage_init'});
    await runGit(['remote', 'add', 'origin', CANONICAL_REPOSITORY], {cwd: temporary, env: gitEnv, code: 'stage_remote'});
    await runGit(['-c', 'protocol.file.allow=never', 'fetch', '--quiet', '--depth=1', 'origin', PINNED_COMMIT], {
      cwd: temporary, env: gitEnv, code: 'stage_fetch', timeoutMs: 120_000
    });
    await runGit(['checkout', '--quiet', '--detach', 'FETCH_HEAD'], {cwd: temporary, env: gitEnv, code: 'stage_checkout'});
    await validatePinnedSource(temporary);
    publishNewDirectory(temporary, resolved);
    created = false;
    return validatePinnedSource(resolved);
  } finally {
    if (created && isAttemptTemp(parent, temporary, base)) {
      await fs.rm(temporary, {recursive: true, force: true}).catch(() => {});
    }
  }
}
