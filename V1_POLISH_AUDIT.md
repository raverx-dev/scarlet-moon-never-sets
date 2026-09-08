# V1 polish and acceptance audit

Status: **COMPLETE — CURRENT BUILD DOES NOT MEET CREATIVE ACCEPTANCE**  
Audit scope: diagnosis only; no shipped game behavior changed.  
Baseline: `main`, commit `08c2a1704a1943ee8d57b402e7a962395ab3f85b`.  
Executable SHA-256 recorded by the original audit: `b891b4e6f4f7e6cd07111f584897219520bfe89ffde09c06db66d331fe222eb5`.  
Audit branch: `v1-polish-audit`.

## Executive conclusion

The first Astra build is a **functionally substantial and recoverable game implementation**, not a throwaway prototype. Its state machine, player mechanics, authored stage waves, all fourteen boss phases, dialogue flow, continues, ending, credits, Web Audio runtime, and return-to-title loop are present and survive the recovered regression suite.

The build nevertheless **fails the approved V1 acceptance bar** because the visual and musical realization is materially below the agreed late-era Famicom/NES target. The primary problem is not the game architecture or the boss-pattern implementation. It is an underdeveloped art/audio/presentation layer plus several concrete rendering/layering bugs.

The correct remediation strategy is therefore **preserve the game systems and overhaul the weak presentation layers**, not rebuild the game.

This completed recovery audit synthesizes:

- the original authoritative written specifications;
- all four approved mockups already preserved under `audit/reference/`;
- the existing visual inspection and evidence captured before the Astra rate-limit interruption;
- the recovered 32-group regression suite and its committed result;
- direct source review of `index.html`;
- deterministic QA inspection tooling under `qa/`;
- user human-play feedback gathered from the published game.

No new image captures were required to finish this document. Existing evidence is retained; future agents should capture additional images only when they support a genuinely new finding.

---

# 1. What is already accepted as a foundation

These areas should be preserved unless a later repair specifically requires touching them.

## Functional game loop — PASS

The recovered regression result is **32 passed / 0 failed** and exercises:

- fresh resources;
- immediate movement and normalized diagonals;
- focused movement;
- held fire and all four power levels;
- point and power items;
- collection-line behavior;
- tiny hitbox and graze;
- delayed death and the eight-frame deathbomb window;
- bomb stock and power loss;
- pause/resume;
- continues and score reset;
- player shots against enemies and bosses;
- spell-capture scoring and bomb forfeiture;
- laser telegraph/collision state;
- Red Magic survival timing;
- all dialogue pages;
- all fourteen boss phases;
- all three stages;
- ending and credits;
- attract/how-to-play round trip;
- audio initialization, track changes, effects, and mute;
- return to title and a second run.

This is strong evidence that the game is a viable base for V1 polish.

## Boss-pattern identity — PASS WITH LATER HUMAN TUNING

Source review confirms that the intended attack ideas are genuinely implemented rather than replaced by random spam:

- Cirno: aimed Cold Snap, Icicle Fall wall/gap behavior, Perfect Freeze field stop/resume;
- Marisa: curved star sweep, opposed rotating Stardust Reverie layers, telegraphed Non-Directional Laser, wide Master Spark with perimeter fire;
- Sakuya: knife geometry and Private Square freeze/redirect behavior;
- Remilia: Scarlet Waltz, bat-wing Scarlet Shoot, Gungnir spear hazard, counter-rotating Scarlet Gensokyo, escalating Red Magic.

The regression measured a peak of **194 hostile objects in Red Magic**, satisfying the intended impossible-NES density target.

This does not certify subjective difficulty; human playtesting remains necessary after presentation work so visual changes do not accidentally damage readability.

## Stage choreography — PASS AS A STRUCTURAL BASE

`WAVES` contains authored timed cue lists rather than continuous random spawning. The current ordinary stages are therefore suitable for polish rather than replacement.

## Distribution/runtime architecture — PASS

