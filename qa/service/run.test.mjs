import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {classifyRegression, runQa} from './run.mjs';

test('classifies real regression and browser failures truthfully', () => {
  assert.equal(classifyRegression({failed: 0}, [], []).status, 'passed');
  const failed = classifyRegression({failed: 2}, [{type: 'pageerror', text: 'boom', url: null}], []);
  assert.equal(failed.status, 'failed');
  assert.equal(failed.failedChecks, 2);
  assert.equal(failed.materialErrors.length, 1);
  assert.equal(classifyRegression({failed: 0}, [], [{url: 'https://example.com/x'}]).status, 'failed');
  assert.throws(() => classifyRegression({failed: '0'}, [], []), /invalid/);
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
