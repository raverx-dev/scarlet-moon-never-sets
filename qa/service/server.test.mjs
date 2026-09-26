import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import http from 'node:http';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import {Client} from '@modelcontextprotocol/sdk/client/index.js';
import {StreamableHTTPClientTransport} from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import {PINNED_COMMIT} from './constants.mjs';
import {createSerializedExecutor, loadServiceSecret, startQaService} from './server.mjs';

const secret = crypto.randomBytes(32).toString('base64url');

async function fixture(executor) {
  const runRoot = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-service-test-'));
  const service = await startQaService({port: 0, secret, runRoot, executor});
  const url = new URL(`http://127.0.0.1:${service.port}/mcp`);
  const client = new Client({name: 'qa19-test', version: '1.0.0'});
  const transport = new StreamableHTTPClientTransport(url, {requestInit: {headers: {authorization: `Bearer ${secret}`}}});
  await client.connect(transport);
  return {
    service, client, transport, runRoot, url,
    async close() {
      await transport.close().catch(() => {});
      await service.close();
      await fs.rm(runRoot, {recursive: true, force: true});
    }
  };
}

test('exposes exactly the two bounded tools and accepts the pinned optional inputs', async () => {
  const calls = [];
  const f = await fixture(async kind => {
    calls.push(kind);
    return {result: {status: kind === 'regression' ? 'failed' : 'passed', operation: `qa_${kind}`}, imageData: kind === 'capture' ? Buffer.from('png').toString('base64') : undefined};
  });
  try {
    const tools = await f.client.listTools();
    assert.deepEqual(tools.tools.map(tool => tool.name).sort(), ['qa_capture', 'qa_regression']);
    const capture = await f.client.callTool({name: 'qa_capture', arguments: {exact_commit: PINNED_COMMIT, case: 'stage3-interior'}});
    assert.equal(capture.isError, undefined);
    assert.equal(capture.structuredContent.status, 'passed');
    assert.equal(capture.content[1].type, 'image');
    const regression = await f.client.callTool({name: 'qa_regression', arguments: {}});
    assert.equal(regression.isError, undefined, 'real regression failure is not an infrastructure error');
    assert.equal(regression.structuredContent.status, 'failed');
    assert.deepEqual(calls, ['capture', 'regression']);
  } finally { await f.close(); }
});

test('rejects wrong commit, wrong case, and extra path/url/js/shell inputs before execution', async () => {
  let calls = 0;
  const f = await fixture(async () => { calls += 1; return {result: {status: 'passed'}}; });
  try {
    const invalid = [
      {exact_commit: 'main'},
      {case: 'stage3-roof'},
      {path: 'versions/v4/index.html'},
      {url: 'https://example.com'},
      {js: 'return document.body'},
      {shell: 'id'},
      {pinnedSource: '/tmp/not-accepted-from-the-caller'}
    ];
    for (const args of invalid) {
      const result = await f.client.callTool({name: 'qa_capture', arguments: args});
      assert.equal(result.isError, true, JSON.stringify(args));
    }
    assert.equal(calls, 0);
  } finally { await f.close(); }
});

test('requires auth for MCP discovery/calls and artifact reads, and limits request bodies', async () => {
  const f = await fixture(async () => ({result: {status: 'passed'}}));
  try {
    const noAuthGet = await fetch(f.url);
    assert.equal(noAuthGet.status, 401);
    const noAuthPost = await fetch(f.url, {method: 'POST', headers: {'content-type': 'application/json'}, body: '{}'});
    assert.equal(noAuthPost.status, 401);

    const runId = crypto.randomUUID();
    const artifactId = `${crypto.randomUUID()}.json`;
    const evidence = path.join(f.runRoot, runId, 'evidence');
    await fs.mkdir(evidence, {recursive: true});
    await fs.writeFile(path.join(evidence, artifactId), '{"ok":true}\n');
    const artifactUrl = `http://127.0.0.1:${f.service.port}/artifacts/${runId}/${artifactId}`;
    assert.equal((await fetch(artifactUrl)).status, 401);
    const artifact = await fetch(artifactUrl, {headers: {authorization: `Bearer ${secret}`}});
    assert.equal(artifact.status, 200);
    assert.deepEqual(await artifact.json(), {ok: true});
    assert.equal((await fetch(`http://127.0.0.1:${f.service.port}/artifacts/../../etc/passwd`, {headers: {authorization: `Bearer ${secret}`}})).status, 404);

    const tooLarge = await fetch(f.url, {
      method: 'POST',
      headers: {authorization: `Bearer ${secret}`, 'content-type': 'application/json'},
      body: JSON.stringify({padding: 'x'.repeat(70 * 1024)})
    });
    assert.equal(tooLarge.status, 413);
  } finally { await f.close(); }
});

