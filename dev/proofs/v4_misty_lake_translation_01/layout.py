"""Explicit native integer placements; each scene has its own camera/staging."""
import json
from pathlib import Path
ROOT=Path(__file__).parent
def scene(w):return {'width':w,'height':240,'background':'#101b42','placements':[]}
def put(s,a,x,y,flip=False):s['placements'].append({'asset':a,'x':x,'y':y,**({'flip_x':True} if flip else {})})
g=scene(192)
for x in [0,128]:
 for y in [64,192]:put(g,'deep-water',x,y)
put(g,'twilight',0,0);put(g,'scarlet-moon',132,8)
put(g,'scarlet-cloud',-40,-5);put(g,'scarlet-cloud',85,3);put(g,'scarlet-cloud',21,-24)
put(g,'far-ridges',-27,30);put(g,'west-woods',-17,9);put(g,'east-woods',127,26)
put(g,'distant-torii',5,8)
put(g,'scarlet-reflection',127,78)
for a,x,y,f in [('mist-bank',1,59,False),('mist-bank',105,64,True),('frosted-point',-15,36,False),('frosted-point',170,53,True),('blue-ripples',-14,83,False),('blue-ripples',157,93,True),('blue-ripples',-6,179,True)]:put(g,a,x,y,f)
for a,x,y,f in [('silver-reeds',-7,92,False),('boulder',-12,123,False),('small-rock',16,137,False),('ice-cluster',2,139,False),('silver-reeds',179,140,True),('boulder',168,171,True),('flat-stones',166,190,True),('ice-cluster',177,181,True),('silver-reeds',-9,181,False),('boulder',-6,211,False),('flat-stones',13,227,False),('small-rock',41,232,False),('silver-reeds',169,209,True),('boulder',161,231,True)]:put(g,a,x,y,f)
s=scene(256)
for x in [0,128]:
 for y in [75,203]:put(s,'deep-water',x,y)
put(s,'twilight',0,0);put(s,'scarlet-moon',186,10)
put(s,'scarlet-cloud',130,0);put(s,'scarlet-cloud',21,-18);put(s,'scarlet-cloud',-69,7)
put(s,'far-ridges',0,34);put(s,'west-woods',0,23);put(s,'east-woods',176,33)
put(s,'distant-torii',34,24)
put(s,'scarlet-reflection',178,91)
put(s,'mist-bank',38,73);put(s,'mist-bank',149,77,True)
put(s,'frosted-point',-4,45)
put(s,'blue-ripples',2,97);put(s,'blue-ripples',115,115,True);put(s,'blue-ripples',222,94)
put(s,'story-shore',0,149)
for a,x,y,f in [('silver-reeds',-6,115,False),('boulder',5,144,False),('flat-stones',31,159,False),('boulder',63,169,False),('flat-stones',105,182,False),('small-rock',152,185,False),('boulder',202,181,True),('ice-cluster',90,174,False),('silver-reeds',232,151,True),('ice-cluster',225,183,True),('boulder',-9,209,False),('silver-reeds',5,198,False),('flat-stones',218,227,True),('silver-reeds',238,208,True)]:put(s,a,x,y,f)
put(s,'shore-tree',-2,-7)
(ROOT/'layouts.json').write_text(json.dumps({'gameplay':g,'story':s},indent=2))
