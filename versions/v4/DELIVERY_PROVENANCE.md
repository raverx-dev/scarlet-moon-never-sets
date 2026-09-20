# Version 4 splash-logo delivery provenance

Source: formally approved RoboPixel asset `scarlet-moon-never-sets/v4-can-cigarette-splash-logo-01`.

- Approved revision: 6
- Approved revision hash: `6166ab944d1eb0d863ef934a78e92e5ec7e47f053a07039d637edfafb0ed8472`
- Active approval ID: `approval-c69b61bf-6866-4702-934e-3ac9aad73920`
- Approval subject hash: `e0009f7229aaf6f914812ebc472fc422fc919bd29a5d09dee5877ae25a4f55eb`
- Reference-set hash: `d847516b85477cbf6b86f7da0df884dce40e693822c720630c3cc06cc4007458`
- Canonical palette hash: `eb49f56d4966b7361fb8a2773efbb26d66edcf5539a99baee94a19199f44498c`
- Trusted export profile: `scarlet-v4-can-splash-delivery`; profile hash `0c205298172e39e0a317a79cef8a079fd246166bab2375e6c877755d093c9d2a`
- Original delivery ID: `export-fc1a4a28-a0a7-4548-b64d-c6ddfa97020b`
- Re-fetched delivery ID for source-byte transport into GitHub: `export-97de4ab7-e864-4b16-9359-72216a8fb0cd`
- Delivery subject hash: `163cfc2f435c2d50c0786d485c5eb920b7433cdc37d2fa6ffaccbc1683c4f021`
- Both deliveries carry the same artifact SHA-256: `f7b5f92c858b2b54873b3e2296170bb6be9265b93e550bce4b41a29b5a1dfea7`

`assets/v4-can-cigarette-splash-logo-01.scarlet-moon.json` preserves the exact byte-for-byte delivered Scarlet adapter payload; `index.html` embeds that JSON unchanged as `V4_CAN_EXPORT`. The renderer maps each declared exported symbol directly to its delivered hex color and honors the exported transparent `.` symbol without remapping into the older game's palette. It draws the approved 64×64 pixels at integer coordinates. No outside asset fetch is performed.

This is a V4 *candidate* pending automated browser regression, splash/credits capture, owner visual review, and merge authorization. Frozen V1–V3 snapshots are unchanged. Root version selectors are deliberately not updated before V4 acceptance.
