# Version 3 Global UI Chrome — Art Package

Governing spec: GitHub issue #16, Workstream A / GLOBAL UI CHROME ONLY.

Baseline PAL: accepted `sprite-redesign` checkpoint `69d06766c0a6c165f26f71ded96d7b5bd8a122df`.

No runtime integration is included. No palette extension is requested. `.` means transparency.

## Assets

| Asset | Dimensions | PAL keys used | Intended use |
|---|---:|---|---|
| `ui_frame_corner_tl` | 8×8 | `Rgr` | Shared 8×8 frame-language building block for Pause / How To Play / Continue. |
| `ui_frame_corner_tr` | 8×8 | `Rgr` | Shared 8×8 frame-language building block for Pause / How To Play / Continue. |
| `ui_frame_corner_bl` | 8×8 | `Rgr` | Shared 8×8 frame-language building block for Pause / How To Play / Continue. |
| `ui_frame_corner_br` | 8×8 | `Rgr` | Shared 8×8 frame-language building block for Pause / How To Play / Continue. |
| `ui_frame_edge_top` | 8×8 | `Rr` | Shared 8×8 frame-language building block for Pause / How To Play / Continue. |
| `ui_frame_edge_bottom` | 8×8 | `Rr` | Shared 8×8 frame-language building block for Pause / How To Play / Continue. |
| `ui_frame_edge_left` | 8×8 | `Rr` | Shared 8×8 frame-language building block for Pause / How To Play / Continue. |
| `ui_frame_edge_right` | 8×8 | `Rr` | Shared 8×8 frame-language building block for Pause / How To Play / Continue. |
| `ui_frame_title_tab` | 32×8 | `Rgr` | 32×8 header accent for Pause / How To Play / Continue. |
| `ui_hud_divider` | 56×8 | `HRgr` | Reusable 56×8 section divider used by the HUD panel. |
| `ui_hud_panel` | 64×240 | `BHRgkr` | Complete 64×240 HUD/sidebar chrome for x=192..255; content overlays remain unchanged. |
| `ui_life_icon` | 8×8 | `Rrw` | 8×8 life indicator treatment. |
| `ui_bomb_icon` | 8×8 | `Rgrw` | 8×8 Fantasy-Seal/bomb indicator. |
| `ui_power_cell_on` | 8×8 | `gry` | 8×8 filled power cell. |
| `ui_power_cell_off` | 8×8 | `BHh` | 8×8 empty power cell. |
| `ui_stage_thumb_lake` | 16×16 | `BCabcik` | 16×16 Misty Lake stage thumbnail. |
| `ui_stage_thumb_forest` | 16×16 | `Gektuv` | 16×16 Forest of Magic stage thumbnail. |
| `ui_stage_thumb_mansion` | 16×16 | `BHkrx` | 16×16 Scarlet Devil Mansion stage thumbnail. |
| `ui_dialogue_frame` | 248×62 | `HRgkr` | Exact 248×62 bottom-dialogue panel frame/fill; current intended placement x=4,y=174. |
| `ui_portrait_bezel` | 40×40 | `Rgrw` | 40×40 bezel with a transparent 32×32 portrait opening at local x=4..35,y=4..35. |

## Layout notes

- `ui_hud_panel` is exactly 64×240 and stays inside the HUD contract. Panel-local x=0 maps to screen x=192.
- HUD divider rhythm is at panel-local y=56, 114, 145, 174, and 228; the existing SCORE / HI-SCORE / LIVES / BOMBS / POWER / GRAZE / STAGE / mute information contract remains unchanged.
- HUD stage-thumbnail bracket occupies panel-local x=21..42, y=204..225. Place a 16×16 thumbnail at local x=23,y=206.
- `ui_dialogue_frame` is exactly 248×62 and is intended for the existing x=4,y=174 dialogue box.
- `ui_portrait_bezel` is 40×40 with an exact 32×32 transparent opening.
- Shared menu chrome is tile-based: four 8×8 corners, four 8×8 edges, plus a 32×8 title tab. Fill the interior with PAL `k` and repeat/crop edge tiles mechanically to the existing menu dimensions.

## Validation

- Every row width equals its declared matrix width.
- Every matrix height equals its declared height.
- Every non-transparent character is an existing PAL key.
- Result: **PASS**.

`ui_preview.html` renders the exact matrices directly from `ui_assets.js` at integer nearest-neighbor scale. The owner-review package also includes a generated PNG preview from the same matrices.
