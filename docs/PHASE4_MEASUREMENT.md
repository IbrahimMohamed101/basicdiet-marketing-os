# Phase 4 — Read-only commercial measurement

**Status: tool implemented, no authenticated live numbers captured.**

## Source of truth checked

Backend repository: `IbrahimMohamed101/basicdiet145` on `main` (2026-10-08).
Files: `src/services/dashboard/marketingAnalyticsService.js`,
`src/controllers/dashboard/marketingAnalyticsController.js`,
`src/routes/dashboardAccounting.js`.

API: **GET** `/api/dashboard/accounting/marketing-analytics`; wrapped response
`{ "status": true, "data": { ... } }`. Route is protected by
`dashboardAuthMiddleware` and `dashboardRoleMiddleware(["admin"])`.
Existing backend route implements aggregate queries; no write operation or
marketing API endpoint changes are required.

Timezone `Asia/Riyadh`, currency `SAR`, moneyUnit `halala`,
response range `from`, `to` and `days` inclusive. Date filters passed as
`YYYY-MM-DD`. Backend `filters` defaults:
`promoCode=""`, `fulfillmentMethod="all"`, `paymentProvider="all"`,
`daysCount=null`, `grams=null`, `mealsPerDay=null`.
A filtered report is **not** a full company-wide baseline.

## KPI definitions to preserve

| KPI | Source meaning / caveat |
| --- | --- |
| `registrations` | Non-merged role=client users created in period (not app installs) |
| `loggedInUsers` | Users with `lastLoginAt` in period, not app sessions |
| `checkoutStarted` | CheckoutDraft count in period |
| `checkoutUsers` | Distinct checkout customers in period |
| `paidTransactions` | App checkout-related paid transactions |
| `paidCustomers` | Distinct app checkout-related paid customers |
| `firstTimeSubscribers` | Customer whose first historically paid subscription payment is within period |
| `repeatSubscribers` | Paid customers in period minus first-time subscribers |
| `newRegistrationsPaid` | Registered-in-period customers intersected with paid customers |
| `appRevenueHalala` | Revenue tied to app CheckoutDraft |
| `totalSubscriptionRevenueHalala` | Across app, dashboard and other subscription payment sources |
| `aovHalala` | Backend-defined average based on app revenue / paid transactions |
| `registerToPaidRate` | Backend rate of new registrations paid |
| `checkoutToPaidRate` | Backend rate of checkout customers paid |
| `repeatCustomerRate` | Backend repeat share of paid customers |

Additional counts: pending/abandoned checkouts, failed payments and cancellations.
Marketing endpoints do **not** count Play Store installs or `first_open`; do
not imply correct Meta/Google/TikTok source-to-revenue attribution, CAC or ROAS.

## Phase 4 baseline procedure — last complete Riyadh reporting day

Default reports capture 30, 60, and 90 *inclusive* Saudi calendar days ending
**yesterday**, to avoid a partially completed today. To reproduce the
2026-10-08 setup, specify `--to-date 2026-10-07`:

| Window | from | to |
| --- | --- | --- |
| 30 days | 2026-09-08 | 2026-10-07 |
| 60 days | 2026-08-09 | 2026-10-07 |
| 90 days | 2026-07-10 | 2026-10-07 |

### Option A — offline import, no API calls

On a trusted machine with an authorized dashboard session, export **three**
individual JSON API responses to a directory outside the repository:
`30d.json`, `60d.json`, `90d.json` (using matching `from`/`to`
above and `comparePrevious=false`). **Never paste access tokens in chat or
commit raw response files.** The importer validates all three period and
currency contracts before writing any files:

```bash
python3 scripts/marketing_baseline.py --input-dir /secure/local/analytics-json --to-date 2026-10-07
```

Results: ignored `output/marketing-baseline/baseline-YYYY-MM-DD-30d.json`,
similarly `60d` and `90d`, with Markdown companion reports. Each contains
only allowlisted numeric aggregates, capture metadata and caveats. Unknown
response fields, arbitrary arrays, user IDs, notes, raw payments and tokens are
discarded. Offline data is explicitly labeled
`operator_supplied_aggregate_not_live_verified`.

### Option B — explicitly authorized live, GET-only

Uses a **fixed production endpoint**, rejects redirects, never falls back to
another host and never includes tokens in output. Make dashboard credentials
available only through a secure local environment. The value must not appear
in terminal history, logs, ChatGPT, GitHub commits or output files.

```bash
# BASICDIET_DASHBOARD_TOKEN must already exist as a secure environment variable
python3 scripts/marketing_baseline.py --live --to-date 2026-10-07
```

The command fetches exactly three date-scoped API aggregates, requiring the
existing dashboard **admin** permission. No bypass, password login, token
creation or stored GitHub secret is provided. This request touches live
production only for authorized **GET** reports.

### Review and promote

1. Compare numbers with `المحاسبة → تحليلات التسويق` for same time window and filters.
2. Verify current backend schema still matches. If not, **do not** reinterpret unknown fields silently.
3. Check `firstTimeSubscribers` and app/all-channel revenue definitions.
4. Share/commit **only** reviewed allowlisted aggregate snapshots into `data/reports/`.
5. Record approved date, source authority and limitations in `STATE.md`.
6. Treat 30/60/90 windows as overlapping; **do not sum** their totals.
7. Next: verify one precise Drive asset and real published URL; reconcile UTMs
and source-to-paid before making budget scaling claims.

## Verification

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Unit tests use **synthetic** counts. Passing tests does **not** mean
production credentials were accessed, real revenue was measured, or a live
report has been captured.
