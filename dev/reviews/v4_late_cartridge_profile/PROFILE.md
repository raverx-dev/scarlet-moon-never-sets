# Scarlet Moon V4 Late-Cartridge Profile

## 1. Machine fiction

Design Scarlet Moon V4 as if it were an unusually ambitious **late-life
Famicom/NES cartridge** made by an experienced team that understood the machine
deeply.

The game is implemented with modern web tooling. That is not a license for
modern visual grammar.

The player should be able to look at an unfiltered native frame and believe that
the image was *designed under an 8-bit cartridge discipline*, even where Scarlet
Moon deliberately waives real hardware limits to preserve its established
danmaku mechanics.

### The target is not

- a literal NES emulator certification exercise;
- a filter applied to modern illustration;
- official PC Touhou sprites redrawn at the same construction style;
- generic "pixel art";
- the intentionally earlier/austerer V3 look;
- Drillimation's exact look.

Drillimation is method evidence: define the machine first, then produce content
inside its rules. Scarlet Moon applies that discipline to a later, richer target.

---

## 2. Native-screen contract

### LC-SCREEN-1 — fixed native presentation — MUST

The authoritative visual surface is **256×240**.

Gameplay retains the existing Scarlet Moon composition:

- **192×240 gameplay field**
- **64×240 sidebar**
- total **256×240**

The current V4 runtime already uses a 256×240 canvas and disables canvas image
smoothing. This profile preserves that foundation.

### LC-SCREEN-2 — native review first — MUST

Every candidate is reviewed at **1× native pixels before enlargement**.

Nearest-neighbor 2×/3× views MAY be supplied for inspection. Enlarged views do
not override problems visible at 1×.

### LC-SCREEN-3 — no resolution laundering — MUST NOT

Do not:
- paint high-resolution art and downsample it;
- anti-alias then quantize;
- use soft resampling;
- use vector/smooth-shape construction as the final drawing method;
- hide weak native pixels behind CRT shaders, scanlines, blur, curvature or
  phosphor effects during acceptance.

Those effects may be explored later as presentation options, never as proof that
the underlying pixels work.

---

## 3. Tile and metatile construction

### LC-TILE-1 — 8×8 visual atom — MUST

Treat **8×8 pixels** as the fundamental background construction cell.

Final implementation does not need literal NES pattern-table serialization, but
important environment forms MUST be explainable as deliberate 8×8-authored
pieces rather than arbitrary large smooth rasters.

### LC-TILE-2 — 16×16 planning neighborhood — MUST

Treat **16×16** as the default environment/metatile and palette-planning
neighborhood.

Repeated architecture, ground, walls, foliage families, water, trim and other
scene vocabulary SHOULD be designed as reusable 8×8 tiles grouped into useful
16×16 metatiles or larger assemblies.

Unique landmarks MAY be larger. Their internal construction must still respect
the same cluster/tile grammar.

### LC-TILE-3 — visible vocabulary, not visible stamping — MUST

A scene needs a discoverable tile vocabulary, but it must not look like a cheap
wallpaper.

Reuse SHOULD be broken with:
- variants;
- overlap and occlusion;
- selective omission;
- asymmetric placement;
- bank/phase variants;
- landmark-specific pieces.

Do not solve "authenticity" by forcing every organic shape into obvious repeated
squares.

### LC-TILE-4 — stage-local bank thinking — SHOULD

Think in **stage/local banks** rather than one unlimited global art pool.

A scene family should identify the small vocabulary that is "resident" for that
location and the exceptional bank/phase changes used for bosses, transitions or
special presentation.

Exact CHR-ROM byte accounting is waived unless a later proof specifically needs
it. The *discipline of bounded resident vocabulary* is not waived.

---

## 4. Palette and subpalette contract

The real NES PPU exposes four background palettes and four sprite palettes; a
normal background palette assignment applies over 16×16 regions, and each
hardware sprite uses one palette. Scarlet Moon uses this as a construction
discipline rather than a cycle-accurate requirement.

### LC-PAL-1 — small live palette families — MUST

Every gameplay proof must include a **palette ledger** separating:

- background subpalettes;
- sprite/actor subpalettes;
- HUD/UI usage;
- any deliberate phase/palette swap.

Do not treat the larger NES color gamut as an unrestricted paint box.

