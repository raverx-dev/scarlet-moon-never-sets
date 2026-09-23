"""Explicit low-resolution pixel grids submitted to RoboPixel, never scene inputs.
No concept image is sampled, traced, resized or quantized by this authoring aid.
Pillow draws indexed, un-antialiased pixels; canonical read-back is mandatory.
"""
import json, math
from pathlib import Path
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parent
old=ROOT.parent/'v4_mansion_refinement_01/exports'
symbols=json.loads((old/'column.json').read_text())['matrix']['symbols']
colors={s:p['hex'] for s,p in symbols.items() if 'hex' in p}
colors.update(D='#260b1c',E='#490e28',F='#84233e',G='#ca4963',H='#97764f',I='#ffd19a',J='#111421')
tokens='.'+''.join(colors)
palette={'palette_id':'v4-mansion-translation-01','version':1,'entries':[{'index':i,'color_id':'transparent' if s=='.' else 'tone-'+s.lower(),'text_token':s,'adapter_symbols':{'scarlet-moon-js':s},'rgba':[0,0,0,0] if s=='.' else list(bytes.fromhex(colors[s][1:]))+[255]} for i,s in enumerate(tokens)]}
A={}
def canvas(w,h,bg='.'):
    global im,d
    im=Image.new('L',(w,h),tokens.index(bg));d=ImageDraw.Draw(im)
def rect(box,c): d.rectangle(box,fill=tokens.index(c))
def line(points,c,width=1):d.line(points,fill=tokens.index(c),width=width)
def poly(points,c):d.polygon(points,fill=tokens.index(c))
def ell(box,c):d.ellipse(box,fill=tokens.index(c))
def save(name,role,kind='reusable'):
    A[name]={'asset_id':'v4-mansion-trans01-'+name,'width':im.width,'height':im.height,'rows':[''.join(tokens[im.getpixel((x,y))] for x in range(im.width)) for y in range(im.height)],'role':role,'kind':kind,'status':'created'}
# Circular stone tracery with eight separate glass lobes, quiet dark outer field.
canvas(56,56,'1')
for box,c in [((0,0,55,55),'2'),((1,1,54,54),'4'),((2,2,53,53),'3'),((4,4,51,51),'0'),((5,5,50,50),'5'),((6,6,49,49),'3'),((8,8,47,47),'0')]:ell(box,c)
for i in range(8):
    a=i*math.pi/4;cx=27.5+14*math.cos(a);cy=27.5+14*math.sin(a)
    pts=[]
    for u,v in [(0,-6),(4,-2),(4,3),(0,6),(-4,3),(-4,-2)]:
        pts.append((round(cx+u*math.cos(a)-v*math.sin(a)),round(cy+u*math.sin(a)+v*math.cos(a))))
    poly(pts,'F');ell((int(cx)-2,int(cy)-2,int(cx)+2,int(cy)+2),'G');rect((round(cx),round(cy)-3,round(cx)+1,round(cy)-2),'I')
    # Dark leading splits each lobe into actual stained-glass facets.
    ux,uy=math.cos(a),math.sin(a)
    line([(round(cx-4*ux),round(cy-4*uy)),(round(cx+4*ux),round(cy+4*uy))],'2')
    line([(round(cx+3*uy),round(cy-3*ux)),(round(cx-3*uy),round(cy+3*ux))],'E')
    # Small outer glass jewel, no smooth glow.
    x=round(27.5+20*math.cos(a+math.pi/8));y=round(27.5+20*math.sin(a+math.pi/8))
    poly([(x,y-2),(x+2,y),(x,y+2),(x-2,y)],'C')
