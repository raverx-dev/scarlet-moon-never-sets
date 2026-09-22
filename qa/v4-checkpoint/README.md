# V4 controlled checkpoint — 2026-09-22

Candidate branch: `v4-autonomous-production-20260921`.
Runtime implementation commit: `df75dfe3a3e6f288b520f4ef576abd90e228f114`.
Verified main remains `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8`.

## State at interruption
Implementation was already pushed. Final rendered captures and independent playable-link verification were in progress. This bounded continuation reconciled the local files with GitHub and preserved the existing QA evidence; it did not begin another production objective.

## Implemented candidate
Composed forest, vaulted mansion, separate mansion gate approach, and moonlit rooftop environments; retained Misty Lake and the accepted splash. Added back-facing gameplay Reimu, centered the focus indicator without changing collision mechanics, corrected Cirno dialogue facing, stabilized affected cast animation, and improved ending clear-message contrast. These remain candidate artwork and presentation changes awaiting Owner review.

## Verification
This checkpoint reran:
- `node qa/v4-splash-smoke.mjs`: PASS (delivered splash, transparency, branding, JavaScript syntax).
- `SCARLET_QA_SOURCE=versions/v4/index.html python3 qa/build.py`: PASS.
- `git diff --check`: PASS.
- Exact local-byte comparison against the remote candidate: all five implementation files match.
- Remote main hash: unchanged.

The adjacent regression and diagnostics JSON files were produced during the preceding production interval, not rerun at this checkpoint. The existing browser regression reported 32 passed, 0 failed against the candidate. This is not a full human playthrough. The standalone Playwright runner was not successfully run because its Chromium download failed.

## Approval boundary
RoboPixel asset `v4-reimu-back-gameplay-candidate-01`, revision 8, hash `cf2de4cef1e70427d5033db2dc54d34ddc6b0826d235e906d7fabfad16fbdf7a` is PREVIEW / REVIEW ONLY, not formally approved or delivered. The integrated preview records are committed under versions/v4/assets. Validation passed with pixel-orphan warnings; no approval or delivery bypass was used. Existing approved splash revision 6 is preserved.

## Remaining delivery work — not started in this checkpoint
Finish representative final captures, particularly Cirno dialogue, both clear-message states, and dense roof combat; verify the distinct direct playable candidate URL and its code identity. Several earlier captures predate final refinements, so a completed before/after review package is not claimed.

A separate private Sites project was created previously, but its deployed version still contains the baseline and its sign-in gate prevented hosted-game verification. The local scarlet-preview workspace contains the candidate dist files and development configuration, which are not committed/deployed there. Do not deliver that baseline URL as the new candidate. No CDN candidate link has yet been verified.

The game implementation is durably on GitHub. Local JPEG captures and preview workspace files remain available but are not a finished durable review package. Optional touch/gamepad work (#9/#10) and engine extraction (#3) remain deferred. No PR, merge, public V4 replacement, final acceptance, or release freeze was performed.

Next bounded task: complete candidate playable-link verification, then stop and report its result. Owner visual acceptance and formal approval of new canonical artwork remain outstanding.
