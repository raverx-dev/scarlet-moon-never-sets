# Remilia Scarlet — V4 character reference packet

**Status:** COMPLETE / OWNER-MANAGER REVIEW READY  
**Governing issue:** #42 · parent #28 · master #24  
**Source baseline:** `d2586870b92551e931f784631ddfc891208df35b`

## Authority and provenance

Scarlet Moon current source + the merged reconnaissance define what must exist, how it is used, and all runtime/staging constraints. Official Touhou material below is pose/silhouette/prop vocabulary only. The Owner-approved V4 sheet is appearance authority. Final art is a new late-Famicom/NES-style reinterpretation, not a literal official-sprite copy or a downscaled illustration.

- Reconnaissance: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html
- Current source: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html
- Approved sheet supplied to the coordinator: **image-gen-6(3).png**, 1122×1402, SHA-256 `ffee33a38617885a585ea5d4eb0431d176820c4ec21363c8ba317f9009d09265`
- Sheet binary is intentionally **not copied into this repository**. The filename + hash identify the exact Owner-approved input that must be supplied to the later artist.

## 1. Complete coverage matrix

| State / asset | Native canvas | Actual scene/use | Meaning | Reuse class | Runtime / staging notes | Evidence |
|---|---:|---|---|---|---|---|
| `remilia` | 32×32 | Boss, dialogue, defeat, credits and ending exit | Idle A / base body | Reusable combat/story body | Current family is also reused outside combat; keep body scale independent of wing articulation. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L673) |
| `remiliaB` | 32×32 | Same body-family uses | Idle B | Reusable combat/story body | Recon flags current idle body-scale discontinuity; V4 should correct it. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L707) |
| `remiliaFinal` | 32×32 | Boss phase r5 / Red Magic | Final-phase special pose | Reusable special combat pose | Must remain same apparent body scale and readable inside boss combat bounds. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L741) |
| `p_remilia` | 32×32 | Dialogue portrait bezel | Portrait | Presentation-specific UI art | Clipped to the 32×32 portrait interior. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1148) |
| `remiliaParasol` | 32×32 | Shrine morning ending arrival | Parasol arrival | Presentation-specific independent art | Enters from the right toward x=126 at y=160. Parasol/body/wings must fit this independent 32×32 presentation. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L775) |
| `remiliaAttract` | 64×40 | Distinct attract card on black | Attract presentation art | Presentation-specific independent art | Rendered at (128,88) in the attract sequence; larger canvas permits more identity but still needs NES-like cluster discipline. | [source](https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L809) |

## 2. Current Scarlet Moon evidence

- Current definitions are at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L673, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L707, https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L741, parasol https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L775, attract https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L809, portrait https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1148; final selector at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L1775.
- Dialogue/body reuse is at https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2039–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2040; attract art https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2079; credits body https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2095; parasol/ending exit https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2113–https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/versions/v4/index.html#L2114.
- Reconnaissance explicitly flags Remilia's current apparent body-size discontinuity between idle frames and requires common face/scale/wing design across combat, portrait, parasol and attract.
- Reconnaissance source-rendered evidence and full frame inventory: https://github.com/raverx-dev/scarlet-moon-never-sets/blob/d2586870b92551e931f784631ddfc891208df35b/dev/reviews/v4_character_art_reconnaissance/Scarlet-Moon-Character-Review-2026-09-24.html

## 3. Curated official Touhou reference set

1. **Embodiment of Scarlet Devil / Imperishable Night Remilia — character page** — Official boss/playable silhouette, bat wings and parasol context.
   - Source: https://en.touhouwiki.net/wiki/Remilia_Scarlet
   - Teaches: Small vampire body against large black bat wings; official page also records the shrine parasol appearance and IN back sprite.
   - Do not copy: Do not copy EoSD/IN pixels, fighting-game proportions, or infer a new runtime pose from official material.
2. **Embodiment of Scarlet Devil official image archive** — Remilia boss/bat sprite and official artwork cross-check.
   - Source: https://en.touhouwiki.net/wiki/Category:Embodiment_of_Scarlet_Devil_Images
   - Teaches: Wing span, compact body and early-Windows portrait vocabulary; useful to distinguish Remilia from Flandre.
   - Do not copy: Do not literal-copy the boss/bat frames or replace Scarlet Moon's distinct parasol/attract compositions.

These are reference links/metadata only. No third-party sprite sheet is copied into the repository.

## 4. Owner-approved V4 design sheet

- Light blue hair, pink mob cap with a large red bow, pink/red layered dress and red chest-gem accent.
- Large dark bat wings are the defining outer silhouette; these are Remilia's bat wings, not Flandre's crystal wings.
- Red shoes/ribbons support lower-body color continuity.
- At 32×32 preserve cap/bow + blue head mass + bat-wing shape + pink/red body; simplify frills and gem before shrinking the body. The approved sheet does not supply a parasol pose.

The sheet is a design authority, not an exact pose blueprint. Generated labels or ornamental details that conflict with actual character identity or the live Scarlet Moon contract are non-authoritative.

## 5. Translation notes

- Correct the current idle/final scale drift: body/head size stays constant while wing pose changes.
- Bat wings are the outer silhouette. Use broad stepped membranes and a few structural pixels; do not substitute Flandre-style crystal ornaments.
- Parasol is independent 32×32 presentation art. Since the approved sheet lacks a parasol pose, combine current ending staging with official parasol vocabulary rather than inventing a generic prop pose.
- Use the 64×40 attract canvas for a richer but still deliberately pixel-built Remilia; do not downscale the high-resolution design sheet.
- Portrait, combat, parasol and attract should share the same hair/cap/bow/face palette logic even though their compositions differ.

The translation equation for the later artist is:

**Scarlet Moon state contract + official Touhou visual vocabulary + exact approved V4 design sheet + deliberate late-Famicom/NES construction.**

## 6. Production-brief seed

> Author Remilia as one coherent family spanning idle A/B, final phase, portrait, independent 32×32 parasol arrival and independent 64×40 attract art. Keep one stable body scale and one bat-wing language. Use official EoSD/IN references for vampire/wing/parasol vocabulary and the approved sheet for V4 appearance. Translate each canvas separately into late-Famicom/NES construction; do not downscale illustration or borrow Flandre wing traits.

**Do not execute that art from this packet-preparation branch.** Canonical RoboPixel authoring and runtime integration remain separately authorized work.
