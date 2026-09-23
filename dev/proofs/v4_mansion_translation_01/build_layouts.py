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
tile(s,'wall-masonry',0,0,256,240)
tile(s,'wall-masonry',106,0,127,139,crop=[2,2,1,1])
floor(s,256,149,173)
runner(s,154,141,198,-28,249)
for x,y in ((151,178),(139,215)):stamp(s,'runner-motif',x,y)
# Offset far elevation. Nearer rose and stair stay native, surrounded differently.
stamp(s,'rose',146,8)
for x in (145,163,181):stamp(s,'lancet',x,65)
for x in (131,199):column(s,x,44,95)
for x in (109,204):stamp(s,'banner',x,16)
for x in (120,209):stamp(s,'candelabra',x,108)
for x in (104,200,224):stamp(s,'balustrade',x,128)
stamp(s,'stairs',140,135)
# Left gallery turns toward the viewer in descending courses, then a nearer bay.
for x,y in ((72,16),(27,41),(-18,68)):
    stamp(s,'arch',x,y);stamp(s,'lancet',x+16,y+21)
    stamp(s,'balustrade',x+9,y+73)
for x,y,h in ((66,11,133),(21,34,137)):
    column(s,x,y,h);stamp(s,'banner',x+17,y+13)
column(s,-10,0,197,True)
column(s,243,0,181,True)
stamp(s,'arch',-17,-34,crop=[0,0,48,40])
# Right wall remains quieter to support a standing character silhouette.
stamp(s,'lancet',224,66)
# No foreground cornice crossing candle stems or the open stage.

layouts={'schema':'mansion-translation-layout/v1','transforms':['integer-placement','crop','repeat','horizontal-reflection'],
'gameplay':{'width':192,'height':240,'operations':g},'story':{'width':256,'height':240,'operations':s},
'staging':{'gameplay_quiet_lane':[66,124,60,116],'story_actor_zones':[[44,128,32,44],[201,124,32,44]],'dialogue_box':[4,178,248,58]}}
(R/'layouts.json').write_text(json.dumps(layouts,separators=(',',':'))+'\n')
print('Wrote two independent layouts')
