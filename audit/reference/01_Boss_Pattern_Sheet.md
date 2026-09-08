# Touhou NES Fan Game — Boss Pattern Sheet

## Game

**東方紅月夜 ~ Scarlet Moon Never Sets ~**  
Working/final title unless changed before the Astra build prompt.

This is a miniature Touhou Project fan game reimagined with a late-era Famicom/NES visual and audio language.

The boss encounters should feel authentically Touhou rather than like generic arcade-shooter bosses. Existing recognizable Touhou spell-card names may be used, but their implementation in this game should be newly designed for the NES-style format rather than reproducing an existing game's exact patterns.

## Universal Boss Rules

- Boss movement should be graceful and readable rather than random.
- Every major pattern must have a recognizable visual idea.
- Dense patterns must still expose understandable routes through the bullets.
- Bullets should threaten primarily through geometry and movement, not poor visibility.
- New attacks receive roughly 0.75–1.25 seconds of visual breathing room before becoming dangerous.
- Clearing a phase cancels remaining enemy bullets into harmless score items or sparkles.
- Spell cards award a bonus if cleared without dying or bombing.
- Bosses have a visible health/timer display.
- Pattern names appear briefly when spell cards begin.
- Background brightness should reduce slightly during especially dense attacks.
- No decorative particle should resemble an enemy bullet.

---

# STAGE 1 — CIRNO

**Purpose:** Teach the player how Touhou-style bullet patterns work while immediately establishing humor and personality.

Cirno is confident, aggressive, easy to read, and considerably more dangerous than Reimu thinks she is.

Target encounter length: **~90 seconds**

## Attack C1 — Cold Snap

**Type:** Nonspell  
**Purpose:** Teach aimed movement and streaming.

Cirno moves between three upper-screen positions.

Every burst contains:
- one narrow aimed fan targeting Reimu's current position;
- several slower ice pellets surrounding it;
- occasional six-way snowflake bursts.

The intended solution is to move slowly sideways rather than panic-dodge.

**Density:** Low–moderate  
**Speed:** Moderate  
**Visual language:** Pale-blue pellets, tiny ice crystals.

This should feel like the player's first "real Touhou" attack.

## Attack C2 — Ice Sign 「Icicle Fall」

**Type:** Spell card  
**Purpose:** Teach spatial pattern recognition and provide the first fandom joke.

Cirno releases descending curtains of icicles from alternating angles.

The pattern forms dramatic walls that look intimidating but contain generous geometric openings.

There should also be a deliberately ridiculous **near-boss safe region** that an experienced player can discover, referencing the long-running Icicle Fall joke without requiring the player to know it.

Cirno looks extremely proud of herself while using it.

**Density:** Moderate  
**Speed:** Slow–moderate  
**Pattern identity:** Angled icicle walls with conspicuous holes.

## Attack C3 — Freeze Sign 「Perfect Freeze」

**Type:** Final spell  
**Purpose:** Introduce bullet-state changes.

Cirno emits several waves of blue and white bullets.

Sequence:

1. Bullets expand outward normally.
2. A sharp audio cue sounds.
3. Every hostile bullet freezes in place.
4. Cirno continues adding a smaller second layer.
5. Frozen bullets flash.
6. Everything resumes simultaneously, with some bullets continuing on slightly altered angles.

The player should use the frozen moment to identify an escape lane rather than simply moving randomly.

The final cycle becomes substantially denser.

**Density:** Moderate → high  
**Signature effect:** Entire bullet field freezes.

On defeat, Cirno falls downward in exaggerated NES fashion.

---

# STAGE 2 — MARISA KIRISAME

**Purpose:** Test speed, positioning, lasers, and deliberate aggression.

Target encounter length: **~110 seconds**

Marisa fights significantly faster than Cirno and behaves like someone who is enjoying herself.

## Attack M1 — Star Sweep

**Type:** Nonspell  
**Purpose:** Establish Marisa's speed.

Marisa rapidly dashes between upper-screen positions, leaving star bursts behind.

Each dash creates:
- a curved trail of small stars;
- one aimed burst;
- occasional larger slow stars that become temporary obstacles.

The player must pay attention to Marisa's movement rather than stare only at Reimu.

**Density:** Moderate  
**Speed:** Fast

## Attack M2 — Magic Sign 「Stardust Reverie」

**Type:** Spell card  
**Purpose:** Create flowing rotational movement.

Marisa produces overlapping rotating arcs of multicolored star bullets.

One rotation moves clockwise while a second, slower layer moves counterclockwise.

Periodic aimed stars force Reimu to abandon comfortable static positions.

The resulting shape should look like a rotating galaxy rendered with tiny NES star sprites.

**Density:** High but orderly  
**Speed:** Moderate

## Attack M3 — Magic Sign 「Non-Directional Laser」

**Type:** Spell card  
**Purpose:** Teach laser telegraphs and area denial.

Several narrow laser lines appear around Marisa as harmless flashing telegraphs.

After a brief warning they become solid.

Their angles rotate between activations while ordinary star bullets fill the remaining space.

Lasers must always telegraph clearly before becoming lethal.

NES interpretation:
- hard straight pixel beams;
- bright core;
- simple blinking warning line;
- no smooth modern bloom.

