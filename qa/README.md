# Developer QA (audit-only)

The root `index.html` is untouched. These tools inject additional controls into a disposable copy of that file; never deploy the generated copy as the game.

From the repository root:

```
python3 qa/build.py
python3 -m http.server 8000
```

Open `http://localhost:8000/qa/generated.html`. Alternatively open the generated HTML locally in a normal desktop browser. No dependencies are required. `node qa/server.cjs` provides an optional port-4173 adapter for supervised browser QA; its root is the inspector and `/baseline` serves the untouched game.

- **Run regression checks** executes the recovered 32-group simulation suite and displays JSON.
- **Scene**, **Tick**, **Inspect frozen frame** jump to every major scene and all 14 boss phases. Tick is a 60 Hz simulation count from scene/phase start. Boss inspection skips the initial 72-frame phase gap. Stage inspection skips stage cards; Stage 3 inspection after tick 2520 marks Sakuya cleared so the second half can be inspected independently.
- **Advance dialogue** advances a fully printed page. **Resume motion** returns to normal ticking; **Freeze motion** freezes without adding the game's pause overlay.
- **Run acceptance diagnostics** emits music lengths and targeted source-backed behavior measurements.
- Music/effect selectors permit isolated listening on a desktop browser.
- **Invulnerable inspection** is optional for interactive practice. Frozen scene capture uses invulnerability during stepping; on blink-off frames Reimu may be absent. That is a harness artifact, not an invisible-player finding.

`regression.js` is recovered developer tooling. `inspection.js`, `build.py`, and the server adapter were added for this audit. The inspector replaces `tick` only in its generated page so it can freeze rendering. It must not be confused with uninstrumented runtime performance testing. Game source is read directly, without minification or rewrites.

The regression route uses invulnerability, automatic dialogue confirmation, and boss timeouts. It is not a human-played clear, difficulty proof, music-fidelity test, or screenshot comparison. Browser UI checks supplement it. Reports are in `audit/evidence/`. Re-run in a fresh tab, click regression once, wait for results, then use diagnostics and scene inspection. Export displayed JSON by copying it; do not carry inspection state into a release build.
