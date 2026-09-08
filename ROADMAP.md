# Scarlet Moon development roadmap

This document records the intended development direction for **東方紅月夜 ~ Scarlet Moon Never Sets ~** beyond the first complete build.

The immediate goal is still to make **Scarlet Moon itself** a polished, accepted game. The longer-term opportunity is to let the systems that prove useful during that work gradually become a reusable HTML5/JavaScript danmaku framework and authoring environment.

That longer-term direction is intentional, but it must not derail the current game.

## Guiding rule

> **Finish and stabilize Scarlet Moon first. Extract reusable systems second. Do not prematurely rewrite the game into an engine.**

Scarlet Moon should remain the reference game that proves each reusable capability in real play. Abstractions should be introduced because repeated game-development work makes them valuable, not because an engine architecture looks attractive on paper.

The current V1 polish effort is tracked in **Issue #2** and takes precedence over framework work.

---

## Current foundation

Scarlet Moon already contains most of the raw systems a reusable danmaku framework would eventually need:

- fixed-step game loop and state progression;
- player movement, focus, shooting, hitbox, graze, bombs, deathbombs, lives, score, power and items;
- bullets, lasers and scripted projectile transformations;
- authored stage waves and enemy choreography;
- boss definitions and fourteen scripted boss phases;
- dialogue, cutscenes, attract mode, ending and credits;
- Canvas rendering and Web Audio synthesis;
- a permanent `qa/` development tool with deterministic state jumping, regression checks, diagnostics, browser automation and capture generation.

The game is therefore a strong future framework seed, but its implementation is still primarily handcrafted for this one title.

---

# Phase 0 — finish V1 Scarlet Moon

**Status: current priority.**

Complete the accepted game before performing broad engine extraction.

Primary work:

- repair objective presentation/layering defects;
- raise sprites, bosses, portraits, backgrounds, title and HUD to the approved late-era Famicom/NES quality bar;
- replace abbreviated music loops with complete authored arrangements;
- preserve working movement, collision, stage choreography and boss-pattern identity;
- use the `qa/` tool after each meaningful change;
- complete human playtesting and final acceptance.

The V1 effort is tracked in Issue #2.

**Exit condition:** Scarlet Moon is accepted as a polished game, not merely a functioning technical base.

---

# Phase 1 — stabilize the development workflow

After V1, consolidate the practices that proved useful while polishing the game.

Goals:

- keep the `qa/` development tool permanently maintained;
- expand deterministic inspection cases when new stable checkpoints are useful;
- make regression and presentation checks routine for every substantial change;
- preserve a clean distinction between shipped runtime and development tooling;
- document the major runtime subsystems and their ownership;
- establish safe conventions for future contributors and coding agents.

The QA tool may gradually become more than a test surface: it is also the natural foundation for future pattern, scene and content authoring tools.

---

# Phase 2 — identify proven reusable boundaries

Do not start by splitting everything into modules. First identify which concepts have genuinely repeated or become painful to maintain inside the single handcrafted implementation.

Likely reusable boundaries include:

- player/controller rules;
- projectile creation and behavior;
- collision/graze rules;
- stage cue scheduling;
- enemy archetypes;
- boss/phase lifecycle;
- dialogue and scene sequencing;
- rendering layers;
- music scheduling and SFX;
- score/item/power systems;
- save/session state;
- QA/debug hooks.

At this stage, refactoring should improve Scarlet Moon itself while making content/mechanics separation clearer.

**Exit condition:** the code has understandable seams between general runtime behavior and Scarlet Moon-specific content without requiring a wholesale rewrite.

---

# Phase 3 — separate content from mechanics

Gradually move from hardcoded game-specific branches toward explicit content definitions.

For example, instead of embedding every stage and boss decision directly into the main loop, move toward definitions conceptually like:

```js
stages.stage1 = {
  background: 'mistyLake',
  music: 'stage1',
  waves: [...],
  boss: 'cirno'
};
```

and:

```js
bosses.remilia.phases = [
  ScarletWaltz,
  ScarletShoot,
  Gungnir,
  ScarletGensokyo,
  RedMagic
];
```

Likely content categories:

- characters and sprites;
- portraits;
- stages/backgrounds;
- stage waves;
- bosses and phase sequences;
- bullet-pattern parameters;
- dialogue and cutscene scripts;
- music arrangements;
- ending/credits sequences.

The goal is not necessarily “easy skin swapping.” The goal is that a new game or scenario can be authored mostly by defining new content rather than rewriting core mechanics.

---

# Phase 4 — build a deliberate danmaku behavior system

Future bullet-pattern work should favor deterministic authored mathematics over a general-purpose physics engine.

Useful capabilities may include:

- ring/fan/arc emitters;
- polar-coordinate emitters;
- aimed and predictive shots;
- acceleration/deceleration;
- curvature and angular velocity;
- orbiting bullets;
- spline/path motion;
- attractors/repulsors where useful;
- timed freeze/thaw;
- redirect/retarget behavior;
- bullet splitting and transformation;
- scripted state machines/sequences;
- laser and beam geometry;
- reusable safe-gap and lane-generation helpers.

