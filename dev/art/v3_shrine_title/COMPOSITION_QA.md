# V3 Hakurei Shrine / Title — Composition QA

Governing issue: #16

Status: **PASS / ready for mechanical integration**

This is an art-authoring composition QA note only. It does not integrate or modify runtime code.

## Corrected preview issues

The matrix-only preview was corrected after review for:

- morning sky accidentally remaining dark;
- trees/foliage placed in front of shrine architecture;
- shrine door and building component misalignment;
- torii / stairs / path alignment;
- shifted/skewed-looking horizontal assembly lines caused by inconsistent placement;
- scene density and layering.

The revised matrix-only preview was reviewed in the authoring session and accepted as sufficient to proceed.

## Integration scale guidance

The preview is a composition proof, not a fixed-size runtime layout.

- Keep accepted character sprites at their native accepted scale.
- Do **not** shrink Reimu or other gameplay sprites to make the shrine fit.
- Make the shrine larger by composing/repeating the authored 8x8 and 16x16 tiles and architectural components.
- The 64x56 torii may be positioned or integer-scaled where appropriate.
- Use integer logical-pixel placement and nearest-neighbor presentation only.
- No fractional scaling, smoothing, or downsampling.
- The final shrine should read substantially larger and more imposing than the compact matrix-only preview if the runtime scene has room.

## Asset status

- 51 deterministic native matrices.
- Existing `PAL` letters plus `.` transparency only.
- Dimension / allowed-character validation: PASS.
- Scarlet and silver moons retained.
- `東方紅月夜` authored title matrix retained.
- No character redraw.
- No Stage 1/2/3 asset changes.
- No `index.html` or runtime integration changes in this branch.
