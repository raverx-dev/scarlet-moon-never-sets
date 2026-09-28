# Late-Cartridge Reference Index

This file records the small reference set behind #44.

No third-party game art is copied into this directory. External material is for
method, technical understanding and construction vocabulary only.

## 1. Internal Scarlet Moon evidence

### Product/program
- #24 — V4 production plan and current course correction.
- #31 — Manager continuity.
- #44 — Late-Cartridge Profile.
- #45 — dependent native gameplay proof.

### Environment workmanship evidence
- Mansion Gate Exterior — PR #29 at
  `796f76d4c173ce4ae5287d20d74d9c37b8f1c8c4`.
- Mansion Interior — PR #22 at
  `c2241001946ac5456293f9f2b8be137e5c5bc648`.
- Forest — PR #26 at
  `08c2c5364d7e4a5eaa4fbb43e97209e5abf145e0`.
- Misty Lake — PR #34 at
  `040c405e912c85b38f08d7ba4a0660e76cb821a1`.
- Rooftop / Remilia — PR #37 at
  `468e793d03b90d5c30b2ac09ea8992b9af7eb6c9`.
- Shrine — PR #39 at
  `8438cd4e04e82c12a9f16932ed4fc639f5c2979b`.
- #40 merged environment evidence board — workmanship/anti-pattern evidence,
  not final construction authority.
- PR #33 — runtime integration-method evidence only.

### Character evidence
- #28 / preserved reconnaissance — actual state/canvas/anchor/runtime truth.
- Owner-approved six-character V4 design sheets — identity/design evidence.
- #42 / PR #43 — held pre-profile research evidence.
- Official Touhou sprites — pose/orientation/state vocabulary only where useful.

## 2. Drillimation — method evidence

Use Drillimation to study **discipline**, not Scarlet Moon's final look.

- Touhou NES Demakes FAQ  
  https://drillimation.com/ja-touhou-project-nes-demakes-faq/
- Touhou 2 development history  
  https://drillimation.com/2020/10/16/the-story-of-touhou-2-the-story-of-eastern-wonderland-nes-demakes-development/
- Touhou 4 development history  
  https://drillimation.com/2022/02/04/the-story-of-touhou-4-lotus-land-story-nes-demakes-development/
- Touhou 5 development history  
  https://drillimation.com/2022/06/04/the-making-of-the-touhou-5-mystic-square-nes-demake/
- Touhou 4 demake source  
  https://github.com/Drillimation/Touhou-4-Lotus-Land-Story-NES-Demake

Transferable lesson: establish a stable NES-shaped production system, then feed
content through it rather than deciding "what looks NES" separately for every
asset.

## 3. NES/Famicom technical anchors

### PPU / palette / attribute behavior
- https://www.nesdev.org/wiki/PPU_programmer_reference
- https://www.nesdev.org/wiki/PPU_palettes

Relevant construction facts:
- 8×8 tile graphics are fundamental;
- normal background palette selection is organized on 16×16 regions;
- background and sprite graphics each select from four small palettes;
- sprite objects are 8×8 or 8×16 and larger characters are assembled as
  metasprites.

### Late bank-switched cartridge mental model
- https://www.nesdev.org/wiki/MMC3
- https://www.nesdev.org/wiki/Programming_MMC3

Use MMC3-class bank switching as a useful visual-resource fiction, not a literal
implementation requirement.

## 4. Late-era visual inspection targets

These are **construction-vocabulary targets**, not asset sources and not a
ranking.

### Ninja Gaiden II
Inspect:
- readable character silhouettes;
- broad value/shadow grouping;
- cinematic staging;
- controlled environment detail.

### Castlevania III / Akumajou Densetsu
Inspect:
- Gothic architectural mass;
- material-specific tile vocabulary;
- selective ornament;
- dark-value hierarchy and readable actors.

### Batman (NES, Sunsoft)
Inspect:
- compact character shading;
- industrial tile vocabulary;
- high-contrast palettes;
- depth from a small number of values.

### Shatterhand
Inspect:
- late-era environment density without losing actor readability;
- strong reusable structural tiles;
- varied material treatment.

### Crisis Force (Famicom)
Inspect:
- shooter-specific readability;
- large/banked spectacle;
- scrolling background richness;
- boss/phase escalation without abandoning 8-bit grammar.

### Kirby's Adventure
Inspect:
- late-era banked richness;
- animation and state variety;
- confident palette organization.

Do not average these games into one art style. Extract **techniques** that are
compatible with Scarlet Moon's Gothic/Touhou identity.

## 5. Reference-selection rule for later art units

A later brief should normally contain only:
- this profile;
- exact Scarlet Moon state/canvas/runtime requirements;
- the accepted design/identity reference;
- 2–4 narrowly relevant late-era construction examples;
- the prior native candidate when useful.

More references are not automatically better.