A future pattern API might express behavior conceptually as:

```js
emitRing({
  count: 32,
  speed: 1.1,
  rotation: t * 0.015,
  curve: 0.002
});
```

or:

```js
bullet.behavior = sequence(
  moveOutward(90),
  freeze(60),
  redirectTowardPlayer(),
  accelerate(0.01)
);
```

This should make sophisticated spell cards easier to author while preserving precise, reproducible geometry and fairness.

---

# Phase 5 — evolve the QA tool into an authoring environment

The current `qa/` tool already provides several pieces of a future editor/developer console:

- jump to any major scene;
- load individual boss phases;
- choose exact ticks;
- freeze/resume simulation;
- advance dialogue;
- play music and SFX independently;
- run diagnostics and regression;
- capture deterministic frames.

Potential future authoring features:

- live boss-pattern parameter controls;
- restart-current-phase controls;
- bullet count/density readouts;
- hitbox and collision overlays;
- safe-route visualization;
- stage-wave timeline editing/preview;
- scene/layer inspection;
- palette and sprite preview;
- music-channel audition/muting;
- export of edited content definitions.

The tool should remain development-only. The player-facing game should stay clean and cartridge-like.

---

# Phase 6 — reusable HTML5 danmaku framework

Once Scarlet Moon has been stabilized and content/mechanics separation has proven useful, formalize the reusable layer.

A possible development layout might eventually resemble:

```text
engine/
  loop.js
  player.js
  bullets.js
  collisions.js
  stage-runner.js
  bosses.js
  dialogue.js
  renderer.js
  audio.js

content/
  characters/
  stages/
  patterns/
  dialogue/
  music/

qa/
  ...
```

This is illustrative, not a requirement to adopt that exact structure.

Important compatibility goal: **development may become modular without requiring the published game to become complicated to distribute.** A future build step may assemble modular development sources into a self-contained browser artifact if that remains the best release format.

Do not abandon the small, portable browser-game experience merely to make the source tree look like an engine.

---

# Phase 7 — prove reuse with a second game or substantial content set

A framework is not truly reusable merely because Scarlet Moon was refactored.

Before treating the extracted runtime as a mature independent engine, use it to build at least one meaningful second consumer, such as:

- another small Touhou-style scenario;
- alternate playable content with different characters/stages/bosses;
- a separate short danmaku game;
- a substantial new Scarlet Moon content package that exercises different patterns and scene structures.

The second consumer should expose assumptions that were accidentally specific to Scarlet Moon.

Only after that proof should we strongly consider extracting the framework into its own repository or giving it a standalone identity.

---

# Architectural principles

These principles apply across the roadmap.

## 1. Game first, framework second

Scarlet Moon is not a disposable demo for an engine. Improvements must continue to benefit the actual game.

## 2. Preserve deterministic danmaku

Patterns should be reproducible and authored. Randomness may be used deliberately, but generic particle simulation should not replace designed bullet geometry.

## 3. Extract after repetition

Prefer the smallest abstraction that solves a demonstrated maintenance or authoring problem. Avoid speculative generality.

## 4. Preserve readability and feel

Movement, hitbox behavior, bullet readability and fair navigation remain more important than architectural elegance.

## 5. Keep runtime distribution simple

The current self-contained browser-game model is a feature. Development tooling and modular source organization may grow without forcing players to install a toolchain.

## 6. Keep development tooling first-class

The `qa/` tool should evolve alongside the runtime. Every reusable engine capability should be inspectable and testable.

## 7. Do not confuse visual spectacle with physics complexity

Better bullet patterns come primarily from better emitters, timing, transformations and geometry—not from adding a heavyweight physics dependency.

## 8. Scarlet Moon remains the reference implementation

As reusable systems emerge, Scarlet Moon should continue exercising them in production rather than becoming an abandoned legacy implementation.

---

# Near-term decision gates

The following decisions are intentionally deferred:

- whether the reusable framework eventually gets a separate repository;
- whether development source remains one file or becomes modular plus a build/export step;
- whether the authoring environment becomes a visual editor or remains a powerful developer console;
- whether a future framework receives a standalone name;
- how much of the music/art pipeline should become data-driven;
- whether additional input platforms or rendering backends are worthwhile.

Make these decisions when the current game and a concrete next use case provide evidence.

---

# Relationship to current work

- **Issue #2:** finish V1 Scarlet Moon. This is the active implementation priority.
- **`qa/`:** permanent development/QA tool and future authoring-tool seed.
- **This roadmap:** long-term direction, not permission to expand the current V1 repair scope.

The intended progression is:

> **working game → polished game → stable development workflow → clearer reusable boundaries → content/mechanics separation → richer danmaku behavior system → authoring environment → reusable framework → second-game proof**

That is the direction of travel unless later project experience gives a better reason to change it.
