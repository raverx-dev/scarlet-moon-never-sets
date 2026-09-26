# Developer QA harness

This directory contains development-only tooling for inspecting and regression-testing **東方紅月夜 ~ Scarlet Moon Never Sets ~**. The shipped `index.html` is the source under test and is never rewritten in place.

The harness exists so maintainers and coding agents can reproduce the same state-by-state inspection workflow outside ChatGPT Work/Astra.

## Safety model

- `index.html` remains untouched.
- `qa/build.py` creates disposable `qa/generated.html` by injecting the QA controls into a copy of the shipped game.
- Generated captures and reports go under `qa/output/` and are gitignored.
- Do not deploy `qa/generated.html` as the game.
- Promote only evidence that supports a real audit finding into `audit/evidence/`.

## Manual browser workflow — no npm required

From the repository root:

```bash
python3 qa/build.py
python3 -m http.server 8000
```

Open `http://localhost:8000/qa/generated.html`.

The inspector provides:

- **Run regression checks** — recovered 32-group direct-simulation suite.
- **Scene / Tick / Inspect frozen frame** — deterministic state jumping for presentation scenes, dialogues, stages, and all 14 boss phases.
- **Advance dialogue** — advances a fully printed page.
- **Resume motion / Freeze motion** — inspect movement without adding the game's pause overlay.
- **Run acceptance diagnostics** — emits track lengths and targeted source-backed gameplay measurements.
- **Music / effect selectors** — isolated audio listening.
- **Invulnerable inspection** — optional interactive practice.

The scene inspector replaces `tick` only inside the generated page so it can freeze rendering. That behavior is not present in the release game.

## Automated agent workflow

For a CLI coding agent or developer who needs reproducible screenshots and machine-readable results:

```bash
cd qa
npm install
npm run agent
```

Requirements:

- Node.js 20+ (pinned `playwright-core@1.63.0`; the runner scripts themselves are ordinary ESM)
- Python 3
- an installed Chromium-family browser: Chrome, Chromium, or Edge

The runner uses `playwright-core` but **does not download a browser**. It tries common Chrome/Chromium/Edge locations, including Fedora's Chromium ELF under `/usr/lib64/chromium-browser/`, and resolves distro wrapper scripts to the real binary when possible. If discovery fails, set `BROWSER_BIN` to the browser executable, not a launcher script:

```bash
BROWSER_BIN=/path/to/chrome npm run agent
```

The local QA server answers Chromium's automatic `/favicon.ico` and `/apple-touch-icon*` fetches with HTTP 204. Those browser-chrome requests are not game assets and do not fail the suite.

Exit status:

- `0` — regression passed and no material page/console errors
- `1` — harness/infrastructure failure (missing browser, build/server error, unknown capture case)
- `2` — recovered regression reported failures, or a material browser console/page error

`agent-report.json` records every console/page error with its text and source URL when Playwright provides one. Benign favicon/touch-icon fetches are recorded if they still occur, but they do not set exit status 2.

Useful modes:

```bash
npm run agent:headed                 # watch the automated run
npm run agent:no-captures            # regression + diagnostics only
node agent-run.mjs --case=r5-final   # one deterministic capture
QA_HEADED=1 npm run agent             # equivalent headed mode
```

Outputs are written locally under:

```text
qa/output/
├── agent-report.json
└── captures/
    ├── <case>.png
    └── <case>.json
```

`agent-report.json` contains:

- SHA-256 of the tested `index.html`;
- browser executable used;
- full recovered regression result;
- acceptance diagnostics;
- browser console/page errors;
- capture manifest and state metadata.

The capture matrix is versioned in `qa/cases.json`. Add a case there when a new stable inspection checkpoint becomes useful to future maintainers.

## What the regression suite certifies

The recovered suite exercises movement, focus, shooting, power, items, hitbox, graze, death/deathbomb, bombs, pause, continues, scoring, spell capture behavior, lasers, all stages, all dialogue, every boss phase, ending, credits, attract mode, audio state changes, and a second run.

It intentionally uses direct simulation, invulnerability, automatic dialogue progression, and boss timeouts. Therefore it **does not certify**:

- subjective visual quality;
- Touhou/Famicom art fidelity;
- musical quality or arrangement fidelity;
- human-played difficulty/fairness;
- frame pacing on every target machine.

Those require review of captured frames, isolated audio, and human playtesting.

## Recommended acceptance workflow

1. Run `npm run agent:no-captures` after code changes.
2. Fix any regression failure or console error before visual review.
3. Run `npm run agent` to regenerate the standard capture matrix locally.
4. Compare the relevant captures with `audit/reference/` and the acceptance spec.
5. Human-play the changed portion when gameplay feel or difficulty could have changed.
6. Commit game changes only after the relevant acceptance finding is satisfied.
7. Keep QA tooling and shipped-game changes separable in review.

## Existing recovered tooling

`regression.js` is recovered developer tooling from the original build session. `inspection.js`, `build.py`, `server.cjs`, `cases.json`, and `agent-run.mjs` make that tooling reusable outside the original sandbox.

## Local-only MCP QA adapter

`qa/service/` provides a deliberately narrow development adapter using the official MCP SDK's Streamable HTTP transport. It exposes exactly two tools:

