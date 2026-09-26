import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {CANONICAL_REPOSITORY, GAME_SHA256, PINNED_COMMIT} from './constants.mjs';
import {materializePinnedSource, requestGitEnvironment, stagePinnedSource, validatePinnedSource} from './pinned-source.mjs';
import {assertCaptureState, classifyCaptureIssues, classifyRegression, runQa, subprocessEnvironment} from './run.mjs';

const stageParent = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-pin-stage-'));
const pinnedSource = await stagePinnedSource(path.join(stageParent, 'source'));

test('classifies real regression and browser failures truthfully', () => {
  assert.equal(classifyRegression({failed: 0}, [], []).status, 'passed');
  const failed = classifyRegression({failed: 2}, [{type: 'pageerror', text: 'boom', url: null}], []);
  assert.equal(failed.status, 'failed');
  assert.equal(failed.failedChecks, 2);
  assert.equal(failed.materialErrors.length, 1);
  assert.equal(classifyRegression({failed: 0}, [], [{url: 'https://example.com/x'}]).status, 'failed');
  assert.throws(() => classifyRegression({failed: '0'}, [], []), /invalid/);
});

test('capture PASS requires zero actual browser errors and blocked requests', () => {
  assert.equal(classifyCaptureIssues([], []).status, 'passed');
  const consoleIssue = {type: 'console', text: 'runtime error', url: null};
  const pageIssue = {type: 'pageerror', text: 'uncaught error', url: null};
  assert.equal(classifyCaptureIssues([consoleIssue], []).status, 'failed');
  assert.equal(classifyCaptureIssues([pageIssue], []).status, 'failed');
  assert.deepEqual(classifyCaptureIssues([pageIssue], []).materialErrors, [pageIssue]);
  assert.equal(classifyCaptureIssues([], [{url: 'https://example.com/untrusted.js'}]).status, 'failed');
  assert.equal(classifyCaptureIssues([], [], {consoleErrors: 33, blockedRequests: 0}).status, 'failed',
    'truncated event evidence cannot conceal actual errors');
  assert.equal(classifyCaptureIssues([], [], {consoleErrors: 0, blockedRequests: 33}).status, 'failed');
});

test('capture checks actual pinned runtime fields, including wrong and missing values', () => {
  const valid = {state: 'play', stage: 3, stateTick: 900, stageTick: 900, frame: 900};
  assert.deepEqual(assertCaptureState(valid), valid);
  assert.equal(assertCaptureState({...valid, bullets: 21}).stageTick, 900);
  const wrong = {state: 'title', stage: 2, stateTick: 899, stageTick: 899, frame: 899};
  for (const field of Object.keys(valid)) {
    assert.throws(() => assertCaptureState({...valid, [field]: wrong[field]}),
      error => error.code === 'capture_state_mismatch' && error.message.includes(field),
      `incorrect ${field} must fail`);
    const missing = {...valid};
    delete missing[field];
    assert.throws(() => assertCaptureState(missing),
      error => error.code === 'capture_state_mismatch' && error.message.includes(field),
      `missing ${field} must fail`);
  }
  assert.throws(() => assertCaptureState(null), error => error.code === 'capture_state_mismatch');
  assert.throws(() => assertCaptureState([]), error => error.code === 'capture_state_mismatch');
});

test('infrastructure failures retain reports in unique evidence-only run directories', async () => {
  const runRoot = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-run-test-'));
  try {
    const ids = [];
    for (let i = 0; i < 2; i += 1) {
      await assert.rejects(
        runQa('capture', {runRoot, pinnedSource: path.join(runRoot, 'missing-prepared-source')}),
        error => {
          assert.equal(error.code, 'pinned_source_missing');
          assert.equal(error.evidence.status, 'infrastructure_error');
          assert.equal(error.evidence.operation, 'qa_capture');
          assert.match(error.evidence.report.sha256, /^[0-9a-f]{64}$/);
          ids.push(error.evidence.runId);
          return true;
        }
      );
    }
    assert.notEqual(ids[0], ids[1]);
    for (const id of ids) {
      const entries = await fs.readdir(path.join(runRoot, id));
      assert.deepEqual(entries, ['evidence']);
    }
  } finally { await fs.rm(runRoot, {recursive: true, force: true}); }
});

