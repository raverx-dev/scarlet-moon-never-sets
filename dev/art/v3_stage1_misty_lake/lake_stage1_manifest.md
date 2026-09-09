# Version 3 Stage 1 Misty Lake — Asset Manifest + 192×240 Playfield Proof

This package remains art-authoring source only. It does not modify gameplay or runtime rendering.

## Delta from prior pass

The original tile vocabulary passed, but the first assembled proof still read too much like a uniform blue field. Only the minimum additional authored assets were added:

- `lake_water_band_e` (8×8) — darker current break
- `lake_mist_transition_d` (8×8) — broken mist-bank transition
- `lake_edge_cluster_c` (16×16) — combined shoreline/reed cluster

## Danmaku composition rule

- Central safe lane: **x=48..143**. This lane uses darker water bases plus sparse dim ripples, mist, and moon-reflection fragments.
- Edge columns carry most reeds, stones, posts, lanterns, lily pads, ice accents, foam, and denser mist banks.
- White/red/blue hostile bullets should remain the dominant visual layer.

## Exact assets

| Asset | Size | Intended use |
|---|---:|---|
| `lake_water_dark_a` | 8×8 | central-safe / anywhere — primary low-contrast water base |
| `lake_water_dark_b` | 8×8 | central-safe / anywhere — complementary low-contrast water base |
| `lake_water_dark_c` | 8×8 | central-safe / anywhere — sparse low-contrast water base |
| `lake_water_edge_d` | 8×8 | edge columns / sparse — slightly brighter side-water variant |
| `lake_ripple_dim_a` | 8×8 | central-safe / sparse overlay — dim broken ripple |
| `lake_ripple_dim_b` | 8×8 | central-safe / sparse overlay — offset dim broken ripple |
| `lake_ripple_cool_a` | 8×8 | edge columns / upper field — cool moonlit ripple |
| `lake_foam_spark_a` | 8×8 | edge columns only / rare — tiny foam/ice sparkle |
| `lake_foam_edge_b` | 8×8 | edge columns only / rare — broken foam flecks |
| `lake_mist_wisp_a` | 8×8 | anywhere / low density — broken mist wisp |
| `lake_mist_wisp_b` | 8×8 | anywhere / low density — alternate mist wisp |
| `lake_mist_wisp_c` | 8×8 | central-safe / very sparse — minimal center-lane mist |
| `lake_ice_glint` | 8×8 | edge columns only / rare — restrained icy glint |
| `lake_moon_reflect_a` | 8×8 | upper/mid water / sparse — silver moon-reflection fragment |
| `lake_moon_reflect_b` | 8×8 | upper/mid water / sparse — offset reflection fragment |
| `lake_reeds_a` | 16×16 | left/right edge columns — tall reed cluster |
| `lake_reeds_b` | 16×16 | left/right edge columns — complementary reed cluster |
| `lake_shore_stone_a` | 16×16 | edge columns / shoreline — blue-gray stone cluster |
| `lake_shore_stone_b` | 16×16 | edge columns / shoreline — staggered stone cluster |
| `lake_lilypad_a` | 16×16 | edge water / rare — lily pad |
| `lake_shore_post` | 8×24 | edge columns only — weathered shoreline post |
| `lake_lantern_dim` | 16×24 | edge columns only / low frequency — dim shore lantern |
| `lake_ice_shard` | 8×16 | edge water / rare — restrained ice shard |
| `lake_water_band_e` | 8×8 | sparse current break — minimum anti-uniformity addition |
| `lake_mist_transition_d` | 8×8 | sparse broken mist bank — minimum transition addition |
| `lake_edge_cluster_c` | 16×16 | left/right edge columns only — minimum shoreline-density addition |

## Composition proof

`lake_playfield_composition.js` deterministically builds the exact 192×240 reference composition from the matrices above. It does not introduce runtime integration and it does not draw or redefine characters, bullets, items, enemies, or HUD elements.

The review PNGs are not committed by request.

## Validation summary

- assets: **26**
- composition: **192×240**
- placements: **900**
- center safe lane: **x=48..143**
- edge-only asset placements overlapping center lane: **0**
- center bright density: **0.001432**
- edge bright density: **0.044748**
- flattened reference matrix SHA-256: `ae727e9d6552edd4e8ae09152aba4494f2cceed42fd1c737b851521fbb682424`
- result: **PASS**

## Palette

No palette extension is requested. All authored matrix characters are existing `PAL` keys plus `.` transparency.
