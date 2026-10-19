# Basic Diet — tracked landing links (19 October 2026)

**Canonical destination:** https://basicdietksa.com/

## Ready-to-paste links

| Placement | URL |
| --- | --- |
| Instagram bio | https://basicdietksa.com/?utm_source=instagram&utm_medium=organic_social&utm_campaign=profile_2026q4&utm_content=bio |
| TikTok bio | https://basicdietksa.com/?utm_source=tiktok&utm_medium=organic_social&utm_campaign=profile_2026q4&utm_content=bio |
| Snapchat profile | https://basicdietksa.com/?utm_source=snapchat&utm_medium=organic_social&utm_campaign=profile_2026q4&utm_content=bio |
| WhatsApp Business profile | https://basicdietksa.com/?utm_source=whatsapp&utm_medium=referral&utm_campaign=profile_2026q4&utm_content=business_profile |
| WhatsApp follow-up (only for approved, consented contact) | https://basicdietksa.com/?utm_source=whatsapp&utm_medium=referral&utm_campaign=followup_2026q4&utm_content=message |
| Instagram Story link sticker | https://basicdietksa.com/?utm_source=instagram&utm_medium=organic_social&utm_campaign=stories_2026q4&utm_content=story_01 |

All are ordinary HTTPS links. Publishing/link changes in external platforms are **not** performed by this file. Use each link only in its named placement and test opening in an incognito browser and the platform's in-app browser.

## Rules for each campaign

- Keep `utm_source` a stable platform name (`instagram`, `tiktok`, `snapchat`, `whatsapp`).
- Keep `utm_medium` stable: `organic_social`, `paid_social`, `referral`, `cpc` (paid only when actually paid).
- Name `utm_campaign` once, lowercase Latin letters/numbers/underscore; example `meal_subscription_2026q4`.
- Use `utm_content` to distinguish a specific approved creative; e.g. `reel_20261019_c032`.
- NEVER include customer names, phone numbers, IDs, credentials, or other personal data in URL parameters.
- Do not tag internal site-to-site links with new UTMs; those overwrite valid external attribution.
- Never infer an installation, payment, or paid-source return from a store click or lead alone.

## Known baseline (operator-supplied dashboard, 2026-10-19)

Landing report 2026-09-20 through 2026-10-19: 198 page-view events, 193 browser-tab sessions (not distinct people), 21 saved leads, 70 start-subscription clicks, 25 app-store clicks. Old source grouping: 139 empty UTM, 49 `ig`, 10 `snapchat`; referrer rows include Google and Instagram but can be unavailable in many in-app browsers. Sources without evidence are **unattributed**, not proven direct.

Search Console sample 2026-10-11 through 2026-10-17: 12 organic clicks, 10 for `بيسك دايت`. This is a separate data source and range; do not add it to landing page views or interpret clicks as people.

## Tracking and review

- Website `/api/analytics` sends events to a protected backend route. `UTM` values are session-scoped and forwarded with submitted leads.
- Pending code PRs classify source as tagged, referrer-inferred, or unknown, including historical records with referrers; **missing external data cannot be reconstructed**.
- After production verification, observe source attribution coverage: `(tagged + inferred) / pageViews`.
- Check page views, leads, CTA clicks, app-store clicks, page/device/referrer, and staff lead statuses weekly; compare equivalent date windows.
- In dashboard `المحاسبة → تحليلات التسويق → تحليلات صفحة Basic Diet`, check the two panels for sources and lead status. A staff label of converted is not proof of paid purchase. Use verified subscription linkage and payment records where authorized.
- Main outcome remains **first-time paid subscriptions**. Attribution to purchase requires a verified identity handoff/reconciliation; do not claim campaign ROAS without it.

## External profile checklist (manual owner action)

- [ ] Replace Instagram profile website with the Instagram bio link above.
- [ ] Add TikTok bio URL if account permits.
- [ ] Add Snapchat profile URL if available.
- [ ] Update WhatsApp Business website field and use the follow-up link only with opted-in customers.
- [ ] Test all visible links and verify events in dashboard after opening each in a fresh tab.
- [ ] Record next baseline after at least seven complete Saudi reporting days.

No marketing material was posted, profile edited, or ad budget spent as part of this link kit.
