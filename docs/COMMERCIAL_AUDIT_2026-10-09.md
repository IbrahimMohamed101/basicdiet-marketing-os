# Source/channel and promotion metrics audit — 2026-10-09

Source: committed, signed read-only backend aggregates \`data/reports/commerce/2026-10-08/30d.json\` and \`2026-10-07/30d.json\`. These are different **rolling 30-day windows**; snapshot capture time differs. Calculations below audit arithmetic; they do not verify the backend aggregation business semantics.

## Window through 2026-10-08 (2026-09-09 → 2026-10-08)

| Measure | Observed | Valid calculation / limitation |
| --- | --- | --- |
| App source transactions | 65 | Equals app \`paidTransactions=65\` |
| Dashboard source transactions | 50 | Separate channel; no established origin WhatsApp/DM |
| Combined source channel count | 115 | 65 + 50; **not** the app-only paidTransactions KPI |
| App revenue | 6,127,090 halala | Matches appRevenueHalala |
| Dashboard revenue | 4,007,895 halala | Distinct from app revenue |
| Combined source revenue | 10,134,985 halala | Matches totalSubscriptionRevenueHalala |
| App first-time subscribers | 43 | Backend window-specific definition; **not** reconciled to first-ever paid across all sources |
| KSA96 consumed/paidCount | 81 | Promo reports likely cover a different scope, but exact contract must be verified |
| Sum of promo paidCount across four labels | 95 | **Cannot** be compared as a partition of app-only 65 without backend scope and dedupe contract |
| KSA96 discount/revenue | 3,333,090 / 7,777,210 halala | Not enough to infer promotion caused any volume or profitable ROI |

## Rolling window comparison

KSA96 entries (attempts 109, consumed 81, paidCount 81, promo revenue 7,777,210 halala) are identical in 2026-10-07 and 2026-10-08 reports. This **may** happen if no relevant coupon record aged in/out of the rolling range; it also may indicate all-time rather than period-scoped promo aggregation. **Unresolved** until backend query/filter is audited. Other KPI and BASIC15 counts changed, so snapshots are not exact copies.

## Decisions for attribution

1. Do not claim 43% of "paid transactions" as attributed dashboard acquisitions: 50/115=43.5% of **source-channel subscription records**, whereas app-only transactions=65; denominator and event semantics differ.
2. Do not assume code usage records uniquely equal orders, first-time paid buyers, or revenue caused by the promo.
3. To connect creatives to **dashboard** sales: capture source/campaign/creative manually in the protected checkout/admin workflow only with a privacy review, controlled values and event identity dedupe. This is **not implemented** here.
4. Check backend service aggregation semantics for all promo breakdowns, including date filters, cancellation counting and the sourceChannels-to-KPI relationship, before enforcing equality assertions or editing production data.

## Follow-up and limitation

A lightweight offline checker may assert the documented **source revenue** sum and **app source revenue** mapping, but MUST NOT fail on \`promoPerformance.paidCount > app.paidTransactions\` without a shared denominator/contract. No dashboard, payment or promo source code was changed by this audit. Live backend behavior remains to be investigated before interpreting "discount dependence."
