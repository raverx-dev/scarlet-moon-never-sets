# Version 3 final integrated visual acceptance audit

Status: **PASS**  
Audit scope: mechanical/visual verification of the completed UI, shrine/title, Misty Lake, Forest of Magic, mansion interior, and gate/roof integrations. No art invented. No runtime or gameplay change.  
Baseline: `v3-stage3b-roof-integration@449ad2bb677e29f6793b3f5a25ac80c0845f3e14`  
Audit branch: `v3-final-visual-audit`  
Governing issues: #2, #15, #16  
Work run: `ab07211c-f111-4deb-966f-affbd16384e7`

Tested `index.html` SHA-256: `7ff1518457539be21130d492366e956f20e6ce8a3cb9bc463a42e3d694407f8c`

This audit does **not** freeze Version 3 and does **not** publish `main` or `versions/`.

---

## Verdict

**PASS.** Families A–E are integrated from the accepted exact matrices, the recovered regression suite is green, playfield readability holds, R5 lower-field suppression holds, character sprites are unchanged from the accepted Version 3 character checkpoint, and frozen Version 1 / Version 2 snapshots were not modified.

**Concrete blockers: none.**

Remaining items below are scheduled or leftover primitive surfaces. They are not defects in the accepted A–E packages and are not mechanical regressions of already-accepted behavior. Issue #15 still needs an owner display-name decision before implementation. Issue #16 small props still need authored art.

---

## QA

| Run | Result |
|---|---|
| `cd qa && npm run agent:no-captures` | **32 passed / 0 failed**, 0 material console/page errors |
| `cd qa && npm run agent` | **32 passed / 0 failed**, **44/44** captures, 0 material console/page errors |
| Extra harness captures | `continue` @ tick 30; `dawn-anchor` (`dawn` @ tick 90) |

Browser: `/usr/lib64/chromium-browser/chromium-browser`  
44-capture report timestamp: `2026-09-09T20:11:20.222Z`  
Local report: `qa/output/agent-report.json` (not committed)  
Durable 44-capture report: `audit/v3-final/evidence/agent-report-44.json`  
Durable summary: `audit/v3-final/evidence/qa-summary.json`  
Red Magic diagnostic: `r5Density.maxAllocated = 194` (matches the established density target)

Pause is not a separate inspector state. It uses the same `uiMenuFrame` chrome as How To Play and Continue (`uiMenuFrame(34,86,124,64)` over play). How and Continue captures stand in for that family.

---

## Exact accepted assets

Runtime RAW / reconstructed matrices were compared byte-for-byte to the committed art packages on this tree.

| Family | Package | Runtime match |
|---|---|---|
| Global UI chrome | `art/v3/ui/ui_assets.js` | **20/20**, 0 pixel diffs |
| Hakurei shrine / title | `dev/art/v3_shrine_title/v3_shrine_title_assets.js` | **51/51**, 0 pixel diffs |
| Stage 1 Misty Lake | `dev/art/v3_stage1_misty_lake/lake_stage1_assets.js` | **26/26**, 0 pixel diffs |
| Stage 2 Forest of Magic | `dev/art/v3_stage2_forest/forest_stage2_assets.js` | **34/34**, 0 pixel diffs |
| Stage 3A mansion interior | `dev/art/v3_stage3a_mansion/mansion_assets.js` | **35/35**, 0 pixel diffs |
| Stage 3B gate / roof | `dev/art/v3_stage3b_roof/*.json` | **44/44**, 0 pixel diffs |
| Character / portrait `SPRITES` | `sprite-redesign@69d06766c0a6c165f26f71ded96d7b5bd8a122df` | **0 changed lines** |

`roof_scarlet_moon_64` remains the shrine `moon_scarlet_64` carry-forward. No palette extension. No Grok redraw.

---

## Native / integer scaling

| Check | Result |
|---|---|
| Logical canvas | 256×240; playfield 192×240; HUD 64×240 at x≥192 |
| Canvas CSS | `image-rendering: pixelated`; `k = s>=1 ? Math.floor(s) : s` |
| 2D context | `imageSmoothingEnabled = false` |
| Sprite blit | `s = Math.max(1, s\|0)`; integer `fillRect` cells |
| Environment sheets | offscreen 256×240, 1×1 stamps, `drawImage` with integer extents |
| UI / shrine stamps | `stamp` / `stampSlice` at 1 logical pixel |

Integer (not fractional) 2× uses that the packages or prior character acceptance already allow:

- `stampScale(shrine_torii_*, …, 2)` and lanterns in `shrine()` — shrine composition QA explicitly allows integer scale of the 64×56 torii
- `stampScale(title_touhou_kougetsuya, …, 2)` — 96×20 matrix → 192×40 title wordmark
- `sprite('meilingSleep', …, 2)` — accepted 24×16 character matrix
- title `yinyang` blit at scale 2 — pre-existing character/title accessory

