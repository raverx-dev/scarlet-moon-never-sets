#!/usr/bin/env python3
"""Build disposable QA wrapper; never edits the shipped index.html."""
from pathlib import Path
root=Path(__file__).resolve().parent.parent
source=(root/'index.html').read_text()
addon='\n'.join((root/'qa'/f).read_text() for f in ('regression.js','inspection.js'))
out=root/'qa/generated.html'
out.write_text(source.replace('</script>', '\n'+addon+'\n</script>'))
print(out)
