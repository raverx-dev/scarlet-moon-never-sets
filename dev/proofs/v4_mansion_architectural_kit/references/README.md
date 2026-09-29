# Read-only composition references

These are offscreen source renders, not captured gameplay sessions.

- `v3_mansion_192x240.png`: frozen `versions/sprite-redesign/index.html` at main base `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8`; evaluated the original `C`, `PAL` and `MANSION` asset/composition closure using an offscreen Canvas implementation, then cropped the gameplay rectangle 0,0–192,240.
- `astra_mansion_192x240.png`: `versions/v4/index.html` at experimental checkpoint `1633785e7066e152df34edb0d595d28e12f0264a`, branch `v4-autonomous-production-20260921`; evaluated the original `painter`, `arch` and `interior(192)` composition with the unchanged Mansion prop matrices/palette. Used only as a spatial/focal reference.

Rendering used `@napi-rs/canvas` in the transient review workspace. Neither source was modified. No reference artwork was imported as a canonical proof asset. The proof's compositions consume only the ten new RoboPixel exports.

V3 Misty Lake was also visually inspected as a pixel-language/quiet-centre anchor; no Lake asset or scene was modified or included in this proof package.
