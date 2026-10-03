#!/usr/bin/env python3
"""Deterministic local proof supplement for the #51 handoff package."""
import collections
import hashlib
import json
import pathlib
import sys
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
load = lambda name: json.loads((ROOT / name).read_text())
checkpoint = load('checkpoint.json')
artist = load('artist_checkpoint.json')
ledger = load('palette_ledger.json')
authoring = load('authoring.json')
readback = load('canonical_readback.json')
validations = load('validation_selected.json')
assets = {a['name']: a for a in authoring}
assert set(assets) == {a['name'] for a in artist['production_bank']}
assert len(assets) == 41 and len(checkpoint['assets']) == 46
used = {p['asset'] for s in checkpoint['scenes'] for p in s['placements']}
assert used == {a['name'] for a in checkpoint['assets']}
patterns = {}
asset_tiles = {}
for name, asset in assets.items():
    rows = asset['rows']
    assert rows == readback[name]['export']['matrix']['rows']
    w, h = asset['width'], asset['height']
    assert w % 8 == h % 8 == 0 and len(rows) == h and all(len(r) == w for r in rows)
    chunks = []
    rebuilt = [[''] * (w // 8) for _ in range(h // 8)]
    for y in range(0, h, 8):
        for x in range(0, w, 8):
            tile = tuple(r[x:x+8] for r in rows[y:y+8])
            # The family is part of the bank identity; identical symbols in different families carry different colors.
            key = (asset['group'], tile)
            if key not in patterns: patterns[key] = len(patterns)
            chunks.append(patterns[key])
            rebuilt[y//8][x//8] = tile
    assert tuple(''.join(rebuilt[y//8][x//8][y%8] for x in range(0,w,8)) for y in range(h)) == tuple(rows)
    asset_tiles[name] = {'width_tiles': w//8, 'height_tiles': h//8, 'tile_ids': chunks}
cols = 16
atlas = Image.new('RGBA', (cols*8, ((len(patterns)+cols-1)//cols)*8), (0,0,0,0))
for (family, rows), tile_id in patterns.items():
    colors = ledger['families'][family]
    symbols = {'.': (0,0,0,0), 'D': tuple(bytes.fromhex(colors[0][1:]))+(255,)}
    symbols.update({str(i): tuple(bytes.fromhex(colors[i][1:]))+(255,) for i in range(1,4)})
    for y,row in enumerate(rows):
        for x,ch in enumerate(row): atlas.putpixel(((tile_id%cols)*8+x,(tile_id//cols)*8+y), symbols[ch])
atlas.save(OUT/'tiles_8x8.png')
(OUT/'tile_manifest.json').write_text(json.dumps({'schema':'scarlet.mi51-tiles/v1','tile_count':len(patterns),'assets':asset_tiles},indent=2)+'\n')

candidate = Image.open(OUT/'candidate_native.png').convert('RGBA')
readability = Image.open(OUT/'readability_native.png').convert('RGBA')
assert candidate.size == readability.size == (192,240)
colors = {c.lower() for family in ledger['families'].values() for c in family}
assert len(colors) == 13
families = {name: {c.lower() for c in palette} for name,palette in ledger['families'].items()}
metatiles = {}
construction = []
family_counts = collections.Counter()
for y in range(0,240,16):
    row=[]
    for x in range(0,192,16):
        block = candidate.crop((x,y,x+16,y+16))
        key = block.tobytes()
        if key not in metatiles: metatiles[key] = len(metatiles)
        row.append(metatiles[key])
        visible = {'#%02x%02x%02x'%px[:3] for px in block.get_flattened_data() if px[3]}
        fits = [family for family,palette in families.items() if visible <= palette]
        assert fits, f'palette neighborhood {x},{y}: {visible}'
        family_counts[fits[0]] += 1
    construction.append(row)
assert sum(family_counts.values()) == 180
assert len(construction)==15 and all(len(row)==12 for row in construction)
(OUT/'construction_map.json').write_text(json.dumps({'schema':'scarlet.mi51-construction/v1','size':[12,15],'metatile_count':len(metatiles),'ids':construction,'family_counts':dict(sorted(family_counts.items()))},indent=2)+'\n')
meta_atlas = Image.new('RGBA',(16*8,((len(metatiles)+7)//8)*16),(0,0,0,0))
for raw,tile_id in metatiles.items():
    block = Image.frombytes('RGBA',(16,16),raw)
    meta_atlas.paste(block,((tile_id%8)*16,(tile_id//8)*16))
meta_atlas.save(OUT/'metatiles_16x16.png')
reconstructed = Image.new('RGBA',(192,240),(0,0,0,0))
for y,row in enumerate(construction):
    for x,tile_id in enumerate(row):
        raw = next(raw for raw,i in metatiles.items() if i==tile_id)
        reconstructed.paste(Image.frombytes('RGBA',(16,16),raw),(x*16,y*16))
assert reconstructed.tobytes()==candidate.tobytes()

lane=(64,128,128,240)
region_c=candidate.crop(lane)
region_r=readability.crop(lane)
changed=sum(a!=b for a,b in zip(region_c.get_flattened_data(),region_r.get_flattened_data()))
counts=collections.Counter(region_c.get_flattened_data())
mask=Image.new('L',candidate.size,0)
ImageDraw.Draw(mask).rectangle((lane[0],lane[1],lane[2]-1,lane[3]-1),fill=255)
mask.save(OUT/'quiet_lane_mask.png')
warning_count=sum(1 for v in validations.values() for finding in v['report']['findings'] if finding['disposition']=='warning' and finding['rule_id']=='pixel-orphans')
assert len(validations)==41 and all(v['report']['passed'] for v in validations.values()) and warning_count==58
pins=[{**a,'role':'environment' if a['name'] in assets else 'unchanged-witness'} for a in checkpoint['assets']]
# Retain names, revisions and exact hashes; no canonical bitmap copies.
(OUT/'bank_inventory.json').write_text(json.dumps({'schema':'scarlet.mi51-bank-inventory/v1','assets':pins},indent=2)+'\n')
wall, floor=assets['wall-field'],assets['floor-field']
soft=[]
if wall['rows']==floor['rows']:
    soft.append('wall-field and floor-field have pixel-equivalent rows but distinct material identities')
metrics={'schema':'scarlet.mi51-supplement-verification/v1','production_dimensions':[192,240], 'candidate_render_hash':checkpoint['scenes'][0]['render_hash'],'readability_render_hash':checkpoint['scenes'][1]['render_hash'],'environment_assets':41,'unchanged_witness_assets':5,'bank_all_used':True,'selected_validations_pass':41,'retained_orphan_warnings':warning_count,'bg_visible_colors':len(colors),'bg_subpalettes':len(families),'neighborhoods':180,'nonconforming_neighborhoods':0,'unique_8x8_tiles':len(patterns),'unique_16x16_metatiles':len(metatiles),'metatile_reconstruction_exact':True,'quiet_lane':{'x':64,'y':128,'width':64,'height':112,'pixels':64*112,'unique_rgba_colors':len(counts),'readability_changed_pixels':changed},'soft_diagnostics':soft}
(OUT/'supplement_verification.json').write_text(json.dumps(metrics,indent=2)+'\n')

sources=[Image.open(ROOT/'inputs'/f'{key}.png').convert('RGBA') for key in ['v3','accepted-22','proof-45']]+[candidate]
labels=['V3 CONSTRUCTION','ACCEPTED #22 HIERARCHY','#45 MINIMUM PROOF','#51 CANDIDATE']
board=Image.new('RGBA',(192*4,260),(16,18,30,255))
draw=ImageDraw.Draw(board)
for i,(im,label) in enumerate(zip(sources,labels)):
    assert im.size==(192,240)
    draw.text((i*192+4,5),label,fill=(255,255,255,255))
    board.paste(im,(i*192,20))
board.save(OUT/'comparison_four_pane.png')
candidate.resize((576,720),Image.Resampling.NEAREST).save(OUT/'candidate_nn3x.png')
print(json.dumps(metrics))
