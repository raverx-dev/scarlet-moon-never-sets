# V4 Mansion refinement 01 — static candidate

**For Owner visual review. Candidate art only.** The original [architectural-kit proof](../v4_mansion_architectural_kit/README.md) remains intact at `13ff42307d5f008b8fa8ebce80f546b164067a1b`. This new package branches from that exact commit. No game runtime or frozen version is changed.

| Direct native previews | Dimensions |
|---|---:|
| [Gameplay](mansion_gameplay_preview_192x240.png) | 192×240 |
| [Story/dialogue](mansion_story_preview_256x240.png) | 256×240 |

Compare [gameplay before/after](gameplay_proof_vs_refinement.png), [story before/after](story_proof_vs_refinement.png), and [V3 / Astra / proof / refinement](v3_astra_proof_refinement.png). The last comparison uses the original proof's source-bound V3 and Astra reference images; those are context, not new art or game captures.

The gameplay composition places smaller authored far windows and piers behind the main bays. Its floor changes from smaller distant flags to near stone diamonds, while the runner and combat center remain quiet. Story instead frames a wide rear elevation and actor stage, adding narrower side niches outside the actor zones. The rose has segmented blue/red glass and a red-violet reliquary in its former blank niche. The new detail is deliberately restricted to the far wall and outer edges.

## Review evidence

- [Atlas](mansion_asset_atlas.png) and [asset inventory](asset_inventory.md), including all ten original kit IDs and three added far variants.
- [Rose revision before/after](rose-apse_before_after.png), [floor revision before/after](floor_before_after.png), and [RoboPixel selection evidence](robopixel_evidence.json).
- [Gameplay character scale](mansion_gameplay_scale.png) and [story actors with dialogue coverage](mansion_story_staging.png). These reuse unchanged V3 sprite matrices and the proof's existing UI coverage bounds.
- [Layouts](layouts.json), [read-back exports](exports/), [canonical PNGs](canonical_previews/), [compositor](compose.py), [authoring inputs](authoring_inputs.json), and [verification](verification.json).

The five changed assets were authored with RoboPixel `grid_paste` against exact expected revisions or through `asset_create` then `grid_paste`. The new rose is revision 5 from proof revision 4 (183 changed pixels); floor revision 5 from 4 (8 changes). Each far variant is revision 2. The grids in `authoring_inputs.json` are *submitted inputs*; scene assembly consumes only actual `export_preview` read-back matrices in `exports/`. The `canonical_previews/` PNGs are RoboPixel `asset_view` pixels for changed assets and unchanged original proof views for reused assets. No asset was approved or delivery-exported.

Run `python3 compose.py`, `python3 review_context.py`, and `python3 verify.py` here with Python 3 and Pillow. `verify.py` checks all 13 PNG/matrix RGBA equivalences, five selected revision hashes and validation/approval evidence, exact scene pixel reproduction, palette membership, distinct compositions, and byte identity of all 73 files in the original proof branch. Original proof files remain byte-identical.

**Limits:** Static compositions and static sprite/UI witnesses only. No live gameplay or dense bullet/animation QA, runtime dialogue overlay, hardware-exact NES qualification, formal asset approval, merge, or V4 integration. RoboPixel validation passed on the five changed assets but retains pixel-orphan/unused-palette findings; see evidence. The carpet still uses stepped 32-pixel border segments, and the remaining distant stone work is simple; Owner visual review decides whether this candidate is acceptable.
