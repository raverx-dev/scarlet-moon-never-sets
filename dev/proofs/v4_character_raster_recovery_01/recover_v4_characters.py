#!/usr/bin/env python3
"""Recover native Scarlet Moon V4 character matrices from the approved sheet.

Requires Pillow. Run from any directory; see README.md. The source art is never
changed or included in this proof. All output is deterministic for a given
Pillow implementation and the verified source bytes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = Path.home() / "Downloads/Scarlet-Moon-V4-Approved-Character-State-Sheet.png"
SOURCE_SHA256 = "9e50e1a48440882187df834085b3c76b3b538460166daad023f4ec94e3b7fcc5"
ORIGIN_MAIN_SHA = "bd857570e5c55d261392e0e819720cff3637b8c5"
BACKGROUND = (8, 8, 16)
THRESHOLD = 35
PADDING = 0
PREVIEW_SCALE = 8

# Exact PAL symbol colors from versions/v4/index.html at ORIGIN_MAIN_SHA.
# C aliases are resolved here to their literal values from the same file.
PALETTE = {
    "r": "#e83a51", "R": "#9a2438", "w": "#fff0ce", "W": "#d4c4a8",
    "h": "#191528", "H": "#2c2438", "f": "#f6b993", "F": "#e08a72",
    "k": "#080810", "b": "#424d9d", "B": "#2a3160", "c": "#81d8ed",
    "C": "#c8f2ff", "g": "#f5cb70", "G": "#64b58a", "p": "#ff93b4",
    "P": "#c45a88", "m": "#ae68d7", "M": "#6b3d9a", "y": "#ffe08a",
    "s": "#c8c8d8", "S": "#8a8aa0", "u": "#704638", "o": "#c47a4a",
    "i": "#4aa0c8", "n": "#171b39", "e": "#21423e", "d": "#3a2040",
    "x": "#87243b", "v": "#5a8f6a", "l": "#d0e8ff", "t": "#8b5a3c",
    "a": "#a9a4b6", "z": "#ffd0e0",
}

ALLOWED = {
    "Reimu": "rRwWhHfFgk",
    "Cirno": "cCbiBlwWfFhH",
    "Marisa": "hHMwWfFygotbB",
    "Sakuya": "sSwWbBcCfFhH",
    "Remilia": "pPzrRwWbBhHfFx",
    "Meiling": "rRGgevwWfFhH",
}

# Half-open rectangles (left, top, right, bottom), deliberately confined to
# the authored artwork within each labeled panel. No panel or label is used.
STATES = (
    ("reimuStoryA", "Reimu", 24, 32, (28, 93, 215, 308)),
    ("reimuStoryB", "Reimu", 24, 32, (224, 93, 403, 308)),
    ("reimuStoryTalkA", "Reimu", 24, 32, (410, 93, 556, 308)),
    ("reimuStoryTalkB", "Reimu", 24, 32, (589, 93, 739, 308)),
    ("cirno", "Cirno", 24, 32, (44, 429, 217, 663)),
    ("cirnoB", "Cirno", 24, 32, (242, 429, 413, 663)),
    ("cirnoFreeze", "Cirno", 24, 32, (437, 428, 735, 663)),
    ("marisa", "Marisa", 32, 32, (788, 78, 1027, 312)),
    ("marisaB", "Marisa", 32, 32, (1030, 78, 1220, 312)),
    ("marisaAttack", "Marisa", 32, 32, (1235, 100, 1512, 312)),
    ("sakuya", "Sakuya", 32, 32, (800, 426, 1008, 668)),
    ("sakuyaB", "Sakuya", 32, 32, (1008, 417, 1221, 668)),
    ("sakuyaStop", "Sakuya", 32, 32, (1237, 412, 1495, 668)),
    ("remilia", "Remilia", 32, 32, (29, 772, 283, 986)),
    ("remiliaB", "Remilia", 32, 32, (291, 755, 554, 986)),
    ("remiliaFinal", "Remilia", 32, 32, (556, 750, 911, 990)),
    ("meilingSleep", "Meiling", 24, 16, (1019, 777, 1386, 936)),
)

# Exact (x, y, symbol) triples. Currently no pixel corrections are needed.
CORRECTIONS: dict[str, tuple[tuple[int, int, str], ...]] = {}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rgb(hex_color: str) -> tuple[int, int, int]:
    return tuple(bytes.fromhex(hex_color.removeprefix("#")))  # type: ignore[return-value]


def has_content(color: tuple[int, int, int]) -> bool:
    return max(color) > THRESHOLD


def content_bounds(im: Image.Image) -> tuple[int, int, int, int]:
    pix = im.load()
    xs: list[int] = []
    ys: list[int] = []
    for y in range(im.height):
        for x in range(im.width):
            if has_content(pix[x, y]):
                xs.append(x)
                ys.append(y)
    if not xs:
        raise ValueError("Empty source crop")
    return min(xs), min(ys), max(xs) + 1, max(ys) + 1


def nearest_symbol(color: tuple[int, int, int], subset: str) -> str:
    r, g, b = color
    return min(
        subset,
        key=lambda symbol: (
            0.30 * (r - rgb(PALETTE[symbol])[0]) ** 2
            + 0.59 * (g - rgb(PALETTE[symbol])[1]) ** 2
            + 0.11 * (b - rgb(PALETTE[symbol])[2]) ** 2,
            subset.index(symbol),
        ),
    )


def matrix_image(rows: list[str]) -> Image.Image:
    im = Image.new("RGBA", (len(rows[0]), len(rows)), (0, 0, 0, 0))
    pix = im.load()
    for y, row in enumerate(rows):
        for x, symbol in enumerate(row):
            if symbol != ".":
                pix[x, y] = (*rgb(PALETTE[symbol]), 255)
    return im


def recover(sheet: Image.Image, name: str, character: str, width: int, height: int,
            rect: tuple[int, int, int, int]) -> tuple[list[str], Image.Image, tuple[int, int, int, int]]:
    crop = sheet.crop(rect).convert("RGB")
    bounds = content_bounds(crop)
    bounded = crop.crop(bounds)
    scale = min(width / bounded.width, height / bounded.height)
    scaled_width = min(width, max(1, round(bounded.width * scale)))
    scaled_height = min(height, max(1, round(bounded.height * scale)))
    reduced = bounded.resize((scaled_width, scaled_height), Image.Resampling.BOX)
    canvas = Image.new("RGB", (width, height), BACKGROUND)
    canvas.paste(reduced, ((width - scaled_width) // 2, (height - scaled_height) // 2))
    pixels = canvas.load()
    subset = ALLOWED[character]
    rows = [
        "".join("." if not has_content(pixels[x, y]) else nearest_symbol(pixels[x, y], subset)
                for x in range(width))
        for y in range(height)
    ]
    if name in CORRECTIONS:
        mutable = [list(row) for row in rows]
        for x, y, symbol in CORRECTIONS[name]:
            if not (0 <= x < width and 0 <= y < height and symbol in subset + "."):
                raise ValueError(f"Invalid correction: {name} {(x, y, symbol)}")
            mutable[y][x] = symbol
        rows = ["".join(row) for row in mutable]
    native = matrix_image(rows)
    absolute_bounds = (rect[0] + bounds[0], rect[1] + bounds[1],
                       rect[0] + bounds[2], rect[1] + bounds[3])
    return rows, native, absolute_bounds


def review_board(sheet: Image.Image, natives: dict[str, Image.Image]) -> Image.Image:
    font = ImageFont.load_default()
    columns, card_w, card_h = 3, 430, 278
    rows_count = (len(STATES) + columns - 1) // columns
    board = Image.new("RGB", (columns * card_w, rows_count * card_h), (20, 20, 29))
    draw = ImageDraw.Draw(board)
    for index, (name, character, width, height, rect) in enumerate(STATES):
        x0 = (index % columns) * card_w
        y0 = (index // columns) * card_h
        draw.rectangle((x0 + 3, y0 + 3, x0 + card_w - 4, y0 + card_h - 4), outline=(72, 74, 96))
        draw.text((x0 + 12, y0 + 12), f"{name}  {width}x{height}", font=font, fill=(255, 240, 206))
        draw.text((x0 + 12, y0 + 34), "approved source crop", font=font, fill=(169, 164, 182))
        draw.text((x0 + 233, y0 + 34), "recovered native x6", font=font, fill=(169, 164, 182))
        crop = sheet.crop(rect)
        source_scale = min(206 / crop.width, 212 / crop.height)
        source_size = (max(1, round(crop.width * source_scale)),
                       max(1, round(crop.height * source_scale)))
        crop_view = crop.resize(source_size, Image.Resampling.NEAREST)
        board.paste(crop_view, (x0 + 12 + (206 - source_size[0]) // 2,
                                y0 + 56 + (212 - source_size[1]) // 2))
        native = natives[name]
        large = native.resize((width * 6, height * 6), Image.Resampling.NEAREST)
        native_bg = Image.new("RGBA", large.size, (*BACKGROUND, 255))
        native_bg.alpha_composite(large)
        board.paste(native_bg.convert("RGB"),
                    (x0 + 228 + (192 - large.width) // 2,
                     y0 + 56 + (212 - large.height) // 2))
    return board


def native_atlas(natives: dict[str, Image.Image]) -> tuple[Image.Image, dict[str, list[int]]]:
    columns, cell_w, cell_h = 4, 40, 40
    atlas = Image.new("RGBA", (columns * cell_w, 5 * cell_h), (0, 0, 0, 0))
    positions = {}
    for index, (name, _, width, height, _) in enumerate(STATES):
        x = (index % columns) * cell_w + (cell_w - width) // 2
        y = (index // columns) * cell_h + (cell_h - height) // 2
        atlas.alpha_composite(natives[name], (x, y))
        positions[name] = [x, y, width, height]
    return atlas, positions


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    args = parser.parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Approved source is missing: {source}")
    observed_hash = sha256(source)
    if observed_hash != SOURCE_SHA256:
        raise SystemExit(f"Approved source SHA mismatch: {observed_hash}")
    with Image.open(source) as im:
        if im.size != (1536, 1024):
            raise SystemExit(f"Approved source dimensions mismatch: {im.size}")
        sheet = im.convert("RGB")
    for dirname in ("matrices", "native", "previews", "comparison"):
        (ROOT / dirname).mkdir(exist_ok=True)

    natives: dict[str, Image.Image] = {}
    assets: dict[str, dict] = {}
    hashes: dict[str, str] = {}
    for name, character, width, height, rect in STATES:
        rows, native, bounds = recover(sheet, name, character, width, height, rect)
        natives[name] = native
        matrix_path = ROOT / "matrices" / f"{name}.json"
        native_path = ROOT / "native" / f"{name}.png"
        preview_path = ROOT / "previews" / f"{name}.png"
        matrix_path.write_text(json.dumps({"name": name, "width": width, "height": height,
                                           "rows": rows}, indent=2) + "\n")
        native.save(native_path)
        native.resize((width * PREVIEW_SCALE, height * PREVIEW_SCALE),
                      Image.Resampling.NEAREST).save(preview_path)
        assets[name] = {"character": character, "dimensions": [width, height],
                        "crop": list(rect), "content_bounds": list(bounds),
                        "palette_subset": ALLOWED[character],
                        "corrections": [list(item) for item in CORRECTIONS.get(name, ())]}
        for path in (matrix_path, native_path, preview_path):
            hashes[str(path.relative_to(ROOT))] = sha256(path)

    board_path = ROOT / "comparison" / "whole-cast-review.png"
    review_board(sheet, natives).save(board_path)
    hashes[str(board_path.relative_to(ROOT))] = sha256(board_path)
    atlas, positions = native_atlas(natives)
    atlas_path = ROOT / "native-atlas.png"
    atlas.save(atlas_path)
    hashes[atlas_path.name] = sha256(atlas_path)
    for name, position in positions.items():
        assets[name]["atlas_xywh"] = position
    for path in (ROOT / "recover_v4_characters.py", ROOT / "README.md"):
        hashes[path.name] = sha256(path)
    manifest = {
        "source_path": str(source), "source_sha256": observed_hash,
        "origin_main_sha": ORIGIN_MAIN_SHA,
        "palette_source": "versions/v4/index.html:32,43 at origin/main",
        "palette": PALETTE, "threshold_max_rgb_gt": THRESHOLD,
        "padding": PADDING, "background_rgb": "#080810",
        "reduction": "Pillow Image.Resampling.BOX",
        "fit": "aspect-preserving, rounded dimensions, centered with floor offset",
        "quantization": "weighted squared RGB (0.30, 0.59, 0.11), subset order tie-break, no dithering",
        "preview": f"Pillow Image.Resampling.NEAREST x{PREVIEW_SCALE}",
        "manual_corrections": {key: [list(item) for item in value]
                               for key, value in CORRECTIONS.items()},
        "assets": assets, "output_sha256": dict(sorted(hashes.items())),
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Recovered {len(STATES)} states in {ROOT}")


if __name__ == "__main__":
    main()
