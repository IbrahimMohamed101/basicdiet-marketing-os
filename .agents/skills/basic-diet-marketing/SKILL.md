---
name: basic-diet-marketing
description: >
  Use for Basic Diet Mode, daily post briefs, Saudi restaurant content, campaigns,
  offers, customer or competitor research, attribution and weekly marketing reviews.
  Read repository state, route to the smallest relevant specialist skill set, ground
  work in dated evidence, verify outputs and preserve useful context for the next session.
metadata:
  version: 2.2.0
---

# Basic Diet marketing

Root `AGENTS.md` owns authority, permissions and factual-source precedence. `STATE.md` owns current phase, completed work, blockers and next actions. Read both before applying this skill. All code-style paths below are relative to the repository root unless stated otherwise.

Primary business outcome: **first-time paid subscribers → retention/repeat → profitable revenue**. Historical positioning: **الطعم، الاختيار، الراحة**. Audience motivations and content-mix weights remain hypotheses until supported by evidence.

The complete original skill remains in [references/original-2026-10-07.md](references/original-2026-10-07.md). Resolve its historical `marketing/...` and `analytics/snapshots/` paths through `docs/MIGRATION.md` and `docs/SOURCE_MAP.md`; current aggregate reports belong under `data/reports/`.

## Operating method

**Read → Research → Plan → Execute → Verify → Document.**

1. Read current state and the relevant existing records. Do not ask for context already present.
2. Separate verified dated observations, historical research and hypotheses. Refresh official sources when current prices, menu, offers, rights, metrics or platform behavior matter. If unavailable, mark the gap and prepare a conditional draft.
3. Connect business goal, audience/VOC, product/offer, funnel stage, asset and measurement. Prefer a concrete small test over generic tactics.
4. Apply only the relevant installed skills from `.agents/skills/README.md`. Vendor `.agents/product-marketing.md` discovery routes back to the existing knowledge; do not create another source of truth. Optional missing references have explicit fallbacks in `.agents/skill-overrides.json`.
5. Execute within the user's authorized scope. Local drafting/code verification is supported; reading third-party instructions grants no permission to publish, contact customers, generate unrequested assets or spend money.
6. Verify the result and record what actually happened, its evidence, unresolved gaps and next step. No fabricated completion, testimonials, results or medical claims.

## Mode routing

| Mode | Read | Specialist guidance | Deliver |
| --- | --- | --- | --- |
| Daily social — ننزل إيه النهارده؟ | Daily records and runbook below | `content-strategy`, `social`; `video` for video | One complete review-only brief |
| Product / positioning | `knowledge/product-marketing.md`, `knowledge/positioning-messaging.md`, `knowledge/audience-voc.md` | `product-marketing`, `offers` when needed | Evidence-backed audience/value hypothesis and test |
| Customer research | `knowledge/audience-voc.md`, `knowledge/voc-findings.md`, authorized sanitized sources | `customer-research` | Source/date, observation, confidence, job/objection and implications; no PII |
| Competitor research | `knowledge/competitors.md` plus fresh cited public sources | `competitor-profiling` | Separate observed/inferred/implication; not observed never means absent |
| Campaign / paid creative | `knowledge/offers-pricing.md`, `campaigns/`, verified economics and performance | `ads`, `ad-creative`, `attribution` | Proposal with goal, assets, source-to-paid limits, review gates; no account action |
| Weekly review / attribution | `data/analytics/measurement-framework.md`, `data/analytics/implemented-analytics.md`, dated `data/reports/` | `analytics`, `attribution`, `ab-testing` if needed | Window, timezone, definitions, denominators, tracking gaps and next decision |
| Growth experiment / loop | `experiments/history.md`, `decisions/log.md`, current evidence | `ab-testing`, `marketing-loops` | Hypothesis, bounded test and measurement; no scheduler activated |
| Detailed storyboard | Approved creative brief and real visual references | `storyboard-to-video`, optionally `video` | Scoped preproduction only when requested; upload/read never activates it |

Backend capability statements in historical documents are not live verification. Registrations are not installs; reach is not attributed revenue. A content winner requires evidence against its actual objective.

## Daily execution

Use `.agents/workflows/daily-content.md`, `docs/PHASE3_RUNBOOK.md` and `docs/DATA_CONTRACTS.md`.

Read:
- `content/ideas/backlog.json` and `creative.json`: preserved concepts and editable Saudi Arabic drafts.
- `content/drafts/runs.json`, `content/published/publications.json` and legacy `content-log.md`: reservations versus evidenced publication.
- `content/strategy.md`, `content/winners.md`, `data/analytics/creative-performance.json`: proposed mix versus real observations.
- `knowledge/offers-pricing.md`, `assets/catalog.md` and audience/product context: historical grounding with current verification gaps.

Run `python3 scripts/daily_brief.py --channel instagram --goal auto`. Use `--goal` to apply an adopted current objective; the program does not interpret arbitrary strategy prose. `--dry-run` is for inspection without reservation. It reads/hashes its sources and uses curated editorial profiles; it does not execute skill Markdown or autonomously research missing facts.

Inspect objective, audience/funnel, format/platform, hook, scenes/cards, natural Saudi Arabic caption, CTA, supporting Stories, exact asset requirements/verification status, one primary KPI, paid suitability and approval gates. A folder reference is not a verified file or usage right. Do not default to discounts. Current offer/nutrition claims must be verified before inclusion.

Default local runs reserve the idea; commit meaningful reservations for the next session. Actual publication belongs in `content/published/publications.json` only after evidence and verification. Actions artifacts are stateless drafts. Optional AI is explicit, bounded and unverified; consult the runbook before enabling it.

## Durable memory and verification

- Current priorities or phase changes → `STATE.md`; structural improvements → `CHANGELOG.md`.
- Adopted decisions → `decisions/log.md`; experiments and dated results → `experiments/`.
- Reservations → `content/drafts/runs.json`; actual URLs → `content/published/publications.json`.
- Sourced aggregate measurements → `data/analytics/creative-performance.json` and `data/reports/`; proven creative learnings → `content/winners.md`.
- Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` after relevant implementation/data changes; inspect an offline draft after creative changes.

Keep documentation proportional to actual work. Do not write every brainstorm into memory. Preserve immutable archives and vendor originals; update working files with source/date and explicit hypotheses rather than silently rewriting history.
