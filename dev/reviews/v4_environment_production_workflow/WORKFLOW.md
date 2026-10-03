# V4 Environment Production Contract v1

This is the durable form of the contract accepted under #50 and empirically tested
under #51.

## 1. Start with a prior-work reality check

Do not begin a new environment unit from memory or in isolation.

Before mutation, identify and read:

1. the product/program authority;
2. current construction doctrine;
3. current workmanship/style evidence;
4. RoboPixel Artist Development/tutorial guidance relevant to hard subjects;
5. same-location V3 construction evidence;
6. preserved V4 scene/method evidence for that location;
7. the current environment workflow;
8. the exact bounded scene brief.

Return a short preserve/change plan:

- what prior construction should survive;
- what prior V4 composition/workmanship should survive;
- what old method has already been proven and must not be reinvented;
- what is genuinely new work;
- which difficult subjects justify tutorial lookup;
- initial component-authoring order.

This is an anti-duplication gate, not a new Owner-approval gate unless a real authority
conflict is discovered.

## 2. Declare the real scene contract

Before authoring, declare:

- native surface dimensions;
- gameplay/story/night/morning/etc. role;
- quiet/readability region for gameplay;
- location/stage identity;
- active production profile;
- palette/subpalette expectations;
- runtime integration boundary.

For ordinary Scarlet Moon gameplay environments, the working gameplay surface is
192x240. Story/presentation surfaces are 256x240 where the actual scene requires it.

Review native 1x first.

## 3. Use a multi-scale resident bank

The production model is not "tiles or big assets." It supports four scales:

8x8 repeating atoms
-> 16x16 metatiles / palette neighborhoods
-> larger reusable structures / assemblies
-> named unique landmarks
-> deterministic native layouts

Examples:

- 8x8: masonry field, grass, water base, trim, floor, mist;
- 16x16: window section, canopy corner, reeds, parapet segment;
- larger structure: pier cap/shaft/base, torii, shore tree;
- landmark: rose window, gate facade, elder tree, shrine hall.

A large landmark is allowed. Its internal pixel/cluster language must still belong to
the active construction profile; it is not permission for unrestricted illustration.

## 4. Canonical authoring boundary

Production pixels belong in RoboPixel canonical assets/revisions.

Preserve:

- project ID;
- asset ID;
- selected revision;
- revision hash;
- palette identity/hash;
- render identity/hash;
- exact native canvas;
- exact readback.

Do not directly edit canonical storage or render from uncommitted input instead of
the committed revision.

RoboPixel is the canonical asset authority. It is not required to become a generalized
scene editor.

## 5. Composition boundary

The deterministic layout is the scene.

Allowed composition operations:

- integer placement;
- repeat;
- mirror where the production path supports/preserves it;
- crop.

Do not:

- scale canonical environment pieces;
- blur or soft-filter;
- recolor after composition;
- paint vector scene forms in the compositor;
- post-repair individual pixels in the flattened scene.

Gameplay and story compositions use independent placement lists when both exist.
They may share one coherent resident bank.

Actors, bullets, HUD, dialogue, and other dynamic overlays are not baked into the
canonical background.

## 6. Late-Cartridge construction when that profile is active

#44 remains the controlling source. This workflow does not restate it as a competing
profile.

At minimum, a Late-Cartridge environment unit provides:

- deliberate 8x8 construction vocabulary;
- 16x16 planning/palette neighborhoods;
- small shared background subpalette pools;
- explicit palette/subpalette ledger;
- stage-local resident bank/vocabulary;
- stepped deliberate pixel clusters;
- material-specific treatment;
- quiet gameplay/readability space;
- explicit waivers rather than silent constraint expansion.

If a different future production profile is activated, its own accepted construction
rules replace these profile-specific points while the surrounding workflow remains
the same.

## 7. Artist Development / tutorial input

For difficult subjects, do not improvise blindly.

Use:

identify concrete visual problem
-> consult qualified tutorial/reference
-> distill transferable technique
-> apply under project workmanship + active construction profile
-> inspect at native scale
-> revise canonical component

Tutorial/reference material is technique evidence, not an asset source.

Do not copy third-party pixels or bulk prose.

Examples of hard subjects:

- trees / foliage / roots;
- water / mist / reflections;
- masonry / stone;
- columns / architecture;
- glass / stained glass;
- fabric;
- terrain / shoreline;
- clouds / weather.

## 8. Iterate by component family, not by whole-scene repaint

Preferred art loop:

small coherent component family
-> compose native scene
-> inspect at 1x
-> compare to project evidence
-> identify exact weak component OR layout relationship
-> revise only that thing
-> recompose

Do not assume a weak scene requires more assets.

The #51 proof demonstrated that a mechanically strong bank can still produce a bad
layout. Its successful correction preserved almost the entire bank and changed scene
hierarchy instead.

## 9. Separate mechanical and artistic gates

### Hard mechanical evidence

Required where applicable:

- native dimensions;
- canonical revision/readback match;
- deterministic layout;
- palette/subpalette ledger;
- 8x8 tile evidence;
- 16x16 metatile/construction evidence;
- stage-local bank inventory;
- exact reconstruction;
- Production Handoff verification.

### Soft diagnostics

Report, but do not silently turn into art law:

- orphan pixels;
- unused colors;
- near-duplicate assets;
- suspiciously regular stamping;
- tile/metatile reuse counts;
- unique-color counts;
- dimensional alignment;
- V3 / prior-V4 comparisons.

### Owner artistic authority

The Owner decides:

- whether the scene reads as the intended location;
- whether repetition feels useful or cheap;
- whether materials/depth/detail are strong enough;
- whether a landmark is recognizable;
- whether a quiet region is appropriately quiet or simply empty;
- whether a mechanically valid candidate should be ACCEPTED, CORRECTED, or REJECTED.

Mechanical PASS is never artistic acceptance.

## 10. Correction protocol

When a scene is rejected or held:

1. preserve the canonical bank by default;
2. identify whether the failure is asset-local, layout-local, or both;
3. revise the smallest necessary component set;
4. recompose before adding more art;
5. keep rejected/earlier revisions durable;
6. regenerate the review package;
7. compare at native 1x again.

Do not restart merely because the first composition failed.

#51 is the reference example: 40 selected bank assets stayed unchanged, the rose
landmark alone was revised, and the primary correction was spatial recomposition.

## 11. Production Handoff and review package

Use RoboPixel Production Handoff v1 for the durable proof boundary.

A normal environment review package should include:

- native candidate first;
- nearest-neighbor enlargement;
- asset atlas;
- 8x8 tile atlas/manifest;
- 16x16 metatile/construction map;
- palette/subpalette ledger;
- resident-bank inventory;
- exact canonical pins;
- deterministic layout/checkpoint;
- quiet-lane/readability witness where relevant;
- verification/provenance;
- comparison evidence against the appropriate historical/current sources.

No model-mediated Base64 transport.

## 12. Runtime integration boundary

Static art production and runtime integration are separate work units.

Do not modify runtime merely to prove an environment bank or scene composition.
After Owner art acceptance, a later mechanical integration unit may reuse the exact
accepted matrices/revisions/layout semantics without redrawing them.

## 13. Per-scene stop condition

A bounded environment unit stops when:

- one declared scene/variant scope is complete;
- canonical bank and selected revisions are pinned;
- native composition is reviewable;
- required mechanical evidence passes;
- Owner has an explicit ACCEPT / CORRECT / REJECT disposition;
- accepted proof/art state is durably referenced.

Optional polish does not have to block proof acceptance unless it violates the scene's
actual acceptance goal.
