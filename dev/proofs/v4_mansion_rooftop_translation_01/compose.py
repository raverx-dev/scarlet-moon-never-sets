#!/usr/bin/env python3
"""Compose selected canonical PNG exports with explicit integer placements only."""
import json,hashlib,sys
from pathlib import Path
from PIL import Image,ImageOps
ROOT=Path(__file__).resolve().parent
def compose(layout):
 out=Image.new('RGBA',tuple(layout['size']),(16,19,35,255))
 for op in layout['placements']:
  im=Image.open(ROOT/'canonical'/(op['asset']+'.png')).convert('RGBA')
  if op.get('crop'): im=im.crop(tuple(op['crop']))
  if op.get('mirror'): im=ImageOps.mirror(im)
  out.alpha_composite(im,(op['x'],op['y']))
 return out
if __name__=='__main__':
 for mode in ['gameplay','story']:
  layout=json.loads((ROOT/(mode+'_layout.json')).read_text());im=compose(layout)
  path=ROOT/(mode+'_native.png')
  if '--check' in sys.argv:
   assert im.tobytes()==Image.open(path).convert('RGBA').tobytes(),mode
   assert im.resize((im.width*3,im.height*3),Image.Resampling.NEAREST).tobytes()==Image.open(ROOT/(mode+'_3x.png')).convert('RGBA').tobytes(),mode+' 3x'
  else:
   im.save(path);im.resize((im.width*3,im.height*3),Image.Resampling.NEAREST).save(ROOT/(mode+'_3x.png'))
  print(mode,im.size,hashlib.sha256(im.tobytes()).hexdigest())
