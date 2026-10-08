#!/usr/bin/env python3
"""Local structure and basic secret/safety checks, then Phase 1 migration check."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.security import contains_credential
required = [
    "README.md", "AGENTS.md", "STATE.md", "CHANGELOG.md",
    ".agents/skills/basic-diet-marketing/SKILL.md",
    ".agents/workflows/daily-content.md", ".agents/product-marketing.md",
    "content/ideas/backlog.json", "content/ideas/creative.json",
    "content/published/publications.json", "content/drafts/runs.json",
    "data/analytics/creative-performance.json", "docs/DATA_CONTRACTS.md",
    "docs/ROADMAP.md", "docs/SOURCE_MAP.md", "docs/MIGRATION.md",
    "docs/SECURITY.md", "docs/BOOTSTRAP.md",
    "decisions/log.md", "content/ideas/backlog.md",
    "content/published/content-log.md", "data/reports/README.md",
    "scripts/verify_migration.py",
    "scripts/daily_brief.py", "tests/test_daily_brief.py",
    "scripts/marketing_baseline.py", "tests/test_marketing_baseline.py",
    "docs/PHASE4_MEASUREMENT.md",
    ".github/workflows/daily-content-brief.yml", "docs/PHASE3_RUNBOOK.md",
]
missing = [p for p in required if not (ROOT / p).is_file()]
text_files = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix in {".md", ".py", ".sh", ".json", ".yml", ".yaml", ".txt"} and not {".git", ".venv", "output", "node_modules"}.intersection(p.parts)]
bad_keys = []
for p in text_files:
    data = p.read_text(encoding="utf-8")
    if contains_credential(data):
        bad_keys.append(str(p.relative_to(ROOT)))
if missing or bad_keys:
    print("FAIL:", {"missing": missing, "credential_markers": bad_keys})
    sys.exit(1)
print(f"PASS: {len(required)} required files, {len(text_files)} text files, no recognized credential marker (not a PII guarantee).")
subprocess.run([sys.executable, str(ROOT / "scripts/verify_migration.py")], check=True)
subprocess.run([sys.executable, str(ROOT / "scripts/validate_skills.py")], check=True)

subprocess.run([sys.executable, str(ROOT / "scripts/validate_operations.py")], check=True)
