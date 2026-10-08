# Changelog

## 2026-10-08 — Phase 4 (measurement intake; live baseline pending)

- Reviewed existing backend read-only marketing analytics route and current KPI schema.
- Added local-only, strictly typed 30/60/90-day aggregate importer with optional explicit authenticated GET and source-date verification.
- Added synthetic tests for date windows, filtering, privacy allowlist, absent credentials, failed imports, and no default network access.
- Updated agent instructions, milestone status, reporting conventions and runbook.
- Did not request admin credentials, collect live business numbers, modify backend/database, publish posts or spend money.


## 2026-10-08 — Phase 3 reliability and agent-readiness audit

- Migrated all 30 ideas losslessly to validated JSON, added Saudi Arabic editorial adaptations and separate draft/publication/performance records.
- Replaced generic daily output with concrete scenes, audience/funnel, Stories, one KPI, honest asset gaps, source hashes and typed role handoffs. Added reservations, deterministic selection, legacy log compatibility and atomic output/recovery rules.
- Bounded opt-in AI, kept suggestions separate, preserved offline drafts on failure, and removed secret access from offline Actions steps. Pinned actions and expanded quality coverage.
- Added real skill YAML/reference checks, vendor context routing and explicit optional-reference fallbacks; retained every pinned vendor and storyboard byte.
- Corrected stale instructions and memory paths, documented precedence and role permissions, and allowed dated working-memory changes while keeping archives immutable.
- Expanded tests from 10 to 44; local validation and offline dry run executed. No live paid API, publication, ad action or production change. See `docs/AUDIT_2026-10-08.md`.

## 2026-10-08 — Phase 3: executable daily-brief pilot

- Added `scripts/daily_brief.py`: deterministic role pipeline, grounded idea selection and review-only creative draft, with optional manual AI rewriting.
- Added a manually-dispatched GitHub Actions workflow with read-only repository permissions and downloadable draft artifact.
- Added unit tests, local validator integration, runbook, and execution-state rules.
- No autonomous AI agents, social scheduling, posts, media spend or external data sync activated.


## 2026-10-08 — Phase 2: marketing skills integration

- Imported 13 chosen upstream skills and 67 associated Markdown references from `coreyhaines31/marketingskills` at commit `b9ba399dd88b082b926e261e8ccfb844d20aa066`.
- Preserved the MIT license; imported one non-executable static ad review HTML template used by a vendor skill.
- Added user-uploaded **Storyboard-to-Video AI Video Production Director** source in full (newline-normalized text) and a task-scoped `storyboard-to-video` skill, not an automatic activation directive.
- Documented role routing and Basic Diet priority/safety safeguards; added skill structure/provenance checks.
- Did not activate external integrations, schedule autonomous agents, publish content, or launch/spend on ads.


## 2026-10-08 — Phase 1: legacy marketing migration

- Pinned original `basicdiet145` commit `5241bfb0fe8fe4d2a15b15ed85d13648b8a7be37`.
- Archived **23 original documents/skill files** with exact source Git blob SHA; scanned for obvious phone, email, secret/key patterns.
- Added **20 unchanged working copies** in the new architecture; provided the original skill as an active-skill reference.
- Migrated the complete historical 30-idea daily content backlog, marketing/analytics research, data definitions, competitors, VOC, plans, decisions and experiments.
- Updated root entry points, migration manifest, source map and roadmap without modifying the original backend repository.
- No external third-party skills installed. No posts, ads, or payments altered.

## 2026-10-08 — Phase 0: standalone foundation

- Created private repository, `AGENTS.md`, initial skill, role definitions, validation structure and data/marketing governance.
- No platform posting or ad spend.

Historical original changelog preserved at `archive/basicdiet145-2026-10-07/marketing/CHANGELOG.md`.
