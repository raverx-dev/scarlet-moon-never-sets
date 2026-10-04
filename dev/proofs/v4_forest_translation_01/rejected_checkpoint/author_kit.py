"""Native indexed pixel authoring aid. No reference image is loaded or sampled.
Integer silhouettes, explicit bark ribbons and hand-designed leaf/fern clusters.
Canonical RoboPixel grid exports, not this script, are final composition inputs.
"""
from pathlib import Path
from PIL import Image,ImageDraw
import json
ROOT=Path(__file__).resolve().parent
COLORS={'.':'#00000000','0':'#080e1b','1':'#101c29','2':'#182d38','3':'#23434a','4':'#315961','5':'#457078','6':'#5b8990',
 'a':'#15282e','b':'#213b39','c':'#344f45','d':'#527159','e':'#789265','f':'#9caa76',
 'g':'#181e26','h':'#292e2d','i':'#3c4035','j':'#565440','k':'#726c4b',
 'l':'#35304e','m':'#62517b','n':'#a385b6','o':'#c8b2cb','p':'#5a3c38','q':'#9e603e','r':'#d99952','s':'#f1d48a'}
TOKENS=''.join(COLORS); A={}
def canvas(w,h,bg='.'):
 global im,d
 im=Image.new('L',(w,h),TOKENS.index(bg));d=ImageDraw.Draw(im)
def poly(pts,c):d.polygon(pts,fill=TOKENS.index(c))
def line(pts,c,w=1):d.line(pts,fill=TOKENS.index(c),width=w)
def rect(box,c):d.rectangle(box,fill=TOKENS.index(c))
def pattern(rows,x,y,colors=None,flip=False):
 for yy,row in enumerate(rows):
  for xx,c in enumerate(row):
   if c!='.':
    px=x+(len(row)-xx-1 if flip else xx);py=y+yy
    if 0<=px<im.width and 0<=py<im.height:im.putpixel((px,py),TOKENS.index((colors or {}).get(c,c)))
def save(name,role):
 A[name]={'asset_id':'v4-forest-trans01-'+name,'role':role,'width':im.width,'height':im.height,'rows':[''.join(TOKENS[im.getpixel((x,y))] for x in range(im.width)) for y in range(im.height)]}
# Cluster edges intentionally broken, asymmetric; not oval stamping.
LEAF=['....cc....','..ccddc...','.cdeedcc..','cdddecbbc.','.ddecbb...','..ccbbbc..','...bb..b..']
LEAF2=['.....cc.....','...cdedc....','.ccdeedcc...','cdeedccbbc..','.ddecbbccc..','..ccbb...b..','...b........']
def leaves(points,ramp=('b','c','d','e'),variant=0):
 remap=dict(zip('bcde',ramp))
 for i,(x,y) in enumerate(points):pattern(LEAF2 if (i+variant)%3==0 else LEAF,x,y,remap,flip=(i%3==1))
# An atmospheric opening with deliberate stepped contours, not a painted gradient.
canvas(80,112,'1')
poly([(7,0),(75,0),(79,37),(72,58),(76,75),(62,94),(45,107),(30,101),(14,85),(6,70),(0,49)],'2')
poly([(18,0),(66,0),(68,14),(59,27),(61,40),(49,56),(48,74),(32,82),(24,70),(28,55),(15,37),(20,23)],'3')
poly([(30,0),(55,0),(55,12),(49,19),(52,31),(42,44),(34,47),(29,37),(33,28),(27,13)],'4')
poly([(40,0),(49,0),(49,7),(44,13),(38,11)],'5')
for pts in [[(0,62),(18,75),(24,91),(43,96),(56,88),(68,80),(79,79),(79,111),(0,111)],[(0,94),(25,101),(56,100),(79,91),(79,111),(0,111)]]:poly(pts,'1')
save('depth-opening','Stepped, low-contrast distant opening; never stretched')
# A group of irregular distant trunks and crowns.
canvas(56,104)
for pts in [[(3,103),(6,57),(4,35),(8,12),(12,6),(11,41),(14,72),(13,103)],[(28,103),(28,53),(23,27),(25,13),(30,24),(33,52),(33,103)],[(46,103),(48,48),(44,24),(49,0),(52,0),(51,38),(54,65),(52,103)]]:poly(pts,'3')
for pts in [[(9,47),(0,29)],[(12,62),(22,38)],[(30,47),(40,29)],[(48,35),(37,19)]]:line(pts,'3',3)
leaves([(-6,21),(0,14),(10,27),(17,19),(28,17),(36,4),(44,8),(40,30),(20,37),(2,49)],('2','3','3','4'))
# Break the baseline of every distant trunk into irregular low-contrast roots.
for yy in range(78,104):
 for xx in range(56):
  if im.getpixel((xx,yy)):
   if yy>96+(xx*3%7):im.putpixel((xx,yy),0)
   elif yy>84+(xx%5):im.putpixel((xx,yy),TOKENS.index('2'))
