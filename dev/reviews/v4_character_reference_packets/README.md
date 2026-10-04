# Scarlet Moon V4 character reference packets

**Execution unit:** #42 — V4 character reference packets — complete cast preparation  
**Parent:** #28 · **Master plan:** #24  
**Status:** **V4 CHARACTER REFERENCE PACKETS — OWNER/MANAGER REVIEW REQUIRED**

This directory is the complete reference/research/package-preparation return for the six-character V4 lane. It contains **no canonical RoboPixel character art** and changes **no game/runtime code**.

## Read order

1. Open [review.html](review.html) for the cast-wide visual/reference review.
2. Use each per-character packet for exact coverage, selected official references, translation notes and artist-brief seed.
3. Use [manifest.json](manifest.json) for machine-readable provenance/state inventory.
4. Exact Owner-approved design-sheet binaries are committed under [design-sheets/](design-sheets/).

## Authority stack

1. **Scarlet Moon current source + merged reconnaissance** — actual requirements, state names, native canvases, scene uses, anchors, selectors/timing, staging and unused definitions.
2. **Selected official Touhou sprite/sheet/state references** — exact inspect targets for pose/orientation/silhouette/props/headwear vocabulary only. Never literal pixel-copy authority.
3. **Committed Owner-approved V4 design sheet** — appearance, face/hair/headwear/costume/props/palette tendency and shared V4 cast language.
4. **V4 translation target** — a new deliberate late-Famicom/NES-style redraw. Not generic modern pixel art, not a direct PC-Touhou reproduction, and not a high-resolution illustration downscaled.

The latest #28 course correction supersedes the reconnaissance report's older suggested micro-unit production ordering. The reconnaissance remains authoritative for inventory, state semantics and live runtime/staging constraints.

## Reimu V4 gameplay orientation — resolved

**Owner decision on #28: V4 Reimu gameplay is rear-facing/back-view.**

The current V3/current-V4 side-facing gameplay pixels remain historical/source evidence only and are **not** the V4 orientation target. This changes art direction, not mechanics. Preserve:

- `reimu` / `reimuB` / `reimuFocus` / `reimuFire` meanings;
- 16×24 body canvases;
- separate 10×14 / 12×14 gohei extents;
- current player coordinates and body/prop anchoring contract;
- hitbox and movement bounds;
- selectors, timing, clipping and gameplay staging.

The selected TH07/TH08 official playable-character sheets in the Reimu packet are the primary rear-facing shooter vocabulary. The rejected Astra/r2 back-view work remains rejected; the orientation decision does **not** promote its design.

## Baseline / source evidence

- Exact live baseline: `d2586870b92551e931f784631ddfc891208df35b`.
- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html — repository blob `e86e9a8641356daf79fe0ae7ad80da3a25d0fdd4`; preserved self-contained file SHA-256 `7c66f576c6ef5ce12958dd3b99bfb98bc9b60ad34454f9f189775735af0b12bc`.
- Live source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html. Character arrays are inline symbol-row data; this reference branch does not modify them.

## Packet status

| Character | Packet | Review path | Coverage |
|---|---|---|---|
| Reimu Hakurei | COMPLETE | [packet](reimu/README.md) | 12 required matrix rows |
| Marisa Kirisame | COMPLETE | [packet](marisa/README.md) | 5 required matrix rows |
| Cirno | COMPLETE | [packet](cirno/README.md) | 4 required matrix rows |
| Sakuya Izayoi | COMPLETE | [packet](sakuya/README.md) | 4 required matrix rows |
| Hong Meiling | COMPLETE | [packet](meiling/README.md) | 1 required matrix rows + 1 unused inventory row |
| Remilia Scarlet | COMPLETE | [packet](remilia/README.md) | 6 required matrix rows |

## Committed Owner-approved design sheets

| Character | Exact binary | Dimensions | Bytes | SHA-256 | Repository path |
|---|---|---:|---:|---|---|
| Reimu Hakurei | [`image-gen-1(20260927-092333).png`](design-sheets/image-gen-1(20260927-092333).png) | 1122×1402 | 2155565 | `2eb22de905cd9b4738f4b5540fd9f6c8167c828ecfb865becc05171ef9435f7a` | `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-1(20260927-092333).png` |
| Marisa Kirisame | [`image-gen-3(5).png`](design-sheets/image-gen-3(5).png) | 1122×1402 | 2265744 | `b36b542d012b3d1a89198ae43d2feda0c9502bfc1e5b686c6807a355dbd20003` | `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-3(5).png` |
| Cirno | [`image-gen-2(20260927-092334).png`](design-sheets/image-gen-2(20260927-092334).png) | 1122×1402 | 2100443 | `3722af4d2914d212dfb993af17bacfe8d6b373bb46974175858922d9a913811f` | `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-2(20260927-092334).png` |
| Sakuya Izayoi | [`image-gen-5(3).png`](design-sheets/image-gen-5(3).png) | 1122×1402 | 2195028 | `4b743abd1410b4f7b1154855349509d19f53b8485fcc4ebc30767748520e332a` | `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-5(3).png` |
| Hong Meiling | [`image-gen-4(4).png`](design-sheets/image-gen-4(4).png) | 1122×1402 | 2170592 | `4f7741ab795936039491516e9631cd9c8d73671820e556d4be709a2ad5c9a951` | `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-4(4).png` |
| Remilia Scarlet | [`image-gen-6(3).png`](design-sheets/image-gen-6(3).png) | 1122×1402 | 2229817 | `ffee33a38617885a585ea5d4eb0431d176820c4ec21363c8ba317f9009d09265` | `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-6(3).png` |

These are the exact Owner-approved generated V4 design inputs. Their binary identity is part of packet provenance. Official Touhou material is **not** committed; it remains link/metadata-only.

## Cross-cast rules

- Preserve each character's actual native canvas and state semantics; do not invent symmetric requirements.
- Fix visual continuity through art, not mechanics: stable apparent body scale, stable anchors, deliberate wings/props/headwear and clear state differentiation.
- Portraits are clipped to a 32×32 interior. Combat uses the 192×240 playfield plus HUD; story/presentation uses 256×240.
- Idle A/B cadence and special-state triggers remain runtime contracts, not artist choices.
- Defeat sequences reuse body art plus staging/movement; they do not imply hidden defeat sprite families.
- Special independent presentation art stays independent: Reimu title, Marisa book concern, Remilia parasol/attract, Meiling sleeping-only active use.
- Reimu rejected r2 remains negative evidence only.

## Copyright / repository policy

Only Owner-approved generated V4 design-sheet binaries are committed here. Official Touhou/third-party sprite sheets are represented by selected archival links and inspection notes only; none are copied into the repository.

## Non-scope confirmation

This branch adds/updates only reference-package material beneath `dev/reviews/v4_character_reference_packets/`. It does **not** change `versions/v4/index.html`, canonical RoboPixel assets, gameplay, selectors, hitboxes, movement, animation timing, scenes, V1–V3 history, integration, publication or release state.