No fractional sprite magnification and no downsampling of authored matrices were found.

---

## Stage readability and R5

| Surface | Finding |
|---|---|
| Stage 1 / Cirno | Dark water; reeds, posts, lanterns, ice on the edges; center lane quieter than the columns. Ice bullets read against the water. Boss `dimField` checkerboard keeps diamonds readable. |
| Stage 2 / Marisa | Dense canopy/trunks/mushrooms/lanterns on the sides; dark path down the middle. Master Spark and star bullets dominate the lane. |
| Stage 3A / Sakuya | Damask/pillars/windows/chandeliers on the sides; dark carpet corridor in the center. Knives remain readable, including under TIME STOP. |
| Stage 3B / Remilia r1–r4 | Moon and architecture in the upper/side silhouette; existing boss dimming; Gungnir telegraph readable. |
| Remilia R5 | `dimField(level=2)` fills `rect(0,80,w,160,C.black)` after 25s. Capture `r5-final` shows moon/skyline only in the upper band; lower playfield is empty black; Remilia and Reimu stay readable. |

HUD chrome stays in x=192..255 during play.

---

## Frozen Version 1 / Version 2

This branch has no `versions/` tree. `git log 69d0676..449ad2b -- versions/` is empty.

On `origin/main`, the frozen blobs are unchanged from the publish commit `14acbe325eea1d9f635d6ef78bcbd061b482a88b`:

| Snapshot | Blob |
|---|---|
| `versions/original/index.html` (V1) | `2f0dc1b9b598e0704e48bc49d86048e98b0bceb0` |
| `versions/p1-visual-audio/index.html` (V2) | `6b0247d45ded61d233b7831f790d35239d3d6b93` |

Not modified. Not published. Not merged.

---

## Remaining non-blocking work

These do **not** fail A–E integration. They are the leftover items this audit was asked to name.

### Issue #15 — owner attribution (owner-gated)

Still present:

- Boot splash: `EMPTY BOX SOFT` / `PRESENTS` (`index.html` boot branch)
- Credits staff beat: `A TINY LOST CARTRIDGE` / `NEW CODE AND PIXEL ART`
- `FANWORK_NOTICE.md` still describes “Empty Box Soft” as a fictional developer mark

ZUN / Team Shanghai Alice and unofficial-fan-work lines remain on notice, title, credits, and final card. Issue #15 requires an owner-chosen display name before implementation. This audit did not change branding.

### Issue #16 — small props (need authored art)

Still primitive geometry, as scheduled “after A–E”:

| Prop | Current draw | Capture |
|---|---|---|
| Lunar anchor | `nesBox` + disk + line | `dawn-anchor` (dawn @ 90) |
| Marisa grimoire | three `rect`s | `marisa-dialogue` |
| Ending coin | `coin()` disks | `ending-dialogue`, `credits-reimu` |
| Cirno ice-case frame | `iceCase()` cyan box | `credits-cirno` |

Do not invent replacements in the Grok lane.

### Leftover primitive presentation (not in A–E packages)

- Attract captions still use `nesBox` rather than the authored dialogue/menu frame (`attract-donation`, `attract-fine`).
- Stage 3A sheet composition is the accepted 192×240 playfield. Full-width interior dialogue (`sakuya-dialogue`) therefore shows a black column at x≥192, where lake/forest/roof sheets were tiled to 256. Play HUD covers that column. Follow-up would be mechanical tiling of existing mansion tiles, not new art.
- Credits floor still uses the old procedural `roof(181,256)` crenellation.
- Dawn moonset / ending morning sky bands remain `rect` stripes; morning shrine architecture tiles are in use.
- Dead stroke `logo()` remains in source and is unused by `drawTitle()`.

---

## Issue mapping

| Item | After this audit |
|---|---|
| SPEC-003 / 004 / 005 (characters) | Unchanged. KEEP. |
| SPEC-007 HUD chrome | Integrated. Exact UI matrices in use. |
| SPEC-006 shrine / title / moon / wordmark | Integrated. |
| SPEC-002 stage environments | Integrated for Misty Lake, Forest, mansion interior, gate/roof. |
| SPEC-001 remaining language | A–E raise the floor to the authored tile families. Leftover primitives are listed above. |
| Issue #15 | Open. Owner-gated. |
| Issue #16 small props | Open. Need ChatGPT art, then a later mechanical pass. |
| P0 bugs / Audio P1 / regression | Out of scope as new work; QA remains green. |

---

## What this audit did not do

- No art creation, redraw, simplification, or reinterpretation
- No gameplay / collision / audio / dialogue-text / scoring / boss-logic change
- No merge to `main`
- No publish of `versions/*`
- No Version 3 freeze
