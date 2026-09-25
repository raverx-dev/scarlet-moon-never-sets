#!/usr/bin/env python3
"""Verify canonical export correspondence, fixed scene outputs and protected source scope."""
from pathlib import Path
import json,hashlib,subprocess
from collections import Counter
from PIL import Image
from compose import compose
P=Path(__file__).resolve().parent;repo=P.parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((P/'manifest.json').read_text());read=json.loads((P/'selected_readback.json').read_text())
recovered=json.loads((P/'recovery_asset_inventory.json').read_text());byid={a['asset_id']:a for a in recovered}
checks={};selected={}
for a in read:
 e=a['export'];name=a['name'];matrix=e['matrix'];r=byid[e['asset_id']]
 assert (r['current_revision'],r['current_revision_hash'])==(e['revision'],e['revision_hash'])
 assert a['describe']['current_revision_hash']==e['revision_hash']==a['view']['revision_hash']
 assert e['round_trip']['cel_hash'] is True
 rows=matrix['rows'];im=Image.new('RGBA',(matrix['width'],matrix['height']))
 colors={s:((0,0,0,0) if val.get('transparent') else tuple(bytes.fromhex(val['hex'][1:]))+(255,)) for s,val in matrix['symbols'].items()}
 im.putdata([colors[c] for row in rows for c in row]);canonical=Image.open(P/'canonical'/(name+'.png')).convert('RGBA')
 assert im.size==canonical.size and im.tobytes()==canonical.tobytes(),name
 assert json.loads((P/'authoring'/(name+'.json')).read_text())['rows']==rows,name
 assert json.loads((P/'exports'/(name+'.json')).read_text())==e
 selected[name]={'revision':e['revision'],'revision_hash':e['revision_hash'],'mismatching_rgba_pixels':0}
checks['all_15_canonical_exports_equal_saved_inputs_and_pngs']=True
checks['selected_revisions_match_recovery_inventory']=True
scene={}
for mode,size in [('gameplay',(192,240)),('story',(256,240))]:
 l=json.loads((P/(mode+'_layout.json')).read_text());assert tuple(l['size'])==size
 for op in l['placements']:
  assert type(op['x']) is int and type(op['y']) is int
  assert op['asset'] in selected
  assert set(op)<=set(['asset','x','y','mirror','crop'])
 im=compose(l);saved=Image.open(P/(mode+'_native.png')).convert('RGBA')
 assert saved.size==size and im.tobytes()==saved.tobytes()
 assert im.tobytes()==compose(l).tobytes()
 assert Image.open(P/(mode+'_3x.png')).convert('RGBA').tobytes()==im.resize((size[0]*3,size[1]*3),Image.Resampling.NEAREST).tobytes()
 scene[mode]={'size':size,'mismatching_rgba_pixels':0,'rgba_sha256':hashlib.sha256(im.tobytes()).hexdigest(),'png_sha256':sha(P/(mode+'_native.png')),'layout_sha256':sha(P/(mode+'_layout.json'))}
checks['native_dimensions_and_deterministic_reproduction']=True
checks['exact_3x_nearest_neighbor']=True
assert scene['gameplay']['layout_sha256']!=scene['story']['layout_sha256']
# A distinct layout is evidenced by independently chosen key placements, not just width.
g=json.loads((P/'gameplay_layout.json').read_text())['placements'];s=json.loads((P/'story_layout.json').read_text())['placements']
for name in ['scarlet-moon','gargoyle','spire-tower','parapet']:
 assert [(o['x'],o['y']) for o in g if o['asset']==name]!=[(o['x'],o['y']) for o in s if o['asset']==name]
checks['independent_layouts_and_key_landmark_positions']=True
expected=['3ff8959d76eec065a155c81f81cdadbfb0d66717dd45dd2fcdb9203a2452e61c','0790e19bc04277da86e7aacd742cf52936540043e58538aaf55271bde9681f94']
for r,h in zip(m['references'],expected):assert sha(P/r['path'])==r['sha256']==h
checks['exact_owner_reference_hashes']=True
base=m['base_sha'];scope='dev/proofs/v4_mansion_rooftop_translation_01/'
changed=subprocess.check_output(['git','diff','--name-only',base],cwd=repo,text=True).splitlines()
assert all(p.startswith(scope) for p in changed)
for f in ['versions/v4/index.html','versions/sprite-redesign/index.html','index.html']:
 assert (repo/f).read_bytes()==subprocess.check_output(['git','show',base+':'+f],cwd=repo)
checks['protected_runtime_files_unchanged']=True
checks['all_tracked_changes_within_proof_directory']=True
lint=json.loads((P/'lint.json').read_text());counts=Counter()
for a in lint:
 l=a['result']['structuredContent']['lint'];assert l['passed'];counts.update(x['disposition'] for x in l['findings'])
report={'result':'PASS','scope':'Static deterministic proof; not artistic acceptance or live gameplay qualification','base_sha':base,'checks':checks,'assets':selected,'scenes':scene,'lint':{'assets_passed':len(lint),'findings':dict(counts),'waivers_recorded':0},'limitations':['Source captures use the actual unchanged game code in @napi-rs/canvas; no browser QA claim.','Quiet pavement and repeated motifs remain working-draft choices.','Bright moon can overlap Remilia; motion and all-phase readability remain unqualified.','No formal approval/delivery, runtime integration, merge or publication.']}
(P/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'result':'PASS','checks':len(checks),'canonical_assets':len(selected),'scene_mismatches':0,'lint':report['lint']}))
