# Version 3 Stage 2 — Forest of Magic native pixel assets

Governing specification: `raverx-dev/scarlet-moon-never-sets#16`.

Authoring baseline: `sprite-redesign` at `69d06766c0a6c165f26f71ded96d7b5bd8a122df`.

This package is **authoring source only**. It does not change gameplay or runtime code.

## Style / composition lock

- Native integer pixels only.
- Primary building blocks are 8×8 and 16×16.
- Central bullet lane stays dark and low contrast.
- Dense canopy, trunks, mushrooms, lanterns, fireflies, and moonlit foliage are edge-weighted.
- Existing `PAL` letters plus `.` only.
- **PALETTE EXTENSION REQUEST: NONE.**

## Palette inventory

- `B` = `#2a3160` — 262 authored pixels
- `G` = `#64b58a` — 78 authored pixels
- `H` = `#2c2438` — 11 authored pixels
- `M` = `#6b3d9a` — 10 authored pixels
- `R` = `#9a2438` — 36 authored pixels
- `W` = `#d4c4a8` — 46 authored pixels
- `b` = `#424d9d` — 21 authored pixels
- `e` = `#21423e` — 548 authored pixels
- `g` = `#f5cb70` — 14 authored pixels
- `h` = `#191528` — 131 authored pixels
- `i` = `#4aa0c8` — 6 authored pixels
- `m` = `#ae68d7` — 62 authored pixels
- `n` = `#171b39` — 640 authored pixels
- `o` = `#c47a4a` — 41 authored pixels
- `r` = `#e83a51` — 89 authored pixels
- `t` = `#8b5a3c` — 154 authored pixels
- `u` = `#704638` — 328 authored pixels
- `v` = `#5a8f6a` — 487 authored pixels
- `w` = `#fff0ce` — 22 authored pixels
- `y` = `#ffe08a` — 11 authored pixels

## Asset inventory

- `forest_bark_a` — 8×8 — bark — side trunks; repeatable trunk bark.
- `forest_bark_b` — 8×8 — bark — side trunks; alternate repeatable bark.
- `forest_bark_knot` — 8×8 — bark — side trunks only; knot/scar bark insert.
- `forest_leaf_a` — 8×8 — foliage — edges; small leaf cluster.
- `forest_leaf_b` — 8×8 — foliage — edges; alternate leaf cluster.
- `forest_leaf_c` — 8×8 — foliage — edges; broken anti-repetition leaf cluster.
- `forest_leaf_moonlit` — 8×8 — foliage — far edges only; rare moonlit leaf accent.
- `forest_path_lane_a` — 8×8 — ground — central lane; primary quiet bullet-lane ground.
- `forest_path_lane_b` — 8×8 — ground — central lane; quiet lane alternate.
- `forest_path_lane_c` — 8×8 — ground — central lane; quiet lane alternate 2.
- `forest_ground_edge` — 8×8 — ground — lane margins / sides; path-to-vegetation transition.
- `forest_canopy_a` — 16×16 — canopy — side columns / top band; dense organic canopy metatile.
- `forest_canopy_b` — 16×16 — canopy — side columns / top band; alternate organic canopy metatile.
- `forest_canopy_moonlit` — 16×16 — canopy — upper outer edges; rare moonlit canopy highlight.
- `forest_canopy_shadow` — 16×16 — canopy — near lane margins / dim sections; low-contrast canopy mass.
- `forest_trunk_straight` — 16×16 — trunk — outer sides; straight trunk segment.
- `forest_trunk_knotted` — 16×16 — trunk — outer sides; knotted trunk segment.
- `forest_root_left` — 16×16 — trunk — outer left edge; left-spreading root flare.
- `forest_root_right` — 16×16 — trunk — outer right edge; right-spreading root flare.
- `forest_mushroom_red` — 16×16 — mushroom — sides only; red spotted mushroom.
- `forest_mushroom_violet` — 16×16 — mushroom — sides only; violet spotted mushroom.
- `forest_mushroom_cluster` — 16×16 — mushroom — far sides only; small mixed mushroom cluster.
- `forest_lantern_small` — 8×16 — light — outer sides; sparse; small magical forest lantern.
- `forest_firefly_a` — 8×8 — light — outer edges only; single firefly sparkle.
- `forest_firefly_b` — 8×8 — light — outer edges only; alternate firefly sparkle.
- `forest_wisp` — 8×8 — light — outer edges / scripted accent; rare magical wisp.
- `forest_distant_pines_a` — 16×16 — silhouette — upper scenery band; distant pine silhouette.
- `forest_distant_pines_b` — 16×16 — silhouette — upper scenery band; alternate distant pine silhouette.
- `forest_distant_pines_moonlit` — 16×16 — silhouette — upper outer band; rare moonlit distant trees.
- `forest_fern` — 16×16 — vegetation — sides; fern edge detail.
- `forest_grass_tuft` — 16×16 — vegetation — lane margins / sides; dark grass/sedge tuft.
- `forest_vine_hanging` — 16×16 — vegetation — upper side canopy; hanging vine element.
- `forest_shrub` — 16×16 — vegetation — sides; compact edge shrub.
- `forest_path_edge_stone` — 16×16 — ground — side / lane margin only; subdued path-border stone.

## Files

- `forest_stage2_assets.js` — integration-friendly exact matrix source.
- `forest_stage2_assets.json` — machine-readable exact matrix source + dimensions + metadata.
- `forest_stage2_preview.png` — enlarged nearest-neighbor preview rendered directly from the matrices.
- `forest_stage2_playfield_preview.png` — 192×240 composition proof enlarged 4× with nearest-neighbor scaling; assembled only from this asset family.
- `forest_stage2_validation.txt` — dimension / prefix / character / composition validation.
- `render_forest_preview.py` — minimal source loader for reproducible matrix rendering.

## Validation result

- Matrices: **PASS**
- `forest_` prefixes: **PASS**
- Allowed characters: **PASS**
- Palette extension: **NONE**
- Central-lane darkness proof: **PASS**
  - center mean luminance: `29.08`
  - outer-side mean luminance: `85.65`

The playfield proof is not runtime integration. It exists only to demonstrate the required vertical-danmaku value hierarchy before mechanical integration.
