"""Explicit integer placements; two independent native compositions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
L={}
def scene(name,w):
 global P
 P=[];L[name]={'width':w,'height':240,'background':'1','placements':P}
def put(asset,x,y,flip=False):P.append({'asset':asset,'x':x,'y':y,'flip_x':flip})
scene('gameplay',192)
for y in range(112,240,32):
 for x in range(0,192,32):put('quiet-ground',x+(y//32%3)*5,y,(x//32+y//32)%2==1)
put('depth-opening',56,0)
for x,y,f in [(44,0,False),(88,-9,True),(115,7,False),(13,3,True)]:put('far-grove',x,y,f)
for x,y,f in [(20,31,False),(139,21,True),(1,57,True),(147,39,False)]:put('mid-tree',x,y,f)
for x,y,f in [(26,90,False),(129,84,True),(11,117,False),(149,121,True)]:put('understory',x,y,f)
for x,y,f in [(10,94,False),(43,78,True),(134,92,False)]:put('far-thicket',x,y,f)
put('elder-trunk',-8,-6);put('fork-trunk',157,4)
put('root-crook',-13,164,True);put('root-crook',156,173)
put('root-bank',-22,151);put('root-bank',158,155,True)
for x,y,f in [(-13,-8,False),(22,-25,False),(133,-15,True),(170,20,True),(-29,42,True)]:put('canopy',x,y,f)
for x,y,f in [(-10,108,False),(-9,162,False),(162,101,True),(171,167,True),(-15,208,False),(161,219,True)]:put('understory',x,y,f)
for x,y,f in [(8,187,False),(155,202,True),(-1,226,False),(177,229,True),(21,147,False)]:put('fern',x,y,f)
for x,y,f in [(18,171,False),(153,181,True),(2,222,False),(163,231,True)]:put('moss-seam',x,y,f)
for x,y,f in [(-18,187,False),(165,192,True),(-4,231,True),(167,230,False)]:put('understory',x,y,f)
put('lantern',13,55);put('lantern',176,91)
put('mushrooms',7,145);put('mushrooms',171,211,True)
put('firefly',43,91);put('firefly',149,143)
scene('story',256)
for y in range(112,240,32):
 for x in range(0,256,32):put('quiet-ground',x+(y//32%3)*5,y,(x//32+y//32)%2==1)
put('depth-opening',127,-12)
for x,y,f in [(27,-4,False),(75,-17,True),(128,-10,False),(168,3,True),(207,-15,False)]:put('far-grove',x,y,f)
for x,y,f in [(59,-25,False),(100,-29,True),(193,-8,True),(221,-14,False)]:put('mid-tree',x,y,f)
for x,y,f in [(27,73,False),(79,64,True),(165,70,False),(202,83,True)]:put('understory',x,y,f)
for x,y,f in [(15,82,False),(67,71,True),(122,78,False),(178,86,True)]:put('far-thicket',x,y,f)
put('elder-trunk',-12,-24);put('fork-trunk',218,-11)
put('root-crook',-21,152,True);put('root-crook',228,142)
put('root-bank',-16,133);put('root-bank',214,127,True)
for x,y,f in [(-12,-15,False),(30,-26,False),(83,-29,True),(180,-22,True),(225,0,True)]:put('canopy',x,y,f)
for x,y,f in [(-18,99,False),(221,112,True),(-10,157,False),(235,154,True),(-16,206,False),(225,222,True)]:put('understory',x,y,f)
for x,y,f in [(1,146,False),(220,151,True),(15,193,False),(239,208,True)]:put('fern',x,y,f)
for x,y,f in [(62,147,False),(99,138,False),(161,147,True),(24,171,False),(205,183,True)]:put('moss-seam',x,y,f)
put('lantern',27,36);put('lantern',231,54);put('mushrooms',13,133);put('mushrooms',224,142,True)
put('firefly',46,70);put('firefly',199,52)
(ROOT/'layouts.json').write_text(json.dumps(L,indent=2)+'\n')
