# Marisa Kirisame — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is pose/silhouette/prop vocabulary only. The Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved sheet supplied to the coordinator: **image-gen-3(5).png**, 1122×1402, SHA-256 `b36b542d012b3d1a89198ae43d2feda0c9502bfc1e5b686c6807a355dbd20003`
- Sheet binary is intentionally **not copied into this repository**. The filename + hash identify the exact Owner-approved input that must be supplied to the later artist.

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `marisa` | 32×32 | Boss, dialogue, defeat, attract and flying credits | Idle A | Reusable body/broom family | Body and broom are authored together in the current sprite; boss anchor is shared with other bosses. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L469) |
| `marisaB` | 32×32 | Same body-family uses | Idle B | Reusable body/broom family | Recon notes alternate-frame silhouette loss; V4 must keep stable body/hat/broom scale. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L503) |
| `marisaAttack` | 32×32 | Boss phases m3/m4 | Attack / high-power state | Reusable special body pose | Selector chooses this for Non-Directional Laser/Master Spark phases; preserve semantic distinction without enlarging body. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L537) |
| `p_marisa` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1080) |
| `dialogue book (procedural current presentation)` | ≈12×16 visible envelope | Marisa dialogue only, drawn separately near x=136,y=118 | Book prop / presentation cue | Presentation-specific separate concern | Not a SPRITES definition. Keep separate from Marisa body/broom; current source draws a small procedural book, so later redraw may be its own anchored prop without inventing new character states. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2040) |

## 2. Current Scarlet Moon evidence

- Current body definitions are at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L469, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L503 and https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L537; portrait at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1080; selector logic at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775.
- Dialogue body/book staging is at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2040; attract reuse at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2077; flying credits at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2092; defeat reuses the body and adds particles at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2111.
- Reconnaissance identifies body/broom continuity across combat, Forest dialogue, defeat, attract and credits; book remains a distinct presentation concern rather than a body state.
- Reconnaissance source-rendered evidence and full frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Curated official Touhou reference set

1. **Imperishable Night / playable Marisa — character page** — Playable shooter/back-sprite lineage and recurring hat/broom silhouette.
   - Source: https://en.touhouwiki.net/wiki/Marisa_Kirisame
   - Teaches: How the wide hat, blonde head mass and broom communicate Marisa under small shooter-scale constraints.
   - Do not copy: Do not copy official pixel clusters, animation timing or exact broom angle as a required Scarlet Moon pose.
2. **Embodiment of Scarlet Devil official image archive** — Early Windows official Marisa artwork/presentation.
   - Source: https://en.touhouwiki.net/wiki/Category:Embodiment_of_Scarlet_Devil_Images
   - Teaches: Hat/bow, black-white costume and face/hair vocabulary for portrait/body cohesion.
   - Do not copy: Do not downscale official artwork or preserve decorative details that fight the 32×32 envelope.

These are reference links/metadata only. No third-party sprite sheet is copied into the repository.

## 4. Owner-approved V4 design sheet

- Huge dark witch hat with broad brim/floppy crown and a large white bow; long blonde hair.
- Dark navy/black witch dress with white apron/frill and small blue chest accents.
- Broom is a primary identity object; gold star ornaments are secondary decoration.
- At 32×32 preserve hat+broom+blonde-hair silhouette first; reduce dangling star/frill ornament before changing apparent body scale.

The sheet is a design authority, not an exact pose blueprint. Generated labels or ornamental details that conflict with actual character identity or the live Scarlet Moon contract are non-authoritative.

## 5. Translation notes

- Hold a single 32×32 apparent body scale across idle A/B and attack; the hat brim and broom must not make one state look like a larger character.
- Prioritize hat silhouette, blonde hair mass, dark/light costume split and broom. Star ornaments are expendable at native scale.
- Keep attack posture visibly distinct while preserving the same center/foot/body mass used by idle states.
- Treat the dialogue book as independently anchored presentation art if redrawn; do not bake it into the reusable Marisa body.

The translation equation for the later artist is:

**Scarlet Moon state contract + official Touhou visual vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.**

## 6. Production-brief seed

> Author Marisa's complete V4 family: marisa, marisaB, marisaAttack and p_marisa, while treating the dialogue book as a separate presentation prop concern. Preserve the 32×32 body contract and current m3/m4 attack trigger. Use official shooter material for hat/broom/flight vocabulary and the approved sheet for appearance. Translate with stable late-Famicom/NES clusters; prove hat+broom bounds and body-scale continuity. No runtime changes.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
