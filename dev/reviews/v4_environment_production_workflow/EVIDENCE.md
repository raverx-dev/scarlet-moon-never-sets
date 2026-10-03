# Empirical evidence for Environment Production Workflow v1

## 1. Why this record exists

The environment workflow was not designed from one isolated experiment.

It reconciles three generations of Scarlet Moon environment work:

1. V3 tile-heavy construction;
2. pre-profile V4 assembled canonical assets;
3. Late-Cartridge constrained V4 assembled assets.

The purpose of this file is to record what those tests actually demonstrate and what
they do not.

## 2. V3 — tile-heavy/economical construction evidence

Representative Mansion evidence:

- archive commit: ea4c31aa8d2ad92e1a5d8bfb0f25d1ba0863ed31
- path: dev/art/v3_stage3a_mansion/README.md

The V3 Mansion package contains:

- 35 explicit environment assets;
- extensive 8x8 wall/carpet/floor/trim vocabulary;
- 16x16 architecture/furnishing vocabulary;
- one larger 32x24 chandelier;
- deterministic tile_rect / place composition;
- no palette extension;
- explicit quiet gameplay lane x=64..127.

Strengths demonstrated:

- strong construction economy;
- obvious game-art vocabulary;
- disciplined reuse;
- coherent native readability;
- quiet gameplay region.

Limitation for V4:

- small repeated vocabularies can become wallpaper-like or underpowered for richer
  architecture, organic asymmetry, landmarks, depth, and intentionally different
  gameplay/story compositions.

V3 remains evidence, not the V4 quality ceiling.

## 3. Pre-profile V4 — richer assembled canonical assets

Representative Mansion evidence:

- architectural-kit proof: 13ff42307d5f008b8fa8ebce80f546b164067a1b
- accepted working Mansion #22:
  c2241001946ac5456293f9f2b8be137e5c5bc648

The architectural-kit proof established:

- canonical RoboPixel asset creation/revision/readback;
- external deterministic compositor;
- placement/crop/repeat/mirror without repainting;
- no demonstrated need for a generalized scene editor;
- separate gameplay/story placements.

Its evaluation also recorded limitations:

- approximate depth;
- visible symmetry/repetition;
- underdeveloped landmark treatment;
- need for authored near/far variants instead of scaling.

#22 demonstrated richer workmanship and spatial hierarchy. Its floor rollback also
proved an important rule: more detail is not automatically better.

This regime demonstrates that RoboPixel is not restricted to a single tile-heavy
visual style. It can support richer individually authored components assembled into
a scene.

## 4. Late-Cartridge V4 — #51 empirical proof

Final accepted proof state:

- issue: #51
- correction branch: v4-mi51-correction-01
- head: 441f07afaee0fda11271e10e9008d279f3cf5396
- proof directory: dev/proofs/v4_mansion_resident_bank_51/
- corrected candidate render hash:
  9f766329c5d3e1dbd7e334bced46e06ad04293aba99626b0d24c367e9ebdc700

The full resident bank contains 41 environment assets plus five unchanged #45 witness
assets.

Final proof evidence:

- 46/46 canonical pins PASS;
- 41/41 selected environment validations PASS;
- four background subpalettes;
- 13 available/visible background colors in the bank/profile ledger;
- 180/180 final 16x16 neighborhoods conform;
- exact metatile reconstruction;
- quiet lane x=64..127, y=128..239;
- two independent package runs byte-identical;
- no unresolved mechanical blocker.

### Initial candidate lesson

The first package at:

- branch: v4-mi51-review-package-v1
- head: a9ae66e0dcf71de4b8381fd3f1abbc0c064e75b5

was mechanically valid but artistically rejected.

The resident bank was largely usable, but:

- the scene read as two stacked interiors;
- near/far hierarchy was confused;
- the rose landmark was not clearly recognizable;
- carpet/floor transitions read as dark holes/bands.

This is direct evidence that mechanical construction evidence cannot replace native
artistic review.

### Correction lesson

Correction 01 preserved the bank.

- 40 selected assets stayed unchanged;
- only v4-mi51-rose changed, r4 -> r7;
- rose orphan warnings fell from 20 to 0;
- lower ruby-window placements were removed rather than deleting the assets;
- rear/foreground hierarchy was recomposed;
- the door/stair/runner axis was restored;
- the rose was seated inside architecture;
- continuous foreground framing replaced the second-chapel effect.

The major improvement therefore came from composition and hierarchy, not from
throwing away the resident bank.

Owner disposition:

> ACCEPT as a successful Environment Production Contract v1 / Late-Cartridge
> environment-production proof. The exact frame remains eligible for later optional
> polish and is not frozen as final shipping artwork.

## 5. Three demonstrated production regimes

Scarlet Moon now provides evidence for three materially different environment modes:

| Regime | Construction emphasis | Demonstrated character |
| --- | --- | --- |
| V3 | tile-heavy / economical | explicit repeated tile vocabulary, strong cartridge-game construction |
| pre-profile V4 (#22 family) | larger canonical assets + assembly | richer material/depth/ornament; less hardware-constrained |
| Late-Cartridge V4 (#51) | canonical assets + assembly under #44 | 8x8/16x16, small shared palettes, stage bank, late-Famicom/NES discipline |

None of these results proves that one visual regime is universally better. They
demonstrate different production disciplines.

This is useful evidence for the broader RoboPixel proposition that the same canonical
authoring engine can support different visual-production profiles.

## 6. What is not yet proven

Do not overgeneralize #51.

Not yet empirically proven by this program:

- SNES profile;
- Mega Drive / Genesis profile;
- Game Boy profile;
- Master System profile;
- arcade-board profiles;
- a generic implemented Machine Profile Stack;
- automatic profile selection;
- automatic conversion between visual regimes.

RoboPixel's docs/MACHINE_PROFILE_STACK.md remains a conceptual design candidate,
not Scarlet Moon implementation authority.

#51 strengthens the case for future profile work because it demonstrates that one
canonical environment methodology can produce a distinct constrained result when an
explicit construction discipline is applied.

## 7. Durable acceptance lesson

A future scene should not be called successful merely because:

- all revisions validate;
- hashes match;
- palette neighborhoods conform;
- reconstruction is exact;
- packaging is reproducible.

A production result is successful only when those mechanical conditions and the
Owner's native visual review are both satisfied for the intended purpose.

For workflow/profile proofs, optional final-art polish may remain deferred after the
method has been successfully demonstrated.
