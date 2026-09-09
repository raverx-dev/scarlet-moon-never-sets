# Environment construction (as implemented)

All four stage environments are **precomposed once at load** onto an offscreen canvas, then blitted. None of `drawMistyLake` / `drawForest` / `drawInterior` / `drawRoof` use the `t` scroll argument. **All four gameplay fields are static.** V2’s corresponding functions scrolled with `t` and painted to the passed `w`.

Runtime blit:

```
ctx.drawImage(SHEET, 0, 0, w, 240, 0, 0, w, 240)
```

- Gameplay: `w=192`, then HUD at x=192.
- Dialogue / attract teasers / stage cards / gate / defeat / dawn-anchor: `w=256`.

Sheets are 256×240. What is *painted* into them differs.

## Stage 1 — Misty Lake

- **Construction:** IIFE `LAKE` stamps 8×8 water cycles and authored 8×8 / 16×16 props onto `LAKE.sheet`.
- **Proof:** `dev/art/v3_stage1_misty_lake/lake_playfield_composition.js` is **192×240**, center lane x=48–143.
- **Runtime vs proof:** Water tiles loop `tx < 256`. Props stay at the 192 proof positions (max x≈176). HUD column is extra edge-cycle water, no extra reeds.
- **Scrolling:** no.
- **Size:** 256-wide sheet; gameplay shows 192; dialogue/attract/stagecard show 256 (more water).
- **Why it looks cohesive:** Dark center water, edge reeds/lanterns/ice, no HUD-column props fighting the composition. A 256 lake frame is still “lake.”

## Stage 2 — Forest of Magic

- **Construction:** IIFE `FOREST` path-tiles the full 256, then canopy/trunks/mushrooms/lanterns. Non-path pixels in x=56–135 are skipped (center lane stays dark).
- **Proof:** `forest_playfield_composition.js` is **192×240**, trunks at 0 and 176 only.
- **Runtime vs proof:** Extra pines/canopy/trunks/mushrooms at x=192, 208, 224, 240.
- **Scrolling:** no.
- **Size:** 256 sheet; gameplay 192 (HUD hides the extra column); dialogue/attract/stagecard show the third tree.
- **Why it looks more like a tile collage than the lake:** 16×16 canopy is a visible grid; lanterns and mushrooms are regular. Still reads as a forest. The 256 extra column is what breaks story/card frames (F03).

## Stage 3A — Mansion interior

- **Construction:** IIFE `MANSION` `tile_rect` + `place` copied from `mansion_composition.js`.
- **Proof:** **width 192**, HUD excluded. Quiet lane x=64–127.
- **Runtime vs proof:** Same operations. `paint()` **discards x≥192**. HUD column of the sheet is uninitialized black (`C.black` fill).
- **Scrolling:** no. V2 interior scrolled wallpaper/chandelier.
- **Size:** 256 canvas, **192 content**. Gameplay is correct. Any `w=256` interior draw is F01.
- **Why it looks busier than the lake:** Repeating 8×8 damask, stacked 16×16 furniture in the side bays. As a *gameplay corridor* it is a valid SDM hallway. As a *dialogue room* it is a cropped playfield.

## Stage 3B — Gate / roof / Remilia

- **Construction:** IIFE `ROOF` gradient sky + moon + skyline/battlements/spires/gate props, then a translucent black rect `(48,156,96,84)` and a short cobble strip.
- **Proof:** `render_stage3b_preview.py` is **192×240** with lower-center luminance kept below the edges (R5).
- **Runtime vs proof:** Same 192 layout plus HUD-column skyline/battlements/spires/`gate_approach_stone` at x≥192.
- **Scrolling:** no.
- **Size:** 256 content (HUD column has architecture). Gameplay 192. Gate/dialogue/attract/stagecard 256.
- **Why gate/dialogue feel empty:** The 192 proof’s lower-center hole is the story floor. V2 painted a walkway on top for gate and stood dialogue actors on the battlement. V3 did not (F02, F04).

## Shrine (not a stage sheet)

`shrine(morning, t, w=256)` stamps live every frame (hills, grass, 2× torii on story scenes, `shrineHall`). Title has its own lighter composition (native torii, small hall). Intro/ending/notice/ending-arrival use this path. **This is the only story background that is actually authored at 256.** That is why intro/ending still feel like staged scenes.

## Leftover V2 primitives still called

| Function | Still used |
|---|---|
| `roof(y,w)` | `drawCredits()` floor |
| `iceCase()` | Cirno credits gag |
| `moon()` | defined; shrine/title/final use stamped `moon_scarlet_64` instead |
| Marisa book `rect`s | Marisa dialogue |

## Who reuses which sheet at 256

| Caller | Sheet | w |
|---|---|---|
| `drawPlay` | stage 1/2/3A or 3B | 192 |
| Cirno / Marisa / Sakuya dialogue | stage sheet, `sceneKind=''` | 256 |
| Remilia dialogue | roof (`sceneKind='roof'`) | 256 |
| Intro / ending | shrine / morning | 256 |
| Attract q=0,1 | lake / forest | 256 |
| Attract q=2 | roof + Sakuya | 256 |
| Stage cards | lake / forest / roof (stage 3 is roof, not interior) | 256 |
| Gate | roof | 256 |
| Defeat | stage sheet; remilia → roof | 256 |
| Dawn tick&lt;190 | roof | 256 |