ell((19,19,36,36),'0');ell((21,21,34,34),'H');ell((22,22,33,33),'F')
poly([(27,22),(30,27),(33,28),(28,33),(25,29),(22,27)],'G');rect((27,25,28,29),'I')
# Distinct carved outer keystones at cardinal axes.
for x,y in [(26,1),(26,51),(1,26),(51,26)]:rect((x,y,x+3,y+3),'5')
save('rose','Rose window and carved stone ring','focal')
# Tall single lancet; transparent surround allows placement within several bays.
canvas(16,48)
poly([(7,0),(15,12),(15,45),(0,45),(0,12)],'3')
line([(7,1),(1,12),(1,44)],'5');line([(8,1),(14,12),(14,44)],'4')
poly([(7,5),(11,13),(11,42),(4,42),(4,13)],'0')
for y in range(12,42):
    for x in range(5,11):
        im.putpixel((x,y),tokens.index('F' if ((x+y//4)%5)<3 else 'E'))
for y in (15,25,35):
    poly([(7,y-3),(10,y),(7,y+3),(5,y)],'G');rect((7,y-1,8,y),'C')
line([(7,6),(7,42)],'2');line([(4,22),(11,22)],'2');line([(4,32),(11,32)],'2')
rect((0,44,15,44),'5');rect((1,45,14,46),'3');rect((2,47,13,47),'0')
save('lancet','Narrow ruby stained-glass window')
# Large open arch surround: stair-stepped nested mouldings, stone joints.
canvas(48,80)
outer=[(23,0),(29,5),(35,11),(40,18),(44,27),(47,39),(47,79),(0,79),(0,39),(3,27),(7,18),(12,11),(18,5)]
poly(outer,'2')
for points,c in [([(2,78),(2,39),(5,27),(9,19),(14,12),(23,4),(32,12),(38,21),(43,34),(45,45),(45,78)],'4'), ([(4,78),(4,40),(7,28),(12,19),(17,13),(23,8),(29,13),(35,21),(40,34),(42,45),(42,78)],'5'), ([(7,79),(7,43),(10,32),(15,23),(23,14),(31,23),(36,33),(39,44),(39,79)],'0')]:
    line(points,c,2)
poly([(23,16),(30,24),(35,34),(38,45),(38,79),(9,79),(9,45),(12,34),(17,24)],'1')
for y in (46,60,73):
    line([(0,y),(6,y)],'3');line([(41,y),(47,y)],'1')
rect((20,4,25,8),'6');rect((21,9,24,12),'4')
save('arch','Pointed open arcade surround')
# Banner with clustered velvet folds, ochre piping, small bat crest.
canvas(20,56)
rect((0,0,19,2),'H');rect((2,1,17,1),'6')
poly([(3,3),(16,3),(16,44),(10,54),(3,44)],'H')
poly([(4,3),(15,3),(15,43),(10,51),(4,43)],'E')
rect((5,4,6,42),'F');rect((7,4,9,42),'E');rect((12,4,14,43),'D')
poly([(10,17),(12,21),(15,19),(14,26),(12,25),(10,29),(8,25),(5,26),(5,20),(8,22)],'H')
rect((9,19,10,25),'6');rect((9,30,10,36),'H')
save('banner','Velvet banner and bat crest')
# Large near pier with fluted shafts; small columns reuse/revise existing ID.
canvas(24,96)
for b,c in [((0,0,23,2),'3'),((1,1,22,1),'6'),((2,3,21,5),'5'),((3,6,20,8),'4'),((5,9,18,11),'3'),((6,12,17,78),'3')]:rect(b,c)
for x,c in [(6,'5'),(7,'6'),(8,'5'),(9,'4'),(10,'3'),(11,'5'),(12,'4'),(13,'3'),(14,'4'),(15,'3'),(16,'2'),(17,'0')]:rect((x,12,x,78),c)
for x in (4,10,16):
    rect((x,5,x+2,8),'3');rect((x,5,x+1,6),'6')
for y in (35,61):rect((6,y,17,y),'3');rect((7,y+1,8,y+1),'5')
for b,c in [((5,79,18,80),'5'),((4,81,19,83),'4'),((2,84,21,85),'6'),((2,86,21,88),'3'),((0,89,23,90),'5'),((0,91,23,95),'2')]:rect(b,c)
save('near-pier','Foreground pale clustered pier, cap/shaft/base')
# Crimson-carpeted stair flight: separate end piece, not a full scene.
canvas(64,24,'0')
for n in range(6):
    y=n*4;left=12-n*2;right=51+n*2
    rect((left,y,right,y),'5');rect((left,y+1,right,y+3),'2')
    rect((left+7,y,right-7,y),'G' if n==0 else 'F');rect((left+7,y+1,right-7,y+2),'E');rect((left+7,y+3,right-7,y+3),'D')
    rect((left,y,left+2,y),'6');rect((right-2,y,right,y),'4')
save('stairs','Widening six-step carpeted dais','focal')
canvas(24,18)
rect((0,0,23,0),'5');rect((0,1,23,2),'3');rect((0,3,23,3),'0')
for x in (2,10,18):
    rect((x,4,x+3,4),'4');rect((x+1,5,x+2,11),'3');rect((x,11,x+3,12),'5');rect((x-1,13,x+4,14),'2')
rect((0,15,23,15),'5');rect((0,16,23,17),'2')
save('balustrade','Gothic gallery balustrade')
canvas(12,28)
for x,y in ((1,5),(5,1),(9,5)):
    rect((x,y,x+1,y+3),'I');rect((x,y+4,x+1,y+7),'6');rect((x-1,y+8,x+2,y+8),'H')
line([(1,15),(1,17),(5,20),(10,17),(10,15)],'H');rect((5,10,6,26),'H');rect((4,25,7,26),'5');rect((2,27,9,27),'3')
save('candelabra','Three candle accents')
canvas(16,16,'D')
# Quiet woven velvet: just four low contrast pixel pairs.
for x,y in ((2,3),(11,7),(6,13)):rect((x,y,x+1,y),'E')
save('runner','Quiet dark crimson carpet field')
canvas(8,16,'D')
for x,c in [(0,'E'),(1,'H'),(2,'E'),(3,'D'),(6,'F'),(7,'E')]:rect((x,0,x,15),c)
for y in (2,10):
    poly([(4,y),(5,y+2),(4,y+4),(3,y+2)],'F')
save('runner-edge','Fine ochre piping and crimson border')
canvas(16,16)
for pts in [[(7,2),(8,5),(11,7),(8,8),(7,12),(6,8),(3,7),(6,6)],[(2,6),(3,7),(2,8),(1,7)],[(12,6),(13,7),(12,8),(11,7)]]:poly(pts,'E')
save('runner-motif','Sparse low contrast runner emblem')
# Reflective paving swatches: selected as native bands by the placement source.
canvas(32,16,'J')
rect((0,0,15,15),'1');rect((0,0,15,0),'2');rect((16,0,31,0),'7')
for y,x,w,c in [(3,5,3,'2'),(4,6,2,'3'),(5,5,3,'2'),(7,22,3,'7'),(8,23,2,'2')]:rect((x,y,x+w,y),c)
rect((15,0,15,15),'0');rect((31,0,31,15),'0');rect((0,15,31,15),'0')
save('paving','Two dark polished paving swatches, fragmented reflection')
# Revise existing pale column, keeping immutable canvas and palette.
e=json.loads((old/'column.json').read_text());rows=[list(r) for r in e['matrix']['rows']]
for y in range(64):
    for x in range(16):
        s=rows[y][x]
        if s=='5':rows[y][x]='6'
        elif s=='4':rows[y][x]='5'
for y in range(12,52):
    rows[y][5]='5';rows[y][6]='4';rows[y][8]='5';rows[y][9]='3'
A['column']={'asset_id':e['asset_id'],'width':16,'height':64,'rows':[''.join(r) for r in rows],'from_revision':e['revision'],'status':'revised','role':'Pale middle-distance column, stronger clustered shafts','kind':'reusable'}
for name in ('wall-masonry','trim-top','far-pier'):
    e=json.loads((old/(name+'.json')).read_text())
    A[name]={'asset_id':e['asset_id'],'width':e['matrix']['width'],'height':e['matrix']['height'],'revision':e['revision'],'status':'reused','role':{'wall-masonry':'Dark architectural infill','trim-top':'Cornice and gallery ledge','far-pier':'Small distant pier'}[name],'kind':'reusable'}
(ROOT/'authoring_inputs.json').write_text(json.dumps({'palette':palette,'assets':A},indent=2)+'\n')
print('Prepared',len(A),'bounded canonical asset selections')
