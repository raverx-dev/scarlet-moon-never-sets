# 東方紅月夜 ~ Scarlet Moon Never Sets ~

An unofficial Touhou Project fan game: a three-stage vertical danmaku shooter imagined as an impossible late-era Famicom cartridge. Reimu investigates three nights without sunrise—and without donations. Fly through Misty Lake, the Forest of Magic, and the Scarlet Devil Mansion; confront Cirno, Marisa, Sakuya, and Remilia.

The executable is the single, self-contained `index.html`. The release contains exactly this file, this README, and `FANWORK_NOTICE.md`. No installation, build, packages, remote assets, or server is required by the game.

## Play locally

Download the release, extract it if using the ZIP, and open `index.html` in a desktop Chromium- or Firefox-class browser. Press Enter or Z to advance through the boot screens. Audio starts after a keyboard press or a click on the game. Browser previewers that suppress JavaScript are not the game runtime; open the downloaded HTML in your browser.

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

Place the three release files at your repository root. In the repository's Pages settings, publish that root from the chosen branch. `index.html` is the entry point. There are no path-sensitive asset references, network requests, package steps, or runtime API calls. The same bytes work with ordinary static HTTP hosting.

## Implementation

- HTML, CSS, vanilla JavaScript, Canvas 2D, and Web Audio only.
- 256×240 logical canvas; 192×240 playfield and 64-pixel sidebar.
- Integer upscaling where the viewport permits it, nearest-neighbor presentation, manually drawn bitmap lettering, sprites, tiles, and portraits.
- Fixed 60 Hz simulation with bounded frame catch-up; focus loss pauses combat and releases held keys.
- Authored stage cue lists and five ordinary enemy archetypes.
- Fourteen individually scripted boss phases, including freeze/thaw state changes, warning beams, moving spears, and layered final patterns.
- Two pulse voices using explicit duty-cycle waveforms, triangle bass, and deterministic LFSR noise. Effects borrow a pulse channel. No recordings, soundfonts, MIDI files, or external audio are embedded.

The source is organized inside the HTML into drawing primitives and sprites, input/state handling, score synthesis, boss patterns, authored stage cues, collision/scoring, dialogue data, and scene rendering. There is no general-purpose engine or runtime debug menu.

## Music and attribution

Touhou Project, its characters, setting, and source compositions are by ZUN / Team Shanghai Alice. This implementation's code, graphics, synthesis, accompaniment, and short musical adaptations were created for this project. See `FANWORK_NOTICE.md`.

The stage tracks and Sakuya cue use newly composed material. Reimu's title/ending motif was checked against the composer's publicly published *Maiden's Capriccio* score. Marisa uses the shared *Love-coloured Magic / Love-Colored Master Spark* motif, checked against ZUN's published earlier score and newly voiced for this game. The composer's standalone score catalog is at https://www16.big.or.jp/~zun/html/music_old.html . Source score files are not distributed with this release.

Cirno and Remilia have short reconstructed motif adaptations intended for *Beloved Tomboyish Girl* and *Septette for a Dead Princess*. Their note-for-note fidelity to the source compositions was not independently verified. These are abbreviated musical interpretations, not full transcriptions. Musical fidelity therefore remains a limitation of acceptance sign-off.

## Validation and limits

The game was executed in Chromium. An isolated test harness, excluded from this release, ran the actual simulation and Canvas/Web Audio code. Its 32 checks passed after corrections. They covered movement, diagonal normalization, focus, held firing, enemy/boss shot damage, the tiny hitbox, single-use graze, items, all power levels, collection, bombs, eight-frame death/deathbomb behavior, lives, score, spell bonuses, pause/resume, continues, all stage/boss phases, every dialogue page, attract/help screens, audio initialization/transitions/mute, ending, credits, return to title, and a second run. Laser telegraphs were checked as harmless before activation, and final-phase early-clear protection was checked.

The full progression test used accelerated simulation and inspection invulnerability to exercise every phase without interruption. It was not an unassisted human no-continue clear. Direct browser keyboard checks additionally exposed and corrected lost very short key taps. Screenshots were inspected for the title, dialogue, and final-boss presentation. Red Magic reached 194 simultaneous hostile objects in the regression pass. No game-origin console errors were observed; unrelated browser-extension errors were present.

Actual `file://` execution, Firefox, and a deployed GitHub Pages origin were not directly exercised in the available browser. Self-containment and static HTTP operation were checked. Subjective Normal-difficulty tuning and the unverified musical reconstructions are not certified by the automated pass. The functional title-to-credits loop passes; the full creative/audio acceptance specification is not claimed as completely certified.

## Development

The shipped game remains self-contained, but the repository also includes a development-only [`qa/`](qa/) tool for deterministic state inspection, regression checks, diagnostics, automated browser capture, and future maintenance.

The longer-term project direction is documented in [`ROADMAP.md`](ROADMAP.md). The current priority is to finish and stabilize Scarlet Moon itself before extracting reusable systems. The roadmap intentionally treats the game as the future reference implementation for a possible reusable HTML5/JavaScript danmaku framework and authoring environment rather than as a disposable engine demo.
