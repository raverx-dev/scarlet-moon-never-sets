# V3 final visual audit — evidence notes

Baseline: `449ad2bb677e29f6793b3f5a25ac80c0845f3e14`  
Tested `index.html` SHA-256: `7ff1518457539be21130d492366e956f20e6ce8a3cb9bc463a42e3d694407f8c`  
44-capture `generatedAt`: `2026-09-09T20:11:20.222Z`  
Harness: existing `qa/` only. `qa/output/` remains local and is not committed.  
Canonical 44-capture agent report retained at `audit/v3-final/evidence/agent-report-44.json`.  
File checksums: `audit/v3-final/evidence/SHA256SUMS.txt`.

## Commands

```text
cd qa && npm run agent:no-captures
cd qa && npm run agent
cd qa && node agent-run.mjs --case=continue
cd qa && node agent-run.mjs --case=dawn-anchor
```

The two extra `--case` runs used the existing inspector scenes (`continue`, `dawn`) after a temporary `qa/cases.json` addition that was reverted and not committed.

## 44-capture matrix

All ids from `qa/cases.json` were generated and inspected:

`boot`, `notice`, `title`, `how`, `attract-donation`, `attract-fine`, `attract-cirno`, `attract-marisa`, `attract-sakuya`, `attract-eyes`, `intro`, `stage1`, `cirno-dialogue`, `c1`, `c2`, `c3-frozen`, `stage2`, `marisa-dialogue`, `m1`, `m2`, `m3-active`, `m4-active`, `gate`, `stage3-interior`, `stage3-roof`, `sakuya-dialogue`, `s1`, `s2-frozen`, `remilia-dialogue`, `r1`, `r2`, `r3-spear`, `r4`, `r5-final`, `dawn`, `ending-arrival`, `ending-dialogue`, `credits-cirno`, `credits-marisa`, `credits-meiling`, `credits-sakuya`, `credits-remilia`, `credits-reimu`, `final-card`

## Extra captures

| Id | Scene | Tick | Why |
|---|---|---:|---|
| continue | continue | 30 | Pause/how/continue chrome family; Continue overlay |
| dawn-anchor | dawn | 90 | Lunar-anchor beat; standard `dawn` case is tick 280 (moonset) |

Pause is `uiMenuFrame(34,86,124,64)` over play. Not a separate inspector state. How + Continue cover that frame language.

## Promoted stills

Selected stills that support a finding or a required pass check live in `audit/v3-final/evidence/`. They are copies of harness PNGs, not redraws.

| File | Supports |
|---|---|
| `boot.png` | #15 EMPTY BOX SOFT still on splash |
| `title.png` | Shrine/title/moon/wordmark integration |
| `how.png` | Authored menu frame |
| `continue.png` | Continue overlay + same frame family as pause |
| `stage1.png` | Misty Lake edge-weighted readability |
| `stage2.png` | Forest center-lane readability |
| `stage3-interior.png` | Mansion interior readability |
| `stage3-roof.png` | Roof composition, lower field subdued |
| `gate.png` | Gate architecture; Meiling on approach stone |
| `r5-final.png` | R5 lower-field blackout |
| `sakuya-dialogue.png` | Full-width interior leaves x≥192 black |
| `marisa-dialogue.png` | Procedural grimoire rects |
| `dawn-anchor.png` | Procedural lunar anchor |
| `ending-dialogue.png` | Procedural coin; morning shrine |
| `credits-cirno.png` | #15 staff placeholder + procedural ice case |

## Mechanical comparisons (not images)

- UI 20, shrine 51, lake 26, forest 34, mansion 35, roof 44 matrices match their packages with 0 pixel diffs.
- `SPRITES` vs `69d0676`: 0 changed lines.
- Frozen V1/V2 blobs on `origin/main` match `14acbe3`.

## Checksums

See `evidence/SHA256SUMS.txt`. The retained 44-capture report SHA-256 is:

`1c62a56ede3aff761f2d12068518fd34ada4cfd6d16d54071d0f5368e0464238  agent-report-44.json`
