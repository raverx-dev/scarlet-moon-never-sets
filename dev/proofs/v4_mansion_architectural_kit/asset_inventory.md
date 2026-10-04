# Asset inventory

Project: `scarlet-moon-never-sets`. All are **unapproved preview candidates**.

Every asset uses palette `v4-mansion-kit-proof-01`, frame `default`, layer `art`. No additional RoboPixel project, code branch or asset approval was created.

| Asset ID | Revision | Native size | Reuse |
|---|---:|---|---|
| `v4-mansion-proof-window-bay-01` | 3 | 32×64 | Complete 32×64 pointed twin-lancet bay; four game placements and two story placements, always 1×. |
| `v4-mansion-proof-wall-panel-01` | 3 | 16×16 | 16×16 inset wainscot panel; restricted to selected bands under windows. |
| `v4-mansion-proof-column-01` | 3 | 16×64 | 16×64 source; cap rows 0–11, shaft crop rows 12–27, base rows 52–63. Variable-height construction uses repetition, not scaling. |
| `v4-mansion-proof-floor-01` | 4 | 32×16 | 32×16 diamond paving segment with restrained seams and stone marks; repeats beside carpet. |
| `v4-mansion-proof-carpet-field-01` | 3 | 16×16 | 16×16 low-contrast pile; central runner fill. |
| `v4-mansion-proof-carpet-border-01` | 3 | 16×32 | 16×32 left border widening by 4 pixels per segment; horizontal mirror supplies right border. |
| `v4-mansion-proof-trim-side-01` | 3 | 8×16 | 8×16 vertical edge trim; reusable reflection at side boundary. |
| `v4-mansion-proof-trim-top-01` | 3 | 16×8 | 16×8 dentil/cornice strip; top boundary and dais/threshold edges. |
| `v4-mansion-proof-rose-apse-01` | 4 | 48×64 | 48×64 focal panel: small rose window, stone surround and lower niche; shared full asset in both scenes. |
| `v4-mansion-proof-wall-masonry-01` | 2 | 32×16 | 32×16 quiet cut-stone infill; shared upper-wall/shadow support. |

## Exact revisions

| Asset | Revision hash |
|---|---|
| window-bay | `728d687127e2ddc8ae6938ee5c8b74f40ce0f6df0b4fe01a990a78be5cba047d` |
| wall-panel | `10c31697ac6a716fec2adc86af9d4b4c21c0f1b223c10b3b8673eab3bb7e1820` |
| column | `32b38f38f16c8deb716dfb79420d92cb52688a2a801fbb8a7e38218e6d0942a7` |
| floor | `e2978708cc49db568511dbff6692a52517b862634fdb66befa16088f25034cd3` |
| carpet-field | `1c4894a5369c9acaab528ec9d8c265a74068b9ed2189e597aa36de5e9164ef63` |
| carpet-border | `121641ccad16b2cf4b1573f21cc833cc9585a20dc164c476252bf34093120738` |
| trim-side | `78843e6eedd30e67c59ed73b451edb71a8abfa184f0a9bec2861b47394e9d966` |
| trim-top | `9a1bad091af4ad029928d9bf36963a2476a8d589e47a34dde8f8f4104d1565cf` |
| rose-apse | `744aeb00758441dc9a1d2efbba79bce37786eebf3b8429a3f841a42da2e05e43` |
| wall-masonry | `c7a7b82bb2ee25730e1fe092e52d2b9f59c9668c9f68087678d36ec58fd8564d` |

Canonical PNGs are in `canonical_previews/`; preview-export matrices in `exports/`. The full manifest records render hashes and exact approval-status evidence. `layouts.json` is the auditable reuse map.

The shared palette contains transparency plus 13 opaque colors. These are Famicom-inspired color/pixel choices, not a claim of NES per-tile hardware compliance.

The initial nine-piece checkpoint is preserved in Git history; only the final manifest is the current proof selection.
