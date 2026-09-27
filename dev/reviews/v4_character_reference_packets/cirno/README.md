# Cirno — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is narrowly selected pose/silhouette/state vocabulary only. The committed Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved V4 sheet: [`image-gen-2(20260927-092334).png`](../design-sheets/image-gen-2(20260927-092334).png)
- Repository path: `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-2(20260927-092334).png`
- Dimensions: **1122×1402**
- File size: **2100443 bytes**
- SHA-256: `3722af4d2914d212dfb993af17bacfe8d6b373bb46974175858922d9a913811f`

![Owner-approved V4 Cirno design sheet](../design-sheets/image-gen-2(20260927-092334).png)

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `cirno` | 24×32 | Boss, before/after dialogue, defeat, attract sequence and credits | Idle A | Reusable body family | Boss/dialogue/credits share this family; wings belong to the body silhouette. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L367) |
| `cirnoB` | 24×32 | Same body-family uses | Idle B | Reusable body family | Keep wing/body bounds coherent; avoid current alternate-frame silhouette loss. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L401) |
| `cirnoFreeze` | 24×32 | Frozen-bullet condition; frozen credits vignette | Freeze special pose | Reusable special body pose | Distinct state must remain distinct; do not substitute base art for freeze. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L435) |
| `p_cirno` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1046) |

## 2. Current Scarlet Moon evidence

- Current definitions: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L367, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L401, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L435; portrait https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1046; freeze selector https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775.
- Credits/freeze use: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2091; defeat movement reuse: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2111.
- Reconnaissance says defeat is staging rather than separate art and flags wing/body continuity plus alternate-frame silhouette loss.
- Full source-rendered reconnaissance/frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Selected official Touhou production references

1. **TH06 Embodiment of Scarlet Devil — Cirno isolated boss sprite**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06CirnoSprite.png
   - Inspect: Inspect the isolated official boss sprite for compact body/wing proportions and silhouette economy.
   - Teaches: Direct small-sprite evidence for aqua head mass, dress footprint and icicle-wing read.
   - Do not copy: Do not copy pixels or expand Scarlet Moon beyond its 24×32 envelope.
2. **TH06 Embodiment of Scarlet Devil — Stage 2 spell card 06, Freeze Sign “Perfect Freeze”**
   - Exact reference: https://en.touhouwiki.net/wiki/Embodiment_of_Scarlet_Devil/Spell_Cards/Stage_2
   - Inspect: Inspect the official Perfect Freeze state/presentation context only.
   - Teaches: Confirms the freeze visual vocabulary and frozen-bullet identity that Scarlet Moon's cirnoFreeze state references.
   - Do not copy: Do not copy bullet pattern, spell timing or treat it as an exact body-pose blueprint.
3. **TH06 Embodiment of Scarlet Devil — Cirno official artwork file**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06Cirno.png
   - Inspect: Inspect only for face, bow, dress and wing identity at portrait scale.
   - Teaches: Useful portrait/identity vocabulary to reconcile with the V4 sheet.
   - Do not copy: Do not downscale it or import illustrative detail into the tiny body frames.

These references are deliberately small and specific. They tell the later artist **which sheet/file/state to inspect**. Third-party sprite sheets remain external link/metadata only and are not copied into this repository.

## 4. Owner-approved V4 design sheet

- Bright aqua/blue bob hair and oversized deep-blue hair bow.
- Blue/white dress with a red chest bow as a high-value contrast landmark.
- Crystal/icicle wing silhouette is the critical fairy read.
- At 24×32 preserve hair/bow, red chest accent and wing geometry; simplify internal crystal facets aggressively.

The committed sheet is the exact Owner-approved design authority identified by path, dimensions and SHA-256 above. It is not an exact pose blueprint; incidental generated labels or decorative details that conflict with actual character identity or the live Scarlet Moon contract remain non-authoritative.

## 5. Translation notes

- Keep the 24×32 body/wing envelope stable across idle A/B/freeze; freeze must read as a real state rather than a recolor or omitted frame.
- Use the isolated TH06 sprite for silhouette economy and the Perfect Freeze page for state vocabulary, not for literal pixel copying.
- Use large simple ice-wing shapes; internal crystal faceting is secondary at native scale.
- Dialogue/defeat/credits are placements of this same body family, not new sprite requirements.

**Translation equation:** Scarlet Moon state contract + selected official Touhou vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.

## 6. Production-brief seed

> Author Cirno as one 24×32 body family (idle A/B/freeze) plus 32×32 portrait. Preserve the frozen-bullet/credits freeze trigger and all current staging. Inspect the exact TH06 Cirno boss sprite and Perfect Freeze state for official silhouette/state vocabulary, then redraw from the committed approved V4 sheet in late-Famicom/NES clusters. No invented states or runtime changes.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
