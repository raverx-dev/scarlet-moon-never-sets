#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn, spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {chromium} from 'playwright-core';

const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'..');
const sourceHtml=path.resolve(process.env.QA_SOURCE||path.join(root,'index.html'));
const casesFile=path.resolve(process.env.QA_CASES||path.join(here,'cases.json'));
const out=path.resolve(process.env.QA_OUT||path.join(here,'output'));
const captures=path.join(out,'captures');
const base='http://127.0.0.1:4173/';
const args=new Set(process.argv.slice(2));
const headed=args.has('--headed')||process.env.QA_HEADED==='1';
const noCaptures=args.has('--no-captures');
const onlyArg=process.argv.find(x=>x.startsWith('--case='));
const onlyCase=onlyArg?.slice('--case='.length)||null;

function die(msg){console.error(msg);process.exit(1)}
function hashFile(p){return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex')}
function which(cmd){
  try{
    const r=spawnSync(process.platform==='win32'?'where':'which',[cmd],{encoding:'utf8'});
    if(r.status===0)return r.stdout.trim().split(/\r?\n/)[0]||null;
  }catch{}
  return null;
}
function resolveBrowser(p){
  if(!p)return null;
  try{
    if(!fs.existsSync(p))return null;
    const real=fs.realpathSync(p);
    // Distro wrappers (e.g. Fedora /usr/bin/chromium-browser -> *.sh) are not always valid Playwright binaries.
    if(real.endsWith('.sh')){
      const elf=real.slice(0,-3);
      if(fs.existsSync(elf))return elf;
    }
    return real;
  }catch{
    return fs.existsSync(p)?p:null;
  }
}
function isBenignBrowserFetch(url){
  if(!url)return false;
  try{
    const u=new URL(url,base);
    return /^\/(favicon\.ico|apple-touch-icon[^/]*)$/i.test(u.pathname);
  }catch{
    return false;
  }
}
function browserBin(){
  const candidates=[
    process.env.BROWSER_BIN,
    '/usr/lib64/chromium-browser/chromium-browser',
    '/usr/lib/chromium-browser/chromium-browser',
    '/usr/bin/google-chrome-stable','/usr/bin/google-chrome',
    '/usr/bin/chromium','/usr/bin/chromium-browser',
    '/usr/bin/microsoft-edge-stable','/usr/bin/microsoft-edge',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
    process.env.LOCALAPPDATA&&path.join(process.env.LOCALAPPDATA,'Google/Chrome/Application/chrome.exe'),
    process.env.PROGRAMFILES&&path.join(process.env.PROGRAMFILES,'Google/Chrome/Application/chrome.exe'),
    process.env['PROGRAMFILES(X86)']&&path.join(process.env['PROGRAMFILES(X86)'],'Google/Chrome/Application/chrome.exe'),
    process.env.PROGRAMFILES&&path.join(process.env.PROGRAMFILES,'Microsoft/Edge/Application/msedge.exe'),
    process.env.LOCALAPPDATA&&path.join(process.env.LOCALAPPDATA,'Microsoft/Edge/Application/msedge.exe'),
    which('google-chrome-stable'),which('google-chrome'),which('chromium'),
    which('chromium-browser'),which('microsoft-edge'),which('msedge')
  ];
  for(const c of candidates){
    const resolved=resolveBrowser(c);
    if(resolved)return resolved;
  }
  return null;
}
async function waitForServer(){
  for(let i=0;i<50;i++){
    try{const r=await fetch(base);if(r.ok)return}catch{}
    await new Promise(r=>setTimeout(r,100));
  }
  throw new Error('QA server did not become ready on port 4173');
}
async function waitJson(locator,timeout=120000){
  const end=Date.now()+timeout;
  while(Date.now()<end){
    const text=(await locator.textContent())?.trim()||'';
    if(text.startsWith('{'))return JSON.parse(text);
    await new Promise(r=>setTimeout(r,100));
  }
  throw new Error('Timed out waiting for JSON output');
}

fs.mkdirSync(captures,{recursive:true});
const python=process.env.PYTHON||'python3';
const built=spawnSync(python,[path.join(here,'build.py')],{
  cwd:root,
  stdio:'inherit',
  env:{...process.env,QA_SOURCE:sourceHtml}
});
if(built.status!==0)die(`QA build failed using ${python}`);
console.log(`QA source: ${sourceHtml}`);
console.log(`QA cases: ${casesFile}`);
console.log(`QA out: ${out}`);

const exe=browserBin();
if(!exe)die('No Chromium-family browser found. Set BROWSER_BIN to Chrome, Chromium, or Edge. See qa/README.md.');
console.log(`Using browser: ${exe}`);

const server=spawn(process.execPath,[path.join(here,'server.cjs')],{cwd:here,stdio:['ignore','pipe','pipe']});
server.stdout.on('data',d=>process.stdout.write(`[server] ${d}`));
server.stderr.on('data',d=>process.stderr.write(`[server] ${d}`));

let browser;
try{
  await waitForServer();
  browser=await chromium.launch({headless:!headed,executablePath:exe,args:['--autoplay-policy=no-user-gesture-required']});
  const page=await browser.newPage({viewport:{width:1100,height:760}});
  const consoleErrors=[];
  page.on('console',m=>{
    if(m.type()!=='error')return;
    const loc=m.location();
    consoleErrors.push({type:'console',text:m.text(),url:loc?.url||null});
  });
  page.on('pageerror',e=>consoleErrors.push({type:'pageerror',text:String(e),url:null}));
  await page.goto(base,{waitUntil:'load'});
  await page.waitForSelector('#audit-scene');

  await page.locator('#run-qa').click();
  const regression=await waitJson(page.locator('#qa-results'));

  await page.getByRole('button',{name:'Run acceptance diagnostics'}).click();
  const diagnostics=await waitJson(page.locator('#audit-diagnostics'));

  const matrix=JSON.parse(fs.readFileSync(casesFile,'utf8'));
  const selected=onlyCase?matrix.filter(c=>c.id===onlyCase):matrix;
  if(onlyCase&&!selected.length)throw new Error(`Unknown capture case: ${onlyCase}`);
  const captureIndex=[];

  if(!noCaptures){
    for(const c of selected){
      await page.selectOption('#audit-scene',c.scene);
      await page.fill('#audit-tick',String(c.tick));
      await page.locator('#audit-jump').click();
      await page.waitForTimeout(40);
      const meta=JSON.parse((await page.locator('#audit-meta').textContent())||'{}');
      const png=path.join(captures,`${c.id}.png`);
      const json=path.join(captures,`${c.id}.json`);
      await page.locator('#game').screenshot({path:png});
      fs.writeFileSync(json,JSON.stringify({...c,...meta},null,2)+'\n');
      captureIndex.push({...c,meta,png:path.relative(root,png),json:path.relative(root,json)});
      console.log(`captured ${c.id}: ${c.scene} @ ${c.tick}`);
    }
  }

  const report={
    generatedAt:new Date().toISOString(),
    baseline:{path:path.relative(root,sourceHtml)||sourceHtml,sha256:hashFile(sourceHtml)},
    browser:{executable:exe,headed},
    regression,
    diagnostics,
    consoleErrors,
    captures:captureIndex
  };
  fs.writeFileSync(path.join(out,'agent-report.json'),JSON.stringify(report,null,2)+'\n');
  const materialErrors=consoleErrors.filter(e=>!isBenignBrowserFetch(e.url||''));
  console.log(`\nQA report: ${path.relative(root,path.join(out,'agent-report.json'))}`);
  console.log(`Browser: ${exe}`);
  console.log(`Regression: ${regression.passed} passed / ${regression.failed} failed`);
  console.log(`Console/page errors: ${consoleErrors.length} (material: ${materialErrors.length})`);
  if(regression.failed||materialErrors.length)process.exitCode=2;
} finally {
  if(browser)await browser.close();
  server.kill('SIGTERM');
}
