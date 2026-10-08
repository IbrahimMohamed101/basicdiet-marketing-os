# Clone and verify Basic Diet Marketing OS

The remote **private** repository is https://github.com/IbrahimMohamed101/basicdiet-marketing-os. It already exists and is managed as a standalone project; do **not** run the legacy creation helper against it.

## Local checkout

```bash
git clone https://github.com/IbrahimMohamed101/basicdiet-marketing-os.git
cd basicdiet-marketing-os
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The validator performs structure checks, runs the Phase 1 byte-for-byte migration test (23 immutable archived sources + 20 existing working paths), and validates Phase 2 skill provenance (13 upstream skills + 67 references, license and user-supplied video reference). The verified source commit is shown in `docs/MIGRATION.md`. For GitHub CLI users:

```bash
gh repo view IbrahimMohamed101/basicdiet-marketing-os --json isPrivate,nameWithOwner,url
git log -1 --oneline
git ls-files
```

Expected: private repository, `main` branch, the audited Phase 3 workflow and earlier migration/skill installation and `PASS` from both validation checks.

Do not force-push `main`, rewrite archived originals, or commit production tokens/customer data. Use branch/PR review when extending agents or importing upstream skills.
