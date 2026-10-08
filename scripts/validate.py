#!/usr/bin/env python3
"""Phase 0 sanity checks: structure, basic safety and link conventions."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    'README.md','AGENTS.md','STATE.md','CHANGELOG.md',
    '.agents/skills/basic-diet-marketing/SKILL.md',
    '.agents/workflows/daily-content.md',
    'docs/ROADMAP.md','docs/SOURCE_MAP.md','docs/MIGRATION.md',
    'docs/SECURITY.md','docs/BOOTSTRAP.md',
    'decisions/log.md','content/ideas/README.md',
    'content/calendar/README.md','content/published/README.md',
    'data/reports/README.md',
]
missing = [p for p in required if not (ROOT/p).is_file()]
text_files = [p for p in ROOT.rglob('*') if p.suffix in {'.md','.py','.sh'} and p.is_file() and '.git' not in p.parts]
secret_like = []
for p in text_files:
    data = p.read_text(encoding='utf-8')
    # Reject real private-key blocks; ordinary mentions in docs are fine.
    if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', data):
        secret_like.append(str(p.relative_to(ROOT)))
if missing or secret_like:
    print('FAILED:', {'missing': missing, 'private_key_blocks': secret_like})
    sys.exit(1)
print(f'PASS: {len(required)} required files; {len(text_files)} checked text files; no private key blocks.')
