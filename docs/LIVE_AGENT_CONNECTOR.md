# Basic Diet: Live Marketing Agent Connector

## Architecture

Marketing OS runs a private GitHub Actions workflow (.github/workflows/sync-commerce.yml).
It requests an ephemeral signed identity from the official GitHub Actions OIDC issuer.
The backend verifies RSA signature and hard-binds the token to the immutable repository ID,
the exact main-branch workflow, private visibility, accepted event and dedicated audience.
No dashboard user token, admin password or long-lived API secret is required.

Data flow: GitHub Actions OIDC -> backend GET /api/marketing-agent/commercial-report
-> 30/60/90-day aggregates -> validated sanitized snapshots -> private GitHub main.

Service code: basicdiet145/src/middleware/marketingAgentOidc.js and src/routes/marketingAgent.js.
Backend production Railway service: basicdiet145 in dependable-alignment/production.
Deployment flag: MARKETING_AGENT_OIDC_ENABLED=true, default disabled.

## Allowed scopes

- Read aggregated registrations, checkouts, paid customers, first-paid subscribers, repeaters, conversion, revenue.
- Read plan/promo/payment-provider/fulfillment breakdowns and daily aggregate time series.
- No API access to individual users, customer phone numbers, order details, database collections, or customer messaging.
- The existing dashboard admin analytics endpoint and authentication remain unchanged.
- No ability to post to Facebook/Instagram, run ads or change offers.

## Recording

- Action sync-commerce.yml: manual dispatch plus daily 02:30 UTC (05:30 Saudi).
- One push-triggered bootstrap run only when this workflow file first lands on main.
- Writes immutable snapshots at data/reports/commerce/YYYY-MM-DD/30d.json, 60d.json, 90d.json.
- Checks for existing report paths and refuses to overwrite. A run failure never claims capture.
- Bounded numeric allowlist, verified date ranges, Asia/Riyadh and SAR/halala units.
- GitHub content writing is constrained by workflow code, not by GitHub token path-scoped permissions.
- One network request for OIDC identity and three backend GET reports per run, plus GitHub API writes.
- GitHub private repo Actions usage may count toward plan limits. Inspect GitHub usage.

## Agent use

Start with root AGENTS.md, STATE.md, existing native marketing skill.
Use the newest completed dated snapshots only; attach the reporting window and data source to each conclusion.
Use first-time paid subscribers as the commercial North Star. Separate attributed conversions
from unattributed overall paid subscribers. Never claim CAC/ROAS without verified ad spend and attribution.
Do not add raw API envelopes or tokens to the repository; public campaign posts need separate approval.

## Initial activation checklist

1. Merge backend security PR and verify its dedicated OIDC tests are green.
2. Deploy backend with MARKETING_AGENT_OIDC_ENABLED=true on Railway production.
3. Verify unauthenticated GET returns 401 and no private data. Without flag, endpoint returns 404.
4. Merge Marketing OS sync PR to main only after backend endpoint is ready.
5. Inspect bootstrap Actions run, ensure 3 commercial snapshots land as sanitized JSON.
6. Review numbers against dashboard المحاسبة → تحليلات التسويق.
7. Confirm next scheduled daily sync and that errors are visible. Do not assume CI green equals live access.

## Social platform account phase

- Metricool connector was inspected on 2026-10-08; brand exists but no social network was connected.
- Have the restaurant account owner authorize Meta Business Instagram and Facebook Pages
  via the provider's official OAuth connection UI. Keep credentials inside provider/approved secret store.
- Record platform account IDs, scopes, reconnect status and measurement definitions in an access-controlled registry.
- Start read-only impressions, reach, interactions and post URLs; only then add campaign measurement joins.
- Spend, automatic posting and inbox messaging remain disabled without separate user approval.

## Security caveats

GitHub Actions id-token/write identity is short-lived; this is not an independent always-online autonomous agent.
Data refresh happens when Actions runs. A direct agent reading repository files sees latest completed snapshots.
GitHub Actions storage/repo commits are not a substitute for event-level attribution; app instrumentation
and payment-source joining require a later explicit phase.
