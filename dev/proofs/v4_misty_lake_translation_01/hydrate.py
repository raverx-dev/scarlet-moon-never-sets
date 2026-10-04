"""Restore exact PNG bytes from text-only GitHub transport; standard library only."""
from pathlib import Path
import base64,json,hashlib
ROOT=Path(__file__).parent
def hydrate():
 index=json.loads((ROOT/'transport/index.json').read_text())
 for entry in index:
  target=(ROOT/entry['path']).resolve()
  assert target.is_relative_to(ROOT.resolve()) and target.suffix=='.png'
  raw=base64.b64decode(''.join((ROOT/'transport'/p).read_text() for p in entry['parts']),validate=True)
  assert hashlib.sha256(raw).hexdigest()==entry['sha256'],entry['path']
  if target.exists():assert target.read_bytes()==raw, 'Refusing to replace differing local file: '+entry['path']
  else:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
 print('PASS: restored/verified',len(index),'exact PNG files')
if __name__=='__main__':hydrate()
