"""Current art gate: fixed accepted layouts, exact exports and static evidence."""
import hashlib,json,subprocess
from PIL import Image
from compose import R,assets,render
import verify
BASE='4ef4080fc17f53f03393ac74e205220072360c0b';REPO=R.parents[2];PREFIX=str(R.relative_to(REPO))+'/'
def old(p):return subprocess.check_output(['git','show',BASE+':'+PREFIX+p],cwd=REPO)
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    verify.main()
    for p in ('layouts.json','build_layouts.py','review_context.py','sprite_witnesses.json','story_before_after.png','story_correction_provenance.json','story_correction_verification.json','verify_story_correction.py'):
        assert (R/p).read_bytes()==old(p),p
    for p in (R/'story_before_correction').rglob('*'):
        if p.is_file():assert p.read_bytes()==old(str(p.relative_to(R)))
    for p in (R/'accepted_composition_checkpoint').iterdir():
        if p.name!='README.md':assert p.read_bytes()==old(p.name),p.name
    m=json.loads((R/'robopixel_manifest.json').read_text());prev=json.loads(old('robopixel_manifest.json'));assert set(m['assets'])==set(prev['assets'])
    pixel_counts={}
    for name,a in m['assets'].items():
        b=prev['assets'][name];assert (a['asset_id'],a['width'],a['height'])==(b['asset_id'],b['width'],b['height'])
        after=json.loads((R/'exports'/f'{name}.json').read_text())['matrix'];before=json.loads(old(f'exports/{name}.json'))['matrix']
        assert after['symbols']==before['symbols']
        count=sum(x!=y for ar,br in zip(after['rows'],before['rows']) for x,y in zip(ar,br));pixel_counts[name]=count
        if a['status']=='reused':assert count==0 and a['revision']==b['revision'] and a['revision_hash']==b['revision_hash']
        else:assert count>0 and a['revision']>b['revision']
    assert sum(n>0 for n in pixel_counts.values())==12
    before=Image.open(R/'accepted_composition_checkpoint/mansion_gameplay_preview_192x240.png').convert('RGB')
    after=Image.open(R/'mansion_gameplay_preview_192x240.png').convert('RGB')
    quiet=(76,128,116,240);assert before.crop(quiet).tobytes()==after.crop(quiet).tobytes()
    im=Image.open(R/'mansion_story_preview_256x240.png').convert('RGB')
    red={tuple(bytes.fromhex(h)) for h in ('260b1c','490e28','84233e','ca4963')}
    assert all(im.getpixel((128,y)) in red for y in range(102,240))
    required=['gameplay_art_before_after.png','story_art_before_after.png','mansion_gameplay_bullet_witness.png','bullet_readability_before_after.png','bullet_witnesses.json']
    assert all((R/f).is_file() for f in required)
    out={'status':'PASS','accepted_checkpoint':BASE,'layout_bytes_unchanged':True,'layout_source_unchanged':True,'canonical_asset_count':16,'revised':12,'reused':4,'new_assets':0,'changed_pixels_by_asset':pixel_counts,'palette_and_canvas_sizes_unchanged':True,'accepted_images_and_manifest_preserved_exactly':True,'actor_and_dialogue_staging_unchanged':True,'quiet_gameplay_region_unchanged':list(quiet),'story_stair_runner_connection':'PASS','native_images':{n:{'size':[w,240],'sha256':sha((R/f'mansion_{n}_preview_{w}x240.png').read_bytes())} for n,w in [('gameplay',192),('story',256)]},'static_readability':'Unchanged actors/UI plus fixed before-after V3 diamond/star sample','scope':'Mansion static art only; protected older files verified by verify.py','limitations':['Owner art review pending','No live combat/animation QA','No runtime or NES hardware qualification','No asset approval/delivery']}
    (R/'art_development_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
