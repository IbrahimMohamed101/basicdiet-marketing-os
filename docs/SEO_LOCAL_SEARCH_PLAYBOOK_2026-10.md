# Basic Diet — SEO and Jeddah Local Search Playbook (2026-10-09)

Status: **Phase 1 technical SEO implemented; Google/Search Console production verification pending.**
Business: Basic Diet, healthy meal restaurant and subscriptions in Jeddah, Saudi Arabia.
Primary outcome: first-time **paid** subscribers; secondary outcomes: qualified leads and app installs.
Do not conflate organic clicks, landing enquiries, registrations, and paid subscriptions.

## Search intent and launch targets

1. اشتراك وجبات صحية جدة — transactional/local
2. اشتراكات وجبات صحية — national/transactional, longer-term target
3. اشتراك وجبات دايت جدة — local intent
4. اشتراك وجبات صحية شهري — package intent
5. اشتراك وجبات صحية أسبوعي — package intent
6. توصيل وجبات صحية جدة — city delivery intent; avoid claims about unsupported neighborhoods
7. مطعم دايت جدة — Maps/local-intent

These are **intent hypotheses**, not keyword-volume or rank claims.
Semrush keyword dataset unavailable in this run (insufficient API units).
Validate using connected, verified Google Search Console once site/domain is live.

## Competitor signals (qualitative; not audited ranking positions)

- dietworldsa.com has a location-specific, dedicated page targeting اشتراك وجبات صحية جدة.
- palmeradiet.com has category landing content for weekly/monthly diet subscriptions in Jeddah.
- octafoodksa.com presents package detail, meal counts and delivery FAQ.
- dailymealz.com presents weekly/monthly subscriptions and a clear customer journey.
Source review date: 2026-10-09. Do not copy pages, inflate text with keywords, or claim comparative prices without fresh verification.

## Phase 1: deployed website SEO foundation

Repo: IbrahimMohamed101/basicdiet145, branch: landing-page-research.
PR: https://github.com/IbrahimMohamed101/basicdiet145/pull/152
- Clearer home page title/description and natural Jeddah service phrase.
- Unique Arabic user-oriented route: /jeddah/healthy-meals; 7/26/30-day descriptions, help choosing plans and genuine FAQs.
- Live lead-request CTAs integrated in new page, preserving mandatory opt-in and plan validation.
- Auto-generated robots.txt and sitemap.xml.
- Same-site links from footer and working cross-page nav.
- Restaurant structured data enriched with identifiable Jeddah Google Maps location.
- Canonical site origin tied to NEXT_PUBLIC_SITE_URL; update it on domain binding.

Do not invent prices, delivery coverage, expert endorsements, customer results or fake reviews.
Don't add thin neighborhood doorway pages. Add useful pages only when there is unique verified information.

## Phase 2: custom domain and Google ownership — access required

1. Have restaurant owner register **one** brand-controlled domain, not a hosting plan.
   Preferred: basicdiet.sa if a licensed registrar verifies availability and ownership eligibility.
   Alternative: basicdietksa.com (available during Namecheap check 2026-10-09 at $10.98 first year);
   availability and offers can change. basicdiet.com is currently unavailable.
   TLD/domain keywords alone do NOT ensure good rank.
2. Add verified domain to Railway basicdiet-landing service.
3. Update NEXT_PUBLIC_SITE_URL to the canonical https://domain and redeploy.
4. Make old Railway origin canonical/redirect to primary domain only after confirming Railway health
   and backlinks/app links. Avoid indexing duplicate copies as separate sites.
5. Google Search Console: verify the Domain property using registrar DNS TXT.
   Inspect / and /jeddah/healthy-meals, submit sitemap.xml, request indexing.
6. Check Google Business Profile owner access for the already listed
   بيسك دايت - Basic Diet (Jeddah, Al Salamah). Preserve genuine listing, don't create duplicate.
   Update primary website URL, accurate category, services/subscriptions, hours, phone,
   store photos and existing menu link if allowed by the owner.
7. Encourage authentic customer reviews with no incentives or review gating.
   Never claim control or access to the GBP until owner grants it.

## Phase 3: four-week content cadence

Week 1: verify GBP/Search Console, public contact details, canonical/coverage, measure baseline.
Week 2: publish a genuinely helpful FAQ / short article about choosing a 7 vs 26 vs 30-day subscription.
Week 3: publish a real operations explainer (what delivery vs pickup means, real coverage only).
Week 4: publish a photo-led authentic meal example with verified portion and nutrition data if
provided by restaurant; otherwise omit nutrition promises. Cite official menu/app data.

Distribute links via Instagram reels bio, TikTok, Google Business Profile updates,
existing menus-sa listing if platform allows, and relevant locally earned citations.
No bought backlinks or generic directory spam. The QR on the old menus-sa page
must continue working; link to new site instead of breaking printed collateral.

## Measurement and closure

- First measurable baseline day after custom-domain indexation.
- Search Console: impressions, clicks, CTR, average position by keyword and URL.
- GBP: local discovery, direction requests, calls and website clicks, if accessible.
- Landing backend: lp_view, CTA clicks, genuine distinct MongoDB leads (uniqueLeads).
- Business outcome: first-time verified paid subscriptions with campaign attribution
  where reliably available; no unsupported join to anonymous sessions.
- 30-day progress review; 60–90 day content refinement. No guaranteed ranking timeframe.
- Keyword target metrics unavailable until Google Search Console or another
  authorized keyword-volume tool is connected.

## Not yet verified / do not overclaim

- basicdiet.sa availability not confirmed by a licensed Saudi domain registrar.
- Google Business Profile listing exists on maps, but admin control is unverified.
- Domain purchase, DNS linking, Search Console ownership and indexing have not happened.
- Organic keyword positions, search volumes and conversions have not been measured yet.
