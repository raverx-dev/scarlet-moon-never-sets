# Scarlet Moon V4 character reference packets

**Execution unit:** #42 — V4 character reference packets — complete cast preparation  
**Parent:** #28 · **Master plan:** #24  
**Status:** **V4 CHARACTER REFERENCE PACKETS — OWNER/MANAGER REVIEW REQUIRED**

This directory is the complete reference/research/package-preparation return for the six-character V4 lane. It contains **no canonical RoboPixel character art** and changes **no game/runtime code**.

## Read order

1. Open [review.html](review.html) for the cast-wide review surface.
2. Use the per-character packet for exact coverage, references, translation notes and artist-brief seed.
3. Use [manifest.json](manifest.json) for machine-readable provenance/state inventory.

## Authority stack

1. **Scarlet Moon current source + merged reconnaissance** — actual requirements, state names, native canvases, scene uses, anchors, selectors/timing, staging and unused definitions.
2. **Curated official Touhou references** — pose/orientation/silhouette/props/headwear vocabulary only. Never literal pixel-copy authority.
3. **Owner-approved V4 design sheet** — appearance, face/hair/headwear/costume/props/palette tendency and shared V4 cast language.
4. **V4 translation target** — a new deliberate late-Famicom/NES-style redraw. Not generic modern pixel art, not a direct PC-Touhou reproduction, and not a high-resolution illustration downscaled.

The latest #28 course correction supersedes the reconnaissance report's older suggested micro-unit production ordering. The report remains authoritative for inventory and live constraints.

## Baseline / source evidence

- Exact live baseline: d2586870b92551e931f784631ddfc891208df35b.
- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html — repository blob e86e9a8641356daf79fe0ae7ad80da3a25d0fdd4; preserved self-contained file SHA-256 7c66f576c6ef5ce12958dd3b99bfb98bc9b60ad34454f9f189775735af0b12bc.
- Live source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html. Character arrays are inline symbol-row data; this packet does not modify them.
- Current strategy precedence: #28 latest course correction supersedes the reconnaissance report's older micro-unit production sequence, but the reconnaissance inventory, state semantics, scene uses and runtime constraints remain authoritative.

## Packet status

| Character | Packet | Review path | Coverage |
|---|---|---|---|
| Reimu Hakurei | COMPLETE | [packet](reimu/README.md) | 12 required matrix rows |
| Marisa Kirisame | COMPLETE | [packet](marisa/README.md) | 5 required matrix rows |
| Cirno | COMPLETE | [packet](cirno/README.md) | 4 required matrix rows |
| Sakuya Izayoi | COMPLETE | [packet](sakuya/README.md) | 4 required matrix rows |
| Hong Meiling | COMPLETE | [packet](meiling/README.md) | 1 required matrix rows + 1 unused inventory row |
| Remilia Scarlet | COMPLETE | [packet](remilia/README.md) | 6 required matrix rows |

## Approved design-sheet provenance

The six sheets were supplied as one Owner-approved shared-session batch. Their binaries are not duplicated here; hashes make the exact inputs verifiable without bloating this research branch.

| Character | Exact supplied filename | Dimensions | SHA-256 | Repository disposition |
|---|---|---:|---|---|
| Reimu Hakurei | image-gen-1(20260927-092333).png | 1122×1402 | `2eb22de905cd9b4738f4b5540fd9f6c8167c828ecfb865becc05171ef9435f7a` | Not committed; exact Owner-approved input |
| Marisa Kirisame | image-gen-3(5).png | 1122×1402 | `b36b542d012b3d1a89198ae43d2feda0c9502bfc1e5b686c6807a355dbd20003` | Not committed; exact Owner-approved input |
| Cirno | image-gen-2(20260927-092334).png | 1122×1402 | `3722af4d2914d212dfb993af17bacfe8d6b373bb46974175858922d9a913811f` | Not committed; exact Owner-approved input |
| Sakuya Izayoi | image-gen-5(3).png | 1122×1402 | `4b743abd1410b4f7b1154855349509d19f53b8485fcc4ebc30767748520e332a` | Not committed; exact Owner-approved input |
| Hong Meiling | image-gen-4(4).png | 1122×1402 | `4f7741ab795936039491516e9631cd9c8d73671820e556d4be709a2ad5c9a951` | Not committed; exact Owner-approved input |
| Remilia Scarlet | image-gen-6(3).png | 1122×1402 | `ffee33a38617885a585ea5d4eb0431d176820c4ec21363c8ba317f9009d09265` | Not committed; exact Owner-approved input |

## Cross-cast rules

- Preserve each character's **actual** native canvas and state semantics; do not invent symmetric requirements across the cast.
- Fix continuity defects through art, not mechanics: stable apparent body scale, stable anchors, deliberate wings/props/headwear, and clear state differentiation.
- Portraits are clipped to a 32×32 interior. Combat is the 192×240 playfield plus HUD; story/presentation is 256×240.
- Idle A/B selector cadence and special-state triggers remain runtime contracts, not artist choices.
- Defeat sequences reuse body art plus staging/movement; they do not imply hidden defeat sprite families.
- Special independent presentation art stays independent: Reimu title, Marisa book concern, Remilia parasol and attract, Meiling's sleeping-only active use.
- Do not import official sprite pixels or third-party sheets. Curated links explain what to learn and what **not** to copy.
- Reimu rejected r2 remains negative evidence only: technically valid but over-simplified, weakly differentiated and below the V4 identity/quality target.

## Reimu orientation discrepancy recorded, not hidden

#42 explicitly asks that official rear-facing/player-shooter Reimu references be included. The live Scarlet Moon source and merged reconnaissance still describe/render the gameplay body as **side-facing**. This package therefore includes official rear-facing material as required vocabulary/comparison, while treating the current Scarlet Moon orientation as the live state contract. A future canonical orientation change requires explicit Owner/Manager direction; this documentation branch does not silently make that change.

## Copyright / repository policy

No official Touhou sprite sheets or other third-party art are copied into this directory. External material is represented by source links and production-use notes only. Owner-approved generated design-sheet binaries are also not duplicated; exact filenames, dimensions and SHA-256 hashes are preserved above.

## Non-scope confirmation

This branch only adds files beneath `dev/reviews/v4_character_reference_packets/`. It does **not** change `versions/v4/index.html`, canonical RoboPixel assets, gameplay, selectors, hitboxes, animation timing, scenes, V1–V3 history, integration, publication or release state.
