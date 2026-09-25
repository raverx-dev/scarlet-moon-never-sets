"""Preserve unchanged transport and append correction bytes without erasing history."""
from pathlib import Path
import json,hashlib,base64
ROOT=Path(__file__).parent
old=json.loads((ROOT/'before/transport-index.json').read_text())
old_by_path={e['path']:e for e in old};entries=[]
for p in sorted(ROOT.rglob('*.png')):
 rel=str(p.relative_to(ROOT));raw=p.read_bytes();digest=hashlib.sha256(raw).hexdigest()
 if rel in old_by_path and old_by_path[rel]['sha256']==digest:entries.append(old_by_path[rel]);continue
 b64=base64.b64encode(raw).decode();parts=[]
 for i,start in enumerate(range(0,len(b64),400000)):
  name=f'correction01-{digest[:16]}-{i:02}.b64';(ROOT/'transport'/name).write_text(b64[start:start+400000]);parts.append(name)
 entries.append({'path':rel,'sha256':digest,'parts':parts})
(ROOT/'transport/index.json').write_text(json.dumps(entries,indent=2))
print('Preserved',len(entries),'exact PNG files; original transport parts retained')
