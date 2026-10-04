"""Static scale/staging evidence using unchanged V3 sprite matrices.

This is not a running-game capture or character revision. The dialogue rectangle
is a coverage witness at the existing UI bounds, not a new UI proposal.
"""
import json,re,subprocess,hashlib
from PIL import Image,ImageDraw
from compose import ROOT
repo=ROOT.parents[2]
source=subprocess.check_output(['git','show','d7054d2b9b111ff711f44cc3ee5b71268aca6ed8:versions/sprite-redesign/index.html'],cwd=repo,text=True)
c=dict(re.findall(r"(\w+):'([^']+)'",re.search(r'const C=\{(.*?)\};',source).group(1)))
pal={}
for key,value in re.findall(r'(\w+):([^,}]+)',re.search(r'const PAL=\{(.*?)\};',source).group(1)):
    pal[key]=c[value[2:]] if value.startswith('C.') else value.strip('"')
witness={}
def sprite(im,name,cx,cy):
    rows=re.findall(r"'([^']*)'",re.search(r'\b'+name+r':\[(.*?)\]',source,re.S).group(1))
    w=max(map(len,rows));h=len(rows)
    # Same centred integer sprite anchor as V3 blitRows.
    x0=cx-w//2;y0=cy-h//2
    for y,row in enumerate(rows):
        for x,s in enumerate(row):
            if s in pal:im.putpixel((x0+x,y0+y),tuple(bytes.fromhex(pal[s][1:])))
    witness[name]={'rows':rows,'source':'versions/sprite-redesign/index.html','anchor':[cx,cy],'dimensions':[w,h]}
story=Image.open(ROOT/'mansion_story_preview_256x240.png').convert('RGB')
sprite(story,'reimuStoryA',60,144);sprite(story,'sakuya',196,144)
d=ImageDraw.Draw(story);d.rectangle((4,174,251,235),fill='#080810',outline='#a18a92')
d.text((14,184),'DIALOGUE COVERAGE WITNESS',fill='#d4c4a8')
d.text((14,202),'Existing UI bounds: 248 x 62',fill='#8a8aa0')
d.text((14,218),'Static staging / no integration',fill='#8a8aa0')
story.save(ROOT/'mansion_story_staging.png')
game=Image.open(ROOT/'mansion_gameplay_preview_192x240.png').convert('RGB')
sprite(game,'reimu',96,208);sprite(game,'sakuya',96,96)
game.save(ROOT/'mansion_gameplay_scale.png')
(ROOT/'sprite_witnesses.json').write_text(json.dumps({'source_commit':'d7054d2b9b111ff711f44cc3ee5b71268aca6ed8','source_sha256':hashlib.sha256(source.encode()).hexdigest(),'palette':pal,'sprites':witness},indent=2)+'\n')
print('Static V3 sprite-scale and dialogue-coverage witnesses rendered.')
