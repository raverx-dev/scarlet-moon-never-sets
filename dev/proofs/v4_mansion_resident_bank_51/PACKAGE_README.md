# #51 mechanical review package

This package is a review proof for one 192×240 Mansion background. `package/` contains the eight standard RoboPixel Production Handoff v1 files and nine Scarlet-local supplements. `candidate_native.png` is the production background. `readability_native.png` places unchanged #45 actors and bullets over the same background for static inspection. No second environment, story, runtime, approval, or delivery is implied. Owner visual review is required.

## Authority and provenance

- Artist base: `39177310c7c3e82aff41033e4404f07d82137980` (`v4-mi51-resident-bank-v1`), original base `58b06036c1bd102099e0598bf755420c0d71265f`.
- Packager: RoboPixel `79e7d2af9da8ee6b510c2bde07c762fbf877045e`, `tools/handoff/cli.mjs package`; canonical storage read only at `/home/dellis/.local/state/robopixel`.
- `checkpoint.json` is strict `robopixel.production-handoff/v1`; `package/verification.json` is the standard D4 verification. `package/supplement_verification.json` is separate.
- Direct Git materialization of exact comparison PNG bytes: V3 construction `ea4c31aa8d2ad92e1a5d8bfb0f25d1ba0863ed31:dev/art/v3_stage3a_mansion/mansion_composition_proof_192x240.png` SHA-256 `81a3632bea2e534082358b0da284e62c59ff3696e5138daefe6ed151137c9d90`; accepted #22 hierarchy `c2241001946ac5456293f9f2b8be137e5c5bc648:dev/proofs/v4_mansion_translation_01/mansion_gameplay_preview_192x240.png` SHA-256 `4c01e4ec1c385e29bba28a6fc7c12a91600e086a84fdb71f3d4be6738d317fb3`; #45 minimum mechanical proof `4e93c4685c6909b38233ee854036a8308db6aead:dev/proofs/v4_late_cartridge_45/review-package/background_only.png` SHA-256 `fb3b87e36ddd82bc5eb9ac9d19d64538e98d25084eee09a96c10cc3f1d80ea78`. All three are 192×240 and source-hashed by the handoff tool.

## Mechanical results

- All 41 selected environment assets plus five unchanged witness assets matched canonical D4 revision, palette and D3 render pins; every asset is placed. The unused runner-edge is excluded.
- Candidate render hash: `63e7a362cedd179868ffad29483fd7545b984eabd0e12c5f898b25fdfa383136`; readability render hash: `126d5c014a7fe19d4ec6dd2cf23cc6c5d188fbd0779ece028bd79b582fe6a4d3`.
- 13 visible background colors, four background subpalettes, all 180 final 16×16 neighborhoods conform. The exact 8×8 decomposition yields 196 deduplicated family-aware tiles. The exact final scene construction uses 92 distinct 16×16 metatiles; reconstruction is byte exact.
- The quiet lane is x64..127, y128..239: 7,168 pixels, three RGBA colors in the candidate; unchanged witness placement changes 390 pixels there in the static readability view.
- All 41 selected validations PASS. The 58 retained orphan warnings are nonblocking. No waiver or approval was applied. Wall-field and floor-field are pixel-equivalent but separate material identities; this is a soft diagnostic.
- Two independent package and supplement runs produced all 17 output files byte for byte identical (549,896 bytes total). The standard eight files total 447,782 bytes. Both package runs used the exact committed checkpoint and canonical storage. No asset PNG copies or Base64 are included.

`package/comparison_four_pane.png` labels the four distinct evidence roles in chronological order. `package/candidate_nn3x.png` uses nearest-neighbor enlargement. `package/tiles_8x8.png`, `package/tile_manifest.json`, `package/metatiles_16x16.png`, and `package/construction_map.json` document reconstruction. `package/quiet_lane_mask.png`, `package/bank_inventory.json`, and `package/supplement_verification.json` document the other local checks. The standard `review.html` and `verification.json` remain unchanged.
