# Version 3 Stage 3B — Scarlet Devil Mansion gate / rooftop native pixel assets

Governing specification: `raverx-dev/scarlet-moon-never-sets#16`.

Authoring baseline: `69d06766c0a6c165f26f71ded96d7b5bd8a122df`.

This package is **authoring source only**. It does not modify gameplay or runtime code.

## Scope lock

- Mansion gate + rooftop / balcony exterior environment art only.
- No character redraws.
- No bullet, item, UI, dialogue, audio, or gameplay changes.
- Vertical danmaku readability preserved: the **lower center survival area stays intentionally subdued**.
- Existing game `PAL` keys plus `.` only.
- **PALETTE EXTENSION REQUEST: NONE.**
- `roof_scarlet_moon_64` is carried forward from the already-approved shrine/title moon family rather than redesigned independently.

## Asset inventory
- `roof_shingle_a` — 8×8 — palette `Bb`
- `roof_shingle_b` — 8×8 — palette `Bb`
- `roof_shingle_c` — 8×8 — palette `Bb`
- `roof_shingle_shadow` — 8×8 — palette `BHh`
- `roof_masonry_a` — 8×8 — palette `BH`
- `roof_masonry_b` — 8×8 — palette `BH`
- `roof_cobble_a` — 8×8 — palette `Sa`
- `roof_cobble_b` — 8×8 — palette `Sa`
- `roof_ridge_trim` — 8×8 — palette `BHRx`
- `roof_battlement_straight` — 16×16 — palette `BH`
- `roof_battlement_corner_l` — 16×16 — palette `BH`
- `roof_battlement_corner_r` — 16×16 — palette `BH`
- `roof_window_gothic_tall` — 16×16 — palette `BHRWry`
- `roof_window_gothic_wide` — 16×16 — palette `BHRWry`
- `roof_railing_straight` — 16×16 — palette `S`
- `roof_railing_end_l` — 16×16 — palette `S`
- `roof_railing_end_r` — 16×16 — palette `S`
- `roof_spire_base` — 16×16 — palette `BHR`
- `roof_spire_mid` — 16×16 — palette `BHR`
- `roof_spire_cap` — 16×16 — palette `BHR`
- `roof_chimney_stack` — 16×16 — palette `BH`
- `roof_finial_cross` — 16×16 — palette `BSa`
- `roof_gargoyle_left` — 16×16 — palette `BHS`
- `roof_gargoyle_right` — 16×16 — palette `BHS`
- `roof_lantern_hanging` — 16×16 — palette `RWruy`
- `roof_lantern_wall` — 16×16 — palette `HRSWruy`
- `gate_arch_top` — 16×16 — palette `BH`
- `gate_bar_panel` — 16×16 — palette `S`
- `gate_pillar` — 16×16 — palette `BH`
- `gate_pillar_cap` — 16×16 — palette `BH`
- `gate_fence_section` — 16×16 — palette `S`
- `gate_fence_finial` — 16×16 — palette `S`
- `gate_approach_stone` — 16×16 — palette `BH`
- `gate_approach_transition` — 16×16 — palette `BHSa`
- `mansion_ext_wall_panel` — 16×16 — palette `BH`
- `mansion_ext_window_tall` — 16×16 — palette `BHRWry`
- `mansion_ext_buttress` — 16×16 — palette `BH`
- `mansion_ext_balcony_floor` — 16×16 — palette `BHS`
- `mansion_ext_chimney_tall` — 16×16 — palette `BH`
- `mansion_ext_lantern_window` — 16×16 — palette `RWruy`
- `mansion_ext_roofline_trim` — 16×16 — palette `BHRx`
- `mansion_ext_skyline_spires_a` — 16×16 — palette `BHhn`
- `mansion_ext_skyline_spires_b` — 16×16 — palette `BHhn`
- `roof_scarlet_moon_64` — 64×64 — palette `FRrxz`


## Palette inventory
- `B` = `#2a3160` — 2965 authored pixels
- `F` = `#e08a72` — 132 authored pixels
- `H` = `#2c2438` — 900 authored pixels
- `R` = `#9a2438` — 841 authored pixels
- `S` = `#8a8aa0` — 715 authored pixels
- `W` = `#d4c4a8` — 128 authored pixels
- `a` = `#a9a4b6` — 178 authored pixels
- `b` = `#424d9d` — 60 authored pixels
- `h` = `#191528` — 53 authored pixels
- `n` = `#171b39` — 62 authored pixels
- `r` = `#e83a51` — 1909 authored pixels
- `u` = `#704638` — 26 authored pixels
- `x` = `#87243b` — 586 authored pixels
- `y` = `#ffe08a` — 126 authored pixels
- `z` = `#ffd0e0` — 13 authored pixels


## Files

- `roof_tiles.json`, `roof_structures_a.json`, `roof_structures_b.json` — exact roof-family matrices.
- `gate_assets.json` — exact gate-family matrices.
- `mansion_ext_assets.json` — exact mansion-exterior matrices.
- `roof_scarlet_moon.json` — exact approved scarlet moon carry-forward matrix.
- `palette.json` — exact existing-game palette key mapping used by this package.
- `render_stage3b_preview.py` — deterministic nearest-neighbor atlas/composition renderer.
- `MANIFEST.json` — file summary and package metadata.
- `VALIDATION.txt` — dimension / prefix / character / composition validation.
- `stage3b_roof_atlas.png` — enlarged nearest-neighbor atlas rendered directly from the matrices.
- `stage3b_roof_playfield_preview.png` — enlarged 192×240 composition proof for a Remilia-boss readability configuration.
- `stage3b_roof_playfield_native.png` — native-size 192×240 composition proof.

## Validation result

- Matrices: **PASS**
- Required prefixes (`roof_`, `gate_`, `mansion_ext_`): **PASS**
- Allowed characters: **PASS**
- Palette extension: **NONE**
- Remilia-boss readability composition proof: **PASS**
  - upper spectacle mean luminance: 44.17
  - lower-center survival zone mean luminance: 16.08
  - lower-edge detail mean luminance: 22.70

The playfield proof is deliberately conservative in the late-boss lower playfield: architecture and bright light sources are concentrated high and toward the side columns.
