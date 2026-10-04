# Remilia Scarlet — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is narrowly selected pose/silhouette/state vocabulary only. The committed Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved V4 sheet: [`image-gen-6(3).png`](../design-sheets/image-gen-6(3).png)
- Repository path: `dev/reviews/v4_character_reference_packets/design-sheets/image-gen-6(3).png`
- Dimensions: **1122×1402**
- File size: **2229817 bytes**
- SHA-256: `ffee33a38617885a585ea5d4eb0431d176820c4ec21363c8ba317f9009d09265`

![Owner-approved V4 Remilia Scarlet design sheet](../design-sheets/image-gen-6(3).png)

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `remilia` | 32×32 | Boss, dialogue, defeat, credits and ending exit | Idle A / base body | Reusable combat/story body | Keep one stable body scale independent of wing articulation. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L673) |
| `remiliaB` | 32×32 | Same body-family uses | Idle B | Reusable combat/story body | Correct current idle apparent-body-scale discontinuity. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L707) |
| `remiliaFinal` | 32×32 | Boss phase r5 / Red Magic | Final-phase special pose | Reusable special combat pose | Same apparent body scale; readable inside current combat bounds. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L741) |
| `p_remilia` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1148) |
| `remiliaParasol` | 32×32 | Shrine morning ending arrival | Parasol arrival | Presentation-specific independent art | Current ending arrival staging/trajectory remains authoritative. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L775) |
| `remiliaAttract` | 64×40 | Distinct attract card on black | Attract presentation art | Presentation-specific independent art | Larger independent canvas; still deliberate NES-like construction. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L809) |

## 2. Current Scarlet Moon evidence

- Current definitions: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L673, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L707, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L741, parasol https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L775, attract https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L809, portrait https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1148; final selector https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775.
- Dialogue/body reuse: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2039–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2040; attract https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2079; credits https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2095; parasol/ending exit https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2113–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2114.
- Reconnaissance flags current apparent body-size discontinuity and requires common face/scale/wing design across combat, portrait, parasol and attract.
- Full source-rendered reconnaissance/frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Selected official Touhou production references

1. **TH06 Embodiment of Scarlet Devil — Remilia isolated boss sprite**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06RemiliaSprite.png
   - Inspect: Inspect the isolated official boss sprite for compact vampire body, cap/head mass and wing-to-body proportion.
   - Teaches: Primary small-sprite reference for keeping Remilia tiny while her bat-wing silhouette stays dominant.
   - Do not copy: Do not trace pixels or inherit TH06 canvas/animation.
2. **TH06 Embodiment of Scarlet Devil — Remilia bat-form sprite**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06RemiliaBatSprite.png
   - Inspect: Inspect only for official bat-wing shape language and dark membrane economy.
   - Teaches: Helps keep Remilia's wings recognizably bat-like and distinct from Flandre's crystal-wing vocabulary.
   - Do not copy: Do not turn bat form into a new Scarlet Moon state or copy the exact bat sprite.
3. **TH06 Embodiment of Scarlet Devil — Ending & Credits sheet**
   - Exact reference: https://www.spriters-resource.com/pc_computer/touhoukoumakyoutheembodimentofscarletdevil/asset/33550/
   - Inspect: Inspect the Reimu A ending material specifically for Remilia's shrine/parasol presentation context.
   - Teaches: Official parasol/presentation vocabulary for the independent Scarlet Moon morning-arrival asset.
   - Do not copy: Do not copy ending composition, pixels or story staging; Scarlet Moon keeps its own 32×32 arrival contract.
4. **TH06 Embodiment of Scarlet Devil — Remilia official artwork file**
   - Exact reference: https://en.touhouwiki.net/wiki/File:Th06Remilia.png
   - Inspect: Inspect only for face, cap, dress and wing identity relevant to portrait/attract treatment.
   - Teaches: Larger official identity vocabulary that can inform the 32×32 portrait and 64×40 attract art.
   - Do not copy: Do not downscale it or replace the approved V4 design.

These references are deliberately small and specific. They tell the later artist **which sheet/file/state to inspect**. Third-party sprite sheets remain external link/metadata only and are not copied into this repository.

## 4. Owner-approved V4 design sheet

- Light blue hair, pink mob cap with a large red bow, pink/red layered dress and red chest-gem accent.
- Large dark bat wings are the defining outer silhouette; these are Remilia's bat wings, not Flandre's crystal wings.
- Red shoes/ribbons support lower-body color continuity.
- At 32×32 preserve cap/bow + blue head mass + bat-wing shape + pink/red body; simplify frills and gem before shrinking the body. The approved sheet does not supply a parasol pose.

The committed sheet is the exact Owner-approved design authority identified by path, dimensions and SHA-256 above. It is not an exact pose blueprint; incidental generated labels or decorative details that conflict with actual character identity or the live Scarlet Moon contract remain non-authoritative.

## 5. Translation notes

- Correct idle/final body-scale drift: body/head size stays constant while wing pose changes.
- Use the exact TH06 Remilia/bat sprite evidence to keep the outer silhouette broad, stepped and unmistakably bat-winged—not Flandre-like crystal ornament.
- Use the exact Ending & Credits sheet only for parasol presentation vocabulary; Scarlet Moon's arrival canvas/staging remains authoritative.
- Use 64×40 attract space for richer but still deliberately pixel-built treatment; do not downscale the high-resolution design sheet.
- Portrait, combat, parasol and attract must share one hair/cap/bow/face palette logic despite different compositions.

**Translation equation:** Scarlet Moon state contract + selected official Touhou vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.

## 6. Production-brief seed

> Author Remilia as one coherent family spanning idle A/B, final phase, portrait, independent 32×32 parasol arrival and independent 64×40 attract art. Keep one stable body scale and one bat-wing language. Inspect the exact TH06 Remilia boss sprite, bat sprite and ending/parasol material for official vocabulary; use the committed approved V4 sheet for appearance. No Flandre wing traits and no runtime changes.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
