# V1 polish and acceptance audit

Status: IN PROGRESS. Audit only; no shipped behavior changes authorized.

Baseline: `main`, commit `08c2a1704a1943ee8d57b402e7a962395ab3f85b`.
Executable SHA-256: `b891b4e6f4f7e6cd07111f584897219520bfe89ffde09c06db66d331fe222eb5`.
Date: 2026-09-08. Branch: `v1-polish-audit`.

The recovered sandbox executable differs only by its trailing newline. The repository executable is the canonical test target. Original preparation documents and all four mockups are preserved in `audit/reference/`. Recovered regression code is in `qa/regression.js`; it exercises mechanics through direct simulation calls and does not certify visual quality, musical fidelity, or human-played difficulty.

Findings and evidence will be committed incrementally. This checkpoint is not an acceptance decision.

## Interim findings checkpoint

32 recovered regression groups pass. All three stages and all fourteen boss phases have been visually inspected. Acceptance is not met: fractional sprite scaling produces a visible grid through boss artwork; title, portraits and stage environments fall materially below the reference quality; attract close-up, ending dialogue and Cirno credits contain layering defects. Music loops and remaining credits checks are under review. Findings are being expanded into the full required issue schema.
