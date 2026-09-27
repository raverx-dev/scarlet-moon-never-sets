# Cirno — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is pose/silhouette/prop vocabulary only. The Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved sheet supplied to the coordinator: **image-gen-2(20260927-092334).png**, 1122×1402, SHA-256 `3722af4d2914d212dfb993af17bacfe8d6b373bb46974175858922d9a913811f`
- Sheet binary is intentionally **not copied into this repository**. The filename + hash identify the exact Owner-approved input that must be supplied to the later artist.

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `cirno` | 24×32 | Boss, before/after dialogue, defeat, attract sequence and credits | Idle A | Reusable body family | Boss at standard boss anchor; dialogue uses partner staging; wings belong to the body silhouette. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L367) |
| `cirnoB` | 24×32 | Same body-family uses | Idle B | Reusable body family | Recon notes alternate-frame silhouette loss; V4 must keep wing/body bounds coherent. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L401) |
| `cirnoFreeze` | 24×32 | Frozen-bullet condition; frozen credits vignette | Freeze special pose | Reusable special body pose | Distinct state must remain distinct. Do not repeat the rejected experiment's substitution of base art for freeze. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L435) |
| `p_cirno` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1046) |

## 2. Current Scarlet Moon evidence

- Current definitions are at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L367, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L401, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L435 and portrait https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1046; freeze selector at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775.
- Credits reuse/freeze staging is at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2091; defeat movement reuses the named sprite at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2111.
- Reconnaissance says Cirno's defeat is movement, not separate art, and flags wing/body continuity plus lost silhouette in the alternate current frame.
- Reconnaissance source-rendered evidence and full frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Curated official Touhou reference set

1. **Embodiment of Scarlet Devil Cirno — character page** — Official EoSD boss sprite and character design.
   - Source: https://en.touhouwiki.net/wiki/Cirno
   - Teaches: Compact boss silhouette, aqua hair, ribbon and icicle-wing vocabulary; official page also records the wing shape.
   - Do not copy: Do not copy the exact EoSD boss pixels or use later-game detail to expand Scarlet Moon's 24×32 contract.
2. **Embodiment of Scarlet Devil official image archive** — Th06CirnoSprite / official artwork cross-check.
   - Source: https://en.touhouwiki.net/wiki/Category:Embodiment_of_Scarlet_Devil_Images
   - Teaches: Boss-scale wing/body proportion versus larger official art, useful for deciding what survives the tiny sprite.
   - Do not copy: Do not treat one official illustration accessory as a required Scarlet Moon state or copy the sheet literally.

These are reference links/metadata only. No third-party sprite sheet is copied into the repository.

## 4. Owner-approved V4 design sheet

- Bright aqua/blue bob hair and oversized deep-blue hair bow.
- Blue/white dress with a red chest bow as a high-value contrast landmark.
- Crystal/icicle wing silhouette is the critical fairy read.
- At 24×32 preserve hair/bow, red chest accent and wing geometry; simplify internal crystal facets aggressively.

The sheet is a design authority, not an exact pose blueprint. Generated labels or ornamental details that conflict with actual character identity or the live Scarlet Moon contract are non-authoritative.

## 5. Translation notes

- Keep the 24×32 body/wing envelope stable across idle A/B/freeze; freeze must read as a real state rather than a recolor or omitted frame.
- Use large simple ice-wing shapes, not high-frequency crystal faceting; one or two highlight planes are enough at native scale.
- Keep the blue hair/bow and red chest accent separated so the face/head does not disappear into the wings.
- Dialogue/defeat/credits are placement/staging variants of this same body family, not new sprite requirements.

The translation equation for the later artist is:

**Scarlet Moon state contract + official Touhou visual vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.**

## 6. Production-brief seed

> Author Cirno as one 24×32 body family (idle A/B/freeze) plus 32×32 portrait. Preserve frozen-bullet/credits freeze selection and all current staging. Use official EoSD silhouette/wing vocabulary and the approved sheet's blue hair/bow/red accent/crystal-wing identity, simplified into late-Famicom/NES clusters. Prove wing/body continuity at native scale. No invented extra states or runtime changes.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