test('marks infrastructure failures as MCP errors with safe structured JSON', async () => {
  const f = await fixture(async () => { throw new Error('sensitive internal detail'); });
  try {
    const result = await f.client.callTool({name: 'qa_regression', arguments: {}});
    assert.equal(result.isError, true);
    assert.equal(result.structuredContent.status, 'infrastructure_error');
    assert.equal(result.structuredContent.error.code, 'internal_error');
    assert.doesNotMatch(result.content[0].text, /sensitive internal detail/);
  } finally { await f.close(); }
});

test('serialized executor never overlaps requests', async () => {
  let active = 0;
  let maximum = 0;
  const order = [];
  const execute = createSerializedExecutor(async value => {
    active += 1;
    maximum = Math.max(maximum, active);
    order.push(`start-${value}`);
    await new Promise(resolve => setTimeout(resolve, 20));
    order.push(`end-${value}`);
    active -= 1;
    return value;
  });
  assert.deepEqual(await Promise.all([execute(1), execute(2), execute(3)]), [1, 2, 3]);
  assert.equal(maximum, 1);
  assert.deepEqual(order, ['start-1', 'end-1', 'start-2', 'end-2', 'start-3', 'end-3']);
});

test('fails closed for weak secrets and non-loopback binding', async () => {
  const runRoot = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-config-test-'));
  try {
    await assert.rejects(startQaService({port: 0, host: '0.0.0.0', secret, runRoot}), /refuses non-loopback/);
    await assert.rejects(startQaService({port: 0, secret: 'weak', runRoot}), /strong secret/);
    await assert.rejects(startQaService({port: 0, secret, runRoot: path.parse(runRoot).root}), /dedicated child/);
  } finally { await fs.rm(runRoot, {recursive: true, force: true}); }
});

function requestStatus(port, headers) {
  return new Promise((resolve, reject) => {
    const req = http.request({hostname: '127.0.0.1', port, path: '/mcp', method: 'GET', headers}, res => {
      res.resume();
      resolve(res.statusCode);
    });
    req.on('error', reject);
    req.end();
  });
}

test('credential file overrides the environment and host validation stays strict', async () => {
  const runRoot = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-credential-'));
  const credentialsDirectory = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-cred-dir-'));
  const fileSecret = crypto.randomBytes(32).toString('base64url');
  const environmentSecret = crypto.randomBytes(32).toString('base64url');
  await fs.writeFile(path.join(credentialsDirectory, 'qa-secret'), fileSecret, {mode: 0o400});
  const service = await startQaService({
    port: 0,
    runRoot,
    credentialsDirectory,
    environmentSecret
  });
  try {
    assert.equal(await requestStatus(service.port, {host: `127.0.0.1:${service.port}`}), 401);
    assert.equal(await requestStatus(service.port, {host: 'evil.example', authorization: `Bearer ${fileSecret}`}), 421);
    assert.equal(await requestStatus(service.port, {host: `127.0.0.1:${service.port}`, authorization: `Bearer ${environmentSecret}`}), 401);
    const accepted = await requestStatus(service.port, {host: `127.0.0.1:${service.port}`, authorization: `Bearer ${fileSecret}`});
    assert.notEqual(accepted, 401);
    assert.notEqual(accepted, 421);
  } finally {
    await service.close();
    await fs.rm(runRoot, {recursive: true, force: true});
    await fs.rm(credentialsDirectory, {recursive: true, force: true});
  }
});

test('credential loading fails closed for a missing, invalid, or linked credential', async () => {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-cred-fail-'));
  const environmentSecret = crypto.randomBytes(32).toString('base64url');
  try {
    await assert.rejects(
      async () => loadServiceSecret({credentialsDirectory: directory, environmentSecret}),
      /credential file is missing/
    );
    await fs.writeFile(path.join(directory, 'qa-secret'), 'weak-secret-value-should-not-leak\n');
    await assert.rejects(
      async () => loadServiceSecret({credentialsDirectory: directory, environmentSecret}),
      error => error.message.includes('strong secret') && !error.message.includes('weak-secret-value-should-not-leak')
    );
    await fs.rm(path.join(directory, 'qa-secret'));
    await fs.symlink('/etc/hostname', path.join(directory, 'qa-secret'));
    await assert.rejects(
      async () => loadServiceSecret({credentialsDirectory: directory, environmentSecret}),
      /regular file/
    );
  } finally { await fs.rm(directory, {recursive: true, force: true}); }
});
