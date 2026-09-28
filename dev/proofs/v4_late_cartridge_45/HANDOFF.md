# LOCAL PACKAGING HANDOFF READY

Scarlet Moon #45 only. Artist-side handoff, not packaged/published/approved.

## Selected state

Project: `scarlet-moon-never-sets`.

36 `v4-lc45-*` canonical assets survive at r2. Exactly 35 are selected by checkpoint.json; all 35 revision hashes were rechecked against the live RoboPixel project during recovery. The superseded `v4-lc45-bat` r2 is excluded; use `v4-lc45-bat-familiar` r2 (11×7). No asset was recreated during recovery.

`checkpoint.json` is the complete strict `robopixel.production-handoff/v1` input: exact IDs, selected revisions, revision/palette/render hashes, frame IDs/dimensions, 193 ordered neutral placements, 195 ordered fire placements, source hashes and provenance. `asset_inventory.csv` provides the same selected identities plus exact export hashes in a compact table.

Exactly two scenes, each 256×240 with 192×240 gameplay + 64×240 sidebar:

- neutral RGBA render hash: `43f2634d14403f303e580d4a09bf752587c0453652689ae0e1e347d6ff1ca286`
- fire RGBA render hash: `fa9af5e2a0ba920afcbaa1b2b83c4a12f61184498871e5a7e0b0a9ac4db77221`

These are D3 hashes (domain `robopixel-render-v1\0`, uint32 big-endian width/height, RGBA bytes), not predicted package PNG byte hashes.

## Transfer and source root

The archive contains an `overlay/` directory. Copy its `dev/proofs/v4_late_cartridge_45/` directory into a fresh isolated Scarlet checkout at:

`e2891954abfb4505283898eea098fb9db4f822c4`

Do not edit `versions/v4/index.html` or `versions/sprite-redesign/index.html`. Their required SHA-256s:

- V4: `11cf1b906aca600096827f15795ee6282547a7bb161567b868037028bc08d3a4`
- V3: `7c224ab6fd0e6bb0153a7f279af61e4332a2ad4228d60404f26351800e75d7d4`

`source_inventory.json` enumerates every required base file and supplied comparison/evidence file with hashes. All four native comparison PNGs are supplied under inputs/. They are source-rendered static inspection states, not live browser captures. Source/raster adapter code is supplied for reproduction. The exact source commit and referenced approved design/PR provenance are in evidence.md.

`artist-review/` at archive root is a convenience preview generated from canonical readbacks. It is NOT the future local D4 package and should not substitute for handoff:package. Open its `lc45-review.html` for native-first inspection.

## Required local steps — not executed by Work

Use the existing RoboPixel toolchain at exact commit:
`0a959d357bf4d26ff321509d7064b7c920cdf92c`.

Supply absolute paths below; these are placeholders, not literal filesystem values:

```sh
# From the qualified RoboPixel checkout:
npm run handoff:package -- \
  --checkpoint "$SCARLET_CHECKOUT/dev/proofs/v4_late_cartridge_45/checkpoint.json" \
  --storage /home/dellis/.local/state/robopixel \
  --sources "$SCARLET_CHECKOUT" \
  --output "$SCARLET_CHECKOUT/dev/proofs/v4_late_cartridge_45/review-package"

# Python 3 + Pillow; supplements and verifies the real package:
python3 "$SCARLET_CHECKOUT/dev/proofs/v4_late_cartridge_45/supplement.py" \
  --package "$SCARLET_CHECKOUT/dev/proofs/v4_late_cartridge_45/review-package"
```

The output directory must initially be absent. Fail closed on any source, revision, palette, export or scene mismatch. Do not repin to newer revisions or reconstruct art. If Pillow is unavailable, install it in an isolated environment; no application changes are needed.

The standard eight files alone do NOT satisfy #45. The mandatory supplement adds native-first `lc45-review.html`, explicit 3× NN PNGs, 8×8 vocabulary/atlas, 16×16 assembly map, Reimu cell/state/edge evidence, background-only witness, global-palette evidence and additional verification. It verifies the actual local package's native pixels and preserves its verification.json unchanged.

Standard comparator slots are deliberately assigned `current_source=V3` and `reference_source=current V4` to produce V3 → current V4 → Late-Cartridge. Both source PNGs are native size. Standard review.html has generic misleading labels and starts enlarged; use the supplement's `lc45-review.html` as the #45 review entry point.

After both steps pass, publish the proof directory through the qualified handoff:publish path from an isolated branch. Suggested new branch: `v4-late-cartridge-proof-45` (not created by Work). Respect publisher's exact base, current-branch, absent-remote-ref and clean-index guards. Publish paths only under `dev/proofs/v4_late_cartridge_45/`. Open one draft PR referencing #45, record the exact HEAD and return the real local verification/publication results. Do not merge or close #45.

## Evidence and exceptions

Artist checks: 35 canonical render matches; 26 Mansion metatiles; 67 unique 8×8 Mansion tiles; 180 metatile placements; all BG neighborhoods select one of four global pools; HUD shares them; all sprite pieces select one of four shared sprite pools. Two 16×24 Reimu states differ by 70 pixels, retaining shared head/anchor/2×3 cell logic. Props retain 10×14/12×14 envelopes. Source HUD geometry/content is retained through deterministic recoloring.

No new palette exception, swap, overlap trick or waiver. Inherited profile hardware waivers are enumerated in evidence.md. Nonblocking lint findings are preserved with their exact validation reports. Artist checks are not Owner art acceptance or live runtime QA.

No laptop-local packaging/publication was attempted in Work. No branch, PR, merge, approval or broader V4 activation is claimed.

V4 LATE-CARTRIDGE PROOF — OWNER REVIEW REQUIRED
