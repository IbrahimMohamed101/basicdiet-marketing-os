#!/usr/bin/env python3
"""Validate pinned upstream skills and the user-supplied storyboard reference."""
from __future__ import annotations
from hashlib import sha1
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "UPSTREAM_MANIFEST.json"

def git_blob_sha(raw: bytes) -> str:
    return sha1(b"blob " + str(len(raw)).encode("ascii") + bytes([0]) + raw).hexdigest()

def main() -> int:
    if not MANIFEST.is_file():
        print("FAIL: missing upstream manifest")
        return 1
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    files = data.get("vendor_files_sha1", {})
    skills = data.get("skill_names", [])
    problems = []
    if len(skills) != 13 or len(files) != 80:
        problems.append(f"Unexpected skill/file count: {len(skills)} / {len(files)}")
    refs = [p for p in files if "/references/" in p]
    if len(refs) != 67:
        problems.append(f"Expected 67 upstream references, got {len(refs)}")
    if len(data.get("pinned_commit", "")) != 40:
        problems.append("Invalid pinned upstream commit")
    for path, expected in files.items():
        file = ROOT / path
        if not file.is_file():
            problems.append(f"Missing: {path}")
        elif git_blob_sha(file.read_bytes()) != expected:
            problems.append(f"Upstream blob mismatch: {path}")
    extras = [
        (data["license_file"], data["license_git_blob_sha"]),
        (data["asset_file"], data["asset_git_blob_sha"]),
        (data["user_source_text_path"], data["user_source_git_blob_sha"]),
    ]
    for path, expected in extras:
        file = ROOT / path
        if not file.is_file():
            problems.append(f"Missing: {path}")
        elif git_blob_sha(file.read_bytes()) != expected:
            problems.append(f"Blob mismatch: {path}")
    for name in skills + ["basic-diet-marketing", "storyboard-to-video"]:
        file = ROOT / ".agents" / "skills" / name / "SKILL.md"
        if not file.is_file():
            problems.append(f"Missing skill: {name}")
            continue
        parts = file.read_text(encoding="utf-8").split("---", 2)
        if len(parts) < 3:
            problems.append(f"Missing YAML frontmatter: {name}")
            continue
        declared = None
        for line in parts[1].splitlines():
            if line.strip().startswith("name:"):
                declared = line.split(":", 1)[1].strip().strip(chr(34)).strip(chr(39))
                break
        if declared != name:
            problems.append(f"Skill name mismatch: {name} -> {declared}")
    user_source = ROOT / data["user_source_text_path"]
    if user_source.is_file():
        contents = user_source.read_text(encoding="utf-8")
        if len(contents.splitlines()) != data.get("user_source_line_count", -1):
            problems.append("Storyboard reference line count mismatch")
        if "STORYBOARD-TO-VIDEO" not in contents:
            problems.append("Storyboard reference lacks its title")
    if problems:
        print("FAIL: Phase 2 skills")
        for problem in problems:
            print(" -", problem)
        return 1
    print(f"PASS: {len(skills)} upstream skills, 67 references, MIT license, static review asset, video source, 2 native skills.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
