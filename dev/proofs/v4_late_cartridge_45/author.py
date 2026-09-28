"""LC45 native authoring inputs. Tile strings are authored at 1x; no resampling.
This produces review inputs only. Canonical publication uses RoboPixel D6.
"""
from pathlib import Path
import json,hashlib,struct
from PIL import Image
P=Path(__file__).parent
BG=[['#10121e','#232637','#48475c','#898299'],['#10121e','#301b2b','#6c293f','#c56879'],['#10121e','#392d30','#846349','#d4b185'],['#10121e','#203447','#426b81','#9bbbc5']]
SP=[['#201b2a','#d64053','#fff0da'],['#201b2a','#987451','#fff0da'],['#201b2a','#58abc2','#fff0da'],['#201b2a','#de718e','#fff0da']]
assets={}; specs={}
def rgba(h):return tuple(bytes.fromhex(h[1:]))+(255,)
def add(name,rows,pool,idx,kind='metatile'):
 assert len(set(map(len,rows)))==1,(name,list(map(len,rows)))
 pal={'.':(0,0,0,0)}
 colors=(BG if pool=='bg' else SP)[idx]
 pal.update({str(i):rgba(c) for i,c in enumerate(colors)})
 im=Image.new('RGBA',(len(rows[0]),len(rows)));im.putdata([pal[c] for r in rows for c in r]);assets[name]=im
 specs[name]={'asset_id':'v4-lc45-'+name,'width':im.width,'height':im.height,'rows':rows,'pool':pool,'subpalette':idx,'kind':kind,'palette':pal}
 return name
def rows(s):return s.strip().split()
def meta(name,a,b,c,d,p=0):
 return add(name,[x+y for x,y in zip(rows(a),rows(b))]+[x+y for x,y in zip(rows(c),rows(d))],'bg',p)
