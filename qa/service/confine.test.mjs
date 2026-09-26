import test from 'node:test';
import assert from 'node:assert/strict';
import {spawn} from 'node:child_process';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {resolveBrowserLaunch} from './browser-launch.mjs';

const script = path.join(path.dirname(fileURLToPath(import.meta.url)), 'chromium-confine.sh');
const probe = path.join(os.tmpdir(), 'scarlet-qa19-confine-probe.py');

await fs.writeFile(probe, `
import ctypes, errno, os
print("PROBE_START")
print("env_canary", "PRESENT" if "QA_CANARY_ENV" in os.environ else "ABSENT")
print("pid", os.getpid(), "ppid", os.getppid())
host = os.environ.get("HOST_PID", "")
visible = []
try:
    visible = [name for name in os.listdir("/proc") if name.isdigit()]
except OSError as exc:
    print(f"proc_list_denied errno={exc.errno}")
print("host_pid_visible", host in visible)
if host:
    for suffix in ("environ", "mem", "cwd"):
        target = f"/proc/{host}/{suffix}"
        try:
            fd = os.open(target, os.O_RDONLY)
            os.close(fd)
            print(f"ACCESSIBLE {target}")
        except OSError as exc:
            print(f"DENIED {target} errno={exc.errno}")
    libc = ctypes.CDLL(None, use_errno=True)
    libc.ptrace.restype = ctypes.c_long
    rc = libc.ptrace(16, int(host), None, None)
    err = ctypes.get_errno()
    print("PTRACE", "OK" if rc == 0 else f"DENIED errno={err}")
    if rc == 0:
        libc.ptrace(17, int(host), None, None)
try:
    os.read(5, 32)
    print("FD5_READ")
except OSError as exc:
    print(f"FD5_DENIED errno={exc.errno}")
secret = os.environ.get("SECRET_PATH", "")
if secret:
    try:
        fd = os.open(secret, os.O_RDONLY)
        os.close(fd)
        print("SECRET_ACCESSIBLE")
    except OSError as exc:
        print(f"SECRET_DENIED errno={exc.errno}")
for target in ("/home/dellis/.config/gh/hosts.yml", "/home/dellis/.config/chromium"):
    try:
        fd = os.open(target, os.O_RDONLY)
        os.close(fd)
        print(f"ACCESSIBLE {target}")
    except OSError as exc:
        print(f"DENIED {target} errno={exc.errno}")
print("PROBE_END")
`);

function runScript(args, env, stdio) {
  return new Promise((resolve, reject) => {
    const child = spawn(script, args, {env, stdio: stdio || ['ignore', 'pipe', 'pipe']});
    let stdout = '';
    let stderr = '';
    child.stdout.on('data', chunk => { stdout += chunk.toString('utf8'); });
    child.stderr.on('data', chunk => { stderr += chunk.toString('utf8'); });
    child.once('error', reject);
    child.once('close', status => resolve({status, stdout, stderr}));
  });
}

test('production confinement cannot be disabled while a credential directory is set', () => {
  assert.throws(() => resolveBrowserLaunch({QA_BROWSER_CONFINEMENT: 'off', CREDENTIALS_DIRECTORY: '/run/credentials/example'}),
    error => error.code === 'browser_confinement_required');
  assert.equal(resolveBrowserLaunch({QA_BROWSER_CONFINEMENT: 'off'}).confined, false);
  assert.equal(resolveBrowserLaunch({}).confined, true);
  assert.equal(resolveBrowserLaunch({}).executable, script);
});

test('confinement fails closed when bubblewrap is unavailable or the sandbox is disabled', async () => {
  const missing = await runScript(['--version'], {...process.env, QA_BWRAP: '/no/such/bwrap'});
  assert.equal(missing.status, 69);
  assert.match(missing.stderr, /confinement unavailable/);
  const disabled = await runScript(['--no-sandbox', '--version'], process.env);
  assert.equal(disabled.status, 69);
  assert.match(disabled.stderr, /refusing to disable/);
  const homeProfile = await runScript(['--user-data-dir=/home/dellis/chrome-profile', '--version'], process.env);
  assert.equal(homeProfile.status, 69);
  assert.match(homeProfile.stderr, /user-data-dir/);
});

test('confined process cannot read the parent, a leaked descriptor, or the fake credential', async () => {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-confine-canary-'));
  const secret = path.join(directory, 'qa-secret');
  const fdFile = path.join(directory, 'fd-canary.txt');
  await fs.writeFile(secret, 'CANARY-FILE-SECRET-NOT-REAL\n', {mode: 0o600});
  await fs.writeFile(fdFile, 'CANARY-FD-SECRET-NOT-REAL\n', {mode: 0o600});
  const fd = await fs.open(fdFile, 'r');
  try {
    const result = await runScript([], {
      ...process.env,
      QA_CONFINE_PROBE: '1',
      QA_CONFINE_PROBE_SCRIPT: probe,
      QA_CANARY_ENV: 'CANARY-ENV-SECRET-NOT-REAL',
      HOST_PID: String(process.pid),
      SECRET_PATH: secret
    }, ['ignore', 'pipe', 'pipe', 'ignore', 'ignore', fd.fd]);
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /env_canary ABSENT/);
    assert.match(result.stdout, /host_pid_visible False/);
    assert.match(result.stdout, new RegExp(`DENIED /proc/${process.pid}/environ errno=2`));
    assert.match(result.stdout, new RegExp(`DENIED /proc/${process.pid}/mem errno=2`));
    assert.match(result.stdout, /PTRACE DENIED errno=3/);
    assert.match(result.stdout, /FD5_DENIED/);
    assert.match(result.stdout, /SECRET_DENIED/);
    assert.match(result.stdout, /DENIED \/home\/dellis\/\.config\/gh\/hosts\.yml/);
    assert.doesNotMatch(result.stdout, /CANARY-FILE-SECRET-NOT-REAL|CANARY-FD-SECRET-NOT-REAL|CANARY-ENV-SECRET-NOT-REAL/);
  } finally {
    await fd.close();
    await fs.rm(directory, {recursive: true, force: true});
  }
});

test('confined Chromium keeps its native sandbox', async () => {
  const profile = await fs.mkdtemp(path.join(os.tmpdir(), 'scarlet-qa19-confine-profile-'));
  const result = await runScript([
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--user-data-dir=' + profile,
    '--enable-logging=stderr',
    '--v=1',
    '--virtual-time-budget=3000',
    '--dump-dom',
    'about:blank'
  ], process.env);
  assert.equal(result.status, 0, result.stderr.slice(-500));
  assert.match(result.stdout, /<html>/);
  const chromeLog = await fs.readFile(path.join(profile, 'chrome_debug.log'), 'utf8').catch(() => '');
  const observed = `${result.stderr}\n${chromeLog}`;
  assert.match(observed, /Activated seccomp-bpf sandbox for process type: renderer/);
  assert.doesNotMatch(result.stdout, /--no-sandbox/);
  await fs.rm(profile, {recursive: true, force: true});
});
