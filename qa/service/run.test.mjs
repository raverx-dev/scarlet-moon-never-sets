import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {assertCaptureState, classifyCaptureIssues, classifyRegression, runQa} from './run.mjs';

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
        runQa('capture', {runRoot, repository: '/definitely-not-an-authorized-remote'}),
        error => {
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