test('subprocess environment keeps path and language and drops proxy and bearer values', () => {
  const env = subprocessEnvironment({QA_STATIC_TOKEN: 'run-token'}, {
    PATH: '/usr/bin',
    LANG: 'C.UTF-8',
    HTTPS_PROXY: 'http://127.0.0.1:9',
    HTTP_PROXY: 'http://127.0.0.1:9',
    QA_SERVICE_SECRET: 'must-not-be-copied'
  });
  assert.equal(env.PATH, '/usr/bin');
  assert.equal(env.LANG, 'C.UTF-8');
  assert.equal(env.QA_STATIC_TOKEN, 'run-token');
  assert.equal(env.HTTPS_PROXY, undefined);
  assert.equal(env.HTTP_PROXY, undefined);
  assert.equal(env.QA_SERVICE_SECRET, undefined);
});

test('request git environment cannot fetch and does not carry a proxy or bearer', () => {
  const env = requestGitEnvironment({
    PATH: process.env.PATH,
    HTTPS_PROXY: 'http://127.0.0.1:9',
    QA_SERVICE_SECRET: 'must-not-be-copied'
  });
  assert.equal(env.HTTPS_PROXY, undefined);
  assert.equal(env.QA_SERVICE_SECRET, undefined);
  const remote = spawnSync('git', ['ls-remote', CANONICAL_REPOSITORY, 'HEAD'], {env, encoding: 'utf8'});
  assert.notEqual(remote.status, 0);
});

test('prepared offline source keeps the approved identity and is copied without modification', async () => {
  const validated = await validatePinnedSource(pinnedSource.sourceDir);
  assert.equal(validated.head, PINNED_COMMIT);
  assert.equal(validated.toolRevision, PINNED_COMMIT);
  assert.equal(validated.gameSha256, GAME_SHA256);
  assert.equal(validated.acquisition, 'prepared-offline');
  const before = await fs.readFile(path.join(pinnedSource.sourceDir, 'versions/v4/index.html'));
  const runRoot = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-materialize-'));
  try {
    const runDir = path.join(runRoot, 'run');
    await fs.mkdir(runDir);
    const copy = await materializePinnedSource(runDir, pinnedSource.sourceDir, runRoot);
    assert.equal(copy.head, PINNED_COMMIT);
    assert.equal(copy.acquisition, 'prepared-offline');
    const after = await fs.readFile(path.join(pinnedSource.sourceDir, 'versions/v4/index.html'));
    assert.deepEqual(after, before);
    const status = spawnSync('git', ['status', '--porcelain=v1'], {cwd: pinnedSource.sourceDir, encoding: 'utf8'});
    assert.equal(status.stdout, '');
  } finally { await fs.rm(runRoot, {recursive: true, force: true}); }
});

