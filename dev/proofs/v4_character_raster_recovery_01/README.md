# V4 character raster recovery 01

This proof recovers all 17 scoped story states from the approved enlarged
character sheet. The logical matrices in `matrices/` are authoritative. The
`native/` PNGs render those matrices at 1×; `previews/` are exact 8× NEAREST
views. `comparison/whole-cast-review.png` pairs each selected source crop with
its recovered sprite. `native-atlas.png` places every 1× sprite in manifest
order, with each placement recorded in `manifest.json`.

## Reproduce

Install Python 3 and Pillow, place the exact approved sheet at
`~/Downloads/Scarlet-Moon-V4-Approved-Character-State-Sheet.png`, then run:

```sh
python dev/proofs/v4_character_raster_recovery_01/recover_v4_characters.py
```

The converter stops if the source dimensions or SHA-256 differ from the
approved values. Its explicit half-open crop rectangles, dimensions, palette
subsets, threshold, BOX reduction, weighted RGB mapping, and preview scale
are in `recover_v4_characters.py`. The manifest repeats each final crop and
records all generated-output hashes. No manual pixel corrections were used.

## Known compromises

- Broad authored effects and props, especially Cirno Freeze, Marisa Attack,
  Sakuya Stop, and Remilia Final, reduce the body footprint under aspect-fit.
- The horizontal Meiling pose occupies roughly half of its 24×16 canvas height;
  forcing it taller would distort the approved silhouette. The sleep marks
  remain within the source crop but mostly disappear at native size.
- Restricted game palette colors cannot reproduce every tint in the enlarged
  sheet. BOX reduction also merges subpixel facial and costume detail.
- The Remilia A crop starts below the panel subtitle, sacrificing the uppermost
  cap pixels where the subtitle and art overlap vertically. This avoids
  incorporating typography into the native sprite.

This is a local raster proof only. It does not change runtime assets or
RoboPixel data.
