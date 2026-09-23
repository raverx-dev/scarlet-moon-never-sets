# Mansion Art Development 01 — candidate artwork

One Mansion-only art pass on the two **accepted compositions** at `4ef4080fc17f53f03393ac74e205220072360c0b`. Both placement maps are byte-identical to that checkpoint. No viewpoint, proportion, focal axis, carpet/stair join, actor anchor or dialogue coverage was changed. Artwork remains provisional; Owner visual review is required.

| Scene | Native PNG | Direct accepted → developed comparison |
|---|---|---|
| Gameplay | [192×240](mansion_gameplay_preview_192x240.png) | [Before/after](gameplay_art_before_after.png) |
| Story/dialogue | [256×240](mansion_story_preview_256x240.png) | [Before/after](story_art_before_after.png) |

[Gameplay 3×](mansion_gameplay_3x.png) · [Story 3×](mansion_story_3x.png) · [Asset atlas](asset_atlas.png)

## Art changes

Twelve existing canonical assets were revised, with no new assets:

- **Rose:** pointed petal lights, interlocking ruby facets, secondary lights, radial stone tracery, segmented outer moulding and corner leafwork. Its footprint and focal position are unchanged.
- **Architecture:** crocketed arch shoulders, nested side tracery, carved dados, acanthus capitals, recessed column flutes, collars, plinth panels, pierced balustrades and articulated cornice teeth.
- **Glass and fabric:** leaded diamond lancets with restrained cool facets; velvet folds and embroidered crescent/bat banners; woven runner edging.
- **Materials and lighting:** tapered candle flames and scrolling brass arms; beveled stair treads, inset risers and carpet edging; fragmented cool stone reflections.

The runner field, runner motif, masonry and far pier retain their exact previously selected revisions. In particular, the lower central combat lane is pixel-identical to the accepted image. No new decoration was added to its center. One native-scale inspection adjustment filled out initially sparse rose glass and reduced floor-reflection contrast within this pass.

The full-scene [gameplay direction](references/gameplay-direction.png) and [story direction](references/story-direction.png) remain the art references. The corrected near-frontal story camera supersedes the reference's angle. Reference image pixels are not sampled, traced, resized or quantized into assets; they appear only in review boards.

## Exact canonical evidence

[Inventory](asset_inventory.md) and [manifest](robopixel_manifest.json) record exact asset IDs, before/after revisions, revision/render hashes and approval status. [Receipts](authoring_receipts.json) retain every mutation in this pass. [Live read-back](robopixel_readback.json) contains the initial current-head checks, final export matrices, independent canonical PNGs and approval responses.

`art_development_inputs.py` prepares indexed native pixel grids from immutable accepted exports in Git. Its integer raster operations are authoring inputs, not scene-level painting. Those grids were committed through RoboPixel `grid_paste` with exact expected revisions. Every final scene consumes only the actual read-back [exports](exports/), which match independent [canonical PNG views](canonical_previews/). There are no full-scene canonical assets, concept downscales, interpolation, recoloring, gradients or painted lighting in the compositor.

Selected revisions: rose r3→r5, paving r3→r5, column r4→r5, cornice r3→r4; arch, lancet, banner, near pier, stairs, balustrade, candelabra and runner edge r2→r3. Four remaining assets are unchanged. Every selected asset remains unapproved; no delivery export or approval was issued.

## Composition, staging and verification

The accepted `layouts.json` and `build_layouts.py` are unchanged. `compose.py` only places, crops, repeats and reflects exact exported pixels. [Accepted checkpoint](accepted_composition_checkpoint/) preserves both native images, both actor/UI witnesses, exact layouts and the prior asset manifest. The full original kit is retrievable at the recorded Git head. Earlier original/refinement packages and rejected-angle/correction history are intact.

[Gameplay scale](mansion_gameplay_scale.png) and [story dialogue coverage](mansion_story_staging.png) use unchanged V3 sprite matrices and anchors. [Fixed bullet comparison](bullet_readability_before_after.png) overlays identical V3 diamond/star primitives on the accepted and developed scenes; [witness metadata](bullet_witnesses.json) records exact colors and placements. It is a static contrast sample, not live combat QA.

Requires Python 3 and Pillow. From this directory:

```sh
python3 unpack_readback.py
python3 compose.py
python3 review_context.py
python3 art_review.py
python3 verify_art_development.py
```

The [current verification](art_development_verification.json) checks all 16 canonical PNG/export correspondences, final submitted grids, exact native reproduction, byte-identical layout/source and staging, preserved accepted evidence, unchanged quiet center, continuous story stair-to-carpet color path, protected repository files and candidate approval status. `verify_story_correction.py` and its report are historical checks for the previous correction head, not the gate for this art pass.

## Remaining limitations

This is still more schematic than the rich reference: repeated side bays, stylized rather than physically matched reflections, and compact symmetrical rose tracery. Lighting remains discrete highlights rather than animated candlelight. The fixed bullet witness samples only two shapes and does not establish dense moving-pattern readability. Final aesthetics, runtime correspondence and hardware constraints have not been approved or qualified.

No playable V4 or frozen-version changes, other environments, RoboPixel product changes, runtime integration, merge, deployment, publication or formal asset approval.
