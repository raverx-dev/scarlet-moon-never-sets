#!/usr/bin/env node
import http from 'node:http';
import fs from 'node:fs/promises';
import fsSync from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {McpServer} from '@modelcontextprotocol/sdk/server/mcp.js';
import {StreamableHTTPServerTransport} from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import * as z from 'zod/v4';
import {CASE_ID, DEFAULT_PORT, MAX_REQUEST_BYTES, PINNED_COMMIT, RUN_TIMEOUT_MS} from './constants.mjs';
import {QaInfrastructureError, runQa} from './run.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));

function validateSecret(secret) {
  if (typeof secret !== 'string' || Buffer.byteLength(secret) < 32 || secret.trim() !== secret || new Set(secret).size < 16) {
    throw new Error('QA_SERVICE_SECRET must be a strong secret of at least 32 bytes');
  }
  return secret;
}

const CREDENTIAL_NAME = 'qa-secret';

export function loadServiceSecret({
  explicitSecret,
  credentialsDirectory,
  environmentSecret
} = {}) {
  if (explicitSecret !== undefined) return validateSecret(explicitSecret);
  const directory = credentialsDirectory === undefined ? process.env.CREDENTIALS_DIRECTORY : credentialsDirectory;
  const fromEnvironment = environmentSecret === undefined ? process.env.QA_SERVICE_SECRET : environmentSecret;
  if (directory) return readCredentialFile(directory);
  return validateSecret(fromEnvironment);
}

function readCredentialFile(directory) {
  if (!path.isAbsolute(directory)) throw new Error('CREDENTIALS_DIRECTORY must be absolute');
  const root = path.resolve(directory);
  const file = path.join(root, CREDENTIAL_NAME);
  let info;
  try { info = fsSync.lstatSync(file); }
  catch { throw new Error('QA service credential file is missing'); }
  if (!info.isFile() || info.isSymbolicLink() || info.size > 4096) {
    throw new Error('QA service credential file must be a regular file');
  }
  const value = fsSync.readFileSync(file, 'utf8');
  return validateSecret(value);
}

function bearerMatches(header, secret) {
  const supplied = Buffer.from(String(header || ''));
  const expected = Buffer.from(`Bearer ${secret}`);
  return supplied.length === expected.length && crypto.timingSafeEqual(supplied, expected);
}

function json(res, status, body, headers = {}) {
  const data = Buffer.from(JSON.stringify(body));
  res.writeHead(status, {'content-type': 'application/json; charset=utf-8', 'content-length': data.length, 'cache-control': 'no-store', ...headers});
  res.end(data);
}

function readJson(req) {
  return new Promise((resolve, reject) => {
    let total = 0;
    const chunks = [];
    let tooLarge = false;
    req.on('data', chunk => {
      total += chunk.length;
      if (total > MAX_REQUEST_BYTES) {
        tooLarge = true;
        chunks.length = 0;
      } else if (!tooLarge) chunks.push(chunk);
    });
    req.on('end', () => {
      if (tooLarge) {
        reject(Object.assign(new Error('request too large'), {status: 413}));
        return;
      }
      try { resolve(JSON.parse(Buffer.concat(chunks).toString('utf8'))); }
      catch { reject(Object.assign(new Error('invalid JSON'), {status: 400})); }
    });
    req.on('error', () => reject(Object.assign(new Error('request read failed'), {status: 400})));
  });
}

export function createSerializedExecutor(executor) {
  let tail = Promise.resolve();
  return (...args) => {
    const current = tail.then(() => executor(...args), () => executor(...args));
    tail = current.catch(() => {});
    return current;
  };
}

function formatSuccess(outcome) {
  const content = [{type: 'text', text: JSON.stringify(outcome.result, null, 2)}];
  if (outcome.imageData) content.push({type: 'image', data: outcome.imageData, mimeType: 'image/png'});
  return {content, structuredContent: outcome.result};
}

function formatInfrastructureFailure(error) {
  const result = error instanceof QaInfrastructureError && error.evidence?.status
    ? error.evidence
    : {status: 'infrastructure_error', error: {code: 'internal_error', message: 'QA infrastructure failed'}};
  return {content: [{type: 'text', text: JSON.stringify(result, null, 2)}], structuredContent: result, isError: true};
}

function createMcpServer(execute) {
  const server = new McpServer({name: 'scarlet-moon-local-qa', version: '0.1.0'});
  const inputSchema = z.object({
    exact_commit: z.literal(PINNED_COMMIT).optional(),
    case: z.literal(CASE_ID).optional()
  }).strict();
  server.registerTool('qa_capture', {
    description: 'Capture the pinned stage3-interior frozen frame from the exact local-only QA source.',
    inputSchema
  }, async () => {
    try { return formatSuccess(await execute('capture')); }
    catch (error) { return formatInfrastructureFailure(error); }
  });
  server.registerTool('qa_regression', {
    description: 'Run the pinned recovered regressions and acceptance diagnostics in an isolated browser.',
    inputSchema
  }, async () => {
    try { return formatSuccess(await execute('regression')); }
    catch (error) { return formatInfrastructureFailure(error); }
  });
  return server;
}