save('far-grove','Distant crooked-tree group with restrained canopy')
# Medium tree: narrow twisting trunk; branch junctions vary.
canvas(36,112)
poly([(9,111),(13,88),(10,67),(15,49),(16,26),(12,9),(16,0),(21,0),(20,28),(23,48),(18,68),(22,96),(28,111)],'a')
poly([(14,110),(17,91),(14,68),(18,47),(18,25),(16,9),(19,7),(20,29),(21,49),(16,71),(20,99),(23,110)],'b')
line([(18,47),(30,26),(33,13)],'a',4);line([(14,63),(4,43),(0,39)],'a',5)
line([(19,37),(7,20),(4,9)],'b',3)
leaves([(-3,3),(4,-2),(14,1),(23,7),(21,18),(0,31),(3,42),(25,24),(12,26)],('a','b','c','d'))
line([(20,82),(16,91),(17,101)],'c');save('mid-tree','Middle-distance crooked trunk and branch clusters')
# Major old-growth trunk, 64x176. Explicit ribbons follow the bends.
canvas(64,176)
poly([(0,0),(41,0),(36,15),(27,29),(26,43),(33,61),(28,80),(31,100),(27,120),(37,143),(56,163),(63,175),(37,175),(19,155),(9,128),(6,102),(11,80),(6,61),(13,40),(9,22)],'g')
poly([(13,0),(34,0),(28,18),(20,33),(20,46),(27,62),(21,81),(26,101),(20,123),(28,147),(43,166),(49,175),(37,175),(21,156),(13,131),(11,104),(16,81),(11,59),(17,40),(14,24)],'h')
poly([(25,0),(32,0),(24,20),(18,35),(19,47),(25,62),(20,79),(23,97),(20,113),(15,102),(17,80),(13,60),(18,39),(16,27)],'i')
poly([(19,110),(23,129),(33,151),(48,169),(47,175),(36,164),(25,148),(18,130)],'i')
# Branch swept right, visibly interlocks the trunk.
poly([(23,48),(28,29),(42,21),(54,11),(63,0),(63,10),(53,22),(39,29),(33,44),(29,59)],'h')
line([(26,47),(33,30),(46,23),(58,12),(63,5)],'i',3)
line([(30,40),(36,31),(47,26),(59,15)],'j')
# Moss side ribbon and broken clusters, avoids a uniform luminous contour.
line([(32,1),(26,16),(20,27),(19,36)],'d',3)
line([(21,50),(25,61),(21,74)],'c',3)
line([(21,88),(23,100),(19,116),(24,136),(33,150),(46,164)],'c',3)
for pts in [[(29,7),(26,13)],[(21,23),(19,30)],[(23,94),(23,99)],[(21,120),(24,131)],[(28,141),(32,148)],[(39,157),(46,164)]]:line(pts,'e')
# Bark fissures turn with the wood; side branches and a dark knot.
for pts in [[(9,4),(13,16),(12,25)],[(20,3),(21,10),(17,19),(17,26)],[(13,43),(11,56),(15,69)],[(20,54),(22,62),(18,72)],[(12,86),(10,100),(12,112)],[(17,119),(19,135),(24,144)],[(28,151),(34,159),(35,165)],[(36,163),(43,171)]]:line(pts,'0')
poly([(14,91),(18,85),(21,91),(20,99),(16,103),(13,98)],'g');line([(14,95),(16,89),(19,90)],'j');line([(17,94),(17,98)],'0')
leaves([(2,32),(-3,70),(0,118),(15,149),(40,164)],('a','b','c','d'))
save('elder-trunk','Twisted foreground elder trunk, moss ribbons, knot and rising branch')
# Slender contrasting right-hand fork.
canvas(40,160)
poly([(16,159),(19,130),(15,105),(18,80),(15,59),(17,37),(12,22),(10,0),(18,0),(20,21),(23,38),(20,60),(24,81),(21,108),(26,137),(39,159)],'g')
poly([(20,159),(23,131),(19,105),(21,80),(18,59),(20,37),(16,19),(14,0),(17,0),(21,25),(23,38),(20,60),(24,81),(21,108),(26,137),(35,159)],'i')
poly([(18,49),(28,29),(31,10),(37,0),(39,0),(35,18),(32,36),(23,62)],'h')
line([(24,47),(30,32),(33,14)],'j');line([(21,133),(22,118),(19,107),(21,85)],'c',2)
line([(22,145),(29,157)],'d',2)
line([(18,26),(19,37),(17,53)],'c',2)
for pts in [[(17,66),(20,80),(18,96)],[(22,137),(26,145)],[(31,25),(31,32)]]:line(pts,'0')
leaves([(1,17),(21,8),(22,44),(0,70),(20,107),(5,136)],('a','b','c','d'))
save('fork-trunk','Narrow forked foreground tree with asymmetric root foot')
# Broad irregular canopy with hand-positioned layered leaf clusters.
canvas(64,40)
poly([(0,0),(63,0),(63,19),(55,19),(57,27),(47,25),(42,34),(36,29),(29,39),(22,31),(14,33),(10,23),(0,26)],'a')
poly([(0,2),(57,0),(61,11),(50,12),(44,23),(33,21),(24,30),(15,24),(7,27),(0,19)],'b')
leaves([(0,0),(13,-3),(28,0),(42,-4),(53,2),(6,11),(20,8),(34,11),(47,12),(12,21),(27,21),(39,23)],('a','b','c','d'))
# A few light-facing leaf tips only.
for x,y in [(17,4),(39,15),(26,12),(12,15)]:pattern(['ee.','.d.'],x,y)
save('canopy','Asymmetric canopy mass; layered lobe clusters, broken underside')
canvas(40,28)
poly([(0,16),(5,10),(11,12),(16,3),(24,0),(29,8),(35,7),(39,16),(35,25),(15,27),(0,23)],'a')
leaves([(0,12),(8,9),(16,0),(24,5),(29,12),(17,12),(5,18),(22,20)],('a','b','c','d'))
save('understory','Low irregular shrub with readable leaf masses')
# Fern built from explicitly stepped leaflets along curved fronds, no ovals.
canvas(28,30)
for pts in [[(13,29),(13,16),(8,8),(1,4)],[(13,29),(16,17),(24,10),(27,10)],[(13,29),(11,17),(3,14),(0,16)],[(13,29),(19,23),(27,22)],[(13,29),(17,12),(18,3)]]:line(pts,'c')
for x,y,flip in [(2,4,0),(6,7,0),(9,11,0),(2,14,0),(6,16,0),(10,20,0),(18,5,1),(17,10,1),(20,14,1),(24,11,1),(18,23,1),(24,22,1)]:
 pattern(['..d..','.dec.','ddc..','.b...'],x-2,y,flip=bool(flip))
