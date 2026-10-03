"""Floor01A gate and before/after boards; only visible paving may change."""
import io,json,subprocess,hashlib
from PIL import Image,ImageDraw,ImageChops
from compose import R,assets,render
import verify
BASE='41132bc77e632d06132989cf134b7ed9719211e3';REPO=R.parents[2];PREFIX=str(R.relative_to(REPO))+'/'
def old(p):return subprocess.check_output(['git','show',BASE+':'+PREFIX+p],cwd=REPO)
def main():
    verify.main()
    for p in ('layouts.json','build_layouts.py','compose.py','review_context.py','sprite_witnesses.json','bullet_witnesses.json'):
        assert (R/p).read_bytes()==old(p),p
    kit=assets();m=json.loads((R/'robopixel_manifest.json').read_text());prior=json.loads(old('robopixel_manifest.json'))
    for name in kit:
        if name=='paving':continue
        for folder,ext in [('exports','json'),('canonical_previews','png')]:
            p=f'{folder}/{name}.{ext}';assert (R/p).read_bytes()==old(p),p
        assert m['assets'][name]==prior['assets'][name]
    target=json.loads(subprocess.check_output(['git','show','4ef4080fc17f53f03393ac74e205220072360c0b:'+PREFIX+'exports/paving.json'],cwd=REPO))['matrix']
    assert json.loads((R/'exports/paving.json').read_text())['matrix']==target
    # Render an ownership mask through identical placements and opaque occlusion.
    masks={}
    for name,a in kit.items():
        mask=Image.new('RGBA',a.size,'white' if name=='paving' else 'black');mask.putalpha(a.getchannel('A'));masks[name]=mask
    layouts=json.loads((R/'layouts.json').read_text());results={}
    for name,w in [('gameplay',192),('story',256)]:
        file=f'mansion_{name}_preview_{w}x240.png';before=Image.open(io.BytesIO(old(file))).convert('RGB');after=Image.open(R/file).convert('RGB');assert after.size==(w,240)
        diff=ImageChops.difference(before,after);owner=render(layouts[name],masks)
        changed=[(x,y) for y in range(240) for x in range(w) if diff.getpixel((x,y))!=(0,0,0)]
        assert changed and all(owner.getpixel(p)==(255,255,255) for p in changed)
        board=Image.new('RGB',(w*2,260),'#080810');d=ImageDraw.Draw(board);board.paste(before,(0,20));board.paste(after,(w,20));d.text((4,4),'BEFORE FLOOR 01A',fill='#d4c4a8');d.text((w+4,4),'CLEANER PAVING',fill='#d4c4a8');board.save(R/f'{name}_floor_before_after.png')
        results[name]={'dimensions':[w,240],'changed_pixels':len(changed),'all_changes_on_visible_paving':True,'non_floor_pixels_unchanged':True,'sha256':hashlib.sha256((R/file).read_bytes()).hexdigest()}
    report={'status':'PASS','baseline':BASE,'asset_id':'v4-mansion-trans01-paving','revision_change':[5,6],'restored_pixel_revision':3,'other_15_canonical_assets_unchanged':True,'layouts_unchanged':True,'staging_unchanged':True,'scenes':results,'candidate_only':True}
    (R/'floor_correction_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':main()
