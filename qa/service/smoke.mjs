#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {Client} from '@modelcontextprotocol/sdk/client/index.js';
import {StreamableHTTPClientTransport} from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import os from 'node:os';
import {CASE_ID, CASE_SCENE, CASE_TICK, GAME_SHA256, LOGICAL_HEIGHT, LOGICAL_WIDTH, PINNED_COMMIT} from './constants.mjs';
import {stagePinnedSource} from './pinned-source.mjs';
import {startQaService} from './server.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const qaRoot = path.resolve(here, '..');
const outputRoot = path.join(qaRoot, 'output');
const runRoot = path.join(outputRoot, 'service-runs');
const summaryFile = path.join(outputRoot, 'service-smoke-summary.json');
const secret = crypto.randomBytes(32).toString('base64url');

function sha256(data) { return crypto.createHash('sha256').update(data).digest('hex'); }
function dimensions(png) {
  if (png.length < 24 || png.toString('ascii', 12, 16) !== 'IHDR') throw new Error('inline capture is not PNG');
  return {width: png.readUInt32BE(16), height: png.readUInt32BE(20)};
}

await fs.mkdir(outputRoot, {recursive: true});
const prepared = await stagePinnedSource(process.env.QA_PINNED_SOURCE || path.join(os.tmpdir(), `scarlet-qa19-pinned-source-${PINNED_COMMIT}`));
process.env.QA_PINNED_SOURCE = prepared.sourceDir;
const service = await startQaService({port: 0, secret, runRoot});
const client = new Client({name: 'qa19-local-smoke', version: '1.0.0'});
const transport = new StreamableHTTPClientTransport(new URL(`http://127.0.0.1:${service.port}/mcp`), {
  requestInit: {headers: {authorization: `Bearer ${secret}`}}
});

try {
  await client.connect(transport);
  const request = {exact_commit: PINNED_COMMIT, case: CASE_ID};
  const capture = await client.callTool({name: 'qa_capture', arguments: request});
  if (capture.isError) throw new Error(`qa_capture infrastructure error: ${capture.content[0]?.text}`);
  const image = capture.content.find(item => item.type === 'image');
  if (!image) throw new Error('qa_capture did not return inline image content');
  const png = Buffer.from(image.data, 'base64');
  const captureMeta = capture.structuredContent;
  const size = dimensions(png);
  if (size.width !== LOGICAL_WIDTH || size.height !== LOGICAL_HEIGHT) throw new Error('capture dimensions mismatch');
  if (sha256(png) !== captureMeta.capture.artifact.sha256) throw new Error('inline PNG hash mismatch');
  if (captureMeta.source.exactCommit !== PINNED_COMMIT || captureMeta.source.gameSha256 !== GAME_SHA256 || captureMeta.source.qaToolRevision !== PINNED_COMMIT || captureMeta.source.acquisition !== 'prepared-offline') throw new Error('capture source identity mismatch');
  if (captureMeta.request.scene !== CASE_SCENE || captureMeta.request.tick !== CASE_TICK || captureMeta.capture.sceneMetadata.stage !== 3) throw new Error('capture scene metadata mismatch');

  const artifactUrl = new URL(captureMeta.capture.artifact.endpoint, `http://127.0.0.1:${service.port}`);
  const artifactResponse = await fetch(artifactUrl, {headers: {authorization: `Bearer ${secret}`}});
  if (!artifactResponse.ok) throw new Error('authenticated artifact read failed');
  const artifactPng = Buffer.from(await artifactResponse.arrayBuffer());
  if (sha256(artifactPng) !== captureMeta.capture.artifact.sha256) throw new Error('artifact PNG hash mismatch');

  const regression = await client.callTool({name: 'qa_regression', arguments: request});
  if (regression.isError) throw new Error(`qa_regression infrastructure error: ${regression.content[0]?.text}`);
  const regressionMeta = regression.structuredContent;
  if (regressionMeta.source.acquisition !== 'prepared-offline' || regressionMeta.source.exactCommit !== PINNED_COMMIT) throw new Error('regression source identity mismatch');
  const summary = {
    completedAt: new Date().toISOString(),
    protocol: 'MCP Streamable HTTP',
    localOnly: true,
    capture: {
      status: captureMeta.status,
      runId: captureMeta.runId,
      source: captureMeta.source,
      browser: captureMeta.runtime.browser,
      dimensions: size,
      pngSha256: captureMeta.capture.artifact.sha256,
      reportSha256: captureMeta.report.sha256,
      request: captureMeta.request,
      sceneMetadata: captureMeta.capture.sceneMetadata,
      serviceRevision: captureMeta.runtime.serviceRevision,
      acquisition: captureMeta.source.acquisition,
      consoleErrors: captureMeta.consoleErrors,
      blockedRequests: captureMeta.blockedRequests
    },
    regression: {
      status: regressionMeta.status,
      runId: regressionMeta.runId,
      source: regressionMeta.source,
      browser: regressionMeta.runtime.browser,
      passed: regressionMeta.regression.passed,
      failed: regressionMeta.regression.failed,
      errors: regressionMeta.regression.errors,
      consoleErrors: regressionMeta.consoleErrors,
      blockedRequests: regressionMeta.blockedRequests,
      reportSha256: regressionMeta.report.sha256
    }
  };
  await fs.writeFile(summaryFile, `${JSON.stringify(summary, null, 2)}\n`, {mode: 0o600});
  process.stdout.write(`${JSON.stringify({summaryFile, ...summary}, null, 2)}\n`);
  if (captureMeta.status !== 'passed' || regressionMeta.status !== 'passed') process.exitCode = 2;
} finally {
  await transport.close().catch(() => {});
  await service.close();
}
