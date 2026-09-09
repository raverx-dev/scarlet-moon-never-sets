from pathlib import Path
from PIL import Image, ImageDraw
import json, statistics
ROOT=Path(__file__).parent
PAL=json.loads((ROOT/'palette.json').read_text())
FILES=['roof_tiles.json','roof_structures_a.json','roof_structures_b.json','gate_assets.json','mansion_ext_assets.json','roof_scarlet_moon.json']
A={}
for fn in FILES: A.update(json.loads((ROOT/fn).read_text())['assets'])
def rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))+(255,)
P={k:rgb(v) for k,v in PAL.items()}
def mat(rows,s=1):
 im=Image.new('RGBA',(len(rows[0])*s,len(rows)*s),(0,0,0,0)); q=im.load()
 for y,r in enumerate(rows):
  for x,ch in enumerate(r):
   if ch=='.': continue
   c=P[ch]
   for yy in range(s):
    for xx in range(s): q[x*s+xx,y*s+yy]=c
 return im
# atlas: exact matrices, nearest-neighbor 4x
names=list(A); cols=4; scale=4; cw=280; lh=18
rows=(len(names)+cols-1)//cols; atlas=Image.new('RGBA',(cols*cw,rows*100),(8,8,16,255)); d=ImageDraw.Draw(atlas)
for i,n in enumerate(names):
 x=(i%cols)*cw+8; y=(i//cols)*100+8; tile=mat(A[n],scale); atlas.alpha_composite(tile,(x,y+lh)); d.text((x,y),f'{n} {len(A[n][0])}x{len(A[n])}',fill=(255,240,206,255))
atlas=atlas.crop(atlas.getbbox()); atlas.save(ROOT/'stage3b_roof_atlas.png')
# Remilia boss readability proof: architecture/motion mass high and edge-weighted; lower-center survival lane subdued.
W,H=192,240; pf=Image.new('RGBA',(W,H),P['k']); d=ImageDraw.Draw(pf)
for y in range(H): d.line((0,y,W,y),fill=P['n'] if y<40 else P['d'] if y<80 else P['h'] if y<120 else P['k'])
pf.alpha_composite(mat(A['roof_scarlet_moon_64']),((W-64)//2,4))
for x,y,n in [(8,24,'mansion_ext_skyline_spires_a'),(40,28,'mansion_ext_skyline_spires_b'),(132,30,'mansion_ext_skyline_spires_a'),(152,24,'mansion_ext_skyline_spires_b')]: pf.alpha_composite(mat(A[n]),(x,y))
for x in range(24,168,16): pf.alpha_composite(mat(A['roof_battlement_straight']),(x,78))
for x in range(16,176,16): pf.alpha_composite(mat(A['roof_railing_straight']),(x,94))
for bx in (0,160):
 pf.alpha_composite(mat(A['roof_spire_base']),(bx+8,104)); pf.alpha_composite(mat(A['roof_spire_mid']),(bx+8,88)); pf.alpha_composite(mat(A['roof_spire_cap']),(bx+8,72)); pf.alpha_composite(mat(A['roof_window_gothic_tall']),(bx+8,120))
for x in (8,24,144,160): pf.alpha_composite(mat(A['gate_pillar']),(x,160))
for x in (24,40,56,120,136,152): pf.alpha_composite(mat(A['gate_fence_section']),(x,188))
for x in (56,72,88,104): pf.alpha_composite(mat(A['gate_bar_panel']),(x,144))
pf.alpha_composite(mat(A['gate_arch_top']),(72,128)); pf.alpha_composite(mat(A['roof_gargoyle_left']),(12,184)); pf.alpha_composite(mat(A['roof_gargoyle_right']),(164,184))
for x in (20,148): pf.alpha_composite(mat(A['roof_lantern_hanging']),(x,152))
for x in (0,16,176): pf.alpha_composite(mat(A['mansion_ext_wall_panel']),(x,208))
pf.alpha_composite(Image.new('RGBA',(96,84),(8,8,16,180)),(48,156))
for x in range(56,136,16): pf.alpha_composite(mat(A['roof_cobble_a' if (x//16)%2==0 else 'roof_cobble_b']),(x,224))
for x in (32,144): pf.alpha_composite(mat(A['roof_lantern_wall']),(x,204))
pf.save(ROOT/'stage3b_roof_playfield_native.png'); pf.resize((768,960),Image.Resampling.NEAREST).save(ROOT/'stage3b_roof_playfield_preview.png')
def lum(c): return .2126*c[0]+.7152*c[1]+.0722*c[2]
px=pf.load(); center=[lum(px[x,y]) for y in range(156,240) for x in range(48,144)]; upper=[lum(px[x,y]) for y in range(132) for x in range(192)]; edges=[lum(px[x,y]) for y in range(144,240) for x in list(range(48))+list(range(144,192))]
print(f'upper={statistics.mean(upper):.2f} center={statistics.mean(center):.2f} edges={statistics.mean(edges):.2f}')
assert statistics.mean(center)<statistics.mean(edges)<statistics.mean(upper)
