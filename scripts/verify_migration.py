#!/usr/bin/env python3
"""Verify that all pinned 2026-10-07 source files survived Phase 1 byte-for-byte.

Reads docs/MIGRATION.md as the manifest; does not call network or access secrets.
"""
from __future__ import annotations

from hashlib import sha1
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/MIGRATION.md"
EXPECTED_COUNT = 23
EXPECTED_WORKING = 20

def git_blob_sha(raw: bytes) -> str:
    """Git object SHA-1 for a normal blob; same bytes imply same Git blob SHA."""
    return sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

def run() -> int:
    if not MANIFEST.is_file():
        print("FAIL: migration manifest is missing")
        return 1

    rows: list[tuple[str, str, str | None, str]] = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\| `(?:marketing|skills)/", line):
            continue
        fields = re.findall(r"`([^`]+)`", line)
        if len(fields) == 4:
            source, archived, working, expected_sha = fields
        elif len(fields) == 3 and "archive only" in line:
            source, archived, expected_sha = fields
            working = None
        else:
            print(f"FAIL: malformed manifest row: {line}")
            return 1
        if archived != "archive/basicdiet145-2026-10-07/" + source:
            print(f"FAIL: bad archive route: {source}")
            return 1
        if not re.fullmatch(r"[0-9a-f]{40}", expected_sha):
            print(f"FAIL: invalid SHA: {source}")
            return 1
        rows.append((source, archived, working, expected_sha))

    problems: list[str] = []
    if len(rows) != EXPECTED_COUNT:
        problems.append(f"Expected {EXPECTED_COUNT} entries, found {len(rows)}")
    if len({row[0] for row in rows}) != len(rows):
        problems.append("Duplicate source rows")
    mapped = sum(working is not None for _, _, working, _ in rows)
    if mapped != EXPECTED_WORKING:
        problems.append(f"Expected {EXPECTED_WORKING} working copies, found {mapped}")

    unchanged_working = 0
    for original, archive, working, expected in rows:
        file = ROOT / archive
        if not file.is_file():
            problems.append(f"Missing: {archive}")
        elif git_blob_sha(file.read_bytes()) != expected:
            problems.append(f"SHA mismatch: {archive} (source {original})")
        if working:
            file = ROOT / working
            if not file.is_file():
                problems.append(f"Missing working path: {working}")
            elif git_blob_sha(file.read_bytes()) == expected:
                unchanged_working += 1

    if problems:
        print("FAIL: Phase 1 migration verification")
        for problem in problems:
            print(" - " + problem)
        return 1
    print(f"PASS: {EXPECTED_COUNT}/{EXPECTED_COUNT} original files preserved; {mapped} working paths present, {unchanged_working} still byte-identical to initial migration.")
    return 0

if __name__ == "__main__":
    sys.exit(run())