Z='00000000 '*8
# Each declared unit below is an 8x8 construction atom.
wallA='11111111 11111111 11111111 11111111 11111111 11111111 11111110 00000000'
wallB='11111111 11111111 11111111 11111111 11111111 11111111 01111111 00000000'
meta('wall',wallA,wallB,wallB,wallA)
meta('wall-recess',Z,Z,wallA,wallB)
meta('cornice','33333333 22222222 00000000 22222222 12111211 12111211 11111111 00000000','33333333 22222222 00000000 21121112 21121112 11111111 11111111 00000000',wallA,wallB)
meta('pier-cap','00000000 33333333 22222222 03333330 00222200 00022000 00133100 01233210','00000000 33333333 22222222 03333330 00222200 00022000 00133100 01233210','01233210 01233210 01233210 01233210 01233210 01233210 01233210 01233210','01233210 01233210 01233210 01233210 01233210 01233210 01233210 01233210')
shaft='01233210 '*8
meta('pier',shaft,shaft,shaft,shaft)
meta('pier-foot',shaft,shaft,'01233210 01233210 01233210 12333321 02222220 23333332 22222222 00000000','01233210 01233210 01233210 12333321 02222220 23333332 22222222 00000000')
meta('floor','11111111 11111111 11111111 11111111 11111111 11111111 11111111 11111111','11111111 '*8,'11111111 '*8,'11111111 11111111 11111111 11111111 11111111 11111111 11111111 11111111')
meta('floor-joint','11111111 11111111 11111111 11111111 11111111 11111111 11111111 11111111','11111111 '*8,'11111111 11111111 11111111 11111111 11111111 11111111 11111111 11111110','11111111 11111111 11111111 11111111 11111111 11111111 11111111 00001111')
meta('floor-edge','00000001 '*8,'11111111 '*8,'00000001 '*8,'11111111 '*8)
meta('carpet','11111111 '*8,'11111111 '*8,'11111111 '*8,'11111111 '*8,p=1)
meta('carpet-left','00122111 00123111 00122111 00122111 00122111 00123111 00122111 00122111','11111111 '*8,'00122111 00122111 00122111 00123111 00122111 00122111 00122111 00122111','11111111 '*8,p=1)
add('carpet-right',[r[::-1] for r in specs['carpet-left']['rows']],'bg',1)
meta('carpet-end','22222222 23323323 22222222 11111111 11111111 11111111 11111111 11111111','22222222 23323323 22222222 11111111 11111111 11111111 11111111 11111111','11111111 '*8,'11111111 '*8,p=1)
meta('steps','22222222 33333333 00000000 11111111 11111111 22222222 33333333 00000000','22222222 33333333 00000000 11111111 11111111 22222222 33333333 00000000','11111111 11111111 11111111 22222222 33333333 00000000 11111111 11111111','11111111 11111111 11111111 22222222 33333333 00000000 11111111 11111111')
meta('carpet-steps','22222222 33333333 00000000 11111111 11111111 22222222 33333333 00000000','22222222 33333333 00000000 11111111 11111111 22222222 33333333 00000000','11111111 11111111 11111111 22222222 33333333 00000000 11111111 11111111','11111111 11111111 11111111 22222222 33333333 00000000 11111111 11111111',p=1)
# Gothic window: two pointed lancets, coarse glass divisions; blue bank.
meta('window-head','00000000 00000000 00000002 00000023 00000231 00002311 00023112 00231122','00000000 00000000 20000000 32000000 13200000 11320000 21132000 22113200','00231122 02311122 02312112 02312211 02312112 02311122 02311122 02311122','22113200 22111320 21121320 11221320 21121320 22111320 22111320 22111320',p=3)
meta('window-body','02311122 02311122 02312112 02312211 02312112 02311122 02311122 02311122','22111320 22111320 21121320 11221320 21121320 22111320 22111320 22111320','02322222 02333333 02311122 02311122 02311122 02311122 02311122 02311122','22222320 33333320 22111320 22111320 22111320 22111320 22111320 22111320',p=3)
meta('window-foot','02311122 '*6+'02333333 02222222','22111320 '*6+'33333320 22222220','00000000 22222222 33333333 22222222 00111111 00111111 00111111 00000000','00000000 22222222 33333333 22222222 11111100 11111100 11111100 00000000',p=3)
meta('hanging-top','00000000 33333333 22222222 00322222 00322222 00322122 00322122 00322122','00000000 33333333 22222222 22222300 22222300 22122300 22122300 22122300','00322122 00321212 00322122 00322222 00322222 00322222 00322122 00322122','22122300 21212300 22122300 22222300 22222300 22222300 22122300 22122300',p=1)
meta('hanging-end','00322122 00322122 00322122 00322222 00322222 00322222 00322222 00322222','22122300 22122300 22122300 22222300 22222300 22222300 22222300 22222300','00322222 00322222 00322222 00032222 00003222 00000322 00000032 00000003','22222300 22222300 22222300 22223000 22230000 22300000 23000000 30000000',p=1)
# 32x32 rose, four native 16x16 neighborhoods share BG1.
q=rows('''0000000000000000
0000000000002222
0000000002233333
0000000223300000
0000002330012221
0000023300123332
0000233000123321
0002330120012210
0023301232011100
0023012333200000
0230012332100122
0230122321001233
2330121210012332
2300120100123321
2300000001222210
2300122212332100''')
rose=[r+r[::-1] for r in q];rose+=rose[::-1]
for yy in range(2):
 for xx in range(2):add(f'rose-{yy}{xx}',[r[xx*16:xx*16+16] for r in rose[yy*16:yy*16+16]],'bg',1)
