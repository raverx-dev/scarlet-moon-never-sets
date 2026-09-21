#!/usr/bin/env python3
"""Build disposable QA wrapper; never edits the shipped index.html."""
from pathlib import Path
import os
root=Path(__file__).resolve().parent.parent
source_path=(root/os.environ.get('SCARLET_QA_SOURCE','index.html')).resolve()
if root not in source_path.parents or not source_path.is_file():
    raise SystemExit('SCARLET_QA_SOURCE must select an existing game HTML inside the repository')
source=source_path.read_text()
addon='\n'.join((root/'qa'/f).read_text() for f in ('regression.js','inspection.js'))
if source_path == (root/'versions/v4/index.html').resolve():
    addon+='\n'+(root/'qa/v4-inspection.js').read_text()
out=root/'qa/generated.html'
out.write_text(source.replace('</script>', '\n'+addon+'\n</script>'))
print(out)
