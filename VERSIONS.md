# Playable Version Archive

Scarlet Moon deliberately preserves notable playable iterations instead of treating every later visual or audio pass as a destructive replacement.

## Public playable snapshots

| Version | Description | Source checkpoint | Play path |
| --- | --- | --- | --- |
| Version 1 — Original Build | Original shipped build before P0, Visual P1, and Audio P1 | `08c2a1704a1943ee8d57b402e7a962395ab3f85b` | `versions/original/` |
| Version 2 — Visual + Audio P1 | P0 fixes, Visual P1 presentation/art, and Audio P1 expanded music | `d505ce85103be0011fd60c7bfc6e5734e4df6833` | `versions/p1-visual-audio/` |

The repository-root `index.html` is the GitHub Pages version selector, so the normal project Pages URL opens the chooser first. `versions/index.html` is a secondary copy of the selector.

## Source archive branches

The exact source histories are also pinned by convention on archive branches:

- `archive/original-build`
- `archive/p1-visual-audio`

These branches are archival checkpoints and should not be used for ongoing development.

## Ongoing development

Active work continues separately. `v1-polish` remains frozen at the accepted Visual + Audio P1 checkpoint while sprite replacement work proceeds on `sprite-redesign`. A future sprite-redesign build will become Version 3 only after it is accepted as a distinct playable iteration. At that point, copy its exact self-contained `index.html` into a new immutable-style folder under `versions/` and create a corresponding `archive/...` source branch before further development continues.

Do not overwrite an existing version folder with a newer build. Each preserved version must remain launchable exactly as it was accepted.