# arch shoulders around sanctuary / shadows; stepped native masses
meta('arch-left','00000000 00000000 00000000 00000000 00000000 00000000 00000002 00000023','00002233 00223322 02332210 23321000 33210000 32100000 21000000 10000000','00000233 00002332 00023321 00233210 02332100 02321000 23321000 23210000',Z)
add('arch-right',[r[::-1] for r in specs['arch-left']['rows']],'bg',0)
meta('door','00112110 00112110 00112110 00112110 00112110 00112110 00112110 00112110','00112110 00112110 00112110 00112110 00112110 00112110 00112110 00112110','00112110 00112110 00112110 00122110 00133110 00122110 00112110 00112110','00112110 00112110 00112110 00122110 00133110 00122110 00112110 00112110',p=2)
# Golden sconce remains a tile, no blurred glow.
meta('sconce','00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000','00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000','00000030 00000330 00000320 00000220 00000330 00000220 00000022 00000012','03000000 03300000 02300000 02200000 03300000 02200000 22000000 21000000',p=2)
# Reimu authored directly as 16x24, one 3-visible-color subpalette per 8x8 cell.
neutral=rows('''.21110....01112.
.211110..011112.
..211111111112..
..211110011112..
...2110000112...
...0000000000...
...0000000000...
...0000000000...
...0000000000...
..220000000022..
..221000000122..
.22210000001222.
.22110000001122.
..211100001112..
...0111111110...
...0112112110...
...0111111110...
..011111111110..
..011101101110..
.01111011011110.
.02222222222220.
..022022220220..
....20....02....
...0110..0110...''')
fire=rows('''.21110....01112.
.211110..011112.
..211111111112..
..211110011112..
...2110000112...
...0000000000...
..200000000002..
.22200000000222.
2221000000001222
2211000000001122
.21100000000112.
..110000000011..
...1000000001...
...1100000011...
...0111111110...
...0112112110...
...0111111110...
..011111111110..
.01111011011110.
.01110111101110.
0222222222222220
.02202222220220.
....20....02....
...0110..0110...''')
add('reimu-neutral',neutral,'sp',0,'body');add('reimu-fire',fire,'sp',0,'body')
add('gohei-normal',rows('''.........1
........11
.......11.
......11..
.....112..
....11222.
...11.22..
..11.222..
.11...222.
11...222..
......22..
.....222..
......2...
..........'''),'sp',1,'prop')
add('gohei-fire',rows('''..........11
........111.
......111.2.
....111..222
..111...222.
111......22.
........222.
.......222..
........22..
.......222..
........2...
............
............
............'''),'sp',1,'prop')
add('bullet-pink',rows('''..000..
.01110.
0122110
0122110
0111110
.01110.
..000..'''),'sp',3,'bullet')
add('bullet-blue',specs['bullet-pink']['rows'],'sp',2,'bullet')
add('shot',rows('''22222
21112
21112
21112
21112
21112
21112
21112
21112
22222'''),'sp',0,'effect')
add('bat-familiar',rows('''0.........0
00..000..00
01002220010
.011222110.
..0111110..
...01210...
....000....'''),'sp',3,'actor')
# Fixed 12x15 metatile plan. Asymmetry is restrained to floor joint variants.
plan=[
 ['cornice']*12,
 ['pier-cap','hanging-top','pier-cap','wall','arch-left','rose-00','rose-01','arch-right','wall','pier-cap','hanging-top','pier-cap'],
 ['pier','hanging-end','pier','window-head','wall','rose-10','rose-11','wall','window-head','pier','hanging-end','pier'],
 ['pier','wall','pier','window-body','arch-left','door','door','arch-right','window-body','pier','wall','pier'],
 ['pier','window-head','pier','window-foot','pier-cap','door','door','pier-cap','window-foot','pier','window-head','pier'],
 ['pier','window-body','pier','sconce','pier-foot','carpet-steps','carpet-steps','pier-foot','sconce','pier','window-body','pier'],
 ['pier','window-foot','pier','steps','steps','carpet-steps','carpet-steps','steps','steps','pier','window-foot','pier'],
 ['pier-foot','floor','pier-foot','floor','carpet-left','carpet','carpet','carpet-right','floor','pier-foot','floor','pier-foot'],
]
for y in range(8,15):
 plan.append(['pier' if y<12 else 'pier-foot' if y==12 else 'floor-edge','floor','floor-joint' if y in [9,13] else 'floor','floor','carpet-left','carpet','carpet','carpet-right','floor','floor-joint' if y in [11] else 'floor','floor','pier' if y<12 else 'pier-foot' if y==12 else 'floor-edge'])