The shipped game remains a self-contained `index.html` using vanilla JavaScript, Canvas, and Web Audio. The development-only QA tooling may use Node/npm without changing the runtime delivery contract.

---

# 2. Confirmed findings

Severity meanings:

- **Critical** — central project promise is not met; V1 cannot ship as accepted.
- **Major** — clearly visible/audible deficiency requiring intentional repair.
- **Moderate** — real defect or quality problem, but localized.
- **Minor** — cleanup/polish after larger work.

Classification meanings:

- **BUG** — implementation/rendering is objectively wrong.
- **SPEC DEVIATION** — implementation exists but materially misses an approved requirement/reference.
- **POLISH** — technically valid but not at the desired quality bar.
- **VALIDATION GAP** — no confirmed defect, but acceptance still requires targeted human review.

---

## BUG-001 — fractional sprite scaling corrupts pixel structure

**Severity:** Major  
**Location:** Boss rendering, portraits, title/presentation sprites, HUD life icons  
**Confidence:** High

**Observed**

The sprite renderer operates on one source pixel at a time, but many callers pass fractional scales such as `1.25`, `1.4`, `1.45`, `1.5`, `1.6`, `2.5`, and `.65`. `rect()` independently rounds the destination position and destination width/height. This creates nonuniform source-pixel expansion and can produce visible grid/seam distortion through scaled sprites. The interrupted Astra visual pass explicitly identified a visible grid through boss artwork.

**Expected**

Hard, intentional NES/Famicom pixel clusters with no resampling-like artifacts.

**Supporting requirements**

`03_Build_Art_Acceptance_Spec.md` §13: hard pixel edges, nearest-neighbor character, restricted sprite palettes, small sprites. The mockups establish deliberate integer-looking pixel density.

**Recommended correction**

Do not repair this by smoothing. Keep pixel rendering hard. Replace fractional enlargement of source sprite matrices with one of:

1. artwork authored directly at the intended logical pixel dimensions; or
2. integer-only source-pixel scaling where enlargement is genuinely needed.

Bosses should preferably receive proper target-size sprite art instead of magnifying tiny matrices.

---

## BUG-002 — attract-mode close-up draws duplicate Reimu and duplicate moons

**Severity:** Major  
**Location:** Attract mode, approximately the `REIMU: FINE.` beat  
**Confidence:** High

**Observed**

`drawAttract()` first calls `shrine(false,t)`, which already draws the scarlet moon, and immediately draws a standing Reimu. During the final shrine beat it then draws another large moon and another flying Reimu without removing/recomposing the earlier scene elements. This matches the published-game screenshot showing two Reimus/two moons.

**Expected**

A deliberate close-up/composition change with exactly the intended actors and scenery.

**Recommended correction**

Separate scene rendering into background/scenery/actors/effects/UI ownership. For this beat, draw the intended close-up from explicit layers rather than stacking a second composition on top of the first.

---

## BUG-003 — ending-dialogue draw order obscures the compensation gag

**Severity:** Moderate  
**Location:** Final Reimu/Remilia shrine dialogue  
**Confidence:** High

**Observed**

The ending scene draws Reimu, Remilia, the donation box, and the compensation coin and then draws the large dialogue box beginning at `y=174`. The coin is placed at approximately the same boundary and important lower-scene pixels are repainted by the dialogue UI. The original Astra visual inspection flagged this scene for layering defects.

**Expected**

The one-coin compensation gag should read immediately while dialogue remains legible.

**Recommended correction**

Recompose the ending scene so foreground story props remain visible. Establish explicit scene → actors/props → dialogue UI layering and place the coin where the box cannot cover it.

---

## BUG-004 — Cirno credits gag paints the freeze box over the character

**Severity:** Moderate  
**Location:** Credits, Cirno/STAFF segment  
**Confidence:** High

**Observed**

