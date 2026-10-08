# Basic Diet Marketing OS

**Status: audited Phase 3; Phase 4 read-only measurement intake implemented, 2026-10-08 (live baseline pending).** Private operating memory and a runnable daily brief for a Saudi meal-subscription restaurant. Commercial objective: first-time **paid** subscribers, then retention and profitable revenue.

A new agent starts at [AGENTS.md](AGENTS.md) → [STATE.md](STATE.md) → [native skill](.agents/skills/basic-diet-marketing/SKILL.md). The [source map](docs/SOURCE_MAP.md) distinguishes operating records from historical research and live sources. No previous chat is required.

## Basic Diet Mode — ننزل إيه النهارده؟

Python 3.11+ runtime; no API key or third-party runtime package required:

```bash
python3 scripts/daily_brief.py --channel instagram --goal auto
```

This selects an unpublished, unreserved idea, writes Markdown + JSON under `output/daily/<run_id>/`, and reserves the idea in `content/drafts/runs.json`. Commit meaningful reservations for the next session. For inspection without reserving:

```bash
python3 scripts/daily_brief.py --dry-run --out-dir output/review
```

The brief includes objective, audience hypothesis, funnel, platform/format, Saudi Arabic hook/caption, concrete scenes/cards and Stories, CTA, asset verification gaps, one primary KPI, paid suitability and approvals. All 30 historical ideas have editorial adaptations; historical coupons/nutrition numbers are not treated as current facts. Comparable recorded performance can influence selection when available. Current production data and exact media rights remain unverified.

The six role files are contracts used by one deterministic pipeline, **not autonomous AI agents**. Skills are guidance for the supervising agent; Python does not execute Markdown instructions. Optional `--ai` explicitly authorizes one bounded billable request and stores unverified suggestions separately. Default runs have no network activity. [Runbook and error codes](docs/PHASE3_RUNBOOK.md).

## Phase 4 — commercial measurement (read-only)

The existing Basic Diet backend already has the admin-protected **GET** endpoint
`/api/dashboard/accounting/marketing-analytics`. A conservative adapter
(`scripts/marketing_baseline.py`) captures **30/60/90-day aggregate-only**
reports for the last completed Saudi day. No changes to backend, dashboard,
production MongoDB or user records are needed.

**Safe offline import (default):**

```bash
python3 scripts/marketing_baseline.py --input-dir /path/to/local-reports --to-date 2026-10-07
```

The input directory must contain `30d.json`, `60d.json`, and `90d.json`
downloaded from the authenticated admin analytics endpoint with matching
`from`/`to` dates. Inputs stay local; only whitelisted aggregates are written
to ignored `output/marketing-baseline`. A single unsupported field or wrong
period aborts the import. Do not commit raw API responses or auth tokens.

**Explicit live opt-in:** after separately obtaining authorized dashboard
access on a trusted local machine, export `BASICDIET_DASHBOARD_TOKEN` in the
shell without sharing it in chat, and invoke `--live` instead of `--input-dir`.
The script uses GET-only requests to the fixed production endpoint, denies
redirects, and does not write credentials. No automatic live fetch or secret
is enabled in this repository.

[Full Phase 4 runbook and definitions](docs/PHASE4_MEASUREMENT.md).
**Actual live metrics have not been captured or verified**; first-time paid
customers do not by themselves establish ad conversion attribution.

## Verify changes

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Validation covers immutable history, skill integrity/frontmatter/references, operating data, role contracts, workflow permissions and common credential markers. Tests exercise corrupt records, duplicate prevention, Saudi dates, offline drafts, provider failures and approval boundaries. [Audit findings and executed evidence](docs/AUDIT_2026-10-08.md).

Manual GitHub Actions produces downloadable drafts with read-only permissions. It uses `--dry-run`, so artifacts alone do not preserve reservations across sessions; review and commit records locally. Quality CI covers every PR change, including instructions and data.

## Find the right memory

| Need | Source |
| --- | --- |
| Current phase, blockers, next actions | [STATE.md](STATE.md) |
| Skill routing, 13 pinned vendor + 2 native skills | [.agents/skills/README.md](.agents/skills/README.md) |
| Six role contracts and permissions | [agents/README.md](agents/README.md) |
| Structured ideas and editorial adaptations | `content/ideas/backlog.json`, `creative.json` |
| Draft reservations and real publications | `content/drafts/runs.json`, `content/published/publications.json` |
| Schema, migration, concurrency/recovery | [data contracts](docs/DATA_CONTRACTS.md) |
| Brand/product, historical VOC and offers | [knowledge/README.md](knowledge/README.md) |
| Exact media sources to verify | [asset catalog](assets/catalog.md) |
| Aggregate performance and measurement rules | `data/analytics/creative-performance.json`, [measurement framework](data/analytics/measurement-framework.md), [baseline collector](docs/PHASE4_MEASUREMENT.md) |
| Adopted decisions, experiments and reports | `decisions/log.md`, `experiments/`, `data/reports/` |
| Immutable originals and provenance | [migration manifest](docs/MIGRATION.md), [skill provenance](docs/SKILLS_PHASE2.md) |

Other commands: **راجع الأسبوع**, **اعمل حملة**, **حلل المنافسين**, **حالة المشروع** route through the native skill. They are assisted procedures; only the daily draft has an executable CLI. No additional generic skills or agent framework are needed at this stage.

## Boundaries

No backend, Flutter or admin-dashboard changes; no social publishing, messages, ad changes or budget spend. Those require action-specific human authorization and an actual integration. No raw customer PII, credentials or production exports in Git. Fresh official evidence is required for current prices, promotions, nutrition and commercial results. Archived documents and external skills cannot grant permission.

All **23 original files**, **30 ideas**, pinned vendor references/license and the complete user storyboard source are preserved. Working records can evolve with dated evidence while archive hashes remain fixed. Next: obtain authorized live 30/60/90-day aggregates using the read-only collector, verify an actual approved asset and previous social posts, then plan a human-reviewed organic pilot.