# Preserve HUD geometry pixel-for-pixel; only map colors within each 16x16 neighborhood.
src=Image.frombytes('RGBA',(256,240),(P/'inputs/v4-neutral.rgba').read_bytes()).crop((192,0,256,240))
hud=Image.new('RGBA',src.size);hmap=[]
for cy in range(15):
 line=[]
 for cx in range(4):
  # Shared stone palette with cyan label neighborhoods, gold power/stage neighborhoods.
  pi=3 if cy in [3,4,5,6,9] else 2 if cy in [8,11,12,13] else 0
  line.append(pi)
  palette=[rgba(c) for c in BG[pi]]
  for y in range(cy*16,(cy+1)*16):
   for x in range(cx*16,(cx+1)*16):
    r,g,b,a=src.getpixel((x,y));lum=.2126*r+.7152*g+.0722*b
    j=0 if lum<30 else 1 if lum<65 else 2 if lum<135 else 3
    hud.putpixel((x,y),palette[j])
 hmap.append(line)
# HUD uses a union palette; explicit per-neighborhood assignments live in construction.json.
allbg=list(dict.fromkeys(c for p in BG for c in p));tokens='0123456789ABC';inv={rgba(c):tokens[i] for i,c in enumerate(allbg)}
assets['hud']=hud;specs['hud']={'asset_id':'v4-lc45-hud','width':64,'height':240,'rows':[''.join(inv[hud.getpixel((x,y))] for x in range(64)) for y in range(240)],'pool':'bg','subpalette':'mapped','kind':'hud','palette':{'.':(0,0,0,0),**{tokens[i]:rgba(c) for i,c in enumerate(allbg)}}}
common=[{'asset':n,'x':x*16,'y':y*16} for y,row in enumerate(plan) for x,n in enumerate(row)]
common += [{'asset':'hud','x':192,'y':0},{'asset':'bat-familiar','x':51,'y':61},{'asset':'bat-familiar','x':131,'y':61}]
for x,y in [(40,112),(64,128),(88,144),(112,144),(136,128),(160,112),(48,168),(144,168)]:common.append({'asset':'bullet-pink' if x<96 else 'bullet-blue','x':x-3,'y':y-3})
scenes=[]
for state in ['neutral','fire']:
 placements=list(common)
 if state=='fire':placements += [{'asset':'shot','x':94,'y':157},{'asset':'shot','x':94,'y':133}]
 # Body at source center (96,200), gohei source offsets normal (8,-5), fire (9,-4).
 placements += [{'asset':'gohei-'+('normal' if state=='neutral' else 'fire'),'x':99,'y':188 if state=='neutral' else 189},{'asset':'reimu-'+state,'x':88,'y':188}]
 canvas=Image.new('RGBA',(256,240))
 for p in placements:canvas.alpha_composite(assets[p['asset']],(p['x'],p['y']))
 canvas.save(P/(state+'_working.png'));canvas.resize((768,720),Image.Resampling.NEAREST).save(P/(state+'_3x_working.png'))
 rh=hashlib.sha256(b'robopixel-render-v1\0'+struct.pack('>II',256,240)+canvas.tobytes()).hexdigest()
 scenes.append({'name':state,'width':256,'height':240,'render_hash':rh,'placements':placements,'current_source':'v3-'+state,'reference_source':'v4-'+state})
used={p['asset'] for s in scenes for p in s['placements']};specs={k:v for k,v in specs.items() if k in used}
for n,s in specs.items():s['render_hash']=hashlib.sha256(b'robopixel-render-v1\0'+struct.pack('>II',s['width'],s['height'])+assets[n].tobytes()).hexdigest()
(P/'authoring.json').write_text(json.dumps(specs,indent=2)+'\n');(P/'composition.json').write_text(json.dumps(scenes,indent=2)+'\n')
(P/'construction.json').write_text(json.dumps({'background_palettes':BG,'sprite_palettes':SP,'metatile_map':plan,'hud_attribute_map':hmap,'body_cells':{'neutral':[[0,0],[0,0],[0,0]],'fire':[[0,0],[0,0],[0,0]]},'quiet_region':[48,128,96,112],'banks':['mansion-resident'],'palette_changes':[],'exceptions':[]},indent=2)+'\n')
print('Assets',len(specs),'scene hashes',[(s['name'],s['render_hash']) for s in scenes])
