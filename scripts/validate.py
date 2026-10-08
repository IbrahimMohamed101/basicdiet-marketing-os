#!/usr/bin/env python3
"""Local structure and basic secret/safety checks, then Phase 1 migration check."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "AGENTS.md", "STATE.md", "CHANGELOG.md",
    ".agents/skills/basic-diet-marketing/SKILL.md",
    ".agents/workflows/daily-content.md",
    "docs/ROADMAP.md", "docs/SOURCE_MAP.md", "docs/MIGRATION.md",
    "docs/SECURITY.md", "docs/BOOTSTRAP.md",
    "decisions/log.md", "content/ideas/backlog.md",
    "content/published/content-log.md", "data/reports/README.md",
    "scripts/verify_migration.py",
    "scripts/daily_brief.py", "tests/test_daily_brief.py",
    ".github/workflows/daily-content-brief.yml", "docs/PHASE3_RUNBOOK.md",
]
missing = [p for p in required if not (ROOT / p).is_file()]
text_files = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix in {".md", ".py", ".sh"} and ".git" not in p.parts]
bad_keys = []
for p in text_files:
    data = p.read_text(encoding="utf-8")
    if re.search(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", data):
        bad_keys.append(str(p.relative_to(ROOT)))
if missing or bad_keys:
    print("FAIL:", {"missing": missing, "private_keys": bad_keys})
    sys.exit(1)
print(f"PASS: {len(required)} required files, {len(text_files)} text files, no private-key block.")
subprocess.run([sys.executable, str(ROOT / "scripts/verify_migration.py")], check=True)
subprocess.run([sys.executable, str(ROOT / "scripts/validate_skills.py")], check=True)
