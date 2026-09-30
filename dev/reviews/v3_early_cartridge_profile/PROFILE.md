# Scarlet Moon V3 Early-Cartridge Profile

## 1. Status and authority

This document is the controlling visual-construction doctrine for any future
separately authorized refinement of the **Scarlet Moon V3 Early-Cartridge line**.

Governing issue:

- #47 — V3 Early-Cartridge Profile — controlling visual construction authority

Related authority:

- RoboPixel Machine Profile Stack — merged through RoboPixel PR #33 at
  `3bc307b1e8e082eee747fa83fd0cc55f32003836`
- #44 — V4 Late-Cartridge Profile — sibling doctrine for the later production-era
  interpretation

This document is **doctrine only**.

It does not authorize:

- V3 art production;
- runtime changes;
- mutation of the frozen public V3 snapshot;
- a V3 proof gate;
- merge/publication of a revised V3 edition;
- changes to the active V4 #45 proof.

A separate Owner decision is required before any Early-Cartridge production unit
is activated.

---

## 2. Historical V3 is preserved

The accepted historical V3 checkpoint remains immutable:

- source/checkpoint:
  `ea4c31aa8d2ad92e1a5d8bfb0f25d1ba0863ed31`
- archive:
  `archive/version-3`
- public snapshot:
  `versions/sprite-redesign/`

### EC-HIST-1 — frozen checkpoint is immutable — MUST

No future Early-Cartridge work may silently rewrite, replace or mutate the
historical V3 checkpoint.

### EC-HIST-2 — frozen does not mean dead aesthetic line — MUST

"Frozen V3" means the historical snapshot is preserved.

It does **not** mean the V3 Early-Cartridge aesthetic line is permanently closed.

A future refinement may branch from the preserved checkpoint under separate
versioning and explicit Owner authority.

### EC-HIST-3 — future version naming remains open — MUST

This profile does not decide whether a future refinement is called V3.1, Revised
V3, Early-Cartridge Edition, or something else.

Naming and publication semantics remain a later Owner decision.

---

## 3. Machine Profile Stack resolution

Scarlet Moon V3 Early-Cartridge conceptually resolves as:

```text
family:
  8-bit-home-console

machine:
  nintendo.nes-famicom

production-era:
  early-cartridge

genre:
  vertical-danmaku

project:
  scarlet-moon

authenticity:
  credible-machine-fiction
```

### EC-STACK-1 — this is a consumer profile — MUST

This document is a Scarlet Moon project profile.

It is not the generic NES/Famicom machine schema.

Reusable machine-level facts may later be extracted into RoboPixel, but that
future extraction must not retroactively change this profile's accepted meaning.

### EC-STACK-2 — Early-Cartridge is a production-era overlay — MUST

Early-Cartridge describes how Scarlet Moon is pretending to use the NES/Famicom
production substrate.

It is not a different machine from V4.

### EC-STACK-3 — Early is a positive target — MUST

Early-Cartridge must never be treated as:

- unfinished Late-Cartridge;
- intentionally bad pixel art;
- "less detail equals authentic";
- a generic low-effort 8-bit filter.

The target is deliberate economy, strong shape language, direct readability and
disciplined reuse.

---

## 4. Core thesis

Design any future V3 refinement as if Scarlet Moon were a convincing
**earlier-generation Famicom/NES cartridge production**.

The result should feel:

- compact;
- economical;
- strongly silhouette-driven;
- deliberate about tile reuse;
- restrained in ornament;
- clear in palette roles;
- selective in animation;
- direct at native size;
- mechanically credible as an earlier or more conservative cartridge production.

The player should be able to look at an unfiltered native frame and believe that
the art was designed under an early-era 8-bit cartridge discipline.

The target is not:

- literal emulator certification;
- generic "retro";
- high-resolution art reduced to pixels;
- Late-Cartridge art with details deleted;
- official PC Touhou rendering miniaturized into sprites;
- procedural/vector-like shapes with a pixel filter;
- intentionally crude or careless art.

---

## 5. Relationship to V4 Late-Cartridge

Early-Cartridge and Late-Cartridge are siblings.

They share:

- the NES/Famicom machine family;
- Scarlet Moon's project identity;
- vertical-danmaku readability requirements;
- native pixel authorship;
- palette economy;
- tile/metasprite thinking;
- explicit hardware waivers;
- deterministic RoboPixel production/evidence when future work is authorized.

They differ in production-era grammar.

