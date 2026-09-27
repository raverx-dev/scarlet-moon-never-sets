# Hong Meiling — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is narrowly selected pose/silhouette/state vocabulary only. The committed Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved V4 sheet: [`image-gen-4(4).png`](../design-sheets/image-gen-4(4).png)
- Repository path: `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-4(4).png`
- Dimensions: **1122×1402**
- File size: **2170592 bytes**
- SHA-256: `4f7741ab795936039491516e9631cd9c8d73671820e556d4be709a2ad5c9a951`

![Owner-approved V4 Hong Meiling design sheet](../design-sheets/image-gen-4(4).png)

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `meilingSleep` | 24×16 | Mansion gate arrival and credits, both drawn at 2× | Sleeping gatekeeper | Reusable active presentation sprite | Actual production requirement; preserve exact 2× gate/credit staging. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L869) |
| `meiling` | 16×16 | No live call site found | Standing definition | Inventory only — NOT a production requirement | Keep documented only; do not create boss/dialogue/portrait requirements from this unused definition. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L851) |

## 2. Current Scarlet Moon evidence

- Current unused standing definition: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L851; active sleeping definition: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L869.
- Credits draw meilingSleep at 2×: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2093; gate draws the same 24×16 sprite at 2×: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2108.
- Reconnaissance found no Meiling portrait, boss, defeat, dialogue or title call site.
- Full source-rendered reconnaissance/frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Selected official Touhou production references

1. **TH06 Embodiment of Scarlet Devil — Hong Meiling isolated boss sprite**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06HongSprite.png
   - Inspect: Inspect the isolated official boss sprite only for compact red-hair/green-costume/cap identity and silhouette economy.
   - Teaches: Small official evidence for the minimum recognizable Meiling color/silhouette vocabulary.
   - Do not copy: Do not turn the standing boss pose into a Scarlet Moon combat/dialogue requirement.
2. **TH06 Embodiment of Scarlet Devil — Meiling official artwork file**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06Meiling.png
   - Inspect: Inspect cap, red hair and Chinese-style costume identity; not as a sleeping-pose blueprint.
   - Teaches: Identity vocabulary for translating the approved sheet into the horizontal sleeping silhouette.
   - Do not copy: Do not downscale it or invent a portrait/standing production family.

These references are deliberately small and specific. They tell the later artist **which sheet/file/state to inspect**. Third-party sprite sheets remain external link/metadata only and are not copied into this repository.

## 4. Owner-approved V4 design sheet

- Long scarlet/red hair, green beret with gold star/dragon-emblem cue, and green Chinese-style tunic.
- White baggy trousers and dark/gold guards/footwear create a strong lower-body contrast.
- The approved sheet includes a simplified sleeping pose, directly useful to Scarlet Moon's actual active requirement.
- For the 24×16 sleeping asset preserve red-hair mass + green cap/body + white-trouser read; do not force standing-sheet detail into the horizontal silhouette.

The committed sheet is the exact Owner-approved design authority identified by path, dimensions and SHA-256 above. It is not an exact pose blueprint; incidental generated labels or decorative details that conflict with actual character identity or the live Scarlet Moon contract remain non-authoritative.

## 5. Translation notes

- Design the actual 24×16 sleeping silhouette first and inspect it at native 1× plus the game's exact 2× nearest-neighbor scale.
- Use the isolated TH06 sprite only for identity economy; the sleeping posture comes from Scarlet Moon's actual state contract plus the approved V4 sheet.
- Use red hair, green cap/body and white clothing as three large readable masses; gold ornament is optional micro-detail.
- The 16×16 standing definition stays inventory-only unless scope changes later.

**Translation equation:** Scarlet Moon state contract + selected official Touhou vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.

## 6. Production-brief seed

> Author only Meiling's active V4 requirement: the 24×16 sleeping sprite, proven at the game's exact 2× gate/credits scale. Inspect the exact TH06 Hong Meiling boss sprite for identity economy, but derive the sleeping posture from Scarlet Moon's actual state and the committed approved V4 sheet. The unused 16×16 standing definition remains non-requirement. No runtime changes.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