**Density:** Moderate bullets + strong area denial

## Attack M4 — Love Sign 「Master Spark」

**Type:** Final spell  
**Purpose:** Deliver Stage 2 spectacle.

Marisa moves to one side of the upper screen.

A large flashing warning line targets approximately toward Reimu.

Then:

**MASTER SPARK.**

An enormous NES-style beam consumes a major section of the playfield.

While the beam persists:
- star bullets spill around its perimeter;
- Reimu must move around the beam rather than simply hug the bottom;
- Marisa changes position between firings.

Final cycle:
- faster reposition;
- shorter telegraph;
- substantially heavier star field.

The beam should feel hilariously oversized for a "NES" game.

---

# STAGE 3 MIDBOSS — SAKUYA IZAYOI

**Purpose:** Introduce knife geometry and time manipulation immediately before the final boss.

Target encounter: **~45–60 seconds**

## Attack S1 — Illusion Sign 「Killing Doll」

Sakuya emits rings and fans of knife-shaped bullets.

Unlike round bullets, their visual orientation follows their direction of movement.

Patterns alternate between:
- radial knife rings;
- aimed knife fans;
- crossing diagonals.

The attack should be crisp and geometric.

## Attack S2 — Time Sign 「Private Square」

Sakuya fills the screen with several incomplete knife formations.

A clock-like sound plays.

**Time stops.**

All hostile bullets freeze.

Sakuya moves to a new position and places additional knives.

Second clock sound.

Everything resumes simultaneously.

Some previously frozen knives redirect toward Reimu's position at the instant time resumes.

The freeze must never create an unavoidable trap; the player should be able to inspect the frozen pattern and find a route.

After defeat, Sakuya exits rather than exploding dramatically.

---

# FINAL BOSS — REMILIA SCARLET

**Purpose:** Deliver the full bullet-hell payoff.

Target encounter: **~2–2.5 minutes**

Her battle should escalate from elegant patterns into a screen that looks impossible for an NES to produce.

## Attack R1 — Scarlet Waltz

**Type:** Nonspell

Remilia moves in smooth horizontal arcs.

She releases:
- red aimed fans;
- slower purple rings;
- small bat-shaped formations.

The opposing velocities create the feeling of weaving through moving curtains.

**Density:** Moderate–high  
**Tone:** Controlled, elegant, confident.

## Attack R2 — Scarlet Sign 「Scarlet Shoot」

Remilia fires bursts that unfold into enormous symmetrical **bat-wing shapes**.

Each wing consists of curved red projectile chains.

Successive wings overlap at different angles.

Occasional aimed bullets prevent simply memorizing one stationary safe location.

The symmetry should be visually striking on a 256×240 screen.

## Attack R3 — Divine Spear 「Spear the Gungnir」

A flashing spear-shaped warning appears.

Remilia launches a large scarlet projectile through the field.

The spear itself creates a major moving hazard while smaller bullets shed from its path in angled streams.

Later cycles use two crossing spear trajectories, but never simultaneously in a way that produces unavoidable damage.

The spear should be represented as an enormous multi-sprite NES object.

## Attack R4 — 「Scarlet Gensokyo」

The screen fills with rotating crimson rings.

Alternating rings rotate in opposite directions.

Small gaps migrate around the circles, forcing controlled focused movement.

Every few seconds Remilia adds an aimed burst that temporarily disrupts the otherwise mathematical pattern.

This is the first phase where a new player should genuinely think:

**"This is a lot of bullets."**

**Density:** Very high  
**Movement:** Slow and precise

## Attack R5 — 「Red Magic」

**Type:** Final survival/spell-card hybrid  
**Purpose:** The entire game's visual climax.

Target duration: **~30–35 seconds**

The attack escalates continuously.

### Wave 1
Large expanding crimson rings.

### Wave 2
Purple bullets interleave between the red rings.

### Wave 3
Rotating bat-wing formations are added.

### Wave 4
Slow aimed projectiles force relocation.

### Final 8–10 seconds
The game deliberately abandons plausible NES sprite limits.

Approximately **150–200 hostile bullets may exist simultaneously**, provided frame rate and readability remain stable.

The screen should look absurdly advanced for an NES while every individual element still looks authentically 8-bit.

No cheap unavoidable wall should occur.

The player survives through small, deliberate focused movements.

During the last few seconds:
- music reaches maximum intensity;
- Remilia flashes with each emitted wave;
- background becomes nearly black for bullet readability.

Defeating the spell immediately cancels the enormous field into score sparkles and gives a moment of silence before the ending.

---

# Difficulty Progression

**Cirno:** "I understand how to move now."

**Marisa:** "I actually have to pay attention."

**Sakuya:** "I need to understand what the pattern is doing."

**Remilia:** "This is legitimate bullet hell."

The game should be approximately comparable to a forgiving Touhou **Normal** difficulty, not Lunatic.

The patterns should reward deliberate movement and pattern recognition rather than twitch reflexes alone.

## Implementation Priority

If a pattern proves too computationally expensive:

1. Preserve movement geometry.
2. Preserve readability.
3. Preserve the pattern's visual identity.
4. Reduce projectile quantity.
5. Never replace a designed pattern with random bullet spam.
