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
