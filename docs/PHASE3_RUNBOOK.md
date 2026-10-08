# Basic Diet Mode — operational runbook

The Arabic command **Basic Diet Mode — ننزل إيه النهارده؟** routes through AGENTS → STATE → native skill → daily workflow. This is a deterministic drafting tool with six stage contracts, not six autonomous AI agents.

## Setup and local execution

Python 3.11+ and timezone data are required (tested on Python 3.12). Runtime has no third-party dependencies. Validation uses pinned PyYAML:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/daily_brief.py --channel instagram --goal auto
```

Normal execution reserves the selected idea in `content/drafts/runs.json`. Commit this ledger when the draft is worth retaining so the next checkout sees it. Change a reservation to `released` only after deciding to discard/rework it. Published ideas remain blocked regardless of reservation status.

```bash
# Inspection only: no durable reservation or API call.
python3 scripts/daily_brief.py --dry-run --channel instagram --goal auto --out-dir output/review
# Choose a specific unused/unreserved idea.
python3 scripts/daily_brief.py --idea-id C006 --goal consideration
```

Output: `output/<directory>/<run_id>/daily-brief.md` and `.json`. The CLI prints the exact path. The date defaults to Asia/Riyadh; `--as-of YYYY-MM-DD` supports reproducible snapshots but rejects future dates and records later than the snapshot. Replaying identical inputs requires a new output parent; existing runs are not overwritten.

Exit codes: **0** draft produced; **2** invalid data/configuration/I/O (never reported as success); **3** draft available but optional AI failed. JSON `ai.status` records disabled, failed or unverified_suggestions. On I/O interruption inspect both artifact and ledger before rerunning. See [data contracts](DATA_CONTRACTS.md).

## What the workflow actually uses

It validates the structured 30-idea backlog, editorial profiles, draft reservations, publication evidence, available aggregate performance, and reads state, strategy, audience/VOC, brand, product, offers, asset catalog, measurement and routed skill files. Source hashes make the exact inputs inspectable. Python uses curated editorial adaptations; it does not execute Markdown skill text or interpret arbitrary changes to strategy as new algorithms. A supervising agent reviews the sources and updates profiles/logic when strategy changes.

Current assets, prices and performance are **not verified live**. Asset folders are candidate sources only; exact file ID, rights, destination URL and current menu remain pending. The brief is useful preparation, never a ready-to-publish approval. Historical coupons, nutrition numbers, testimonial quotes and service promises are omitted from the adapted copy.

## Optional AI — explicit paid opt-in

```bash
# Configure OPENAI_API_KEY through your local secret manager, never in Git.
python3 scripts/daily_brief.py --dry-run --ai --model gpt-5 --max-output-tokens 1200
```

One Responses API request, no retries, 30-second timeout, maximum 16 KB serialized input and 128 KB response, 128–2000 output-token ceiling, `store: false`, no tools. Only allowlisted creative fields are transmitted; state, source documents, source links and histories are excluded. Token caps are not a currency budget; model availability/pricing and account-level limits must be checked before opting in. No live paid API was used for the audit. All provider tests use mocks.

AI text stays in `ai-suggestions.md`, unverified and never inserted into the standard brief. Missing keys, HTTP errors, malformed/incomplete/oversized responses produce exit 3 with the manual draft preserved. No provider error body or key is logged. Default execution and tests never need credentials.

## GitHub Actions

Manual workflow only; read-only repository permission, pinned actions, no persisted checkout credentials. Offline and AI steps are separate; only the explicitly selected AI step receives the key. Artifacts contain only draft files, and still upload when optional AI fails. No schedule, repo commit or platform publishing exists. Actions drafts are stateless (`--dry-run`), so repeated dispatches may select the same unreserved idea until the reviewed ledger is committed.

## Human review and actual publication

Review Saudi Arabic copy, current menu/offer/claims, exact source file/rights, service coverage and official destination. Verify recent platform history manually. Obtain action-specific authorization before asset generation, publication, customer messages or ad spend. The tool has no command to perform those actions.

After an actual authorized publication, add its canonical URL, idea ID, platform/date and verifier/source to `content/published/publications.json`, run validation, and commit. Record performance only after its measurement window. Never write fake rows to make the backlog advance.
