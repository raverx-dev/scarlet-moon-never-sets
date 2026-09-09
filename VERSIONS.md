# Playable Version Archive

Scarlet Moon preserves notable playable iterations instead of treating every later visual or audio pass as a destructive replacement.

Versions 1, 2, and 3 are frozen. Version 3 is the owner-approved visual-redesign snapshot. Remaining Version 3 imperfections are accepted; later corrections are deferred to Version 4. Version 4 has not been created.

## Public playable snapshots

| Version | Description | Source checkpoint | Play path | Status |
| --- | --- | --- | --- | --- |
| Version 1 — Original Build | Original shipped build before P0, Visual P1, and Audio P1 | `08c2a1704a1943ee8d57b402e7a962395ab3f85b` | `versions/original/` | Frozen |
| Version 2 — Visual + Audio P1 | P0 fixes, Visual P1 presentation/art, and Audio P1 expanded music | `d505ce85103be0011fd60c7bfc6e5734e4df6833` | `versions/p1-visual-audio/` | Frozen |
| Version 3 — Sprite Redesign | Frozen owner-approved visual-redesign build: Version 2 foundation plus redesigned sprites, P0 character repairs, story-character integration, global UI chrome, Hakurei shrine/title, Stage 1–3 environment art, and owner-playtest story/dialogue staging fixes | `ea4c31aa8d2ad92e1a5d8bfb0f25d1ba0863ed31` | `versions/sprite-redesign/` | Frozen |

The repository-root `index.html` is the GitHub Pages version selector, so the normal project Pages URL opens the chooser first. `versions/index.html` is a secondary copy of the selector.

## Source archive branches

The exact source histories are also pinned by convention on archive branches:

- `archive/original-build`
- `archive/p1-visual-audio`
- `archive/sprite-redesign`
- `archive/version-3`

`archive/sprite-redesign` is historical: the initial Version 3 sprite checkpoint at `beb667e2cfec5faf38e689350c04e11addff6221`. It is not the frozen Version 3 source and must remain untouched.

`archive/version-3` is the frozen Version 3 source checkpoint at `ea4c31aa8d2ad92e1a5d8bfb0f25d1ba0863ed31`.

These branches are archival checkpoints and should not be used for ongoing development.

## After Version 3

Version 3 is frozen at `ea4c31aa8d2ad92e1a5d8bfb0f25d1ba0863ed31` on `sprite-redesign` and `archive/version-3`. `v1-polish` remains frozen at the accepted Visual + Audio P1 checkpoint.

Public Version 3 is frozen in place and must not be updated. Later work becomes Version 4. Version 4 has not been created.

Existing Version 1, Version 2, and Version 3 folders remain immutable and must never be overwritten.
