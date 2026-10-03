# #51 correction 01 — Owner visual review required

Inspect [candidate_native.png](package/candidate_native.png) first, then [the V3 / #22 / #45 / corrected #51 comparison](package/comparison_four_pane.png). [3x inspection](package/candidate_nn3x.png); [native-first review](owner-review.html).

## 1. Preserved unchanged

Original review branch `v4-mi51-review-package-v1` remains at `a9ae66e0dcf71de4b8381fd3f1abbc0c064e75b5`. Correction continues its exact bank. All 40 non-rose selected assets, their palettes and pixels are unchanged; the unselected `v4-mi51-runner-edge` r2 is also preserved. No replacement family was created. Four members are intentionally unplaced: floor-field, floor-joint, floor-worn, lancet-ruby. Their exact pins and tiles remain in the full bank inventory/atlas.

| Exact preserved asset | Revision |
|---|---:|
| `v4-mi51-wall-field` | r2 |
| `v4-mi51-wall-joint-a` | r2 |
| `v4-mi51-wall-joint-b` | r2 |
| `v4-mi51-floor-field` | r2 |
| `v4-mi51-floor-joint` | r2 |
| `v4-mi51-floor-worn` | r3 |
| `v4-mi51-runner-field` | r2 |
| `v4-mi51-runner-motif` | r2 |
| `v4-mi51-cornice` | r2 |
| `v4-mi51-pier-cap` | r2 |
| `v4-mi51-pier-shaft` | r2 |
| `v4-mi51-pier-collar` | r2 |
| `v4-mi51-pier-base` | r2 |
| `v4-mi51-dado-panel` | r2 |
| `v4-mi51-stair-stone` | r2 |
| `v4-mi51-stair-runner` | r2 |
| `v4-mi51-lancet-near` | r2 |
| `v4-mi51-lancet-ruby` | r2 |
| `v4-mi51-lancet-far` | r2 |
| `v4-mi51-arch-shoulder` | r3 |
| `v4-mi51-arch-jamb` | r2 |
| `v4-mi51-arch-foot` | r2 |
| `v4-mi51-banner` | r2 |
| `v4-mi51-sconce` | r2 |
| `v4-mi51-backdrop` | r2 |
| `v4-mi51-runner-turn-far` | r2 |
| `v4-mi51-runner-turn-mid` | r2 |
| `v4-mi51-runner-turn-near` | r2 |
| `v4-mi51-runner-turn-full` | r2 |
| `v4-mi51-near-pier-cap` | r2 |
| `v4-mi51-near-pier-shaft` | r2 |
| `v4-mi51-near-pier-base` | r2 |
| `v4-mi51-door` | r2 |
| `v4-mi51-arch-shoulder-mirror` | r2 |
| `v4-mi51-arch-jamb-mirror` | r2 |
| `v4-mi51-arch-foot-mirror` | r2 |
| `v4-mi51-runner-turn-far-mirror` | r2 |
| `v4-mi51-runner-turn-mid-mirror` | r2 |
| `v4-mi51-runner-turn-near-mirror` | r2 |
| `v4-mi51-runner-turn-full-mirror` | r2 |

## 2. Revised asset

Only `v4-mi51-rose`: **r4 -> r7**, via r5 positive pane masses, r6 internal lead divisions, r7 masonry seating clearance. Original r4 remains immutable. Final revision hash `0ddf597abdd5163f48032fbc03a73d7aff88249f74f83e42792b09fe8ff5ed72`. All other revision/palette/render hashes are identical to the original bank.

## 3. Exact layout changes

- Rose canvas (64,0) -> **(64,16)**; visible circular glass about **46x46**, at x73..118 / y25..70. Full cornice y0..7; wall surrounds the landmark, including the four empty 16x16 canvas-corner neighborhoods. Stone is placed from its own bank outside visible glass, never mixed into the crimson asset.
- Door **(80,64) -> (80,96)**. Clear masonry band y80..95 separates the rose canvas and door. Stair tiles y96 -> **y128**, retaining door -> stair -> runner.
- Banners **(48,16)/(128,16) -> (32,16)/(144,16)**, within side bays. Sconces now (32,64)/(144,64); large cyan lancets (32,80)/(144,80). Existing small far lancets flank the door at (64,96)/(112,96). Recovery found `lancet-far` is crimson r2, not cyan; it was preserved and not recolored.
- Removed both lower `lancet-ruby` placements. Side arches now begin at y16, continue to y128, and share the same side-bay/inner-pier axes. Inner piers x48/x128 run from caps y32 to bases y128. Larger foreground piers x0/x160 now extend from y16 to bases y224, instead of starting a separate lower register at y128.
- Exact **1440 integer placements** are in `layout.json` and the strict handoff `checkpoint.json`. One 192x240 production background; readability adds the unchanged original 12 witness placements only.

## 4. Rose readability

Positive rose-colored panes fill eight radial lobes around a luminous central roundel. Dark lead and ring structure separates panes; internal divisions replace the old isolated emblem-like markings. The smaller circle has breathing room beneath the cornice and masonry between it and the door. Rose orphan warnings **20 -> 0**; no blanket cleanup of other assets.

Guidance consulted again: [Slynyrd Pixelblog 5](https://www.slynyrd.com/blog/2018/5/16/pixelblog-5-back-to-basics), deliberate connected clusters and hard native pixels; [French Ministry of Culture rose-window record IM28000472](https://pop.culture.gouv.fr/notice/palissy/IM28000472), central eye / radial compartments / outer ring, simplified into an original eight-lobe design. Text descriptions only; no tutorial pixels copied.

## 5. Runner / floor

Existing runner-turn assets and mirrors remain **r2**. First widening uses far/mid/near/full at y144/160/176/192, x64/x112; second widening uses far/mid at y208/224, x48/x128. The surrounding floor continues in the same shared dark value as the transitions' outside pixels, eliminating isolated dark wedges against a lighter field. Floating side-floor patches from the first correction iteration were removed. Two existing low-contrast motifs remain at (88,168)/(96,208). Quiet lane remains x64..127 / y128..239, with stairs at its rear edge and calm carpet below.

## 6. Native comparison / visual assessment

Four native passes were inspected against V3 construction, accepted #22 and #45. The corrected frame has one stair/runner axis, tall foreground piers and a smaller seated rear landmark. #45 remains mechanical evidence. #22 remains stronger in material richness and more nuanced depth; this correction aims to be competitive in spatial coherence without adding ornament.

Artist readiness checks: (1) circular stained-glass landmark recognizable: yes; (2) one receding hall: yes; (3) foreground/rear hierarchy: yes, constrained and symmetric; (4) wall seating: improved by smaller circle/corner masonry and separated door; (5) side bays support focal hierarchy: yes; (6) lower half is foreground framing: yes, no ruby chapel; (7) apparent floor holes removed: yes; (8) quiet lane calm: yes below the rear steps; (9) competitive coherence with #22: reviewable, with #22 still stronger in depth/workmanship. These are readiness judgments, not Owner acceptance.

## 7. Package location

Correction package branch: `v4-mi51-correction-01`; exact published head is supplied with the completion response. Directory remains `dev/proofs/v4_mansion_resident_bank_51/`. Original branch/head and all original proofs remain intact. The standard packager selects **37 placed environment + 5 witness** assets. Full bank inventory and 8x8 atlas retain **41 environment + 5 witness** pins, with four unplaced environment members explicitly marked. This selection distinction preserves the existing strict every-selected-asset-placed rule.

## 8. Verification

Author-side: all recovered original 41 D3 pins matched before mutation; final 41 bank matrices match their selected canonical pins; 41 bound validations PASS, with **38 retained nonblocking orphan warnings** (58 -> 38). Four unchanged background subpalettes, 13 available colors; all 180 final 16x16 neighborhoods conform. Native candidate hash `9f766329c5d3e1dbd7e334bced46e06ad04293aba99626b0d24c367e9ebdc700`; readability hash `f0a269c3144435bc434ba70bf357079f1975a880541f12fa72b70962eae8139d`.

Mechanical packaging at RoboPixel `79e7d2af9da8ee6b510c2bde07c762fbf877045e` verified the 42 standard placed pins through canonical D4/render, and an independent check through the same canonical repository/render stack verified the four preserved unplaced pins. Full bank plus witnesses are therefore 46/46 PASS. Two independently generated and supplemented outputs are byte-identical across all 17 files (453,144 bytes); detailed file and RGBA hashes are in `mechanical_results.json`. The final package has no unresolved mechanical blocker. This is mechanical readiness only and does not claim Owner artistic acceptance.

## 9–10. Remaining issues / artistic questions

No author-side mechanical blocker. Mechanical package completion must be checked against the published verification records. Static witness does not claim live scrolling/dense-danmaku QA. Owner should judge whether the rear rose is sufficiently luminous/architecturally seated, whether the foreground is too tall or regular, whether the dark floor is too empty, and whether spatial depth now competes adequately with #22. No runtime/character/HUD/story/other environment change, merge, release or artistic approval.

**OWNER VISUAL REVIEW REQUIRED.**
