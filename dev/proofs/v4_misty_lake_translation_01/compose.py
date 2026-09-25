"""Rebuild canonical proof with Pillow: python compose.py [--check].
No network, reference sampling, random numbers or author.py needed.
"""
import json,hashlib,base64,io,sys
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).parent
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):return json.loads((ROOT/p).read_text())
def matrix(m):
 im=Image.new('RGBA',(m['width'],m['height']))
 colors={s:((0,0,0,0) if d.get('transparent') else (*bytes.fromhex(d['hex'][1:]),255)) for s,d in m['symbols'].items()}
 im.putdata([colors[s] for row in m['rows'] for s in row]);return im
def build(check=False):
 exports=load('exports/canonical.json');renders=load('evidence/renders.json');layouts=load('layouts.json');assets={};outputs={};records=[]
 for name,e in exports.items():
  im=matrix(e['matrix']);r=renders[name];png=base64.b64decode(r['png_base64']);rp=Image.open(io.BytesIO(png)).convert('RGBA')
  assert im.size==rp.size and im.tobytes()==rp.tobytes(),f'Canonical render mismatch {name}'
  assert e['revision_hash']==r['revision_hash'] and e['revision']==r['revision'] and e['round_trip']['cel_hash']
  assets[name]=im;outputs['exports/'+name+'.png']=png
  records.append({'name':name,'asset_id':e['asset_id'],'revision':e['revision'],'revision_hash':e['revision_hash'],'render_hash':r['render_hash'],'rgba_sha256':sha(im.tobytes()),'png_sha256':sha(png),'width':im.width,'height':im.height})
 def encoded(im):
  b=io.BytesIO();im.save(b,format='PNG',compress_level=9);return b.getvalue()
 scenes={}
 for name,s in layouts.items():
  im=Image.new('RGBA',(s['width'],s['height']),s['background'])
  for p in s['placements']:
   a=assets[p['asset']]
   if p.get('flip_x'):a=a.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
   im.alpha_composite(a,(p['x'],p['y']))
  assert im.getextrema()[3]==(255,255)
  scenes[name]=im
  outputs[f'previews/{name}_{im.width}x240.png']=encoded(im)
  outputs[f'previews/{name}_3x.png']=encoded(im.resize((im.width*3,720),Image.Resampling.NEAREST))
 # Readable contact sheet: exact native assets placed without resampling.
 atlas=Image.new('RGBA',(600,790),'#101725');d=ImageDraw.Draw(atlas)
 x=y=12;rowh=0
 for n,im in assets.items():
  if x+max(im.width,160)>590:x=12;y+=rowh+30;rowh=0
  d.text((x,y),n,fill='#d4dded');atlas.alpha_composite(im,(x,y+17));x+=max(im.width,160)+18;rowh=max(rowh,im.height)
 atlas=atlas.crop((0,0,600,y+rowh+29));outputs['previews/atlas.png']=encoded(atlas)
 assert scenes['story'].crop((0,0,192,240)).tobytes()!=scenes['gameplay'].tobytes()
 # Exact static source reconstructions; these are not browser/live captures.
 source=load('evidence/source-matrices.json');baselines={}
 def source_image(rows,pal):
  out=Image.new('RGBA',(len(rows[0]),len(rows)))
  out.putdata([(*bytes.fromhex(pal[ch][1:]),255) if ch in pal else (0,0,0,0) for row in rows for ch in row]);return out
 for v,data in source['versions'].items():
  im=Image.new('RGBA',(256,240),data['background'])
  for p in data['placements']:im.alpha_composite(source_image(data['assets'][p['asset']],data['palette']),(p['x'],p['y']))
  baselines[v]=im
  for n,w in [('gameplay',192),('story',256)]:outputs[f'previews/baseline_{v}_{n}.png']=encoded(im.crop((0,0,w,240)))
 wit=source['witness'];pal=wit['palette']
 def actor(im,n,x,y):
  a=source_image(wit['sprites'][n],pal);im.alpha_composite(a,(x-a.width//2,y-a.height//2))
 gameplay=scenes['gameplay'].copy();actor(gameplay,'reimu',96,206);actor(gameplay,'cirno',96,45)
 for x,y in [(29,74),(161,95)]:actor(gameplay,'fairyIce',x,y)
 d=ImageDraw.Draw(gameplay)
 for x,y in [(57,100),(71,119),(87,133),(103,138),(121,129),(135,115),(143,99),(48,153),(72,162),(123,175),(150,161)]:
  d.ellipse((x-2,y-3,x+2,y+3),fill='#81d8ed',outline='#d6f4ff')
 for x,y in [(53,183),(142,187)]:d.rectangle((x-2,y-2,x+2,y+2),fill='#e83a51',outline='#fff0ce')
 story=scenes['story'].copy();actor(story,'reimuStoryA',56,124);actor(story,'cirno',196,108)
 story.alpha_composite(source_image(wit['dialogue'],pal),(4,174));story.alpha_composite(source_image(wit['sprites']['p_cirno'],pal),(9,181))
 d=ImageDraw.Draw(story);d.text((50,180),'CIRNO',fill='#81d8ed');d.text((50,194),'STOP RIGHT THERE!',fill='#fff0ce');d.text((228,226),'Z >',fill='#f5cb70')
 for n,im in [('gameplay',gameplay),('story',story)]:
  outputs[f'previews/{n}_witness.png']=encoded(im);outputs[f'previews/{n}_witness_3x.png']=encoded(im.resize((im.width*3,720),Image.Resampling.NEAREST))
 for n,w,ref in [('gameplay',192,'image-a-gameplay.png'),('story',256,'image-b-story.png')]:
  board=Image.new('RGBA',(w*4+40,275),'#101725');d=ImageDraw.Draw(board)
  panels=[('V3 source static',baselines['v3'].crop((0,0,w,240))),('V4 source static',baselines['v4'].crop((0,0,w,240))),('APPROVED REFERENCE',Image.open(ROOT/'references'/ref).convert('RGBA').resize((w,240),Image.Resampling.LANCZOS)),('CANONICAL CANDIDATE',scenes[n])]
  for i,(label,im) in enumerate(panels):
   x=8+i*(w+8);d.text((x,6),label,fill='#d4dded');board.alpha_composite(im,(x,26))
  outputs[f'previews/{n}_comparison.png']=encoded(board)
 for p,b in outputs.items():
  path=ROOT/p
  if check:assert path.read_bytes()==b,f'Reproduction mismatch: {p}'
  else:path.parent.mkdir(exist_ok=True,parents=True);path.write_bytes(b)
 report={'passed':True,'canonical_assets':len(assets),'canonical_export_render_differences':0,'all_adapter_roundtrips':True,'native_dimensions':{n:list(i.size) for n,i in scenes.items()},'independent_layouts':True,'baseline_v3_v4_lake_rgba_equal':baselines['v3'].tobytes()==baselines['v4'].tobytes(),'outputs':{p:sha(b) for p,b in outputs.items()},'assets':records}
 if check:
  assert load('verification.json')==report
  print('PASS: all canonical RGBA readbacks, adapter roundtrips, native dimensions and '+str(len(outputs))+' byte-exact reproduced PNGs')
 else:(ROOT/'verification.json').write_text(json.dumps(report,indent=2));print('Built '+str(len(outputs))+' exact proof outputs')
 return scenes
if __name__=='__main__':build('--check' in sys.argv)
