# Hong Meiling — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is pose/silhouette/prop vocabulary only. The Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved sheet supplied to the coordinator: **image-gen-4(4).png**, 1122×1402, SHA-256 `4f7741ab795936039491516e9631cd9c8d73671820e556d4be709a2ad5c9a951`
- Sheet binary is intentionally **not copied into this repository**. The filename + hash identify the exact Owner-approved input that must be supplied to the later artist.

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `meilingSleep` | 24×16 | Mansion gate arrival and credits, both drawn at 2× | Sleeping gatekeeper | Reusable active presentation sprite | This is the actual production requirement. Current placements: gate (204,186)×2 and credits (128,165)×2. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L869) |
| `meiling` | 16×16 | No live call site found | Standing definition | Inventory only — NOT a production requirement | Keep documented so it is not accidentally mistaken for a missing boss/dialogue family. Do not create a new role from this unused definition. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L851) |

## 2. Current Scarlet Moon evidence

- Current standing definition is at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L851 and sleeping definition at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L869.
- Credits draw meilingSleep at 2× at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2093; gate draws the same 24×16 sprite at 2× at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2108.
- Reconnaissance found no Meiling portrait, boss, defeat, dialogue or title call site. The 16×16 standing definition is explicitly unused.
- Reconnaissance source-rendered evidence and full frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Curated official Touhou reference set

1. **Embodiment of Scarlet Devil Hong Meiling — character page** — Official EoSD boss/design identity.
   - Source: https://en.touhouwiki.net/Hong_Meiling
   - Teaches: Scarlet hair, green beret/dress, traditional-Chinese silhouette and gold-star/dragon cap vocabulary.
   - Do not copy: Do not turn the official standing/boss pose into a new Scarlet Moon combat or dialogue requirement.
2. **Embodiment of Scarlet Devil official image archive** — Th06 Hong/Meiling sprite and artwork cross-check.
   - Source: https://en.touhouwiki.net/wiki/Category:Embodiment_of_Scarlet_Devil_Images
   - Teaches: How compact official boss art reduces the red/green silhouette, useful for identity even though Scarlet Moon needs a sleeping pose.
   - Do not copy: Do not copy official boss pixels or infer unused states from the archive.

These are reference links/metadata only. No third-party sprite sheet is copied into the repository.

## 4. Owner-approved V4 design sheet

- Long scarlet/red hair, green beret with gold star/dragon-emblem cue, and green Chinese-style tunic.
- White baggy trousers and dark/gold guards/footwear create a strong lower-body contrast.
- The approved sheet includes a simplified sleeping pose, directly useful to Scarlet Moon's actual active requirement.
- For the 24×16 sleeping asset preserve red-hair mass + green cap/body + white trouser read; do not force standing-sheet detail into the horizontal silhouette.

The sheet is a design authority, not an exact pose blueprint. Generated labels or ornamental details that conflict with actual character identity or the live Scarlet Moon contract are non-authoritative.

## 5. Translation notes

- Design the actual 24×16 sleeping silhouette first, because that is what the game shows at 2×; test both native 1× and exact 2× nearest-neighbor.
- Use red hair, green cap/body and white clothing as three large readable masses; gold ornament is optional micro-detail.
- The approved sheet's sleeping study is appearance guidance, not a pixel pose blueprint; reconcile it to the current horizontal canvas/placement.
- Keep the 16×16 standing definition in inventory only. Do not author a new boss/dialogue/portrait family unless scope changes later.

The translation equation for the later artist is:

**Scarlet Moon state contract + official Touhou visual vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.**

## 6. Production-brief seed

> Author only Meiling's active V4 requirement: the 24×16 sleeping gatekeeper sprite, designed to read cleanly at the game's exact 2× gate/credits scale. Use official Meiling material for red-hair/green-cap/Chinese-costume identity and the approved sheet's sleeping study for V4 appearance. The existing 16×16 standing definition remains unused inventory and does not authorize new combat/dialogue art.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
