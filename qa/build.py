#!/usr/bin/env python3
"""Build disposable QA wrapper; never edits the shipped index.html.

QA_SOURCE may point at a frozen snapshot (e.g. Version 2) for comparison
captures. The source file is only read; it is never rewritten.
"""
import os
from pathlib import Path
root=Path(__file__).resolve().parent.parent
source_path=Path(os.environ.get('QA_SOURCE') or (root/'index.html')).resolve()
source=source_path.read_text()
addon='\n'.join((root/'qa'/f).read_text() for f in ('regression.js','inspection.js'))
out=root/'qa/generated.html'
out.write_text(source.replace('</script>', '\n'+addon+'\n</script>', 1))
print(out)
print(f'QA_SOURCE={source_path}')
