"""Offline verification of actual canonical read-back, assembly and boundaries."""
import hashlib,json,subprocess
from pathlib import Path
from PIL import Image
from compose import R,assets,decode,render
REPO=R.parents[2]; BASE='44530dd918ce498544025ca1919e91faccb619d4'
def git(*a):return subprocess.check_output(['git',*a],cwd=REPO)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    manifest=json.loads((R/'robopixel_manifest.json').read_text());inputs=json.loads((R/'authoring_inputs.json').read_text());layouts=json.loads((R/'layouts.json').read_text());kit=assets();checks=[]
    for name,a in manifest['assets'].items():
        e=json.loads((R/'exports'/f'{name}.json').read_text());p=Image.open(R/'canonical_previews'/f'{name}.png').convert('RGBA');m=decode(e)
        assert p.size==m.size==(a['width'],a['height'])
        assert p.tobytes()==m.tobytes(),name
        assert e['revision']==a['revision'] and e['revision_hash']==a['revision_hash']
        assert e['round_trip']['cel_hash'] is True
        st=a['approval']['status'];assert not st['approved'] and st['revision']==a['revision'] and st['revision_hash']==a['revision_hash']
        if a['status']!='reused':assert inputs['assets'][name]['rows']==e['matrix']['rows']
        checks.append({'asset':name,'asset_id':a['asset_id'],'revision':a['revision'],'revision_hash':a['revision_hash'],'canonical_png_vs_export_rgba':'PASS','submitted_rows':'PASS' if a['status']!='reused' else 'reused','approved':False})
    used={o['asset'] for n in ('gameplay','story') for o in layouts[n]['operations']};assert used==set(kit)
    palette={c[:3] for a in kit.values() for c in a.getdata() if c[3]}
    scenes={}
    for name,w in [('gameplay',192),('story',256)]:
        p=R/f'mansion_{name}_preview_{w}x240.png';im=Image.open(p).convert('RGB');assert im.size==(w,240)
        assert im.tobytes()==render(layouts[name],kit).tobytes()
        assert set(im.getdata())<=palette
        scenes[name]={'dimensions':[w,240],'reproduces_exactly':True,'palette_membership':True,'sha256':sha(p)}
    assert layouts['gameplay']['operations']!=layouts['story']['operations']
    protected=[]
    for raw in git('ls-tree','-r','-z',BASE).split(b'\0'):
        if not raw:continue
        meta,path=raw.split(b'\t');rel=path.decode();blob=meta.decode().split()[2];local=REPO/rel
        assert local.is_file(),rel
        assert git('hash-object',str(local)).decode().strip()==blob,rel
        protected.append(rel)
    tracked=git('diff','--name-only',BASE).decode().splitlines();assert all(p.startswith('dev/proofs/v4_mansion_translation_01/') for p in tracked)
    untracked=git('ls-files','--others','--exclude-standard').decode().splitlines();assert all(p.startswith('dev/proofs/v4_mansion_translation_01/') for p in untracked)
    required=['README.md','asset_inventory.md','robopixel_manifest.json','authoring_receipts.json','robopixel_readback.json','author_inputs.py','authoring_inputs.json','unpack_readback.py','compose.py','build_layouts.py','layouts.json','asset_atlas.png','gameplay_comparison.png','story_comparison.png','references/provenance.json','mansion_gameplay_scale.png','mansion_story_staging.png']
    assert all((R/p).is_file() for p in required)
    out={'status':'PASS','source_commit':BASE,'canonical_readback':checks,'scenes':scenes,'all_selected_assets_used':True,'protected_tracked_files_unchanged':len(protected),'original_proof_files_unchanged':sum(p.startswith('dev/proofs/v4_mansion_architectural_kit/') for p in protected),'refinement_files_unchanged':sum(p.startswith('dev/proofs/v4_mansion_refinement_01/') for p in protected),'required_files_present':required,'runtime_modified':False,'limits':['static only','not final art approval','no live combat or dialogue QA','not NES hardware qualification']}
    (R/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','canonical_assets':len(checks),'protected_files_unchanged':len(protected),'native_sizes':[[192,240],[256,240]]}))
if __name__=='__main__':main()
