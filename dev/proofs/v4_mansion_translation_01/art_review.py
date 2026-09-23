"""Art comparison and fixed static bullet witnesses; no runtime execution.
Only review overlays are painted here, never canonical environment pixels.
Diamond/star primitives and colors come from unchanged V3 drawBullet.
"""
import json,re,subprocess,hashlib
from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;BASE='4ef4080fc17f53f03393ac74e205220072360c0b';repo=R.parents[2]
source=subprocess.check_output(['git','show',BASE+':versions/sprite-redesign/index.html'],cwd=repo,text=True)
colors=dict(re.findall(r"(\w+):'([^']+)'",re.search(r'const C=\{(.*?)\};',source).group(1)))
placements=[{'x':x,'y':y,'shape':'diamond' if j%2==0 else 'star','color':('cyan','pink','gold')[j%3]} for j,y in enumerate((132,158,184)) for x in (48,72,96,120,144)]
def bullets(im):
    d=ImageDraw.Draw(im)
    def rect(x,y,w,h,c):d.rectangle((x,y,x+w-1,y+h-1),fill=c)
    for b in placements:
        x,y=b['x'],b['y'];c=colors[b['color']]
        if b['shape']=='diamond':
            for yy in range(-3,4):rect(x-(3-abs(yy)),y+yy,1+2*(3-abs(yy)),1,c)
            rect(x,y-1,1,3,colors['white'])
        else:
            rect(x-1,y-4,2,9,c);rect(x-4,y-1,9,2,c);rect(x-2,y-2,5,5,c);rect(x-1,y-1,2,2,colors['white'])
    return im
before=bullets(Image.open(R/'accepted_composition_checkpoint/mansion_gameplay_scale.png').convert('RGB'))
after=bullets(Image.open(R/'mansion_gameplay_scale.png').convert('RGB'));after.save(R/'mansion_gameplay_bullet_witness.png')
board=Image.new('RGB',(384,260),'#080810');d=ImageDraw.Draw(board);board.paste(before,(0,20));board.paste(after,(192,20));d.text((4,4),'ACCEPTED + FIXED BULLETS',fill='#d4c4a8');d.text((196,4),'ART DEVELOPMENT 01',fill='#d4c4a8');board.save(R/'bullet_readability_before_after.png')
(R/'bullet_witnesses.json').write_text(json.dumps({'source_commit':BASE,'source_file':'versions/sprite-redesign/index.html','source_sha256':hashlib.sha256(source.encode()).hexdigest(),'primitive':'drawBullet diamond/star integer rectangles','colors':colors,'placements':placements,'limits':'Fixed static comparison; not a combat simulation or runtime screenshot.'},indent=2)+'\n')
print('Static before/after bullet witnesses generated')
