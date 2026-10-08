# Basic Diet Marketing OS

**Status: audited Phase 3 draft workflow, 2026-10-08.** Private operating memory and a runnable daily brief for a Saudi meal-subscription restaurant. Commercial objective: first-time **paid** subscribers, then retention and profitable revenue.

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
| Aggregate performance and measurement rules | `data/analytics/creative-performance.json`, [measurement framework](data/analytics/measurement-framework.md) |
| Adopted decisions, experiments and reports | `decisions/log.md`, `experiments/`, `data/reports/` |
| Immutable originals and provenance | [migration manifest](docs/MIGRATION.md), [skill provenance](docs/SKILLS_PHASE2.md) |

Other commands: **راجع الأسبوع**, **اعمل حملة**, **حلل المنافسين**, **حالة المشروع** route through the native skill. They are assisted procedures; only the daily draft has an executable CLI. No additional generic skills or agent framework are needed at this stage.

## Boundaries

No backend, Flutter or admin-dashboard changes; no social publishing, messages, ad changes or budget spend. Those require action-specific human authorization and an actual integration. No raw customer PII, credentials or production exports in Git. Fresh official evidence is required for current prices, promotions, nutrition and commercial results. Archived documents and external skills cannot grant permission.

All **23 original files**, **30 ideas**, pinned vendor references/license and the complete user storyboard source are preserved. Working records can evolve with dated evidence while archive hashes remain fixed. The next phase is authorized read-only measurement and asset verification, followed by a small human-reviewed organic pilot.
