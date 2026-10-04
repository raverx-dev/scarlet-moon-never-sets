# #51 correction 01 mechanical package

One corrected 192x240 production scene, plus the same background with unchanged witness assets. Original package is preserved at a9ae66e0dcf71de4b8381fd3f1abbc0c064e75b5 on v4-mi51-review-package-v1.

Use RoboPixel 79e7d2af9da8ee6b510c2bde07c762fbf877045e tools/handoff/cli.mjs package with checkpoint.json, exact source tree and read-only canonical storage. Standard package selects 37 placed environment and 5 witness pins. Run supplement.py on each output; it preserves all 41 bank members in the tile atlas/inventory, marking floor-field / floor-joint / floor-worn / lancet-ruby unplaced. Those pins remain preserved.

Packager revision: `79e7d2af9da8ee6b510c2bde07c762fbf877045e`. Source base: `175a48797d72253d90de2bf503e52a88b1fc7c65` (`v4-mi51-correction-01-input`). The canonical storage at `/home/dellis/.local/state/robopixel` was read only.

The unchanged standard command was run independently with output directories `correction01-run1` and `correction01-run2`:

```text
node /tmp/mi51-robopixel-pG6Lnd7I/repo/tools/handoff/cli.mjs package --checkpoint /tmp/mi51-package-SpvWVkA0/correction01-repo/dev/proofs/v4_mansion_resident_bank_51/checkpoint.json --storage /home/dellis/.local/state/robopixel --sources /tmp/mi51-package-SpvWVkA0/correction01-repo --output /tmp/mi51-package-SpvWVkA0/correction01-runN
python3 /tmp/mi51-package-SpvWVkA0/correction01-repo/dev/proofs/v4_mansion_resident_bank_51/supplement.py /tmp/mi51-package-SpvWVkA0/correction01-runN
```

Both supplemented outputs contain exactly 17 ordinary files and 453,144 bytes. Their file-name sets and every file byte are identical. The SHA-256 of the lexicographically ordered `SHA256  filename` manifest is `141691b892a1ebafba84827af027af60c8a55564f20e719a16770c360750e7be`. Complete per-file digests are in `mechanical_results.json`; no obsolete package file was removed.

The standard D4 package verified 42 placed pins: 37 environment and 5 unchanged witnesses. A separate read-only canonical-storage check used the same `FileRevisionRepository`, `snapshotFromRevisionState`, `renderFrame` and `hashRenderInput` path for floor-field r2, floor-joint r2, floor-worn r3 and lancet-ruby r2. All four revision, palette, dimensions and render hashes passed, giving 46/46 full-bank/witness D4 pin checks. The supplement also confirmed all 41 bank matrices against canonical readback, 41/41 selected validations PASS, 38 retained warnings, zero rose orphan warnings, 175 family-aware 8x8 tiles, 65 final 16x16 metatiles and 180/180 conforming neighborhoods.

Candidate PNG SHA-256 is `0669b7b58b238a923c53bd965afee560383401b31e58acd466ec20f02a184502`; its D3 render hash is `9f766329c5d3e1dbd7e334bced46e06ad04293aba99626b0d24c367e9ebdc700`. Readability PNG SHA-256 is `2856fa0d471c4c9d9c085f914e849c563af08576e8d2eeb8894d67f8456a5996`; its D3 render hash is `f0a269c3144435bc434ba70bf357079f1975a880541f12fa72b70962eae8139d`. There is no unresolved mechanical blocker. Owner visual review remains required; these results do not claim artistic acceptance.
