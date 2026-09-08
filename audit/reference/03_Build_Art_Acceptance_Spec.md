# Touhou NES Fan Game — Build, Art & Acceptance Specification

## Product Goal

Create a small but genuinely finished Touhou Project fan game that answers:

**"What if Touhou had somehow existed as an impossibly advanced late-era Famicom/NES vertical shooter?"**

The game must prioritize completeness, controls, boss patterns and audiovisual identity over feature count.

Target complete playthrough:

**8–12 minutes**

---

# 1. DELIVERY FORMAT

Repository structure:

```text
/
├── index.html
├── README.md
└── FANWORK_NOTICE.md
```

## index.html

The complete executable game.

Requirements:

- HTML5
- CSS
- vanilla JavaScript
- Canvas API
- Web Audio API
- no npm
- no build process
- no external JavaScript libraries
- no external fonts
- no network dependency
- no remotely loaded graphics
- no remotely loaded audio
- no extracted official Touhou assets

Opening `index.html` locally should be sufficient to play.

It must also work when hosted through GitHub Pages.

## README.md

Include:

- game description;
- controls;
- local-play instructions;
- GitHub Pages instructions;
- fan-work attribution;
- technical notes.

## FANWORK_NOTICE.md

Clearly state that:

- this is an unofficial Touhou Project fan work;
- Touhou Project, characters and setting originate with ZUN / Team Shanghai Alice;
- the implementation is not official;
- graphics/code/audio implementation were newly created for this project;
- no claim of ownership is made over Touhou Project.

---

# 2. TARGET PLATFORM

Primary target:

**Desktop modern Chromium / Firefox-class browser**

Keyboard is mandatory.

Mobile support is not required.

Gamepad support may be added only if it does not interfere with core implementation.

No server is required.

---

# 3. DISPLAY

Logical game resolution:

**256 × 240**

Rendering rules:

- Canvas scales using nearest-neighbor interpolation.
- Prefer integer scaling.
- Pixels must remain crisp.
- Never use antialiasing for game artwork.
- Center the canvas in browser window.
- Fullscreen may be supported.
- Browser background should remain unobtrusive and dark.

Gameplay layout:

Approximate:

- **192 px wide:** primary playfield
- **64 px wide:** HUD/sidebar

Minor adjustment is acceptable if necessary for readability.

Title/dialogue/ending screens may use the full 256×240 canvas.

---

# 4. CONTROLS

## Keyboard

**Arrow keys** — move  
**Z** — shoot / confirm  
**X** — bomb / cancel  
**Shift** — focus / slow movement  
**Enter** — start / pause  
**M** — mute/unmute

Holding Z should continuously fire.

Focus mode:
- slows movement;
- tightens Reimu's shot formation;
- displays her hitbox.

---

# 5. PLAYER

Playable character:

**Reimu Hakurei only**

## Movement

Target normal speed:

approximately **2.3–2.6 logical pixels/frame**

Focused movement:

approximately **1.1–1.3 logical pixels/frame**

Tune through playtesting.

Movement should feel immediately responsive.

No acceleration/inertia.

## Collision

Player collision hitbox:

approximately **4×4 pixels**

Displayed hitbox may be visually larger for legibility but collision must remain tiny and centered.

## Starting resources

- 3 lives
- 3 bombs
- Power Level 1

## Power

Four shot-power levels.

Red **P** pickups increase power.

At higher levels:
- Reimu gains stronger forward shots;
- yin-yang options/familiars become more prominent;
- focused fire becomes more concentrated.

## Bomb

NES-style interpretation of **Fantasy Seal**.

Bomb:
- grants temporary invulnerability;
- clears hostile bullets;
- damages enemies/boss;
- produces dramatic but readable screen effect.

## Deathbomb

After receiving lethal contact, provide approximately:

**8 frames**

during which pressing Bomb can prevent the death.

Tune if necessary.

## Death

On death:
- clear nearby bullets;
- brief invulnerability on respawn;
- lose some power;
- preserve stage progress.

---

# 6. ITEMS & SCORING

## Items

**P** — Power  
**Blue point item** — Score

Optional dropped life/bomb item only if needed for balance.

## Graze

Enemy bullets passing near Reimu without colliding increase:

**GRAZE**