- `qa_capture` renders only `stage3-interior` (`stage3`, tick `900`) and returns the browser-derived 256×240 canvas PNG inline with structured source, runtime, state, artifact, and hash metadata.
- `qa_regression` separately runs the existing recovered regression suite and acceptance diagnostics, and returns the real checks, diagnostics, browser console/page errors, and blocked requests.

Both tools accept no arguments, or the optional exact values `exact_commit=d7054d2b9b111ff711f44cc3ee5b71268aca6ed8` and `case=stage3-interior`. Unknown fields and every other commit, case, path, branch, URL, JavaScript, or shell value are rejected before execution. This is not a general browser or filesystem service.

Install and test from `qa/`:

```bash
npm install
npm run service:test
npm run service:smoke
```

The smoke stages the approved game commit once, starts an ephemeral loopback MCP server with a random test secret, calls both tools through MCP against that prepared source, verifies the inline PNG dimensions/hash and authenticated artifact copy, and writes `qa/output/service-smoke-summary.json`. Its per-run evidence is under `qa/output/service-runs/`; each completed run retains only its private `evidence/` directory.

Stage the approved game commit before starting the service. The destination must not already exist. This command does not delete or replace an existing directory; a later update is a separate reviewed procedure that publishes a new directory and switches `QA_PINNED_SOURCE` only after validation. This provisioning step is the only place that contacts GitHub. A QA request does not fetch, and it does not accept a source path from the caller:

```bash
cd qa
node service/stage-pinned-source.mjs /absolute/new-prepared-source
export QA_PINNED_SOURCE=/absolute/new-prepared-source
export QA_SERVICE_SECRET="$(openssl rand -base64 48 | tr -d '\n')"
export QA_SERVICE_RUN_ROOT="$(pwd)/output/service-runs"
npm run service
```

For a future systemd service, do not put the bearer in the unit, the command line, or the writable state directory. Point `LoadCredential=qa-secret:` at a root-owned file such as `/etc/scarlet-qa/qa-secret` and let the process read `$CREDENTIALS_DIRECTORY/qa-secret`. When `CREDENTIALS_DIRECTORY` is set, an environment secret is not accepted as a fallback and browser confinement cannot be turned off. The file must contain the secret with no trailing newline. Local development can still use `QA_SERVICE_SECRET` when that directory is unset.

The default endpoint is `http://127.0.0.1:3020/mcp`. Every MCP request, including `GET` discovery attempts, and every `/artifacts/<run-id>/<artifact-id>` request requires `Authorization: Bearer <secret>`. The process rejects every bind host except the literal `127.0.0.1`, rejects weak secrets, applies a 64 KiB request limit, serializes tool runs, and does not log the secret. Do not put the older `qa/server.cjs` on any externally reachable interface.

Each request creates a random private run directory, copies the prepared detached checkout of commit `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8`, and rejects a missing, dirty, branch-attached, wrong-commit, wrong-remote, or wrong-hash tree before execution. It validates the QA-tool revision, tracked symlink containment, `versions/v4/index.html`, and game SHA-256 `11cf1b906aca600096827f15795ee6282547a7bb161567b868037028bc08d3a4`. The static server receives `PATH`, `LANG`, and `LC_ALL` only. Chromium is started through `chromium-confine.sh`, which requires bubblewrap, closes inherited descriptors above stderr, and gives the browser a new user, pid, and mount namespace. That view has a fresh `/proc`, temporary `/home` and `/run`, read-only system libraries and fonts, and only the Playwright profile under `/tmp` or `/dev/shm`. It does not receive proxy variables, the MCP bearer, or the host `/proc`. The launcher refuses `--no-sandbox`. `QA_BROWSER_CONFINEMENT=off` is an explicit local-development escape and is rejected while `CREDENTIALS_DIRECTORY` is set. The default is confined Chromium.

The launcher keeps the host network namespace so the browser can reach the loopback game server. That is not an external-egress control. Page routing still permits only the run's ephemeral authenticated loopback origin; external and `file:` requests are blocked and reported. Neither the wrapper nor that routing proves an OS policy that denies remote TCP. A future unit must enforce that separately. Browser/server processes and command output are bounded, and the per-run source copy is removed in `finally` while run-scoped evidence remains. The prepared source itself is not written.

Regression failures are successful MCP calls with structured `status: "failed"`; they are not disguised as infrastructure errors. Clone, hash, build, browser, timeout, or other infrastructure failures return structured `status: "infrastructure_error"` with MCP `isError: true` and a safe run-scoped error report.

### External deployment is blocked

This module is qualified only for local development use. It does **not** claim that OS-level isolation or remote-ingress controls are installed, reviewed, or sufficient. Before any future remote exposure, a separate host qualification must fail closed unless all of the following are independently implemented and verified:

- a dedicated restricted service UID;
- a Chromium sandbox suitable for untrusted content, without `--no-sandbox`;
- filesystem/process isolation that exposes no host secrets or unrelated files;
- outbound network restriction, with pinned source acquisition staged separately from browser execution;
- OS-enforced per-run temporary isolation, cleanup, wall-clock, CPU, memory, process, and output caps;
- authenticated TLS ingress through a trusted boundary, with secret rotation and request controls; and
- artifact serving restricted to authorized run-scoped evidence only.

No tunnel, public listener, system service, or ChatGPT connector is created by this QA module or its tests.
