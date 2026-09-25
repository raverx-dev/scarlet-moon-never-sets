"""One bounded art correction: explicit seam clusters, grouped relief, independent staging."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
def grid(s):
 r=s.strip('\n').splitlines();return [x.ljust(max(map(len,r)),'.') for x in r]
def put(a,x,y,s):
 for j,row in enumerate(grid(s)):
  for i,c in enumerate(row):
   if c!='.' and 0<=y+j<len(a) and 0<=x+i<len(a[0]):a[y+j][x+i]=c
# Every seam contour below is explicit native pixel data; no interpolated line or noise field.
seams={
 'short':'''...kb\n...kb\n..kkb\n..kb.\n..kb.\n.kkb.\n.kb..\n.kb..\nkkb..''',
 'middle':'''......kb\n......kb\n......kb\n.....kkb\n.....kb.\n.....kb.\n....kkb.\n....kb..\n....kb..\n....kb..\n...kkb..\n...kb...\n...kb...\n..kkb...\n..kb....\n..kb....\n.kkb....\n.kb.....''',
 'long':'''.........kb\n.........kb\n.........kb\n........kkb\n........kb.\n........kb.\n........kb.\n.......kkb.\n.......kb..\n.......kb..\n......kkb..\n......kb...\n......kb...\n......kb...\n.....kkb...\n.....kb....\n.....kb....\n....kkb....\n....kb.....\n....kb.....\n...kkb.....\n...kb......\n...kb......\n..kkb......\n..kb.......\n..kb.......\n.kkb.......\n.kb........'''}
# Course edges have varied broken lengths, highlights and chips, unlike repeated tile strokes.
edges=[
'kkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkbbbkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkbbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',
'kkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkbbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',
'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',
'kkkkkkkkkkkbbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk']
for mode,w,h,courses,marks in [
 ('gameplay',192,112,[9,22,43,72,106],[(21,0,'short'),(57,0,'short'),(98,0,'short'),(139,0,'short'),(180,0,'short'),(5,11,'short'),(43,11,'short'),(84,11,'short'),(129,11,'short'),(169,11,'short'),(25,24,'middle'),(76,24,'middle'),(128,24,'middle'),(180,24,'middle'),(5,45,'long'),(64,45,'long'),(131,45,'long'),(33,76,'long'),(108,76,'long'),(183,76,'long')]),
 ('story',256,96,[10,27,51,84],[(12,0,'short'),(56,0,'short'),(100,0,'short'),(144,0,'short'),(192,0,'short'),(237,0,'short'),(33,12,'middle'),(94,12,'middle'),(157,12,'middle'),(218,12,'middle'),(10,29,'middle'),(81,29,'middle'),(154,29,'middle'),(231,29,'middle'),(44,55,'long'),(130,55,'long'),(216,55,'long')])]:
 a=[list('b'*w) for _ in range(h)]
 for i,y in enumerate(courses):
  put(a,0,y,edges[i%4]+edges[(i+2)%4])
 for x,y,kind in marks:put(a,x,y,seams[kind])
 # Selective stone-face planes, avoiding centered high-contrast noise.
 for x,y,s in [(14,2,'dddddddb'),(67,12,'dddddddddb'),(109,25,'dddddddb'),(22,46,'ddddddddddbb'),(87,75,'ddddddddddddbb'),(150,45,'ddddddddbb'),(39,109,'dddddbb'),(12,65,'dddb'),(166,96,'ddd'),(103,56,'dd'),(49,35,'ddd'),(227,53,'dddddddddb'),(178,87,'dddddddddddddb')]:put(a,x,y,s)
 light='''...ddddd........\n.ddsssssdd......\ndssmmsmsssdd....\n..sssmmssssd....\n....ssssddd.....\n......dd........'''
 for x,y in [(0,57),(w-16,51),(0,98),(w-17,84)]:put(a,x,y,light)
 data={'name':'paving-'+mode,'width':w,'height':h,'rows':[''.join(r) for r in a]}
 (P/('paving-'+mode+'.json')).write_text(json.dumps(data,indent=2)+'\n')
# Break the mountain's continuous pale ridge with broader, hand-positioned rock facets.
p=P/'mountain-range.json';d=json.loads(p.read_text());a=[list(r.replace('m','F')) for r in d['rows']]
for x,y,s in [(38,5,'''...ss......\n..ssFF.....\n.ssFFFF....\nssFFffFF...\n.FFfffFFF..\n..fffffFFF.\n....fffFF..'''),(16,11,'''..FFFF...\n.FFffFF..\nFFffffFF.\n.ffffffFF\n..fffFFFF'''),(65,13,'''....FFFF.....\n..FFFFFF.....\n.FFFffffFF...\nFFffffffffF..\n..ffffffffFF.\n....ffffffffF'''),(32,17,'''ffffbbbb....\nffbbbbbb....\nbbbbbbbbb...\nbbbbbbbbbbb.''')]:put(a,x,y,s)
d['rows']=[''.join(r) for r in a];p.write_text(json.dumps(d,indent=2)+'\n')
