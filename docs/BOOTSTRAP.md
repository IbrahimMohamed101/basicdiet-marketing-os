# Repository bootstrap and verification

The remote **private** repository `IbrahimMohamed101/basicdiet-marketing-os` already exists. Phase 0 was published in October 2026; do not re-create it.

## Clone to Windows / WSL

```bash
git clone https://github.com/IbrahimMohamed101/basicdiet-marketing-os.git
cd basicdiet-marketing-os
python3 scripts/validate.py
```

For later edits, use standard Git branches/PRs or commit with permission. Never force-push `main`. Avoid storing user credentials, customer identity, payments or access tokens in the repository.

## Verify

```bash
gh repo view IbrahimMohamed101/basicdiet-marketing-os --json isPrivate,nameWithOwner,url
git ls-files
python3 scripts/validate.py
```

Expected: `isPrivate: true`, correct owner and complete Phase 0 foundation in `main`.

The helper `scripts/bootstrap-github.sh` is retained for audit/history but does **not** need to be run on an already existing repository.
