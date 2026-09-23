"""Art Development 01: native indexed asset revisions, never concept sampling.
Reads immutable accepted exports from Git. Outputs only RoboPixel grid inputs.
All silhouettes/canvas sizes and scene placements are retained.
"""
import json,math,subprocess
from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;REPO=R.parents[2];BASE='4ef4080fc17f53f03393ac74e205220072360c0b';PREFIX=str(R.relative_to(REPO))+'/'
def original(name):return json.loads(subprocess.check_output(['git','show',BASE+':'+PREFIX+name],cwd=REPO))
manifest=original('robopixel_manifest.json');initial=original('authoring_inputs.json');out={'source_commit':BASE,'palette':initial['palette'],'assets':{}}
for name,a in manifest['assets'].items():
    e=original('exports/'+name+'.json');out['assets'][name]={**{k:a[k] for k in ('asset_id','width','height','role','kind')},'status':'reused','revision':a['revision'],'from_revision':a['revision'],'rows':e['matrix']['rows'],'basis_revision_hash':a['revision_hash']}

def load(name,clear=False):
    global im,d,tokens,current
    current=name;e=original('exports/'+name+'.json');tokens=''.join(e['matrix']['symbols']);im=Image.new('L',(e['matrix']['width'],e['matrix']['height']),tokens.index('.'))
    if not clear:
        for y,row in enumerate(e['matrix']['rows']):
            for x,s in enumerate(row):im.putpixel((x,y),tokens.index(s))
    d=ImageDraw.Draw(im)
def dot(x,y,c):
    if 0<=x<im.width and 0<=y<im.height:im.putpixel((x,y),tokens.index(c))
def rect(b,c):d.rectangle(b,fill=tokens.index(c))
def line(p,c,w=1):d.line(p,fill=tokens.index(c),width=w)
def poly(p,c):d.polygon(p,fill=tokens.index(c))
def ell(b,c):d.ellipse(b,fill=tokens.index(c))
def save(note):
    a=out['assets'][current];a['rows']=[''.join(tokens[im.getpixel((x,y))] for x in range(im.width)) for y in range(im.height)];a['status']='revised';a['art_change']=note

def point(r,a):return (round(27.5+r*math.cos(a)),round(27.5+r*math.sin(a)))
load('rose',True);rect((0,0,55,55),'1')
# Recessed stone surround with an articulated archivolt and eight leaf-shaped lights.
for b,c in [((0,0,55,55),'2'),((1,1,54,54),'4'),((2,2,53,53),'5'),((3,3,52,52),'3'),((5,5,50,50),'0'),((6,6,49,49),'4'),((7,7,48,48),'2'),((8,8,47,47),'E')]:ell(b,c)
for i in range(16):
    a=i*math.pi/8
    line([point(24,a),point(26,a)],'1')
    dot(*point(25,a+0.08),'6' if i in (8,9,10,11,12,13) else '4')
# Eight narrow pointed petals are separated by stone spokes; facets are not discs.
for i in range(8):
    a=i*math.pi/4
    poly([point(8,a),point(12,a-.29),point(19,a-.21),point(22,a),point(19,a+.21),point(12,a+.29)],'5')
    poly([point(10,a),point(14,a-.13),point(19,a-.11),point(21,a),point(19,a+.11),point(14,a+.13)],'F')
    poly([point(12,a),point(17,a-.10),point(20,a),point(16,a)],'G')
    line([point(10,a),point(20,a)],'E')
    line([point(16,a-.11),point(16,a+.11)],'2')
    dot(*point(18,a-.07),'I');dot(*point(19,a),'C')
    # Secondary ruby lancet lights interlock between the principal petals.
    b=a+math.pi/8
    poly([point(10,b),point(15,b-.12),point(21,b-.09),point(23,b),point(21,b+.09),point(15,b+.12)],'0')
    poly([point(12,b),point(17,b-.08),point(21,b),point(17,b+.08)],'F')
    dot(*point(18,b),'G');dot(*point(20,b),'C')
    # Smaller quatrefoil lights fill each interstitial wedge.
    x,y=point(16,a+math.pi/8)
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):dot(x+dx,y+dy,'G')
    dot(x,y,'H')
    x,y=point(21,a+math.pi/8);dot(x,y,'C');dot(x+1,y,'F')
