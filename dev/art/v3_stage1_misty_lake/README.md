# Version 3 Stage 1 Misty Lake — exact art package

Art-authoring source only. **No runtime integration.** Governing issue: #16. Base checkpoint: `69d06766c0a6c165f26f71ded96d7b5bd8a122df`.

## Approval-pass delta

The original exact tile vocabulary passed dimensional/palette validation, but its first 192×240 assembly read too uniformly blue. The composition proof therefore adds only three minimal support assets:

- `lake_water_band_e` — 8×8 darker current break
- `lake_mist_transition_d` — 8×8 broken mist bank transition
- `lake_edge_cluster_c` — 16×16 shoreline/reed cluster

No other family was redesigned. No palette extension was added.

## Danmaku rule

The deterministic composition proof reserves **x=48..143** as the dark/simple central player-and-bullet lane. Reeds, stones, posts, lanterns, lily pads, ice, foam, and denser mist are concentrated toward the edge columns. White/red/blue hostile bullets are intended to dominate visual attention.

## Committed files

- `lake_stage1_assets.js` — exact `lake_` matrices and palette mapping
- `lake_stage1_assets.json` — machine-readable exact asset inventory
- `lake_playfield_composition.js` — deterministic 192×240 composition proof source using only those matrices
- `lake_stage1_manifest.md` — inventory, placement rules, and palette usage
- `lake_validation.txt` / `lake_validation.json` — dimensional, palette, naming, and composition checks

Preview PNGs are intentionally not committed; they remain review artifacts in the originating chat.

## Validation summary

- Asset count: **26**
- Composition: **192×240**
- Composition placements: **900**
- Edge-only center-lane overlap violations: **0**
- Center bright-pixel density: **0.001432**
- Edge bright-pixel density: **0.044748**
- Reference flattened matrix SHA-256: `ae727e9d6552edd4e8ae09152aba4494f2cceed42fd1c737b851521fbb682424`
- Result: **PASS**
