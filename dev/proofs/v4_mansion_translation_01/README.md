# Mansion Translation Pass 01 — candidate artwork

A bounded translation of the Owner-selected full-scene Mansion direction into canonical RoboPixel pixel assets. **Candidate artwork for visual review; not final approved V4 art.** No runtime integration, asset approval/delivery, merge or site publication.

| Native preview | Review enlargement | Comparison |
|---|---|---|
| [Gameplay — 192×240](mansion_gameplay_preview_192x240.png) | [3× nearest neighbor](mansion_gameplay_3x.png) | [Direction / original proof / refinement / translation](gameplay_comparison.png) |
| [Story — 256×240](mansion_story_preview_256x240.png) | [3× nearest neighbor](mansion_story_3x.png) | [Direction / original proof / refinement / translation](story_comparison.png) |

## Direction and scope

The primary anchors are the [centered gameplay hall](references/gameplay-direction.png) and [offset story hall](references/story-direction.png) made and selected in this Work conversation. These are saved exact 192×240 and 256×240 reference exports of generated concepts, not authored game assets. Neither reference is sampled, traced, quantized or downscaled to produce this kit. They appear only in comparison boards. See [reference provenance](references/provenance.json).

The translation retains ruby rose glass, crimson bat-crested banners, pale fluted columns, pointed arcades, a red runner, dark perspective paving and a raised far dais. Pixel values are discrete palette entries, with stepped contours and no antialiasing, gradients or scene-level lighting effects. The palette is Famicom-inspired, not hardware-strict.

Gameplay puts a centered rose and triple-lancet elevation above the stair, leaving a quiet widening runner for the lower combat area. Story moves the focal wall to the right, steps the left gallery toward the viewer and sends the runner diagonally across a broad foreground. Its placement map is separate, not a widened gameplay crop. Existing V3 actors and dialogue coverage are shown in [gameplay scale](mansion_gameplay_scale.png) and [story staging](mansion_story_staging.png); these are static witnesses only.

## Canonical kit

Sixteen selected assets: **12 new, 1 revised, 3 reused**. The existing `v4-mansion-proof-column-01` is revised from r3 to r4 to strengthen pale shafts and capitals. The old proof still selects and preserves r3. Dark masonry r2, cornice r3 and far pier r2 are reused unchanged. New rose and paving reached r3 after one native-scale inspection correction; the other ten new pieces select r2. Exact IDs, revisions, hashes and approval-status snapshots are in [the manifest](robopixel_manifest.json); roles and dimensions are in [the inventory](asset_inventory.md).

[Atlas](asset_atlas.png) shows each independent building block. Rose and stair are special focal pieces; the other pieces are reusable. No full scene is stored as a canonical asset. New assets were created with `asset_create`; pixel grids were committed with `grid_paste`. The workflow uses the exposed RoboPixel authoring engine, never direct storage writes or product code changes.

`author_inputs.py` prepares explicit indexed grids using low-resolution integer raster primitives. It is an authoring aid, not the canonical result. `authoring_inputs.json` records final submitted rows; [transaction receipts](authoring_receipts.json) retain creation, first submissions and corrections. `robopixel_readback.json` preserves live export/view/approval responses; `unpack_readback.py` extracts the exact [export matrices](exports/) and [canonical PNG views](canonical_previews/).

## Reproduce and verify

Requires Python 3 and Pillow. From this directory:

```sh
python3 unpack_readback.py
python3 build_layouts.py
python3 compose.py
python3 review_context.py
python3 verify.py
```

`compose.py` consumes only read-back export matrices and `layouts.json`. It permits native placement, crop, repetition and horizontal reflection. Perspective floor courses and the runner are explicit native pixel-row placements; there is no resampling or recoloring. `build_layouts.py` regenerates those independent placement maps. Review enlargements alone use nearest-neighbor scaling. Labels and static actor/UI witnesses are not canonical environment art.

Verification checks all 16 independently rendered RoboPixel PNGs against exported matrices; submitted rows for authored pieces; revision/hash correspondence; unapproved status; exact scene reproduction; required files and sizes; asset use; opaque output and palette membership; and Git blob identity for every protected tracked file. The original proof at `13ff42307d5f008b8fa8ebce80f546b164067a1b` and the refinement at `44530dd918ce498544025ca1919e91faccb619d4` remain unchanged. The branch inherits those proof-only commits; its PR against main therefore also contains the preserved baselines.

## What this proves, and remaining gaps

This demonstrates a reference-led translation into reusable canonical pixels, real revision of an existing piece, exact read-back and two reproducible static compositions. It does not demonstrate runtime correspondence, live danmaku readability, animation, tile-budget/hardware compliance or final artistic acceptance. Approval status is recorded as false; no approval, validation waiver or delivery export was issued.

The result is deliberately lower-detail than the generated direction. Rose tracery is simplified and symmetrical; side architecture still repeats; floor reflections are restrained symbolic fragments rather than reflections of each placed column. Story depth is expressed through staggered native pieces and an offset dais, not a fully perspective-redrawn architectural set. Candelabra and thin pale columns may need contrast balancing in live combat. The Owner should judge those artistic gaps before any subsequent authoring or integration pass.