Provide:
- small score increase;
- satisfying short high-frequency audio cue;
- subtle visual feedback.

Graze radius must be larger than collision radius.

## Point-of-Collection Line

When sufficiently powered, moving into approximately the upper quarter of the playfield automatically attracts loose items.

This mechanic should be visually obvious when activated.

## Score

Score sources:

- enemy destruction;
- point items;
- grazing;
- boss phase completion;
- spell-card capture bonuses.

High score persists only for current browser session unless easy localStorage persistence is implemented cleanly.

Persistent save infrastructure is not required.

---

# 7. CONTINUES

Continues should be generous because this is intended to be shown to friends.

**Unlimited continues.**

Continuing:
- resets score;
- restores 3 lives;
- restores 3 bombs;
- resumes from a sensible current-stage checkpoint.

At minimum:
- stage beginning;
- boss beginning once boss has been reached.

Continue screen countdown:

**⑨, 8, 7, 6, 5, 4, 3, 2, 1...**

This is intentional.

A no-continue clear is the meaningful scoring achievement.

---

# 8. DIFFICULTY

Only **one difficulty**.

Target approximately:

**forgiving Touhou Normal**

Do not implement:
- Easy;
- Hard;
- Lunatic;
- selectable difficulty.

The player should be able to see the entire game with continues.

---

# 9. STAGES

## Stage 1 — Misty Lake

Approximate pre-boss duration:

**60–80 seconds**

Visual identity:
- dark blue water;
- drifting mist;
- moon reflections;
- icy accents.

Teaches:
- aimed bullets;
- streaming;
- focus;
- graze;
- item collection.

Boss:

**Cirno**

## Stage 2 — Forest of Magic

Approximate pre-boss duration:

**75–95 seconds**

Visual identity:
- dark forest;
- mushrooms;
- stars visible through canopy;
- moving foliage/tile patterns.

Introduces:
- faster enemies;
- side-entry formations;
- rotating patterns;
- denser attacks.

Boss:

**Marisa Kirisame**

## Stage 3 — Scarlet Devil Mansion

Approximate pre-final-boss duration:

**75–90 seconds**

Visual progression:
- mansion exterior;
- sleeping Meiling gag;
- interior corridors/windows/chandeliers;
- rooftop/balcony under enormous scarlet moon.

Midboss:

**Sakuya Izayoi**

Final boss:

**Remilia Scarlet**

---

# 10. ORDINARY ENEMY VOCABULARY

Keep ordinary enemy types deliberately small.

Use approximately five reusable archetypes.

## A. Basic Fairy
Moves downward or along shallow curve.

Fires one aimed burst.

Low HP.

## B. Arc Fairy
Enters from left/right in an arc.

Fires a fan while crossing playfield.

## C. Formation Fairy
Appears in coordinated groups.

Creates geometric synchronized bullet formations.

## D. Spirit / Orb
Moves slowly.

Higher HP.

Emits radial rings.

## E. Stage-Specific Familiar
Examples:
- ice fairy behavior on Stage 1;
- star/magic familiar on Stage 2;
- bat or mansion familiar on Stage 3.

Reuse systems rather than inventing many more enemies.

---

# 11. STAGE CHOREOGRAPHY

Do not randomly spawn enemies continuously.

Each stage should be deliberately composed as short musical/gameplay phrases:

**wave → formation → breathing room → wave → escalation → item opportunity → boss transition**

Enemy choreography should line up loosely with musical measures when practical.

Difficulty should come from designed overlapping behaviors rather than raw enemy count.

---

# 12. AUDIO

All runtime audio must be newly implemented.

Use Web Audio API.

Aim for an NES/Famicom-like synthesis architecture:

- 2 pulse/square voices;
- triangle-like bass voice;
- noise percussion;
- extremely limited extra effects where useful.

Audio should evoke actual NES arrangement technique rather than generic modern "chiptune."

## Music plan

### Title / Attract
Short Touhou-style 8-bit title arrangement using a recognizable Reimu musical motif.

### Stage 1
Original stage material transitioning into an NES-style arrangement of:

**Beloved Tomboyish Girl**

for Cirno.

### Stage 2
Original forest-stage material transitioning into:

**Love-Colored Master Spark**

