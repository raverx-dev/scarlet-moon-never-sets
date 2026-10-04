"""Guard the accepted gameplay and canonical kit while verifying story-only edits."""
import json,hashlib,subprocess
from PIL import Image
from compose import R,assets,render
import verify
BASE='37c2e611d469925fbc4e99e79bc84ddc7ed7934f';REPO=R.parents[2];PREFIX=str(R.relative_to(REPO))+'/'
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def old(path):return git('show',BASE+':'+PREFIX+path)
def digest(b):return hashlib.sha256(b).hexdigest()
def main():
    verify.main()
    layouts=json.loads((R/'layouts.json').read_text());prior=json.loads(old('layouts.json'))
    assert layouts['gameplay']==prior['gameplay']
    protected=['mansion_gameplay_preview_192x240.png','mansion_gameplay_3x.png','mansion_gameplay_scale.png','gameplay_comparison.png','robopixel_manifest.json','robopixel_readback.json','authoring_inputs.json','authoring_receipts.json','author_inputs.py','asset_inventory.md','asset_atlas.png','sprite_witnesses.json']
    for folder in ('exports','canonical_previews','references'):
        protected += [str(p.relative_to(R)) for p in (R/folder).rglob('*') if p.is_file()]
    for name in protected:assert (R/name).read_bytes()==old(name),name
    saved=['mansion_story_preview_256x240.png','mansion_story_3x.png','mansion_story_staging.png','story_comparison.png']
    for name in saved:assert (R/'story_before_correction'/name).read_bytes()==old(name)
    assert json.loads((R/'story_before_correction/story_layout.json').read_text())==prior['story']
    allowed={'README.md','build_layouts.py','layouts.json','compose.py','mansion_story_preview_256x240.png','mansion_story_3x.png','mansion_story_staging.png','story_comparison.png','verification.json','story_before_after.png','story_correction_provenance.json','story_correction_verification.json','verify_story_correction.py'}
    paths=git('diff','--name-only',BASE).decode().splitlines()+git('ls-files','--others','--exclude-standard').decode().splitlines()
    for p in paths:
        assert p.startswith(PREFIX),p
        local=p[len(PREFIX):];assert local in allowed or local.startswith('story_before_correction/'),p
    evidence=json.loads((R/'story_correction_provenance.json').read_text());used={o['asset'] for o in layouts['story']['operations']}
    assert used=={a['name'] for a in evidence['assets']}
    assert all(a['readback_matches_saved_export'] and a['round_trip']['cel_hash'] for a in evidence['assets'])
    im=Image.open(R/'mansion_story_preview_256x240.png').convert('RGB');assert im.size==(256,240)
    assert im.tobytes()==render(layouts['story'],assets()).tobytes()
    # The central red path must remain continuous from stair top to the foreground.
    red={tuple(bytes.fromhex(h)) for h in ('260b1c','490e28','84233e','ca4963')}
    assert all(im.getpixel((128,y)) in red for y in range(102,240))
    out={'status':'PASS','reviewed_head':BASE,'scope':'story only','gameplay_layout_unchanged':True,'gameplay_png_sha256':digest((R/'mansion_gameplay_preview_192x240.png').read_bytes()),'protected_translation_files_unchanged':len(protected),'previous_story_preserved_exactly':True,'story_dimensions':[256,240],'story_sha256':digest((R/'mansion_story_preview_256x240.png').read_bytes()),'canonical_story_assets_reconfirmed':len(used),'canonical_assets_changed':0,'story_reproduces_exactly':True,'continuous_crimson_path_stairs_to_runner':True,'file_scope':'PASS','dialogue_coverage':[4,174,248,62],'limits':'Static composition only; Owner visual review pending; no runtime or approval claim.'}
    (R/'story_correction_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
