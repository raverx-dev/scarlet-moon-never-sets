"""Static Mansion assembly from exact read-back RoboPixel preview matrices.

Only placement, crop, repeat and horizontal reflection are permitted; no
resampling or scene-level drawing. The original proof directory is untouched.
"""
import json
from pathlib import Path
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parent
exports={p.stem:json.loads(p.read_text()) for p in sorted((ROOT/'exports').glob('*.json'))}
assets={}
for name,e in exports.items():
    m=e['matrix'];im=Image.new('RGBA',(m['width'],m['height']))
    for y,row in enumerate(m['rows']):
        for x,s in enumerate(row):
            p=m['symbols'][s]
            if not p.get('transparent'):im.putpixel((x,y),tuple(bytes.fromhex(p['hex'][1:]))+(255,))
    assets[name]=im

def tile(ops,a,x,y,w,h,**kw):ops.append(dict(op='tile',asset=a,x=x,y=y,w=w,h=h,**kw))
def stamp(ops,a,x,y,**kw):ops.append(dict(op='stamp',asset=a,x=x,y=y,**kw))
def column(ops,x,y,h):
    stamp(ops,'column',x,y,crop=[0,0,16,12])
    tile(ops,'column',x,y+12,16,h-24,crop=[0,12,16,16])
    stamp(ops,'column',x,y+h-12,crop=[0,52,16,12])
def runner(ops,cx,y,end_y,half):
    for top in range(y,end_y,32):
        bh=min(32,end_y-top);left=cx-half-7;right=cx+half-9
        for dy in range(bh):
            edge=7-dy//8
            tile(ops,'carpet-field',left+edge+5,top+dy,right+10-edge-(left+edge+5),1,
                crop=[0,(top+dy)%16,16,1])
        stamp(ops,'carpet-border',left,top,crop=[0,0,16,bh])
        stamp(ops,'carpet-border',right,top,crop=[0,0,16,bh],flip=True)
        half+=4
def render(width,ops):
    im=Image.new('RGBA',(width,240))
    for o in ops:
        a=assets[o['asset']]
        if 'crop' in o:
            x,y,w,h=o['crop'];a=a.crop((x,y,x+w,y+h))
        if o.get('flip'):a=a.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        if o['op']=='tile':
            for yy in range(0,o['h'],a.height):
                for xx in range(0,o['w'],a.width):
                    im.alpha_composite(a.crop((0,0,min(a.width,o['w']-xx),min(a.height,o['h']-yy))),
                        (o['x']+xx,o['y']+yy))
        else:im.alpha_composite(a,(o['x'],o['y']))
    assert im.getextrema()[3]==(255,255)
    return im.convert('RGB')

game=[]
tile(game,'wall-masonry',0,0,192,240)
for x,y,w,h in ((52,68,88,16),(44,84,104,24)):
    tile(game,'far-floor',x,y,w,h)
for x,y,w,h in ((36,108,120,36),(28,144,136,40),(16,184,160,56)):
    tile(game,'floor',x,y,w,h)
stamp(game,'rose-apse',72,8)
tile(game,'trim-top',48,66,96,8)
runner(game,96,76,240,23)
for x in (21,147):stamp(game,'far-window-bay',x,25)
for x in (48,132):stamp(game,'far-pier',x,24)
for x in (7,153):stamp(game,'window-bay',x,95)
for x in (-10,170):stamp(game,'window-bay',x,174)
for x in (6,170):column(game,x,72,104)
for x in (22,154):column(game,x,153,87)
for x in (4,172):tile(game,'wall-panel',x,157,16,16)
tile(game,'trim-top',0,0,192,8)
tile(game,'trim-side',0,8,8,47)
tile(game,'trim-side',184,8,8,47,flip=True)

story=[]
tile(story,'wall-masonry',0,0,256,240)
tile(story,'far-floor',0,108,256,24)
tile(story,'floor',0,132,256,108)
stamp(story,'rose-apse',104,12)
for x in (32,192):stamp(story,'window-bay',x,22)
for x in (5,227):stamp(story,'far-window-bay',x,43)
for x in (77,167):stamp(story,'far-pier',x,56)
for x in (12,76,164,228):column(story,x,8,105)
tile(story,'wall-panel',20,82,64,16)
tile(story,'wall-panel',172,82,64,16)
tile(story,'trim-top',0,100,256,8)
tile(story,'trim-top',72,112,112,8)
runner(story,128,120,240,29)
tile(story,'trim-top',0,0,256,8)
for x in (-8,248):column(story,x,92,148)

layouts={'schema':'scarlet-mansion-refinement-layout/v1','transforms':['integer-translation','crop','repeat','horizontal-reflection'],
 'gameplay':{'width':192,'height':240,'operations':game},
 'story':{'width':256,'height':240,'operations':story},
 'staging':{'gameplay_quiet_lane':[76,112,40,128],'story_actor_zones':[[44,124,32,44],[180,124,32,44]],'dialogue_box':[4,174,248,62]}}

def main():
    (ROOT/'layouts.json').write_text(json.dumps(layouts,indent=2)+'\n')
    for name,w in [('gameplay',192),('story',256)]:
        im=render(w,layouts[name]['operations']);im.save(ROOT/f'mansion_{name}_preview_{w}x240.png')
        im.resize((w*3,720),Image.Resampling.NEAREST).save(ROOT/f'mansion_{name}_3x.png')
    atlas=Image.new('RGB',(4*104,4*102),'#11111d');d=ImageDraw.Draw(atlas)
    for i,(name,a) in enumerate(assets.items()):
        x=(i%4)*104+6;y=(i//4)*102+20
        atlas.paste(a,(x,y),a);d.text((x,y-14),name,fill='#ddd3dd')
    atlas.save(ROOT/'mansion_asset_atlas.png')
    # Paired native images are direct comparison, with no image resampling.
    old=ROOT.parent/'v4_mansion_architectural_kit'
    for name,w in [('gameplay',192),('story',256)]:
        before=Image.open(old/f'mansion_{name}_preview_{w}x240.png').convert('RGB')
        after=Image.open(ROOT/f'mansion_{name}_preview_{w}x240.png').convert('RGB')
        comp=Image.new('RGB',(w*2,240));comp.paste(before,(0,0));comp.paste(after,(w,0))
        comp.save(ROOT/f'{name}_proof_vs_refinement.png')
    print('Rendered native scenes, 3x review views, atlas, and direct proof comparisons.')

if __name__=='__main__':main()
