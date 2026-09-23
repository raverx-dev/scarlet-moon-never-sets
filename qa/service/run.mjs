import fs from 'node:fs/promises';
import fsSync from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn, spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {chromium} from 'playwright-core';
import {
  CANONICAL_REPOSITORY,
  CASE_ID,
  CASE_SCENE,
  CASE_TICK,
  GAME_PATH,
  GAME_SHA256,
  LOGICAL_HEIGHT,
  LOGICAL_WIDTH,
  PINNED_COMMIT,
  RUN_TIMEOUT_MS
} from './constants.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const qaRoot = path.resolve(here, '..');
const repoRoot = path.resolve(qaRoot, '..');
const staticServerPath = path.join(here, 'static-server.mjs');

export class QaInfrastructureError extends Error {
  constructor(code, message, evidence = {}) {
    super(message);
    this.name = 'QaInfrastructureError';
    this.code = code;
    this.evidence = evidence;
  }
}

function hashBuffer(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

function remaining(deadline, maximum) {
  const value = Math.min(maximum, deadline - Date.now());
  if (value <= 0) throw new QaInfrastructureError('run_timeout', 'QA run exceeded its time limit');
  return value;
}

async function hashFile(file) {
  return hashBuffer(await fs.readFile(file));
}

function childEnv(extra = {}) {
  const keep = ['PATH', 'LANG', 'LC_ALL', 'HTTPS_PROXY', 'HTTP_PROXY', 'NO_PROXY', 'https_proxy', 'http_proxy', 'no_proxy'];
  const env = {};
  for (const key of keep) if (process.env[key]) env[key] = process.env[key];
  return {...env, ...extra};
}

function terminate(child) {
  if (!child || child.exitCode !== null || child.killed) return;
  try {
    if (process.platform !== 'win32' && child.pid) process.kill(-child.pid, 'SIGTERM');
    else child.kill('SIGTERM');
  } catch {}
  const timer = setTimeout(() => {
    try {
      if (process.platform !== 'win32' && child.pid) process.kill(-child.pid, 'SIGKILL');
      else child.kill('SIGKILL');
    } catch {}
  }, 1_000);
  timer.unref();
}

function runCommand(command, args, {cwd, env = childEnv(), timeoutMs = 45_000, maxOutput = 256 * 1024, code = 'subprocess_failed'} = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, {cwd, env, stdio: ['ignore', 'pipe', 'pipe'], detached: process.platform !== 'win32'});
    let stdout = '';
    let stderr = '';
    let overflow = false;
    const append = (target, chunk) => {
      const next = target + chunk.toString('utf8');
      if (Buffer.byteLength(next) > maxOutput) overflow = true;
      return next.slice(0, maxOutput);
    };
    child.stdout.on('data', chunk => { stdout = append(stdout, chunk); if (overflow) terminate(child); });
    child.stderr.on('data', chunk => { stderr = append(stderr, chunk); if (overflow) terminate(child); });
    const timer = setTimeout(() => {
      terminate(child);
      reject(new QaInfrastructureError(`${code}_timeout`, `${code} timed out`));
    }, timeoutMs);
    child.once('error', error => {
      clearTimeout(timer);
      reject(new QaInfrastructureError(code, `${code}: ${error.code || 'spawn error'}`));
    });
    child.once('close', status => {
      clearTimeout(timer);
      if (overflow) reject(new QaInfrastructureError(`${code}_output_limit`, `${code} exceeded its output limit`));
      else if (status !== 0) reject(new QaInfrastructureError(code, `${code} exited with status ${status}`));
      else resolve({stdout, stderr});
    });
  });
}