line([(13,27),(14,18),(16,12)],'d');save('fern','Stepped fern fronds, deliberately sparse silhouette')
# Root shelf anchors trees; broken top moss edge, shadow undercuts.
canvas(64,32)
poly([(0,6),(7,3),(17,7),(26,9),(35,8),(43,16),(53,20),(63,26),(63,31),(0,31)],'g')
poly([(0,7),(8,6),(18,11),(29,12),(35,11),(45,20),(59,27),(51,28),(37,23),(27,17),(14,16),(0,13)],'i')
line([(0,8),(7,7),(17,12),(28,13),(35,12),(45,21),(58,27)],'c',3)
for pts in [[(1,7),(7,7),(12,9)],[(19,12),(27,13)],[(34,12),(40,17)],[(47,23),(52,25)]]:line(pts,'e')
line([(0,19),(12,20),(21,26),(35,29)],'h',3)
leaves([(0,1),(15,6),(37,18)],('a','b','c','d'));save('root-bank','Root and moss transition shelf for lower edge framing')
canvas(32,32,'0')
# Intentionally extremely low contrast floor marks; no fixed brick/grid pattern.
for box in [(5,9,9,9),(22,27,25,27)]:rect(box,'1')
save('quiet-ground','Dark native ground field with sparse horizontal marks')
canvas(32,16)
for pts,c in [([(0,10),(8,7),(12,8),(21,3),(30,4),(27,7),(17,9),(9,12),(0,12)],'b'), ([(7,9),(14,8),(20,5),(24,5)],'c'), ([(18,5),(22,4)],'d')]:
 if len(pts)>4:poly(pts,c)
 else:line(pts,c)
