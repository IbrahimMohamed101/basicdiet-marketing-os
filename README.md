# Basic Diet Marketing OS

**Status:** Phase 3 manual pilot implemented (2026-10-08) — grounded content brief workflow. **Private GitHub repository**.

AI-assisted marketing system for the Saudi meal-subscription restaurant Basic Diet. This repository is a **durable knowledge and operational protocol**, not the app backend, live database, automated publisher or running ad platform.

## Starting a marketing session

1. Read [`AGENTS.md`](AGENTS.md) → [`STATE.md`](STATE.md) → [native skill](.agents/skills/basic-diet-marketing/SKILL.md).
2. Read only relevant current working docs, with [source/path manifest](docs/MIGRATION.md) for historic references.
3. Where real-time accuracy matters, check authorized backend/dashboard, asset owner or dated public source before publishing claims.
4. Follow **Read → Research → Plan → Execute (only with approval) → Verify → Document**.

## Short commands

- **Basic Diet Mode — ننزل إيه النهارده؟** → [30-item backlog](content/ideas/backlog.md), [content strategy](content/strategy.md), [publication log](content/published/content-log.md), [asset catalog](assets/catalog.md).
- **Basic Diet Mode — راجع الأسبوع** → [analytics dictionary](data/analytics/measurement-framework.md), [baseline status](data/analytics/baseline-status.md), and live verified measurements.
- **Basic Diet Mode — اعمل حملة** → [offers](knowledge/offers-pricing.md), [audience research](knowledge/audience-voc.md), [previous experiments](experiments/history.md).
- **Basic Diet Mode — حلل المنافسين** → [historical competitor baseline](knowledge/competitors.md) + refreshed sources.
- **Basic Diet Mode — حالة المشروع** → [STATE.md](STATE.md) + [ROADMAP.md](docs/ROADMAP.md).

## Installed AI marketing skills (Phase 2)

The **13 imported upstream skills** and their reference files are registered in [`.agents/skills/README.md`](.agents/skills/README.md). The project also includes its native Basic Diet skill and the user-supplied [storyboard-to-video skill](.agents/skills/storyboard-to-video/SKILL.md), bringing the project skill count to **15**.

Source and license details: [Phase 2 skills provenance](docs/SKILLS_PHASE2.md). No automatic image generation, social publishing, scheduled tasks or advertising spend is enabled by installing these documents.

## Daily content workflow — Phase 3

The repository now includes a **manual read-only run** that selects an unused grounded idea and produces an approval-only brief with proposed hook, shots, caption, story, CTA, KPI, source notes and review gates.

Run locally:

    python3 scripts/validate.py
    python3 -m unittest discover -s tests -v
    python3 scripts/daily_brief.py --channel instagram --goal auto

Or use GitHub Actions → **Basic Diet - draft content (manual)** → Run workflow. Download the draft artifact. Nothing is published, scheduled or spent automatically.

[Execution and approval guide](docs/PHASE3_RUNBOOK.md). The six role handoffs are implemented as deterministic, inspectable steps; independent live AI agents are **not yet deployed**. Optional AI writing uses an explicitly configured billable API key and must be separately enabled.

## Repository directories

- `.agents/skills/`, `.agents/workflows/`: current native skill, **13 pinned third-party marketing skills**, user-supplied storyboard workflow, supporting references and manual workflows.
- `agents/`: six role descriptions; **not automatically running agents**.
- `knowledge/`: brand, product, audience, VOC, competitors and historic offers.
- `content/`: content ideas, legacy content log, verified publications and strategy.
- `assets/`: historical asset index; media originals remain in approved storage.
- `data/`: measurement rules, sources and later aggregated dated snapshots.
- `campaigns/`, `experiments/`, `decisions/`, `plans/`: controlled execution and history.
- `archive/basicdiet145-2026-10-07/`: **all 23 original marketing/skill source files**, unchanged.
- `docs/`: roadmap, privacy safeguards, provenance and migration manifest.

## Migration evidence

Legacy repo: [basicdiet145](https://github.com/IbrahimMohamed101/basicdiet145) at commit `5241bfb0fe8fe4d2a15b15ed85d13648b8a7be37`. **23 archived exact copies + 20 mapped working copies**; original files were not changed or removed. See [MIGRATION.md](docs/MIGRATION.md) for file-by-file original/new paths and Git SHA verification.

## Safety

Never commit raw customer records, secrets, payment data, unpublished private customer conversations or large raw video. Current prices, current promo eligibility and attributed return on ad spend **require live verification**. Publishing, changing offers and spending money require express human authorization.
