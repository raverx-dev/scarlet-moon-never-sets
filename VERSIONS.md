# Playable Version Archive

Scarlet Moon preserves notable playable iterations instead of treating every later visual or audio pass as a destructive replacement.

Versions 1 and 2 are frozen. Version 3 is the current published visual-redesign line: it is playable now, but it is still active development and may be updated in place until the owner explicitly declares Version 3 complete.

## Public playable snapshots

| Version | Description | Source checkpoint | Play path | Status |
| --- | --- | --- | --- | --- |
| Version 1 — Original Build | Original shipped build before P0, Visual P1, and Audio P1 | `08c2a1704a1943ee8d57b402e7a962395ab3f85b` | `versions/original/` | Frozen |
| Version 2 — Visual + Audio P1 | P0 fixes, Visual P1 presentation/art, and Audio P1 expanded music | `d505ce85103be0011fd60c7bfc6e5734e4df6833` | `versions/p1-visual-audio/` | Frozen |
| Version 3 — Sprite Redesign | Current live visual-redesign build: Version 2 foundation plus redesigned sprites, P0 character repairs, and approved story-character integration | `69d06766c0a6c165f26f71ded96d7b5bd8a122df` | `versions/sprite-redesign/` | Active / published |

The repository-root `index.html` is the GitHub Pages version selector, so the normal project Pages URL opens the chooser first. `versions/index.html` is a secondary copy of the selector.

## Source archive branches

The exact source histories are also pinned by convention on archive branches:

- `archive/original-build`
- `archive/p1-visual-audio`
- `archive/sprite-redesign`

`archive/sprite-redesign` is historical: the initial Version 3 sprite checkpoint at `beb667e2cfec5faf38e689350c04e11addff6221`. It is not the active Version 3 source and must remain untouched.

These branches are archival checkpoints and should not be used for ongoing development.

## Ongoing development

Active Version 3 work continues on the `sprite-redesign` integration branch, currently at `69d06766c0a6c165f26f71ded96d7b5bd8a122df`. `v1-polish` remains frozen at the accepted Visual + Audio P1 checkpoint.

Public Version 3 may be updated in place during the ongoing V3 visual redesign. It becomes frozen only when the owner explicitly declares Version 3 complete. After that, later work becomes Version 4.

Existing Version 1 and Version 2 folders remain immutable and must never be overwritten. Do not create Version 4 until Version 3 is frozen.
