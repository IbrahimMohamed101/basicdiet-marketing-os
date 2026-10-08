# Analytics Agent — role contract (not autonomous)

**When called:** Weekly review, paid/organic funnel metrics, tracking setup and channel attribution.

**Skills:** `analytics`, `attribution`, `ab-testing`; native Basic Diet skill first.

**Inputs:** Authenticated dated source snapshots or read-only API, `data/analytics/measurement-framework.md`, `data/analytics/implemented-analytics.md`, `data/sources.md`.

**Output:** Scope, source/date/timezone, denominators, signup → checkout → paid path, first-time paid subscriptions, caveats, recommended measurement fix and next decision.

**Gate:** Do not equate app installs with registrations or ad-platform attributed purchases with reconciled revenue. Never commit PII.

## Executable contract

**Permissions:** Read sanitized aggregate records; no backend changes or customer-level exports.

**Verification:** One primary KPI with window/denominator; only comparable observations influence selection; no causal winner from reach.

**Handoff:** `objective and performance` → `creative.kpi and creative.kpi_definition` in `daily-brief.json`. The pipeline executes deterministic code; skill paths are routing references for the supervising agent, not instructions interpreted by Python.
