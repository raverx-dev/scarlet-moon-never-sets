"""Static checks for this isolated proof; no runtime/acceptance claims."""
from pathlib import Path
import hashlib,json,subprocess,sys
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pixels(p):return Image.open(p).convert('RGBA')
A=json.loads((ROOT/'authoring_inputs.json').read_text())['assets'];M=json.loads((ROOT/'robopixel_manifest.json').read_text());L=json.loads((ROOT/'layouts.json').read_text());C=json.loads((ROOT/'palette.json').read_text())
checks={};details={}
for n,a in A.items():
 ex=json.loads((ROOT/'exports'/f'{n}.json').read_text());m=ex['matrix'];v=M['assets'][n]
 assert m['rows']==a['rows'],n+' matrix differs'
 assert len(m['rows'])==a['height'] and all(len(r)==a['width'] for r in m['rows'])
 assert (m['width'],m['height'])==(a['width'],a['height'])
 assert ex['round_trip']['cel_hash'] is True and ex['delivery'] is False
 assert ex['revision']==v['revision'] and ex['revision_hash']==v['revision_hash']
 for token,symbol in m['symbols'].items():
  assert symbol.get('transparent') is True if token=='.' else symbol['hex'].lower()==C[token].lower()
 # Compare all RGBA pixels, including alpha, not PNG encoding.
 assert pixels(ROOT/'assets'/f'{n}.png').tobytes()==pixels(ROOT/'exports'/f'{n}.png').tobytes(),n+' PNG differs'
 details[n]={'revision':v['revision'],'matrix_equals_submitted':True,'canonical_png_equals_composition_asset':True,'size':[a['width'],a['height']]}
checks['all_16_canonical_matrix_and_png_round_trips']=len(details)==16
outputs=list(ROOT.glob('*.png'));before={p.name:digest(p) for p in outputs}
subprocess.run([sys.executable,str(ROOT/'compose.py')],check=True,capture_output=True)
assert before=={p.name:digest(p) for p in outputs}
checks['recompose_all_proof_pngs_byte_identical']=True
for name,w in [('gameplay',192),('story',256)]:
 p=ROOT/f'forest_{name}_preview_{w}x240.png';assert pixels(p).size==(w,240)
 en=pixels(ROOT/f'forest_{name}_3x.png');assert en.tobytes()==pixels(p).resize((w*3,720),Image.Resampling.NEAREST).tobytes()
 assert len(set(pixels(p).getdata()))<=26
checks['native_sizes_and_exact_nearest_neighbor_enlargements']=True
assert L['gameplay']['placements']!=L['story']['placements']
g=pixels(ROOT/'forest_gameplay_preview_192x240.png');s=pixels(ROOT/'forest_story_preview_256x240.png')
assert all(s.crop((x,0,x+192,240)).tobytes()!=g.tobytes() for x in range(65))
checks['story_not_any_gameplay_width_crop']=True
used=[{p['asset'] for p in L[view]['placements']} for view in ['gameplay','story']]
assert used[0]==set(A) and used[1]==set(A)
checks['all_16_assets_reused_in_both_compositions']=True
# Lane report is a static color/content fact, not dynamic readability qualification.
lane=g.crop((56,128,136,240)).convert('RGB');lane_colors=set(lane.getdata());allowed={tuple(bytes.fromhex(C[t][1:])) for t in ['0','1']}
assert lane_colors<=allowed
checks['lower_gameplay_lane_80x112_contains_only_two_dark_ground_colors']=True
# Check baseline trees in Git, including working copy. All changes must remain in proof dir.
base=M['base_commit'];prefix='dev/proofs/v4_forest_translation_01/'
changed=subprocess.check_output(['git','diff','--name-only',base],cwd=REPO,text=True).splitlines()
assert all(p.startswith(prefix) for p in changed),changed
tracked=subprocess.check_output(['git','ls-tree','-r','--name-only',base],cwd=REPO,text=True).splitlines()
for p in tracked:
 expected=subprocess.check_output(['git','rev-parse',base+':'+p],cwd=REPO,text=True).strip()
 actual=subprocess.check_output(['git','hash-object',p],cwd=REPO,text=True).strip()
 assert actual==expected,p+' protected baseline changed'
checks['all_base_tracked_files_unchanged']=True
refhash={'gameplay-REFERENCE-192x240.png':'20defa25e289b4d9c9b145c56b8f29a01e5aadcda95919ba7ce92ac85ed2a395','story-REFERENCE-256x240.png':'7e41e52e252a922f26e51aaa3d26290cea96f5c37cdea81361d868de96593d1e'}
assert all(digest(ROOT/'references'/n)==h for n,h in refhash.items())
checks['accepted_reference_hashes_preserved']=True
# The rejected checkpoint must remain an exact copy of the reviewed Git commit.
checkpoint='fa929a5627c17ac283ebb5e0bc9da2a1f26c71b7'
for p in (ROOT/'rejected_checkpoint').iterdir():
 if p.name=='SOURCE.txt':continue
 expected=subprocess.check_output(['git','show',checkpoint+':'+prefix+p.name],cwd=REPO)
 assert p.read_bytes()==expected,p.name+' rejected checkpoint changed'
checks['rejected_checkpoint_preserved_byte_exact']=True
assert all(not a['approval']['status']['approved'] for a in M['assets'].values())
checks['all_assets_unapproved_candidates']=True
correction_changes={}
for name,w in [('gameplay',192),('story',256)]:
 b=pixels(ROOT/'rejected_checkpoint'/f'forest_{name}_preview_{w}x240.png')
 a=pixels(ROOT/f'forest_{name}_preview_{w}x240.png')
 correction_changes[name]=sum(x!=y for x,y in zip(b.getdata(),a.getdata()))
checks['both_scenes_substantially_redrawn']=all(n>10000 for n in correction_changes.values())
assert checks['both_scenes_substantially_redrawn']
report={'status':'PASS','scope':'static proof only; not runtime QA or Owner art acceptance','base_commit':base,'protected_base_files':len(tracked),'correction_changed_pixels':correction_changes,'checks':checks,'assets':details,'native_outputs':{p.name:{'sha256':digest(p),'size':list(pixels(p).size),'rgba_sha256':hashlib.sha256(pixels(p).tobytes()).hexdigest()} for p in [ROOT/'forest_gameplay_preview_192x240.png',ROOT/'forest_story_preview_256x240.png']}}
(ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['status','protected_base_files','checks']},indent=2))
