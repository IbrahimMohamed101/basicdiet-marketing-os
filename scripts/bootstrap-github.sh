#!/usr/bin/env bash
# Historical creation entry point retained as a safe diagnostic, never stages/pushes.
set -euo pipefail
cd "$(dirname "$0")/.."
echo 'Repository already provisioned. Read docs/BOOTSTRAP.md for checkout and verification.'
git status --short --branch
python3 scripts/validate.py