The credits renderer draws Cirno first and then, after the freeze beat, draws an opaque `box()` across the same area. Because `box()` has a black interior, it obscures the sprite rather than convincingly freezing/encasing it. The interrupted Astra audit independently identified the Cirno credits as having a layering defect.

**Expected**

The gag should visibly read as Cirno freezing STAFF/herself, not as UI geometry covering the sprite.

**Recommended correction**

Draw the ice effect behind/around the character or use transparent-looking pixel crystal borders/highlights rather than an opaque black-centered UI box.

---

## SPEC-001 — overall visual language is substantially below the approved late-era Famicom/NES target

**Severity:** Critical  
**Location:** Whole game  
**Confidence:** High

**Observed**

The current presentation is dominated by flat primitives, sparse repeated geometry, tiny matrix sprites, minimal shading, and limited environmental detail. Human feedback consistently describes the result as closer to an early Atari-era visual impression than the sophisticated late-Famicom/NES target. The interrupted Astra visual pass concluded that the title, portraits, and stage environments fall materially below the approved references.

**Expected**

An unusually sophisticated late-era Famicom/NES game: strong pixel clusters, purposeful constrained palettes, tile-oriented backgrounds, recognizable character silhouettes, deliberate UI language, and rich composition while preserving the 256×240 logical presentation.

**Supporting requirements**

`03_Build_Art_Acceptance_Spec.md` §§13–18 and all four visual references. The master implementation directive describes the target as a "tiny lost cartridge," not a generic retro web-game prototype.

**Recommended correction**

Perform a dedicated art/presentation overhaul while retaining the existing renderer/state machine wherever practical. Do not merely add more particles. Replace the core sprite/background/UI assets and drawing routines with deliberately authored late-NES compositions.

---

## SPEC-002 — stage environments are too sparse and abstract

**Severity:** Major  
**Location:** Misty Lake, Forest of Magic, Scarlet Devil Mansion interior/roof  
**Confidence:** High

**Observed**

The environment functions are primarily procedural rectangles, lines, a few repeated structures, and simple moving marks. They identify broad themes but do not provide the tile density, environmental identity, or depth suggested by the gameplay/dialogue mockups. Stage 1 in particular can read simply as a large blue field rather than unmistakably Misty Lake.

**Expected**

Immediately recognizable location-specific late-NES backgrounds with controlled detail and good bullet contrast.

**Recommended correction**

Create a small authored tile vocabulary per stage (water/mist/shore silhouettes; forest trunks/canopy/magic accents; mansion wall/window/floor/roof architecture) and assemble backgrounds from those tiles. Keep boss backgrounds simplified/darkened for readability.

---

## SPEC-003 — boss sprites are undersized/under-detailed and rely on magnification

**Severity:** Major  
**Location:** Cirno, Marisa, Sakuya, Remilia battles  
**Confidence:** High

**Observed**

Bosses are represented by small matrix sprites and then rendered at fractional scale (`1.25`, Remilia `1.45`). Cirno and Sakuya source matrices are especially short vertically. The resulting silhouettes are functional but lack the bespoke boss presence established by the specification and references.

**Expected**

Approximately 24×32 logical-pixel boss art, with modest flexibility, immediately recognizable from silhouette and palette.

**Recommended correction**

Author proper boss-sized sprites at their final logical dimensions. Give each boss at least a strong idle/attack pose language and a small number of clean animation states. Do not solve size by fractional scaling.

---

## SPEC-004 — ordinary fairies compete visually with Reimu

**Severity:** Major  
**Location:** Ordinary stage enemies  
**Confidence:** High

**Observed**

The generic fairy sprite uses prominent red/white humanoid/bow-like color masses—the same core visual vocabulary that identifies Reimu. In play, multiple ordinary enemies can read as small Reimu-like figures, weakening instant player/enemy separation.

**Expected**

Player, hostile enemies, hostile bullets, items, and effects should be distinguishable immediately.

**Supporting requirements**