### LC-PAL-2 — background baseline — SHOULD

Default still-frame fiction:

- one shared backdrop/background color;
- up to **four background subpalettes**;
- each subpalette contributes up to **three local colors** in addition to the
  shared backdrop;
- one 16×16 neighborhood normally selects one background subpalette.

This corresponds to a **13-color background baseline** at one time.

A candidate MAY exceed this only through an explicit Late-Cartridge trick or
waiver recorded in the ledger. "It looked better" is not sufficient by itself.

### LC-PAL-3 — sprite baseline — SHOULD

Default sprite fiction:

- up to **four sprite subpalettes**;
- each logical hardware-sprite piece uses one subpalette;
- each subpalette provides up to **three visible colors plus transparency**.

This corresponds to a **12-color sprite baseline** at one time.

A metasprite MAY combine pieces using different sprite subpalettes.

### LC-PAL-4 — color roles — MUST

Every recurring color must have a job: material, depth, light, identity,
readability, UI, threat, or effect.

Avoid:
- one-off "pretty" colors;
- many near-duplicate shades;
- local gradients with no cartridge logic;
- unrelated highlight colors scattered across a surface.

### LC-PAL-5 — deliberate swaps — MAY

Late-era richness MAY come from explicit palette changes by:
- scene;
- phase;
- boss state;
- spell/effect moment;
- transition;
- story/presentation screen.

These are deliberate state changes, not permission for unrestricted per-object
colors in one ordinary frame.

---

## 5. Sprite and metasprite contract

### LC-SPR-1 — design as 8×8/8×16 pieces — MUST

Characters and moving objects must be conceived as **metasprites assembled from
small hardware-like pieces**, even if the web runtime stores a single bitmap.

Use 8×8 or 8×16 logical pieces as the construction model.

### LC-SPR-2 — Reimu #45 decomposition — MUST

For the #45 proof, Reimu's existing **16×24** body envelope is a feature, not a
problem.

Default construction map:

- 2 columns × 3 rows of logical 8×8 cells for the body;
- separate gohei piece(s) where already required by Scarlet Moon state/runtime
  semantics;
- each logical piece selects one sprite subpalette unless an explicitly
  documented overlap trick is used.

The final runtime may still store/render a single 16×24 bitmap. The construction
map is the artistic constraint.

### LC-SPR-3 — identity hierarchy — MUST

At 1×, character identity is carried in this order:

1. silhouette / body mass;
2. signature head shape/headwear/hair;
3. high-value costume divisions;
4. signature prop;
5. pose/state change;
6. small internal detail.

If small detail is required to recognize the character, the sprite has failed
its hierarchy.

### LC-SPR-4 — state differentiation — MUST

Animation/state changes must read through meaningful silhouette, pose, prop or
value changes—not merely a few noisy pixels.

For Reimu, rear-facing/back-view remains the controlling gameplay orientation
unless the Owner explicitly changes it.

### LC-SPR-5 — bullets/effects — SHOULD

Small bullets/effects should behave like compact sprite objects:
- simple silhouette first;
- high contrast against the playfield;
- few colors;
- repeated vocabulary;
- animation/palette change preferred over extra static detail.

---

## 6. Cluster and edge language

### LC-PIX-1 — pixel-designed contours — MUST

Curves and diagonals are authored as intentional stepped clusters.

Avoid:
- smooth vector contours rasterized afterward;
- long uniform one-pixel staircases where chunkier clusters would read better;
- wiry branches, trim or ornament;
- accidental single-pixel debris.

### LC-PIX-2 — mass before texture — MUST

Large form must read before internal marks.

Examples:
- wall plane before bricks;
- trunk/crown before bark;
- water mass before ripples;
- dress/skirt mass before trim;
- boss silhouette before ornament.

### LC-PIX-3 — broad value groups — SHOULD

Prefer a few clear shadow/midtone/highlight masses to weak continuous shading.

Late-era richness means **more information per constrained pixel**, not more
pixels and not more noise.

---

## 7. Environment contract

### LC-ENV-1 — location vocabulary — MUST

Each environment family defines:
- background/backdrop role;
- 8×8 tile families;
- 16×16 metatile/assembly families;
- palette families;
- landmark pieces;
- quiet gameplay regions;
- special/boss/transition bank variants if used.

