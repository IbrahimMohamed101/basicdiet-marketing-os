# Sanitized marketing aggregate reports

Phase 4 importer: [`scripts/marketing_baseline.py`](../../scripts/marketing_baseline.py)
with [runbook](../../docs/PHASE4_MEASUREMENT.md).

**Do not commit:** dashboard Bearer tokens, local response exports, names, phone
numbers, user IDs, checkout details or raw paid transaction records.

The importer produces ignored drafts in `output/marketing-baseline/` with
`baseline-<to>-30d|60d|90d.json` and matching Markdown. After comparing
these reports with the authenticated dashboard and confirming scope, a human
may place explicitly approved, aggregate-only immutable snapshots here.
Do not auto-label a manual import as official live verification.

Record date range (inclusive Saudi days), `captured_at`, source, filters,
timezone Asia/Riyadh, money in **halala**, the definition of first-time paid
subscribers, and limits of missing app-install/ad attribution metrics.

**No live reports have been captured as part of Phase 4 implementation.**
