# #45 Late-Cartridge Proof Gate

This is the acceptance contract for issue #45.

The proof is deliberately small. It exists to answer one question:

> Does the Late-Cartridge Profile produce the Scarlet Moon V4 look we actually
> want in real native gameplay?

## 1. Frozen proof scope

Use:

- Reimu gameplay;
- Mansion Interior;
- existing V4 HUD/sidebar;
- representative ordinary bullets/effects/actors;
- actual 256×240 presentation with 192×240 playfield.

Do not expand the proof into another scene, another playable character, a full
Mansion redesign, title art, dialogue, ending art or broad runtime integration.

## 2. Required comparison

Present in one review package:

1. **V3** native-equivalent gameplay evidence.
2. **Current/pre-profile V4** native-equivalent evidence.
3. **Late-Cartridge proof** at native 256×240.
4. Late-Cartridge proof at nearest-neighbor 3× for inspection.

The 1× image is the primary acceptance surface.

## 3. Required construction evidence

### Environment

Provide:
- 8×8 tile vocabulary/atlas used by the proof;
- 16×16 metatile/assembly map or equivalent construction explanation;
- background palette ledger;
- identification of quiet gameplay regions;
- any bank/phase variants.

The Mansion does not need to become a literal ROM tilemap. The proof must make
its tile logic inspectable.

### Reimu

Provide:
- 16×24 native body;
- logical 2×3 8×8 cell decomposition;
- separate gohei construction where applicable;
- sprite subpalette assignment;
- rear-facing/back-view readable at 1×;
- state comparison sufficient to show that the construction can extend beyond
  one frozen pose.

Do not enlarge Reimu's gameplay envelope merely to make the design easier.

### HUD and gameplay activity

Provide:
- sidebar/HUD palette usage;
- representative bullets/effects;
- a readability witness with Reimu and bullets over the Mansion;
- no baked-in actors/bullets inside the canonical background.

## 4. Palette acceptance

The proof must include a palette ledger showing:

- backdrop;
- background subpalettes;
- sprite subpalettes;
- HUD use;
- any deliberate palette change;
- every exception to the baseline budget.

Target baseline:
- 4 background subpalettes × 3 local colors + shared backdrop;
- 4 sprite subpalettes × 3 visible colors + transparency.

An exception is reviewable; an undocumented exception fails the proof.

## 5. Hard fail conditions

The proof fails mechanically/art-directionally if any of these occur:

- final art was downsampled from high-resolution illustration;
- antialiasing/soft resampling is present in canonical pixels;
- acceptance depends on CRT/scanline/shader treatment;
- no inspectable 8×8/16×16 environment logic exists;
- no palette ledger exists;
- Reimu is enlarged beyond the controlling gameplay envelope without separate
  Owner authority;
- official PC Touhou sprite rendering is used as the target construction style;
- bullets/actors are unreadable at native size;
- modern/vector-like smooth construction remains visible;
- the proof silently changes gameplay mechanics, hitbox, stage flow or unrelated
  V4 surfaces.

## 6. Owner visual questions

After hard gates pass, review the native frame with these questions:

### Cartridge identity

- Does this look designed for a late-life Famicom/NES cartridge rather than
  merely displayed at low resolution?
- Is it visibly more mature/rich than V3 without looking 16-bit?
- Does it avoid the "generic modern pixel-art" tell?

### Reimu

- Is Reimu recognizable immediately at 16×24?
- Does rear-facing Reimu have a clear bow/head/hair/sleeve/skirt/gohei hierarchy?
- Are state changes likely to remain readable without redesigning her from
  scratch?

### Mansion

- Do stone, glass, carpet/trim and architectural masses read through deliberate
  tile/cluster logic?
- Does the Mansion retain the strongest useful workmanship from the pre-profile
  candidate without carrying forward modern/vector-like habits?
- Is detail concentrated where it helps rather than everywhere?

### Gameplay

- Can Reimu and bullets be tracked instantly?
- Is the central playfield calm enough for danmaku?
- Does the HUD feel like part of the same cartridge?
- Does the frame still feel rich when viewed at 1× with no display effects?

### Consistency

- Could the same construction rules plausibly govern Forest, Lake, Gate,
  Rooftop, Shrine, the rest of the cast and presentation surfaces?
- Are we confident enough in the rules to stop rediscovering "late Famicom"
  asset by asset?

## 7. Acceptance outcomes

### ACCEPT

Owner accepts the machine fiction in native gameplay.

Then:
- #44 becomes the controlling construction doctrine;
- #45 becomes the concrete golden application;
- broader V4 art may resume in smaller bounded units.

### CORRECT

The direction is right but one or more rules/proof results need adjustment.

Revise #44 and/or #45 and re-review. Do not start broad production.

### REJECT

The profile does not produce the desired visual generation.

Preserve the proof as evidence, revise the doctrine, and repeat the same bounded
gate before broad production.

## 8. Stop

No result from #45 automatically authorizes:
- merging old art PRs;
- full environment polish;
- whole-cast redraw;
- runtime-wide integration;
- publication;
- V4 freeze/release.
