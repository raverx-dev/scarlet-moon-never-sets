#!/usr/bin/env node
/**
 * Compare the running V4 game's undecorated mansion backgrounds to the
 * accepted proof PNGs. Scene shots are optional and are not a pixel pass.
 *
 *   node dev/v4_mansion_runtime/verify_runtime_pixels.mjs --shots DIR
 *   node dev/v4_mansion_runtime/verify_runtime_pixels.mjs --pixels
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import {spawn, spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {chromium} from '../../qa/node_modules/playwright-core/index.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../..');
const registered = '/home/dellis/Projects/scarlet-moon-never-sets';
if (root === registered) {
  console.error('refusing to verify inside the registered Scarlet root');
  process.exit(1);
}
const qa = path.join(root, 'qa');
const receiptPath = path.join(here, 'generation_receipt.json');
const args = process.argv.slice(2);
const wantPixels = args.includes('--pixels');
const shotAt = args.indexOf('--shots');
const shotDir = shotAt >= 0 ? path.resolve(args[shotAt + 1]) : null;
const SHOTS = [
  'stage3-interior',
  'sakuya-dialogue',
  's1',
  's2-frozen',
  'gate',
  'stage3-roof',
  'remilia-dialogue',
  'r5-final',
];

function which(cmd) {
  const r = spawnSync('which', [cmd], {encoding: 'utf8'});
  return r.status === 0 ? r.stdout.trim().split(/\r?\n/)[0] : null;
}
function resolveBrowser(p) {
  if (!p || !fs.existsSync(p)) return null;
  const real = fs.realpathSync(p);
  if (real.endsWith('.sh')) {
    const elf = real.slice(0, -3);
    if (fs.existsSync(elf)) return elf;
  }
  return real;
}
function browserBin() {
  const candidates = [
    process.env.BROWSER_BIN,
    '/usr/lib64/chromium-browser/chromium-browser',
    '/usr/bin/chromium-browser',
    '/usr/bin/chromium',
    '/usr/bin/google-chrome',
    which('chromium-browser'),
    which('chromium'),
    which('google-chrome'),
  ];
  for (const candidate of candidates) {
    const resolved = resolveBrowser(candidate);
    if (resolved) return resolved;
  }
  return null;
}

function packEval() {
  return `function pack(w,h){
    const im=ctx.getImageData(0,0,w,h),d=im.data,out=new Uint8Array(w*h*3);
    for(let i=0,j=0;i<d.length;i+=4,j+=3){
      if(d[i+3]!==255) throw Error('background alpha '+d[i+3]);
      out[j]=d[i];out[j+1]=d[i+1];out[j+2]=d[i+2];
    }
    let s='';
    for(let i=0;i<out.length;i+=4096)s+=String.fromCharCode.apply(null,out.subarray(i,Math.min(i+4096,out.length)));
    return btoa(s);
  }`;
}

const built = spawnSync('python3', ['build.py'], {
  cwd: qa,
  env: {...process.env, SCARLET_QA_SOURCE: 'versions/v4/index.html'},
  encoding: 'utf8',
});
if (built.status !== 0) {
  console.error(built.stdout, built.stderr);
  process.exit(1);
}
const exe = browserBin();
if (!exe) {
  console.error('BLOCKED: no Chromium-family browser for runtime pixel QA');
  process.exit(1);
}
const server = spawn(process.execPath, ['server.cjs'], {cwd: qa, stdio: ['ignore', 'pipe', 'pipe']});
let serverLog = '';
server.stdout.on('data', d => { serverLog += d; });
server.stderr.on('data', d => { serverLog += d; });

async function waitForServer() {
  for (let i = 0; i < 50; i++) {
    try {
      const response = await fetch('http://127.0.0.1:4173/');
      if (response.ok) return;
    } catch {}
    await new Promise(r => setTimeout(r, 100));
  }
  throw new Error('QA server did not become ready: ' + serverLog);
}

const report = {browser: exe, pixels: null, shots: [], errors: []};
let browser;
try {
  await waitForServer();
  browser = await chromium.launch({headless: true, executablePath: exe});
  const page = await browser.newPage({viewport: {width: 1100, height: 760}});
  const pageErrors = [];
  page.on('pageerror', e => pageErrors.push(String(e)));
  await page.goto('http://127.0.0.1:4173/', {waitUntil: 'load'});
  await page.waitForSelector('#audit-scene');
  if (pageErrors.length) throw new Error(pageErrors.join('\n'));

  if (wantPixels) {
    const receipt = JSON.parse(fs.readFileSync(receiptPath, 'utf8'));
    const measured = await page.evaluate(new Function(`${packEval()}
      const ctx=document.getElementById('game').getContext('2d',{alpha:false});
      function clear(){ctx.fillStyle='#080810';ctx.fillRect(0,0,256,240)}
      clear(); drawInterior(0,192,0); const gameplay=pack(192,240);
      clear(); drawInterior(0,256,0); const story=pack(256,240);
      clear(); state='dialogue'; boss=null; stage=3; sakuyaDone=false;
      background(3,0,256,''); const dialogueBg=pack(256,240);
      clear(); state='play'; boss=null; sakuyaDone=false; stage=3;
      background(3,0,192,''); const stageBg=pack(192,240);
      clear(); state='play'; boss={who:'sakuya',data:{id:'s1',duration:100},t:10}; sakuyaDone=false;
      background(3,0,192,''); const sakuyaDim=pack(192,240);
      clear(); state='play'; boss={who:'remilia',data:{id:'r1',duration:100},t:0}; sakuyaDone=false;
      background(3,0,192,''); const remilia=pack(192,240);
      clear(); state='play'; boss=null;
      background(3,0,256,'roof'); const roof=pack(256,240);
      stage=3; boss=null; sakuyaDone=false;
      showDialogue('sakuya_before',()=>{}); dialogue.print=999; draw();
      const sakuyaTop=pack(256,40);
      return {gameplay,story,dialogueBg,stageBg,sakuyaDim,remilia,roof,sakuyaTop};
    `));
    const hashes = {};
    for (const [name, b64] of Object.entries(measured)) hashes[name] = crypto.createHash('sha256').update(Buffer.from(b64, 'base64')).digest('hex');
    const gameplay = receipt.scenes.gameplay.rgb_sha256;
    const story = receipt.scenes.story.rgb_sha256;
    const storyTop = crypto.createHash('sha256').update(Buffer.from(measured.story, 'base64').subarray(0, 256 * 40 * 3)).digest('hex');
    const checks = {
      drawInterior_gameplay_192: hashes.gameplay === gameplay,
      drawInterior_story_256: hashes.story === story,
      stage3_play_background_is_gameplay: hashes.stageBg === gameplay,
      sakuya_dialogue_background_is_story: hashes.dialogueBg === story,
      sakuya_draw_top_rows_are_story: hashes.sakuyaTop === storyTop,
      sakuya_boss_dim_changes_pixels: hashes.sakuyaDim !== gameplay,
      remilia_play_is_not_mansion_gameplay: hashes.remilia !== gameplay,
      roof_mode_is_not_mansion_story: hashes.roof !== story,
    };
    report.pixels = {hashes, expected: {gameplay, story, storyTop}, checks};
    const failed = Object.entries(checks).filter(([, ok]) => !ok).map(([name]) => name);
    if (failed.length) {
      report.errors.push('pixel checks failed: ' + failed.join(', '));
    }
  }

  if (shotDir) {
    fs.mkdirSync(shotDir, {recursive: true});
    const cases = JSON.parse(fs.readFileSync(path.join(qa, 'cases.json'), 'utf8'));
    for (const id of SHOTS) {
      const item = cases.find(c => c.id === id);
      if (!item) throw new Error('missing case ' + id);
      await page.selectOption('#audit-scene', item.scene);
      await page.fill('#audit-tick', String(item.tick));
      await page.locator('#audit-jump').click();
      await page.waitForTimeout(40);
      const dataUrl = await page.evaluate(() => document.getElementById('game').toDataURL('image/png'));
      const png = Buffer.from(dataUrl.split(',', 2)[1], 'base64');
      const file = path.join(shotDir, `${id}.png`);
      fs.writeFileSync(file, png);
      report.shots.push({id, scene: item.scene, tick: item.tick, bytes: png.length, sha256: crypto.createHash('sha256').update(png).digest('hex')});
    }
    const bare = await page.evaluate(() => {
      const ctx = document.getElementById('game').getContext('2d', {alpha: false});
      ctx.fillStyle = '#080810';
      ctx.fillRect(0, 0, 256, 240);
      drawInterior(0, 192, 0);
      const gameplay = document.getElementById('game').toDataURL('image/png');
      ctx.fillStyle = '#080810';
      ctx.fillRect(0, 0, 256, 240);
      drawInterior(0, 256, 0);
      const story = document.getElementById('game').toDataURL('image/png');
      return {gameplay, story};
    });
    for (const [name, url] of Object.entries(bare)) {
      const png = Buffer.from(url.split(',', 2)[1], 'base64');
      fs.writeFileSync(path.join(shotDir, `undecorated-${name}.png`), png);
      report.shots.push({id: `undecorated-${name}`, bytes: png.length, sha256: crypto.createHash('sha256').update(png).digest('hex')});
    }
  }
} catch (error) {
  report.errors.push(String(error && error.stack || error));
} finally {
  if (browser) await browser.close();
  server.kill('SIGTERM');
}

const out = path.join(here, shotDir && !wantPixels ? 'review-shots.json' : 'runtime_pixel_report.json');
fs.writeFileSync(out, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({out, errors: report.errors, pixels: report.pixels && report.pixels.checks, shots: report.shots.map(s => s.id)}, null, 2));
if (report.errors.length) process.exit(1);
