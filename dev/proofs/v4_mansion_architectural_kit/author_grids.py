"""Prepare explicit indexed pixel grids for RoboPixel grid_paste.

This file is an authoring input, NOT the preview renderer or canonical store.
Final composition consumes only read-back RoboPixel exports in exports/.
No gradients, antialiasing, runtime vector artwork, or generated-image tracing.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = {}

class Grid:
    def __init__(self, w, h, fill='.'):
        self.w, self.h = w, h
        self.p = [list(fill*w) for _ in range(h)]
    def dot(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.p[y][x] = c
    def rect(self, x, y, w, h, c):
        for yy in range(y, y+h):
            for xx in range(x, x+w): self.dot(xx, yy, c)
    def row(self, y, x, s):
        for i,c in enumerate(s): self.dot(x+i,y,c)
    def save(self, name):
        ASSETS[name] = {'width': self.w, 'height': self.h, 'rows':[''.join(r) for r in self.p]}

# 32 x 64 window bay: individually stepped pointed arch, cut-stone joints,
# paired lancets and sparse clustered stained-glass facets, not noisy dithering.
g=Grid(32,64,'2')
g.rect(1,0,30,62,'3'); g.rect(3,2,26,57,'2')
for y in (8,20,32,44):
    g.rect(1,y,4,1,'4');g.rect(27,y+3,4,1,'1')
for x,y in ((2,12),(28,5),(1,37),(29,49)):g.rect(x,y,2,2,'4')
# Half widths of pointed arch at each native-pixel row.
halves=[1,2,3,4,5,6,7,8,9,10,10,11,11,12,12,12]
for j,hw in enumerate(halves):
    y=j+3; left=16-hw; right=15+hw
    g.rect(left,y,right-left+1,1,'5')
    g.dot(left,y,'6' if j%4 else '4');g.dot(right,y,'4')
    if hw>3: g.rect(left+3,y,right-left-5,1,'1')
for y in range(19,52):
    g.row(y,4,'654');g.row(y,25,'453')
    g.rect(7,y,18,1,'8');g.dot(7,y,'1');g.dot(24,y,'1')
for y in (20,28,36,44,51):
    g.rect(4,y,3,1,'3');g.rect(25,y,3,1,'2')
# Two slender internal pointed lancets; explicit small motifs repeat in glass.
for ox in (8,17):
    g.row(16,ox,'...5...');g.row(17,ox,'..515..');g.row(18,ox,'.51815.')
    g.row(19,ox,'5188815')
    for y in range(20,50):
        g.dot(ox,y,'5');g.dot(ox+6,y,'4')
    for y in (24,36,46):
        for dy,s in enumerate(['..9..','.999.','99899','.989.','..9..']):g.row(y+dy,ox+1,s)
    for x,y in ((ox+2,23),(ox+3,24),(ox+1,37),(ox+2,38)):g.dot(x,y,'A')
    g.rect(ox,33,7,1,'3');g.rect(ox,34,7,1,'5')
g.rect(15,17,2,35,'4');g.rect(15,21,1,29,'5')
g.row(10,12,'...66...');g.row(11,12,'..6886..');g.row(12,12,'.689986.');g.row(13,12,'..6886..');g.row(14,12,'...44...')
g.rect(3,52,26,1,'6');g.rect(2,53,28,2,'4');g.rect(4,55,24,2,'1')
g.rect(5,58,22,1,'4');g.rect(6,59,20,3,'2');g.rect(7,59,1,3,'5')
g.save('window-bay')

# Column atlas: cap rows 0:12, repeatable shaft 12:52, base 52:64.
g=Grid(16,64)
for y,s in enumerate([
 '..444444444444..','..566666666654..','.45555555555543.',
 '.65445445445443.','..543543543543..','...544444443....',
 '...654444543....','....6544543.....','....6544543.....',
 '....4544543.....','....6544543.....','....6544543.....']):g.row(y,0,s)
for y in range(12,52):
    g.row(y,4,'65445431')
    if y in (23,39):g.row(y,4,'45443431')
    if y in (24,40):g.dot(5,y,'5')
g.row(52,4,'65445431');g.row(53,3,'4655554431');g.row(54,3,'6544444431')
g.rect(2,55,12,1,'6');g.rect(2,56,12,2,'4');g.rect(1,58,14,1,'5')
g.rect(1,59,14,2,'3');g.rect(0,61,16,1,'5');g.rect(0,62,16,2,'1')
g.save('column')

# Subdued wall support; stepped inset panel, seams have no high-value speckles.
g=Grid(16,16,'2')
g.rect(1,1,14,1,'4');g.rect(1,2,1,13,'3');g.rect(14,2,1,13,'1')
g.rect(2,14,12,1,'1');g.rect(3,4,10,8,'3');g.rect(4,5,8,7,'2')
g.row(5,5,'..3...');g.row(6,5,'.343..');g.row(7,5,'..3...')
g.save('wall-panel')

# Running-bond blue-violet limestone. Long sparse veins, no random noise.
g=Grid(32,16,'3')
g.rect(0,0,32,1,'2');g.rect(0,1,32,1,'4')
g.rect(0,8,32,1,'2');g.rect(0,9,32,1,'4')
g.rect(7,1,1,7,'2');g.rect(23,9,1,7,'2')
g.row(4,17,'442');g.row(5,20,'42');g.row(12,3,'444');g.row(13,6,'42')
g.save('floor')

# Broad quiet velvet runner. Only two restrained 2px pile marks per repeat.
g=Grid(16,16,'B');g.row(4,3,'22');g.row(12,11,'22');g.save('carpet-field')
# Reusable left border wedge, moves 4px outward per 32px depth segment.
# Mirror to right. Transparent outside; carpet interior lives to the right.
g=Grid(16,32)
for y in range(32):
    x=7-y//8
    g.row(y,x,'2C54CB')
    if y%8 in (3,4):g.row(y,x+1,'C64C')
    if y%8 in (0,7):g.dot(x+2,y,'4')
g.save('carpet-border')

# Horizontal cornice + vertical border are distinct reusable trim pieces.
g=Grid(16,8,'1')
for y,s in enumerate(['5555555555555555','6666666666666666','4444444444444444','5253525352535253','4243424342434243','3333333333333333','5555555555555555','1111111111111111']):g.row(y,0,s)
g.save('trim-top')
g=Grid(8,16)
for y in range(16):g.row(y,0,'.165431.')
for y in (3,11):g.row(y,1,'14543')
g.save('trim-side')

# Focal apse panel. Hand-pixelled octagonal rose with eight stone spokes,
# warm centre and blue/red petals, plus recessed lower arched niche.
g=Grid(48,64,'2')
for y in range(2,60):
    g.row(y,2,'453');g.row(y,43,'341')
g.rect(2,1,44,1,'5');g.rect(2,61,44,1,'5');g.rect(1,62,46,1,'4')
for y in (8,20,32,44):
    g.rect(6,y,5,1,'3');g.rect(36,y+2,6,1,'3')
rose=[
 '.......555555.......',
 '.....5566666655.....',
 '...55654444445655...',
 '..5654899339984565..',
 '..6548999339989456..',
 '.564889993399988465.',
 '.654888993399888456.',
 '5649A4889339884A9465',
 '56499A44333344A99465',
 '56433333566533333465',
 '56433333577533333465',
 '564CCB44355344BCC465',
 '564CB488B33B884BC465',
 '.654888BB33BB888456.',
 '.56488BBB33BBB88465.',
 '..6548BBB33BBB8456..',
 '..56548BB33BB84565..',
 '...55654444445655...',
 '.....5566666655.....',
 '.......555555.......']
# The 20x20 jewel sits in a 32px stepped cut-stone surround.
for j,hw in enumerate([4,8,10,12,13,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,14,14,13,12,10,8,4]):
    y=5+j;g.rect(24-hw,y,2*hw,1,'4')
    g.dot(24-hw,y,'5');g.dot(23+hw,y,'3')
    if hw>3:g.rect(26-hw,y,2*hw-4,1,'1')
for j,row in enumerate(rose):
    for x,c in enumerate(row):
        if c!='.':g.dot(14+x,9+j,c)
g.rect(10,35,28,1,'5');g.rect(9,36,30,2,'3')
for y,hw in enumerate([2,4,6,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8]):
    g.rect(24-hw,40+y,hw*2,1,'4')
    if hw>2:g.rect(26-hw,40+y,hw*2-4,1,'1')
g.rect(12,58,24,1,'6');g.rect(10,59,28,1,'4');g.rect(8,60,32,1,'1')
g.save('rose-apse')

if __name__=='__main__':
    # Canonical palette uses symbol 0 for darkest opaque; align design notation.
    mapping=str.maketrans('123456789ABC','0123456789AB')
    for asset in ASSETS.values():
        asset['rows']=[row.translate(mapping) for row in asset['rows']]
    out=ROOT/'authoring_inputs.json'
    out.write_text(json.dumps(ASSETS,indent=2)+'\n')
    print(f'{len(ASSETS)} grid inputs written to {out}')
