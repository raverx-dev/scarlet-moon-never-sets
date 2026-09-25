"""Original integer pixel drafting; never reads reference-image pixels.
Drafts are submitted to RoboPixel; compose.py consumes only canonical readbacks.
"""
from PIL import Image, ImageDraw
import random,json
from pathlib import Path
ROOT=Path(__file__).parent
COLORS=['00000000','080e29','101b42','152951','1b3764','25477d','365b99','526eb2','8096ca','b9cbea','181b36','2b294a','44415f','625b78','9590a3','331d49','56234f','852958','bc345e','ed5279','ff8e9c','b7eafa','71bce5','3976ad']
TOKENS='.123456789ABCDEFGHIJKLMNOP'
PAL=[tuple(bytes.fromhex(c)) if len(c)==8 else (*bytes.fromhex(c),255) for c in COLORS]
assets={}
def canvas(w,h,c=0): return Image.new('L',(w,h),c)
def poly(im,pts,c): ImageDraw.Draw(im).polygon(pts,fill=c)
def line(im,pts,c,width=1): ImageDraw.Draw(im).line(pts,fill=c,width=width)
def rect(im,box,c): ImageDraw.Draw(im).rectangle(box,fill=c)
def dot(im,x,y,c):
 if 0<=x<im.width and 0<=y<im.height: im.putpixel((x,y),c)
def save(n,im): assets[n]=im
def pine(im,x,y,h,c,lit=None):
 line(im,[(x,y),(x,y+h)],c)
 for k in range(3,h,3):
  r=max(1,int(k*.29)); poly(im,[(x,y+k-4),(x-r,y+k+2),(x-1,y+k),(x+r,y+k+1)],c)
  if lit is not None and k>6: line(im,[(x-r,y+k+1),(x-1,y+k-1)],lit)
def grain(im,seed,colors,count,region=None):
 r=random.Random(seed); box=region or (0,0,im.width,im.height)
 for _ in range(count):
  x=r.randrange(box[0],box[2]);y=r.randrange(box[1],box[3])
  if im.getpixel((x,y)): line(im,[(x,y),(min(im.width-1,x+r.randrange(1,3)),y)],r.choice(colors))
# Quiet twilight with pixel-cluster atmospheric transitions.
im=canvas(256,88,1)
for y,c in [(28,2),(51,3),(70,4)]:rect(im,(0,y,255,87),c)
r=random.Random(31)
for y,c in [(28,2),(51,3),(70,4)]:
 for _ in range(65):
  x=r.randrange(256); yy=y-r.randrange(1,5);line(im,[(x,yy),(x+r.randrange(1,5),yy)],c)
for x,y in [(18,9),(59,18),(91,5),(118,24),(156,9),(224,14),(242,34),(82,29)]:dot(im,x,y,8)
save('twilight',im)
# Scarlet cloud ribbons, deliberately broken clusters and scalloped undersides.
im=canvas(128,44)
for pts,c in [([(0,2),(18,6),(30,3),(44,10),(57,9),(66,15),(82,12),(95,16),(110,10),(127,9),(127,21),(108,22),(99,26),(80,23),(70,27),(53,20),(38,19),(26,12),(10,14),(0,8)],15), ([(0,4),(14,9),(24,7),(40,14),(55,13),(69,20),(82,18),(100,22),(118,15),(127,14),(127,18),(110,19),(102,25),(79,22),(71,25),(53,18),(39,17),(24,11),(13,12)],16), ([(3,7),(16,11),(24,9),(39,16),(55,16),(70,23),(83,20),(101,25),(117,19),(124,19),(110,23),(101,28),(78,24),(70,28),(53,20),(38,20),(24,13)],17)]:poly(im,pts,c)
r=random.Random(89)
for _ in range(180):
 x=r.randrange(128);y=r.randrange(44)
 if im.getpixel((x,y))==17 and r.random()<.65:line(im,[(x,y),(min(127,x+2),y)],18)
