# Basic Diet Marketing OS — Current State

**Last verified:** 2026-10-08  
**Repository phase:** **Phase 3 — manual daily-content pilot implemented**  
**Next implementation:** Phase 4 — read-only commercial measurement baseline and attribution QA. Automated social publishing and ad spend remain disabled.

## North Star

First-time **paid** subscribers → repeat/retention → profitable revenue. Engagement and reach are diagnostic metrics, not the main outcome.

## Established brand/product context (legacy research, dated 2026-10-07)

- Saudi restaurant Basic Diet: meal subscriptions with 7/26/30-day plans, pickup/delivery. Verify current eligibility and price from official systems.
- Positioning: **أكل حقيقي تحبه، بكميات محسوبة، بخيارات كثيرة، ويوفر عليك قرار الأكل كل يوم.**
- Core pillars: **الطعم، الاختيار، الراحة**.
- Content mix (experimental starting hypothesis): Food Desire 30%, Education 20%, Lifestyle/Problem 20%, Trust/Proof 15%, Conversion/Offer 15%.
- Imported original backlog: **30 grounded concepts**, now at `content/ideas/backlog.md`.
- Customer research and competitor pass 01 are historical snapshots, not fresh claims. See `knowledge/`.

## Completed

- Phase 0 private repository, boot protocol, six role definitions and guardrails.
- Phase 1: **23/23 source files** pinned to commit `5241bfb0fe8fe4d2a15b15ed85d13648b8a7be37` preserved under `archive/basicdiet145-2026-10-07/` with matching Git blob SHA.
- Phase 1: **20 working copies** mapped into `knowledge/`, `data/`, `content/`, `assets/`, `decisions/`, `experiments/`, `plans/`, `docs/`, and the original skill reference.
- Full provenance and path resolution in `docs/MIGRATION.md` and `docs/SOURCE_MAP.md`.
- Legacy backend repo intentionally remains untouched.

## Phase 2 — completed 2026-10-08

- Selected and installed **13** upstream marketing skills (each with its original `SKILL.md`) plus **67** Markdown reference files and one optional static creative HTML template; all match their pinned upstream Git blob SHAs.
- Original library: `coreyhaines31/marketingskills`, commit `b9ba399dd88b082b926e261e8ccfb843d20aa066`; MIT license preserved under `.agents/licenses/`.
- Imported the complete **user-supplied storyboard-to-video** Markdown reference (284 lines after newline normalization); added a task-scoped, safe `storyboard-to-video` active skill.
- Added routing docs, version provenance and validation tests. Only plan/generate media on user request, with approvals and verified brand details.
- Skills are instructions and references, **not** automated publishing, budget control, agency staffing or activated platform connectors.

## Phase 3 — implemented 2026-10-08

- Added a runnable, source-grounded, **approval-only** daily content orchestrator at `scripts/daily_brief.py`.
- Six role handoffs: research, strategy, creative, analytics, media-buyer, operations. These are **deterministic steps**, not independent autonomous language-model agents.
- A manually dispatched, read-only GitHub Actions workflow builds `daily-brief.md` and `daily-brief.json` artifacts. No schedule, posting, billing, production code changes or API calls by default.
- Optional AI drafting uses a separately configured OpenAI API key and an explicit opt-in; no key or spend was provisioned here.
- Unit tests cover unused-idea selection, trusted publication proof, duplicate prevention, safe output, and disabled-by-default API behavior.
- Runbook: `docs/PHASE3_RUNBOOK.md`. External/social-connected end-to-end execution has **not** been verified.

## Known measurement/data gaps

- Live 30/60/90-day commercial baseline is not yet saved in this repository.
- Installs/first-open and source-to-paid attribution were incomplete according to last documented state; do not infer installs from registrations.
- No confirmed campaign CAC/ROAS measurement here. Paid spend needs verification and approval before launch.
- Google Drive asset references are not the same as synced, authenticated media assets.
- No new actual social publishing or campaigns performed in this phase; migrated logs may contain templates/hypotheses.

## Runbook: Basic Diet Mode — ننزل إيه النهارده؟

1. Read `AGENTS.md`, active skill and this STATE.
2. Read `content/ideas/backlog.md`, `content/published/content-log.md`, and `content/strategy.md`.
3. Check verified `knowledge/offers-pricing.md` against live packages/promos, plus `assets/catalog.md` and available evidence.
4. Choose an unused idea and deliver hook, script, caption, CTA, stories, creative/asset, one KPI and paid suitability.
5. Never say a post was published until publication is verified. Record results only with confirmed source/date.

## Next implementation phase (not started)

**Phase 4 — Measurement:** obtain consented read-only 30/60/90-day commercial baseline and source-to-paid tracking evidence. Do not infer install counts or paid campaign ROAS from incomplete instrumentation.
