# Version 3 owner-playtest visual QA / regression audit

**DECISION: BOUNDED_CORRECTIONS_REQUIRED**

Not a new art pass. Runtime was not modified. Frozen V1/V2 were not touched. Issue #15 branding is out of scope.

| Item | Value |
|---|---|
| Audit branch | `v3-owner-playtest-qa` |
| Base | `sprite-redesign@449ad2bb677e29f6793b3f5a25ac80c0845f3e14` |
| Published main | `bc9568c47b345e38aca0acd193a5824812982aa3` |
| V3 `index.html` SHA-256 | `7ff1518457539be21130d492366e956f20e6ce8a3cb9bc463a42e3d694407f8c` |
| Published `versions/sprite-redesign/index.html` | **byte-equivalent** (same SHA-256) |
| Frozen V2 SHA-256 | `724abb7d4a34a7814b65a332ffaf13891001404e05c22c418feaba51a65e8670` |
| QA V3 | 32/32, 0 material console errors, 53 captures |
| QA V2 (comparison only) | 32/32, 53 captures |
| Governing issues | #2, #16 (read); #15 not this pass |

---

## 1. Executive summary

Version 3 is **healthy as a playable late-Famicom build**. Character sprites, portraits, HUD chrome, Hakurei shrine, Misty Lake gameplay, Forest gameplay readability, R5 dimming, Master Spark, intro, ending, title, How-To, Continue, and the coin gag are in good shape. The owner being broadly pleased matches what the capture matrix shows.

The owner’s playtest suspicions are **partly substantiated, not wholesale**:

1. **Some dialogue scenes now look like paused gameplay** — **true for combat-stage dialogues, false for intro/ending.** V2 already reused gameplay backgrounds for Cirno/Marisa/Sakuya. V2 those backgrounds **reflowed to 256**. V3 those backgrounds are **192 proofs** (plus uneven HUD-column extras). That is the actual regression.
2. **Not every dialogue** — confirmed. Intro and ending are shrine-staged and are upgrades.
3. **Character placement/spacing/sizing** — combat X is unchanged (other at 196). That slot is now the HUD column, so Sakuya is in a void and Marisa is in a tree. Scale change is the accepted native sprites (D).
4. **Mansion, especially Stage 3, looks stamped** — **true for full-width interior dialogue** (black gutter). Gameplay interior is a denser hallway, not a collapse. **Gate/roof** is the weaker Stage 3 composition: scattered props, no floor.
5. **Misty Lake is cohesive** — confirmed.
6. **Stage 2 vs 3 coherence** — Forest reads as a forest with an obvious 16×16 canopy grid. Interior hallway is busier. Roof/gate is the incoherent one.
7. **Tiles are not automatically bad** — agreed. Lake integration is the successful pattern. Forest HUD-column extension and mansion 192-clip-at-256 are the bad integrations.
8. **Unintended V2 staging loss** — yes, specifically: 256-wide interior room, gate walkway, Remilia-on-the-battlement. Do **not** roll back V3 art.

Five findings. Three P1 (must), two P2 (should). No P0.

---

## 2. Findings table