test('rejects missing, dirty, wrong-commit, and wrong-hash prepared sources', async () => {
  await assert.rejects(validatePinnedSource(path.join(os.tmpdir(), 'scarlet-qa19-absent-pin')), error => error.code === 'pinned_source_missing');
  const dirty = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-dirty-pin-'));
  const wrongCommit = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-wrong-commit-'));
  const wrongHash = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-wrong-hash-'));
  try {
    const dirtyTree = path.join(dirty, 'tree');
    await fs.cp(pinnedSource.sourceDir, dirtyTree, {recursive: true});
    await fs.writeFile(path.join(dirtyTree, 'untracked.txt'), 'dirty\n');
    await assert.rejects(validatePinnedSource(dirtyTree), error => error.code === 'pinned_source_dirty');

    const wrongHashTree = path.join(wrongHash, 'tree');
    await fs.cp(pinnedSource.sourceDir, wrongHashTree, {recursive: true});
    spawnSync('git', ['update-index', '--assume-unchanged', 'versions/v4/index.html'], {cwd: wrongHashTree});
    await fs.appendFile(path.join(wrongHashTree, 'versions/v4/index.html'), '\n');
    await assert.rejects(validatePinnedSource(wrongHashTree), error => error.code === 'game_hash_mismatch');

    const git = (args, cwd) => {
      const result = spawnSync('git', args, {cwd, encoding: 'utf8'});
      assert.equal(result.status, 0, result.stderr);
    };
    git(['init', '--quiet'], wrongCommit);
    git(['config', 'user.email', 'qa19@example.invalid'], wrongCommit);
    git(['config', 'user.name', 'qa19'], wrongCommit);
    await fs.writeFile(path.join(wrongCommit, 'README'), 'not the pin\n');
    git(['add', 'README'], wrongCommit);
    git(['commit', '--quiet', '-m', 'not the pin'], wrongCommit);
    git(['remote', 'add', 'origin', CANONICAL_REPOSITORY], wrongCommit);
    await assert.rejects(validatePinnedSource(wrongCommit), error => error.code === 'pinned_source_wrong_commit');
  } finally {
    await fs.rm(dirty, {recursive: true, force: true});
    await fs.rm(wrongCommit, {recursive: true, force: true});
    await fs.rm(wrongHash, {recursive: true, force: true});
  }
});

test('QA request path does not fetch or stage a remote source', async () => {
  const source = await fs.readFile(new URL('./run.mjs', import.meta.url), 'utf8');
  const server = await fs.readFile(new URL('./server.mjs', import.meta.url), 'utf8');
  assert.doesNotMatch(source, /git fetch|stagePinnedSource|cloneAndValidate/);
  assert.doesNotMatch(server, /git fetch|stagePinnedSource/);
});

test('first-install staging refuses existing, partial, and symlink destinations', async () => {
  const parent = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-stage-refuse-'));
  try {
    const empty = path.join(parent, 'empty');
    await fs.mkdir(empty);
    await assert.rejects(stagePinnedSource(empty), error => error.code === 'stage_destination_exists');
    assert.deepEqual(await fs.readdir(empty), []);

    const partial = path.join(parent, 'partial');
    await fs.mkdir(path.join(partial, '.git'), {recursive: true});
    await fs.writeFile(path.join(partial, '.git', 'scarlet-qa-pin'), 'partial\n');
    await assert.rejects(stagePinnedSource(partial), error => error.code === 'stage_destination_exists');
    assert.equal(await fs.readFile(path.join(partial, '.git', 'scarlet-qa-pin'), 'utf8'), 'partial\n');

    const link = path.join(parent, 'link');
    await fs.symlink(empty, link);
    await assert.rejects(stagePinnedSource(link), error => error.code === 'stage_destination_exists');
    await assert.rejects(stagePinnedSource(pinnedSource.sourceDir), error => error.code === 'stage_destination_exists');
  } finally { await fs.rm(parent, {recursive: true, force: true}); }
});

test('unsuccessful staging publishes nothing and removes only its temporary directory', async () => {
  const parent = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-stage-fail-'));
  const bin = path.join(parent, 'bin');
  await fs.mkdir(bin);
  await fs.writeFile(path.join(bin, 'git'), `#!/bin/sh
for arg in "$@"; do
  if [ "$arg" = "fetch" ]; then exit 44; fi
done
exec /usr/bin/git "$@"
`, {mode: 0o755});
  const destination = path.join(parent, 'source');
  try {
    await assert.rejects(stagePinnedSource(destination, {env: {...process.env, PATH: `${bin}:${process.env.PATH}`}}),
      error => error.code === 'stage_fetch');
    await assert.rejects(fs.lstat(destination), error => error.code === 'ENOENT');
    const leftovers = (await fs.readdir(parent)).filter(name => name.includes('.staging-'));
    assert.deepEqual(leftovers, []);
  } finally { await fs.rm(parent, {recursive: true, force: true}); }
});
