# Playable Version Archive

Scarlet Moon deliberately preserves notable playable iterations instead of treating every later visual or audio pass as a destructive replacement.

## Public playable snapshots

| Version | Description | Source checkpoint | Play path |
| --- | --- | --- | --- |
| Version 1 — Original Build | Original shipped build before P0, Visual P1, and Audio P1 | `08c2a1704a1943ee8d57b402e7a962395ab3f85b` | `versions/original/` |
| Version 2 — Visual + Audio P1 | P0 fixes, Visual P1 presentation/art, and Audio P1 expanded music | `d505ce85103be0011fd60c7bfc6e5734e4df6833` | `versions/p1-visual-audio/` |
| Version 3 — Sprite Redesign | Version 2 foundation plus the dedicated character-sprite redesign, native character assets, and approved sprite-animation/integration work | `beb667e2cfec5faf38e689350c04e11addff6221` | `versions/sprite-redesign/` |

The repository-root `index.html` is the GitHub Pages version selector, so the normal project Pages URL opens the chooser first. `versions/index.html` is a secondary copy of the selector.

## Source archive branches

The exact source histories are also pinned by convention on archive branches:

- `archive/original-build`
- `archive/p1-visual-audio`
- `archive/sprite-redesign`

These branches are archival checkpoints and should not be used for ongoing development.

## Ongoing development

Active work continues separately from the preserved snapshots. `v1-polish` remains frozen at the accepted Visual + Audio P1 checkpoint. Version 3 is frozen from `sprite-redesign` commit `beb667e2cfec5faf38e689350c04e11addff6221`; later sprite/background/polish work may continue on active branches without changing the published Version 3 snapshot.

Do not overwrite an existing version folder with a newer build. Each preserved version must remain launchable exactly as it was accepted. If an older published build ever receives a backported feature, treat that as an explicit version-maintenance decision rather than silently replacing its frozen snapshot.