function browserBinary() {
  const candidates = [
    process.env.BROWSER_BIN,
    '/usr/lib64/chromium-browser/chromium-browser',
    '/usr/lib/chromium-browser/chromium-browser',
    '/usr/bin/google-chrome-stable', '/usr/bin/google-chrome',
    '/usr/bin/chromium', '/usr/bin/chromium-browser',
    '/usr/bin/microsoft-edge-stable', '/usr/bin/microsoft-edge'
  ];
  for (const candidate of candidates) {
    if (!candidate) continue;
    try {
      if (!fsSync.existsSync(candidate)) continue;
      const real = fsSync.realpathSync(candidate);
      if (real.endsWith('.sh') && fsSync.existsSync(real.slice(0, -3))) return real.slice(0, -3);
      return real;
    } catch {}
  }
  for (const command of ['google-chrome-stable', 'google-chrome', 'chromium', 'chromium-browser', 'microsoft-edge']) {
    const result = spawnSync('which', [command], {encoding: 'utf8'});
    if (result.status === 0 && result.stdout.trim()) return fsSync.realpathSync(result.stdout.trim().split(/\r?\n/)[0]);
  }
  return null;
}

async function validateTrackedSymlinks(sourceDir) {
  const {stdout} = await runCommand('git', ['ls-files', '-s', '-z'], {cwd: sourceDir, code: 'source_symlink_scan'});
  for (const entry of stdout.split('\0').filter(Boolean)) {
    const match = entry.match(/^(\d+) [0-9a-f]+ \d+\t(.+)$/s);
    if (!match) throw new QaInfrastructureError('source_index_invalid', 'source index entry was invalid');
    if (match[1] !== '120000') continue;
    const link = path.resolve(sourceDir, match[2]);
    let target;
    try { target = await fs.realpath(link); }
    catch { throw new QaInfrastructureError('source_symlink_invalid', 'source contains a dangling symlink'); }
    if (target !== sourceDir && !target.startsWith(`${sourceDir}${path.sep}`)) {
      throw new QaInfrastructureError('source_symlink_escape', 'source contains an escaping symlink');
    }
  }
}

async function cloneAndValidate(runDir, repository, deadline) {
  const sourceDir = path.join(runDir, 'source');
  await fs.mkdir(sourceDir, {mode: 0o700});
  const gitEnv = childEnv({
    GIT_CONFIG_GLOBAL: '/dev/null',
    GIT_CONFIG_SYSTEM: '/dev/null',
    GIT_TERMINAL_PROMPT: '0',
    GIT_ASKPASS: '/bin/false'
  });
  await runCommand('git', ['init', '--quiet'], {cwd: sourceDir, env: gitEnv, timeoutMs: remaining(deadline, 45_000), code: 'source_init'});
  await runCommand('git', ['remote', 'add', 'origin', repository], {cwd: sourceDir, env: gitEnv, timeoutMs: remaining(deadline, 45_000), code: 'source_remote'});
  await runCommand('git', ['-c', 'protocol.file.allow=never', 'fetch', '--quiet', '--depth=1', 'origin', PINNED_COMMIT], {
    cwd: sourceDir, env: gitEnv, timeoutMs: remaining(deadline, 60_000), code: 'source_fetch'
  });
  await runCommand('git', ['checkout', '--quiet', '--detach', 'FETCH_HEAD'], {cwd: sourceDir, env: gitEnv, timeoutMs: remaining(deadline, 45_000), code: 'source_checkout'});
  const head = (await runCommand('git', ['rev-parse', 'HEAD'], {cwd: sourceDir, env: gitEnv, timeoutMs: remaining(deadline, 45_000), code: 'source_revision'})).stdout.trim();
  const remote = (await runCommand('git', ['remote', 'get-url', 'origin'], {cwd: sourceDir, env: gitEnv, timeoutMs: remaining(deadline, 45_000), code: 'source_remote_check'})).stdout.trim();
  const toolRevision = (await runCommand('git', ['log', '-1', '--format=%H', '--', 'qa/build.py', 'qa/regression.js', 'qa/inspection.js', 'qa/cases.json'], {
    cwd: sourceDir, env: gitEnv, timeoutMs: remaining(deadline, 45_000), code: 'qa_tool_revision'
  })).stdout.trim();
  if (head !== PINNED_COMMIT || toolRevision !== PINNED_COMMIT || remote !== repository) {
    throw new QaInfrastructureError('source_identity_mismatch', 'source or QA-tool revision did not match the pin');
  }
  await validateTrackedSymlinks(sourceDir);
  const gameFile = path.join(sourceDir, GAME_PATH);
  const gameReal = await fs.realpath(gameFile);
  if (!gameReal.startsWith(`${sourceDir}${path.sep}`) || await hashFile(gameReal) !== GAME_SHA256) {
    throw new QaInfrastructureError('game_hash_mismatch', 'pinned game HTML failed identity validation');
  }
  return {sourceDir, head, toolRevision};
}