| Dimension | Early-Cartridge | Late-Cartridge |
| --- | --- | --- |
| Primary strength | economy and directness | selective technical/artistic wealth |
| Tile vocabulary | smaller, more reusable | more specialized variants/banks |
| Material rendering | few strong cues | richer material-specific treatment |
| Animation | fewer meaningful states | more deliberate state/phase variety |
| Sprite construction | compact, restrained | richer metasprite/state vocabulary |
| Presentation tricks | selective, conservative | more frequent bank/palette/phase sophistication |
| Ornament | restrained | selective richer ornament |
| Cinematic ambition | compact/direct | greater selective staging wealth |
| Resource fiction | bounded conservative vocabulary | ambitious late-life banked vocabulary |
| Failure mode to avoid | looking cheap/unfinished | looking modern/noisy/unconstrained |

### EC-SIBLING-1 — neither profile ranks above the other — MUST

Late-Cartridge is not the "better" edition by definition.

Early-Cartridge and Late-Cartridge are different visual-production languages.

Future Owner acceptance is based on whether each edition succeeds at its intended
language.

---

## 6. Native-screen contract

Scarlet Moon remains the same game and retains its established presentation.

### EC-SCREEN-1 — native presentation is authoritative — MUST

The authoritative full gameplay surface remains **256×240**.

Gameplay retains:

- **192×240 gameplay field**
- **64×240 sidebar**
- total **256×240**

### EC-SCREEN-2 — review at 1× first — MUST

Every future Early-Cartridge candidate must be judged at native 1× before enlarged
inspection.

Nearest-neighbor enlarged views may support review but cannot rescue weak native
pixels.

### EC-SCREEN-3 — no resolution laundering — MUST NOT

Do not:

- paint high-resolution art and downsample it;
- use anti-aliasing then quantize;
- use soft resampling;
- use vector/smooth-shape construction as final authored form;
- depend on CRT/scanline/blur/curvature effects for acceptance.

The underlying native pixels must succeed unaided.

---

## 7. Tile and metatile construction

### EC-TILE-1 — 8×8 visual atom — MUST

Treat 8×8 as the fundamental background construction cell.

Important forms should be explainable through intentional tile-authored pieces
rather than arbitrary large smooth rasters.

### EC-TILE-2 — 16×16 planning neighborhood — MUST

Treat 16×16 as the default local environment and palette-planning neighborhood
where the NES/Famicom visual lesson applies.

Repeated forms should normally emerge from small 8×8 vocabularies assembled into
useful 16×16 or larger structures.

### EC-TILE-3 — smaller resident vocabulary — SHOULD

An Early-Cartridge environment should prefer a smaller scene-local vocabulary than
its Late-Cartridge sibling.

This does not require literal minimum tile count.

The visual lesson is:

- reuse first;
- specialized tile variants only when they materially improve readability or
  location identity;
- landmarks created through arrangement and a few intentional exceptions rather
  than unrestricted unique raster pieces.

### EC-TILE-4 — visible reuse may be stylistic — MAY

Early-Cartridge may allow tile reuse to remain somewhat more visible than
Late-Cartridge.

Visible reuse is acceptable when it reads as deliberate cartridge construction.

It fails when it reads as accidental wallpaper, obvious procedural stamping or
uncontrolled repetition.

### EC-TILE-5 — asymmetry is still allowed — SHOULD

Economy does not require sterile symmetry.

Use:

- selective omission;
- mirrored reuse where useful;
- offset repetition;
- limited variants;
- foreground overlap;
- landmark placement;
- compositional asymmetry.

The goal is efficient authored structure, not mechanical tiling for its own sake.

---

## 8. Palette and color contract

Early-Cartridge uses the same NES/Famicom palette-economy lesson as V4, but with
more conservative production expectations.

### EC-PAL-1 — small live palette families — MUST

Gameplay-facing work must be conceived with small reusable background and sprite
subpalette families.

Do not use the machine's full gamut as an unrestricted paint box.

### EC-PAL-2 — global palette economy — MUST

HUD, playfield, actors, bullets and effects must be designed as one cartridge
presentation rather than independent modern layers with private color budgets.

Where a future proof uses the same ordinary-frame fiction as #44, the working
baseline remains:

- up to four background subpalettes;
- up to four sprite subpalettes;
- shared backdrop/background behavior as appropriate;
- no automatic private HUD palette family;
- no private actor/effect palette pools.

Any deviation must be explicit.

### EC-PAL-3 — fewer shade steps by default — SHOULD

Early-Cartridge should prefer:

- clear dark/mid/light roles;
- strong local contrast;
- limited material ramps;
- reuse of established colors across related surfaces.

Avoid multiplying near-duplicate shades merely to simulate richer rendering.

