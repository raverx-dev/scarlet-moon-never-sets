# Version 3 Stage 3A — Scarlet Devil Mansion Interior Art

Art-only package for `raverx-dev/scarlet-moon-never-sets`, authored for GitHub issue #16 against the owner-approved `scarlet_moon_mansion_nes_stage_concept_board.png` direction.

- Base checkpoint: `69d06766c0a6c165f26f71ded96d7b5bd8a122df`
- Branch: `v3-art-stage3a-mansion`
- Logical game canvas: 256×240
- Stage playfield proof: 192×240 (HUD excluded)
- Scope: Scarlet Devil Mansion interior environment only
- Runtime integration: none
- Character / bullet / item / UI changes: none
- Palette extension request: **none**

## Exact deterministic source

The canonical matrices are explicit native-size rows in these files:

- `mansion_assets_8x8.js`
- `mansion_assets_arch16.js`
- `mansion_assets_furnish16.js`
- `mansion_chandelier.js`
- `mansion_assets.js` — aggregate export only

Every asset name begins with `mansion_`. `.` is transparency. Every other character is an existing checkpoint `PAL` key.

`mansion_composition.js` is the deterministic recipe used for the 192×240 proof. Its operations are only `tile_rect` and `place` references to the exact matrices. The proof does not import or draw any independent scene art.

## Asset inventory

### 8×8 wall / carpet / floor / trim

| Asset | Size |
|---|---:|
| `mansion_wall_plain` | 8×8 |
| `mansion_wall_damask_a` | 8×8 |
| `mansion_wall_damask_b` | 8×8 |
| `mansion_wall_panel` | 8×8 |
| `mansion_carpet_center` | 8×8 |
| `mansion_carpet_motif` | 8×8 |
| `mansion_carpet_edge_l` | 8×8 |
| `mansion_carpet_edge_r` | 8×8 |
| `mansion_floor_wood` | 8×8 |
| `mansion_floor_stone` | 8×8 |
| `mansion_molding_horizontal` | 8×8 |
| `mansion_trim_vertical` | 8×8 |
| `mansion_masonry_shadow` | 8×8 |

### 16×16 architecture

| Asset | Size |
|---|---:|
| `mansion_window_gothic_a` | 16×16 |
| `mansion_window_gothic_b` | 16×16 |
| `mansion_sconce_single` | 16×16 |
| `mansion_sconce_double` | 16×16 |
| `mansion_pillar_cap` | 16×16 |
| `mansion_pillar_mid` | 16×16 |
| `mansion_pillar_base` | 16×16 |
| `mansion_railing` | 16×16 |
| `mansion_door_arch_l` | 16×16 |
| `mansion_door_arch_r` | 16×16 |
| `mansion_door_side_l` | 16×16 |
| `mansion_door_side_r` | 16×16 |
| `mansion_door_panel` | 16×16 |
| `mansion_corridor_shadow` | 16×16 |
| `mansion_corridor_threshold` | 16×16 |

### 16×16 furnishing / accents

| Asset | Size |
|---|---:|
| `mansion_painting_frame` | 16×16 |
| `mansion_bookcase` | 16×16 |
| `mansion_side_table` | 16×16 |
| `mansion_vase_flowers` | 16×16 |
| `mansion_bust_statue` | 16×16 |
| `mansion_drape_banner` | 16×16 |

### Larger prop

| Asset | Size |
|---|---:|
| `mansion_chandelier` | 32×24 |

Total: **35 exact assets**.

## Palette inventory

Exact package usage:

`B H R S W a b d e g h k l n o r s t u x y`

The validator reads the live checkpoint `PAL` keys from `index.html` and rejects any source character outside that set plus `.`.

## Danmaku composition rule

The proof reserves x=64..127 as the principal quiet bullet lane. Rich wallpaper, windows, sconces, chandeliers, paintings, railings, bookcases, busts, flowers, and most bright gold highlights stay toward the side architecture or scene boundaries.

Measured on the proof before the lower doorway boundary (y<208):

- central bright-pixel density: `0.000000`
- side-zone bright-pixel density: `0.114633`
- central edge density: `0.130843`
- side-zone edge density: `0.435491`

The center is therefore materially darker and less visually busy than the sides.

## Preview / proof

- `mansion_asset_atlas.png` — enlarged 4× nearest-neighbor atlas rendered from the exact matrices.
- `mansion_asset_atlas_map.txt` — row/column mapping for the unlabeled atlas.
- `mansion_composition_proof_192x240.png` — exact native 192×240 vertical-danmaku composition proof made only from the matrix family.

## Validation

Run:

```bash
node dev/art/v3_stage3a_mansion/mansion_validate.js
```

The validator checks:

- `mansion_` prefixes;
- exact declared height and row widths;
- allowed `PAL` characters;
- exact 192×240 composition dimensions;
- composition references only existing assets;
- PNG dimensions for the proof and enlarged atlas.

The committed `VALIDATION.txt` is the passing report.

## Integration boundary

This branch is an art-source handoff only. `index.html` is intentionally untouched. A later mechanical integration pass may copy these exact matrices into runtime tile structures, but should not redraw or reinterpret them.
