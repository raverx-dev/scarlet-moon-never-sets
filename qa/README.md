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
