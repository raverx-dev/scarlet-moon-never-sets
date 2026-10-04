"""Correction 01: native raster cluster authoring, no reference sampling.
Substantial scanline trunk masses, bark grooves, buttresses, and dense leaf stencils.
All drawing is at final integer resolution; no vector render, resize or antialiasing.
The resulting grids must be committed and read back through RoboPixel.
"""
from pathlib import Path
from PIL import Image
import json,math
R=Path(__file__).resolve().parent
old=json.loads((R/'rejected_checkpoint/authoring_inputs.json').read_text())
P=old['palette'];T=''.join(e['text_token'] for e in P['entries']);A={}
def new(w,h,bg='.'):
 global im
 im=Image.new('L',(w,h),T.index(bg))
def px(x,y,c):
 x,y=int(x),int(y)
 if 0<=x<im.width and 0<=y<im.height:im.putpixel((x,y),T.index(c))
def at(x,y):return T[im.getpixel((x,y))] if 0<=x<im.width and 0<=y<im.height else '.'
def stamp(rows,x,y,m={},flip=False):
 for yy,row in enumerate(rows):
  for xx,c in enumerate(row):
   if c!='.':px(x+(len(row)-1-xx if flip else xx),y+yy,m.get(c,c))
def stroke(points,c,width=1):
 for (x0,y0),(x1,y1) in zip(points,points[1:]):
  n=max(abs(x1-x0),abs(y1-y0),1)
  for i in range(n+1):
   x=round(x0+(x1-x0)*i/n);y=round(y0+(y1-y0)*i/n)
   for yy in range(y-width//2,y+(width+1)//2):
    for xx in range(x-width//2,x+(width+1)//2):px(xx,yy,c)
def save(n):
 a=old['assets'][n].copy();a['rows']=[''.join(T[im.getpixel((x,y))] for x in range(im.width)) for y in range(im.height)];A[n]=a
# Interlocking clustered leaves: connected bodies, lit crowns, dark undersides.
LEAF=[
'......ccc.......',
'...cccdedcc.....',
'..cddeeeeddc....',
'.cdeeffeededdc..',
'cddeeeedddedcc..',
'cdeddccdddddcbc.',
'.cdddccbbcddbbc.',
'..ccbcb.bbccbbc.',
'...bbb...bbbb...',
'....b......b....']
SMALL=['...ccc...','..cdedc..','.cdeeddc.','cddedcbc.','.ccddbbc.','..bbbbb..','...b.b...']
def leaf(x,y,level=0,flip=False,small=False):
 ramps=[dict(zip('bcdef','bcdef')),dict(zip('bcdef','abcde')),dict(zip('bcdef','12344')),dict(zip('bcdef','aabcd'))]
 stamp(SMALL if small else LEAF,x,y,ramps[level],flip)
def leaves_region(w,h,level=0):
 # Explicit stagger and variable cluster sizes avoid a tiled stamp rhythm.
 for j,y in enumerate(range(-5,h,7)):
  for i,x in enumerate(range(-9,w,11)):
   leaf(x+(j*7+i*3)%9,y+(i*5+j)%4,level,(i+j)%2==1,(i+2*j)%5==0)
def tree(w,h,center,width,phase=0,far=False):
 """Connected substantial wood; grooved highlights follow twisting longitudinal grain."""
 new(w,h)
 # Roots widen at foot, rather than a narrow stem ending on a flat baseline.
 limits=[]
 for y in range(h):
  turn=round(3*math.sin(y/23+phase)+2*math.sin(y/47))
  c=center+turn
  flare=round(max(0,(y/h-.70))*w*1.35)
  half=width//2+flare+round(2*math.sin(y/16+phase))
  left=max(0,c-half);right=min(w-1,c+half)
  limits.append((left,right,c))
  for x in range(left,right+1):
   u=(x-left)/max(1,right-left)
   col=('2' if u<.20 or u>.82 else '3') if far else ('g' if u<.12 or u>.91 else 'h' if u<.30 or u>.74 else 'i')
   px(x,y,col)
 # Wind-shaped branches are thick, stepped, and shaded within the silhouette.
 for pts,bw in [([(center,42),(center+9,29),(w-8,14),(w-1,8)],max(3,width//3)), ([(center,66),(center-9,50),(2,39)],max(3,width//4))]:
  stroke(pts,'2' if far else 'g',bw+3);stroke(pts,'3' if far else 'h',bw)
 if far:return
 # Native bark ribbons: discontinuous ridges and black fissures, no single flat polygon.
 for y in range(h):
  left,right,c=limits[y]
  for k in range(-4,6):
   x=c+k*5+round(2*math.sin(y/17+k*.9)+math.sin(y/6+k))
   for xx,col in [(x,'g'),(x+1,'j'),(x+2,'i')]:
    if left+2<xx<right-2 and at(xx,y)!='.' and not ((y+k*11)%31>25):px(xx,y,col)
  # Small bark plates grouped along ridges, not uniform speckle.
  if y%13 in (1,2,3):
   x=c-5+round(3*math.sin(y/14))
   for xx in range(x,x+3):
    if left+3<xx<right-2:px(xx,y,'j')
  # Patchy moss climbs one uneven light-facing rim.
  mx=right-3-(y//9%3)
  if (y//7)%6 not in (2,5):
   for xx in range(mx-2,mx+1):px(xx,y,'c' if xx<mx else 'd')
   if y%7 in (1,2):px(mx,y,'e')
 # Hollow knot: exact small stencil, shaded rim, irregular shoulders.
 knot=['....jjj....','..jjihhjj..','.jiiggggij.','jig0000gij.','jig0000ggij','jig0000ggij','.ig000ggij.','.iiggggij..','..iiihij...','....hh.....']
 stamp(knot,max(1,center-5),int(h*.53))
 # Buttress ridges diverge into anchored soil near the base.
 for k in [-1,0,1]:
  points=[(center+k*4,h-38),(center+k*8,h-19),(max(1,min(w-2,center+k*(width//2+10))),h-2)]
  stroke(points,'g',3);stroke([(x+2,y) for x,y in points],'j',1)
new(80,112,'1')
# Distant illumination is broken by actual little canopy clusters, not nested polygons.
for y in range(112):
 for x in range(80):
  distance=abs(x-43)+y*.30
  c='4' if distance<19 and y<47 else '3' if distance<32 and y<79 else '2' if distance<44 and y<100 else '1'
  if (y//5+x//9)%7==0 and c=='4':c='3'
  px(x,y,c)
for x,y in [(0,9),(63,18),(6,37),(58,50),(14,74),(43,89)]:leaf(x,y,2,small=True)
save('depth-opening')
# Far trees: a group of different substantial forms with branched crowns.
new(56,104);combined=im.copy()
for cx,ww,ph,yy in [(7,9,1,6),(27,12,2,-5),(49,8,4,0)]:
 tree(56,104,cx,ww,ph,True);layer=im
 for y in range(104):
  for x in range(56):
   if layer.getpixel((x,y)) and 0<=y+yy<104:combined.putpixel((x,y+yy),layer.getpixel((x,y)))
im=combined
# Recede the branches into shade and clothe their angular joints in crowns.
for y in range(104):
 for x in range(56):
  c=at(x,y)
  if c=='3':px(x,y,'2')
  elif c=='2':px(x,y,'1')
for x,y in [(-7,6),(8,0),(26,8),(42,1),(-2,27),(20,22),(37,35),(4,43),(22,39),(42,47)]:leaf(x,y,2)
for y in range(87,104):
 for x in range(56):
  if at(x,y)!='.':px(x,y,'2' if y<96 else '1')
save('far-grove')
tree(36,112,17,17,1)
# Midground stays cooler and less contrasted than near bark.
mapping={'g':'1','h':'a','i':'b','j':'c','d':'c','e':'d','0':'1'}
for y in range(112):
 for x in range(36):
  c=at(x,y)
  if c in mapping:px(x,y,mapping[c])
for x,y in [(-6,0),(12,9),(20,26),(-2,39)]:leaf(x,y,1)
save('mid-tree')
tree(64,176,25,35,.4)
for x,y in [(-4,15),(39,34),(4,119),(25,153)]:leaf(x,y,1,small=True)
save('elder-trunk')
tree(40,160,18,24,2.7)
for x,y in [(20,12),(-3,47),(19,125)]:leaf(x,y,1,small=True)
save('fork-trunk')
new(64,40)
leaves_region(64,31,0)
# A scalloped lower edge made from leaf shapes, not a solid angular slab.
for x,y in [(-4,24),(14,28),(35,25),(49,20)]:leaf(x,y,1)
save('canopy')
new(40,28)
for x,y in [(10,0),(22,4),(-3,7),(6,9),(18,12),(30,13),(0,17),(12,19)]:leaf(x,y,1)
for x,y in [(9,1),(20,5),(1,9)]:leaf(x,y,0,small=True)
save('understory')
new(28,30)
# Broader unfurling fern fans; paired 2-3px leaflets, stepped tips.
for pts in [[(13,29),(12,17),(7,8),(0,4)],[(13,29),(17,17),(24,8),(27,8)],[(13,29),(8,19),(1,16)],[(13,29),(22,21),(27,20)],[(13,29),(16,13),(16,1)]]:
 stroke(pts,'c',2)
for x,y,flip in [(2,5,0),(6,8,0),(9,12,0),(4,17,0),(9,20,0),(16,4,1),(16,9,1),(20,14,1),(24,10,1),(21,22,1)]:stamp(['..e..','.ded.','dddc.','.cc..'],x-2,y,{},flip)
save('fern')
new(64,32)
for y in range(32):
 for x in range(64):
  top=7+round(3*math.sin(x/9)+2*math.sin(x/4))
  if y>=top:
   c='c' if y<top+2 else 'b' if y<top+5 else 'h' if y<top+10 else 'g'
   px(x,y,c)
for pts in [[(0,20),(16,17),(30,23),(45,24),(63,29)],[(10,12),(24,18),(39,18),(59,24)],[(2,28),(15,23),(25,28)]]:
 stroke(pts,'g',4);stroke([(x,y-1) for x,y in pts],'i',2);stroke([(x,y-2) for x,y in pts],'j')
for x,y in [(-3,0),(15,2),(36,3),(51,0)]:leaf(x,y,1,small=True)
save('root-bank')
new(32,32,'1')
# Broken loam patches, not connected wave bands or isolated repeated dashes.
for rows,x,y in [(['..1111....','11111111..','.111111111','...11111..'],1,3),
                 (['....111...','..1111111.','11111111..','.1111.....'],17,13),
                 (['..111111..','1111111111','.111111...','...11.....'],4,24),
                 (['1111....','111111..','..111...'],25,29)]:stamp(rows,x,y,{'1':'0'})
save('quiet-ground')
new(32,16)
for x,y in [(-3,5),(6,2),(16,3),(24,7)]:leaf(x,y,3,small=True)
for x in range(3,28):
 if x%5<3:px(x,13+(x//8%2),'a')
save('moss-seam')
# Keep successful small lights/flora rather than inflate scope.
for n in ['lantern','mushrooms','firefly']:A[n]=old['assets'][n]
new(60,72)
# Multiple interlocking roots and soil, not one floating curved stripe.
for y in range(72):
 for x in range(60):
  edge=21+round(8*math.sin(y/20))+int(y*.2)
  if x<edge:px(x,y,'a' if x>edge-4 else 'g')
for i,pts in enumerate([[(6,0),(14,14),(18,31),(35,45),(52,65)],[(22,0),(19,15),(29,27),(36,48),(58,58)],[(2,23),(9,38),(17,47),(26,70)]]):
 stroke(pts,'g',12-i*2);stroke([(x-1,y) for x,y in pts],'h',8-i);stroke([(x-2,y) for x,y in pts],'i',4);stroke([(x-3,y) for x,y in pts],'c',2)
for x,y in [(-4,0),(9,17),(-3,33),(20,43),(38,58),(2,58)]:leaf(x,y,1,small=True)
save('root-crook')
new(64,32)
for x,y in [(1,8),(13,1),(26,7),(40,0),(53,6),(-4,18),(11,16),(29,17),(45,15)]:leaf(x,y,2)
# Low near-shadow fill connects clumps into the ground.
for y in range(24,32):
 for x in range(64):
  if at(x,y)!='.':px(x,y,'1' if y>27 else '2')
save('far-thicket')
(R/'authoring_inputs.json').write_text(json.dumps({'palette':P,'assets':A},indent=2)+'\n')
for n,a in A.items():
 p=Image.new('RGBA',(a['width'],a['height']));p.putdata([tuple(P['entries'][T.index(c)]['rgba']) for row in a['rows'] for c in row]);p.save(R/'assets'/f'{n}.png')
print('Native correction authored:',len(A),'assets;',sum(A[n]['rows']!=old['assets'][n]['rows'] for n in A),'substantially rebuilt')
