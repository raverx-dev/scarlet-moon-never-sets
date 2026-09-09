# Version 3 Stage 3A — Scarlet Devil Mansion Interior Art Package

Scope: **environment art only** for the 192×240 vertical playfield. Based directly on issue #16 V3 checkpoint `69d06766c0a6c165f26f71ded96d7b5bd8a122df`.

## Canonical exact source

`v3_stage3a_mansion_assets.js` is the canonical deterministic matrix/tile source. All authored asset names are `mansion_` prefixed. Every visible matrix character is an existing game `PAL` key and `.` is transparency.

**PALETTE EXTENSION REQUEST: none.**

Package palette inventory: `B G H R S W b d g h i n p r t u x y`

## Assets

| Asset | Exact size | Intended use |
|---|---:|---|
| `mansion_wall_dark_a` | 8×8 | quiet central/side wall base; alternate to suppress visible tiling |
| `mansion_wall_dark_b` | 8×8 | quiet wall variant; alternate with mansion_wall_dark_a |
| `mansion_wallpaper_damask` | 8×8 | side-zone ornament only; do not blanket central bullet lane |
| `mansion_carpet_dark_a` | 8×8 | central lane base; deliberately low contrast |
| `mansion_carpet_dark_b` | 8×8 | central lane alternate; low contrast |
| `mansion_carpet_border` | 8×8 | repeat vertically at lane edge; gold only on outermost seam |
| `mansion_wood_panel` | 8×8 | side paneling/furnishing fill |
| `mansion_stone_molding` | 8×8 | horizontal architectural divider; side or scene boundary |
| `mansion_gold_trim` | 8×8 | small side-zone trim/accent; avoid dense central use |
| `mansion_floor_shadow` | 8×8 | dark transition/floor shadow tile |
| `mansion_gothic_window` | 16×16 | outer side walls; cool blue contrast against dark red interior |
| `mansion_gothic_window_dim` | 16×16 | alternate/distant window for lower contrast |
| `mansion_wall_sconce` | 16×16 | side wall highlight; keep out of central bullet lane |
| `mansion_column` | 16×16 | side-zone structural separator |
| `mansion_railing` | 16×16 | repeat along side balconies/scene boundaries |
| `mansion_painting` | 16×16 | side-wall furnishing; abstract scarlet motif |
| `mansion_bookcase` | 16×16 | side-wall bookcase/detail block |
| `mansion_cabinet` | 16×16 | side-zone cabinet/chest |
| `mansion_door_arch_left` | 16×16 | pair with mansion_door_arch_right at corridor boundary |
| `mansion_door_arch_right` | 16×16 | pair with mansion_door_arch_left at corridor boundary |
| `mansion_door_jamb` | 16×16 | vertical doorway continuation/side return |
| `mansion_corridor_edge_left` | 16×16 | scene-boundary taper/side corridor transition |
| `mansion_corridor_edge_right` | 16×16 | mirrored scene-boundary taper |
| `mansion_flower_vase` | 16×16 | optional side furnishing; restrained floral accent |
| `mansion_statue_bust` | 16×16 | optional side architectural accent |
| `mansion_chandelier` | 32×24 | top/scene-boundary focal prop; avoid sustained central-lane occupation |

## Vertical-danmaku composition proof

The canonical source also contains the deterministic `compositionProof` recipe. The native proof is exactly **192×240**. Its visible pixels are produced only by stamping/repeating exact `mansion_*` matrices; no environment rectangles, lines, gradients, resampling, antialiasing, characters, bullets, items, or UI are drawn into it.

The quiet central bullet lane is x=48..143. Dark carpet variants occupy that band; architectural detail is concentrated in x=0..39 and x=152..191, with 8-pixel carpet borders between them. The chandelier is restricted to the top scene boundary.

Review files:

- `mansion_asset_atlas.png` — exact matrices arranged into an atlas and enlarged **4× nearest-neighbor** by literal pixel duplication.
- `mansion_composition_proof_192x240.png` — exact native-size vertical-danmaku proof generated from the embedded composition recipe.

## Validation

`VALIDATION.txt` records the passed dimension, prefix, duplicate-name, allowed-character, composition-reference, proof-size, and palette checks, plus SHA-256 hashes for the committed source and preview images.

## Non-goals

No Reimu, Sakuya, Remilia, fairy, portrait, bullet, item, UI, gameplay, or runtime integration changes are included. `index.html` remains untouched.
