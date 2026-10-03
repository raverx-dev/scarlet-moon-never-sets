"""Unpack recorded live MCP read-back. No input-grid rendering."""
import json,base64
from pathlib import Path
R=Path(__file__).resolve().parent
b=json.loads((R/'robopixel_readback.json').read_text()); inp=json.loads((R/'authoring_inputs.json').read_text())
manifest={'project_id':'scarlet-moon-never-sets','candidate':True,'source_commit':b.get('source_commit','44530dd918ce498544025ca1919e91faccb619d4'),'assets':{}}
for name,v in b['assets'].items():
    e=v['export'];(R/'exports'/f'{name}.json').write_text(json.dumps(e,indent=2)+'\n')
    png=next(c for c in v['view']['content'] if c['type']=='image')
    (R/'canonical_previews'/f'{name}.png').write_bytes(base64.b64decode(png['data']))
    a=inp['assets'][name]
    manifest['assets'][name]={k:a[k] for k in ('asset_id','status','role','kind','width','height')}
    manifest['assets'][name].update(revision=e['revision'],revision_hash=e['revision_hash'],render_hash=v['view']['structuredContent']['render_hash'],round_trip=e['round_trip'],approval=v['approval'].get('structuredContent'),from_revision=a.get('from_revision'),art_change=a.get('art_change','Unchanged'))
(R/'robopixel_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(R/'authoring_receipts.json').write_text(json.dumps(b['receipts'],indent=2)+'\n')
print('Unpacked',len(manifest['assets']),'exact live exports and PNG views')
