# Scarlet Moon V4 Environmental Style Guide — v0.2 evidence board

This directory is the mechanical review artifact authorized by issue #40. Open
`review.html` locally. It assembles Manager-authored doctrine and exact internal
evidence; it does not redesign, edit, approve, integrate, publish, freeze, or
merge any art.

## Pinned provenance

The branch starts from remote `main` at
`45e701cf41ef089808babd567a59574b4e326deb`.

| Evidence package | Exact source head |
| --- | --- |
| Mansion Gate Exterior / PR #29 | `796f76d4c173ce4ae5287d20d74d9c37b8f1c8c4` |
| Mansion Interior / PR #22 | `c2241001946ac5456293f9f2b8be137e5c5bc648` |
| Forest / PR #26 | `08c2c5364d7e4a5eaa4fbb43e97209e5abf145e0` |
| Misty Lake / PR #34 | `040c405e912c85b38f08d7ba4a0660e76cb821a1` |
| Rooftop / PR #37 | `468e793d03b90d5c30b2ac09ea8992b9af7eb6c9` |
| Shrine / PR #39 | `8438cd4e04e82c12a9f16932ed4fc639f5c2979b` |

`manifest.json` is the file-level source index. Every image entry records the
exact source commit, original path, copied path, copied-byte SHA-256, role, and
annotation category.

## Curation and reproduction

- Gate and Interior are workmanship benchmarks, not hardware-perfect NES claims.
- Forest, Misty Lake, Rooftop, and Shrine are working checkpoints with explicit
  preserve/polish questions; they are not rejected scenes.
- Forest, Rooftop, and Shrine V3/current images are construction-signature
  references for visible tile vocabulary, palette economy, banding/stepping,
  and reuse. V3 is not the V4 quality ceiling.
- The caution set stays small: Misty Lake rejected-before/corrected evidence,
  Interior floor rollback, and Forest working before/after.
- External NES/Famicom screenshots are links only. No third-party screenshot is
  stored here, and the links are vocabulary/technical references rather than
  instructions to copy art.

All direct proof PNGs were extracted from the pinned Git objects and copied
without pixel or byte changes. Misty Lake is the package's documented exception:
in a detached checkout of exact head `040c405…`, `python hydrate.py` restored 41
PNG payloads from the committed transport index. The five selected presentation
PNGs were then copied from their original generated `previews/` paths; their
hashes matched `verification.json` and the transport index. No `transport/*.b64`
file is present here.

Run from this directory:

```sh
python verify.py
```

The verifier uses only the Python standard library. It checks every manifest
entry, rejects unlisted PNGs, and confirms that no transport payload is exposed.
For direct Git-backed sources it also compares copied bytes with
`git show <commit>:<path>`. Misty Lake generated files are checked against the
pinned SHA-256 recorded after hydration because their generated paths are not
Git blobs.

## Limits and stop

The page is CSS/HTML only and loads only local Scarlet Moon images. CSS nearest-
neighbor enlargement is presentation-only; source PNGs were not resampled or
annotated. This board grants no authority for canonical art mutation, RoboPixel
state changes, runtime integration, proof-branch changes, publication, merge, or
release. Owner review is required before any later environment-polish work.