save('scarlet-cloud',im)
im=canvas(28,28);ImageDraw.Draw(im).ellipse((1,1,26,26),fill=19);ImageDraw.Draw(im).ellipse((2,1,25,25),fill=20)
for pts in [[(6,5),(11,3),(15,5),(12,8),(15,11),(11,13),(9,10),(5,10)],[(20,7),(24,10),(23,15),(19,14),(17,11)],[(7,17),(12,16),(15,18),(14,22),(9,24),(6,21)],[(18,19),(21,17),(24,19),(21,23),(17,24)]]:poly(im,pts,19)
for x,y in [(6,6),(10,5),(20,9),(9,20),(21,20)]:dot(im,x,y,18)
save('scarlet-moon',im)
# Mountain range is a large silhouette, not repeated triangular tiles.
im=canvas(256,53)
ridge=[(0,19),(13,16),(25,9),(34,14),(47,4),(56,8),(67,19),(78,22),(92,15),(107,20),(119,10),(131,2),(142,12),(151,16),(165,29),(177,26),(190,16),(201,19),(216,10),(226,15),(241,8),(255,14)]
poly(im,ridge+[(255,52),(0,52)],3)
for x,y in [(25,9),(47,4),(131,2),(190,16),(216,10),(241,8)]:
 poly(im,[(x,y),(x+5,y+7),(x+21,45),(x+7,34),(x-2,y+6)],4)
 line(im,[(x,y+1),(x+4,y+8),(x+9,y+14)],15)
 line(im,[(x+4,y+6),(x+8,y+11),(x+13,y+19)],16)
grain(im,23,[3,4,5],530)
save('far-ridges',im)
# Sweeping wooded distance banks. Depth slope is authored independently each side.
for name,w,h,points,seed in [('west-woods',112,65,[(0,10),(15,14),(27,24),(45,28),(58,39),(75,46),(96,55),(111,59)],21),('east-woods',104,53,[(0,48),(16,44),(30,35),(47,29),(60,25),(79,10),(103,4)],44)]:
 im=canvas(w,h);poly(im,points+[(w-1,h-1),(0,h-1)],4)
 r=random.Random(seed)
 def edge(x):
  for a,b in zip(points,points[1:]):
   if a[0]<=x<=b[0]: return int(a[1]+(b[1]-a[1])*(x-a[0])/(b[0]-a[0]))
  return points[-1][1]
 for x in range(1,w,3):
  y=edge(x); pine(im,x,y-r.randrange(4,12),r.randrange(8,17),3)
 for x in range(0,w,5):
  y=min(h-4,edge(x)+r.randrange(5,15));pine(im,x,y-7,r.randrange(9,20),2,5 if x%3==0 else None)
 grain(im,seed,[4,5,6],int(w*h*.08))
 for x in range(4,w-5,9):
  y=min(h-2,edge(x)+9)
  if x<w-20:dot(im,x,y,18);dot(im,x,y-1,19)
 save(name,im)
im=canvas(22,20)
line(im,[(1,2),(5,4),(17,4),(21,2)],1,2);line(im,[(3,4),(19,4)],18)
rect(im,(5,6,6,19),17);rect(im,(16,6,17,19),18);rect(im,(4,7,18,8),1);dot(im,6,8,19);dot(im,17,8,19)
save('distant-torii',im)
im=canvas(112,18)
for pts,c in [([(0,14),(12,11),(23,12),(38,7),(48,8),(61,3),(73,5),(83,8),(99,10),(111,15),(96,16),(72,13),(54,14),(33,16)],5), ([(3,14),(25,13),(41,10),(55,11),(66,7),(76,9),(89,12),(107,15),(88,14),(65,12),(45,14)],6)]:poly(im,pts,c)
line(im,[(10,15),(27,15),(43,13),(63,13),(77,12),(94,14)],7)
save('mist-bank',im)
# Non-periodic sparse blue water. Broad calm values; no checkerboard noise.
im=canvas(128,128,2);r=random.Random(112)
for _ in range(260):
 x=r.randrange(128);y=r.randrange(128);length=r.randrange(2,10)
 line(im,[(x,y),(min(127,x+length),y)],3 if r.random()<.88 else 4)
save('deep-water',im)
im=canvas(64,128);r=random.Random(203)
for y in range(0,128,3):
 for _ in range(3):
  x=r.randrange(0,55);L=r.randrange(2,11);c=r.choices([4,5,6,7],[4,5,3,1])[0]
  line(im,[(x,y),(min(63,x+L),y)],c)
  if c>=6:dot(im,min(63,x+L+2),y,5)
save('blue-ripples',im)
im=canvas(44,160);r=random.Random(909)
for y in range(0,160,3):
 width=5+int(y*.035);cx=22+r.randrange(-6,7)
 line(im,[(cx-width,y),(cx+width,y)],17)
 if y%9!=0:line(im,[(cx-width+3,y),(cx+width-2,y)],18 if y<90 else 17)
 if y<65:line(im,[(cx-2,y),(cx+3,y)],19)
 for k in [-1,1]:
  x=cx+k*(width+4+r.randrange(5));line(im,[(x,y),(x+2,y)],16)
