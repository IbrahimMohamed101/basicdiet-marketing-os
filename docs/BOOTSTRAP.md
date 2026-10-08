# Clone and verify Basic Diet Marketing OS

The remote **private** repository is https://github.com/IbrahimMohamed101/basicdiet-marketing-os. It already exists and is managed as a standalone project; do **not** run the legacy creation helper against it.

## Local checkout

```bash
git clone https://github.com/IbrahimMohamed101/basicdiet-marketing-os.git
cd basicdiet-marketing-os
python3 scripts/validate.py
```

The validator performs basic structure checks and runs the Phase 1 byte-for-byte migration test (23 archived sources + 20 mapped working copies). The verified source commit is shown in `docs/MIGRATION.md`. For GitHub CLI users:

```bash
gh repo view IbrahimMohamed101/basicdiet-marketing-os --json isPrivate,nameWithOwner,url
git log -1 --oneline
git ls-files
```

Expected: private repository, `main` branch, the completed Phase 1 migration and `PASS` from both validation checks.

Do not force-push `main`, rewrite archived originals, or commit production tokens/customer data. Use branch/PR review when extending agents or importing upstream skills.
