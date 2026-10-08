#!/usr/bin/env bash
set -euo pipefail

OWNER="IbrahimMohamed101"
REPO="basicdiet-marketing-os"
cd "$(dirname "$0")/.."

command -v git >/dev/null || { echo "Missing git" >&2; exit 1; }
command -v gh >/dev/null || { echo "Missing GitHub CLI (gh). See docs/BOOTSTRAP.md" >&2; exit 1; }
python3 scripts/validate.py

gh auth status >/dev/null || { echo "Run gh auth login first" >&2; exit 1; }
LOGIN="$(gh api user --jq '.login')"
if [[ "$LOGIN" != "$OWNER" ]]; then
  echo "Authenticated as $LOGIN, expected $OWNER; switch account before continuing" >&2
  exit 1
fi

if [[ ! -d .git ]]; then git init -b main; fi
if [[ "$(git branch --show-current 2>/dev/null || true)" != "main" ]]; then
  echo "Expected current branch 'main'. Correct locally and retry." >&2; exit 1
fi

git add .
if ! git diff --cached --quiet; then
  git -c user.name="$OWNER" -c user.email="${OWNER}@users.noreply.github.com" commit -m "chore: initialize Basic Diet Marketing OS phase 0"
fi

if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  echo "Remote repository already exists. Do not overwrite it; inspect it before pushing." >&2
  exit 1
fi

gh repo create "$OWNER/$REPO" --private --source=. --remote=origin --push
PRIVATE="$(gh repo view "$OWNER/$REPO" --json isPrivate --jq '.isPrivate')"
if [[ "$PRIVATE" != "true" ]]; then
  echo "ERROR: repository visibility is not private" >&2; exit 1
fi

echo "Published: https://github.com/$OWNER/$REPO (private)"
