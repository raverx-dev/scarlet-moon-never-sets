"""Correction 02: bounded native cluster edits from accepted a58f4eb grids.
Four rebuilt pieces. Other twelve assets and composition placements preserved.
No generated-image sampling, vector rendering, scaling or antialiasing.
"""
from pathlib import Path
from PIL import Image
import json
R=Path(__file__).resolve().parent
old=json.loads((R/'accepted_checkpoint/authoring_inputs.json').read_text())
P=old['palette'];T=''.join(e['text_token'] for e in P['entries']);A=old['assets']
def new(w,h,c='.'):
 global rows
 rows=[[c]*w for _ in range(h)]
def px(x,y,c):
 if 0<=y<len(rows) and 0<=x<len(rows[0]):rows[y][x]=c
def span(y,l,r,c):
 for x in range(l,r+1):px(x,y,c)
def stamp(x,y,ss,m={}):
 for j,s in enumerate(ss):
  for i,c in enumerate(s):
   if c!='.':px(x+i,y+j,m.get(c,c))
def save(n):A[n]={**A[n],'rows':[''.join(s) for s in rows]}
def profile(keys,y):
 for (a,l,r),(b,ll,rr) in zip(keys,keys[1:]):
  if a<=y<=b:return round(l+(ll-l)*(y-a)/(b-a)),round(r+(rr-r)*(y-a)/(b-a))
 return keys[-1][1:]
leaf=['....222....','..2233322..','.233433332.','2333332232.','.222322122.','..1122111..','....11.....']
# Distant opening: irregular canopy pockets, many slim partially occluded trees.
# No concentric funnel/wedge or bright flat spotlight.
new(80,112,'1')
for y in range(90):
 l,r=profile([(0,5,73),(19,8,76),(41,3,69),(63,13,65),(89,25,54)],y)
 span(y,l,r,'2')
for x,top,end,w,lean in [(7,0,75,3,2),(18,2,81,2,-2),(31,0,71,3,3),(45,0,90,2,1),(61,4,79,4,-3),(73,0,62,2,-2)]:
 for y in range(top,end):
  xx=x+round(lean*y/max(1,end))+(1 if y%29>22 else 0)
  span(y,xx,xx+w,'1')
for x,y in [(1,3),(18,10),(34,0),(54,6),(67,22),(8,32),(29,29),(46,23),(57,45),(16,53),(37,61),(26,77),(48,83)]:stamp(x,y,leaf,{'4':'3','3':'2','2':'2','1':'1'})
save('depth-opening')
# Far grove: unequal upright boles; compact forks high in crowns only.
new(56,104)
for keys,end,shade in [([(0,3,7),(23,5,9),(52,2,7),(81,3,9),(96,0,13)],97,'1'), ([(0,23,26),(28,21,25),(61,24,28),(83,22,28)],84,'2'), ([(0,45,50),(32,42,47),(67,44,49),(99,39,52)],100,'1')]:
 for y in range(end):
  l,r=profile(keys,y);span(y,l,r,shade)
  if y%19<13:span(y,l+1,l+1,'2' if shade=='1' else '3')
# Small irregular lateral limbs, deliberately not repeating diagonal lattice.
for x,y,ss in [(6,18,['...11','..111','.111.','111..']), (39,31,['11....','.111..','..1111','....11']), (24,7,['22...','222..','.222.','..22.'])]:stamp(x,y,ss)
for x,y in [(-4,0),(11,5),(28,-2),(42,9),(1,22),(24,17),(39,33),(-5,44),(16,42),(34,55),(4,70),(25,78),(40,87)]:stamp(x,y,leaf,{'4':'3'})
save('far-grove')
# Mid tree: stout leaning hornbeam, solid bole with broad bark plates, no eye knot.
new(36,112)
keys=[(0,9,23),(16,11,26),(33,9,23),(52,7,21),(72,8,23),(90,6,24),(103,2,29),(111,0,33)]
for y in range(112):
 l,r=profile(keys,y);span(y,l,r,'1');span(y,l+2,r-2,'a');span(y,l+4,r-5,'b')
 # Short plates with staggered ends; no continuous string-like parallel ribbons.
 for off in [4,10]:
  x=l+off+(y//17%2)
  if y%17<11 and x<r-2:span(y,x,x+2,'c' if off==4 else 'a')
 if y%23 in [9,10]:span(y,l+5,min(r-2,l+10),'a')
for x,y,ss in [(21,21,['....11','...111','..1111','.11aa1','11aaa1','1aaa1.','aaa1..']), (0,47,['111......','1aa11....','.1aaa11..','..11aaa11','....11aaa'])]:stamp(x,y,ss)
for x,y in [(-2,0),(17,9),(23,30),(-3,44),(1,92)]:stamp(x,y,leaf,{'1':'a','2':'b','3':'c','4':'d'})
save('mid-tree')
# Foreground fork tree: angular old oak with a high split, wide block bark,
# one-sided buttress and blunt broken limb; no hollow knot.
new(40,160)
keys=[(0,6,30),(18,8,33),(39,13,35),(61,10,31),(87,7,28),(112,10,31),(132,8,32),(145,3,35),(159,0,39)]
for y in range(160):
 l,r=profile(keys,y);span(y,l,r,'g');span(y,l+2,r-2,'h');span(y,l+5,r-4,'i')
 if y<32:
  gap=19+y//9
  span(y,gap,gap+max(0,4-y//8),'.')
 for k in range(3):
  x=l+3+k*7+(y//14+k)%3
  if x<r-2:
   if (y+k*4)%18<13:span(y,x,min(x+2,r-2),'h')
   if (y+k*4)%18 in range(2,9):px(x+3,y,'j')
 if y%21 in [10,11]:span(y,l+5,min(r-3,l+10),'g')
 # Sparse moss shelves rather than a continuous outline.
 if y//9%4==1:span(y,r-3,r-1,'c')
for x,y,ss in [(0,62,['ggg.......','ghhgg.....','ghiiigg...','.ghiiiigg.','..ghhiiiig','....ghhiii','......ghhi'])]:stamp(x,y,ss)
for y in range(133,160):
 l,r=profile(keys,y);x=18-(y-133)//3
 span(y,x,x+2,'g')
 if y%9<6:span(y,x+3,x+4,'j')
for x,y in [(23,18),(2,72),(25,139)]:stamp(x,y,leaf,{'1':'a','2':'b','3':'c','4':'d'})
save('fork-trunk')
(R/'authoring_inputs.json').write_text(json.dumps({'palette':P,'assets':A},indent=2)+'\n')
for n,a in A.items():
 im=Image.new('RGBA',(a['width'],a['height']));im.putdata([tuple(P['entries'][T.index(c)]['rgba']) for row in a['rows'] for c in row]);im.save(R/'assets'/f'{n}.png')
print('Correction 02: four targeted pieces rebuilt; twelve retained')
