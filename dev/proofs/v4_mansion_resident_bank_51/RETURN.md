# #51 completion record — Owner visual review required

One new native **192×240 Mansion Interior gameplay candidate** and its complete review package are ready. Artistic acceptance remains with the Owner.

**Inspect first:** [native candidate](package/candidate_native.png), then [four-role comparison board](package/comparison_four_pane.png). [owner-review.html](owner-review.html) presents the native image first, followed by 3× inspection and the complete evidence.

## Preserve / change checkpoint

Preserved V3's finite 8×8/16×16 construction, repeat/place economy and quiet lane; #22's rose/lancet/pier/hanging/stair/runner hierarchy and clean paving; the old kit's canonical authoring → exact readback → deterministic external composition method. #45 supplied construction/palette proof, not copied pixels or an aesthetic ceiling.

New work improves the rose glass masses, stepped Gothic shoulders, compound piers, near/far bay framing and bounded runner/floor vocabulary. [Original pre-authoring checkpoint](PRESERVE_CHANGE.md) records the read-order reality check.

## Guidance actually consulted

- [Slynyrd Pixelblog 45 — brickwork](https://www.slynyrd.com/blog/2023/7/21/pixelblog-45-bricks-walls-doors-and-more): distinguish planes through pattern scale/value; use restrained variants and short shadows.
- [Pixelblog 37 — Castlevania study](https://www.slynyrd.com/blog/2022/3/19/pixelblog-37-classic-castlevania-study): constrained Gothic tile variation and focused section-by-section construction.
- [Pixelblog 16 — Medieval Fantasy](https://www.slynyrd.com/blog/2019/4/23/pixelblog-16-medieval-fantasy): architectural massing; limited exterior-focused applicability.
- Lospec stone index was discovery only. Linked tutorial GIFs were inaccessible; no claim of inspecting them. No third-party pixels or bulk prose were copied.
- Current #40 Gate/Interior native scenes and Interior atlas were visually consulted under #44 construction rules.

## Canonical bank / selected revisions

Project: `scarlet-moon-never-sets`. **41 selected new `v4-mi51-*` environment assets.**

- `v4-mi51-rose`: **r4**.
- `v4-mi51-arch-shoulder`, `v4-mi51-floor-worn`: **r3**.
- Every other selected member, including seven exact mirrored variants: **r2**.
- [Bank inventory](package/bank_inventory.json) and [checkpoint](package/checkpoint.json) give every exact asset ID/revision/revision hash/palette hash/render hash.
- Unselected `v4-mi51-runner-edge` r2 remains preserved outside this bank.
- Existing #22/#45 families were not mutated. Five unchanged #45 r2 assets appear only in the readability witness.

| Native component size | Selected count |
|---|---:|
| 8×8 atoms | 9 |
| 16×8 cornice | 1 |
| 16×16 metatiles | 20 |
| 16×32 structures | 3 |
| 16×48 structures | 3 |
| 32×16 near-pier pieces | 3 |
| 32×32 doors | 1 |
| 64×64 rose landmark | 1 |

Families cover masonry, paving, carpet, near/far piers, lancets, trim/edges, stairs, hanging, doors, sconce and rose. Mirrored variants are canonical because the v1 packager's strict placement schema lacks transform fields; no RoboPixel product change was needed.

## Palette / gameplay layout

Four shared background subpalettes, **13 visible colors**, common backdrop `#10121e`: stone, crimson/fabric, warm metal/wood, cool glass. All **180 final 16×16 neighborhoods conform**; no swap or waiver. Future HUD must share these four slots. Exact colors and witness sprite allocations are in [palette ledger](palette_ledger.json).

One production background: **192×240**. Rear rose, cool side lancets, folded hangings, warm doors, authored smaller far windows, raised stairs and widening carpet; overlapping near piers/arches frame the lower field. **Quiet lane x64..127, y128..239**. Integer placement only; no scale, recolor, post-composition repair, story scene or baked-in overlays.

## Package location / verification

Repository branch: `v4-mi51-review-package-v1`. Proof directory:
`dev/proofs/v4_mansion_resident_bank_51/`.

Mechanical package commit: `659e3a18519a7063db2431aca9871306806ece39`, based exactly on artist input `39177310c7c3e82aff41033e4404f07d82137980`. This completion record and native-first Owner page are additive text files; they preserve the 17 verified generated outputs.

- Canonical D4 readback / D3 render pins: **46/46 PASS** — 41 environment + five unchanged witness assets.
- Selected asset validation: **41/41 PASS**, **58 nonblocking orphan warnings retained**.
- Construction: **196 family-aware 8×8 tiles**, **92 final 16×16 metatiles**, exact reconstruction. Independent RGBA-only deduplication finds **194 pixel patterns**; palette-family identity explains the count difference.
- Two independent package/supplement runs: **all 17 generated files byte-identical**, total 549,896 bytes.
- Coordinator independently checked published PNG dimensions, exact native/witness D3 hashes, exact nearest-neighbor enlargement and all canonical pins.
- Changes remain within this proof directory. No runtime, gameplay, character/HUD authoring, other environments, merge or release.
- **Unresolved mechanical issues: none.** Static readability does not claim live scrolling/dense-danmaku QA.

Candidate D3 render hash:
`63e7a362cedd179868ffad29483fd7545b984eabd0e12c5f898b25fdfa383136`.

Readability witness D3 render hash:
`126d5c014a7fe19d4ec6dd2cf23cc6c5d188fbd0779ece028bd79b582fe6a4d3`.

## Unresolved artistic questions

Owner should judge rose dominance, bilateral symmetry, stone/material richness relative to #22, and the dark bands beside the widening carpet. The candidate is more restrained than #22; construction compliance does not settle whether that tradeoff succeeds visually.

**OWNER VISUAL REVIEW REQUIRED.**
