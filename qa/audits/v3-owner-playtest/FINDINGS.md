# Findings

Five findings. Scene-by-scene notes that are **fine** live in `REPORT.md` section 6.

Classification: **A** real regression · **B** composition/placement · **C** inconsistent presentation · **D** acceptable V3 change · **E** optional polish.

---

## F01 — P1 — A — Sakuya interior dialogue black gutter

**Scene:** `dialogue:sakuya_before`, `dialogue:sakuya_after`. Same sheet is also what a full-width interior defeat frame would show.

**V3 behavior:** The mansion interior is a precomposed 256×240 offscreen sheet whose painter **drops every pixel with x ≥ 192**. `drawDialogue()` then blits that sheet at **width 256**. The right 64 px is `C.black`. The opposing character is `sprite(other, 196, 108, 1)`, which sits in that void. Sakuya is half off the architecture, standing in empty black.

Measured on `sakuya-dialogue.png` (logical x≥192, character band y=80–170): **94.8% near-black**.

**V2/reference:** `drawInterior(t, w)` painted to whatever `w` was passed. Dialogue used `w=256`, so carpet, pillars, windows, and chandelier were composed across the full screen. Sakuya at x=196 stood in front of windows, not in a gutter.

**Evidence:**
- `evidence/v3/sakuya-dialogue.png`
- `evidence/v3/sakuya-after.png`
- `evidence/compare/sakuya-dialogue.png`
- `evidence/analysis/gutter_v3.csv`

**Likely technical cause:** Art package `mansion_composition.js` is explicitly `width: 192` (HUD excluded). Integration copied that recipe and kept `if (x < 0 || x >= 192) continue` in `MANSION.paint`. Gameplay (`w=192` + HUD) is correct. Full-width story presentation was not given a 256 composition. Character x=196 is the old V2 256-wide slot.

**Recommended MINIMAL correction:**
1. For full-width interior draws only, fill x=192–255 from existing `mansion_*` tiles (repeat the right damask/pillar bay; do not invent new art).
2. Move the opposing dialogue actor left onto architecture (about x=168), not x=196.
3. Do not change the 192 gameplay clip + HUD contract.

**Asset redesign required?** NO.

---

## F02 — P1 — A — Gate / Remilia story scenes lost the walkway

**Scene:** `gate`, `dialogue:remilia_before`, `dialogue:remilia_after`, `attract-sakuya`, `stagecard-3`, `dawn` tick 90 backdrop.

