#!/usr/bin/env node
// No worker, browser, or network needed: verify the exact delivered art embedded in V4.
import fs from 'node:fs';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import vm from 'node:vm';
const file=new URL('../versions/v4/index.html',import.meta.url);
const artifact=new URL('../versions/v4/assets/v4-can-cigarette-splash-logo-01.scarlet-moon.json',import.meta.url);
const src=fs.readFileSync(file,'utf8'),bytes=fs.readFileSync(artifact);
const expected='f7b5f92c858b2b54873b3e2296170bb6be9265b93e550bce4b41a29b5a1dfea7';
assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),expected,'delivered artifact hash');
const data=JSON.parse(bytes.toString('utf8'));
assert.equal(data.width,64);assert.equal(data.height,64);assert.equal(data.rows.length,64);
assert.equal(data.symbols['.'].transparent,true);
assert.equal(data.rows.flatMap(row=>[...row]).filter(c=>c==='.').length,2351,'transparent cells');
for(const row of data.rows){assert.equal(row.length,64);for(const key of row){
 const symbol=data.symbols[key];assert.ok(symbol,'undeclared export symbol '+key);
 assert.ok(symbol.transparent===true||/^#[0-9a-fA-F]{6}$/.test(symbol.hex),'invalid exported RGB');}}
const match=src.match(/const V4_CAN_EXPORT=([^\n]+);/);
assert.ok(match,'embedded export absent');assert.deepEqual(JSON.parse(match[1]),data,'embedded matrix differs from delivered file');
assert.ok(src.includes("drawV4CanLogo(96,45)"),'boot must render approved art');
assert.ok(src.includes("center('RAVER X DEV',121"),'boot developer mark');
assert.ok(!src.includes('EMPTY BOX SOFT'),'fictional developer still present in V4');
const script=src.match(/<script>([\s\S]*?)<\/script>/);assert.ok(script,'game script');
new vm.Script(script[1],{filename:'versions/v4/index.html'});
console.log('PASS: exact delivered 64x64 artwork, transparency, V4 boot/credits branding and JS syntax');
