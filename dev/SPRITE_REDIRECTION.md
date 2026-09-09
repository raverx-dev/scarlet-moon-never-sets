# Approved Sprite Redesign Direction

Owner approval: 2026-09-08.

This branch is a character-art-only pass based on Visual P1 `2a27cb17103e9d0d9f9f6d8881ba57fd059073ea`.

## Locked native sizes

| Asset | Native size |
| --- | ---: |
| Reimu gameplay | 16×24 |
| Reimu title | 32×48 |
| Reimu portrait | 32×32 authored / 30×32 visible |
| Cirno boss | 24×32 |
| Marisa boss | 32×32 |
| Sakuya boss | 32×32 |
| Remilia boss | 32×32 |
| Boss portraits | 32×32 authored / 30×32 visible |
| Remilia parasol | 32×32 |
| Meiling sleep/story | 24×16 |
| Ordinary fairies | 16×16 |

## Locked scene-scale policy

- Gameplay character art is 1×.
- `reimuTitle` is 1×.
- Portraits are 1×.
- New boss/story matrices are 1× in dialogue, attract, credits, defeat, and ending scenes.
- Only compact gameplay Reimu may stay 2× in story staging.
- `meilingSleep` may be 2× for the gate/credits sleep gag if composition benefits.
- Never 2× a new 24–32px boss/story matrix.

## Locked implementation rules

- Distinct keys for scene-only art: `reimuTitle`, `remiliaParasol`, `meilingSleep`.
- Gameplay animation keys remain gameplay-only.
- Remove procedural gohei/broom/wing character rendering. Reimu may use the authored integer-pixel gohei stamp fallback.
- Remove the procedural ending parasol once `remiliaParasol` is used.
- Preserve `PAL` letter meanings.
- No smoothing, fractional scale, downsampling at runtime, or external runtime assets.
- Collision and boss patterns remain untouched.
- Fill the allocated sprite box deliberately; do not recreate padded/underfilled placeholder art.
- Use the existing permanent `qa/` harness and existing capture matrix; do not invent another QA stack.

`dev/sprites/*.js` contains the exact approved logical-pixel matrices for integration. These files are implementation source/reference only, not shipped runtime dependencies.

## Character Repair P0 notes

### Story Reimu scale (diagnosis only)

No `reimuStory` asset exists. Non-play scenes still stamp compact gameplay `reimu` at 2× (32×48). Native 1× (16×24) is smaller than the 24–32px boss/story matrices and does not improve composition. Do not broadly change these scales until dedicated story art exists.

| Scene | Call | Scale | 1× safe? |
| --- | --- | ---: | --- |
| intro dialogue | `sprite('reimu',70,138,2)` | 2× | no — too small vs shrine / title art |
| boss dialogue (left) | `sprite('reimu',56,116,2)` | 2× | no — 16×24 vs 24–32px bosses |
| boss dialogue (right fallback) | `sprite(other,…, other==='reimu'?2:1)` | 2× if Reimu | no — same |
| ending dialogue | `sprite('reimu',64,128,2)` | 2× | no — smaller than 32×32 Remilia |
| attract shrine | `sprite('reimu',58,168,2)` | 2× | no |
| attract "FINE" / moon | `sprite('reimu',78,150-(t-720)*.28,2)` | 2× | no |
| gate | `sprite('reimu',45+…,168-…,2)` | 2× | no — vs 2× `meilingSleep` |
| defeat | `sprite('reimu',90,190,2)` | 2× | no |
| endingScene / endingExit / theend | `sprite('reimu',58–59,166,2)` | 2× | no |
| credits Reimu | `sprite('reimu',102,156,2)` | 2× | no |

Gameplay `drawPlay` remains 1×. Title uses `reimuTitle` at 1×.

ART REQUIRED: dedicated native `reimuStory` art.

### Remilia attract eyes (unchanged)

`drawAttract()` montage slot `q===3` (`index.html`): two primitive rectangles on black, left unchanged.

- `rect(105,92,11,3,C.red)`
- `rect(142,92,11,3,C.red)`

QA case `attract-eyes` at tick 1130. ART REQUIRED: remilia attract eyes / silhouette.
