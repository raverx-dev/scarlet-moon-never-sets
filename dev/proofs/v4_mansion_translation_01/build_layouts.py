"""Explicit native-piece placement design; no asset/image authoring.
Perspective uses cropped material rows, not resampling. All geometry is a map
of canonical pixel placements. Input reference images are not opened here.
"""
import json
from pathlib import Path
R=Path(__file__).resolve().parent

def stamp(o,a,x,y,**kw):o.append(dict(op='stamp',asset=a,x=x,y=y,**kw))
def tile(o,a,x,y,w,h,**kw):
    if w>0 and h>0:o.append(dict(op='tile',asset=a,x=x,y=y,w=w,h=h,**kw))
def column(o,x,y,h,near=False):
    if near:
        stamp(o,'near-pier',x,y,crop=[0,0,24,12]);tile(o,'near-pier',x,y+12,24,h-29,crop=[0,12,24,24]);stamp(o,'near-pier',x,y+h-17,crop=[0,79,24,17])
    else:
        stamp(o,'column',x,y,crop=[0,0,16,12]);tile(o,'column',x,y+12,16,h-24,crop=[0,12,16,16]);stamp(o,'column',x,y+h-12,crop=[0,52,16,12])
def floor(o,w,start,vp):
    # Growing native stone courses. Row segments select a dark or light swatch.
    bounds=[start,start+5,start+13,start+24,start+39,start+60,start+89,start+127,240]
    bounds=sorted(set(min(240,b) for b in bounds))
    for band,(top,bottom) in enumerate(zip(bounds,bounds[1:])):
        for y in range(top,bottom):
            unit=10+(y-start)//3
            for k in range(-30,30):
                x=vp+k*unit;end=x+unit
                if end<=0 or x>=w:continue
                l=max(0,x);r=min(w,end)
                sx=0 if (k+band)%2 else 16
                sy=15 if y==bottom-1 else (3+(y-top)%3 if y-top in (2,3,4) else 12)
                tile(o,'paving',l,y,r-l,1,crop=[sx,sy,15,1])
                if x>=0:stamp(o,'paving',x,y,crop=[15,0,1,1])
def runner(o,start,left,right,endleft,endright):
    for y in range(start,240):
        t=(y-start)/(239-start);l=round(left+(endleft-left)*t);r=round(right+(endright-right)*t)
        tile(o,'runner',l,y,r-l+1,1,crop=[0,(y-start)%16,16,1])
        stamp(o,'runner-edge',l,y,crop=[0,(y-start)%16,8,1])
        stamp(o,'runner-edge',r-7,y,crop=[0,(y-start)%16,8,1],flip=True)

g=[]
tile(g,'wall-masonry',0,0,192,240)
tile(g,'wall-masonry',63,0,66,95,crop=[2,2,1,1])
# Quiet base of the nave, framed by taller receding side architecture.
floor(g,192,101,96)
runner(g,104,72,119,17,174)
for y in (136,184,226):stamp(g,'runner-motif',88,y)
# Far wall: rose above a triple lancet, raised carpeted landing.
stamp(g,'rose',68,2)
for x in (71,88,105):stamp(g,'lancet',x,55)
for x in (59,121):stamp(g,'far-pier',x,50)
stamp(g,'stairs',64,95)
for x in (43,125):stamp(g,'balustrade',x,94)
# Nested side bays. Columns overlap joins to read as architecture rather than tiles.
for x in (17,127):
    stamp(g,'arch',x,2);stamp(g,'lancet',x+16,23)
    stamp(g,'balustrade',x+12,78)
for x in (5,167):stamp(g,'banner',x,17)
for x in (47,129):column(g,x,5,113)
for x in (-22,166):
    stamp(g,'arch',x,56);stamp(g,'lancet',x+16,78)
for x in (1,179):stamp(g,'candelabra',x,116)
for x in (48,132):stamp(g,'candelabra',x,82)
for x in (-10,178):column(g,x,38,167,True)
# A thin dark cornice across the crop anchors the roof without closing the view.
tile(g,'trim-top',0,0,192,4,crop=[0,4,16,4])

s=[]
# One near-frontal elevation and one floor vanishing point at x=128, y=96.
# The floor's native strip spacing and the runner edges converge together.
tile(s,'wall-masonry',0,0,256,240)
tile(s,'wall-masonry',78,0,100,126,crop=[2,2,1,1])
floor(s,256,126,128)
runner(s,126,105,150,20,235)
for y in (153,206):stamp(s,'runner-motif',120,y)
# Continuous rear plinth: ends stop at the stair opening, all on one plane.
for x,w in ((0,96),(160,96)):
    tile(s,'trim-top',x,120,w,6,crop=[0,0,16,6])
# Rose, lancets, stair and runner share the same center line.
stamp(s,'rose',100,4)
for x in (104,120,136):stamp(s,'lancet',x,61)
stamp(s,'stairs',96,102)
# Side bays belong to the same frontal wall; no descending diagonal gallery.
for x in (14,194):
    stamp(s,'arch',x,20)
    stamp(s,'lancet',x+16,43)
    stamp(s,'balustrade',x+12,102)
for x in (64,176):column(s,x,8,118)
# Banners occupy their own wall strips, clear of glass and column shafts.
for x in (80,156):stamp(s,'banner',x,22)
for x in (83,161):stamp(s,'candelabra',x,98)
# A matched foreground frame defines the shallow stage without blocking actors.
for x in (-10,242):column(s,x,0,166,True)
tile(s,'trim-top',0,0,256,4,crop=[0,4,16,4])

layouts={'schema':'mansion-translation-layout/v1','transforms':['integer-placement','crop','repeat','horizontal-reflection'],
'gameplay':{'width':192,'height':240,'operations':g},'story':{'width':256,'height':240,'operations':s},
'staging':{'gameplay_quiet_lane':[66,124,60,116],'story_actor_zones':[[44,128,32,44],[180,128,32,44]],'dialogue_box':[4,174,248,62]}}
(R/'layouts.json').write_text(json.dumps(layouts,separators=(',',':'))+'\n')
print('Wrote two independent layouts')
