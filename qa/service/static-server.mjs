#!/usr/bin/env node
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const file = process.env.QA_STATIC_FILE;
const token = process.env.QA_STATIC_TOKEN;
const port = Number(process.env.QA_STATIC_PORT || '0');

if (!file || !path.isAbsolute(file) || !token || token.length < 32 || !Number.isInteger(port) || port < 0 || port > 65535) {
  process.exitCode = 1;
  throw new Error('invalid isolated static server configuration');
}

const expected = Buffer.from(`Bearer ${token}`);
function authorized(req) {
  const supplied = Buffer.from(String(req.headers.authorization || ''));
  return supplied.length === expected.length && crypto.timingSafeEqual(supplied, expected);
}

const server = http.createServer((req, res) => {
  if (!authorized(req)) {
    res.writeHead(401, {'content-type': 'text/plain', 'cache-control': 'no-store'}).end('unauthorized');
    return;
  }
  let url;
  try {
    url = new URL(req.url, 'http://127.0.0.1');
  } catch {
    res.writeHead(400, {'content-type': 'text/plain'}).end('bad request');
    return;
  }
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    res.writeHead(405, {'allow': 'GET, HEAD'}).end();
    return;
  }
  if (/^\/(favicon\.ico|apple-touch-icon[^/]*)$/i.test(url.pathname)) {
    res.writeHead(204, {'cache-control': 'no-store'}).end();
    return;
  }
  if (url.pathname !== '/' && url.pathname !== '/generated.html') {
    res.writeHead(404, {'content-type': 'text/plain', 'cache-control': 'no-store'}).end('not found');
    return;
  }
  fs.readFile(file, (error, data) => {
    if (error) {
      res.writeHead(500, {'content-type': 'text/plain', 'cache-control': 'no-store'}).end('unavailable');
      return;
    }
    res.writeHead(200, {
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'no-store',
      'content-security-policy': "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; media-src data:; connect-src 'none'",
      'x-content-type-options': 'nosniff',
      'referrer-policy': 'no-referrer'
    });
    res.end(req.method === 'HEAD' ? undefined : data);
  });
});

server.on('clientError', (_error, socket) => socket.end('HTTP/1.1 400 Bad Request\r\nConnection: close\r\n\r\n'));
server.listen(port, '127.0.0.1', () => {
  const address = server.address();
  process.stdout.write(`${JSON.stringify({port: address.port})}\n`);
});

for (const signal of ['SIGTERM', 'SIGINT']) {
  process.on(signal, () => server.close(() => process.exit(0)));
}
