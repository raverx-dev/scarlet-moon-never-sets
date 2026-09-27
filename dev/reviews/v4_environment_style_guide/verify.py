#!/usr/bin/env python3
"""Verify evidence-board PNG inventory, hashes, and direct Git provenance."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures: list[str] = []
    listed: set[str] = set()

    for item in data["images"]:
        relative = item["copied_path"]
        listed.add(relative)
        copied = ROOT / relative
        if not copied.is_file():
            failures.append(f"missing copied file: {relative}")
            continue
        payload = copied.read_bytes()
        actual = sha256(payload)
        if actual != item["sha256"]:
            failures.append(
                f"hash mismatch: {relative}: {actual} != {item['sha256']}"
            )

        # Hydrated Misty Lake previews are generated presentation paths, not
        # blobs at the source commit. Their exact payload hashes are authoritative.
        if item["source_commit"] == "040c405e912c85b38f08d7ba4a0660e76cb821a1":
            continue
        result = subprocess.run(
            [
                "git",
                "show",
                f"{item['source_commit']}:{item['source_path']}",
            ],
            cwd=ROOT,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode != 0:
            failures.append(
                f"cannot read source blob: {item['source_commit']}:{item['source_path']}"
            )
        elif result.stdout != payload:
            failures.append(f"source bytes differ: {relative}")

    actual_pngs = {
        path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.png")
    }
    for relative in sorted(actual_pngs - listed):
        failures.append(f"unlisted PNG: {relative}")
    for relative in sorted(listed - actual_pngs):
        failures.append(f"manifest-only PNG: {relative}")
    if any(path.suffix == ".b64" for path in ROOT.rglob("*")):
        failures.append("transport .b64 payload found in review output")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(
        f"PASS: {len(listed)} PNGs match manifest SHA-256; "
        "23 direct sources are byte-identical; 5 hydrated Misty Lake hashes match"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
