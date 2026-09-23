import fs from 'node:fs/promises';
import fsSync from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
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
  if (resolved === path.parse(resolved).root || resolved.split(path.sep).length < 3) {
    throw new QaInfrastructureError('stage_destination_invalid', 'stage destination is too broad');
  }
}

export async function stagePinnedSource(destination) {
  assertStageDestination(destination);
  try { return await validatePinnedSource(destination); }
  catch (error) {
    if (!(error instanceof QaInfrastructureError)) throw error;
    if (!fsSync.existsSync(destination)) {
      // create below
    } else {
      const entries = await fs.readdir(destination);
      const marker = path.join(destination, '.git', 'scarlet-qa-pin');
      if (entries.length > 0 && !fsSync.existsSync(marker)) {
        throw new QaInfrastructureError('stage_destination_refused', 'refusing to replace a directory that is not a previous pin stage');
      }
    }
  }
  await fs.rm(destination, {recursive: true, force: true});
  await fs.mkdir(destination, {recursive: true, mode: 0o755});
  const env = provisioningGitEnvironment();
  await runGit(['init', '--quiet'], {cwd: destination, env, code: 'stage_init'});
  await fs.writeFile(path.join(destination, '.git', 'scarlet-qa-pin'), `${PINNED_COMMIT}\n`, {mode: 0o644});
  await runGit(['remote', 'add', 'origin', CANONICAL_REPOSITORY], {cwd: destination, env, code: 'stage_remote'});
  await runGit(['-c', 'protocol.file.allow=never', 'fetch', '--quiet', '--depth=1', 'origin', PINNED_COMMIT], {
    cwd: destination, env, code: 'stage_fetch', timeoutMs: 120_000
  });
  await runGit(['checkout', '--quiet', '--detach', 'FETCH_HEAD'], {cwd: destination, env, code: 'stage_checkout'});
  return validatePinnedSource(destination);
}
