#!/usr/bin/env python3
"""Lossless, no-overwrite Markdown → version-1 JSON backlog migration."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.records import parse_backlog, read_required


def migrate(source: Path, destination: Path):
    rows = parse_backlog(read_required(source))
    payload = {'schema_version': 1, 'source': source.as_posix(), 'source_date': '2026-10-07', 'ideas': rows}
    with destination.open('x', encoding='utf-8') as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    return rows


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', type=Path, default=Path('content/ideas/backlog.md'))
    p.add_argument('--destination', type=Path, default=Path('content/ideas/backlog.json'))
    args = p.parse_args()
    try:
        rows = migrate(args.source, args.destination)
    except (OSError, ValueError) as exc:
        p.exit(2, f'Migration failed: {exc}\n')
    print(f'Migrated {len(rows)} ideas; original unchanged')
