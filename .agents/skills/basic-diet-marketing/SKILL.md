---
name: basic-diet-marketing
description: >
  Operating skill for all Basic Diet marketing work. Activate whenever the user says
  "Basic Diet Mode", asks what to post today, requests a marketing plan, content strategy,
  campaign, offer, ad creative, customer research, competitor research, marketing analytics,
  attribution, weekly review, retention idea, or any marketing decision for Basic Diet.
  This skill requires agents to read the repository Marketing OS before generating tactics,
  ground recommendations in real Basic Diet inputs, and document meaningful execution/results
  so future chats can continue without starting over.
metadata:
  version: 2.1.0
---

# Basic Diet Marketing Skill

## Phase 1 operational bootstrap (2026-10-08)

The complete original skill is preserved unchanged in `references/original-2026-10-07.md` and `archive/basicdiet145-2026-10-07/skills/basic-diet-marketing/SKILL.md`. This active skill adapts paths to the separate marketing repository and carries forward the former full operating rules.

1. Read root `AGENTS.md` and `STATE.md` before interpreting the task.
2. Read only the relevant migrated working documents. Resolve any remaining historical `marketing/...` paths with `docs/MIGRATION.md`.
3. Historic competitor, price, package, analytics and content facts were reviewed in 2026-10-07. They are **not automatically live**. Always verify live facts before publishing material claims or approving spend.
4. All social publication, outgoing messages, changes to offers/pricing, budget commitments and third-party campaign execution require explicit user approval. No unverified publication or paid results can be represented as completed.
5. No raw customer personal data, credential material or private conversations in Git; store dated aggregate records with source/timezone/scope only.
6. The six Markdown role descriptions in `agents/` are planning contracts, not running autonomous agents. External upstream marketing skills are **not installed until Phase 2**.


## Mission

Operate Basic Diet marketing as a learning system, not a series of disconnected ideas.

Primary outcome:

**First-time paid subscribers -> repeat/retention -> profitable revenue**

## Mandatory startup

Before any meaningful Basic Diet marketing task:

1. Read `STATE.md`.
2. Read the relevant context/logs for the task.
3. Check live/fresh sources when the answer depends on current metrics, campaigns, competitors, trends, prices, or platform behavior.
4. Do not ask the user to repeat information already documented.
5. Do not assume an old snapshot is current live data.

## Source priority

Use the right source for the right fact:

1. **Live backend/dashboard** — current commercial metrics and product behavior.
2. **Google Drive** — creative assets, menus, product source material.
3. **Marketing OS** — durable context, decisions, previous experiments and learnings.
4. **Current public research** — competitors/market/platform changes.
5. **Hypothesis** — only when evidence is incomplete; label it clearly.

## Marketing brain

For every recommendation, connect:

`Business goal + audience/VOC + product/offer + funnel stage + creative asset + measurement`

A marketing output missing those links is incomplete.

## Core modes

### 1. Product/Positioning
Use when deciding audience, value proposition, messaging, differentiation, objections, proof, or brand voice.

Read:
- `knowledge/product-marketing.md`
- `knowledge/positioning-messaging.md`
- `knowledge/audience-voc.md`

Separate:
- known facts,
- hypotheses,
- learned customer truth.

### 2. Customer Research / VOC
Mine real reviews, support/customer-service language, comments, objections, cancellations and renewal reasons.

Extract:
- job to be done,
- pain,
- desired outcome,
- trigger,
- objection,
- alternatives,
- exact language.

Assign High/Medium/Low confidence.

Never commit PII.

### 3. Competitor Intelligence
Use current public sources.

For every important claim mark mentally or explicitly:
- observed,
- inferred,
- implication.

Never treat "not observed" as "does not exist."

### 4. Content Strategy
Read:
- `content/strategy.md`
- `content/published/content-log.md`
- `content/winners.md`
- `assets/catalog.md`

Optimize the mix from measured outcomes; do not preserve pillar percentages as dogma.

### 5. Daily Social Execution

Trigger example:
> Basic Diet Mode — ننزل إيه النهارده؟

Process:
1. Check current weekly objective.
2. Check recent content.
3. Check current funnel/analytics when available.
4. Check active offer.
5. Choose a grounded idea and asset.
6. Select one primary KPI.
7. Return:
   - objective,
   - audience/funnel stage,
   - format,
   - hook,
   - script/design,
   - caption,
   - CTA,
   - supporting stories,
   - exact/recommended asset,
   - KPI,
   - whether it is suitable for paid promotion.
8. After actual publication, update `content/published/content-log.md`.

Never default to "post a discount."

### 6. Offers
Before proposing a bigger discount, ask whether value can be improved through:
- convenience,
- bundle,
- delivery,
- add-on,
- return/reactivation,
- referral/partnership,
- better framing.

Check live economics before recommending a commercial offer for launch.

### 7. Paid Ads / Creative
Do not generate scaled ad batches from thin air.

Build from:
- winning content/ads,
- reviews/VOC,
- comments/objections,
- product facts,
- brand assets,
- offer,
- actual campaign performance.

Testing loop:
`Signal -> concept -> variants -> launch -> measure -> winner/loser -> next iteration`

Do not scale spend based only on CTR or views.

### 8. Analytics / Attribution
Read:
- `data/analytics/measurement-framework.md`
- `data/analytics/implemented-analytics.md`

Rule:
**Track for decisions, not for data collection.**

Never report installs or attribution as known if they are not instrumented.

### 9. Marketing Learning Loop
Weekly:
1. Pull live results.
2. Compare against baseline/previous period.
3. Identify meaningful winners/losers.
4. Check for tracking/data-quality issues before interpreting changes.
5. Generate a small number of hypotheses.
6. Prioritize next tests.
7. Update experiments/content winners/state as appropriate.

## Grounding rules

Every important creative/campaign concept should be traceable to one or more:
- verified menu/product fact,
- existing asset,
- real customer language,
- measured winner,
- current offer,
- business/funnel data.

Forbidden:
- fabricated testimonials,
- fabricated metrics,
- unsupported medical/weight-loss claims,
- claiming customer motivations as facts without evidence,
- using stale pricing without verification for a live campaign.

## Documentation protocol

Meaningful work follows:

**Execute -> Verify -> Document**

Update:
- `STATE.md` when project phase/priorities materially change.
- `CHANGELOG.md` when Marketing OS structure/context changes materially.
- `decisions/log.md` for strategic decisions.
- `experiments/history.md` for tests.
- `content/published/content-log.md` for published content.
- `content/winners.md` only after evidence.
- `analytics/snapshots/` for dated decision-relevant aggregate metrics.

Do not create documentation noise for trivial brainstorming that was not chosen/executed.

## External framework inspiration

This skill adapts useful concepts reviewed from:
- `coreyhaines31/marketingskills` (MIT-licensed at review time)

Especially:
- product marketing context,
- customer research,
- social/content,
- offers,
- ads/ad creative,
- analytics,
- attribution,
- marketing loops.

Basic Diet-specific evidence and business rules always override generic framework advice.
