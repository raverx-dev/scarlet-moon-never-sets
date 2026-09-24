#!/usr/bin/env python3
"""Rebuild recovered proofs from canonical renders; --check writes nothing.
Requires Python 3, Pillow and NumPy. Originals are never written.
"""
from pathlib import Path
import argparse, hashlib, json
from PIL import Image, ImageDraw
import numpy as np
P = Path(__file__).resolve().parent
ORIGINAL_HASHES = {
    'gameplay': '6e5c9e62c47ab47777c9530089ce8a65ede34df733a973a571b8575eeac9e7a9',
    'story': 'b6151fd7ccf91357dbf2cbcb9600c4760db57619bbd60b3327caaabf49af49cb',
}
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def mismatch(a,b):
    aa,bb=np.array(a.convert('RGBA')),np.array(b.convert('RGBA'))
    assert aa.shape==bb.shape, 'Dimension mismatch'
    return np.any(aa!=bb,axis=2)
def run(check=False):
    layouts=json.loads((P/'layouts.json').read_text())
    manifest=json.loads((P/'asset_manifest.json').read_text())
    assets={}; report={'schema_version':1,'status':'PASS','method':'Exact RGBA comparison; original file SHA-256; pinned canonical render hashes.', 'assets':[], 'scenes':{}}
    for row in manifest['assets']:
        file=P/row['file'];assert sha(file)==row['png_sha256'],file
        im=Image.open(file).convert('RGBA');assert im.size==(row['width'],row['height'])
        assert row['revision']==2
        name=row['asset_id'].removeprefix('v4-mansion-gate-trans01-');assets[name]=im
        uses={s:sum(n['asset']==name for n in l['placements']) for s,l in layouts.items()}
        assert sum(uses.values())>0, name
        report['assets'].append({'asset_id':row['asset_id'],'revision':2,'revision_hash':row['revision_hash'],'render_hash':row['render_hash'],'png_sha256':row['png_sha256'],'dimensions':list(im.size),'placement_counts':uses})
    outputs={}
    for scene,layout in layouts.items():
        path=P/f'gate_{scene}_3x.png';assert sha(path)==ORIGINAL_HASHES[scene], 'Recovered original changed'
        original=Image.open(path).convert('RGBA');expected=(192,240) if scene=='gameplay' else (256,240)
        assert original.size==(expected[0]*3,expected[1]*3)
        # Exact block sample, not an interpolating resize.
        native=Image.fromarray(np.array(original)[::3,::3].copy())
        enlarged=native.resize(original.size,Image.Resampling.NEAREST)
        block_diff=int(mismatch(original,enlarged).sum());assert block_diff==0,'Original is not uniform 3x blocks'
        composed=Image.new('RGBA',expected,tuple(layout['background']))
        for n in layout['placements']:
            im=assets[n['asset']]
            if n['flip_x']: im=im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            composed.alpha_composite(im,(n['x'],n['y']))
        diff=mismatch(native,composed);count=int(diff.sum())
        diff3=int(mismatch(original,composed.resize(original.size,Image.Resampling.NEAREST)).sum())
        mask=Image.fromarray(np.where(diff[:,:,None],np.array([255,70,120,255],dtype=np.uint8),np.array([0,0,0,255],dtype=np.uint8)))
        outputs[f'gate_{scene}_native.png']=native
        outputs[f'gate_{scene}_recomposed.png']=composed
        outputs[f'gate_{scene}_mismatch.png']=mask
        report['scenes'][scene]={'original_sha256':sha(path),'original_dimensions':list(original.size),'native_dimensions':list(native.size),'native_rgba_sha256':hashlib.sha256(native.tobytes()).hexdigest(),'recomposed_rgba_sha256':hashlib.sha256(composed.tobytes()).hexdigest(),'native_to_original_3x_differing_pixels':block_diff,'canonical_to_native_differing_pixels':count,'canonical_to_original_3x_differing_pixels':diff3,'placements':len(layout['placements']),'exact':count==0 and diff3==0}
        if count or diff3: report['status']='FAIL'
    atlas=Image.new('RGBA',(1120,760),(20,24,39,255));draw=ImageDraw.Draw(atlas)
    for i,(name,im) in enumerate(assets.items()):
        x=(i%4)*280;y=(i//4)*190
        draw.text((x+10,y+8),f'{name} / r2 / {im.width}x{im.height}',fill='#e9d9c0')
        atlas.alpha_composite(im,(x+10,y+29))
    outputs['gate_asset_atlas.png']=atlas
    for name,im in outputs.items():
        if check: assert not mismatch(Image.open(P/name),im).any(), f'Stale output: {name}'
        else: im.save(P/name)
    text=json.dumps(report,indent=2)+'\n'
    if check: assert (P/'validation.json').read_text()==text,'Stale validation.json'
    else: (P/'validation.json').write_text(text)
    print(json.dumps({'status':report['status'],'scenes':report['scenes']},indent=2))
    return report['status']=='PASS'
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true')
    raise SystemExit(0 if run(parser.parse_args().check) else 1)
