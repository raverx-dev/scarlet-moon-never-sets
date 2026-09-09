#!/usr/bin/env python3
"""Read-only visual measurements for the V3 owner-playtest audit.

Does not modify game runtime. Reads PNG captures and writes JSON/CSV
plus optional side-by-side comparison strips.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = Path(__file__).resolve().parent / "evidence"
V3 = EVIDENCE / "v3"
V2 = EVIDENCE / "v2"
COMPARE = EVIDENCE / "compare"
ANALYSIS = EVIDENCE / "analysis"
BLACK = (8, 8, 16)  # C.black
GUTTER_SCENES = [
    "cirno-dialogue",
    "marisa-dialogue",
    "sakuya-dialogue",
    "remilia-dialogue",
    "intro",
    "ending-dialogue",
    "gate",
    "attract-cirno",
    "attract-marisa",
    "attract-sakuya",
    "stage1",
    "stage2",
    "stage3-interior",
    "stage3-roof",
    "stagecard-1",
    "stagecard-2",
    "stagecard-3",
    "continue",
    "dawn-anchor",
    "credits-cirno",
    "credits-reimu",
    "title",
    "how",
    "r5-final",
    "s1",
    "c1",
    "m4-active",
]


def scale_of(im: Image.Image) -> int:
    return max(1, round(im.size[0] / 256))


def region_stats(im: Image.Image, box, near_black=18):
    x0, y0, x1, y1 = box
    crop = im.crop((x0, y0, x1, y1)).convert("RGB")
    px = list(crop.getdata())
    n = len(px) or 1
    mean = tuple(sum(c[i] for c in px) / n for i in range(3))
    lum = 0.2126 * mean[0] + 0.7152 * mean[1] + 0.0722 * mean[2]
    blackish = sum(
        1
        for r, g, b in px
        if abs(r - BLACK[0]) <= near_black
        and abs(g - BLACK[1]) <= near_black
        and abs(b - BLACK[2]) <= near_black
    )
    return {
        "mean_rgb": [round(x, 2) for x in mean],
        "mean_luma": round(lum, 2),
        "near_black_frac": round(blackish / n, 4),
        "pixels": n,
    }


def analyze_one(path: Path) -> dict | None:
    if not path.exists():
        return None
    im = Image.open(path).convert("RGB")
    s = scale_of(im)
    w, h = im.size
    play = region_stats(im, (0, 0, 192 * s, h))
    gutter = region_stats(im, (192 * s, 0, min(w, 256 * s), h))
    # Dialogue text box occupies y>=174; measure character band y=80..170
    char_gutter = region_stats(im, (192 * s, 80 * s, min(w, 256 * s), 170 * s))
    right_edge = region_stats(im, (240 * s, 0, min(w, 256 * s), h))
    return {
        "file": path.name,
        "size": [w, h],
        "scale": s,
        "playfield_0_192": play,
        "gutter_192_256": gutter,
        "gutter_char_band": char_gutter,
        "right_16px": right_edge,
    }


def side_by_side(v2: Path, v3: Path, dest: Path, label: str):
    a = Image.open(v2).convert("RGB")
    b = Image.open(v3).convert("RGB")
    # Match height; keep native capture scale
    h = max(a.size[1], b.size[1])
    def fit(im):
        if im.size[1] == h:
            return im
        w = round(im.size[0] * h / im.size[1])
        return im.resize((w, h), Image.Resampling.NEAREST)
    a, b = fit(a), fit(b)
    pad = 28
    gap = 8
    canvas = Image.new("RGB", (a.size[0] + b.size[0] + gap, h + pad), (12, 12, 20))
    canvas.paste(a, (0, pad))
    canvas.paste(b, (a.size[0] + gap, pad))
    draw = ImageDraw.Draw(canvas)
    draw.text((8, 8), f"V2  {label}", fill=(245, 203, 112))
    draw.text((a.size[0] + gap + 8, 8), f"V3  {label}", fill=(255, 147, 180))
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest)


def main():
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    COMPARE.mkdir(parents=True, exist_ok=True)
    rows = []
    for name in GUTTER_SCENES:
        p = V3 / f"{name}.png"
        rec = analyze_one(p)
        if rec:
            rec["id"] = name
            rec["version"] = "v3"
            rows.append(rec)
    (ANALYSIS / "gutter_v3.json").write_text(json.dumps(rows, indent=2) + "\n")
    with (ANALYSIS / "gutter_v3.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "id",
                "gutter_luma",
                "gutter_near_black_frac",
                "char_band_luma",
                "char_band_near_black_frac",
                "playfield_luma",
            ]
        )
        for r in rows:
            w.writerow(
                [
                    r["id"],
                    r["gutter_192_256"]["mean_luma"],
                    r["gutter_192_256"]["near_black_frac"],
                    r["gutter_char_band"]["mean_luma"],
                    r["gutter_char_band"]["near_black_frac"],
                    r["playfield_0_192"]["mean_luma"],
                ]
            )
    compared = []
    for p3 in sorted(V3.glob("*.png")):
        p2 = V2 / p3.name
        if p2.exists():
            dest = COMPARE / p3.name
            side_by_side(p2, p3, dest, p3.stem)
            compared.append(p3.stem)
    summary = {
        "v3_analyzed": len(rows),
        "side_by_sides": compared,
        "v3_dir": str(V3),
        "v2_dir": str(V2),
    }
    (ANALYSIS / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    print("\nV3 gutter (x>=192) near-black fraction / luma:")
    for r in rows:
        g = r["gutter_192_256"]
        c = r["gutter_char_band"]
        print(
            f"  {r['id']:22} gutter_black={g['near_black_frac']:.3f} luma={g['mean_luma']:6.1f}  "
            f"char_band_black={c['near_black_frac']:.3f} luma={c['mean_luma']:6.1f}"
        )


if __name__ == "__main__":
    sys.exit(main())
