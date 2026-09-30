# Hakurei Shrine Translation 01

**SHRINE WORKING STATIC-ART CANDIDATE — OWNER REVIEW REQUIRED**

Static environment proof for #38, under #24 / #17; Manager continuity #31.
Branch: `v4-shrine-translation-01`.
Verified source/base: `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8`.

## Review

- [Night native](night_native.png) · [Night 3×](night_3x.png)
- [Morning native](morning_native.png) · [Morning 3×](morning_3x.png)
- [Complete 22-asset atlas](asset_atlas.png)
- [Night current → reference → authored](night_comparison.png)
- [Morning current → reference → authored](morning_comparison.png)
- [Opening dialogue witness](witnesses/intro_dialogue_3x.png)
- [Ending dialogue witness](witnesses/ending_dialogue_3x.png)
- [Visual review page](review.html)

The two backgrounds are exactly 256×240. Their 768×720 previews use nearest-neighbor scaling. Backgrounds contain no actors or UI. The ending witness omits the background donation box and places the exact canonical box at the existing story anchor instead.

## Surviving work and recovery

The interrupted authoring session preserved all 22 canonical assets at revision 2, exact PNG readbacks and Scarlet Moon adapter exports, authoring receipts and token grids, both independent layouts, native compositions, previews, atlas, comparisons and source-rendered current-game evidence. Recovery reused these files without recreating or revising artwork. `recovery_inventory.json` records the live project inventory checked against every saved revision hash. Only witnesses, documentation and packaging were completed during recovery.

## Sources and separation

1. `references/`: exact Owner-approved concept images. Neither is sampled, traced or downscaled into production pixels. Resized copies appear only in labeled comparison boards.
2. `assets/` and `exports/`: exact canonical RoboPixel r2 PNG renders and Scarlet Moon preview exports. These are candidate previews, not formal approval/delivery.
3. `night_layout.json`, `morning_layout.json`, `compose.py`: independent scene layouts, integer placement and deterministic composition. Shared architecture retains location continuity; morning has separate sky, mist, light accents, doorway treatment and courtyard shadow pixels, plus a different mountain placement.
4. `current/`: actual V3 and current V4 drawing functions executed in headless Canvas2D, including original actors/UI when appropriate. These are source-rendered static evidence, not live browser captures or gameplay QA.
5. `witnesses/`: illustrative source actor/dialogue overlays on the candidate backgrounds. Disposable VM overrides substitute only the background and donation-box draw for the witness; no game file is edited.

## Source inspection and routing

Both `versions/sprite-redesign/index.html` (V3) and `versions/v4/index.html` were inspected at the source/base above. Their Shrine routes and staging are shared:

| Use | Current behavior / requirement |
| --- | --- |
| Opening | `newRun` → `showDialogue('intro', ..., 'shrine')`; Reimu at (70,146). Three nights without sunrise/visitors. |
| Night environment | `shrine(false,...)`: sky/moon, trees, torii, hall, lanterns, approach and donation box. |
| Notice | Night Shrine with donation suppressed; large legal notice overlay. |
| Relevant night story | Attract's existing Shrine and donation close-up uses were inspected for identity only; its presentation redesign is outside this task. |
| Dawn | Rooftop lunar anchor until tick 190; moon/horizon transition until tick 370; then morning ending. No Shrine-art substitution is claimed for this transition. |
| Morning arrival | `endingScene`: Reimu (58,174), Remilia enters with parasol, coin descends to donation anchor. |
| Ending dialogue | `showDialogue('ending', ..., 'morning')`: Reimu (64,136), Remilia (168,124), donation (112,148), coin (112,140). |
| Ending exit | Reimu remains, Remilia moves right, donation at (88,175). |
| THE END | Morning Shrine, characters/coin/box, text at y62 and y96. |

Dialogue frame begins at (4,174), covering the bottom 66 pixels. Source-rendered evidence for opening, notice, dawn, ending arrival/dialogue/exit and THE END exists for both V3 and V4. Exact dialogue text is retained in `current/*_dialogue.json`. No Title/attract/credits family is authored here.

## Workmanship review and limitations

