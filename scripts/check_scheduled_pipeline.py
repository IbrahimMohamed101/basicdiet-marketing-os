#!/usr/bin/env python3
"""Read-only audit of daily Basic Diet creative stage handoffs.

Reports missing or blocked stages. This is not a creative generator, automatic
ChatGPT Task retrigger, image pixel QA, rights check, or publishing approval.
"""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import re
from zoneinfo import ZoneInfo

STAGES = [
    ("01", "01-ideas.md"),
    ("02", "02-critique.md"),
    ("03", "03-approved-brief.md"),
    ("04", "04-draft-images.md"),
    ("05", "05-final-review.md"),
]
FIELDS = (
    "date", "stage", "status", "run_key", "source_refs",
    "predecessor_refs", "attempts", "generated_at_riyadh", "next_action",
)
STATUSES = {"COMPLETED", "BLOCKED", "NEEDS_USER_REVIEW"}


def check_date(root: Path, day: str) -> list[str]:
    directory = root / "automation" / "daily" / day
    issues = []
    for stage, filename in STAGES:
        file = directory / filename
        if not file.is_file():
            issues.append(f"{filename}: NOT FOUND")
            continue
        content = file.read_text(encoding="utf-8")
        header = {}
        for key in FIELDS:
            match = re.search(rf"(?m)^\s*{re.escape(key)}\s*:\s*(.+)\s*$", content)
            if match is None:
                issues.append(f"{filename}: missing {key}")
            else:
                header[key] = match.group(1).strip().strip("\"'")
        if header.get("date") != day:
            issues.append(f"{filename}: wrong date")
        if header.get("stage") != stage:
            issues.append(f"{filename}: wrong stage")
        if header.get("run_key") != f"{day}:{stage}":
            issues.append(f"{filename}: wrong run_key")
        status = header.get("status")
        if status not in STATUSES:
            issues.append(f"{filename}: invalid status {status!r}")
        elif status == "BLOCKED":
            issues.append(f"{filename}: BLOCKED; inspect file for diagnosis")
        elif stage != "05" and status != "COMPLETED":
            issues.append(f"{filename}: premature review status")
        elif stage == "05" and status != "NEEDS_USER_REVIEW":
            issues.append(f"{filename}: missing human-review handoff")
        if header.get("attempts") and not re.fullmatch(r"[123]", header["attempts"]):
            issues.append(f"{filename}: attempts should be 1-3")
        if stage == "04" and status == "COMPLETED":
            if not re.search(r"(?m)^draft_image_urls:\s*https://\S+", content):
                issues.append(f"{filename}: missing permanent draft_image_urls")
        if stage == "05" and status == "NEEDS_USER_REVIEW":
            if not re.search(r"(?m)^final_image_url:\s*https://\S+", content):
                issues.append(f"{filename}: missing permanent final_image_url")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="Date YYYY-MM-DD in Asia/Riyadh")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    today = args.date or datetime.now(ZoneInfo("Asia/Riyadh")).date().isoformat()
    try:
        datetime.strptime(today, "%Y-%m-%d")
    except ValueError as exc:
        parser.error(str(exc))
    issues = check_date(args.repo_root, today)
    if issues:
        print(f"FAIL — Basic Diet {today}: {len(issues)} pipeline problem(s)")
        for issue in issues:
            print(" -", issue)
        return 1
    print(f"PASS — Basic Diet {today}: all five handoff reports are present")
    print("NOTICE: links, actual image pixels, permissions and owner review not verified by this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
