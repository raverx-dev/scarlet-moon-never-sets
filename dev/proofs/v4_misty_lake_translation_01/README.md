# Misty Lake — static art candidate 01

**MISTY LAKE ART CORRECTION — OWNER REVIEW REQUIRED**

The candidate at `90a6d3efbebcdd8ca30cb937086ad164e63a6396` was rejected by the Owner.
This is one bounded correction on the same PR #34 and same branch.
Before-state exports, renders, manifest, layouts and validation are in `before/`;
the original head and original transport payloads remain retrievable.

Open `review.html` for both native views, 3× enlargements, exact source comparisons,
separate readability witnesses, atlas and reference viewing thumbnails. It is self-contained.
GitHub transport is text-only: exact PNG bytes are preserved in `transport/`.
Run `python hydrate.py` in a fresh checkout to restore all 41 exact PNG files, then run the check below.

## Authority and source

- Workstream #32; production #24; Manager continuity #31; program #17.
- Inspected main: `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8`.
- `versions/v4/index.html`: LAKE at line 1323; drawMistyLake at 1954; Stage 1 background at 1993;
  dialogue at 2035–2047; attract at 2076; stagecard at 2107; defeat at 2111.
- V3 `versions/sprite-redesign/index.html` and V4 LAKE reconstructions have identical RGBA.
- Story anchors: Reimu (56,124), Cirno (196,108), dialogue panel (4,174). Current story actors
  float above the shoreline; actor position/orientation is preserved only in illustrative witnesses.
- Gameplay boss origin (96,45); representative Reimu witness (96,206).
- Source reconstructions are extracted static matrices, not live browser captures.

## Approved references

Image A is the supplied gameplay reference; Image B is the supplied story reference.
Original bytes and SHA-256 identities are preserved losslessly in `transport/` and `manifest.json`;
`hydrate.py` restores them into `references/` and all other PNG paths.
Neither image was regenerated, traced, sampled for colors, nor downscaled into production.
Reference resizing occurs only inside the clearly labelled comparison boards.

The interpretation preserves blue night water, scarlet moon and off-centre reflection,
wooded slopes, distant torii/lights, frost, rock banks and reeds. Gameplay keeps an open central
water lane. Story independently frames the lake with a left tree and diagonal lower shore.
The kit uses 23 opaque colors plus transparency; detailed generated-reference microtexture is simplified.

## Reproduce

Python 3 + Pillow (tested 12.3.0):

```sh
python hydrate.py
python compose.py --check
```

This needs only the committed canonical exports, render evidence, source matrices, references and layouts.
No RoboPixel service, GitHub, authoring generator or game runtime is needed to reproduce the selected proof.
`python compose.py` rebuilds outputs. `python package.py` rebuilds review/provenance.
`node extract-baseline.cjs` re-extracts baseline evidence only when the repository files match the pinned source.

`author.py` and `draft-grids.json` are REJECTED BEFORE-state drafting evidence, not the compositor's inputs or
a replacement for canonical RoboPixel state. For future edits reopen the exact asset ID with an
expected current revision; persist a new revision, read it back, then update proof inputs.

## Verification

- 19/19 canonical export matrices exactly match decoded RoboPixel PNG RGBA; zero pixel differences.
- 19/19 Scarlet adapter logical round trips pass.
- Native outputs are opaque 192×240 and 256×240; layouts are distinct.
- 37 generated PNGs reproduce byte-for-byte with `compose.py --check`.
- 19/19 RoboPixel validation reports pass, with 168 pixel-orphan warnings and 330 unused-color information findings.
  These concern fine stars/frost/texture and a shared family palette. They remain visible and unwaived;
  technical validation is not a visual quality approval.
- Runtime and protected versions are untouched. No unrelated branch or asset was changed.

## Correction 01

All 19 canonical assets were inspected against the existing scene, approved references and
accepted Mansion Gate native previews/atlas. Thirteen were revised, six retained. Palette and
both layout files remain unchanged. No new asset IDs were created.

- Reeds: thick grouped blades, restrained seedheads and substantial shadow bases.
- Shore tree: stepped trunk/bark blocks, broader branch junctions and frost foliage masses.
- Ridges/banks: connected foliage clusters, broken ridge steps and nested rock/shadow patches.
- Water/reflection: sparse authored wave groups and broken red light fragments, with calmer gaps.
- Clouds/moon/mist: explicit stepped token grids and limited highlight clusters.
- Story shore: layered turf/frost and soil groups along the original diagonal.
- Atlas: fixed height calculation so all 19 assets, including the shore tree, are visible.

