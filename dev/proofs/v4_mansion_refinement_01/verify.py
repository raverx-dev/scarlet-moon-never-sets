"""Static exact-export, scene, provenance and protected-baseline checks."""
import hashlib,json,subprocess
from collections import Counter
from PIL import Image
from compose import ROOT,assets,exports,layouts,render

REPO=ROOT.parents[2]
PROOF='13ff42307d5f008b8fa8ebce80f546b164067a1b'
evidence=json.loads((ROOT/'robopixel_evidence.json').read_text())['assets']
inputs=json.loads((ROOT/'authoring_inputs.json').read_text())
old=json.loads((ROOT.parent/'v4_mansion_architectural_kit'/'robopixel_manifest.json').read_text())
old={a['key']:a for a in old['assets']}
result={'proof_head':PROOF,'assets':{},'scenes':{},'protected':{}}
assert len(exports)==13 and set(exports)==set(assets)
for key,e in exports.items():
    assert e['preview'] and not e['delivery'] and e['round_trip']['cel_hash'] is True
    assert e['matrix']['width']==assets[key].width and e['matrix']['height']==assets[key].height
    source=Image.open(ROOT/'canonical_previews'/f'{key}.png').convert('RGBA')
    assert source.size==assets[key].size and source.tobytes()==assets[key].tobytes(),key
    if key in inputs:
        assert e['matrix']['rows']==inputs[key]['rows']
        info=evidence[key]
        assert e['asset_id']==info['asset_id'] and e['revision']==info['revision']
        assert e['revision_hash']==info['revision_hash'] and info['validation_passed']
        assert info['approved'] is False and not info['active_approval_ids']
        if key in old:
            assert e['revision']==old[key]['revision']+1
            assert e['revision_hash']!=old[key]['revision_hash']
        else:assert e['revision']==2
    else:
        assert e['revision']==old[key]['revision']
        assert e['revision_hash']==old[key]['revision_hash']
        assert (ROOT/'exports'/f'{key}.json').read_bytes()==(ROOT.parent/'v4_mansion_architectural_kit'/'exports'/f'{key}.json').read_bytes()
    result['assets'][key]={'asset_id':e['asset_id'],'revision':e['revision'],'revision_hash':e['revision_hash'],
       'canonical_png_rgba_equal':True,'preview_round_trip':True,'approval':False if key in evidence else 'unchanged proof candidate'}
for name,w in [('gameplay',192),('story',256)]:
    path=ROOT/f'mansion_{name}_preview_{w}x240.png';im=Image.open(path).convert('RGB')
    assert im.size==(w,240) and im.tobytes()==render(w,layouts[name]['operations']).tobytes()
    palette={tuple(bytes.fromhex(p['hex'][1:])) for e in exports.values() for p in e['matrix']['symbols'].values() if 'hex' in p}
    assert set(im.getdata())<=palette
    result['scenes'][name]={'size':list(im.size),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
       'palette_only':True,'reproduced_from_exports':True,'operations':len(layouts[name]['operations']),
       'asset_usage':dict(Counter(o['asset'] for o in layouts[name]['operations']))}
assert Image.open(ROOT/'mansion_gameplay_preview_192x240.png').tobytes()!=Image.open(ROOT.parent/'v4_mansion_architectural_kit'/'mansion_gameplay_preview_192x240.png').tobytes()
assert Image.open(ROOT/'mansion_story_preview_256x240.png').tobytes()!=Image.open(ROOT.parent/'v4_mansion_architectural_kit'/'mansion_story_preview_256x240.png').tobytes()
assert Image.open(ROOT/'mansion_story_preview_256x240.png').crop((32,0,224,240)).tobytes()!=Image.open(ROOT/'mansion_gameplay_preview_192x240.png').tobytes()
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',PROOF],cwd=REPO,text=True).splitlines()
for p in paths:
    prior=subprocess.check_output(['git','show',PROOF+':'+p],cwd=REPO)
    assert (REPO/p).read_bytes()==prior,'Protected proof or runtime changed: '+p
result['protected']={'baseline_files_byte_identical':len(paths),'proof_directory_unchanged':True,
    'runtime_integration':False,'delivery_export':False,'live_game_qa':False}
(ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: 13 exact matrices/PNGs; 5 new selections unapproved; two reproducible native scenes; '+str(len(paths))+' baseline files unchanged.')