function safeArtifactPath(runRoot, pathname) {
  const match = pathname.match(/^\/artifacts\/([0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})\/([0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\.(?:png|json))$/i);
  if (!match) return null;
  return {file: path.join(runRoot, match[1], 'evidence', match[2]), mediaType: match[2].endsWith('.png') ? 'image/png' : 'application/json'};
}

export async function startQaService({
  host = process.env.QA_SERVICE_HOST || '127.0.0.1',
  port = Number(process.env.QA_SERVICE_PORT || DEFAULT_PORT),
  secret,
  credentialsDirectory,
  environmentSecret,
  runRoot = process.env.QA_SERVICE_RUN_ROOT,
  executor
} = {}) {
  if (host !== '127.0.0.1') throw new Error('QA service refuses non-loopback binding');
  if (!Number.isInteger(port) || port < 0 || port > 65535) throw new Error('QA_SERVICE_PORT is invalid');
  secret = loadServiceSecret({explicitSecret: secret, credentialsDirectory, environmentSecret});
  if (!runRoot || !path.isAbsolute(runRoot)) throw new Error('QA_SERVICE_RUN_ROOT must be an absolute path');
  await fs.mkdir(runRoot, {recursive: true, mode: 0o700});
  const runRootReal = await fs.realpath(runRoot);
  if (runRootReal === path.parse(runRootReal).root) throw new Error('QA_SERVICE_RUN_ROOT must be a dedicated child directory');
  const execute = createSerializedExecutor(executor || (kind => runQa(kind, {runRoot: runRootReal})));

  const server = http.createServer(async (req, res) => {
    try {
      const address = server.address();
      const expectedHost = `127.0.0.1:${address.port}`;
      if (req.headers.host !== expectedHost) {
        json(res, 421, {error: 'misdirected request'});
        return;
      }
      if (!bearerMatches(req.headers.authorization, secret)) {
        json(res, 401, {error: 'unauthorized'}, {'www-authenticate': 'Bearer'});
        return;
      }
      const url = new URL(req.url, `http://${expectedHost}`);
      if (url.pathname === '/mcp') {
        if (req.method !== 'POST') {
          json(res, 405, {error: 'method not allowed'}, {allow: 'POST'});
          return;
        }
        if (!String(req.headers['content-type'] || '').toLowerCase().startsWith('application/json')) {
          json(res, 415, {error: 'unsupported media type'});
          return;
        }
        const contentLength = Number(req.headers['content-length'] || '0');
        if (!Number.isFinite(contentLength) || contentLength < 0 || contentLength > MAX_REQUEST_BYTES) {
          json(res, 413, {error: 'request too large'});
          return;
        }
        const body = await readJson(req);
        const mcp = createMcpServer(execute);
        const transport = new StreamableHTTPServerTransport({sessionIdGenerator: undefined, enableJsonResponse: true});
        await mcp.connect(transport);
        res.on('close', () => { transport.close().catch(() => {}); mcp.close().catch(() => {}); });
        await transport.handleRequest(req, res, body);
        return;
      }
      if (req.method === 'GET') {
        const artifact = safeArtifactPath(runRootReal, url.pathname);
        if (artifact) {
          let real;
          try { real = await fs.realpath(artifact.file); }
          catch { json(res, 404, {error: 'not found'}); return; }
          if (real !== artifact.file || !real.startsWith(`${runRootReal}${path.sep}`)) { json(res, 404, {error: 'not found'}); return; }
          const data = await fs.readFile(real);
          res.writeHead(200, {'content-type': artifact.mediaType, 'content-length': data.length, 'cache-control': 'no-store', 'x-content-type-options': 'nosniff'});
          res.end(data);
          return;
        }
      }
      json(res, 404, {error: 'not found'});
    } catch (error) {
      if (!res.headersSent) json(res, error?.status || 500, {error: error?.status ? error.message : 'internal server error'});
      else res.destroy();
    }
  });
  server.requestTimeout = RUN_TIMEOUT_MS + 10_000;
  server.headersTimeout = 10_000;
  server.maxHeadersCount = 64;
  await new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(port, host, resolve);
  });
  return {
    server,
    host,
    port: server.address().port,
    close: () => new Promise((resolve, reject) => server.close(error => error ? reject(error) : resolve()))
  };
}

const invoked = process.argv[1] && path.resolve(process.argv[1]) === path.join(here, 'server.mjs');
if (invoked) {
  startQaService().then(service => {
    process.stdout.write(`${JSON.stringify({host: service.host, port: service.port, protocol: 'mcp-streamable-http', localOnly: true})}\n`);
    const stop = () => service.close().finally(() => process.exit(0));
    process.on('SIGTERM', stop);
    process.on('SIGINT', stop);
  }).catch(error => {
    process.stderr.write(`QA service failed to start: ${error.message}\n`);
    process.exit(1);
  });
}
