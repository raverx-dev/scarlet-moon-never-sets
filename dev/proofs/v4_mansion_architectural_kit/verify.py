"""Verify exact exported pixels, provenance, dimensions and proof-only boundary."""
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from PIL import Image
from compose import ROOT, assets, exports, layouts

BASE='d7054d2b9b111ff711f44cc3ee5b71268aca6ed8'
REPO=ROOT.parents[2]
manifest=json.loads((ROOT/'robopixel_manifest.json').read_text())
inputs=json.loads((ROOT/'authoring_inputs.json').read_text())
validation=json.loads((ROOT/'validation_reports.json').read_text())
result={'base':BASE,'canonical_assets':{},'previews':{},'protected_files':{},'boundaries':{}}
for asset in manifest['assets']:
    key=asset['key'];export=exports[key];im=assets[key]
    canonical=Image.open(ROOT/'canonical_previews'/f'{key}.png').convert('RGBA')
    assert im.size==canonical.size and im.tobytes()==canonical.tobytes(),key+' RGBA mismatch'
    assert inputs[key]['rows']==export['matrix']['rows'],key+' authoring grid mismatch'
    assert export['round_trip']['cel_hash'] is True
    assert export['revision_hash']==asset['revision_hash']
    status=asset['approval']['status']
    assert status['revision_hash']==asset['revision_hash'] and not status['approved']
    report=validation[key]['report']
    assert report['passed'] and report['revision_hash']==asset['revision_hash']
    result['canonical_assets'][key]={'revision':export['revision'],'revision_hash':export['revision_hash'],
       'rgba_equal':True,'source_rows_equal':True,'round_trip':True,'approved':False,
       'validation_passed':True,'findings':dict(Counter(f['disposition'] for f in report['findings']))}
for name,width in [('gameplay',192),('story',256)]:
    path=ROOT/f'mansion_{name}_preview_{width}x240.png';im=Image.open(path)
    assert im.size==(width,240)
    used=set(im.getdata())
    palette={tuple(bytes.fromhex(p['hex'][1:])) for e in exports.values() for p in e['matrix']['symbols'].values() if 'hex' in p}
    assert used <= palette, 'Unexpected interpolated color'
    result['previews'][name]={'dimensions':list(im.size),'colors':len(used),'palette_only':True,
         'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'asset_usage':dict(Counter(o['asset'] for o in layouts[name]['operations']))}
story=Image.open(ROOT/'mansion_story_preview_256x240.png')
game=Image.open(ROOT/'mansion_gameplay_preview_192x240.png')
assert story.crop((0,0,192,240)).tobytes()!=game.tobytes()
assert story.crop((32,0,224,240)).tobytes()!=game.tobytes()
for path in subprocess.check_output(['git','ls-tree','-r','--name-only',BASE],cwd=REPO,text=True).splitlines():
    old=subprocess.check_output(['git','show',BASE+':'+path],cwd=REPO)
    assert (REPO/path).read_bytes()==old,'Out-of-scope tracked file change: '+path
    if path.startswith('versions/') or path=='index.html':
        result['protected_files'][path]=hashlib.sha256(old).hexdigest()
result['boundaries']={'all_base_files_byte_identical':True,'distinct_compositions':True,
 'runtime_integration':False,'artwork_approval':False,'delivery_export':False,
 'note':'Local static proof verification only; no live combat/browser regression or hardware-exact NES compliance claimed.'}
(ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: 10 exact canonical RGBA/matrix exports; exact scene dimensions; palette-only pixels; all base files unchanged.')
