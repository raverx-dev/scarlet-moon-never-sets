"""#45 evidence supplement. Python 3 + Pillow. No canonical mutation/publication.
Without --package: artist-side verification/output in artist-review.
With --package: require and verify real D4 package before adding #45 evidence.
"""
from pathlib import Path
import argparse,json,hashlib,struct,math,html
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
args=argparse.ArgumentParser();args.add_argument('--package',type=Path);a=args.parse_args()
C=json.loads((P/'checkpoint.json').read_text());S=json.loads((P/'authoring.json').read_text());E=json.loads((P/'canonical_exports.json').read_text());K=json.loads((P/'construction.json').read_text())
O=a.package.resolve() if a.package else P/'artist-review'
if a.package:
 V=json.loads((O/'verification.json').read_text())
 assert V['checkpoint_sha256']==hashlib.sha256((O/'checkpoint.json').read_bytes()).hexdigest()
 assert json.loads((O/'checkpoint.json').read_text())==C
 for n,info in V['files'].items():assert hashlib.sha256((O/n).read_bytes()).hexdigest()==info['sha256'],n
else:O.mkdir(exist_ok=True)
def sha(b):return hashlib.sha256(b).hexdigest()
def rh(im):return sha(b'robopixel-render-v1\0'+struct.pack('>II',*im.size)+im.tobytes())
def savejson(n,d):(O/n).write_text(json.dumps(d,indent=2)+'\n')
def col(h):return tuple(bytes.fromhex(h[1:]))+(255,)
def image(e):
 m=e['matrix'];pal={k:(0,0,0,0) if v.get('transparent') else col(v['hex']) for k,v in m['symbols'].items()};im=Image.new('RGBA',(m['width'],m['height']));im.putdata([pal[t] for row in m['rows'] for t in row]);return im
ims={n:image(e) for n,e in E.items()};pins={x['name']:x for x in C['assets']};exports=json.loads((P/'export_hashes.json').read_text())['assets'];checks=[]
for n,im in ims.items():
 assert rh(im)==pins[n]['render_hash']==S[n]['render_hash'],n
 assert E[n]['revision_hash']==pins[n]['revision_hash'] and E[n]['revision']==pins[n]['revision']
 assert sha(json.dumps(E[n]['matrix'],sort_keys=True,separators=(',',':')).encode())==exports[n]['export_matrix_sha256']
 assert E[n]['matrix']['rows']==S[n]['rows'];assert set(im.getchannel('A').getdata())<={0,255}
 checks.append(n)
for f in C['sources']+C['source_files']:assert sha((ROOT/f['path']).read_bytes())==f['sha256'],f['path']
# All background and HUD 16x16 regions fit ONE of the same four pools.
bgpal=[{col(c) for c in p} for p in K['background_palettes']];sppal=[{col(c) for c in p}|{(0,0,0,0)} for p in K['sprite_palettes']]
for n,s in S.items():
 im=ims[n]
 if s['kind']=='metatile':assert set(im.getdata())<=bgpal[s['subpalette']],n
 elif s['kind']=='hud':
  for y,row in enumerate(K['hud_attribute_map']):
   for x,pi in enumerate(row):assert set(im.crop((x*16,y*16,x*16+16,y*16+16)).getdata())<=bgpal[pi]
 else:
  for y in range(0,im.height,8):
   for x in range(0,im.width,8):assert set(im.crop((x,y,min(x+8,im.width),min(y+8,im.height))).getdata())<=sppal[s['subpalette']],n
