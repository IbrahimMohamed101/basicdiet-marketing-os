# Basic Diet — Jeddah organic first-page SEO sprint
Date: 2026-10-19 | owner: Marketing OS
Goal: sustainably earn first-page organic visibility for relevant local purchase-intent searches. **No guaranteed position #1**.

## Starting point (user-supplied Google Search Console)
Period: 2026-10-11 through 2026-10-17.
- 12 Google Search clicks; 10 from `بيسك دايت` (brand).
- Nonbrand queries with impressions and zero reported clicks include:
  - `اشتراك وجبات صحية جدة رخيصة` (14 impressions)
  - `أرخص اشتراك وجبات دايت جدة` (13)
  - `وجبات دايت اشتراك شهري جدة` (10)
  - `اشتراك وجبات صحية جدة` (4)
  - `اشتراك اكل صحي جدة` (3).
- The supplied report did not include average positions by query/page, exact total impressions, geo/device split, or a Google Maps Business Profile performance export. **Request these before making ranking claims**.
- Indexed pages: `/` and `/jeddah/healthy-meals`; one excluded HTTP-to-HTTPS redirect is expected and not a defect.

## Search-intent map
| Search intent | Preferred canonical page | Positioning |
| --- | --- | --- |
| Brand `بيسك دايت`, `Basic Diet جدة` | `/` | Official identity, phone, genuine Jeddah location, app and subscription links |
| `اشتراك وجبات صحية جدة`, `اشتراك وجبات دايت جدة` | `/jeddah/healthy-meals` | Useful plan comparison and what happens before checkout |
| `اشتراك وجبات صحية شهري جدة`, `وجبات دايت اشتراك شهري جدة` | Existing `/jeddah/healthy-meals` until there is distinct verified product content | Explain 26 vs 30 days and plan choice naturally |
| `مطعم دايت جدة`, `مطعم بيسك دايت` | Homepage + genuine existing Google Business Profile | Accurate address, services, hours, reviews, photos |

**Do not** add thin near-identical pages for every neighborhood or query. Don't optimize for `الأرخص` unless a current objective comparative-price study verifies it and owner approves pricing claims (site policy: no prices).

## Technical changes prepared
Backend repo `IbrahimMohamed101/basicdiet145`, site branch `landing-page-research`, PR #164 `seo/jeddah-search-intent-20261019`.
- Contextual, search-descriptive homepage-to-Jeddah internal link.
- Better helpful information for 7/26/30-day subscriptions, daily meal selection, real menu example, and Jeddah map/location.
- Page-specific BreadcrumbList structured data with canonical items.
- Dedicated automated tests for internal link, real image, canonical/structured data and mobile.
- No payment or checkout change, no unverified product/service claims or invented reviews.
- Confirm PR CI and Railway deploy success before marking this phase released.

## Owner/marketer action gate: Google Business Profile
This is critical for the Maps/local result panel. Owner must recover access to the **existing verified Basic Diet listing**, not create duplicate listings.
1. Request owner/manager access from whoever controls the existing Google Business Profile. Access to Instagram alone is insufficient.
2. Verify legal name and Arabic spelling, store location, matching phone, accurate opening hours, categories and services; confirm address `H4GX+JF7، السلامة`.
3. Set official website `https://basicdietksa.com/`; use actual original logo, storefront photos and available food photos.
4. Encourage genuine voluntary customer reviews, no payments/incentives, gating or review swaps; answer reviews where authorized.
5. Correct inconsistency: website footer and Restaurant JSON-LD currently claim **24 hours daily**. **Confirm true hours with restaurant owner** before changing either.

## Link/discovery work
- Use the tracked site links from `campaigns/basicdiet-utm-link-kit-2026-10.md` for Instagram, TikTok, Snapchat, and WhatsApp.
- Seek legitimate links from owned business profiles, partners and existing menu listings (e.g. verified actual relationship with Sally if owner confirms). Never buy bulk backlinks.
- Link new content only where it adds unique verified benefit; do not scrape, plagiarize or manufacture testimonials.
- Keep official phone, Maps location and name consistent wherever the owner controls the listing.

## Measurement: first page, not vanity impressions
Baseline: request Google Search Console `Performance > Search results`: set Saudi Arabia, Web, last 28 days then compare after 14/28 days, export Queries **and Pages** with `Clicks, Impressions, CTR, Average position`. At query level check exact brand plus the target nonbrand keywords, and at page level the two canonical URLs.
- Targets for first 14 days: production content stable, both pages indexed, zero meaningful structured-data errors, track average position/impressions/CTR for key terms.
- Targets for 30–60 days: measurable nonbrand organic clicks and increases in relevant local-query impressions and position, **not promised thresholds**.
- For business outcomes use first-time paid subscriptions; don't mistake landing clicks, leads or app-store clicks for payments. Reconcile saved website leads with verified subscription records only when authorized.
- Organic position can vary by location, device, search personalization and time. Never assert '#1' from an uncontrolled manual search.

## Next execution order
1. Finish PR #164 CI and deploy.
2. Reopen Search Console, request recrawl on updated `/jeddah/healthy-meals`; check URL live/indexable.
3. Capture query/page ranking baseline with Average Position.
4. Resolve official Google Business Profile authorization and business details.
5. Review Google business signals and nonbrand rankings every 2 weeks; prioritize edits based on real clicks and customer questions.