async function startStaticServer(sourceDir, generatedFile) {
  const token = crypto.randomBytes(32).toString('hex');
  const child = spawn(process.execPath, [staticServerPath], {
    cwd: sourceDir,
    env: childEnv({QA_STATIC_FILE: generatedFile, QA_STATIC_TOKEN: token, QA_STATIC_PORT: '0'}),
    stdio: ['ignore', 'pipe', 'pipe'],
    detached: process.platform !== 'win32'
  });
  let stderr = '';
  child.stderr.on('data', chunk => { stderr = (stderr + chunk.toString('utf8')).slice(0, 16 * 1024); });
  const port = await new Promise((resolve, reject) => {
    let stdout = '';
    const timer = setTimeout(() => { terminate(child); reject(new QaInfrastructureError('static_server_timeout', 'isolated QA server did not start')); }, 5_000);
    child.stdout.on('data', chunk => {
      stdout += chunk.toString('utf8');
      const newline = stdout.indexOf('\n');
      if (newline < 0) return;
      clearTimeout(timer);
      try {
        const parsed = JSON.parse(stdout.slice(0, newline));
        if (!Number.isInteger(parsed.port) || parsed.port < 1 || parsed.port > 65535) throw new Error('bad port');
        resolve(parsed.port);
      } catch {
        terminate(child);
        reject(new QaInfrastructureError('static_server_invalid', 'isolated QA server returned invalid startup data'));
      }
    });
    child.once('error', error => { clearTimeout(timer); reject(new QaInfrastructureError('static_server_failed', `isolated QA server: ${error.code || 'spawn error'}`)); });
    child.once('exit', status => {
      if (status !== null) {
        clearTimeout(timer);
        reject(new QaInfrastructureError('static_server_failed', `isolated QA server exited with status ${status}`));
      }
    });
  });
  return {child, port, token, stderr: () => stderr};
}

