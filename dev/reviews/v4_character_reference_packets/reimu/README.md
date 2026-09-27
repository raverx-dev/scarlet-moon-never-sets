# Reimu Hakurei — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is narrowly selected pose/silhouette/state vocabulary only. The committed Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved V4 sheet: [`image-gen-1(20260927-092333).png`](../design-sheets/image-gen-1(20260927-092333).png)
- Repository path: `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-1(20260927-092333).png`
- Dimensions: **1122×1402**
- File size: **2155565 bytes**
- SHA-256: `2eb22de905cd9b4738f4b5540fd9f6c8167c828ecfb865becc05171ef9435f7a`

![Owner-approved V4 Reimu Hakurei design sheet](../design-sheets/image-gen-1(20260927-092333).png)

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `reimu` | 16×24 | Gameplay player in every stage | Idle A | Reusable gameplay body | V4 orientation is rear-facing/back-view. Preserve the existing idle-A semantics, player coordinate/hitbox contract, clipping and normal-gohei layering; the current side-facing pixels are historical evidence only. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L45) |
| `reimuB` | 16×24 | Gameplay player in every stage | Idle B | Reusable gameplay body | Rear-facing/back-view V4. Same body scale/anchor as idle A; preserve existing idle cadence and normal-gohei relationship. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L71) |
| `reimuFocus` | 16×24 | Gameplay while focus is held | Focused stance | Reusable gameplay body | Rear-facing/back-view V4. Focus remains the existing state override; movement/hitbox/coordinates are unchanged. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L97) |
| `reimuFire` | 16×24 | Gameplay while firing and alive | Firing stance | Reusable gameplay body | Rear-facing/back-view V4. Fire remains the existing state override; fire gohei remains independent. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L123) |
| `reimuGohei` | 10×14 | Layered with idle A/B and focus | Normal held purification rod | Reusable independent prop | Current compatible extent and body/prop separation remain evidence/contract. Author the V4 prop to work with the new rear-facing body without moving the player anchor. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L149) |
| `reimuGoheiFire` | 12×14 | Layered with reimuFire | Firing gohei state | Reusable independent prop | Separate extent/state from normal gohei; do not fuse into body or change selectors. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L165) |
| `reimuStoryA` | 24×32 | Intro/opening, dialogue staging, gate transit, defeat staging, ending and credits | Story idle A | Reusable story body | Story orientation/staging is not changed by the gameplay back-view decision; preserve actual scene semantics and 256×240 placement. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L231) |
| `reimuStoryB` | 24×32 | Same story/presentation uses | Story idle B | Reusable story body | Stable story-body scale and anchor across A/B. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L265) |
| `reimuStoryTalkA` | 24×32 | Dialogue while Reimu is active speaker and text is printing | Talking A | Reusable story body | Selected by storyReimu; do not convert text timing into animation timing. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L299) |
| `reimuStoryTalkB` | 24×32 | Same speaking use | Talking B | Reusable story body | Must remain recognizably the same 24×32 story family. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L333) |
| `p_reimu` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior; compose for clipping. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1012) |
| `reimuTitle` | 32×48 | Title screen only | Independent title presentation | Presentation-specific independent art | Current title staging moves the asset around the 256×240 title composition; do not force gameplay proportions/orientation onto it. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L181) |

## 2. Current Scarlet Moon evidence

- Current source definitions remain at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L45 onward; selector/prop composition remains https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1777. These are semantic/runtime evidence, not the V4 orientation target.
- Current gameplay render/coordinates remain https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2027 and movement bounds remain in the existing play step; those mechanics are unchanged by the art-direction decision.
- Current story/dialogue/title staging remains https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2038–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2056 and https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2108–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2115.
- The 2026-09-27 Owner decision on #28 supersedes the side-facing V3/current visual orientation for V4 gameplay: V4 gameplay is rear-facing/back-view. Side-facing current art remains historical evidence only.
- The rejected six-asset Reimu r2 attempt remains rejected evidence; choosing back-view does not promote its design or simplification.
- Full source-rendered reconnaissance/frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Selected official Touhou production references