# Independently check source-preserving recolor, not merely whether a HUD fits its palette.
original=Image.open(P/'inputs/v4-neutral.png').convert('RGBA').crop((192,0,256,240));mapped=Image.new('RGBA',(64,240))
for y in range(240):
 for x in range(64):
  r,g,b,_=original.getpixel((x,y));lum=.2126*r+.7152*g+.0722*b;j=0 if lum<30 else 1 if lum<65 else 2 if lum<135 else 3
  mapped.putpixel((x,y),col(K['background_palettes'][K['hud_attribute_map'][y//16][x//16]][j]))
assert mapped.tobytes()==ims['hud'].tobytes(),'HUD changed beyond declared recolor'
# Exact tile vocabulary and 2x2 assembly for metatiles, sorted first-use order.
tiles=[];tile_lookup={};assembly={};meta_names=[n for n in S if S[n]['kind']=='metatile']
for n in meta_names:
 assembly[n]=[]
 for y in [0,8]:
  row=[]
  for x in [0,8]:
   im=ims[n].crop((x,y,x+8,y+8));key=rh(im)
   if key not in tile_lookup:tile_lookup[key]=len(tiles);tiles.append(im)
   row.append(tile_lookup[key])
  assembly[n].append(row)
 rebuilt=Image.new('RGBA',(16,16))
 for y in range(2):
  for x in range(2):rebuilt.paste(tiles[assembly[n][y][x]],(x*8,y*8))
 assert rebuilt.tobytes()==ims[n].tobytes()
atlas=Image.new('RGBA',(16*8,math.ceil(len(tiles)/16)*8))
for i,im in enumerate(tiles):atlas.paste(im,((i%16)*8,(i//16)*8))
atlas.save(O/'mansion_8x8_atlas.png');atlas.resize((atlas.width*3,atlas.height*3),Image.Resampling.NEAREST).save(O/'mansion_8x8_atlas_3x.png')
meta=Image.new('RGBA',(8*16,math.ceil(len(meta_names)/8)*16))
for i,n in enumerate(meta_names):meta.paste(ims[n],(i%8*16,i//8*16))
meta.save(O/'mansion_16x16_atlas.png')
# Plain background is reconstructed only from the canonical tile set.
bg=Image.new('RGBA',(192,240));tilemap=[]
for y,row in enumerate(K['metatile_map']):
 for x,n in enumerate(row):bg.paste(ims[n],(x*16,y*16))
 for suby in range(2):tilemap.append([t for n in row for t in assembly[n][suby]])
bg.save(O/'background_only.png')
mapim=bg.resize((576,720),Image.Resampling.NEAREST);d=ImageDraw.Draw(mapim)
for y in range(16):d.line((0,y*48,576,y*48),fill='#d4b185')
for x in range(13):d.line((x*48,0,x*48,720),fill='#d4b185')
for y,row in enumerate(K['metatile_map']):
 for x,n in enumerate(row):d.text((x*48+2,y*48+2),str(meta_names.index(n)),fill='white',stroke_width=1,stroke_fill='black')
mapim.save(O/'mansion_assembly_map.png')
savejson('tile_vocabulary.json',{'tile_size':[8,8],'tiles':[{'id':i,'render_hash':rh(im)} for i,im in enumerate(tiles)],'metatile_atlas_order':meta_names,'metatile_2x2_tile_ids':assembly,'mansion_24x30_tile_map':tilemap,'hud_attribute_map':K['hud_attribute_map']})
# Reimu cell/pose evidence and independent edge clipping inspection.
bodies=[];cell_data={}
for state in ['neutral','fire']:
 n='reimu-'+state;im=ims[n];assert im.size==(16,24);im.save(O/(n+'.png'));cells=[]
 board=im.resize((96,144),Image.Resampling.NEAREST);d=ImageDraw.Draw(board)
 for x in [0,48,95]:d.line((x,0,x,143),fill='#58abc2')
 for y in [0,48,96,143]:d.line((0,y,95,y),fill='#58abc2')
 board.save(O/(n+'-cells.png'))
 for y in range(3):
  for x in range(2):cells.append({'origin':[x*8,y*8],'subpalette':'SP0','render_hash':rh(im.crop((x*8,y*8,x*8+8,y*8+8)))})
 cell_data[state]=cells;bodies.append(im)
changed=sum(p!=q for p,q in zip(bodies[0].getdata(),bodies[1].getdata()));assert changed>40 and E['reimu-neutral']['matrix']['rows'][:6]==E['reimu-fire']['matrix']['rows'][:6]
savejson('reimu_construction.json',{'body_anchor':[8,12],'body_size':[16,24],'cell_size':[8,8],'cells':cell_data,'changed_body_pixels':changed,'shared_top_rows':6,'normal_gohei_size':[10,14],'fire_gohei_size':[12,14],'offsets':{'neutral':[8,-5],'fire':[9,-4]},'sprite_palettes':K['sprite_palettes']})
strip=Image.new('RGBA',(64,24));strip.paste(bodies[0],(0,0));strip.paste(bodies[1],(18,0));strip.paste(ims['gohei-normal'],(36,5));strip.paste(ims['gohei-fire'],(48,5));strip.save(O/'reimu_states_native.png');strip.resize((384,144),Image.Resampling.NEAREST).save(O/'reimu_states_inspection.png')
edge=Image.new('RGBA',(192*5,240*2))
for row,state in enumerate(['neutral','fire']):
 for column,(x,y) in enumerate([(96,120),(8,120),(184,120),(96,18),(96,230)]):
  frame=bg.copy();body=ims['reimu-'+state];prop=ims['gohei-'+('normal' if state=='neutral' else 'fire')];ox,oy=(8,-5) if state=='neutral' else (9,-4)
  frame.alpha_composite(prop,(x+ox-prop.width//2,y+oy-prop.height//2));frame.alpha_composite(body,(x-8,y-12));edge.paste(frame,(column*192,row*240))
edge.save(O/'edge_witnesses.png')
scene_checks=[]
for scene in C['scenes']:
 im=Image.new('RGBA',(256,240))
 for pl in scene['placements']:
  tile=ims[pl['asset']];assert pl['x']>=0 and pl['y']>=0 and pl['x']+tile.width<=256 and pl['y']+tile.height<=240
  im.alpha_composite(tile,(pl['x'],pl['y']))
 assert rh(im)==scene['render_hash'];n=scene['name']
 if a.package:assert Image.open(O/(n+'_native.png')).convert('RGBA').tobytes()==im.tobytes()
 else:im.save(O/(n+'_native.png'))
 im.resize((768,720),Image.Resampling.NEAREST).save(O/(n+'_inspection_3x.png'))
 board=Image.new('RGBA',(768,240));board.paste(Image.open(P/'inputs'/('v3-'+n+'.png')),(0,0));board.paste(Image.open(P/'inputs'/('v4-'+n+'.png')),(256,0));board.paste(im,(512,0));board.save(O/(n+'_comparison_labeled-order.png'))
 scene_checks.append({'name':n,'render_hash':rh(im),'opaque':set(im.getchannel('A').getdata())=={255}})
# 4x4 preview swatches, one row per global pool. Labels are review furniture only.
swatch=Image.new('RGB',(384,8*28),'#10121e');d=ImageDraw.Draw(swatch)
for i,pal in enumerate(K['background_palettes']+K['sprite_palettes']):
 label=('BG'+str(i)) if i<4 else ('SP'+str(i-4));d.text((2,i*28+8),label,fill='white')
 for j,c in enumerate(pal):d.rectangle((40+j*85,i*28+2,120+j*85,i*28+25),fill=c);d.text((43+j*85,i*28+8),c,fill='white' if sum(bytes.fromhex(c[1:]))<380 else 'black')
swatch.save(O/'global_palettes.png')
report={'phase':'local-D4-package-plus-supplement' if a.package else 'artist-side-only; local D4 packaging pending','selected_assets':len(ims),'canonical_render_matches':len(checks),'opaque_or_transparent_only':True,'background_live_subpalettes':4,'sprite_live_subpalettes':4,'hud_private_palette':False,'palette_swaps':[],'palette_exceptions':[],'mansion_metatiles':len(meta_names),'mansion_unique_8x8_tiles':len(tiles),'mansion_metatile_cells':180,'reimu_changed_pixels':changed,'hud_exact_declared_recolor':True,'scenes':scene_checks,'runtime_modified':False}
savejson('lc45_verification.json',report)
parts=['<!doctype html><html><head><meta charset="utf-8"><title>Scarlet Moon #45 — native proof</title><style>body{background:#12121c;color:#eee5d8;font:16px system-ui;margin:24px;line-height:1.5}img{image-rendering:pixelated;display:block}figure{margin:0 0 24px}h1{font-size:24px}h2{margin-top:36px}a{color:#9bcbe0}.scroll{overflow:auto}.row{display:flex;gap:20px;flex-wrap:wrap}pre{white-space:pre-wrap}table{border-collapse:collapse}td,th{padding:6px;border:1px solid #555}</style></head><body><h1>Scarlet Moon V4 · #45</h1><p>Owner review required. Read the native 256×240 frames first. Static faithful combat composition; no runtime integration or live QA claimed.</p><div class="row">']
for n in ['neutral','fire']:parts.append(f'<figure><h2>{n.title()} · 1× authoritative</h2><img width="256" height="240" src="{n}_native.png"></figure>')
parts.append('</div><h2>V3 → current V4 → Late-Cartridge</h2><p>All panes native 256×240. The first two are unmodified source inspection renders; right pane is canonical proof composition.</p>')
for n in ['neutral','fire']:parts.append(f'<h3>{n.title()}</h3><div class="scroll"><img width="768" height="240" src="{n}_comparison_labeled-order.png"></div>')
parts.append('<h2>Secondary nearest-neighbor inspection</h2>')
for n in ['neutral','fire']:parts.append(f'<details><summary>{n.title()} at 3×</summary><div class="scroll"><img width="768" height="720" src="{n}_inspection_3x.png"></div></details>')
parts.append('<h2>Reimu · neutral / fire / normal gohei / fire gohei</h2><img width="64" height="24" src="reimu_states_native.png"><img width="384" height="144" src="reimu_states_inspection.png"><p>Both bodies 16×24; six SP0 cells. Props SP1. Body and prop anchors stay separate.</p><div class="row"><img src="reimu-neutral-cells.png"><img src="reimu-fire-cells.png"></div><h2>Global frame palettes</h2><img src="global_palettes.png"><p>HUD shares background pools. All actors, bullets and effects share sprite pools. No swaps or extra palette exceptions.</p><h2>Mansion native tile vocabulary</h2><img src="mansion_8x8_atlas.png"><img src="mansion_8x8_atlas_3x.png"><p>8×8 IDs are row-major. Exact maps: <a href="tile_vocabulary.json">tile vocabulary</a>.</p><h3>16×16 units</h3><img src="mansion_16x16_atlas.png"><details><summary>Numbered assembly map (review overlay)</summary><img src="mansion_assembly_map.png"></details><h2>Background only</h2><img width="192" height="240" src="background_only.png"><details><summary>Center / left / right / top / bottom clipping witnesses; neutral above fire</summary><div class="scroll"><img src="edge_witnesses.png"></div></details>')
parts.append('<h2>Authority, palette ledger, construction and limits</h2><pre>'+html.escape((P/'evidence.md').read_text())+'</pre><h2>Mechanical artist/supplement checks</h2><pre>'+html.escape(json.dumps(report,indent=2))+'</pre><p><a href="lc45_verification.json">Supplement verification</a> · <a href="reimu_construction.json">Reimu map</a></p><p><strong>V4 LATE-CARTRIDGE PROOF — OWNER REVIEW REQUIRED</strong></p></body></html>')
(O/'lc45-review.html').write_text(''.join(parts))
print(json.dumps(report,indent=2))