save('moss-seam','Broken moss ledge for quiet clearing edges')
canvas(10,20)
line([(4,0),(4,5)],'i');pattern(['...jj...','..jpqj..','.jqqqqj.','.pqrrqp.','.pqssqp.','.pqrsqp.','.pqrrqp.','..pqqp..','...jj...'],0,5)
rect((3,17,4,18),'h');save('lantern','Small hanging amber lantern, hard pixel light not glow')
canvas(16,16)
pattern(['....mm......','..mmnnm.....','.mnnonnm....','mmnnnnnmm...','..lllll.....','....io......','....io......','....ii......','...bhhb.....'],0,1)
pattern(['..mm..','.mnnm.','mmnnmm','..ll..','..i...','..i...'],9,8)
save('mushrooms','Two restrained violet mushroom caps')
canvas(5,5)
pattern(['.....','..r..','.rsr.','..r..','.....'],0,0);save('firefly','Single restrained edge light accent')
# Foreground serpentine root continuation: tapered turns with bark splits.
canvas(60,72)
poly([(0,0),(17,0),(22,9),(20,21),(28,35),(40,42),(48,52),(59,68),(53,71),(40,62),(30,52),(16,43),(10,31),(12,21),(9,11),(0,8)],'g')
poly([(5,0),(13,0),(18,11),(16,23),(23,38),(37,47),(46,57),(55,69),(49,66),(37,56),(23,48),(15,35),(14,25),(14,14)],'i')
line([(11,1),(16,13),(14,24),(20,38),(34,49),(44,58),(52,68)],'c',3)
for pts in [[(12,3),(15,11)],[(15,24),(18,32)],[(22,41),(30,47)],[(36,52),(41,57)]]:line(pts,'e')
line([(7,2),(12,15),(10,24),(14,37),(25,50),(38,57)],'0')
leaves([(-3,5),(0,35),(18,51),(39,61)],('a','b','c','d'))
save('root-crook','Curved near-root continuation, with broken moss crest')
canvas(64,32)
poly([(0,16),(5,11),(11,13),(16,5),(23,4),(27,9),(34,7),(40,12),(48,7),(54,12),(63,10),(63,23),(58,25),(53,23),(48,27),(43,24),(38,26),(33,23),(29,25),(23,24),(19,27),(14,24),(8,25),(4,22),(0,24)],'1')
leaves([(-2,10),(8,6),(20,2),(30,8),(43,5),(54,9),(4,21),(20,16),(37,19),(52,18)],('1','2','3','3'))
save('far-thicket','Low-contrast horizon thicket conceals hard trunk endpoints')
palette={'schema':'robopixel.palette/v1','palette_id':'v4-forest-translation-01','version':1,'entries':[]}
for i,(s,c) in enumerate(COLORS.items()):
 rgba=[0,0,0,0] if s=='.' else list(bytes.fromhex(c[1:]))+[255]
 palette['entries'].append({'index':i,'color_id':'transparent' if s=='.' else 'forest-'+s,'text_token':s,'adapter_symbols':{'scarlet-moon-js':s},'rgba':rgba})
(ROOT/'authoring_inputs.json').write_text(json.dumps({'palette':palette,'assets':A},indent=2)+'\n')
(ROOT/'palette.json').write_text(json.dumps(COLORS,indent=2)+'\n')
# Local authoring previews only; later compose.py consumes verified canonical exports.
for name,a in A.items():
 p=Image.new('RGBA',(a['width'],a['height']));p.putdata([tuple(e['rgba']) for row in a['rows'] for e in [palette['entries'][TOKENS.index(s)] for s in row]])
 p.save(ROOT/'assets'/f'{name}.png')
print(f'{len(A)} assets authored, {sum(a["width"]*a["height"] for a in A.values())} indexed cells')