1. **TH07 Perfect Cherry Blossom — Characters sheet**
   - Exact reference: https://www.spriters-resource.com/pc_computer/touhouyouyoumuperfectcherryblossom/sheet/44412/
   - Inspect: Inspect Reimu's playable-character rear-facing/back-view sprite group, especially neutral/movement/shot-scale silhouettes.
   - Teaches: Primary shooter vocabulary for how Reimu's giant bow, hair mass, detached sleeves and red/white body read from behind at small player scale.
   - Do not copy: Do not trace pixels, inherit its canvas, or import TH07 timing/shot mechanics.
2. **TH08 Imperishable Night — Playable Characters sheet**
   - Exact reference: https://www.spriters-resource.com/pc_computer/touhoueiyashouimperishablenight/asset/34544/page-1/
   - Inspect: Inspect Reimu's playable back sprite group in the Reimu/Yukari player set; compare compact rear silhouette and state readability.
   - Teaches: Second official shooter-generation check for rear-facing body economy and recognizable bow/sleeve construction.
   - Do not copy: Do not average or copy official pixels; Scarlet Moon keeps its own 16×24/state/anchor contract.
3. **TH06 Embodiment of Scarlet Devil — Reimu official artwork file**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06Reimu.png
   - Inspect: Inspect only for early-Windows face/bow/costume presentation cues relevant to portrait/title families.
   - Teaches: Useful identity/presentation vocabulary at larger scale without overriding the approved V4 sheet.
   - Do not copy: Do not downscale the artwork or use it as gameplay-pose authority.

These references are deliberately small and specific. They tell the later artist **which sheet/file/state to inspect**. Third-party sprite sheets remain external link/metadata only and are not copied into this repository.

## 4. Owner-approved V4 design sheet

- Oversized red hair bow with white frilled edge; dark long hair as the dominant head mass.
- Strong red/white shrine-maiden split with detached white sleeves and red skirt; yellow chest accent.
- Gohei/ofuda vocabulary is explicit; red footwear and ribbon accents support the lower silhouette.
- At tiny scale preserve bow, dark hair mass, red/white separation, detached-sleeve read and gohei; discard decorative pattern noise before sacrificing identity.

The committed sheet is the exact Owner-approved design authority identified by path, dimensions and SHA-256 above. It is not an exact pose blueprint; incidental generated labels or decorative details that conflict with actual character identity or the live Scarlet Moon contract remain non-authoritative.

## 5. Translation notes

- Gameplay body orientation is now resolved: all four 16×24 V4 gameplay bodies are rear-facing/back-view. This is an art-direction change only.
- Preserve existing idle A/B/focus/fire meanings, 16×24 canvases, separate 10×14/12×14 gohei extents, player coordinates, hitbox, movement bounds, selector timing and edge/staging behavior.
- Use the selected TH07/TH08 rear-facing shooter sprites as pose/orientation vocabulary, then redraw as the Owner-approved Scarlet Moon V4 Reimu rather than tracing them.
- At 16×24, spend pixels on the giant bow, dark-hair head mass, red/white body split, sleeves and gohei readability before frill/pattern detail.
- Story, portrait and title families remain separate presentation problems; the gameplay back-view decision does not silently force those scenes into a rear view.

**Translation equation:** Scarlet Moon state contract + selected official Touhou vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.

## 6. Production-brief seed

> Author Reimu as one coherent V4 family. For gameplay, redraw reimu/reimuB/reimuFocus/reimuFire as rear-facing/back-view 16×24 bodies, using the selected TH07/TH08 official shooter player sprites only for orientation/pose vocabulary and the committed approved V4 sheet for appearance. Preserve all existing state semantics, canvases, coordinates, hitbox, movement, selectors/timing, clipping and separate gohei extents. Treat current side-facing pixels and rejected r2 as historical/negative evidence only. Continue story/talk, portrait and title from the same V4 identity without changing their actual staging. No runtime mutation.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