| ID | Pri | Class | Scene | V3 | V2 | Evidence | Cause | Minimal correction | Redesign? |
|---|---|---|---|---|---|---|---|---|---|
| **F01** | P1 | A | Sakuya before/after (any 256 interior) | 192 sheet + black x≥192; Sakuya at 196 in the void (94.8% near-black in the character-band gutter) | Interior painted to `w=256`; Sakuya in the room | `evidence/v3/sakuya-dialogue.png`, `sakuya-after.png`, `evidence/compare/sakuya-dialogue.png` | `MANSION.paint` clips x≥192; dialogue uses w=256 | Fill HUD column with existing right-bay tiles; move actor onto architecture (~168) | NO |
| **F02** | P1 | A | Gate, Remilia before/after, attract-sakuya, stagecard-3 | R5-empty lower center is the story floor; Reimu/Remilia float; Sakuya in the fence | Gate had a full-width walkway; Remilia dialogue stood on the battlement | `evidence/compare/gate.png`, `remilia-dialogue.png`, `attract-sakuya.png` | One roof sheet for boss readability and all roof story frames | Keep R5; on `w===256` roof frames stamp a walkway from existing cobble/approach tiles | NO |
| **F03** | P1 | B | Marisa before/after; stagecard-2; attract-marisa | Marisa + rect grimoire on the x=176 trunk; third tree column at 256 | Marisa in open sky between edge trees | `evidence/compare/marisa-dialogue.png`, `stagecard-2.png` | 192 proof extended to x≥192; actor still at 196 | Drop HUD-column forest stamps; move Marisa off the trunk | NO |
| **F04** | P2 | B | Gate / roof gameplay / Remilia frames | Oval “arch”, barcode bars, floating fence in black | Naive but complete towers + facade + walkway | `evidence/v3/gate.png`, `stage3-roof.png`, `stagecard-3.png` | 16×16 props placed on the R5-empty sheet without a connecting mass | After F02, restack arch/bars/pillars on the walkway using existing tiles | NO |
| **F05** | P2 | C | Credits floor; Cirno ice case | V3 sprites on leftover `roof(181,256)` + `iceCase()` | Same floor/case with old sprites | `evidence/compare/credits-cirno.png`, `credits-reimu.png` | Credits never switched to V3 tiles | Replace floor with existing cobble/battlement or shrine ground; ice-case may wait on #16 | NO |

Full write-ups: `FINDINGS.md`. Machine-readable: `findings.json`.

---

## 3. Dialogue / staging comparison

See `COMPARISON.md` for the full table.

**Materially changed and wrong:** Sakuya before/after (F01), Marisa before/after (F03), Remilia before/after (F02).

**Materially changed and fine:** intro, ending, attract shrine/donation/FINE, title-adjacent story.

**Policy unchanged, result changed:** Cirno before/after still use the stage sheet at 256. V3 lake fills the width and still says “Misty Lake.” Lost V2 moon/horizon. Classification **D**.

---

## 4. Environment construction

See `ENVIRONMENTS.md` for the exact IIFEs.

Short version:

| Env | Built how | Scroll? | Proof size | Runtime sheet | 256-wide story uses it? |
|---|---|---|---|---|---|
| Misty Lake | Offscreen tile stamp, once | No | 192 | 256 water; props stay in 192 | Yes (Cirno dialogue/attract/card) |
| Forest | Offscreen tile stamp, once | No | 192 | 256 + **extra** HUD-column trees | Yes (Marisa dialogue/attract/card) |
| Mansion interior | Offscreen tile_rect/place, once | No | 192 | 256 canvas, **content clipped at 192** | Yes (Sakuya dialogue) → black gutter |
| Roof/gate | Offscreen place, once | No | 192 (R5-empty center) | 256 + HUD-column extras | Yes (Remilia/gate/card/attract) |
| Shrine | Live stamps each frame | Hills only in morning birds | Authored 256 | 256 | Intro/ending/notice/arrival |

This architecture **is** the visual problem for F01–F03. Lake happened to survive it. Forest over-filled the HUD column. Mansion under-filled it. Roof used a boss-readability hole as a story floor.

---

## 5. Placement / composition review

### Misty Lake — fine

Edge reeds, lanterns, posts, ice; dark center; HUD chrome reads. 256-wide frames are extra water, not a void. Owner observation 5 confirmed.

### Forest — readable forest, two integration mistakes

Gameplay: dark path, side trunks, mushrooms, lanterns. Center lane is quiet. Master Spark dominates. Canopy grid is obvious (P3). HUD-column third trunk is F03.

### Mansion interior — hallway, not a collage collapse

Side bays have a vertical rhythm (chandelier → painting/window → sconce → banner → railing → bookcase → door). Damask is a visible 8×8 grid. Gameplay + HUD is correct. The freeze issue is **256-wide dialogue**, not “throw the interior out.”

