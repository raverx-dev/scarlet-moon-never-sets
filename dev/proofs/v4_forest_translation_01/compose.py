"""Reproduce native proofs from exact indexed assets and explicit placements.
Normal mode requires canonical exports. --author-preview is pre-submission only.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageChops
import json,sys
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'palette.json').read_text());L=json.loads((ROOT/'layouts.json').read_text())
A=json.loads((ROOT/'authoring_inputs.json').read_text())['assets']
author='--author-preview' in sys.argv
assets={}
for n,a in A.items():
 if author:rows=a['rows']
 else:rows=json.loads((ROOT/'exports'/f'{n}.json').read_text())['matrix']['rows']
 im=Image.new('RGBA',(a['width'],a['height']));im.putdata([tuple(bytes.fromhex(C[s][1:]))+(255,) if s!='.' else (0,0,0,0) for r in rows for s in r]);assets[n]=im
 if not author:im.save(ROOT/'assets'/f'{n}.png')
font=ImageFont.load_default()
for name,layout in L.items():
 im=Image.new('RGBA',(layout['width'],240),C[layout['background']])
 for p in layout['placements']:
  a=assets[p['asset']]
  if p['flip_x']:a=a.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
  im.alpha_composite(a,(p['x'],p['y']))
 im=im.convert('RGB');im.save(ROOT/f'forest_{name}_preview_{im.width}x240.png')
 im.resize((im.width*3,720),Image.Resampling.NEAREST).save(ROOT/f'forest_{name}_3x.png')
 before=Image.open(ROOT/'references'/f'{name}-V3-source-render.png').convert('RGB')
 ref=Image.open(ROOT/'references'/f'{name}-REFERENCE-{im.width}x240.png').convert('RGB')
 board=Image.new('RGB',(im.width*6+48,534),'#10151e');draw=ImageDraw.Draw(board)
 for i,(v,title) in enumerate([(before,'V3 / public V4 source render'),(ref,'Accepted GENERATED REFERENCE'),(im,'Native RoboPixel candidate' if not author else 'Native authoring preview')]):
  x=12+i*(im.width*2+12);draw.text((x,12),title,fill='white',font=font);board.paste(v.resize((im.width*2,480),Image.Resampling.NEAREST),(x,36))
 board.save(ROOT/f'{name}_comparison.png')
 bg=Image.open(ROOT/'references/v3-background.png').convert('RGB').crop((0,0,im.width,240))
 mask=ImageChops.difference(before,bg).convert('L').point(lambda p:255 if p else 0)
 wit=im.copy();wit.paste(before,(0,0),mask);wit.save(ROOT/f'{name}_staging_witness.png')
 wit.resize((im.width*3,720),Image.Resampling.NEAREST).save(ROOT/f'{name}_staging_witness_3x.png')
# Atlas uses exact native cells doubled, never scaled for composition.
board=Image.new('RGB',(768,2048),'#10151e');draw=ImageDraw.Draw(board)
x=y=12;rowh=0
for n,im in assets.items():
 w=max(im.width*2,158);h=im.height*2+40
 if x+w>768:x=12;y+=rowh+12;rowh=0
 draw.text((x,y),n,fill='white',font=font);draw.text((x,y+13),f'{im.width} x {im.height}',fill='#91b1b8',font=font)
 scaled=im.resize((im.width*2,im.height*2),Image.Resampling.NEAREST);board.paste(scaled,(x,y+30),scaled)
 x+=w+12;rowh=max(rowh,h)
board.crop((0,0,768,y+rowh+12)).save(ROOT/'forest_asset_atlas_2x.png')
print('Composed gameplay192x240 and story256x240 from',len(assets),'assets')

# Immutable rejected checkpoint -> current canonical candidate.
for name,w in [('gameplay',192),('story',256)]:
 before=Image.open(ROOT/'rejected_checkpoint'/f'forest_{name}_preview_{w}x240.png').convert('RGB')
 after=Image.open(ROOT/f'forest_{name}_preview_{w}x240.png').convert('RGB')
 board=Image.new('RGB',(w*6+36,768),'#10151e');draw=ImageDraw.Draw(board)
 for i,(pic,title) in enumerate([(before,'REJECTED fa929a5'),(after,'CORRECTION candidate')]):
  x=12+i*(w*3+12);draw.text((x,12),title,fill='white',font=font);board.paste(pic.resize((w*3,720),Image.Resampling.NEAREST),(x,36))
 board.save(ROOT/f'{name}_correction_before_after.png')

# Owner-accepted working checkpoint -> current revised candidate.
for name,w in [('gameplay',192),('story',256)]:
 before=Image.open(ROOT/'accepted_checkpoint'/f'forest_{name}_preview_{w}x240.png').convert('RGB')
 after=Image.open(ROOT/f'forest_{name}_preview_{w}x240.png').convert('RGB')
 board=Image.new('RGB',(w*6+36,768),'#10151e');draw=ImageDraw.Draw(board)
 for i,(pic,title) in enumerate([(before,'ACCEPTED WORKING a58f4eb'),(after,'CORRECTION 02 / review candidate')]):
  x=12+i*(w*3+12);draw.text((x,12),title,fill='white',font=font);board.paste(pic.resize((w*3,720),Image.Resampling.NEAREST),(x,36))
 board.save(ROOT/f'{name}_working_before_after.png')