Master prompt §Gameplay Quality / Bullet readability and `03_Build_Art_Acceptance_Spec.md` character identity rules.

**Recommended correction**

Reserve Reimu's strongest red/white/bow silhouette for Reimu. Redesign ordinary fairies with stage-appropriate enemy palettes and a different wing/body silhouette while keeping them around the intended 16×16 scale.

---

## SPEC-005 — dialogue portraits are scaled gameplay sprites rather than bespoke portraits

**Severity:** Major  
**Location:** Dialogue UI  
**Confidence:** High

**Observed**

`portrait()` clips and renders the same gameplay sprite at scale `2` inside a portrait box. The specification explicitly calls for small NES-style bust/head portraits. The interrupted Astra visual review classified portrait quality as materially below the reference.

**Expected**

Recognizable, expressive constrained-palette portrait art designed for dialogue framing.

**Recommended correction**

Create separate portrait/bust data for Reimu, Cirno, Marisa, Sakuya, and Remilia. Keep the small dialogue box/typewriter system, but stop treating enlarged field sprites as portraits.

---

## SPEC-006 — title-screen composition falls below the approved reference

**Severity:** Major  
**Location:** Title screen  
**Confidence:** High

**Observed**

The title has the required moon, logo, Reimu, menu, and attribution, but a large black block dominates the lower/middle composition and the custom logo/sprite/background detail is much simpler than the approved title reference. Astra's interrupted visual review independently flagged title quality as materially below reference.

**Expected**

A convincing late-era Famicom title composition that establishes the game's visual ambition before gameplay starts.

**Recommended correction**

Recompose the title using a richer shrine/torii silhouette layer, deliberate scarlet-moon framing, stronger Japanese logo pixel work, and a better-integrated small menu. Preserve readability and the existing required legal/fan-work line.

---

## SPEC-007 — HUD is functional but visually under-designed

**Severity:** Moderate  
**Location:** 64-pixel right-side HUD  
**Confidence:** Medium-high

**Observed**

The HUD presents the required information but is mostly plain bitmap text and boxes. Life icons use a fractionally scaled Reimu sprite (`.65`), inheriting the scaling artifact problem. The presentation does not yet match the decorative/compact late-NES UI language shown in the gameplay reference.

**Expected**

Readable score/lives/bombs/power/graze/stage information with a deliberate cartridge-era frame/icon language.

**Recommended correction**

Retain the 192+64 layout but redesign separators, icons, life markers, bomb markers, labels, and small decorative motifs at final integer pixel sizes.

---

## POLISH-001 — character animation is too static for the intended sophistication

**Severity:** Moderate  
**Location:** Player, bosses, story scenes  
**Confidence:** Medium-high

**Observed**

Most character matrices are single static frames. Movement is largely positional; Remilia receives a small procedural wing-line motion and some scenes move sprites across the screen, but there is little authored frame animation.

**Expected**

The specification allows minimal animation frames, but the target is still an unusually polished late-era game rather than static tokens moving over a field.

**Recommended correction**

Add only high-value frames: Reimu movement/focus or firing variation, boss idle/attack/hit states, Cirno freeze pose, Marisa attack pose, Sakuya time-stop pose, Remilia final-phase pose. Keep the frame count deliberately small.

---

## AUDIO-001 — almost every music track loops after only ~6–8 seconds

**Severity:** Critical  
**Location:** Music system  
**Confidence:** High

**Observed**

Source inspection shows every normal song is exactly 64 sixteenth-note steps. At the configured BPM values the complete loop durations are:

| Track | Loop duration |
| --- | ---: |
| Title | 7.27 s |
| Stage 1 | 7.27 s |
| Cirno | 6.23 s |
| Stage 2 | 6.67 s |
| Marisa | 5.85 s |
| Stage 3 | 7.62 s |
| Sakuya | 6.32 s |
| Remilia | 6.49 s |
| Ending | 20.00 s |

This exactly explains the human-play report that the music repeats the same tiny phrase over and over.