ell((20,20,35,35),'0');ell((22,22,33,33),'H');ell((23,23,32,32),'E')
poly([(27,23),(29,26),(32,27),(29,29),(28,32),(26,29),(23,28),(26,26)],'G');rect((27,26,28,28),'I')
# Small corner leafwork anchors the ring into the far wall.
for ox,oy in ((3,3),(48,3),(3,48),(48,48)):
    poly([(ox+2,oy),(ox+4,oy+2),(ox+2,oy+4),(ox,oy+2)],'3');dot(ox+2,oy+1,'5');dot(ox+2,oy+2,'4')
save('Eight pointed petal lights, radial stone tracery, interstitial quatrefoils, segmented archivolt and corner leaf carving')

load('arch')
# Carved crockets on the external rising edges, leaving the open bay unobstructed.
for x,y in ((4,26),(8,17),(13,10),(18,5)):
    for xx in (x,47-x):
        poly([(xx,y-2),(xx+1,y),(xx,y+2),(xx-2,y+1)],'4');dot(xx,y-1,'6');dot(xx+1,y+1,'2')
# Inner blind tracery joins lancet sill and shoulders, outside its glass footprint.
line([(10,72),(10,45),(13,34),(17,27)],'3');line([(37,72),(37,45),(34,34),(30,27)],'3')
for x in (10,36):
    rect((x,49,x+1,67),'2');rect((x,48,x+2,48),'4');rect((x,69,x+2,70),'4')
# Dado below the glass, subtle and structural.
rect((9,73,38,73),'4');rect((9,74,38,75),'0')
for x in (12,22,32):
    poly([(x+2,76),(x+4,78),(x,78)],'3');dot(x+2,77,'5')
for y in (42,55,68):
    line([(1,y),(5,y+1)],'2');dot(3,y-1,'5');line([(42,y),(46,y+1)],'0')
rect((22,5,24,7),'6');rect((23,8,24,10),'5')
save('Crocketed arch shoulders, nested mouldings, blind side tracery and a carved lower dado')

