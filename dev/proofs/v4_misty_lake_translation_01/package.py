"""Build provenance, full inventory and self-contained visual review."""
from pathlib import Path
import json,hashlib,base64,html,collections,io
from PIL import Image
ROOT=Path(__file__).parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v=json.loads((ROOT/'verification.json').read_text());valid=json.loads((ROOT/'evidence/validation.json').read_text())
refs=[]
for role,n,original in [('A / gameplay','image-a-gameplay.png','6f48a305-2539-433d-b235-149c149d6067.png'),('B / story','image-b-story.png','17603529-92cd-43ab-8cd7-7cb50ff8fd79.png')]:
 refs.append({'role':role,'original_filename':original,'path':'references/'+n,'sha256':sha(ROOT/'references'/n),'authority':'Owner-selected art direction supplied with this assignment; not production pixels'})
counts=collections.Counter((f['rule_id'],f['disposition']) for d in valid.values() for f in d['report']['findings'])
manifest={'schema':'scarlet-moon.static-art-proof/v1','project_id':'scarlet-moon-never-sets','unit':'v4-misty-lake-translation-01','governing_issues':[17,24,31,32],'source_commit':'d7054d2b9b111ff711f44cc3ee5b71268aca6ed8','source_paths':['versions/v4/index.html','versions/sprite-redesign/index.html'],'branch':'v4-misty-lake-translation-01','scope':'Static art candidate only. No runtime integration, approval, delivery, merge, publication or release acceptance.','references':refs,'palette_id':'v4-misty-lake-trans01','palette_hash':'a3653262fb23fce79d8bc0a4788636077cb422778da949c9e282f2d6d03fd952','assets':v['assets'],'validation':{'passed_assets':sum(d['report']['passed'] for d in valid.values()),'findings':[{'rule':r,'disposition':d,'count':c} for (r,d),c in counts.items()],'waivers':0},'proof_outputs':v['outputs'],'limitations':['Static overlays are illustrative, not live gameplay QA.','Witness sprites retain existing runtime art and orientation; no character fixes were authorized.','Reference microtexture and tonal range are deliberately simplified to 23 opaque palette colors at native resolution.','Pixel-orphan warnings and unused shared-palette information remain unwaived.','Mist and reflection are static; animation and defeat/attract routing require later runtime qualification.'],'method':'Original native integer indexed drafting from visual interpretation; D6 asset_create and grid_paste; exact D7 export and D3 render readback; proof-local integer composition. No reference raster sampling in production.'}
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
table='\n'.join(f"| `{a['asset_id']}` | {a['revision']} | {a['width']}×{a['height']} |" for a in v['assets'])
readme=f'''# Misty Lake — static art candidate 01

**Ready for Owner visual review, not accepted art or runtime integration.**

Open `review.html` for both native views, 3× enlargements, exact source comparisons,
separate readability witnesses, atlas and reference viewing thumbnails. It is self-contained.
GitHub transport is text-only: exact PNG bytes are preserved in `transport/`.
Run `python hydrate.py` to restore all 36 original PNG files, then run the check below.

## Authority and source

- Workstream #32; production #24; Manager continuity #31; program #17.
- Inspected main: `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8`.
- `versions/v4/index.html`: LAKE at line 1323; drawMistyLake at 1954; Stage 1 background at 1993;
  dialogue at 2035–2047; attract at 2076; stagecard at 2107; defeat at 2111.
- V3 `versions/sprite-redesign/index.html` and V4 LAKE reconstructions have identical RGBA.
- Story anchors: Reimu (56,124), Cirno (196,108), dialogue panel (4,174). Current story actors
  float above the shoreline; actor position/orientation is preserved only in illustrative witnesses.
- Gameplay boss origin (96,45); representative Reimu witness (96,206).
- Source reconstructions are extracted static matrices, not live browser captures.

## Approved references

Image A is the supplied gameplay reference; Image B is the supplied story reference.
Original bytes and SHA-256 identities are preserved losslessly in `transport/` and `manifest.json`;
`hydrate.py` restores them into `references/` and all other PNG paths.
Neither image was regenerated, traced, sampled for colors, nor downscaled into production.
Reference resizing occurs only inside the clearly labelled comparison boards.

The interpretation preserves blue night water, scarlet moon and off-centre reflection,
wooded slopes, distant torii/lights, frost, rock banks and reeds. Gameplay keeps an open central
water lane. Story independently frames the lake with a left tree and diagonal lower shore.
The kit uses 23 opaque colors plus transparency; detailed generated-reference microtexture is simplified.

## Reproduce

Python 3 + Pillow (tested 12.3.0):

```sh
python hydrate.py
python compose.py --check
```

This needs only the committed canonical exports, render evidence, source matrices, references and layouts.
No RoboPixel service, GitHub, authoring generator or game runtime is needed to reproduce the selected proof.
`python compose.py` rebuilds outputs. `python package.py` rebuilds review/provenance.
`node extract-baseline.cjs` re-extracts baseline evidence only when the repository files match the pinned source.

`author.py` and `draft-grids.json` are original drafting evidence, not the compositor's inputs or
a replacement for canonical RoboPixel state. For future edits reopen the exact asset ID with an
expected current revision; persist a new revision, read it back, then update proof inputs.

## Verification

- 19/19 canonical export matrices exactly match decoded RoboPixel PNG RGBA; zero pixel differences.
- 19/19 Scarlet adapter logical round trips pass.
- Native outputs are opaque 192×240 and 256×240; layouts are distinct.
- 34 generated PNGs reproduce byte-for-byte with `compose.py --check`.
- 19/19 RoboPixel validation reports pass, with 388 pixel-orphan warnings and 338 unused-color information findings.
  These concern fine stars/frost/texture and a shared family palette. They remain visible and unwaived;
  technical validation is not a visual quality approval.
- Runtime and protected versions are untouched. No unrelated branch or asset was changed.

## Canonical selected revisions

| Asset ID | Revision | Native size |
| --- | ---: | --- |
{table}

All IDs belong to project `scarlet-moon-never-sets`, frame `default`, layer `art`.
Full revision, render, palette, RGBA and PNG hashes are in `manifest.json` and the exact readback records.

## Package inventory

- `exports/`: D7 canonical matrices plus 19 exact D3 PNG exports.
- `evidence/`: D3 PNG transport/readbacks, D9 validation, D6 mutation receipts and pinned source matrices.
- `layouts.json`, `layout.py`, `compose.py`: explicit independent scenes and deterministic build/check logic.
- `previews/`: native/3× scenes, atlas, V3/V4 reconstructions, comparison boards and separate static witnesses.
- `references/`: both unchanged Owner-selected images.
- `manifest.json`, `verification.json`, `README.md`, `review.html`, `changed-files.txt`: provenance and review.
- `author.py`, `draft-grids.json`, `palette.json`, `extract-baseline.cjs`, `package.py`: reproduction/authoring evidence.

## Limits and stop

Static proof only. No animated mist, moving-bullet test, in-game performance or defeat/attract routing qualification.
The story witness uses original sprites and a substitute static text font; it does not fix known Cirno orientation.
Owner visual acceptance remains pending. No formal per-asset delivery, runtime integration, merge,
publication, freeze or release acceptance is claimed. Corrections should stay on this branch/PR.
'''
(ROOT/'README.md').write_text(readme)
def img(p,klass='',width=None):
 raw=(ROOT/p).read_bytes()
 if p.startswith('references/'):
  im=Image.open(io.BytesIO(raw));im.thumbnail((512,640));b=io.BytesIO();im.save(b,format='PNG');raw=b.getvalue()
 data=base64.b64encode(raw).decode();return f'<img class="{klass}" src="data:image/png;base64,{data}" alt="{html.escape(p)}" '+(f'width="{width}"' if width else '')+'>'