**Expected**

Purposeful NES/Famicom arrangements with enough structure to function as stage and boss music, including recognizable Touhou material where specified.

**Recommended correction**

Replace the short scores with real arrangements. Target roughly 45–75 seconds for stage loops and 45–90 seconds for major boss loops where practical, using explicit sections (intro/A/A'/B/return) rather than repeating one four-bar phrase.

---

## AUDIO-002 — accompaniment is largely procedural rather than authored arrangement writing

**Severity:** Major  
**Location:** Web Audio music engine/data  
**Confidence:** High

**Observed**

Each song supplies one authored `lead` phrase and four bass roots. The second pulse channel is generated from a repeating four-step multiplier pattern over the bass root; the triangle similarly follows a simple repeating bass rule; noise percussion fires on a repeating fixed grid. The engine is technically four-voice and NES-like, but the supporting voices do not contain song-specific composed counterlines/rhythmic development.

**Expected**

The approved audio direction asks for something that sounds deliberately adapted for Famicom-like synthesis rather than generic square-wave accompaniment.

**Recommended correction**

Preserve Web Audio and the limited-channel discipline, but change song data to explicit per-track pulse-1, pulse-2, triangle/bass, and noise/percussion arrangements. Allow the engine to schedule authored events rather than deriving nearly all accompaniment from four roots.

---

## AUDIO-003 — required Touhou-theme arrangement fidelity is not demonstrated to acceptance level

**Severity:** Major  
**Location:** Title/Reimu material, Cirno, Marisa, Remilia, ending  
**Confidence:** Medium-high

**Observed**

The code comments record a check for the Reimu motif and a shared Marisa motif, but the committed build/audit does not establish that the Cirno and Remilia tracks are recognizable, structurally adequate arrangements of the specified compositions. The tiny loop lengths alone prevent the music from functioning as complete adaptations.

**Expected**

Direct new NES-style adaptations of the specified Touhou compositions, without third-party fan arrangements or recordings.

**Recommended correction**

During the audio overhaul, verify the source-theme melody/harmony against legitimate source/reference material and document which sections were adapted. The new arrangements should remain original implementations, not copied recordings or third-party arrangements.

---

## POLISH-002 — rendering responsibilities are too entangled, causing recurring scene-layer defects

**Severity:** Major  
**Location:** Presentation architecture  
**Confidence:** High

**Observed**

Helpers such as `shrine()` draw background, celestial scenery, architecture, and the donation box together. Higher-level states then add alternate moons, actors, props, and UI. The attract and ending defects are direct consequences of not having clear ownership of scene layers.

**Expected**

Simple but deterministic late-NES scene composition.

**Recommended correction**

Without turning the project into a general engine, separate presentation responsibilities into a few explicit layers/functions:

`background → scenery/props → actors → effects → dialogue/UI`.

This is a small architecture cleanup justified by concrete bugs, not an engine rewrite.

---

# 3. Areas reviewed with no current blocker

The audit found no evidence requiring a rewrite of the following systems:

- input/control mapping;
- focused movement;
- player hitbox/deathbomb flow;
- score/power/item core mechanics;
- continue behavior;
- stage cue scheduling;
- core boss attack sequencing;
- freeze/time-stop mechanics;
- laser telegraph state;
- Red Magic object-count target;
- dialogue text content/character tone;
- fan-work notice and attribution structure;
- title-to-credits state progression;
- restart without page reload;
- runtime self-containment.

These may receive incidental fixes during polish, but they should not be proactively redesigned.

---

# 4. Validation gaps that remain after this audit

These are **not reasons to keep Astra involved** and are not missing audit work. They are validation steps to run after repairs, because the current build is already known to fail acceptance.

## VALIDATION-001 — human difficulty/fairness

The recovered regression uses invulnerability/direct simulation and cannot prove that Normal-ish difficulty feels fair to a human. After art changes, human-play at least one full run and targeted boss phases to verify readable routes, collision clarity, and progression.

## VALIDATION-002 — subjective SFX quality

The regression proves effects trigger, not that every effect sounds good. During the audio pass, audition shot/hit/death/graze/item/bomb/menu/spell/clear/warning/pause/time-stop/Master Spark/ending effects in isolation using the QA selector.

## VALIDATION-003 — target-browser smoke test

The original README noted that file://, Firefox, and deployed Pages were not all directly tested in the original sandbox. The published Pages build is confirmed playable by human use. After V1 changes, smoke-test current Chrome/Chromium plus Firefox if available and verify no material console errors.

---

# 5. Prioritized remediation plan

## P0 — concrete rendering bugs and QA safety

Fix first because they are objective and local:

1. BUG-001 fractional sprite scaling artifacts.
2. BUG-002 attract duplicate Reimu/moon composition.
3. BUG-003 ending-dialogue prop/UI layering.
4. BUG-004 Cirno credits layering.
5. Keep the recovered regression suite green after each change.

## P1 — visual identity overhaul

Treat this as one coherent art-direction pass rather than isolated cosmetic patches:

1. SPEC-001 overall late-Famicom/NES fidelity.
2. SPEC-002 stage environments.
3. SPEC-003 boss sprites.
4. SPEC-004 ordinary fairy/player distinction.
5. SPEC-005 bespoke dialogue portraits.
6. SPEC-006 title composition.
7. SPEC-007 HUD treatment.
8. POLISH-001 targeted animation.
9. POLISH-002 simple layer separation where needed.

Do not change boss geometry or core game mechanics merely because art is changing.

## P1 — audio overhaul (parallelizable with art once interfaces are stable)

1. AUDIO-001 replace 6–8 second loops with complete arrangements.
2. AUDIO-002 author supporting channels instead of generic accompaniment formulas.
3. AUDIO-003 verify required Touhou theme identity.
4. Audition and polish SFX.

Preserve the self-contained Web Audio runtime unless a small refactor materially improves authoring.

## P2 — playtest/tuning

After visual/audio work:

- run automated regression;
- regenerate the standard local QA capture matrix;
- compare changed scenes with `audit/reference/`;
- human-play the full run;
- specifically replay C2/C3, M3/M4, S2, R3/R4/R5;
- tune density/timing only where human play shows a real problem.

## P3 — final acceptance

A V1 candidate passes when:

- all Critical/Major findings above are closed;
- no objective scene-layer bugs remain;
- music no longer consists of tiny repetitive phrase loops;
- the title, stages, dialogue, bosses, and HUD convincingly share one late-era Famicom/NES art language;
- functional regression remains green;
- no material console errors appear;
- a human full run completes with acceptable readability/fairness;
- the ending/credits/title-return loop is visually clean.

---

# 6. QA tooling disposition

The recovered QA system is now a durable project asset rather than recovery-only scaffolding.

`qa/` contains:

- recovered direct-simulation regression checks;
- deterministic scene/boss inspection controls;
- local disposable-build tooling;
- a development server;
- a versioned acceptance capture matrix;
- a headless agent runner that can execute regression/diagnostics and capture the standard canvas states with a locally installed Chrome/Chromium/Edge browser.

Generated QA reports/captures stay under gitignored `qa/output/`. Developers should commit only evidence that supports a specific durable finding.

This harness should remain available to future maintainers even after the current V1 repair effort is complete.

---

# Final acceptance decision

**FUNCTIONAL FOUNDATION: PASS**  
**BOSS/STATE-MACHINE FOUNDATION: PASS**  
**V1 VISUAL ACCEPTANCE: FAIL**  
**V1 MUSIC ACCEPTANCE: FAIL**  
**OVERALL CURRENT BUILD: NOT ACCEPTED AS FINAL V1**

No further Astra recovery is required. The project can proceed using the repository, the recovered QA harness, ordinary local coding agents, and human playtesting.
