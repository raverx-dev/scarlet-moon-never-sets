# Sakuya Izayoi — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is pose/silhouette/prop vocabulary only. The Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved sheet supplied to the coordinator: **image-gen-5(3).png**, 1122×1402, SHA-256 `4b743abd1410b4f7b1154855349509d19f53b8485fcc4ebc30767748520e332a`
- Sheet binary is intentionally **not copied into this repository**. The filename + hash identify the exact Owner-approved input that must be supplied to the later artist.

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `sakuya` | 32×32 | Boss, dialogue, defeat, attract and credits | Idle A | Reusable body family | Standard boss anchor; dialogue staged at x=208,y=108. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L571) |
| `sakuyaB` | 32×32 | Same body-family uses | Idle B | Reusable body family | Keep same apparent height/width and maid silhouette as idle A. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L605) |
| `sakuyaStop` | 32×32 | Frozen-bullet/time-stop condition; timed credits vignette | Time-stop special pose | Reusable special body pose | State selector is semantic contract; knife/clock/projectile effects remain separate presentation systems. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L639) |
| `p_sakuya` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1114) |

## 2. Current Scarlet Moon evidence

- Current definitions are at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L571, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L605, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L639 and portrait https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1114; stop selector at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775.
- Dialogue staging is at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2040; attract use https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2078; credits time-stop vignette https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2094; defeat exit reuses the body at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2111.
- Reconnaissance separates Sakuya body/stop/portrait from knife/clock effects; no extra character-art family is required for those effects.
- Reconnaissance source-rendered evidence and full frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Curated official Touhou reference set

1. **Perfect Cherry Blossom / Imperishable Night Sakuya — character page** — Official back sprites plus EoSD/Windows sprite lineage.
   - Source: https://en.touhouwiki.net/wiki/Sakuya_Izayoi
   - Teaches: Maid silhouette, silver hair/headdress and shooter-facing compact body vocabulary; recurring knife identity.
   - Do not copy: Do not trace sprite pixels or import official animation timing/weapon count.
2. **Embodiment of Scarlet Devil Stage 5 spell-card archive** — Official knife/time manipulation presentation vocabulary.
   - Source: https://en.touhouwiki.net/wiki/Embodiment_of_Scarlet_Devil/Spell_Cards/Stage_5
   - Teaches: How Sakuya's time/knife identity is communicated around the body without requiring the body sprite itself to carry every effect.
   - Do not copy: Do not copy projectile patterns, timings or spell-card layouts into Scarlet Moon.

These are reference links/metadata only. No third-party sprite sheet is copied into the repository.

## 4. Owner-approved V4 design sheet

- Silver/lavender braided hair with white maid headdress.
- Dark navy/white maid dress and apron create the primary body split; green chest bow is a secondary accent.
- Knife vocabulary is explicit and should read as a controlled prop, not visual noise.
- At 32×32 preserve silver head mass, white headdress, navy/white apron silhouette and a clean knife cue; reduce lace and bow detail first.

The sheet is a design authority, not an exact pose blueprint. Generated labels or ornamental details that conflict with actual character identity or the live Scarlet Moon contract are non-authoritative.

## 5. Translation notes

- Keep a stable 32×32 maid body silhouette; make the stop pose distinct through stance/arm/knife cue rather than changing body scale.
- Use hair/headdress and apron value blocks as the recognition backbone; lace detail is subordinate.
- Knives can be compact highlights; avoid multiple thin anti-aliased blades that become noise.
- Do not absorb time-stop overlays/projectiles into the character sprite—they remain separate presentation concerns.

The translation equation for the later artist is:

**Scarlet Moon state contract + official Touhou visual vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.**

## 6. Production-brief seed

> Author Sakuya idle A/B, time-stop pose and portrait as one coherent family. Preserve the current 32×32 body contract and the existing stop trigger; do not alter knife/time mechanics. Use official shooter/knife vocabulary only as reference and the approved sheet as appearance authority. Translate silver hair/headdress + navy/white maid silhouette into deliberate NES-era clusters, with a clearly distinct but same-scale stop pose.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
