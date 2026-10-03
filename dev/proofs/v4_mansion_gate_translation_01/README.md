# Mansion Gate Translation 01 — completed recovery package

**Exact canonical-to-composition correspondence: PASS for both scenes, zero differing RGBA pixels.**

Continuation of draft PR #29, branch `v4-mansion-gate-recovery-20260924`, from preserved checkpoint `7a0c906b423f5a794eea8d8668246798a6d58453`. Governing plan: [#24](https://github.com/raverx-dev/scarlet-moon-never-sets/issues/24). Mechanical reconstruction only; no new artwork, canonical asset mutations, runtime integration, merge or deployment.

## Review

Open [review.html](review.html) with this directory intact. All links are relative; no external resources are needed.

| Scene | Recovered original | Derived native | Canonical recomposition | Difference mask |
| --- | --- | --- | --- | --- |
| Gameplay | [576×720](gate_gameplay_3x.png) | [192×240](gate_gameplay_native.png) | [192×240](gate_gameplay_recomposed.png) | [Zero differences](gate_gameplay_mismatch.png) |
| Story/dialogue | [768×720](gate_story_3x.png) | [256×240](gate_story_native.png) | [256×240](gate_story_recomposed.png) | [Zero differences](gate_story_mismatch.png) |

- [Canonical asset atlas](gate_asset_atlas.png): all 14 revision-2 assets at 1×, labeled; presentation background and labels are atlas-only.
- [Asset manifest](asset_manifest.json): canonical identities, revision/render hashes, dimensions and exact downloaded PNG SHA-256 hashes.
- [Reconstructed layouts](layouts.json): 27 gameplay and 28 story placements, ordered back-to-front.
- [Compositor and verifier](compose.py).
- [Validation artifact](validation.json): inventory, usage counts, dimensions, raster hashes and exact comparison results.

## A. Verified recovered evidence — unchanged originals

These two Owner-supplied composed PNGs were recovered from an interrupted Astra Work session and preserved in PR #29. They are controlling visual evidence, not generated references or live captures.

| Original | Bytes | SHA-256 |
| --- | --- | --- |
| `gate_gameplay_3x.png` | 24515 | `6e5c9e62c47ab47777c9530089ce8a65ede34df733a973a571b8575eeac9e7a9` |
| `gate_story_3x.png` | 31805 | `b6151fd7ccf91357dbf2cbcb9600c4760db57619bbd60b3327caaabf49af49cb` |

Original bytes are unchanged. Native previews are **new recovery derivatives**, obtained by taking one pixel from each exact uniform 3×3 block. A full RGBA comparison proves their nearest-neighbor 3× enlargement matches the originals: 0 differing pixels in both scenes. They are not represented as recovered original native files.

## B. Canonical assets and reconstructed composition

Read-only RoboPixel project inventory reconfirmed all 14 assets at revision 2. `asset_view` was called with explicit revision 2, scale 1 and default frame. The exact returned PNG bytes are preserved in `assets/`. No approval, delivery or canonical mutation was performed.