| Canonical asset | Old → selected revision |
| --- | --- |
| `v4-misty-lake-trans01-scarlet-cloud` | 3 → 4 |
| `v4-misty-lake-trans01-scarlet-moon` | 2 → 3 |
| `v4-misty-lake-trans01-far-ridges` | 3 → 4 |
| `v4-misty-lake-trans01-west-woods` | 2 → 3 |
| `v4-misty-lake-trans01-east-woods` | 2 → 3 |
| `v4-misty-lake-trans01-mist-bank` | 3 → 4 |
| `v4-misty-lake-trans01-scarlet-reflection` | 2 → 3 |
| `v4-misty-lake-trans01-blue-ripples` | 2 → 3 |
| `v4-misty-lake-trans01-frosted-point` | 2 → 3 |
| `v4-misty-lake-trans01-deep-water` | 2 → 3 |
| `v4-misty-lake-trans01-silver-reeds` | 2 → 3 |
| `v4-misty-lake-trans01-story-shore` | 2 → 3 |
| `v4-misty-lake-trans01-shore-tree` | 3 → 4 |

Retained at r2: twilight, distant-torii, boulder, flat-stones, small-rock and ice-cluster.
The rocks/ice retain useful compact facets; the torii remains a distant landmark, and the
sky remains a low-detail backing. No formal approvals or deliveries were recorded.

Before/corrected gameplay and story comparisons plus the seven-asset comparison are in `previews/`
after hydration and embedded in `review.html`. Approval-reference comparisons and witnesses remain included.

## Canonical selected revisions

| Asset ID | Revision | Native size |
| --- | ---: | --- |
| `v4-misty-lake-trans01-twilight` | 2 | 256×88 |
| `v4-misty-lake-trans01-scarlet-cloud` | 4 | 128×44 |
| `v4-misty-lake-trans01-scarlet-moon` | 3 | 28×28 |
| `v4-misty-lake-trans01-far-ridges` | 4 | 256×53 |
| `v4-misty-lake-trans01-west-woods` | 3 | 112×65 |
| `v4-misty-lake-trans01-east-woods` | 3 | 104×53 |
| `v4-misty-lake-trans01-distant-torii` | 2 | 22×20 |
| `v4-misty-lake-trans01-mist-bank` | 4 | 112×18 |
| `v4-misty-lake-trans01-scarlet-reflection` | 3 | 44×160 |
| `v4-misty-lake-trans01-blue-ripples` | 3 | 64×128 |
| `v4-misty-lake-trans01-frosted-point` | 3 | 76×58 |
| `v4-misty-lake-trans01-deep-water` | 3 | 128×128 |
| `v4-misty-lake-trans01-boulder` | 2 | 30×26 |
| `v4-misty-lake-trans01-flat-stones` | 2 | 38×18 |
| `v4-misty-lake-trans01-small-rock` | 2 | 17×15 |
| `v4-misty-lake-trans01-ice-cluster` | 2 | 18×24 |
| `v4-misty-lake-trans01-silver-reeds` | 3 | 30×38 |
| `v4-misty-lake-trans01-story-shore` | 3 | 256×91 |
| `v4-misty-lake-trans01-shore-tree` | 4 | 81×115 |

All IDs belong to project `scarlet-moon-never-sets`, frame `default`, layer `art`.
Full revision, render, palette, RGBA and PNG hashes are in `manifest.json` and the exact readback records.

## Package inventory

- `exports/`: D7 canonical matrices plus 19 exact D3 PNG exports.
- `evidence/`: D3 PNG transport/readbacks, D9 validation, D6 mutation receipts and pinned source matrices.
- `layouts.json`, `layout.py`, `compose.py`: explicit independent scenes and deterministic build/check logic.
- `previews/`: native/3× scenes, atlas, V3/V4 reconstructions, comparison boards and separate static witnesses.
- `references/`: both unchanged Owner-selected images.
- `manifest.json`, `verification.json`, `README.md`, `review.html`, `changed-files.txt`: provenance and review.
- `correct_clusters.py`, `correction-grids.json`: explicit native correction grids; each character is one pixel.
- `author.py`, `draft-grids.json`: historical rejected-before drafting evidence only.
- `palette.json`, `extract-baseline.cjs`, `package.py`: reproduction/packaging evidence.

## Limits and stop

Static proof only. No animated mist, moving-bullet test, in-game performance or defeat/attract routing qualification.
The story witness uses original sprites and a substitute static text font; it does not fix known Cirno orientation.
The corrected crags/clouds remain stylized and some reusable foliage motifs remain recognizable;
only the Owner can decide whether their craftsmanship now meets the desired standard.
Owner visual acceptance remains pending. No formal per-asset delivery, runtime integration, merge,
publication, freeze or release acceptance is claimed. Corrections should stay on this branch/PR.
