# Decision log

## 2026-10-08 — Independent private marketing repository

- **Decision:** Basic Diet marketing guidance and history live in an independent private repository, separate from app backend runtime code.
- **Reason:** keep context recoverable across agents/chats, distinguish live metrics from retained research, and enable phased work.
- **Status:** executed in Phase 0.

## 2026-10-08 — Lossless historical import (Phase 1)

- **Decision:** Keep every original marketing document and original skill under a pinned-commit archive; expose working copies under new domain paths without rewriting historical facts.
- **Scope:** 23 originals + 20 active/reference copies; root README/STATE/AGENTS remain modern operating docs.
- **Result:** Historical marketing strategy, analytics spec, 30-item idea backlog, competitor research, VOС, experiments and past decisions can be retrieved directly in the new repository.
- **Guardrail:** the historical working docs remain dated; the historic 'current week' plan is archived, not adopted as current. Original source stays untouched.
- **Source:** `docs/MIGRATION.md`.

## Future decisions

Only add decisions when explicitly adopted or validated. A drafted idea or experiment is not an approved execution result.

## 2026-10-08 — Audited deterministic drafting and durable state

- **Decision implemented:** keep one deterministic orchestrator with six typed handoff contracts; no autonomous multi-agent runtime or new generic skills.
- **Reason:** current work needs reliable evidence, reusable creative and state, not concurrent independent workers.
- **Data:** version-1 JSON for original ideas, editorial profiles, reservations, verified publications and comparable performance. Preserve original Markdown and consult legacy publications.
- **Persistence:** normal local runs reserve ideas; dry runs/Actions do not. Commit useful reservations and source-linked results. Immutable archives protect history while working records may evolve with evidence.
- **Provider/CI:** one explicit bounded optional AI request; no retries, separate unverified output. Read-only pinned Actions and full-source PR checks.
- **Verification:** local validator, 44 tests and C003 offline dry run. See `docs/AUDIT_2026-10-08.md`. No business outcomes or publishing claimed.


## 2026-10-09 — Creative Director protocol and Drive source of truth

- **Adopted:** Marketing OS is the durable project memory, while the signed read-only backend sync provides aggregate commercial context and authenticated Drive holds real source media; do not start from scratch in a new chat.
- **Mandatory cold start:** AGENTS.md → STATE.md → native basic-diet-marketing skill → docs/CREATIVE_AGENT_PROTOCOL.md; task-specific installed skills must be read before creative ideation.
- **Creative quality:** supervised AI proposes multiple genuinely distinct original Saudi-market concepts and full production prompts; deterministic Python daily briefs are offline examples, not autonomous creative reasoning.
- **Drive assets:** keep the precise folder/file references in assets/drive-source-index.json; do not treat file existence as pixel inspection, menu approval, commercial rights or published status.
- **Controls:** all actual generated media, publications, direct messages, budgets and integrations remain subject to separate authorization. Persist only decisions, confirmed sources, adopted briefs and evidenced outcomes.


## 2026-10-09 — Adopt P1 corrections after external audit

- Fix tests that incorrectly require asset verification to remain false. Permit evidence-backed transitions; no hardcoded snapshot date.
- Read short root AGENTS and docs/BOOT as startup, with task-targeted skills and evidence retrieval, not every full vendor skill/idea profile by default. Preserve old root contract in docs/OPERATING_HISTORY_2026-10-09.md.
- Track actual visually inspected sources and a first original creative draft, without calling rights, menu, public posts or purchase attribution verified.
- Enforce YAML-frontmatter creative metadata with semantic tests. Actual publishing and seven-day performance remain blocked until independently verifiable.
- Aggregate report's dashboard counts are not app checkout attribution; do not use promo records as a partition of app KPI. See docs/COMMERCIAL_AUDIT_2026-10-09.md.

## 2026-10-12 — Reuse living-poster Reel concept as a creative format

- **User-directed decision:** preserve the user-made **«وش تختار اليوم؟»** three-meal poster + 8-second Google Flow animation as a tracked *creative draft*, to avoid losing the concept in future sessions. Track it at `content/production/2026-10-12-living-poster-steam-leaves.md`.
- **Production lesson:** choose a stable 9:16 full-poster composition and restrict motion to upward food steam and decorative green leaves swaying in place; **no zoom, no falling leaves, no color change, no new objects, no changed branding or food**. AI may alter the dish during generation; verify against genuine photos.
- **Not implied:** no confirmed Instagram/TikTok publication, final owner creative approval, advertising usage rights, actual menu matches, published URL, attributed orders or performance. Need a stable approved media storage reference and real platform URLs to advance those steps.

## 2026-10-12 — Pause repeated animated-poster Reels; investigate TikTok delivery before optimizing hooks

- **Adopted by user feedback:** the new three-plate `وش تختار اليوم؟` living-poster Reel did not reach the user's desired result. Do not treat it as a winning organic pattern or automatically re-create steam/leaf motion for upcoming Reels.
- **Evidence/qualification:** Metricool latest Oct 11 TikTok video shows 2 views in two Oct 12 reads; user's native Instagram screenshot of last Reel shows 500 views, 3 interactions and zero profile actions. Platform causes **unknown**; no verified 'shadowban', content restriction, or proven hook-retention issue. The TikTok post's exact media match with the user-submitted Flow file was not proven.
- **New course:** prioritize genuine kitchen/process footage or verified in-app choice footage over nearly static AI visuals; put the first two seconds, actual product truth, story, and useful CTA above decorative animation. Treat three replacements as hypotheses, not campaign results.
- **TikTok recovery first:** check actual post visibility, TikTok Studio Account check, native Analytics/For You eligibility and sync discrepancy. Preserve the existing post while diagnosing. No impulsive delete/repost, boost, or spending.
- **Canonical incident/report:** `docs/INCIDENT_2026-10-12_NEW_REELS_LOW_DISTRIBUTION.md`. Original draft `content/production/2026-10-12-living-poster-steam-leaves.md` is historical evidence, not current default.