Chandeliers sit in the side bays (x=8 and 152), not on the carpet. Pillars cap/mid/base stack. Door arches at the carpet edges. Not nonsense; just dense.

### Gate / roof — weakest environment

Moon and skyline work. Lower field is correctly empty for R5 (`r5-final.png`). Gate/dialogue/card reuse that emptiness. `gate_arch_top` does not read as an arch. Bar panels read as a grate. Meiling sleeps on a disconnected right pad. F02 + F04.

---

## 6. Suspicious but actually fine

| Surface | Why it looked suspicious | Why it is fine |
|---|---|---|
| Cirno dialogue = lake gameplay | Owner concern 1 | Same V2 policy; 256 water; still Misty Lake |
| Static (non-scrolling) fields | V2 scrolled | Intentional authored sheets; lake/forest still read |
| Title torii smaller than intro torii | Scale 1 vs 2 | Title composition; wordmark + flying Reimu carry the screen |
| Attract donation = box in void | Sparse | Same V2 beat (`architecture:false`) |
| Attract FINE | Old duplicate-Reimu bug | Single Reimu, single moon |
| How / Continue / Pause chrome | New frames | Shared `uiMenuFrame`; Continue capture is clean |
| HUD x=192 | “black gutter” during play | Authored 64×240 panel. Gutter math on play captures is the dark HUD, not a hole |
| R5 lower black | Empty | Specified; `dimField(2)` after 25s |
| Ending coin | Small | Visible in ending-dialogue and credits-reimu |
| Boot EMPTY BOX SOFT | Wrong studio | Issue #15, later |
| Lunar anchor primitive | Programmer box | Scheduled #16; floor behind it is F02 |
| Notice shrine peek | Moon/ground around the box | Intentional |
| Character scale vs V2 | Smaller than scale-2 chibis | Native V3 sprites, accepted |

---

## 7. Freeze recommendation

### MUST before Version 3 freeze

1. **F01** — Interior 256-wide gutter + Sakuya in the void.
2. **F02** — Gate / Remilia story walkway. Do not touch R5.
3. **F03** — Marisa off the trunk; stop HUD-column forest stamps.

Mechanical, existing tiles, no gameplay change, no character redraw.

### SHOULD if inexpensive

4. **F04** — Restack gate arch/bars onto the new walkway.
5. **F05** — Credits floor tiles. Ice-case may wait.

### Can wait

- Issue #15 owner mark.
- #16 small props: lunar anchor, Marisa grimoire, Cirno ice-case frame, ending coin polish.
- Forest canopy anti-repeat / mansion damask variation (P3).
- Restoring Cirno-dialogue moon/horizon (D, not required).

Do **not** freeze until F01–F03 are re-captured. Do **not** return to V2 art. Do **not** publish or merge this audit branch into gameplay.

---

## 8. Audit branch + SHA

Branch: **`v3-owner-playtest-qa`** (this commit, after the docs land).

Base SHA (untouched runtime): `449ad2bb677e29f6793b3f5a25ac80c0845f3e14`

QA-only edits on this branch: `qa/build.py` `QA_SOURCE`, `qa/agent-run.mjs` `QA_SOURCE`/`QA_OUT`/`QA_CASES`, `qa/inspection.js` `stagecard:N`, `qa/cases-owner-playtest-extra.json`, `qa/README.md` env notes, `qa/audits/v3-owner-playtest/**`.

Reproduce:

```bash
cd qa && npm install
npm run agent:no-captures
npm run agent
QA_CASES=./cases-owner-playtest-extra.json QA_OUT=/tmp/v3-extra npm run agent
QA_SOURCE=/path/to/v2/index.html \
  QA_CASES=../qa/audits/v3-owner-playtest/cases-combined.json \
  QA_OUT=/tmp/v2-out npm run agent
python3 qa/audits/v3-owner-playtest/analyze_frames.py
```