**V3 behavior:** One roof sheet serves Remilia-boss readability **and** every roof story frame. The 192 proof deliberately keeps the lower-center survival lane empty (issue #16). That emptiness is then shown full-width. Reimu walks through black on the gate scene; Remilia dialogue plants both characters in the empty lower field / in the railing; attract Sakuya stands in the battlement.

**V2/reference:** `drawRoof` plus, on the gate, an extra full-width ground (`rect(0,150,256,90,'#1a1830')` and a walkway band). Remilia dialogue stood both characters **on** the battlement with a building facade under their feet. Attract-sakuya showed the roof with no character (V3 adding Sakuya is fine; putting her in the fence is not).

**Evidence:**
- `evidence/v3/gate.png`
- `evidence/v3/remilia-dialogue.png`
- `evidence/v3/attract-sakuya.png`
- `evidence/compare/gate.png`
- `evidence/compare/remilia-dialogue.png`
- `evidence/compare/attract-sakuya.png`

**Likely technical cause:** `ROOF` is assembled once from the 192 Remilia-boss proof, then extra HUD-column architecture is stamped at x≥192. `background(..., 256, 'roof')` is shared by gate, remilia dialogue, attract q=2, and the stage 3 card. Boss play uses `w=192` and `dimField`; R5 still correctly blacks y≥80 after 25s. The story path never restored a floor.

**Recommended MINIMAL correction:**
- Keep R5 / boss-play lower-field suppression unchanged.
- When `w===256` and the roof sheet is shown (gate, remilia dialogue, attract, stagecard), stamp a full-width walkway from existing `roof_cobble_*` / `gate_approach_stone` / railing tiles under the character foot line.
- Place gate Reimu/Meiling and Remilia-dialogue actors on that band.
- Attract Sakuya: stand her on the walkway, not in the fence.

**Asset redesign required?** NO.

---

## F03 — P1 — B — Marisa dialogue overlap + 256 forest extension

**Scene:** `dialogue:marisa_before`, `dialogue:marisa_after`, `stagecard-2`, `attract-marisa`.

**V3 behavior:** Forest proof is 192×240 with trunks at x=0 and x=176. Runtime also stamps pines/canopy/trunks at x=192, 208, 224, 240. Dialogue blits the sheet at 256. Marisa is still at x=196, so she sits on the playfield-edge trunk. The leftover programmer-art grimoire (`rect` gold/red book at 168,118) sits on the same trunk. The Stage 2 card is left-heavy / right-heavy: one trunk on the left, two on the right.

**V2/reference:** Trees on the far left and far right of 256. Marisa stood in open sky with broom and book, not inside a trunk.

**Evidence:**
- `evidence/v3/marisa-dialogue.png`
- `evidence/v3/marisa-after.png`
- `evidence/v3/stagecard-2.png`
- `evidence/compare/marisa-dialogue.png`
- `evidence/compare/stagecard-2.png`

**Likely technical cause:** Integration extended the 192 forest proof into the HUD column so 256-wide frames would not be empty. Character coordinates were not updated. `forest_playfield_composition.js` never placed trunks past x=176.

**Recommended MINIMAL correction:**
1. Stop stamping forest decorations at x≥192 (return to the 192 proof). Path-lane fill into the HUD column can stay dark.
2. For Marisa dialogue, move the opposing actor off the x=176 trunk (path, ~x=152) and move or hide the rect grimoire. Authored grimoire art is issue #16 later work; do not block freeze on a new asset.

**Asset redesign required?** NO.

---

## F04 — P2 — B — Roof/gate architecture reads as scattered stamps

**Scene:** Gate, roof gameplay (`stage3-roof`), Remilia dialogue, Stage 3 card.

**V3 behavior:** Individual assets are valid. Assembled, `gate_arch_top` at (72,128) reads as a small oval hole, `gate_bar_panel` as a barcode, fence segments float in the lower black, cobbles are a short center strip. It does not read as “the mansion gate / roof” the way V2’s towers + facade + walkway did.

This is **not** “tiles are bad.” It is this particular stamp layout on a sheet that was authored for R5 emptiness.

**V2/reference:** Naive but spatially complete: two towers, continuous battlement, building face, walkway.

**Evidence:**
- `evidence/v3/gate.png`
- `evidence/v3/stage3-roof.png`
- `evidence/v3/stagecard-3.png`
- `evidence/compare/gate.png`
- `evidence/compare/stage3-roof.png`

**Likely technical cause:** `ROOF` operations copy the 192 proof plus HUD-column extras. Several 16×16 props (`gate_arch_top`, bar panels, gargoyles) are placed without a connecting wall/floor mass except the intentional lower-center hole.

**Recommended MINIMAL correction:** After F02’s walkway, regroup the gate bars/arch on that band so the oval and barcode sit in a wall rather than in empty space. Prefer existing `mansion_ext_wall_panel` / `gate_pillar` / `gate_bar_panel` restacking over new pixels.

**Asset redesign required?** NO for a freeze-pass regroup. New gate-arch art only if restacking still fails to read as a gate.

---

## F05 — P2 — C — Credits still use leftover V2 `roof()` + `iceCase`

**Scene:** `credits` parts 0–5 (floor). Cirno ice-case gag. Reimu/coin/donation.

**V3 behavior:** New character sprites and the V3 donation box stand on the old procedural `roof(181, 256)` battlement. Cirno is still in the primitive `iceCase()` frame. Same gag as V2, now next to Version 3 art.

**V2/reference:** Identical floor and ice case (with the old sprites). Not a lost V2 behavior. It is an incomplete V3 presentation pass.

**Evidence:**
- `evidence/v3/credits-cirno.png`
- `evidence/v3/credits-reimu.png`
- `evidence/compare/credits-cirno.png`

**Likely technical cause:** `drawCredits()` still calls leftover `roof()` / `iceCase()`. Issue #16 listed the ice-case frame as a later small prop. The floor was never switched to shrine/roof tiles.

**Recommended MINIMAL correction:** Replace `roof(181,256)` with a strip of existing roof cobble/battlement or shrine ground tiles. Keep Cirno ice-case as scheduled #16 art unless a 1-hour tile-frame substitute is wanted.

**Asset redesign required?** NO for the floor. Ice-case frame: NO to freeze V3 if the floor is fixed; YES later per #16.

---

## Explicitly not raised as freeze findings

| Observation | Why it is not a finding |
|---|---|
| Cirno dialogue uses the lake gameplay sheet | Same V2 *policy*; V3 lake fills 256 and still reads as Misty Lake. Lost moon/horizon is a D, documented in `COMPARISON.md`. |
| Mansion interior *gameplay* looks stamp-dense | It still reads as an SDM hallway; HUD clip is correct. Noted as P3 in placement review. |
| Forest 16×16 canopy repeat | Reads as a forest; center lane is dark. P3. |
| Intro / ending / title / HUD / How / Continue | Coherent V3 upgrades (D). |
| R5 lower-field black | Specified and working. |
| Master Spark | Readable against the forest. |
| EMPTY BOX SOFT | Issue #15, out of this pass. |
| Lunar-anchor `nesBox`+disk | Scheduled #16 small prop; backdrop issue is F02. |
| Marisa grimoire rects | Folded into F03; authored asset is later #16. |
