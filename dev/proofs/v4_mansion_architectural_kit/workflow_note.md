# Workflow and boundary

## Canonical RoboPixel work

All ten kit assets were created with `asset_create` and authored through `grid_paste` in the existing `scarlet-moon-never-sets` project. An explicit indexed palette, immutable revisions, optimistic revision checks and unique idempotency keys were used. No fixture bootstrap, direct storage writes, formal approvals or delivery exports were used.

`author_grids.py` prepares exact pixel-grid tool inputs, including hand-stepped pointed arches, glass clusters, capital/base details, panel insets and the rose motif. It is a compact authoring aid; the authoritative result is the revision committed by RoboPixel. The pipeline reads the actual committed result back through `export_preview` and `asset_view`, rather than quietly rendering the original input instead.

Revision history records real iteration: revision 2 initial grids; revision 3 palette-index correction; floor and rose revision 4 refinements. The later masonry support is revision 2. Every selected revision, hash, PNG render hash, approval status and validation finding is preserved in the manifest/evidence files.

## Outside RoboPixel

`compose.py` places, crops, repeats and horizontally reflects native assets using Pillow. It never resamples or recolors assets, adds lighting, paints vector scene shapes, or loads the game. Columns are cap + repeated shaft + base from one canonical source. The runner consists of a tiled low-contrast field and repeated mirrored border wedges. Its footprint expands 4 pixels per 32-pixel segment.

The two composition lists are independent. Gameplay has receding side-bay placement around a long central corridor, with the apse at the top. Story presents the rear elevation across the width, a shallow dais, two actor positions and a broad foreground reserved for UI coverage. The floor uses native diamond paving; it is not mathematically convergent perspective.

PNG composition, atlas labels, 3× nearest-neighbor views, the HTML review page, static V3 sprite witnesses and documentation were assembled outside RoboPixel. No complete scene was uploaded as a fake reusable asset. No scene editor or tilemap feature was added to RoboPixel.

## Exact correspondence

For each asset, the Scarlet preview export reports `round_trip.cel_hash=true`. `verify.py` independently decodes its matrix and compares all RGBA bytes with the native `asset_view` PNG. It also checks exact equality between the recorded grid inputs and read-back rows, manifest/export/validation revision agreement, and unapproved status. All ten match. This is preview equivalence, not delivery approval.

## Concrete friction

1. The exposed `asset_create` tool description advertises `rgba` as string arrays. The live engine rejects strings and accepts numeric arrays. The first attempt failed before creation; numeric values resolved it. No server changes were made.
2. The current exposed tools do not offer a first-class multi-asset scene composition operation. This proof needs only a small external placement manifest and compositor; it does not demonstrate a need for a broad scene-system redesign.
3. Pixel-orphan lint flags deliberately separated diagonal pixels, cornice teeth and tiny glass/stone highlights. All validations pass but retain 106 warning findings in total, plus unused-palette informational findings. No waivers were recorded. Lint success is not an aesthetic quality certificate.
4. Shell Git push was unavailable in this workspace. The authorized GitHub tools persisted the checkpoint and final branch commits, including binary PNG blobs. This was transport friction, not an asset-workflow blocker.

No separate RoboPixel branch or new project was created. The durable candidates are the manifest's ten IDs in the existing project.
