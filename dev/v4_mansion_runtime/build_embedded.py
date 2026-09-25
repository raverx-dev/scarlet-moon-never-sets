#!/usr/bin/env python3
"""Build the two native V4 mansion backgrounds from the accepted proof exports.

Reads dev/v4_mansion_runtime/inputs (verbatim proof files) and the accepted
preview PNGs. Renders with the proof compose.py placement rules, checks every
RGB pixel against those PNGs, and writes a synchronous palette buffer into
versions/v4/index.html. No network and no RoboPixel at runtime.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import importlib.util
import json
from pathlib import Path

from PIL import Image

REGISTERED_ROOT = Path("/home/dellis/Projects/scarlet-moon-never-sets")
PROOF = "c2241001946ac5456293f9f2b8be137e5c5bc648"
BASE = "d7054d2b9b111ff711f44cc3ee5b71268aca6ed8"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
INPUTS = HERE / "inputs"
ACCEPTED = HERE / "accepted"
HTML = ROOT / "versions" / "v4" / "index.html"
RECEIPT = HERE / "generation_receipt.json"
START = "/* V4_MANSION_EMBEDDED_START */"
END = "/* V4_MANSION_EMBEDDED_END */"
SCENES = (
    ("gameplay", 192, ACCEPTED / "mansion_gameplay_preview_192x240.png"),
    ("story", 256, ACCEPTED / "mansion_story_preview_256x240.png"),
)

MANSION_IIFE = """const MANSION=(function(){
  function canvasFrom(spec){
    const canvas=document.createElement('canvas');
    canvas.width=spec.w;canvas.height=spec.h;
    const g=canvas.getContext('2d',{alpha:false});
    g.imageSmoothingEnabled=false;
    const image=g.createImageData(spec.w,spec.h),data=image.data,raw=atob(spec.idx);
    if(spec.kind==='index'){
      if(raw.length!==spec.w*spec.h)throw Error('mansion index length');
      for(let i=0;i<raw.length;i++){
        const rgb=parseInt(spec.palette[raw.charCodeAt(i)].slice(1),16),o=i*4;
        data[o]=(rgb>>16)&255;data[o+1]=(rgb>>8)&255;data[o+2]=rgb&255;data[o+3]=255;
      }
    }else{
      if(raw.length!==spec.w*spec.h*3)throw Error('mansion rgb length');
      for(let i=0,o=0;i<raw.length;i+=3,o+=4){
        data[o]=raw.charCodeAt(i);data[o+1]=raw.charCodeAt(i+1);data[o+2]=raw.charCodeAt(i+2);data[o+3]=255;
      }
    }
    g.putImageData(image,0,0);
    return canvas;
  }
  const sheet=canvasFrom(V4_MANSION_BG.gameplay),story=canvasFrom(V4_MANSION_BG.story);
  if(sheet.width!==192||sheet.height!==240||story.width!==256||story.height!==240)throw Error('mansion background size');
  return Object.freeze({sheet,story,source:V4_MANSION_BG.source});
})();
"""

DRAW_OLD = """function drawInterior(t,w,dim){
  ctx.drawImage((w>=256&&MANSION.story)?MANSION.story:MANSION.sheet,0,0,w,240,0,0,w,240);
  if(dim)dimField(w,dim);
}"""

DRAW_NEW = """function drawInterior(t,w,dim){
  const src=(w>=256&&MANSION.story)?MANSION.story:MANSION.sheet;
  ctx.drawImage(src,0,0);
  if(dim)dimField(w,dim);
}"""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_compose():
    spec = importlib.util.spec_from_file_location("mansion_compose", INPUTS / "compose.py")
    if spec is None or spec.loader is None:
        raise SystemExit("compose.py could not be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rgb_bytes(image) -> bytes:
    if image.mode != "RGB":
        image = image.convert("RGB")
    return image.tobytes()


def pack(raw: bytes, width: int, height: int) -> dict:
    if len(raw) != width * height * 3:
        raise SystemExit(f"rgb length {len(raw)} != {width}x{height}")
    colors: list[str] = []
    index: dict[bytes, int] = {}
    buf = bytearray()
    for i in range(0, len(raw), 3):
        px = raw[i:i + 3]
        slot = index.get(px)
        if slot is None:
            slot = len(colors)
            index[px] = slot
            colors.append("#{:02x}{:02x}{:02x}".format(px[0], px[1], px[2]))
        buf.append(slot)
    if len(colors) <= 256:
        return {
            "kind": "index",
            "w": width,
            "h": height,
            "palette": colors,
            "idx": base64.b64encode(buf).decode("ascii"),
        }
    return {
        "kind": "rgb",
        "w": width,
        "h": height,
        "palette": [],
        "idx": base64.b64encode(raw).decode("ascii"),
    }


def unpack(spec: dict) -> bytes:
    raw = base64.b64decode(spec["idx"])
    if spec["kind"] == "index":
        if len(raw) != spec["w"] * spec["h"]:
            raise SystemExit("packed index length mismatch")
        out = bytearray()
        palette = [bytes.fromhex(color[1:]) for color in spec["palette"]]
        for byte in raw:
            out.extend(palette[byte])
        return bytes(out)
    if len(raw) != spec["w"] * spec["h"] * 3:
        raise SystemExit("packed rgb length mismatch")
    return raw


def render_scenes(compose):
    kit = compose.assets()
    layouts = json.loads((INPUTS / "layouts.json").read_text())
    rendered = {}
    for name, width, _path in SCENES:
        image = compose.render(layouts[name], kit)
        if image.size != (width, 240):
            raise SystemExit(f"{name} rendered {image.size}, expected {(width, 240)}")
        rendered[name] = image
    return rendered, layouts


def input_manifest() -> dict:
    files = {
        "compose.py": INPUTS / "compose.py",
        "layouts.json": INPUTS / "layouts.json",
        "robopixel_manifest.json": INPUTS / "robopixel_manifest.json",
        "floor_correction_verification.json": INPUTS / "floor_correction_verification.json",
        "historic_verification.json": INPUTS / "historic_verification.json",
        "accepted/mansion_gameplay_preview_192x240.png": ACCEPTED / "mansion_gameplay_preview_192x240.png",
        "accepted/mansion_story_preview_256x240.png": ACCEPTED / "mansion_story_preview_256x240.png",
    }
    for path in sorted((INPUTS / "exports").glob("*.json")):
        files[f"exports/{path.name}"] = path
    return {name: sha256_file(path) for name, path in files.items()}


def build_payload():
    if ROOT == REGISTERED_ROOT:
        raise SystemExit("refusing to build inside the registered Scarlet root")
    compose = load_compose()
    rendered, layouts = render_scenes(compose)
    floor = json.loads((INPUTS / "floor_correction_verification.json").read_text())
    historic = json.loads((INPUTS / "historic_verification.json").read_text())
    manifest = json.loads((INPUTS / "robopixel_manifest.json").read_text())
    paving = json.loads((INPUTS / "exports" / "paving.json").read_text())
    if paving.get("asset_id") != "v4-mansion-trans01-paving" or paving.get("revision") != 6:
        raise SystemExit(f"paving export is not r6: {paving.get('asset_id')} rev {paving.get('revision')}")
    if floor.get("status") != "PASS" or floor.get("asset_id") != "v4-mansion-trans01-paving":
        raise SystemExit("floor correction report is not the current paving PASS")
    scenes = {}
    payload_scenes = {}
    for name, width, path in SCENES:
        accepted = Image.open(path).convert("RGB")
        if accepted.size != (width, 240):
            raise SystemExit(f"accepted {name} is {accepted.size}")
        got = rgb_bytes(rendered[name])
        expect = rgb_bytes(accepted)
        if got != expect:
            mismatch = next(i for i, (a, b) in enumerate(zip(got, expect)) if a != b)
            pixel = mismatch // 3
            raise SystemExit(f"{name} pixel mismatch at {(pixel % width, pixel // width)}")
        file_hash = sha256_file(path)
        if file_hash != floor["scenes"][name]["sha256"]:
            raise SystemExit(f"{name} file sha256 does not match floor correction report")
        raw_hash = sha256_bytes(got)
        packed = pack(got, width, 240)
        if unpack(packed) != got:
            raise SystemExit(f"{name} palette buffer did not round-trip")
        scenes[name] = {
            "width": width,
            "height": 240,
            "png_sha256": file_hash,
            "rgb_sha256": raw_hash,
            "kind": packed["kind"],
            "palette_size": len(packed["palette"]),
            "floor_correction_png_sha256": floor["scenes"][name]["sha256"],
            "historic_verification_png_sha256": historic["scenes"][name]["sha256"],
        }
        payload_scenes[name] = packed
    assets = []
    for stem, meta in manifest["assets"].items():
        assets.append({
            "stem": stem,
            "asset_id": meta["asset_id"],
            "revision": meta["revision"],
            "revision_hash": meta["revision_hash"],
        })
    if len(assets) != 16:
        raise SystemExit(f"expected 16 manifest assets, found {len(assets)}")
    used = sorted({op["asset"] for name in ("gameplay", "story") for op in layouts[name]["operations"]})
    payload = {
        "source": {
            "proof": PROOF,
            "base": BASE,
            "paving": {
                "asset_id": paving["asset_id"],
                "revision": paving["revision"],
                "revision_hash": paving["revision_hash"],
            },
            "gameplay_png_sha256": scenes["gameplay"]["png_sha256"],
            "story_png_sha256": scenes["story"]["png_sha256"],
            "gameplay_rgb_sha256": scenes["gameplay"]["rgb_sha256"],
            "story_rgb_sha256": scenes["story"]["rgb_sha256"],
            "generator": "dev/v4_mansion_runtime/build_embedded.py",
        },
        "gameplay": payload_scenes["gameplay"],
        "story": payload_scenes["story"],
    }
    embedded = (
        f"{START}\n"
        "// Exact native mansion backgrounds from proof "
        f"{PROOF} exports and layouts. Paving v4-mansion-trans01-paving r6. "
        "Synchronous palette buffer; the game does not fetch pixels or call RoboPixel.\n"
        f"const V4_MANSION_BG={json.dumps(payload, separators=(',', ':'))};\n"
        f"{END}\n"
    )
    if "</script>" in embedded:
        raise SystemExit("embedded buffer would close the game script")
    receipt = {
        "proof": PROOF,
        "base": BASE,
        "historic_verification_source_commit": historic.get("source_commit"),
        "historic_verification_status": historic.get("status"),
        "floor_correction_status": floor.get("status"),
        "floor_correction_baseline": floor.get("baseline"),
        "qualification": "pixel equality with the two accepted PNGs at the proof commit; floor_correction_verification.json is the current paving PASS. historic verification.json source_commit is not the accepted head.",
        "paving": payload["source"]["paving"],
        "assets": assets,
        "layout_assets": used,
        "scenes": scenes,
        "inputs_sha256": input_manifest(),
        "command": "python3 dev/v4_mansion_runtime/build_embedded.py --apply",
    }
    return embedded, receipt


def splice(html: str, embedded: str) -> str:
    if START in html and END in html:
        pre, rest = html.split(START, 1)
        _old, post = rest.split(END, 1)
        # drop the newline that belonged to the previous block; embedded includes markers
        if pre.endswith("\n"):
            pre = pre[:-1]
        html = pre + "\n" + embedded + post.lstrip("\n")
    else:
        needle = "const MANSION=(function(){"
        if needle not in html:
            raise SystemExit("MANSION initializer not found")
        html = html.replace(needle, embedded + needle, 1)
    start = html.find("const MANSION=(function(){")
    roof = html.find("\nconst ROOF=(function(){", start)
    if start < 0 or roof < 0:
        raise SystemExit("could not locate MANSION initializer bounds")
    html = html[:start] + MANSION_IIFE + html[roof + 1:]
    if DRAW_OLD not in html:
        if DRAW_NEW not in html:
            raise SystemExit("drawInterior was not the expected one-line blit")
    else:
        html = html.replace(DRAW_OLD, DRAW_NEW, 1)
    return html


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the embedded buffer into versions/v4/index.html")
    args = parser.parse_args()
    embedded, receipt = build_payload()
    receipt["embedded_sha256"] = sha256_bytes(embedded.encode())
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in ("proof", "floor_correction_status", "historic_verification_source_commit", "scenes", "paving")}, indent=2))
    if not args.apply:
        print("check only; index.html not modified")
        return
    html = splice(HTML.read_text(), embedded)
    if embedded not in html or DRAW_NEW not in html:
        raise SystemExit("splice did not land in index.html")
    HTML.write_text(html)
    # Re-read and confirm the packed buffers still decode to the accepted RGB hashes.
    block = html.split(START, 1)[1].split(END, 1)[0]
    marker = "const V4_MANSION_BG="
    payload = json.loads(block.split(marker, 1)[1].strip().rstrip(";"))
    for name, _width, _path in SCENES:
        raw = unpack(payload[name])
        digest = sha256_bytes(raw)
        if digest != receipt["scenes"][name]["rgb_sha256"]:
            raise SystemExit(f"html {name} buffer hash {digest}")
    print(f"wrote {HTML.relative_to(ROOT)} and {RECEIPT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
