# Marketing OIDC live sync verification — 2026-10-08

**Status: PASS for signed data retrieval and private repository persistence.**
**Evidence:** [GitHub Actions run #37805596216 (attempt 2)](https://github.com/IbrahimMohamed101/basicdiet-marketing-os/actions/runs/37805596216), backend Railway production deployed successfully, and the following three immutable report files.

## Connection proof

1. The Railway production service `basicdiet145` has `MARKETING_AGENT_OIDC_ENABLED` configured (observed via service variable names, without reading or copying secrets).
2. Its latest deployment was `SUCCESS`.
3. An authorized failed-job rerun of `Basic Diet - signed commercial data sync` completed **SUCCESS** on attempt 2; the data pull/store step is green.
4. The workflow wrote `data/reports/commerce/2026-10-07/{30d,60d,90d}.json` to private Marketing OS `main`, commit `889d853e592fb036a984519bee1d3edfb5c79881`.
5. Each file has `verification=official_authenticated_aggregate_response`, `origin=signed_github_actions_oidc_readonly`, `source_mode=live`, `timezone=Asia/Riyadh`, `currency=SAR`, `money_unit=halala`, and matching inclusive periods.
6. Basic safety/integrity scan: aggregate fields and allowlisted breakdown names only; no ordinary personal contact/user/token fields in the inspected persisted JSON. This is not a formal security/privacy audit.

## Aggregate comparison

| Metric | 30 days (2026-09-08 onward) | 60 days (2026-08-09 onward) | 90 days (2026-07-10 onward) |
| --- | ---: | ---: | ---: |
| Registrations | 162 | 329 | 425 |
| Checkout starts | 105 | 176 | 205 |
| Distinct paid customers | 65 | 97 | 114 |
| First-time paid subscription customers | 47 | 86 | 114 |
| Repeat customers (window-relative) | 18 | 11 | 0 |
| Paid transactions | 70 | 117 | 138 |
| App-checkout revenue, SAR | 67,101.20 | 114,700.15 | 138,481.80 |
| All-source subscription revenue, SAR | 109,732.15 | 196,102.20 | 250,664.00 |

All three periods end at **2026-10-07** (last complete Saudi reporting day of this verification). **The windows overlap; never add them together.**

## Quality checks

- **PASS:** `paidCustomers = firstTimeSubscribers + repeatSubscribers` in all windows.
- **PASS:** daily row count and unique dates are exactly 30, 60, 90 respectively; the first/last daily date matches each period.
- **PASS:** sum of daily registrations, paid transactions, and app revenue exactly matches period-level KPIs for all three windows.
- **PASS:** revenue is denominated in **halala** in JSON; SAR displayed here divides by 100.
- **PASS:** allowed breakdowns include promo, plans, daily aggregates, payment provider, fulfillment and source channel.
- **PASS:** the production sync used signed GitHub OIDC and did not require a dashboard admin token.

**Metric interpretation:** `repeatSubscribers` is relative to the start of the requested reporting window: a customer can count as repeat in a 30-day window, but as first-time paid in a 60- or 90-day window if their first historical payment falls earlier than the 30-day start but within the longer window. Therefore do not interpret decreasing repeat counts across nested windows as proof of a retention decline. See `basicdiet145/src/services/dashboard/marketingAnalyticsService.js`.

## Still unverified / future gates

- Direct independent unauthenticated HTTP 401 check was not completed from this assistant's available HTTP browsing environment; JWT signature and negative-claim protections were separately tested in the backend suite.
- The following day's scheduled update has not run yet, so **daily recurrence is configured but not empirically verified**.
- Historical app installs/first_open, Meta campaign cost, creative-to-paid attribution, CAC/ROAS, and independent payment reconciliation are **not available** from this report.
- Meta/Facebook/Instagram connections are still absent in the currently inspected Metricool brand.
- No advertising, public post or account action was performed.
