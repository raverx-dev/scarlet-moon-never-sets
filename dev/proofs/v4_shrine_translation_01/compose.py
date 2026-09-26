#!/usr/bin/env python3
"""Compose exact canonical PNGs using independent integer-coordinate layouts.

python compose.py          rebuild presentation artifacts
python compose.py --check  reproduce and verify in memory, without writing
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib,sys,subprocess
ROOT=Path(__file__).resolve().parent
BASE='d7054d2b9b111ff711f44cc3ee5b71268aca6ed8'
CHECK='--check' in sys.argv
def digest(b):return hashlib.sha256(b).hexdigest()
def read(f):return json.loads((ROOT/f).read_text())
def rgba_from_export(e):
 m=e['matrix'];pal={c:(0,0,0,0) if v.get('transparent') else tuple(bytes.fromhex(v['hex'][1:]))+(255,) for c,v in m['symbols'].items()}
 im=Image.new('RGBA',(m['width'],m['height']));im.putdata([pal[c] for r in m['rows'] for c in r]);return im
def same(a,b):return a.size==b.size and a.convert('RGBA').tobytes()==b.convert('RGBA').tobytes()
def compose(mode,donation=True):
 layout=read(mode+'_layout.json');im=Image.new('RGBA',(layout['width'],layout['height']))
 for p in layout['placements']:
  if not donation and p['asset'].startswith('donation-box'):continue
  assert type(p['x']) is int and type(p['y']) is int
  im.alpha_composite(Image.open(ROOT/'assets'/(p['asset']+'.png')).convert('RGBA'),(p['x'],p['y']))
 return im
def write_or_check(name,im):
 if CHECK:assert same(im,Image.open(ROOT/name)),name+' differs'
 else:im.save(ROOT/name)
def font(size):
 try:return ImageFont.truetype('DejaVuSans.ttf',size)
 except OSError:return ImageFont.load_default()
def atlas(items):
 names=[i['name'] for i in items if i['name'].endswith('-night')]
 heights=[max(Image.open(ROOT/'assets'/(n+'.png')).height,Image.open(ROOT/'assets'/(n.replace('-night','-morning')+'.png')).height)*2+48 for n in names]
 im=Image.new('RGB',(1064,sum(heights)+48),'#131726');d=ImageDraw.Draw(im)
 d.text((12,10),'SHRINE CANONICAL KIT / ALL 22 ASSETS / REVISION 2 / 2x',font=font(20),fill='#eee5d4');y=48
 for n,h in zip(names,heights):
  for col,mode in enumerate(['night','morning']):
   key=n.replace('-night','-'+mode);q=Image.open(ROOT/'assets'/(key+'.png')).convert('RGBA');q=q.resize((q.width*2,q.height*2),Image.Resampling.NEAREST)
   x=12+col*532;d.text((x,y),key+' / r2',font=font(16),fill='#e1c995');im.paste(q,(x,y+28),q)
  y+=h
 return im
def comparison(mode,scene):
 im=Image.new('RGB',(1552,548),'#101421');d=ImageDraw.Draw(im)
 panes=[('CURRENT V4 / SOURCE RENDER',Image.open(ROOT/'current'/('v4_'+mode+'.png')),'nearest'),('OWNER REFERENCE / NOT PRODUCTION',Image.open(ROOT/'references'/(mode+'.png')),'fit'),('ROBO PIXEL CANDIDATE / 256 x 240',scene,'nearest')]
 for j,(title,q,kind) in enumerate(panes):
  x=j*520;d.text((x+8,12),title,font=font(18),fill='#efddb9')
  if kind=='fit':q=q.copy();q.thumbnail((512,480),Image.Resampling.LANCZOS)
  else:q=q.resize((512,480),Image.Resampling.NEAREST)
  im.paste(q.convert('RGB'),(x+4+(512-q.width)//2,44+(480-q.height)//2))
 d.text((8,527),'Static art proof. Current = original drawing functions in headless Canvas2D; no runtime integration.',font=font(14),fill='#b6c0d0')
 return im
def verify():
 items=read('asset_manifest.json');grids=read('authoring/grids.json');report={'status':'PASS','base':BASE,'canonical_assets':len(items),'assets':[],'scenes':{},'references':{},'protected_files_unchanged':False}
 for a in items:
  raw=(ROOT/a['png']).read_bytes();png=Image.open(ROOT/a['png']).convert('RGBA');exp=read(a['export']);rec=read('receipts/'+a['name']+'.json')
  assert digest(raw)==a['png_sha256']
  assert a['revision']==a['description']['current_revision']==exp['revision']==rec['paste']['receipt']['new_revision']==2
  assert a['revision_hash']==a['description']['current_revision_hash']==exp['revision_hash']==rec['paste']['receipt']['new_revision_hash']
  assert same(png,rgba_from_export(exp)),a['name']+' export pixels differ'
  assert exp['matrix']['rows']==grids[a['name']]['rows'],a['name']+' authoring mismatch'
  assert exp['round_trip']['cel_hash'] is True
  report['assets'].append({'asset_id':a['asset_id'],'revision':2,'revision_hash':a['revision_hash'],'png_sha256':a['png_sha256'],'export_png_differing_pixels':0,'authoring_rows_exact':True})
 recovered={a['asset_id']:a for a in read('recovery_inventory.json')}
 assert len(recovered)==22
 for a in items:
  assert recovered[a['asset_id']]['current_revision']==a['revision']
  assert recovered[a['asset_id']]['current_revision_hash']==a['revision_hash']
 report['recovered_live_inventory_matches']=True
 for mode in ['night','morning']:
  scene=compose(mode);assert scene.size==(256,240);assert scene.getextrema()[3]==(255,255)
  assert same(scene,compose(mode));write_or_check(mode+'_native.png',scene);write_or_check(mode+'_3x.png',scene.resize((768,720),Image.Resampling.NEAREST));write_or_check(mode+'_comparison.png',comparison(mode,scene))
  report['scenes'][mode]={'size':[256,240],'rgba_sha256':digest(scene.tobytes()),'deterministic_differing_pixels':0,'opaque':True,'layout':mode+'_layout.json'}
 for mode,expected in [('night','2fa833ed6c3ebb2fca995d66e70e8b59a7ab88cefb761cc0e301f99edbb7e769'),('morning','fce5623f68b48b5ea89daa7209f64429d1b872fbb4fd44c99c47297dd5e94471')]:
  p=ROOT/'references'/(mode+'.png');assert digest(p.read_bytes())==expected;assert Image.open(p).size==(1448,1086);report['references'][mode]={'sha256':expected,'size':[1448,1086]}
 write_or_check('asset_atlas.png',atlas(items))
 assert same(compose('morning',donation=False),Image.open(ROOT/'witnesses/morning_without_box.png'))
 for name in ['intro','ending']:
  im=Image.open(ROOT/'witnesses'/(name+'_dialogue_native.png'));assert im.size==(256,240)
  assert same(im.resize((768,720),Image.Resampling.NEAREST),Image.open(ROOT/'witnesses'/(name+'_dialogue_3x.png')))
 report['witness_dimensions_and_nearest_neighbor']='PASS'
 repo=ROOT.parents[2];changed=subprocess.check_output(['git','diff',BASE,'--name-only'],cwd=repo,text=True).splitlines()
 assert all(p.startswith('dev/proofs/v4_shrine_translation_01/') for p in changed),changed
 tracked=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE],cwd=repo,text=True).splitlines()
 for p in tracked:
  assert (repo/p).read_bytes()==subprocess.check_output(['git','show',BASE+':'+p],cwd=repo),p
 report['protected_files_unchanged']=True;report['base_tracked_files_verified']=len(tracked)
 report['artistic_acceptance']='OWNER REVIEW REQUIRED; technical checks do not confer acceptance'
 if CHECK and (ROOT/'manifest.json').exists():
  for file,sha in read('manifest.json')['proof_file_sha256'].items():assert digest((ROOT/file).read_bytes())==sha,file+' manifest mismatch'
 if not CHECK:(ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k not in ['assets','references']},indent=2))
if __name__=='__main__':verify()