async function waitJson(locator, timeout = 90_000) {
  const end = Date.now() + timeout;
  while (Date.now() < end) {
    const text = (await locator.textContent())?.trim() || '';
    if (text.startsWith('{')) return JSON.parse(text);
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  throw new QaInfrastructureError('browser_result_timeout', 'browser QA result timed out');
}

function safeRequestUrl(value) {
  try {
    const url = new URL(value);
    return `${url.protocol}//${url.host}${url.pathname}`;
  } catch { return 'invalid-url'; }
}

function pngDimensions(buffer) {
  const signature = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  if (buffer.length < 24 || !buffer.subarray(0, 8).equals(signature) || buffer.toString('ascii', 12, 16) !== 'IHDR') {
    throw new QaInfrastructureError('capture_png_invalid', 'browser capture was not a valid PNG');
  }
  return {width: buffer.readUInt32BE(16), height: buffer.readUInt32BE(20)};
}

export function assertCaptureState(metadata) {
  const expected = {
    state: 'play',
    stage: Number(CASE_SCENE.slice('stage'.length)),
    stateTick: CASE_TICK,
    stageTick: CASE_TICK,
    frame: CASE_TICK
  };
  if (!metadata || typeof metadata !== 'object' || Array.isArray(metadata)) {
    throw new QaInfrastructureError('capture_state_mismatch', 'browser capture did not return runtime state metadata');
  }
  for (const [field, value] of Object.entries(expected)) {
    if (!Object.hasOwn(metadata, field) || metadata[field] !== value) {
      throw new QaInfrastructureError('capture_state_mismatch', `browser capture runtime ${field} did not match the pinned case`);
    }
  }
  return metadata;
}

export function classifyCaptureIssues(consoleErrors, blockedRequests, counts = {
  consoleErrors: consoleErrors.length,
  blockedRequests: blockedRequests.length
}) {
  // No errors are exempted for this pinned capture. Preserve a failed frame as evidence, never as PASS.
  return {
    status: counts.consoleErrors === 0 && counts.blockedRequests === 0 ? 'passed' : 'failed',
    materialErrors: consoleErrors
  };
}

export function classifyRegression(regression, consoleErrors, blockedRequests) {
  const failedChecks = regression?.failed;
  if (typeof failedChecks !== 'number' || !Number.isInteger(failedChecks) || failedChecks < 0) {
    throw new QaInfrastructureError('regression_result_invalid', 'regression result was invalid');
  }
  const materialErrors = consoleErrors.filter(error => {
    try { return !/^\/(favicon\.ico|apple-touch-icon[^/]*)$/i.test(new URL(error.url).pathname); }
    catch { return true; }
  });
  return {
    status: failedChecks === 0 && materialErrors.length === 0 && blockedRequests.length === 0 ? 'passed' : 'failed',
    failedChecks,
    materialErrors
  };
}

async function browserRun(kind, sourceDir, deadline) {
  const generatedFile = path.join(sourceDir, 'qa', 'generated.html');
  await runCommand(process.env.PYTHON || 'python3', [path.join(sourceDir, 'qa', 'build.py')], {
    cwd: sourceDir,
    env: childEnv({SCARLET_QA_SOURCE: GAME_PATH}),
    timeoutMs: remaining(deadline, 20_000),
    code: 'qa_build'
  });
  if (!fsSync.existsSync(generatedFile)) throw new QaInfrastructureError('qa_build_missing', 'QA build did not create the generated page');
  const executable = browserBinary();
  if (!executable) throw new QaInfrastructureError('browser_missing', 'no supported Chromium-family browser was found');

  let browser;
  let context;
  let isolatedServer;
  const consoleErrors = [];
  const blockedRequests = [];
  const MAX_RECORDED_BROWSER_EVENTS = 32;
  let consoleErrorCount = 0;
  let blockedRequestCount = 0;
  try {
    isolatedServer = await startStaticServer(sourceDir, generatedFile);
    const origin = `http://127.0.0.1:${isolatedServer.port}`;
    browser = await chromium.launch({
      headless: true,
      executablePath: executable,
      timeout: remaining(deadline, 30_000),
      env: childEnv(),
      args: ['--autoplay-policy=no-user-gesture-required']
    });
    const browserVersion = browser.version();
    context = await browser.newContext({
      viewport: {width: 1100, height: 760},
      extraHTTPHeaders: {authorization: `Bearer ${isolatedServer.token}`},
      serviceWorkers: 'block'
    });
    await context.route('**/*', async route => {
      const requestUrl = route.request().url();
      try {
        const parsed = new URL(requestUrl);
        if (parsed.origin === origin && ['/', '/generated.html', '/favicon.ico'].includes(parsed.pathname)) {
          await route.continue();
          return;
        }
      } catch {}
      blockedRequestCount += 1;
      if (blockedRequests.length < MAX_RECORDED_BROWSER_EVENTS) {
        blockedRequests.push({url: safeRequestUrl(requestUrl), resourceType: route.request().resourceType()});
      }
      await route.abort('blockedbyclient');
    });
    const page = await context.newPage();
    page.setDefaultTimeout(remaining(deadline, 90_000));
    page.on('console', message => {
      if (message.type() !== 'error') return;
      const location = message.location();
      consoleErrorCount += 1;
      if (consoleErrors.length < MAX_RECORDED_BROWSER_EVENTS) {
        consoleErrors.push({type: 'console', text: message.text().slice(0, 2_000), url: location?.url ? safeRequestUrl(location.url) : null});
      }
    });
    page.on('pageerror', error => {
      consoleErrorCount += 1;
      if (consoleErrors.length < MAX_RECORDED_BROWSER_EVENTS) {
        consoleErrors.push({type: 'pageerror', text: String(error).slice(0, 2_000), url: null});
      }
    });
    await page.goto(`${origin}/`, {waitUntil: 'load', timeout: remaining(deadline, 30_000)});
    await page.waitForSelector('#audit-scene');

    if (kind === 'capture') {
      await page.selectOption('#audit-scene', CASE_SCENE);
      await page.fill('#audit-tick', String(CASE_TICK));
      await page.locator('#audit-jump').click();
      await page.waitForFunction(() => document.querySelector('#audit-meta')?.textContent?.trim().startsWith('{'));
      const captured = await page.evaluate(() => {
        const canvas = document.querySelector('#game');
        if (!(canvas instanceof HTMLCanvasElement)) throw new Error('game canvas missing');
        return {
          pngBase64: canvas.toDataURL('image/png').replace(/^data:image\/png;base64,/, ''),
          metadata: JSON.parse(document.querySelector('#audit-meta')?.textContent || '{}'),
          canvas: {width: canvas.width, height: canvas.height},
          selectedScene: document.querySelector('#audit-scene')?.value,
          selectedTick: Number(document.querySelector('#audit-tick')?.value)
        };
      });
      const png = Buffer.from(captured.pngBase64, 'base64');
      const dimensions = pngDimensions(png);
      if (dimensions.width !== LOGICAL_WIDTH || dimensions.height !== LOGICAL_HEIGHT ||
          captured.canvas.width !== LOGICAL_WIDTH || captured.canvas.height !== LOGICAL_HEIGHT ||
          captured.selectedScene !== CASE_SCENE || captured.selectedTick !== CASE_TICK) {
        throw new QaInfrastructureError('capture_state_mismatch', 'browser capture dimensions or selected state did not match the pinned case');
      }
      const sceneMetadata = assertCaptureState(captured.metadata);
      return {
        browser: {executable, version: browserVersion, headless: true},
        consoleErrors, blockedRequests,
        browserEventCounts: {consoleErrors: consoleErrorCount, blockedRequests: blockedRequestCount},
        ...classifyCaptureIssues(consoleErrors, blockedRequests, {consoleErrors: consoleErrorCount, blockedRequests: blockedRequestCount}),
        png, dimensions, sceneMetadata
      };
    }

    await page.locator('#run-qa').click();
    const regression = await waitJson(page.locator('#qa-results'), remaining(deadline, 90_000));
    await page.getByRole('button', {name: 'Run acceptance diagnostics'}).click();
    const diagnostics = await waitJson(page.locator('#audit-diagnostics'), remaining(deadline, 90_000));
    const classification = classifyRegression(regression, consoleErrors, blockedRequests);
    return {browser: {executable, version: browserVersion, headless: true}, consoleErrors, blockedRequests, regression, diagnostics, ...classification};
  } catch (error) {
    if (error instanceof QaInfrastructureError) throw error;
    throw new QaInfrastructureError('browser_execution_failed', `browser execution failed: ${error.name || 'error'}`);
  } finally {
    if (context) await context.close().catch(() => {});
    if (browser) await browser.close().catch(() => {});
    if (isolatedServer) terminate(isolatedServer.child);
  }
}

async function serviceRevision() {
  const result = await runCommand('git', ['rev-parse', 'HEAD'], {cwd: repoRoot, code: 'service_revision'});
  const dirty = spawnSync('git', ['diff', '--quiet', '--', 'qa/service', 'qa/package.json', 'qa/package-lock.json', 'qa/README.md'], {cwd: repoRoot}).status !== 0;
  return {commit: result.stdout.trim(), dirty};
}

async function writeJson(file, value) {
  await fs.writeFile(file, `${JSON.stringify(value, null, 2)}\n`, {mode: 0o600});
}

function artifactRecord(runId, artifactId, mediaType, bytes, sha256) {
  return {artifactId, mediaType, bytes, sha256, endpoint: `/artifacts/${runId}/${artifactId}`};
}

export async function runQa(kind, {runRoot, repository = CANONICAL_REPOSITORY, now = () => new Date()} = {}) {
  if (!['capture', 'regression'].includes(kind)) throw new QaInfrastructureError('operation_invalid', 'invalid QA operation');
  if (!path.isAbsolute(runRoot || '')) throw new QaInfrastructureError('run_root_invalid', 'QA_SERVICE_RUN_ROOT must be an absolute path');
  await fs.mkdir(runRoot, {recursive: true, mode: 0o700});
  const rootReal = await fs.realpath(runRoot);
  const runId = crypto.randomUUID();
  const runDir = path.join(rootReal, runId);
  const evidenceDir = path.join(runDir, 'evidence');
  const sourceDir = path.join(runDir, 'source');
  await fs.mkdir(evidenceDir, {recursive: true, mode: 0o700});
  const deadline = Date.now() + RUN_TIMEOUT_MS;
  try {
    const source = await cloneAndValidate(runDir, repository, deadline);
    const runtime = await browserRun(kind, source.sourceDir, deadline);
    remaining(deadline, RUN_TIMEOUT_MS);
    const revision = await serviceRevision();
    const base = {
      status: runtime.status,
      operation: kind === 'capture' ? 'qa_capture' : 'qa_regression',
      runId,
      generatedAt: now().toISOString(),
      source: {
        repository: CANONICAL_REPOSITORY,
        exactCommit: source.head,
        gamePath: GAME_PATH,
        gameSha256: GAME_SHA256,
        qaToolRevision: source.toolRevision
      },
      runtime: {browser: runtime.browser, serviceRevision: revision},
      request: {case: CASE_ID, scene: CASE_SCENE, tick: CASE_TICK},
      consoleErrors: runtime.consoleErrors,
      blockedRequests: runtime.blockedRequests,
      browserEventCounts: runtime.browserEventCounts || {consoleErrors: runtime.consoleErrors.length, blockedRequests: runtime.blockedRequests.length}
    };
    let imageData;
    if (kind === 'capture') {
      const artifactId = `${crypto.randomUUID()}.png`;
      const pngFile = path.join(evidenceDir, artifactId);
      await fs.writeFile(pngFile, runtime.png, {mode: 0o600});
      const pngSha256 = hashBuffer(runtime.png);
      base.materialErrors = runtime.materialErrors;
      base.capture = {
        dimensions: runtime.dimensions,
        sceneMetadata: runtime.sceneMetadata,
        artifact: artifactRecord(runId, artifactId, 'image/png', runtime.png.length, pngSha256)
      };
      imageData = runtime.png.toString('base64');
    } else {
      base.regression = runtime.regression;
      base.diagnostics = runtime.diagnostics;
      base.failedChecks = runtime.failedChecks;
      base.materialErrors = runtime.materialErrors;
    }
    const reportId = `${crypto.randomUUID()}.json`;
    const reportFile = path.join(evidenceDir, reportId);
    await writeJson(reportFile, base);
    const stat = await fs.stat(reportFile);
    const report = artifactRecord(runId, reportId, 'application/json', stat.size, await hashFile(reportFile));
    return {result: {...base, report}, imageData};
  } catch (error) {
    const safe = error instanceof QaInfrastructureError ? error : new QaInfrastructureError('internal_error', 'QA infrastructure failed');
    const failure = {
      status: 'infrastructure_error',
      operation: kind === 'capture' ? 'qa_capture' : 'qa_regression',
      runId,
      generatedAt: now().toISOString(),
      error: {code: safe.code, message: safe.message},
      source: {repository: CANONICAL_REPOSITORY, exactCommit: PINNED_COMMIT, gamePath: GAME_PATH, gameSha256: GAME_SHA256}
    };
    try {
      const reportId = `${crypto.randomUUID()}.json`;
      const reportFile = path.join(evidenceDir, reportId);
      await writeJson(reportFile, failure);
      const stat = await fs.stat(reportFile);
      failure.report = artifactRecord(runId, reportId, 'application/json', stat.size, await hashFile(reportFile));
    } catch {}
    throw new QaInfrastructureError(safe.code, safe.message, failure);
  } finally {
    await fs.rm(sourceDir, {recursive: true, force: true}).catch(() => {});
  }
}