for Marisa.

### Stage 3
Original gothic/scarlet stage material.

### Remilia
NES-style arrangement of:

**Septette for a Dead Princess**

### Ending
Calmer arrangement based around a recognizable Reimu theme such as:

**Maiden's Capriccio**

Important:

Arrange the Touhou source compositions directly.

Do not imitate or reproduce a third-party Touhou fan arrangement.

Do not embed recordings.

## Sound effects

Required:
- player shot;
- enemy hit;
- enemy death;
- player death;
- graze;
- item pickup;
- bomb;
- menu cursor;
- spell-card start;
- boss phase clear;
- warning;
- pause;
- time stop;
- Master Spark;
- ending/credit stings.

Browser autoplay restrictions must be handled correctly.

Audio begins only after appropriate player interaction.

---

# 13. NES/FAMICOM ART DIRECTION

The game is **not** meant to be technically hardware-accurate.

It is meant to convincingly look like an unusually sophisticated late-era Famicom/NES game.

## Hard visual rules

- 256×240 logical resolution
- hard pixel edges
- nearest-neighbor scaling
- no antialiasing
- tile-oriented backgrounds
- restricted sprite palettes
- minimal animation frames
- small sprites
- NES-like bitmap typography
- no modern gradients
- no smooth vector shapes
- no modern particle aesthetic
- no bloom
- no shaders pretending to be pixel art

## Sprite scale targets

Reimu:

approximately **16×24 px**

Normal fairies:

approximately **16×16 px**

Bosses:

approximately **24×32 px**, with modest flexibility.

Bullets:

approximately **4×4 through 8×8 px**

Portraits:

small NES-style bust/head portraits built using intentionally constrained palettes.

## Intentional hardware cheats

Do NOT enforce actual NES restrictions for:

- total bullet count;
- sprite-per-scanline limits;
- CPU budget;
- object count;
- memory capacity.

Gameplay wins over hardware simulation.

Occasional simulated sprite flicker may be used sparingly to reinforce the illusion.

---

# 14. BULLET VISUAL LANGUAGE

Limit the vocabulary.

Suggested shapes:

- round pellet;
- rice/oval;
- star;
- diamond;
- ice crystal;
- knife;
- small bat-like projectile;
- large special projectile.

Player shots must never resemble hostile bullets.

Pickups must never resemble hostile bullets.

Bullet centers must visually correspond to their collision behavior.

Dense backgrounds should darken or simplify during boss patterns.

---

# 15. CHARACTER VISUAL IDENTITY

Final sprites must be newly created NES interpretations.

They should remain immediately recognizable.

## Reimu
- large red bow;
- red/white shrine-maiden silhouette;
- purification rod;
- yin-yang imagery.

## Cirno
- light-blue icy palette;
- blue dress;
- distinctive ice-wing silhouette.

## Marisa
- black witch hat;
- black/white clothing;
- broom;
- star motifs.

## Sakuya
- maid silhouette;
- silver/light hair;
- knives;
- clock/time motifs.

## Remilia
- pink/red dress;
- cap;
- bat wings;
- aristocratic/vampiric silhouette.

## Meiling
Recognizable gatekeeper color/silhouette sufficient for the sleeping cameo.

---

# 16. DIALOGUE PRESENTATION

Dialogue should resemble a late-era NES story sequence.

Use:
- character portrait;
- name;
- short text box;
- typewriter or fast-print effect;
- Z to advance;
- X optionally fast-forward/cancel type-in.

No voice acting.

No giant modern visual-novel UI.

---

# 17. PRESENTATION STATE MACHINE

Required complete flow:

```text
FAKE DEV LOGO
      ↓
FAN-WORK NOTICE
      ↓
TITLE SCREEN
      ↓
ATTRACT MODE if idle
      ↓
TITLE
      ↓
START
      ↓
INTRO
      ↓
STAGE 1
      ↓
CIRNO
      ↓
STAGE 2
      ↓
MARISA
      ↓
STAGE 3
      ↓
SAKUYA
      ↓
REMILIA
      ↓
ENDING
      ↓
CREDITS
      ↓
FINAL CARD
      ↓
TITLE SCREEN
```

Restarting must not require refreshing the webpage.

---

# 18. VISUAL REFERENCE BOARD

