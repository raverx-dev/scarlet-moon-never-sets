"""Deterministic proof-only assembly from exact RoboPixel preview exports.

Requires Python 3 + Pillow. No game runtime imports or writes. Every scene pixel
comes from a canonical kit asset; transforms are integer placement, crop, repeat,
and horizontal reflection. No resampling, gradients, lighting filters or vectors.
"""
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
assets={}
exports={}
for path in sorted((ROOT/'exports').glob('*.json')):
    e=json.loads(path.read_text());m=e['matrix']; exports[path.stem]=e
    im=Image.new('RGBA',(m['width'],m['height']))
    for y,row in enumerate(m['rows']):
        for x,s in enumerate(row):
            p=m['symbols'][s]
            if not p.get('transparent'):im.putpixel((x,y),tuple(bytes.fromhex(p['hex'][1:]))+(255,))
    assets[path.stem]=im

def scene(width,operations):
    im=Image.new('RGBA',(width,240))
    for op in operations:
        a=assets[op['asset']]
        if 'crop' in op:
            x,y,w,h=op['crop'];a=a.crop((x,y,x+w,y+h))
        if op.get('flip'):a=a.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        x,y=op['x'],op['y']
        if op['op']=='tile':
            w,h=op['w'],op['h']
            for yy in range(0,h,a.height):
                for xx in range(0,w,a.width):
                    tile=a.crop((0,0,min(a.width,w-xx),min(a.height,h-yy)))
                    im.alpha_composite(tile,(x+xx,y+yy))
        else:im.alpha_composite(a,(x,y))
    assert im.getextrema()[3]==(255,255), 'Scene has unpainted pixels'
    return im.convert('RGB')

def stamp(ops,asset,x,y,**kw):ops.append(dict(op='stamp',asset=asset,x=x,y=y,**kw))
def tile(ops,asset,x,y,w,h,**kw):ops.append(dict(op='tile',asset=asset,x=x,y=y,w=w,h=h,**kw))
def column(ops,x,y,h):
    stamp(ops,'column',x,y,crop=[0,0,16,12])
    tile(ops,'column',x,y+12,16,h-24,crop=[0,12,16,16])
    stamp(ops,'column',x,y+h-12,crop=[0,52,16,12])
def runner(ops,cx,y,end_y,half):
    # Matching border wedges join without a seam and widen 4px every 32px.
    for top in range(y,end_y,32):
        band_h=min(32,end_y-top)
        left=cx-half-7;right=cx+half-9
        for dy in range(band_h):
            edge=7-dy//8
            tile(ops,'carpet-field',left+edge+5,top+dy,right+10-edge-(left+edge+5),1,
                 crop=[0,(top+dy)%16,16,1])
        stamp(ops,'carpet-border',left,top,crop=[0,0,16,band_h])
        stamp(ops,'carpet-border',right,top,crop=[0,0,16,band_h],flip=True)
        half+=4

game=[]
tile(game,'wall-panel',0,0,192,240,crop=[0,0,1,1])
tile(game,'wall-masonry',0,0,192,240)
# Explicit floor bands are deliberately stepped; all material is the floor tile.
for x,y,w,h in [(40,72,112,40),(32,112,128,40),(24,152,144,40),(16,192,160,48)]:
    tile(game,'floor',x,y,w,h)
stamp(game,'rose-apse',72,8)
tile(game,'trim-top',48,68,96,8)
runner(game,96,76,240,25)
for x in (12,148):stamp(game,'window-bay',x,55)
for x in (-8,168):stamp(game,'window-bay',x,143)
for x in (8,152):tile(game,'wall-panel',x,119,32,16)
for x in (0,176):tile(game,'wall-panel',x,207,16,32)
for x in (0,176):column(game,x,48,89)
for x in (40,136):column(game,x,44,95)
for x in (16,160):column(game,x,134,106)
tile(game,'trim-top',0,0,192,8)
tile(game,'trim-side',0,8,8,40)
tile(game,'trim-side',184,8,8,40,flip=True)

story=[]
tile(story,'wall-panel',0,0,256,240,crop=[0,0,1,1])
tile(story,'wall-masonry',0,0,256,240)
tile(story,'floor',0,112,256,128)
stamp(story,'rose-apse',104,16)
# Entire rear elevation reads horizontally; it is not an extended gameplay crop.
for x in (36,188):stamp(story,'window-bay',x,24)
tile(story,'wall-panel',20,80,16,16)
tile(story,'wall-panel',68,80,120,16)
tile(story,'wall-panel',220,80,16,16)
tile(story,'trim-top',0,94,256,8)
tile(story,'trim-top',80,102,96,8)
tile(story,'trim-top',72,112,112,8)
for x in (12,76,164,228):column(story,x,8,104)
runner(story,128,120,240,31)
tile(story,'trim-top',0,0,256,8)
# Foreground piers frame the stage at its outside edges, leaving both actors free.
for x in (-8,248):column(story,x,92,148)

layouts={'schema':'scarlet-mansion-proof-layout/v1','transforms':['integer-translation','crop','repeat','horizontal-reflection'],
 'gameplay':{'width':192,'height':240,'operations':game},
 'story':{'width':256,'height':240,'operations':story},
 'staging':{'gameplay_quiet_lane':[76,112,40,128],'story_actor_zones':[[44,124,32,44],[180,124,32,44]],'dialogue_box':[4,174,248,62]}}
(ROOT/'layouts.json').write_text(json.dumps(layouts,indent=2)+'\n')
for name,ops,width in [('gameplay',game,192),('story',story,256)]:
    im=scene(width,ops)
    im.save(ROOT/f'mansion_{name}_preview_{width}x240.png')
    im.resize((width*3,720),Image.Resampling.NEAREST).save(ROOT/f'mansion_{name}_3x.png')

# Labelled atlas is review evidence only. Labels are not canonical art.
atlas=Image.new('RGB',(480,208),'#11111d');d=ImageDraw.Draw(atlas)
positions={'window-bay':(8,24),'column':(104,24),'rose-apse':(200,24),'wall-panel':(296,24),
           'wall-masonry':(392,24),'floor':(8,128),'carpet-field':(104,128),'carpet-border':(200,128),
           'trim-top':(296,128),'trim-side':(392,128)}
for key,(x,y) in positions.items():
    a=assets[key];atlas.paste(a,(x,y),a)
    d.text((x,y-14),key,fill='#ddd3dd')
    d.text((x,y+a.height+4),f'{a.width}x{a.height}',fill='#938599')
atlas.save(ROOT/'mansion_asset_atlas.png')
atlas.resize((1440,624),Image.Resampling.NEAREST).save(ROOT/'mansion_asset_atlas_3x.png')

if __name__=='__main__':
    print('Rendered both native compositions, 3x views, atlas and layouts.json.')
