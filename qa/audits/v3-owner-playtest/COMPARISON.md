# Dialogue / staging comparison

`drawDialogue()` is the same *policy* in V2 and V3:

```
background(stage, frame, 256, sceneKind || intro→shrine || ending→morning || '')
```

Combat dialogues do **not** have a unique story background. They reuse the current stage sheet at 256×240. Intro and ending use the shrine. Remilia passes `sceneKind='roof'`.

What changed is **how those sheets are built**, not the call.

## Coordinates (combat / story)

| Scene | V2 | V3 |
|---|---|---|
| Intro Reimu | `sprite('reimu', 70, 138, 2)` | `storyReimu(70, 146)` scale 1 |
| Combat Reimu | `sprite('reimu', 56, 116, 2)` | `storyReimu(56, 124)` |
| Combat other | `sprite(other, 196, 108, 2)` | `sprite(other, 196, 108, 1)` |
| Ending Reimu | `(64, 128, 2)` | `storyReimu(64, 136)` |
| Ending Remilia | `(168, 124, 2)` | `(168, 124, 1)` |
| Gate Reimu y | `168 - t*.4` | `176 - t*.4` |
| Gate Meiling | `(204, 186, 2)` | `meilingSleep(204, 186, 2)` |
| Dialogue frame | `nesBox(4, 174, 248, 62)` | `stamp(UI.ui_dialogue_frame, 4, 174)` |
| Portrait | scaled field sprite in a box | native portrait in `ui_portrait_bezel` |

X of the opposing combat actor is **unchanged at 196**. That slot was the right side of a 256-wide *procedural* V2 scene. On V3 192-composed sheets it is the HUD column.

Reimu Y is +8 for native 24×32 story sprites. Intro/ending still sit on shrine dirt. Combat Y has no floor except F02 scenes.

## Scene-by-scene

| ID | Materially changed? | Verdict |
|---|---|---|
| **intro** | Yes — new shrine, story Reimu, portraits, dialogue chrome | **D — fine.** Better staged than V2. Reimu in the torii. |
| **cirno_before / cirno_after** | Yes — V2 had moon + horizon + edge reeds on a 256 landscape; V3 is the all-water 192 playfield sheet extended with extra water | **D.** Still reads as Misty Lake. Looks more like paused gameplay (owner concern 1, this scene only). Not a freeze defect. ⑨ overlay still works. |
| **marisa_before / marisa_after** | Yes — extra tree column; Marisa + rect grimoire on the x=176 trunk | **F03.** V2 had her in open sky. |
| **sakuya_before / sakuya_after** | Yes — 192 architecture + black gutter; Sakuya in the void | **F01.** V2 had her inside the room. |
| **remilia_before / remilia_after** | Yes — no walkway; actors in the R5-empty lower field / railing | **F02.** V2 stood both on the battlement over a facade. |
| **ending** | Yes — morning shrine, story sprites, V3 donation box | **D — fine.** Coin gag still readable. Staged, not paused gameplay. |
| **attract shrine / donation / FINE** | Art upgrade; same beats | **D — fine.** FINE no longer duplicates Reimu/moon (BUG-002 still closed). |
| **attract-cirno** | Lake sheet at 256 | **D.** Same as Cirno dialogue policy. |
| **attract-marisa** | Forest sheet at 256 with third trunk | **F03** (same 256 extension). Marisa herself is in the path; less bad than dialogue. |
| **attract-sakuya** | V3 *adds* Sakuya on the roof sheet; she stands in the fence | **F02.** V2 showed roof only. |
| **gate** | Lost V2 full-width ground overlay | **F02.** |
| **stagecard 1** | Lake at 256 | **D.** |
| **stagecard 2** | Forest at 256, two right trunks | **F03.** |
| **stagecard 3** | Roof sheet, empty lower field | **F02 / F04.** |

## What owner concern 1 actually is

Not “dialogue started using gameplay backgrounds.” V2 already did that for Cirno / Marisa / Sakuya.

The regression is: **V2 gameplay backgrounds were functions of `w`, so 256-wide dialogue got a 256-wide scene. V3 gameplay backgrounds are 192 proofs (plus uneven HUD-column extras), so 256-wide dialogue is cropped playfield + gutter or leftover HUD forest.**

Intro and ending were never on that path (`sceneKind` shrine/morning). They are not affected.