### EC-PAL-4 — color roles are explicit — MUST

Recurring colors should have stable jobs such as:

- background depth;
- material identity;
- player identity;
- enemy identity;
- projectile threat/readability;
- UI information;
- highlight/accent.

### EC-PAL-5 — palette tricks are selective — MAY

Palette animation, swaps or scene-state changes may exist.

They should be comparatively selective and explicit.

An Early-Cartridge frame should not require elaborate palette trickery to look
successful.

---

## 9. Sprite and metasprite contract

### EC-SPR-1 — compact native envelopes are a feature — MUST

Do not enlarge sprites merely because a modern runtime allows it.

Compact gameplay envelopes are part of the design challenge.

### EC-SPR-2 — design as logical hardware-like pieces — MUST

Characters and moving objects should be conceived as metasprites assembled from
small sprite-like pieces even if the runtime stores a single bitmap.

8×8 or 8×16 logical pieces remain the default mental model.

### EC-SPR-3 — identity hierarchy — MUST

At native size, identity should read through:

1. silhouette/body mass;
2. head/hair/headwear;
3. major costume division;
4. signature prop;
5. state/pose;
6. small internal detail.

If recognition depends on micro-detail, the sprite hierarchy is too weak.

### EC-SPR-4 — restrained piece count — SHOULD

Prefer fewer well-used logical pieces rather than adding pieces simply because
Late-Cartridge would permit richer metasprite construction.

Extra pieces should materially improve:

- silhouette;
- prop readability;
- movement state;
- character identity.

### EC-SPR-5 — meaningful states over many states — MUST

A smaller number of states is acceptable.

Each state should communicate through:

- silhouette;
- posture;
- prop angle;
- value grouping;
- directional lean;
- body mass.

Do not substitute one- or two-pixel noise for actual state differentiation.

### EC-SPR-6 — official Touhou sprites are not construction authority — MUST

Official/source Touhou material may inform:

- identity;
- pose;
- orientation;
- costume;
- state vocabulary.

It does not automatically define the Early-Cartridge pixel-construction target.

---

## 10. Cluster and edge language

### EC-PIX-1 — pixel-designed contours — MUST

Curves and diagonals use deliberate stepped clusters.

Avoid:

- rasterized vector contours;
- long weak one-pixel staircases;
- accidental single-pixel debris;
- thin ornamental lines that do not survive native review.

### EC-PIX-2 — mass before texture — MUST

Large form must read before texture.

Examples:

- wall plane before masonry marks;
- tree trunk/crown before bark;
- roof mass before trim;
- dress/skirt mass before costume decoration.

### EC-PIX-3 — fewer stronger clusters — SHOULD

Compared with Late-Cartridge, Early-Cartridge should normally use fewer internal
clusters with more semantic weight.

A highlight or shadow cluster should explain form, material or identity.

Do not fill empty space merely because more detail is possible.

---

## 11. Environment contract

### EC-ENV-1 — authored place, compact vocabulary — MUST

Every environment must still read as a specific place.

The scene should identify:

- backdrop/depth role;
- compact tile vocabulary;
- major structural assemblies;
- palette family;
- landmarks;
- quiet gameplay regions.

### EC-ENV-2 — restrained material vocabulary — SHOULD

Materials should have recognizable but economical cluster languages.

A material may be conveyed through one or two strong cues rather than the richer
multi-band treatment expected from Late-Cartridge.

### EC-ENV-3 — gameplay quiet regions are deliberate — MUST

Central combat/readability regions must remain controlled.

Sparse areas are not automatically unfinished.

In an Early-Cartridge scene, controlled negative space may be part of the intended
visual economy.

### EC-ENV-4 — repetition must be intentional — MUST

Early-era repetition may be more visible.

It must still feel composed.

Reject:

- unbroken wallpaper fields;
- obvious procedural grids with no compositional hierarchy;
- repetition that competes with bullets;
- material noise that destroys location identity.

### EC-ENV-5 — landmarks are selective — SHOULD

Spend unique visual vocabulary on:

- location-defining structures;
- boss/transition cues;
- important foreground framing;
- story-significant props.

Do not spend uniqueness uniformly across the entire screen.

---

## 12. UI and presentation contract

### EC-UI-1 — HUD belongs to the same cartridge — MUST

The 64-pixel sidebar must share Early-Cartridge construction logic with the
playfield.

It is not a modern overlay pasted beside retro gameplay.

### EC-UI-2 — compact bitmap vocabulary — SHOULD

Prefer:

- compact glyphs;
- tile-like icons;
- economical borders;
- simple repeated framing;
- direct hierarchy.

