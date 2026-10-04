# ROOFTOP WORKING STATIC-ART CANDIDATE — OWNER REVIEW REQUIRED

Static Mansion Rooftop / Remilia proof for #36, under #24 / #17; continuity #31.

## Review

- [Gameplay 3×](gameplay_3x.png), [native 192×240](gameplay_native.png)
- [Story 3×](story_3x.png), [native 256×240](story_native.png)
- [Complete 15-asset atlas](asset_atlas.png)
- [Gameplay current/reference/authored comparison](gameplay_comparison.png)
- [Story current/reference/authored comparison](story_comparison.png)
- [Gameplay witness](gameplay_witness_3x.png), [story witness](story_witness_3x.png)
- [Local review page](review.html), [asset IDs/revisions/hashes](asset_inventory.md)

## Exact source and recovery

Inspected and based on main `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8`.
Branch: `v4-mansion-rooftop-translation-01`.

The originating session's uncommitted files **did survive** the rate-limit interruption: both native compositions, integer layouts, canonical exports/readbacks, source captures, witnesses and authoring inputs. Recovery reverified all 15 current assets against the issue #36 checkpoint, and verified exact deterministic composition. It preserved these existing images/layouts without another art pass. These are the original surviving session layouts, not speculative reconstructions from a flattened image.

Selected revisions: r3 for mountain-range, paving-gameplay and paving-story; r2 for the other 12. All IDs begin `v4-rooftop-trans01-`. Exact hashes are in `manifest.json`, `selected_readback.json`, and `asset_inventory.md`.

## Provenance and workmanship

The two exact Owner-selected generated references are included in `reference/`; dimensions and SHA-256 values match issue #36. They were inspected as art direction. They were not traced, downscaled or inserted into production backgrounds. Only the comparison-board builder scales reference images for display.

Workmanship benchmarks inspected as images: Gate #29 at `796f76d4c173ce4ae5287d20d74d9c37b8f1c8c4`; Interior #22 at `c2241001946ac5456293f9f2b8be137e5c5bc648`. No scenery was copied from either.

Native cluster grids in `authoring/` were committed through RoboPixel `asset_create` and `grid_paste`. `selected_readback.json` preserves the actual canonical PNG transport, D7 matrix export, D3 render hash and asset description. `canonical/` contains those decoded exact PNG bytes; `exports/` contains exact selected preview exports. `readback.json` preserves the earlier all-r2 snapshot, **not** the selected source. `authoring/receipts.json` is a partial creation/edit receipt log; the selected readback and canonical service are authoritative for final revisions.

An initial bounded correction happened before the interruption: less repetitive paving, grouped mountain relief, and a genuinely separate asymmetric story view. Recovery did not revise art. The source grids and correction script serialize explicit authored pixel data; no reference sampling, polygon rasterization, ellipses or random texture generator was used for canonical art.

## Composition

`gameplay_layout.json` and `story_layout.json` are independent ordered layouts. The compositor uses only canonical PNGs, integer placement, explicit integer crops and reflection. It adds no scenery strokes. Gameplay uses a centered deep lane and side guardians. Story moves the moon toward the center, raises the rear parapet, changes the mansion mass and distant spire arrangement, and places one foreground guardian at the right. Story is neither stretched nor cropped gameplay.

`night-field` is the shared palette backdrop. Large pavement fields are independently authored to avoid forcing the scene into tiny tiles. The story field repeats a small visible strip below y=220; normal dialogue covers that region.

## Actual prior/current game inspection

Current V4 and V3 `ROOF` implementations are byte-identical; hashes are recorded in `current/source_correspondence.json`. Inspected actual source routing:

- 192×240 gameplay uses `drawRoof`, including Remilia boss and stage 3 after Sakuya / 70 seconds.
- Remilia before/after dialogue uses the independent 256-wide story sheet.
- Reimu is at (56,124); Remilia at (200,124); the dialogue frame begins at y=174.
- Remilia defeat uses the rooftop story background with the defeat actor path.
- Stage-3 card and attract preview also use the roof; the attract preview places Sakuya there at tick 1045. Remilia's subsequent attract card is black-backed.

`current/` images execute the unchanged drawing functions from the pinned source with a minimal DOM shim and `@napi-rs/canvas`. Chromium installation failed in this environment. These are **source-rendered evidence**, not live browser QA. The harness permits transparent output, disables the animation scheduler, and captures bounded states. Witnesses overlay the existing source-rendered actors/UI/bullets separately; the new environment is never inserted into a runtime file.

## Reproduce and verify

With Python 3 and Pillow, from this directory:

```sh
python compose.py --check
python verify.py
```

To regenerate native/3× images: `python compose.py`. To regenerate the review boards/atlas/manifest: `python package_review.py` (DejaVu Sans font required). Optional source-capture reproduction uses Node and `@napi-rs/canvas` via `CODEX_PRIMARY_RUNTIME_NODE_MODULES`: `node source_capture.cjs`. It must run against the pinned base game source. Do not rerun authoring scripts to mutate assets; they are development inputs, not a service mutation client.

`verification.json`: exact dimensions, zero mismatching RGBA pixels between export matrices and canonical PNGs, exact layout reproduction and 3× scaling, independent landmark placement, exact reference identity, protected runtime preservation. All 15 read-only lint projections pass, with **56 warnings** (pixel orphans) and **191 informational findings** (unused shared-palette colors). No waivers or formal approvals were recorded.

## Artistic self-review and limitations

Both scenes were inspected at native and 3× nearest-neighbor scale against the references and Gate/Interior benchmarks. The result uses stepped clusters, stone masses, separate distant mountains/forest, and restrained crimson lighting. It remains visibly simpler and sparser than the generated references. Pavement has long seams and quiet flat regions; parapets/clouds repeat; the gargoyle is a stylized small silhouette. These are Owner-review questions, not technically proven artistic success.

The static bullet witness retains a calm center, but the bright moon can overlap Remilia and reduce her silhouette contrast. No all-phase/motion readability, live browser equivalence, scrolling/animation, runtime integration, formal asset approval/delivery, merge, publication or release acceptance is claimed.

Protected V1–V3 and `versions/v4/index.html` are unchanged. Other scene branches/PRs are untouched. Stop for Owner review.