| `v4-mansion-gate-trans01-arcade-bridge` | 2 | 77×48 | `a6bef77abba733356b955190139418b9a0251b8cab6c9d2c52cbe352076fe511` |
| `v4-mansion-gate-trans01-banner-pier` | 2 | 33×142 | `0b039bcf7f95d9ac0cd1feb7ac81bae7561aed1e0dc61a6356752e19a7a60818` |
| `v4-mansion-gate-trans01-closed-gate` | 2 | 106×104 | `23bad0deec3b1607fa7a2ff49ddd8c52c0fe155ff1f4b62e8674a127a5cdf816` |
| `v4-mansion-gate-trans01-cloud-bank` | 2 | 106×25 | `c912ed876dd1bdcfac310b07cb036db51925ff8e191f82c13705349fc364f26e` |
| `v4-mansion-gate-trans01-crimson-vine` | 2 | 40×76 | `7995c448c5784ffd10ebfab8112899e7797c63b7037ea4534ef3a8126433146a` |
| `v4-mansion-gate-trans01-cypress` | 2 | 29×89 | `604e2e18b4fb1f5f6dd54fcc590167958857d2c78280b8a015396eed12b6422d` |
| `v4-mansion-gate-trans01-garden-stair` | 2 | 46×49 | `4a08a8e5bc5817910c1ec2587cc89769099f8167f8cf210bb8f3adeba6ea2b3b` |
| `v4-mansion-gate-trans01-gargoyle` | 2 | 27×27 | `ff9e29cc62f80580b0ea83161dd4220db91b4bf7145b2dc3bf469fa6879d75ab` |
| `v4-mansion-gate-trans01-lantern` | 2 | 10×19 | `92d66f27b0f025d54c4a10b410ca5215dec58806b8da3c19e06f974ae32652d0` |
| `v4-mansion-gate-trans01-low-fence` | 2 | 67×48 | `59e63debdc8249fabb37bdd73d1c49d1d27cfb0cdbd937dbd0d0d93b881376d8` |
| `v4-mansion-gate-trans01-mansion-facade` | 2 | 136×102 | `fb95a77c9c053293e2c7024b3c1f0f325dabcd71da871062d8469461695821b2` |
| `v4-mansion-gate-trans01-moon` | 2 | 37×37 | `f0048021d8ff1d4982b20bbbc3785ce7063fc0cf28b770506b4a0da60a86e075` |
| `v4-mansion-gate-trans01-open-gate-wing` | 2 | 24×136 | `973818c1a4843651fe554256de44874f1026d14891a4a6bf3bd2e53e400c5d53` |
| `v4-mansion-gate-trans01-perspective-paving` | 2 | 256×152 | `5d66b3db6618c4222ea1d108189279ce20544689761bad190fca8c3fe40b8e84` |

`layouts.json` is **newly reconstructed source**, not recovered original source. Placements were recovered by exact pixel template matching against the native derivatives, followed by checking translation, horizontal mirroring, clipping and layer order. The result uses only canonical PNGs, integer placements, optional horizontal flip, normal alpha compositing and a uniform RGBA background `[23,30,56,255]` observed in the recovered scenes. No masks, residual patches, recoloring, scene-image overlays, resizing of assets or generated pixels were used to force correspondence. Output clipping at canvas boundaries is intentional.

The compositor builds scenes independently from the canonical asset renders and layouts. Original scenes are used only for recovery and verification, never composited into the canonical output. All 14 assets are used across the two layouts. Pixel identity does not establish that this is the unique or historically original layout; fully occluded placements cannot be recovered uniquely.

## C. Historical limitations

The crashed session reportedly had original native previews, an atlas, layout source and validation files locally. Those original files remain unrecovered and that historical statement remains unverified. This package supplies **new deterministic replacements** for those missing artifacts and explicitly verifies their visual correspondence. It does not claim to have recovered the crashed workspace.

## D. Verification performed in this completion session

- PR #29 remained open/draft at the expected checkpoint; same branch retained.
- All 14 canonical assets were read at revision 2 and their dimensions/identities recorded.
- Both original SHA-256 hashes remained unchanged.
- Native → nearest-neighbor 3× original comparison: **0 differing RGBA pixels**, both scenes.
- Canonical composition → native comparison: **0 differing RGBA pixels**, both scenes.
- Canonical composition → recovered 3× original comparison: **0 differing RGBA pixels**, both scenes.
- `python compose.py` and `python compose.py --check`: **PASS**. Check mode performs no writes, checks original and asset byte hashes, rebuilds the compositions/atlas in memory, compares every committed image output and verifies the validation record.

Reproduce locally with Python 3, Pillow and NumPy:

```sh
python compose.py --check
```

To regenerate derived outputs and validation, run `python compose.py`. Originals and canonical render files are never written by the script. Mismatch images use black for equal pixels and pink for differences; current masks are all black.

No mechanical recovery blocker remains. This proof does **not** claim full art validation, live in-game readability, runtime integration, formal asset approval or final artistic acceptance. V1–V3, `versions/v4/index.html`, main, interior PR #22 and Forest PR #26 are untouched. Stop for Owner review.