Avoid ornamental UI density that would better belong to Late-Cartridge.

### EC-UI-3 — presentation may exceed gameplay, selectively — MAY

Title, attract, dialogue, ending and credits may spend more visual budget than an
ordinary gameplay frame.

They should still feel like the same earlier-generation production.

---

## 13. Animation and production economy

### EC-ANIM-1 — animation is selective — MUST

Do not assume that every object needs many frames.

Use animation where it communicates:

- movement;
- attack;
- state;
- identity;
- gameplay timing;
- scene transition.

### EC-ANIM-2 — state clarity beats smoothness — MUST

A two- or three-state cycle with clear silhouettes may be preferable to a larger
cycle with weak differences.

### EC-ANIM-3 — time should not hide weak stills — MUST

Ordinary native frames should already read correctly.

Animation cannot compensate for unclear silhouette, weak palette hierarchy or
procedural-looking environment construction.

---

## 14. Cartridge economy

Late-Cartridge uses selective wealth.

Early-Cartridge uses **selective economy**.

### EC-ECO-1 — reuse is a design resource — MUST

Tile, palette, sprite and icon reuse should be intentionally visible in the
production logic.

The artist should ask:

- can this form be built from existing vocabulary?
- can one tile serve multiple structural roles?
- can color reuse reinforce identity?
- can one strong animation state replace several weak ones?

### EC-ECO-2 — exceptions must earn their cost — SHOULD

Unique tiles, sprite pieces, palette states and presentation tricks should be used
when they produce clear value:

- readability;
- identity;
- landmark recognition;
- boss emphasis;
- story emphasis.

### EC-ECO-3 — restraint must not become blandness — MUST

The profile fails if economy removes the qualities that make Scarlet Moon locations
and characters recognizable.

Economy should concentrate identity, not erase it.

---

## 15. Danmaku readability layer

This is a genre/project layer, not an NES machine rule.

### EC-GAME-1 — gameplay is preserved — MUST

No Early-Cartridge art decision authorizes changes to:

- movement;
- focus;
- collision;
- hitbox behavior;
- scoring;
- stage timing;
- enemy waves;
- bullet geometry;
- boss phase order;
- difficulty;
- story flow.

### EC-GAME-2 — bullets outrank decoration — MUST

Projectiles and actors must remain legible at native size.

Background complexity must yield where necessary.

### EC-GAME-3 — player identity must survive activity — MUST

Reimu must remain readable during representative bullet activity.

### EC-GAME-4 — compact projectile vocabulary — SHOULD

Bullets/effects should use:

- simple silhouettes;
- high contrast;
- few colors;
- repeated recognizable shapes;
- animation/palette change rather than excessive static detail.

---

## 16. Scarlet Moon identity layer

### EC-PROJ-1 — same game, early cartridge generation — MUST

This profile does not create a different story, cast, setting or gameplay concept.

It is another visual production generation of Scarlet Moon.

### EC-PROJ-2 — V3 is primary evidence — MUST

The frozen V3 checkpoint is the primary evidence corpus for:

- successful Early-Cartridge traits;
- residual style inconsistencies;
- procedural/vector-like leftovers;
- character/environment relationships;
- UI and presentation behavior.

### EC-PROJ-3 — preserve successful V3 traits — MUST

Do not redraw an asset merely because a future refinement exists.

A future correction must identify a concrete reason the frozen V3 asset conflicts
with the accepted Early-Cartridge doctrine or another separately authorized need.

### EC-PROJ-4 — distinguish art defects from runtime defects — MUST

Clipping, anchor errors, scaling bugs and other runtime/integration defects should
not be misclassified as style failures.

---

## 17. Explicit hardware waivers

The target is credible machine fiction, not cycle-accurate NES execution.

The following are not automatically hard requirements:

- CPU-cycle budgets;
- exact PPU timing;
- exact PRG/CHR byte accounting;
- literal mapper behavior;
- physical OAM sprite ceiling;
- real sprites-per-scanline behavior;
- authentic flicker/dropout;
- exact VRAM update bandwidth.

### EC-WAIVER-1 — waived hardware does not waive visual lesson — MUST

Examples:

- ignore literal scanline sprite limits, but keep bullets compact and sprite-like;
- ignore exact ROM bytes, but keep a bounded scene vocabulary;
- ignore literal pattern tables, but keep tile-authored construction;
- ignore exact palette timing, but keep small live palette families.

### EC-WAIVER-2 — Early-Cartridge uses conservative exceptions — SHOULD

