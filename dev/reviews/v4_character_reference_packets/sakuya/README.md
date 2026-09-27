# Sakuya Izayoi — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is narrowly selected pose/silhouette/state vocabulary only. The committed Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved V4 sheet: [`image-gen-5(3).png`](../design-sheets/image-gen-5(3).png)
- Repository path: `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-5(3).png`
- Dimensions: **1122×1402**
- File size: **2195028 bytes**
- SHA-256: `4b743abd1410b4f7b1154855349509d19f53b8485fcc4ebc30767748520e332a`

![Owner-approved V4 Sakuya Izayoi design sheet](../design-sheets/image-gen-5(3).png)

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `sakuya` | 32×32 | Boss, dialogue, defeat, attract and credits | Idle A | Reusable body family | Standard boss/dialogue family; preserve actual placement semantics. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L571) |
| `sakuyaB` | 32×32 | Same body-family uses | Idle B | Reusable body family | Keep same apparent height/width and maid silhouette as idle A. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L605) |
| `sakuyaStop` | 32×32 | Frozen-bullet/time-stop condition; timed credits vignette | Time-stop special pose | Reusable special body pose | State selector is fixed; knife/clock/projectile effects remain separate presentation systems. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L639) |
| `p_sakuya` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1114) |

## 2. Current Scarlet Moon evidence

- Current definitions: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L571, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L605, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L639; portrait https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1114; stop selector https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775.
- Dialogue: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2040; attract https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2078; credits time-stop vignette https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2094; defeat exit https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2111.
- Reconnaissance keeps body/stop/portrait separate from knife/clock presentation effects.
- Full source-rendered reconnaissance/frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Selected official Touhou production references

1. **TH06 Embodiment of Scarlet Devil — Sakuya isolated boss sprite**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06SakuyaSprite.png
   - Inspect: Inspect the isolated official Stage 5 boss sprite for maid silhouette, silver-hair head mass and compact arm/knife read.
   - Teaches: Small official boss-scale evidence for Sakuya's recognizable body proportions.
   - Do not copy: Do not trace pixels or use its canvas/pose as a mandatory Scarlet Moon frame.
2. **TH07 Perfect Cherry Blossom — Characters sheet**
   - Exact reference: https://www.spriters-resource.com/pc_computer/touhouyouyoumuperfectcherryblossom/sheet/44412/
   - Inspect: Inspect Sakuya's playable player-sprite group for compact rear/flight silhouette and maid/headdress continuity.
   - Teaches: Shooter-scale economy for silver hair, headdress and navy/white maid massing.
   - Do not copy: Do not import player mechanics, exact animation or frame clusters.
3. **TH7.5 Immaterial and Missing Power — Sakuya spell cards, Time Sign “Private Square”**
   - Exact reference: https://en.touhouwiki.net/index.php?mobileaction=toggle_view_desktop&title=Immaterial_and_Missing_Power%2FSpell_Cards%2FSakuya_Izayoi
   - Inspect: Inspect Private Square / Sakuya's World as exact official time-stop state vocabulary.
   - Teaches: Supports a distinct controlled time-stop attitude while keeping knives/effects conceptually separable from the body.
   - Do not copy: Do not copy fighter pose sequences, effects or timing into Scarlet Moon.
4. **TH06 Embodiment of Scarlet Devil — Sakuya official artwork file**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06Sakuya.png
   - Inspect: Inspect only for face/headdress/maid-costume cues relevant to the 32×32 portrait.
   - Teaches: Portrait identity vocabulary complementary to the approved V4 design sheet.
   - Do not copy: Do not downscale illustration or overload the native body sprites with lace detail.

These references are deliberately small and specific. They tell the later artist **which sheet/file/state to inspect**. Third-party sprite sheets remain external link/metadata only and are not copied into this repository.

## 4. Owner-approved V4 design sheet

- Silver/lavender braided hair with white maid headdress.
- Dark navy/white maid dress and apron create the primary body split; green chest bow is a secondary accent.
- Knife vocabulary is explicit and should read as a controlled prop, not visual noise.
- At 32×32 preserve silver head mass, white headdress, navy/white apron silhouette and a clean knife cue; reduce lace and bow detail first.

The committed sheet is the exact Owner-approved design authority identified by path, dimensions and SHA-256 above. It is not an exact pose blueprint; incidental generated labels or decorative details that conflict with actual character identity or the live Scarlet Moon contract remain non-authoritative.

## 5. Translation notes

- Keep a stable 32×32 maid silhouette; distinguish stop through stance/arm/knife cue rather than body-size change.
- Use the exact TH06 boss sprite and TH07 player rows for scale/silhouette vocabulary; use Private Square only for state language.
- Hair/headdress and apron value blocks are the recognition backbone; lace detail is subordinate.
- Do not absorb time-stop overlays/projectiles into the character sprite.

**Translation equation:** Scarlet Moon state contract + selected official Touhou vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.

## 6. Production-brief seed

> Author Sakuya idle A/B, time-stop pose and portrait as one coherent family. Preserve the 32×32 body contract and existing stop trigger. Inspect the selected TH06 isolated boss sprite, TH07 playable rows and exact Private Square state for official vocabulary; use the committed approved V4 sheet for appearance. Keep effects separate and do not change runtime.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
