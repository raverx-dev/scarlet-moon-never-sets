"""Deterministic drafting inputs for four RoboPixel mutations.

These grids are submitted to RoboPixel; only its read-back exports become scene
sources. The existing proof revisions remain selected solely in the proof folder.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent / 'v4_mansion_architectural_kit' / 'exports'

def old(name):
    return [list(s) for s in json.loads((OLD / f'{name}.json').read_text())['matrix']['rows']]

def put(a,x,y,s):
    for dx,c in enumerate(s):
        if 0 <= x+dx < len(a[0]) and 0 <= y < len(a): a[y][x+dx]=c

def line(a,x0,y0,x1,y1,c):
    dx=abs(x1-x0);dy=-abs(y1-y0);sx=1 if x0<x1 else -1;sy=1 if y0<y1 else -1;err=dx+dy
    while True:
        put(a,x0,y0,c)
        if (x0,y0)==(x1,y1):break
        e=2*err
        if e>=dy:err+=dy;x0+=sx
        if e<=dx:err+=dx;y0+=sy

rose=old('rose-apse')
# Leadwork and four stained-glass quadrants, leaving the existing stone rim.
for y in range(12,26):
    for x in range(16,32):
        if rose[y][x] in '789ABC':
            dx=x-23.5;dy=y-19
            if abs(dx)<1 or abs(dy)<1 or abs(abs(dx)-abs(dy)*1.13)<0.85:
                rose[y][x]='4'
            elif y<19 and x<24:rose[y][x]=('8' if (x+y)%4 else '9')
            elif y<19:rose[y][x]=('B' if (x+y)%3 else 'C')
            elif x<24:rose[y][x]=('7' if (x+y)%3 else '8')
            else:rose[y][x]=('A' if (x+y)%3 else 'B')
put(rose,22,18,'5665')
for x in (7,39):
    for y in (8,16,24,32):put(rose,x,y,'45' if x==7 else '54')
# The former unlit empty niche becomes a framed red-violet reliquary.
for y in range(44,57):
    for x in range(21,27):rose[y][x]='A' if y<53 else 'B'
for y in range(45,55,3):put(rose,23,y,'C')
put(rose,22,44,'5665');put(rose,20,55,'45555554')
for x,y in ((13,42),(33,42),(13,50),(33,50)):put(rose,x,y,'54')

floor=old('floor')
# Restrained longitudinal stone graining; preserves the original diamond lattice.
for y in (3,11):
    for x in (8,24):
        if floor[y][x]=='2':put(floor,x,y,'3')
for x,y in ((18,2),(3,7),(27,10),(11,14)):
    if floor[y][x]=='2':put(floor,x,y,'1')

# 24x48 far bay: narrower pointed head, one glass lancet, small sill.
bay=[list('1'*24) for _ in range(48)]
for y in range(2,43):
    put(bay,1,y,'2'*22)
for y in range(3,10):
    inset=max(0,9-y)
    put(bay,3+inset,y,'4'*(18-2*inset))
for y in range(7,38):
    span=min(8,(y-7)*2+1)
    left=12-span;right=11+span
    put(bay,left,y,'4'+'0'*max(0,right-left-1)+'3')
for y in range(14,36):
    for x in range(6,18):
        if bay[y][x]=='0':bay[y][x]='7' if (x+y)%5 else '8'
for x in (7,16):
    for y in range(17,36):
        if bay[y][x] in '78':bay[y][x]='4'
for y in (23,31):put(bay,6,y,'444444444444')
for x,y in ((8,18),(14,19),(10,27),(15,33)):put(bay,x,y,'9')
put(bay,3,38,'5'*18);put(bay,3,39,'3'*18)
put(bay,4,40,'2'*16);put(bay,4,42,'4'*16)
put(bay,0,46,'0'*24)

# 12x48 far pier, authored at native size with a lighter cap and shadow-side shaft.
pier=[list('.'*12) for _ in range(48)]
for y in range(4,41):put(pier,4,y,'543320')
for y in range(10,40,9):put(pier,4,y,'443320')
for y,s in enumerate(['..44444444..','.4555555543.','..43434343..','...544432...','....5432....']):put(pier,0,y,s)
for j,s in enumerate(['...354443...','..555555555.','..333333333.','.4444444444.','222222222222','000000000000']):put(pier,0,40+j,s)

# 24x8 small-cut flags for the distant threshold, authored independently.
far_floor=[list('2'*24) for _ in range(8)]
for x in range(0,24,12):
    for y in range(8):
        k=abs(y-3)
        put(far_floor,x+min(11,k*2),y,'3')
        put(far_floor,x+min(11,11-k*2),y,'1')
for x,y in ((4,2),(17,5)):put(far_floor,x,y,'3')

payload={
 'rose-apse':{'asset_id':'v4-mansion-proof-rose-apse-01','from_revision':4,'rows':[''.join(r) for r in rose]},
 'floor':{'asset_id':'v4-mansion-proof-floor-01','from_revision':4,'rows':[''.join(r) for r in floor]},
 'far-window-bay':{'asset_id':'v4-mansion-ref01-far-window-bay-01','rows':[''.join(r) for r in bay]},
 'far-pier':{'asset_id':'v4-mansion-ref01-far-pier-01','rows':[''.join(r) for r in pier]},
 'far-floor':{'asset_id':'v4-mansion-ref01-far-floor-01','rows':[''.join(r) for r in far_floor]},
}
(ROOT/'authoring_inputs.json').write_text(json.dumps(payload,indent=2)+'\n')
assert all(len({len(r) for r in p['rows']})==1 for p in payload.values())
if __name__=='__main__':
    print({k:(len(v['rows'][0]),len(v['rows'])) for k,v in payload.items()})
