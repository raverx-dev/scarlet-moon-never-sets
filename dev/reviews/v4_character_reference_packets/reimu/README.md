# Reimu Hakurei — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is pose/silhouette/prop vocabulary only. The Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved sheet supplied to the coordinator: **image-gen-1(20260927-092333).png**, 1122×1402, SHA-256 `2eb22de905cd9b4738f4b5540fd9f6c8167c828ecfb865becc05171ef9435f7a`
- Sheet binary is intentionally **not copied into this repository**. The filename + hash identify the exact Owner-approved input that must be supplied to the later artist.

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `reimu` | 16×24 | Gameplay player in every stage | Idle A | Reusable gameplay body | Idle cadence via (frame>>4)&1; normal gohei layered separately at [8,-5]. Preserve player coordinate/hitbox contract and existing clipping. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L45) |
| `reimuB` | 16×24 | Gameplay player in every stage | Idle B | Reusable gameplay body | Same body scale/anchor as idle A; normal gohei offset [7,-5]. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L71) |
| `reimuFocus` | 16×24 | Gameplay while focus is held | Focused stance | Reusable gameplay body | State override; normal gohei offset [8,-5]. Do not change movement or hitbox to fit art. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L97) |
| `reimuFire` | 16×24 | Gameplay while firing and alive | Firing stance | Reusable gameplay body | State override; fire gohei layered at [9,-4]. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L123) |
| `reimuGohei` | 10×14 | Layered with idle A/B and focus | Normal held purification rod | Reusable independent prop | Keep body anchor independent of asymmetric prop; may clip at playfield edges under current movement bounds. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L149) |
| `reimuGoheiFire` | 12×14 | Layered with reimuFire | Firing gohei state | Reusable independent prop | Separate asset/extent from normal gohei; do not fuse into body. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L165) |
| `reimuStoryA` | 24×32 | Intro/opening, dialogue staging, gate transit, defeat staging, ending and credits | Story idle A | Reusable story body | Full 256×240 presentation family; alternates on the same frame parity. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L231) |
| `reimuStoryB` | 24×32 | Same story/presentation uses | Story idle B | Reusable story body | Stable story-body scale and anchor across A/B. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L265) |
| `reimuStoryTalkA` | 24×32 | Dialogue while Reimu is active speaker and text is printing | Talking A | Reusable story body | Selected by storyReimu; do not turn text timing into animation timing. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L299) |
| `reimuStoryTalkB` | 24×32 | Same speaking use | Talking B | Reusable story body | Must remain recognizably the same 24×32 body family. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L333) |
| `p_reimu` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior; compose for clipping, not for a larger hidden canvas. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1012) |
| `reimuTitle` | 32×48 | Title screen only | Independent title presentation | Presentation-specific independent art | Current title moves around x≈128±46, y≈48±5 in the 256×240 title scene; do not force gameplay proportions onto it. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L181) |

## 2. Current Scarlet Moon evidence

- Current source definitions: gameplay/body/props/title/story start at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L45; selector and prop layering are at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1777; story selector is at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1778.
- Current staging: gameplay player render https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2027; dialogue/story positions https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2038–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2041; title use https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2056; credits https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2096; gate/defeat/ending uses https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2108–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2115.
- Reconnaissance explicitly records 12 Reimu definitions, side-facing current gameplay, independent gohei anchoring, edge clipping risk, 32×32 portrait clipping, and title art as independent presentation.
- The first six-asset Reimu r2 canonical attempt is rejected evidence only: it was over-simplified, weakened identity/state differentiation, and is not a baseline.
- Reconnaissance source-rendered evidence and full frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Curated official Touhou reference set

1. **Imperishable Night / playable Reimu — character page** — Rear-facing/player-shooter orientation and compact Reimu silhouette vocabulary.
   - Source: https://en.touhouwiki.net/wiki/Reimu_Hakurei
   - Teaches: How bow, hair mass and shrine-maiden costume remain legible from a shooter-facing view; useful comparison material for gameplay orientation.
   - Do not copy: Do not trace official pixels, import its palette/canvas, or silently change Scarlet Moon's current side-facing gameplay contract.
2. **Embodiment of Scarlet Devil official image archive** — Early Windows official Reimu presentation/identity reference.
   - Source: https://en.touhouwiki.net/wiki/Category:Embodiment_of_Scarlet_Devil_Images
   - Teaches: Face, bow, red/white costume and early-series simplification vocabulary relevant to portrait/title translation.
   - Do not copy: Do not downscale the illustration or copy its pixel clusters literally.

These are reference links/metadata only. No third-party sprite sheet is copied into the repository.

## 4. Owner-approved V4 design sheet

- Oversized red hair bow with white frilled edge; dark long hair as the dominant head mass.
- Strong red/white shrine-maiden split with detached white sleeves and red skirt; yellow chest accent.
- Gohei/ofuda vocabulary is explicit; red footwear and ribbon accents support the lower silhouette.
- At tiny scale preserve bow, dark hair mass, red/white separation, detached-sleeve read and gohei; discard decorative pattern noise before sacrificing identity.

The sheet is a design authority, not an exact pose blueprint. Generated labels or ornamental details that conflict with actual character identity or the live Scarlet Moon contract are non-authoritative.

## 5. Translation notes

- State contract wins: preserve all four 16×24 gameplay meanings, two independent gohei states, four 24×32 story states, portrait and independent title art.
- Use official rear-facing shooter material as vocabulary because #42 explicitly requests it, but current Scarlet Moon/recon is side-facing. A canonical orientation change needs an explicit Owner/Manager decision; this packet does not invent one.
- At 16×24, spend pixels on the giant bow, dark-hair head mass, red/white body split and gohei readability before frill/pattern detail.
- At 24×32 and 32×32, restore enough face/sleeve/hair information to unify story and portrait with gameplay without merely enlarging the small sprite.
- Title 32×48 is a separate composition problem: retain Reimu identity but design for its moving title silhouette and surrounding moon/logo staging.

The translation equation for the later artist is:

**Scarlet Moon state contract + official Touhou visual vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.**

## 6. Production-brief seed

> Author Reimu as one coherent V4 family from the exact state/canvas matrix above. Treat live Scarlet Moon semantics, anchors, selector timing and staging as fixed; use official Touhou only for pose/orientation/silhouette vocabulary; use the approved sheet hash as appearance authority. Translate to deliberate late-Famicom/NES pixel construction with stable body scale and distinct states. Keep gohei separate. Return native 1× plus nearest-neighbor review witnesses for gameplay, story, portrait and title; do not modify runtime or promote rejected r2.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
