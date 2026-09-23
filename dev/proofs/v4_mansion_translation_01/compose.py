"""Scene assembly ONLY from exact canonical RoboPixel export matrices.
Allowed operations: native placement, crop, repetition and horizontal reflection.
No generated-image pixels, interpolation, recoloring, geometry or lighting here.
Run build_layouts.py first only when intentionally editing layout source.
"""
import json
from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent

def decode(e):
    m=e['matrix'];im=Image.new('RGBA',(m['width'],m['height']))
    for y,row in enumerate(m['rows']):
        for x,s in enumerate(row):
            p=m['symbols'][s]
            if not p.get('transparent'):im.putpixel((x,y),tuple(bytes.fromhex(p['hex'][1:]))+(255,))
    return im

def assets():return {p.stem:decode(json.loads(p.read_text())) for p in sorted((R/'exports').glob('*.json'))}
def render(spec,kit):
    im=Image.new('RGBA',(spec['width'],spec['height']))
    for o in spec['operations']:
        a=kit[o['asset']]
        if 'crop' in o:
            x,y,w,h=o['crop'];assert min(x,y)>=0 and x+w<=a.width and y+h<=a.height
            a=a.crop((x,y,x+w,y+h))
        if o.get('flip'):a=a.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        if o['op']=='tile':
            for y in range(0,o['h'],a.height):
                for x in range(0,o['w'],a.width):
                    im.alpha_composite(a.crop((0,0,min(a.width,o['w']-x),min(a.height,o['h']-y))),(o['x']+x,o['y']+y))
        else:im.alpha_composite(a,(o['x'],o['y']))
    assert im.getextrema()[3]==(255,255)
    return im.convert('RGB')

def main():
    kit=assets();layouts=json.loads((R/'layouts.json').read_text())
    for name in ('gameplay','story'):
        spec=layouts[name];w=spec['width'];im=render(spec,kit)
        im.save(R/f'mansion_{name}_preview_{w}x240.png')
        im.resize((w*3,720),Image.Resampling.NEAREST).save(R/f'mansion_{name}_3x.png')
        # Compact board: reference / original proof / refinement proof / translation.
        board=Image.new('RGB',(w*4,260),'#080810');d=ImageDraw.Draw(board)
        sources=[R/'references'/f'{name}-direction.png',R.parent/'v4_mansion_architectural_kit'/f'mansion_{name}_preview_{w}x240.png',R.parent/'v4_mansion_refinement_01'/f'mansion_{name}_preview_{w}x240.png',R/f'mansion_{name}_preview_{w}x240.png']
        for i,(label,p) in enumerate(zip(('DIRECTION','ORIGINAL PROOF','REFINEMENT PROOF','TRANSLATION 01'),sources)):
            board.paste(Image.open(p),(i*w,20));d.text((i*w+4,4),label,fill='#d4c4a8')
        board.save(R/f'{name}_comparison.png')
    before=R/'story_before_correction'/'mansion_story_preview_256x240.png'
    if before.exists():
        pair=Image.new('RGB',(512,260),'#080810');d=ImageDraw.Draw(pair)
        for x,label,path in ((0,'BEFORE: MIXED ANGLE',before),(256,'CORRECTED: FRONTAL STAGE',R/'mansion_story_preview_256x240.png')):
            pair.paste(Image.open(path),(x,20));d.text((x+4,4),label,fill='#d4c4a8')
        pair.save(R/'story_before_after.png')
    atlas=Image.new('RGB',(4*136,4*132),'#080810');d=ImageDraw.Draw(atlas)
    for i,(name,a) in enumerate(kit.items()):
        x=(i%4)*136+6;y=(i//4)*132+24;atlas.paste(a,(x,y),a);d.text((x,y-19),name,fill='#d4c4a8');d.text((x,y+98),f'{a.width} x {a.height}',fill='#a18a92')
    atlas.save(R/'asset_atlas.png')
    print('Rendered native scenes, nearest-neighbor review images, comparisons and atlas')
if __name__=='__main__':main()
