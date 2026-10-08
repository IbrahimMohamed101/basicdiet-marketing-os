# Basic Diet Marketing OS — current state

**Last verified: 2026-10-08. Phase 3: audited local draft workflow.**
**Current implementation: Phase 4 measurement intake prepared; authenticated live snapshots not yet obtained.**

## Business and evidence

Basic Diet is a Saudi meal-subscription restaurant. North star: first-time **paid** subscribers → retention/repeat → profitable revenue. Historical positioning: **الطعم، الاختيار، الراحة**; familiar food, portion choice and convenience. Audience segments are hypotheses. The 7/26/30-day plans, portions, menu, prices, promos and Jeddah coverage are 2026-10-07 historical context, requiring fresh official verification before claims. See `knowledge/` and `docs/SOURCE_MAP.md`.

## Verified implementation

- Historical migration: 23 archive originals retain source blob hashes; 20 mapped working paths exist and still match their initial bytes at audit time. Working knowledge can evolve; archive content cannot.
- 13 vendor skills + 67 references, MIT license and static creative template retain pinned upstream hashes. Native Basic Diet and storyboard entry points make 15 skills. Original user storyboard text is preserved and never auto-activates.
- Daily CLI: versioned JSON ideas/publications/reservations/performance, lossless 30-idea migration, 30 editorial adaptations, source hashes, structured six-role handoffs and offline Arabic briefs.
- Normal local runs reserve ideas; `--dry-run` and Actions produce drafts without reservation. Output is ignored by Git; reviewed ledger changes must be committed for future sessions.
- Optional AI: one bounded explicit request, separate unverified output, safe failure status; no paid request executed in this audit.
- Validation and 44 unit/integration tests passed locally during the audit. Final evidence and any remote CI result belong in `docs/AUDIT_2026-10-08.md` / the PR checks, not an assumed deployment claim.

## Current operating records

- Ideas: `content/ideas/backlog.json`; original Markdown preserved.
- Editorial scripts: `content/ideas/creative.json`; proposals, not approved product facts.
- Reservations: `content/drafts/runs.json` (empty at audit; realistic test used `--dry-run`).
- Publications: `content/published/publications.json` (empty); legacy Markdown template still consulted.
- Performance: `data/analytics/creative-performance.json` (empty); no measured creative winners.
- Adopted architecture: `decisions/log.md`; contracts/recovery: `docs/DATA_CONTRACTS.md`.

## Dry-run outcome

The realistic offline Instagram run selected **C003**, awareness: **«إذا قلت أكل دايت… وش أول طبق يجي في بالك؟»**. It produced a 15-second Reel plan, Saudi Arabic caption, three Stories, audience/funnel, Reach as a diagnostic KPI and explicit review gates. No exact media file, current menu, destination link or rights were verified. Paid suitability remains NOT_READY. No publication, reservation, message, asset generation or advertising action occurred.

## Phase 4 measurement intake — implemented 2026-10-08

- Existing backend analytics contract inspected: admin-only `GET /api/dashboard/accounting/marketing-analytics`, Riyadh calendar-day reporting, count/rate/revenue metrics returned as aggregates.
- Added `scripts/marketing_baseline.py` and `tests/test_marketing_baseline.py`: safe import of three period reports or explicit authenticated read-only GETs, with strict exact period and currency checks.
- Outputs contain only selected aggregate KPIs and provenance, **not** raw response arrays, customer data, bearer tokens or invented values.
- Outputs stay ignored locally until independently reviewed and explicitly documented as source-verified.
- Current blocker: no dashboard session or production credentials are available to this repository. No live baseline numbers have been captured. Full runbook in `docs/PHASE4_MEASUREMENT.md`.

## Blockers and next actions

1. Verify recent actual social history and an exact approved media file/rights for the first reviewed idea; populate publication records only from real evidence.
2. Obtain authorized, sanitized 30/60/90-day commercial snapshots using `scripts/marketing_baseline.py`, review them, then commit approved aggregate-only results under `data/reports/`.
3. Reconcile source-to-first-paid attribution. Install/first-open counts, CAC and ROAS are not established here; historical backend capability claims were not reverified.
4. Run a small human-approved organic pilot, capture URLs and seven-day measurements, then adjust creative hypotheses. Posting itself still requires explicit action authorization.

No live integrations, autonomous workers, publishing scheduler or paid campaigns are deployed. Existing user authorization governs requested local coding/review work; root `AGENTS.md` owns permissions and precedence.
