"""Check selected actual copy against project-controlled risky claim patterns.

Never scan quoted reference guidance or entire creative Markdown bodies; only user-visible
copy fields in structured metadata. This is intentionally not a semantic truth detector.
"""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def check_copy(metadata, rules=None):
    if rules is None:
        rules = json.loads((ROOT / "knowledge/copy-rules.json").read_text(encoding="utf-8"))
    if rules.get("schema_version") != 1:
        raise ValueError("unsupported copy-rules version")
    copy = metadata.get("copy", {})
    snippets = [c.get("hook", "") for c in metadata.get("concepts", [])]
    snippets += [copy.get("caption", ""), copy.get("cta", ""), copy.get("on_design_text", "")]
    snippets += copy.get("stories", [])
    problems = []
    for line in snippets:
        if not isinstance(line, str):
            raise ValueError("copy must be strings")
        for rule in rules["blocked_patterns"]:
            if re.search(rule["pattern"], line, flags=re.IGNORECASE | re.UNICODE):
                problems.append(rule["reason"])
    if problems:
        raise ValueError("blocked creative claim/copy: " + "; ".join(sorted(set(problems))))
    return True
