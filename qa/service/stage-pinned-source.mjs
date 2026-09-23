#!/usr/bin/env node
import path from 'node:path';
import {stagePinnedSource} from './pinned-source.mjs';

const destination = path.resolve(process.argv[2] || '');
if (!process.argv[2]) {
  process.stderr.write('usage: node service/stage-pinned-source.mjs <absolute-destination>\n');
  process.exitCode = 2;
} else {
  const prepared = await stagePinnedSource(destination);
  process.stdout.write(`${JSON.stringify({
    destination: prepared.sourceDir,
    commit: prepared.head,
    gameSha256: prepared.gameSha256,
    qaToolRevision: prepared.toolRevision,
    acquisition: prepared.acquisition
  })}\n`);
}
