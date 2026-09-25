#!/usr/bin/env python3
"""Build review-only boards and manifest; never authors canonical pixels."""
from pathlib import Path
import json,hashlib,math
from PIL import Image,ImageDraw,ImageFont
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
read=json.loads((P/'selected_readback.json').read_text())
manifest={'project_id':'scarlet-moon-never-sets','status':'ROOFTOP WORKING STATIC-ART CANDIDATE — OWNER REVIEW REQUIRED','base_sha':'d7054d2b9b111ff711f44cc3ee5b71268aca6ed8','branch':'v4-mansion-rooftop-translation-01','recovery':'Original session files survived. Existing layouts and selected exports preserved; no post-resume art changes.','assets':[],'references':[]}
for a in read:
 e=a['export'];d=a['describe'];manifest['assets'].append({'asset_id':e['asset_id'],'name':a['name'],'revision':e['revision'],'revision_hash':e['revision_hash'],'palette_hash':d['palette_hash'],'render_hash':a['view']['render_hash'],'canvas':d['canvas'],'png_sha256':sha(P/'canonical'/(a['name']+'.png')),'export_sha256':sha(P/'exports'/(a['name']+'.json'))})
for mode in ['gameplay','story']:
 f=P/'reference'/(mode+'.png');manifest['references'].append({'role':mode,'source':'Owner-selected generated art-direction reference; not production raster','path':str(f.relative_to(P)),'dimensions':Image.open(f).size,'sha256':sha(f)})
(P/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
# Complete asset atlas: every selected canonical asset, no omitted large sheets.
atlas=Image.new('RGB',(1160,940),'#111626');draw=ImageDraw.Draw(atlas)
draw.text((20,12),'ROOFTOP / ALL 15 CANONICAL ASSETS',font=font,fill='#f0d2bb')
draw.text((20,38),'Selected RoboPixel exports. Small assets 2x; broad sheets 1x. Full IDs: v4-rooftop-trans01-<label>.',font=small,fill='#abb4cc')
for i,a in enumerate(manifest['assets']):
 x=16+(i%4)*288;y=70+(i//4)*215
 im=Image.open(P/'canonical'/(a['name']+'.png')).convert('RGBA');scale=2 if im.width<=125 and im.height<=76 else 1
 draw.rectangle((x,y,x+272,y+203),fill='#1c2338')
 draw.text((x+8,y+8),a['name']+' / r'+str(a['revision']),font=font,fill='#f0d2bb')
 draw.text((x+8,y+31),f'{im.width} x {im.height} | {scale}x nearest-neighbor',font=small,fill='#abb4cc')
 im=im.resize((im.width*scale,im.height*scale),Image.Resampling.NEAREST);atlas.paste(im,(x+8,y+51),im)
atlas.save(P/'asset_atlas.png')
for mode,w in [('gameplay',192),('story',256)]:
 cell=w*2;board=Image.new('RGB',(cell*3+48,554),'#111626');d=ImageDraw.Draw(board)
 labels=['CURRENT / V3 + V4 SOURCE RENDER','OWNER-APPROVED REFERENCE','AUTHORED / CANONICAL COMPOSITION']
 for i,(path,label) in enumerate(zip([P/'current'/(mode+'.png'),P/'reference'/(mode+'.png'),P/(mode+'_native.png')],labels)):
  x=12+i*(cell+12);d.text((x,12),label,font=small,fill='#f0d2bb')
  im=Image.open(path).convert('RGB')
  if i==1:im.thumbnail((cell,480),Image.Resampling.LANCZOS)
  else:im=im.resize((cell,480),Image.Resampling.NEAREST)
  board.paste(im,(x+(cell-im.width)//2,42+(480-im.height)//2))
 d.text((12,531),'Reference resized ONLY for this comparison. Source render is a canvas harness capture, not live browser QA.',font=small,fill='#abb4cc')
 board.save(P/(mode+'_comparison.png'))
# Accessible local review with native images plus explicit 3x previews and separate witnesses.
sections=[('Gameplay — native 192 × 240','gameplay_native.png'),('Gameplay — 3×','gameplay_3x.png'),('Story — native 256 × 240','story_native.png'),('Story — 3×','story_3x.png'),('Complete canonical asset atlas','asset_atlas.png'),('Gameplay comparison','gameplay_comparison.png'),('Story comparison','story_comparison.png'),('Illustrative gameplay witness','gameplay_witness_3x.png'),('Illustrative story witness','story_witness_3x.png')]
html='<!doctype html><meta charset="utf-8"><title>Rooftop working static-art candidate</title><style>body{background:#111626;color:#e5e7ef;font:16px system-ui;margin:24px;max-width:1600px}img{image-rendering:pixelated;max-width:100%;height:auto}a{color:#ffb9ac}p{max-width:850px}</style><h1>ROOFTOP WORKING STATIC-ART CANDIDATE — OWNER REVIEW REQUIRED</h1><p>Static proof only. No runtime integration, formal approval or delivery. Existing session artwork and layouts preserved after interruption.</p><p>Reference images are art direction only. Native compositions use exact RoboPixel exports. Witnesses use existing game actors/UI/bullets in a source canvas harness, not live browser QA.</p>'
for title,file in sections:html+=f'<h2>{title}</h2><a href="{file}"><img alt="{title}" src="{file}"></a>'
html+='<p>Limitations: quiet, sparse pavement; repeated parapet/cloud motifs; bright moon can compete with Remilia. Animation, all boss phases and runtime integration remain unqualified.</p>'
(P/'review.html').write_text(html)
print('Review boards, complete atlas, manifest and review.html built.')