save('scarlet-reflection',im)
# Shore promontory with crisp frosted rim and irregular mass.
im=canvas(76,58)
poly(im,[(0,13),(8,16),(19,26),(31,30),(37,37),(49,41),(57,47),(72,50),(75,55),(0,57)],1)
poly(im,[(0,27),(9,29),(21,33),(28,37),(39,39),(43,44),(57,47),(66,51),(33,51),(18,46),(0,43)],10)
line(im,[(0,33),(9,35),(18,37),(26,41),(34,42),(43,46),(56,49),(64,51),(74,52)],6)
for x,y,h in [(3,1,32),(13,13,28),(26,23,24),(38,33,16),(49,40,12)]:pine(im,x,y,h,1,5)
for x,y,h in [(18,19,21),(42,35,13)]:
 line(im,[(x,y),(x,y+h)],22);line(im,[(x-5,y+5),(x,y+9),(x+5,y+4)],6);line(im,[(x-4,y+12),(x,y+14),(x+4,y+9)],22)
for x in range(3,70,6):dot(im,x,48+x//15,8)
save('frosted-point',im)
# Faceted shoreline stones with ice caps. Three distinct masses.
for name,w,h,seed,pts in [('boulder',30,26,9,[(0,21),(3,12),(10,4),(19,2),(25,9),(29,21),(24,25),(4,25)]),('flat-stones',38,18,4,[(0,15),(5,7),(12,5),(19,9),(25,1),(32,3),(37,15),(29,17),(5,17)]),('small-rock',17,15,22,[(0,12),(4,4),(10,1),(14,5),(16,12),(12,14),(2,14)])]:
 im=canvas(w,h);poly(im,pts,1);poly(im,[(x,max(0,y-1)) for x,y in pts[:-2]]+[(w//2,h-3),(3,h-4)],11)
 poly(im,[(w//3,5),(w//2,3),(w//2+4,8),(w//3+1,h-3),(3,h-4)],12)
 poly(im,[(w//2+3,7),(w-5,h//2),(w-3,h-3),(w//2,h-2)],10)
 grain(im,seed,[10,11,12,13],w*h//6)
 line(im,pts[1:4],7);line(im,[(pts[1][0],pts[1][1]-1),(pts[2][0],pts[2][1]-1),(pts[3][0]-2,pts[3][1])],8)
 for x,y in pts[1:3]:line(im,[(x,y),(x,y+4)],22)
 save(name,im)
im=canvas(30,38)
for x,y,tip in [(3,37,8),(7,36,0),(11,37,13),(15,37,5),(20,37,10),(24,37,3),(28,37,17)]:
 bend=-4 if x<15 else 3;line(im,[(x,y),(x-1,tip+11),(x+bend,tip+3)],13)
 line(im,[(x-1,y-2),(x-2,tip+12),(x+bend-1,tip+4)],7)
 line(im,[(x+bend-1,tip+8),(x+bend-2,tip+3),(x+bend,tip),(x+bend+2,tip+2)],9)
save('silver-reeds',im)
im=canvas(18,24)
poly(im,[(2,22),(5,7),(8,3),(11,16),(14,9),(17,22)],23)
poly(im,[(5,18),(8,3),(8,20)],22);line(im,[(7,6),(8,3),(10,14)],21)
line(im,[(13,19),(14,10),(16,19)],22);line(im,[(1,22),(16,22)],6)
save('ice-cluster',im)
# Independently shaped story ground: upper shoreline diagonal, bottom quiet soil.
im=canvas(256,91)
edge=[(0,0),(21,8),(36,12),(57,23),(80,28),(106,38),(126,40),(151,47),(173,47),(198,53),(218,48),(241,50),(255,43)]
poly(im,edge+[(255,90),(0,90)],10)
poly(im,[(0,22),(32,32),(58,42),(95,51),(124,53),(156,61),(183,57),(221,64),(255,55),(255,90),(0,90)],11)
line(im,edge,6,2);line(im,[(x,y+3) for x,y in edge],4)
r=random.Random(189)
for _ in range(800):
 x=r.randrange(256);y=r.randrange(91)
 if im.getpixel((x,y)):
  c=r.choice([10,11,12,4]);line(im,[(x,y),(min(255,x+r.randrange(1,5)),y)],c)
for x,y in edge[:-1]:line(im,[(x,y),(min(255,x+8),y)],7)
save('story-shore',im)
# Bent frosted foreground tree only for the wide shore view.
im=canvas(81,115)
poly(im,[(0,114),(0,66),(9,39),(21,21),(27,0),(38,0),(31,28),(16,57),(10,89),(8,114)],1)
poly(im,[(2,106),(6,70),(17,42),(28,22),(31,0),(34,0),(30,25),(20,47),(11,74),(6,110)],12)
for pts,w in [([(11,60),(24,36),(44,23),(70,18),(80,9)],4), ([(23,30),(44,8),(49,0)],4), ([(13,48),(9,20),(2,9)],3), ([(43,24),(54,37),(75,42)],2), ([(51,20),(61,4),(69,0)],2)]:
 line(im,pts,1,w);line(im,[(x,y-2) for x,y in pts],6)
r=random.Random(348)
for _ in range(150):
 x=r.randrange(5,81);y=r.randrange(0,46)
 if (x+y*2)%13<4:
  line(im,[(x,y),(x+2,y)],7);dot(im,x,y+1,6)
save('shore-tree',im)
# Bounded art refinement: airy mist, broken cloud masses, slope-following rock
# detail and frost clusters. These replace drafting grids before r3 submission.
im=canvas(128,44)
r=random.Random(908)
for x,y,w,h in [(0,9,18,5),(13,12,22,5),(28,17,19,5),(42,14,22,6),(57,20,18,5),(73,22,24,6),(92,16,19,5),(105,13,23,6),(15,2,22,3),(68,7,20,4)]:
 poly(im,[(x,y),(x+3,y-2),(x+w//2,y-1),(x+w-4,y-3),(x+w,y),(x+w-2,y+h),(x+w//2,y+h-1),(x+4,y+h+2),(x,y+h-1)],15)
 line(im,[(x+2,y+h-1),(x+7,y+h),(x+w//2,y+h-2),(x+w-2,y+h-1)],16)
 for _ in range(w//2):
  xx=x+r.randrange(w);yy=y+r.randrange(h+3)
  if 0<=xx<128 and 0<=yy<44 and im.getpixel((xx,yy)):
   line(im,[(xx,yy),(min(127,xx+r.randrange(1,4)),yy)],r.choice([15,16,17]))
 for xx in range(x+4,min(127,x+w-3),5):dot(im,xx,y+h+2,18)
save('scarlet-cloud',im)
im=canvas(112,18)
for pts,c in [([(0,13),(15,13),(21,11),(38,11),(46,8),(61,8),(68,10),(79,10),(85,12),(111,12)],5), ([(8,15),(24,15),(32,13),(58,13),(66,11),(82,11),(94,14),(105,14)],6), ([(28,16),(42,16),(49,15),(72,15),(82,16),(101,16)],5), ([(2,10),(13,10),(20,8),(31,8)],4)]:line(im,pts,c)
for pts in [[(11,14),(24,14),(31,12),(48,12)],[(58,10),(69,10),(75,12),(86,12)]]:line(im,pts,6)
save('mist-bank',im)
im=canvas(256,53)
poly(im,ridge+[(255,52),(0,52)],3)
for x,y in [(25,9),(47,4),(131,2),(190,16),(216,10),(241,8)]:
 poly(im,[(x,y),(x+5,y+7),(x+21,45),(x+7,34),(x-2,y+6)],4)
 line(im,[(x,y+1),(x+4,y+8),(x+9,y+14)],15)
 line(im,[(x+4,y+6),(x+8,y+11),(x+13,y+19)],16)
 for k in range(4,24,4):
  line(im,[(x+k//2-4,y+k),(x+k//2-6,y+k+4),(x+k//2-5,y+k+5)],2)
  line(im,[(x+k//2+4,y+k+3),(x+k//2+7,y+k+7)],5)
for x,y,h in [(4,33,17),(14,38,13),(36,40,12),(68,34,19),(76,36,16),(87,31,19),(105,35,17),(113,39,12),(153,40,13),(166,38,14),(181,38,15),(205,41,12),(231,37,14),(249,33,20)]:pine(im,x,y,h,4)
save('far-ridges',im)
im=assets['shore-tree'];r=random.Random(518)
for cx,cy,rx,ry in [(35,3,22,7),(57,5,22,8),(69,20,16,8),(28,22,13,7),(54,32,16,6),(13,6,11,9)]:
 for _ in range(rx*4):
  x=cx+r.randrange(-rx,rx+1);y=cy+r.randrange(-ry,ry+1)
  if 0<=x<81 and 0<=y<115 and ((x-cx)/rx)**2+((y-cy)/ry)**2<1:
   line(im,[(x,y),(min(80,x+2),y)],r.choice([5,6,7]));
   if (x+y)%5==0:dot(im,x,y-1,8)
save('shore-tree',im)
# Serialize authored indexed grids for canonical submission.
draft={}
for n,im in assets.items():
 rows=[''.join(TOKENS[im.getpixel((x,y))] for x in range(im.width)) for y in range(im.height)]
 draft[n]={'width':im.width,'height':im.height,'rows':rows}
(ROOT/'draft-grids.json').write_text(json.dumps(draft,separators=(',',':')))
(ROOT/'palette.json').write_text(json.dumps({'tokens':TOKENS[:len(PAL)],'rgba':PAL,'colors':COLORS},indent=2))
print(f'{len(assets)} original indexed drafts; no reference image read')
