# Marisa Kirisame — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is narrowly selected pose/silhouette/state vocabulary only. The committed Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved V4 sheet: [`image-gen-3(5).png`](../design-sheets/image-gen-3(5).png)
- Repository path: `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-3(5).png`
- Dimensions: **1122×1402**
- File size: **2265744 bytes**
- SHA-256: `b36b542d012b3d1a89198ae43d2feda0c9502bfc1e5b686c6807a355dbd20003`

![Owner-approved V4 Marisa Kirisame design sheet](../design-sheets/image-gen-3(5).png)

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `marisa` | 32×32 | Boss, dialogue, defeat, attract and flying credits | Idle A | Reusable body/broom family | Body and broom are authored together in the current sprite; preserve actual boss/dialogue/credit staging. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L469) |
| `marisaB` | 32×32 | Same body-family uses | Idle B | Reusable body/broom family | Current alternate-frame silhouette loss is a defect to avoid; keep stable body/hat/broom scale. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L503) |
| `marisaAttack` | 32×32 | Boss phases m3/m4 | Attack / high-power state | Reusable special body pose | Selector semantics remain fixed; make the attack visibly distinct without enlarging body. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L537) |
| `p_marisa` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1080) |
| `dialogue book (procedural current presentation)` | ≈12×16 visible envelope | Marisa dialogue only, drawn separately near current book staging | Book prop / presentation cue | Presentation-specific separate concern | Not a SPRITES definition; keep separate from reusable body/broom and do not invent extra character states. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2040) |

## 2. Current Scarlet Moon evidence

- Current body definitions: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L469, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L503, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L537; portrait https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1080; selector https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775.
- Dialogue body/book staging: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2040; attract https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2077; flying credits https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2092; defeat reuse https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2111.
- Reconnaissance identifies body/broom continuity across all those uses; the dialogue book remains a separate presentation concern.
- Full source-rendered reconnaissance/frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Selected official Touhou production references

1. **TH07 Perfect Cherry Blossom — Characters sheet**
   - Exact reference: https://www.spriters-resource.com/pc_computer/touhouyouyoumuperfectcherryblossom/sheet/44412/
   - Inspect: Inspect Marisa's playable player-sprite group, especially witch-hat width, broom relationship and rear/flight silhouette.
   - Teaches: How hat, blonde head mass, dark/light costume and broom remain readable at shooter scale.
   - Do not copy: Do not copy frame clusters, broom angle or animation timing as Scarlet Moon requirements.
2. **TH08 Imperishable Night — Playable Characters sheet**
   - Exact reference: https://www.spriters-resource.com/pc_computer/touhoueiyashouimperishablenight/asset/34544/page-1/
   - Inspect: Inspect Marisa's playable back-sprite group for a second shooter-generation hat/broom/body-scale check.
   - Teaches: Useful continuity reference for compact witch/broom silhouette and stable player footprint.
   - Do not copy: Do not import TH08 canvas, mechanics or exact pixels.
3. **TH06 Embodiment of Scarlet Devil — Marisa official artwork file**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06Marisa.png
   - Inspect: Inspect only for early official face, hat/bow and black/white costume cues relevant to portrait identity.
   - Teaches: Portrait-scale identity vocabulary that can be reconciled with the accepted V4 sheet.
   - Do not copy: Do not downscale it or let artwork detail override the 32×32 body contract.

These references are deliberately small and specific. They tell the later artist **which sheet/file/state to inspect**. Third-party sprite sheets remain external link/metadata only and are not copied into this repository.

## 4. Owner-approved V4 design sheet

- Huge dark witch hat with broad brim/floppy crown and a large white bow; long blonde hair.
- Dark navy/black witch dress with white apron/frill and small blue chest accents.
- Broom is a primary identity object; gold star ornaments are secondary decoration.
- At 32×32 preserve hat+broom+blonde-hair silhouette first; reduce dangling star/frill ornament before changing apparent body scale.

The committed sheet is the exact Owner-approved design authority identified by path, dimensions and SHA-256 above. It is not an exact pose blueprint; incidental generated labels or decorative details that conflict with actual character identity or the live Scarlet Moon contract remain non-authoritative.

## 5. Translation notes

- Hold one 32×32 apparent body scale across idle A/B and attack; hat and broom may change pose but must not make Marisa look like a different-sized actor.
- Prioritize hat silhouette, blonde hair mass, dark/light costume split and broom. Star ornaments are expendable at native scale.
- Use the selected TH07/TH08 player sheets to study compact hat/broom flight vocabulary, not as literal templates.
- Treat the dialogue book as independently anchored presentation art if redrawn; do not bake it into the reusable body.

**Translation equation:** Scarlet Moon state contract + selected official Touhou vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.

## 6. Production-brief seed

> Author Marisa's complete V4 family: marisa, marisaB, marisaAttack and p_marisa, while keeping the dialogue book a separate presentation concern. Preserve 32×32 state semantics and current m3/m4 trigger. Inspect the selected TH07/TH08 playable-sprite groups for hat/broom/flight vocabulary; use the committed approved V4 sheet for appearance. Maintain stable body scale and no runtime changes.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