### LC-ENV-2 — quiet combat lane — MUST

The central gameplay area must preserve bullet/actor readability.

Rich edge framing, foreground elements and landmarks are encouraged. Uniform
high-frequency texture behind active danmaku is not.

### LC-ENV-3 — material-specific rendering — MUST

Different materials need different cluster logic. Do not reuse one generic
"detail noise" language for stone, wood, foliage, water, glass, metal and cloud.

### LC-ENV-4 — pre-profile art is evidence — MUST

Mansion Gate and Mansion Interior are workmanship evidence, not automatic final
style authority.

Forest, Misty Lake, Rooftop and Shrine are preserved working evidence.

Reuse or revise existing assets only after asking whether they satisfy this
profile.

---

## 8. HUD, UI and presentation

### LC-UI-1 — HUD belongs to the cartridge — MUST

The 64-pixel sidebar is not a modern overlay pasted onto retro gameplay.

Its lettering, icons, borders, counters and palette use must fit the same
tile/subpalette/cluster discipline as the playfield.

### LC-UI-2 — bitmap typography — SHOULD

Prefer compact bitmap lettering and reusable glyph/tile vocabulary. Avoid
browser/vector font rendering in final cartridge-facing surfaces.

### LC-UI-3 — selective presentation wealth — SHOULD

Title, attract, boss/spell moments, dialogue, endings and credits MAY spend more
art/animation/bank budget than ordinary gameplay.

The result must still feel like the same cartridge, not a different rendering
pipeline.

---

## 9. Animation and "cartridge wealth"

Late-era sophistication should come substantially from **time and reuse**, not
from overloading every still frame.

Prefer:
- alternate tile/sprite banks;
- short authored animation cycles;
- palette animation;
- boss phase changes;
- state-specific metasprites;
- selective background motion;
- screen/scene transitions;
- strong cinematic composition.

Avoid solving sophistication by making every surface maximally textured.

---

## 10. Explicit hardware waivers

The following are **intentionally not hard V4 acceptance requirements**:

- real CPU-cycle budgets;
- exact PPU timing;
- exact PRG/CHR ROM byte capacity;
- literal mapper register behavior;
- the physical 64-sprite OAM ceiling;
- the real **8 hardware sprites per scanline** limit;
- authentic sprite flicker/dropout;
- exact VRAM update bandwidth;
- mapper-specific raster tricks as implementation requirements.

Reason: literal enforcement would conflict with the established Scarlet Moon
danmaku game and modern runtime.

### Waiver rule

A waived hardware rule does **not** waive its useful visual lesson.

Examples:
- ignore 8-sprites-per-scanline, but keep bullets as compact sprite-like objects;
- ignore exact CHR bytes, but keep stage-local bank vocabulary;
- ignore literal pattern tables, but keep 8×8 tile construction;
- ignore exact palette-register timing, but keep small live subpalette families.

### Mapper fiction

Use a **late bank-switched cartridge, MMC3-class or equivalent, as the default
mental model for visual richness**.

This permits banked graphics and selective phase changes without granting
MMC5-style unrestricted extended attributes or modern framebuffer freedom by
default.

Audio expansion choices are a separate later decision and do not enlarge the
visual palette rules.

---

## 11. Required evidence for a Late-Cartridge art unit

Before Owner acceptance, a candidate unit must preserve enough evidence to show
that the rules were actually used.

For #45, required evidence is defined exactly in [PROOF_GATE.md](PROOF_GATE.md).

For later units, the minimum expected set is:

- native 1× output;
- nearest-neighbor enlarged review view;
- palette ledger;
- tile/metatile or metasprite construction map as applicable;
- source/reference provenance;
- explicit waiver list;
- comparison against the prior V3/current/pre-profile state where useful;
- gameplay/readability witness for gameplay surfaces.

Do not substitute a prose claim of "NES style" for this evidence.

---

## 12. Artist handoff rule

A future artist brief should be small.

Give the artist:
- exact required native states/canvases;
- approved identity/design reference;
- a few narrowly selected pose/subject references;
- a few late-era construction references;
- this profile;
- the prior native candidate if one exists.

Do not rebuild giant reference packets unless a real missing-information problem
requires one.

The artist's job is to make pixels under the cartridge rules, not to rediscover
the whole project history.