load('lancet')
# Genuine small glass facets with lead lines, a ruby/blue counterpoint and diamond lights.
for y in range(13,42):
    for x in range(5,11):
        dot(x,y,'F' if (y//5+x//3)%2 else 'E')
for y in (16,26,36):
    poly([(7,y-3),(10,y),(7,y+3),(5,y)],'G');dot(6,y,'I');dot(8,y+1,'C')
    dot(10,y+3,'8');dot(5,y+4,'7')
for y in (21,31,41):line([(4,y),(11,y)],'2')
line([(7,7),(7,42)],'3');dot(7,10,'6')
for y in (15,29,39):dot(1,y,'6');dot(14,y,'2')
rect((1,44,14,44),'6');rect((2,46,13,46),'4')
save('Leaded ruby diamond lights, small cool-glass facets and crisp stone jamb highlights')

load('banner')
# Woven side chains and broad folded velvet, not texture noise.
for y in range(5,43):
    dot(5,y,'F');dot(6,y,'G' if y%12 in (0,1,2) else 'F');dot(14,y,'D')
for y in (7,13,37,43):
    dot(4,y,'6');dot(15,y,'H')
# Embroidered crescent above the bat, hanging pendant below.
ell((8,7,12,11),'H');ell((10,6,13,10),'E')
line([(8,15),(10,13),(12,15)],'F')
for x,y,c in ((7,23,'6'),(12,23,'6'),(10,21,'I'),(8,32,'H'),(12,32,'H'),(9,38,'H'),(10,40,'6'),(10,48,'6')):dot(x,y,c)
line([(2,0),(17,0)],'5');dot(0,1,'6');dot(19,1,'6')
save('Layered velvet folds, embroidered crescent/bat identity, hem chain and pendant stitching')

load('near-pier')
# Acanthus capital, articulated collar, bundled shafts and beveled base panels.
for x in (4,10,16):
    line([(x,4),(x+2,5),(x+3,7),(x+1,9)],'2');line([(x,4),(x,6),(x+1,7)],'6');dot(x+2,8,'5')
for y in range(13,78):
    if y%16 in (0,1):dot(7,y,'5')
    dot(10,y,'2');dot(12,y,'5');dot(15,y,'4')
for y in (31,57):
    line([(6,y),(17,y)],'2');line([(6,y+1),(16,y+1)],'4');dot(7,y+1,'6')
for x in (3,9,15):
    rect((x,91,x+4,94),'1');line([(x,91),(x+4,91)],'4');dot(x+1,92,'3')
rect((3,85,20,85),'5');rect((5,80,18,80),'6')
save('Acanthus capitals, clustered flutes, shaft collars and inset plinth panels')

load('column')
for x in (3,6,9):
    dot(x,3,'6');dot(x+1,4,'3');dot(x+1,5,'5')
for y in range(12,52):
    dot(7,y,'2');dot(8,y,'5');dot(10,y,'4')
for y in (22,38):
    line([(4,y),(10,y)],'3');dot(5,y+1,'6');dot(8,y+1,'5')
rect((3,56,12,56),'5');rect((2,59,13,60),'2')
for x in (3,7,11):dot(x,59,'4')
save('Matched small acanthus capital, recessed fluting and carved base; accepted column dimensions retained')

load('balustrade')
# Small pierced Gothic rail: dark pointed apertures surrounded by carved stone.
for x in (2,10,18):
    line([(x,5),(x+2,7),(x+1,10)],'5');dot(x+2,5,'6');dot(x,9,'2')
for x in (6,14):
    line([(x-2,9),(x,5),(x+2,9)],'3');dot(x,6,'5')
rect((0,0,23,0),'6');rect((0,2,23,2),'4');rect((0,15,23,15),'4')
save('Pierced pointed stone rail with shaped balusters and a beveled handrail')

load('candelabra',True)
# Flame tapers, wax and separate scrolling arms; no blurry glow.
for x,y in ((1,5),(5,1),(9,5)):
    dot(x+1,y,'G');dot(x,y+1,'I');dot(x+1,y+1,'I');dot(x,y+2,'6')
    rect((x,y+3,x+1,y+7),'5');rect((x,y+3,x,y+6),'I');rect((x-1,y+8,x+2,y+8),'H');dot(x,y+9,'6')
line([(1,15),(1,18),(3,20),(5,20)],'H');line([(10,15),(10,18),(8,20),(6,20)],'H')
line([(5,11),(5,25)],'H');line([(6,12),(6,25)],'3');dot(5,20,'6');rect((4,24,7,25),'H');rect((2,27,9,27),'3');rect((3,26,8,26),'5')
save('Tapered flames, wax shafts, scrolling brass arms and separated highlights')

load('stairs')
for n in range(6):
    y=n*4;l=12-n*2;r=51+n*2
    # Stone nosing and blocks are outside the central carpet connection.
    rect((l+1,y,r-1,y),'5');rect((l+7,y,r-7,y),'F')
    dot(l+1,y,'6');dot(l+4,y+2,'3');dot(r-4,y+2,'3')
    dot(l+7,y,'H');dot(r-7,y,'H')
    rect((l+8,y+1,l+9,y+2),'F');rect((r-9,y+1,r-8,y+2),'D')
    line([(l+3,y+3),(l+6,y+3)],'1');line([(r-6,y+3),(r-3,y+3)],'1')
save('Beveled stone treads, inset risers and carpet edging with unchanged stair silhouette and runner join')

load('runner-edge')
# Decorative detail stays within the existing eight-pixel border footprint.
for y in range(16):
    dot(1,y,'H' if y%4 else '5');dot(2,y,'D');dot(6,y,'E')
for y in (2,10):
    poly([(4,y),(5,y+2),(4,y+4),(3,y+2)],'F');dot(4,y+1,'C');dot(4,y+3,'E')
save('Restrained woven border diamonds; center runner and motifs unchanged')

load('paving')
# Fragmented cool/warm reflections stay low contrast; row12 is the main sampled field.
for x,y,c in ((2,3,'3'),(3,3,'3'),(4,3,'3'),(5,4,'2'),(6,4,'3'),(22,3,'7'),(23,3,'8'),(24,3,'7'),(25,4,'7'),(5,12,'2'),(6,12,'2'),(7,12,'2'),(8,12,'2'),(21,12,'7'),(22,12,'7'),(23,12,'2')):dot(x,y,c)
for x in (1,2,3,17,18,19):dot(x,15,'2' if x<16 else '7')
save('Fragmented polished-stone reflections and softened bevel seams, within accepted perspective strips')

load('trim-top')
for x in range(1,16,4):
    dot(x,1,'6');dot(x+1,2,'5');dot(x,4,'3');dot(x+1,5,'2')
save('Alternating carved cornice dentils and restrained edge highlights')

(R/'authoring_inputs.json').write_text(json.dumps(out,indent=2)+'\n')
print('Art grids:',sum(a['status']=='revised' for a in out['assets'].values()),'revised;',sum(a['status']=='reused' for a in out['assets'].values()),'unchanged')