Before the Astra build prompt, generate **four non-production mockups**.

These are references, not game assets.

Astra should receive them with the instruction:

**Use these images only to understand composition, pixel scale, palette density, UI language and overall art direction. Do not copy them pixel-for-pixel. Create the final artwork yourself.**

## Mockup A — Title Screen

256×240 composition.

Include:
- large Japanese-style Touhou title logo;
- English subtitle;
- Reimu silhouette/sprite;
- huge moon;
- tiny menu;
- late-era Famicom/NES presentation.

Purpose:

Establish what "Touhou as NES" means before gameplay begins.

## Mockup B — Standard Gameplay

Show:
- Reimu near bottom;
- several fairies;
- moderate bullet pattern;
- point/power items;
- HUD;
- Stage 1 Misty Lake background.

Purpose:

Lock pixel scale, playfield proportions and HUD structure.

## Mockup C — Remilia Final Boss

Show:
- Remilia upper field;
- huge scarlet moon;
- very dense but readable danmaku;
- Reimu focused with visible hitbox;
- spell-card UI;
- NES-looking bullets despite impossible object count.

Purpose:

Define the game's maximum visual intensity.

## Mockup D — Dialogue

Show:
- Reimu and Marisa;
- small pixel portraits;
- NES dialogue box;
- readable bitmap text;
- simple forest background.

Purpose:

Prevent Astra from inventing a modern visual-novel interface.

---

# 19. QUALITY PRIORITY

If implementation complexity forces simplification, preserve features in this order:

1. Game functions reliably.
2. Reimu movement/dodging feels excellent.
3. Boss patterns work and are fun.
4. Bullet readability is excellent.
5. NES/Famicom visual identity is convincing.
6. Touhou character identity and personality are convincing.
7. Music/audio works.
8. Stage choreography.
9. Presentation flourishes.

Never sacrifice #1–4 to preserve lower-priority decoration.

---

# 20. FEATURES EXPLICITLY OUT OF SCOPE

Do NOT add:

- multiple playable characters;
- selectable difficulty modes;
- online leaderboard;
- multiplayer;
- crafting;
- roguelike systems;
- inventory;
- shops;
- achievements;
- unlock trees;
- extensive settings UI;
- account system;
- server backend;
- procedural levels;
- asset-download pipeline;
- game engine/framework dependency.

Do not expand scope unless absolutely necessary for reliability.

---

# 21. DEFINITION OF FINISHED

The project is **not complete merely because `index.html` loads**.

All of the following must work:

- boot sequence;
- fan-work notice;
- title;
- attract mode;
- controls;
- Reimu shooting;
- focus;
- collision;
- grazing;
- bombs;
- deathbomb;
- lives;
- power;
- scoring;
- items;
- continues;
- all three stages;
- all normal enemy archetypes;
- Cirno's three attacks;
- Marisa's four attacks;
- Sakuya's two attacks;
- Remilia's five attacks;
- every required dialogue sequence;
- all required music;
- required sound effects;
- ending;
- credits;
- return to title;
- ability to start another run;
- local-file operation;
- GitHub Pages operation.

There must be:

- no TODO placeholders;
- no placeholder art;
- no placeholder music;
- no intentionally unfinished stage;
- no missing boss attack;
- no console errors during a normal complete run.

---

# 22. TESTING EXPECTATION

Before declaring the build complete:

1. Run the game in an actual browser.
2. Test input and audio.
3. Complete or deliberately exercise all three stages.
4. Test every boss phase.
5. Test player death.
6. Test bomb.
7. Test deathbomb.
8. Test continue.
9. Test pause/resume.
10. Test ending and credits.
11. Start a second run without page refresh.
12. Check browser console for errors.
13. Fix material gameplay or presentation defects discovered.

The implementing agent should modify and retest the game rather than merely reporting problems.

---

# 23. CORE IMPLEMENTATION DIRECTIVE

**Build the game, not a game engine.**

Prefer simple explicit code for this particular game over abstractions intended for hypothetical future games.

Prefer polished handcrafted content over generic systems.

Prefer complete implementation over architectural sophistication.

Do not leave work for another agent, developer or asset artist.

The final result should feel like a tiny finished cartridge, not a prototype.