parts=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Misty Lake static art review</title><style>body{margin:0;background:#0b1020;color:#dae4f7;font:16px/1.5 system-ui}main{max-width:1160px;margin:auto;padding:28px}h1{color:#ff8e9c}h2{margin-top:40px}.row{display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start}figure{margin:0 0 20px}figcaption{margin:8px 0;color:#a8bbd7}img{max-width:100%;height:auto}.pixel{image-rendering:pixelated}.large{width:auto;max-height:720px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.5 monospace;background:#151d31;padding:20px}summary{cursor:pointer;color:#a8d7ff;padding:10px}</style><main><h1>Misty Lake / static art candidate</h1><p>Owner review pending • 19 canonical RoboPixel assets • 192×240 gameplay / 256×240 story</p><p>Blue water, a scarlet moon and frosted shores. These are exact authored outputs. No runtime integration or release acceptance.</p><h2>Native 1×</h2><div class="row">']
for n,w in [('gameplay',192),('story',256)]:parts.append(f'<figure>{img(f"previews/{n}_{w}x240.png","pixel")}<figcaption>{n.title()} — {w}×240</figcaption></figure>')
parts.append('</div><h2>Pixel inspection / 3×</h2>')
for n in ['gameplay','story']:parts.append(f'<figure>{img(f"previews/{n}_3x.png","pixel large")}<figcaption>{n.title()} — exact nearest-neighbor enlargement</figcaption></figure>')
parts.append('<h2>Separate illustrative witnesses</h2><p>Existing source sprites and dialogue frame. Representative bullets/items and substitute text font. Static staging only; not live QA.</p>')
for n in ['gameplay','story']:parts.append(img(f'previews/{n}_witness_3x.png','pixel large'))
parts.append('<h2>Source → reference → canonical</h2><p>V3 and current V4 are exact static sheet reconstructions at the inspected commit. The reference panel is resized for comparison only.</p>')
for n in ['gameplay','story']:parts.append(img(f'previews/{n}_comparison.png','pixel'))
parts.append('<h2>Canonical asset atlas</h2>'+img('previews/atlas.png','pixel'))
parts.append('<h2>Approved art-direction references</h2>')
for r in refs:parts.append(f'<details><summary>Image {r["role"]} — viewing thumbnail; exact original in transport bundle</summary>{img(r["path"])}</details>')
parts.append('<h2>Production report and reproducibility</h2><pre>'+html.escape(readme)+'</pre></main></html>')
(ROOT/'review.html').write_text(''.join(parts))
files=sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='changed-files.txt' and p.suffix!='.png')+['changed-files.txt']
(ROOT/'changed-files.txt').write_text('\n'.join(sorted(files))+'\n')
print('Packaged',len(files),'files; standalone review, manifest and full inventory ready')
