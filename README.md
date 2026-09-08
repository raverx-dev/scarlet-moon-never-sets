# 東方紅月夜 ~ Scarlet Moon Never Sets ~

An unofficial Touhou Project fan game: a three-stage vertical danmaku shooter imagined as an impossible late-era Famicom cartridge. Reimu investigates three nights without sunrise—and without donations. Fly through Misty Lake, the Forest of Magic, and the Scarlet Devil Mansion; confront Cirno, Marisa, Sakuya, and Remilia.

The repository now preserves multiple self-contained playable builds. The root `index.html` is a GitHub Pages version selector; each frozen game version remains a single self-contained HTML file under `versions/`. See [`VERSIONS.md`](VERSIONS.md) for the archive policy and exact checkpoints.

## Play locally

For a preserved build, open its `versions/<version>/index.html` in a desktop Chromium- or Firefox-class browser. Press Enter or Z to advance through the boot screens. Audio starts after a keyboard press or a click on the game. Browser previewers that suppress JavaScript are not the game runtime; open the HTML directly in your browser.

| Key | Action |
| --- | --- |
| Arrow keys | Move |
| Z, held | Shoot |
| Z | Confirm / complete text / advance dialogue |
| Shift | Focus: slow movement, tight shots, visible hitbox |
| X | Fantasy Seal bomb; cancel in menus |
| Enter | Start / pause / resume |
| M | Mute / unmute |
| X while paused | Return to title |

Keyboard-only desktop play is the intended platform. Mobile controls and gamepad controls are not implemented.

## Playing and scoring

Start with 3 lives, 3 bombs, and power 1. Red P items raise shot power to a maximum of 4. Blue boxed items give points. Bullets can graze Reimu once each for 50 points. At power 3 or 4, entering the upper quarter of the field attracts items; the collection line appears in gold.

Reimu moves at 2.45 logical pixels per frame normally and 1.2 when focused. Diagonal movement is normalized. The collision core is a centered 4×4 square, independent of the character sprite. Bullets have shape-specific collision sizes; lasers and the large spear use line-segment collision.

Fantasy Seal clears bullets, damages enemies and bosses, and provides invulnerability. An X press during the eight-frame deathbomb window prevents losing a life. Losing a life reduces power and preserves progress. Continues are unlimited, reset score, restore three lives and bombs, and restart the current stage or the current boss from its beginning. The continue countdown intentionally begins with ⑨.

Spell captures require defeating the phase without dying or bombing. Ordinary spell timeouts do not give a capture bonus. Red Magic is a survival hybrid: early damage cannot finish it before 30 seconds; surviving the timer can capture it. High score is stored in browser session storage when available; storage restrictions do not prevent play.

Title idle time starts the scripted attract sequence. The ending, animated credits gags, final card, return to title, and another run are implemented. Dialogue is advanced manually. Runtime depends on reading speed, damage output, and continues.

## GitHub Pages

GitHub Pages publishes `main`. The normal project Pages URL opens the root version selector, which launches immutable playable snapshots under `versions/`. Each preserved build remains self-contained and has no path-sensitive runtime assets, network requests, package steps, or runtime API calls.

Current preserved versions:

- `versions/original/` — Version 1, original build.
- `versions/p1-visual-audio/` — Version 2, accepted P0 + Visual P1 + Audio P1 checkpoint.

Future accepted iterations are added as new version folders; existing folders are never overwritten.

## Implementation

- HTML, CSS, vanilla JavaScript, Canvas 2D, and Web Audio only.
- 256×240 logical canvas; 192×240 playfield and 64-pixel sidebar.
- Integer upscaling where the viewport permits it, nearest-neighbor presentation, manually drawn bitmap lettering, sprites, tiles, and portraits.
- Fixed 60 Hz simulation with bounded frame catch-up; focus loss pauses combat and releases held keys.
- Authored stage cue lists and five ordinary enemy archetypes.
- Fourteen individually scripted boss phases, including freeze/thaw state changes, warning beams, moving spears, and layered final patterns.
- Two pulse voices using explicit duty-cycle waveforms, triangle bass, and deterministic LFSR noise. No recordings, soundfonts, MIDI files, or external audio are embedded.

The source is organized inside each playable HTML into drawing primitives and sprites, input/state handling, score synthesis, boss patterns, authored stage cues, collision/scoring, dialogue data, and scene rendering. There is no general-purpose engine or runtime debug menu.

## Music and attribution

Touhou Project, its characters, setting, and source compositions are by ZUN / Team Shanghai Alice. This implementation's code, graphics, synthesis, accompaniment, and musical adaptations were created for this project. See `FANWORK_NOTICE.md`.

The current Visual + Audio P1 build replaces the original tiny music loops with authored four-voice Famicom-style arrangements. Stage tracks and Sakuya use newly composed material. Reimu/title/ending, Cirno, Marisa, and Remilia use newly implemented theme-inspired adaptations; final recognizability/source-fidelity remains subject to human listening and later acceptance work.

## Validation and limits

The recovered QA tool exercises movement, diagonal normalization, focus, shooting, enemy/boss damage, hitbox, graze, items, power, bombs, death/deathbomb behavior, lives, score, spell bonuses, pause/resume, continues, all stages and boss phases, dialogue, attract/help screens, audio state changes, ending, credits, return to title, and a second run.

Accepted P0, Visual P1, and Audio P1 engineering checkpoints retained 32 passed / 0 failed regression results with no material browser console/page errors. Automated checks do not certify subjective art quality, musical recognizability, Normal-difficulty tuning, or an unassisted human no-continue clear.

## Development

The repository includes a development-only [`qa/`](qa/) tool for deterministic state inspection, regression checks, diagnostics, automated browser capture, and future maintenance.

Active implementation does not happen inside preserved version folders. `v1-polish` is the accepted Visual + Audio P1 feature checkpoint, while the dedicated character replacement work proceeds independently on `sprite-redesign`. Once a new build is accepted, it is frozen as the next numbered playable version before development continues.

The longer-term project direction is documented in [`ROADMAP.md`](ROADMAP.md). The current priority is to finish and stabilize Scarlet Moon itself before extracting reusable systems. The roadmap intentionally treats the game as the future reference implementation for a possible reusable HTML5/JavaScript danmaku framework and authoring environment rather than as a disposable engine demo.