Inspected primary Gate benchmark: #30 / PR #29 at `796f76d4c173ce4ae5287d20d74d9c37b8f1c8c4`; secondary Interior: #20 / PR #22 at `c2241001946ac5456293f9f2b8be137e5c5bc648`. Exact story PNGs are retained in `benchmarks/` for comparison. Their pixel masses, material detail and negative space informed workmanship; their Gothic scenery was not reused.

The initial local assembly had roof gaps and empty backing behind the hall. One bounded correction, completed before the selected canonical r2 assets were committed, joined the roof, added woods/facets/courtyard chips and corrected the Scarlet Moon palette. Recovery performed no further polish.

The candidate preserves a frontal Japanese shrine, curved central gable, sacred rope/shide, torii, donation box, stone lanterns and layered environment. It has solid pillars and explicit pixel clusters, rather than thin wire architecture. Night/morning share the same architectural anchors; morning changes more than palette.

Remaining limitations for Owner review:

- The mountain silhouette is still a broad, simple ridge. Facets and distant cedar shapes visibly repeat; foliage is more stylized and less varied than the references.
- Roof courses and courtyard joints remain regular. The large foreground slabs and blocky morning shadows are flatter than the references and the strongest Gate details.
- The shrine's ornate gable is simplified; surrounding subsidiary structures and much of the reference's landscape depth are omitted for native-size clarity.
- Existing source actor anchors cause Reimu to overlap the torii post and Remilia to overlap the hall. Witnesses deliberately expose this future staging issue. They do not certify integration readiness or THE END text readability on the new background.
- No live runtime, animation, collision, accessibility, gameplay or full RoboPixel artistic-policy acceptance is claimed.

Technical validation is not artistic acceptance. Stop for Owner review; no integration, merge, formal approval/delivery or publication.

## Canonical inventory

All IDs use prefix `v4-shrine-trans01-`. Each row lists two separate canonical assets, both selected at **r2**. Exact full IDs, revision hashes, render hashes, PNG SHA-256 hashes and readback descriptions are in `asset_manifest.json`.

| Asset suffix | Night | Morning |
| --- | --- | --- |
| sky | `sky-night` r2 | `sky-morning` r2 |
| mountain-depth | `mountain-depth-night` r2 | `mountain-depth-morning` r2 |
| wooded-frame | `wooded-frame-night` r2 | `wooded-frame-morning` r2 |
| hall-roof | `hall-roof-night` r2 | `hall-roof-morning` r2 |
| hall-body | `hall-body-night` r2 | `hall-body-morning` r2 |
| courtyard | `courtyard-night` r2 | `courtyard-morning` r2 |
| approach-stairs | `approach-stairs-night` r2 | `approach-stairs-morning` r2 |
| torii | `torii-night` r2 | `torii-morning` r2 |
| stone-lantern | `stone-lantern-night` r2 | `stone-lantern-morning` r2 |
| donation-box | `donation-box-night` r2 | `donation-box-morning` r2 |
| foreground-banks | `foreground-banks-night` r2 | `foreground-banks-morning` r2 |

## Reproduction

Python 3 + Pillow are sufficient for canonical composition and verification:

```sh
python compose.py --check
```

This checks both native images and 3× previews, atlas/comparisons, PNG/export correspondence, exact authoring-grid correspondence, selected revision identities against receipts, reference hashes/dimensions and byte preservation of every base-tracked file. `python compose.py` rebuilds presentation images from canonical PNGs; it never authors or updates RoboPixel assets.

For optional source evidence/witness reproduction, Node.js plus `@napi-rs/canvas` are required; set `CODEX_PRIMARY_RUNTIME_NODE_MODULES` to the node_modules directory containing it. Run `node capture_current.cjs` for current-game evidence and `node build_witnesses.cjs --check` to verify native witnesses. The witness-only morning background is canonical composition with the donation-box placement omitted. 3× witness previews use Pillow nearest-neighbor scaling.

`manifest.json` records source identities and the proof-file hashes. `verification.json` records deterministic checks. All additions are confined to this proof directory; runtime and unrelated branches/PRs remain untouched.