Compared with Late-Cartridge, do not default to elaborate bank/raster/palette
exception logic.

Use special tricks only when the scene or state materially benefits.

---

## 18. Required evidence for any future Early-Cartridge production unit

This section defines doctrine for future units only.

It does not activate one now.

A future candidate should normally preserve:

- native 1× output;
- nearest-neighbor enlarged inspection view;
- palette ledger;
- tile/metatile or metasprite construction map as applicable;
- comparison to the frozen V3 source;
- explicit list of retained successful V3 traits;
- explicit list of corrected doctrine violations;
- reference/source provenance;
- hardware waiver list;
- gameplay readability witness for gameplay surfaces;
- canonical RoboPixel asset IDs, revisions and hashes;
- deterministic composition/export provenance where applicable.

### EC-EVID-1 — reproducibility is required — MUST

A visually successful one-off raster is not enough.

Future production must remain traceable through durable RoboPixel state and the
Production Handoff discipline:

```text
artist
→ compact durable checkpoint
→ mechanical packager/publisher
→ compact review package
```

Do not use model-mediated binary blob publication as the normal production path.

### EC-EVID-2 — before/after must preserve history — MUST

The frozen V3 frame is evidence.

A future refinement should compare against it rather than replacing it invisibly.

---

## 19. Reference hierarchy for future Early-Cartridge work

A future brief should use a small evidence set.

Suggested order:

1. frozen Scarlet Moon V3 source/runtime — exact states, canvases, anchors and
   historical target;
2. this Early-Cartridge Profile — construction authority;
3. approved Scarlet Moon character/location identity evidence;
4. selected early-era NES/Famicom construction examples;
5. Drillimation NES demake work — production-method evidence, not mandatory visual
   imitation;
6. official Touhou material — identity/pose/state evidence where useful.

More references are not automatically better.

Do not rebuild giant reference packets without a concrete information gap.

---

## 20. What Early-Cartridge is not

Do not interpret this profile as permission to produce:

- deliberately primitive art;
- arbitrary low-color art;
- generic "NES filter" output;
- high-resolution art reduced to pixel size;
- vector/Flash-looking geometry;
- excessive procedural stamping;
- uniform checkerboard/detail noise;
- Late-Cartridge art with half the detail erased;
- official PC Touhou sprites redrawn literally at small size;
- changes to gameplay or story;
- edits to the preserved V3 public snapshot.

---

## 21. Future V3-line activation boundary

This profile alone does not authorize production.

A future activation should explicitly define:

- exact V3-line versioning/publication plan;
- one bounded proof surface;
- one or a few representative characters/states;
- environment/HUD scope;
- canonical RoboPixel authoring requirements;
- comparison evidence;
- stop point for Owner review.

The first proof should be small enough to answer one question:

> Does this Early-Cartridge doctrine produce a stronger, more intentional version
> of the V3 aesthetic without collapsing into either crude retro art or V4
> Late-Cartridge?

Only after Owner acceptance should broader V3-line production be considered.

---

## 22. Relationship to future generic profile extraction

Once both Scarlet Moon doctrines are stable:

- #47 / this profile — Early-Cartridge consumer doctrine;
- #44 — Late-Cartridge consumer doctrine;

the shared machine-level rules can be compared and extracted more confidently into
a generic NES/Famicom base profile in RoboPixel.

The intended conceptual shape is:

```text
NES/Famicom Base Machine Profile
        ├── Early-Cartridge production-era overlay
        └── Late-Cartridge production-era overlay

Scarlet Moon
        + vertical-danmaku profile
        + project art direction
        + explicit waivers
```

Do not perform that extraction by silently weakening either accepted Scarlet Moon
profile.

Use both as evidence.

---

## 23. Exit condition

This doctrine is successful when a future artist/Coordinator can answer, without
chat memory:

- what Early-Cartridge Scarlet Moon means positively;
- how it differs from Late-Cartridge;
- which NES/Famicom construction lessons remain active;
- how economy becomes intentional craft rather than lower quality;
- how tile, palette, sprite, environment, UI and animation choices should differ;
- how danmaku readability constrains the art;
- what modern shortcuts remain forbidden;
- what hardware limits are intentionally waived;
- which V3 historical state is immutable;
- how a future refinement can preserve history and remain reproducible.

---

## 24. Stop

After this profile is accepted:

- do not start V3 art production;
- do not create a V3 proof gate without Owner authorization;
- do not modify the historical V3 snapshot;
- do not alter active V4 #45;
- do not merge a revised V3 runtime;
- do not publish a revised V3 edition.

The next V3-line step, if any, is an explicit Owner decision.
