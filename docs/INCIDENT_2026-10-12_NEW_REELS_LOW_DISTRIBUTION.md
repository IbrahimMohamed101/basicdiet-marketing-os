# Incident BD-SOCIAL-20261012-01 — New Reels: weak TikTok distribution, weak Instagram engagement

**Status:** OPEN — platform diagnosis pending; creative approach deprioritized pending controlled testing  
**Opened:** 2026-10-12, Asia/Riyadh  
**Scope:** ONLY the user's newly posted October 2026 videos, not September National Day promotional videos.  
**User feedback:** The first AI-animated three-meal living-poster concept did not achieve the desired result. The user wants alternative, materially stronger concepts and a root-cause investigation of TikTok's unexpectedly low views. Do not keep proposing the same “وش تختار اليوم؟” static poster/steam/leaf animation as a default Reel.

## What is actually observed (do not overclaim)

**TikTok — latest post**  
- Canonical provider-observed video: https://www.tiktok.com/@basicdiet.sa/video/7695519331622456596  
- Published 2026-10-11; reported duration 8 seconds; caption begins `وش أكثر نوع تحبونه في الصفحة؟`.  
- **Metricool read on 2026-10-12:** 2 views, 0 likes, 0 comments, 0 shares. Rechecked the same post on 2026-10-12; **still 2 views**. Some reach/watch fields are anomalous or too small a sample to interpret reliably. 
- Whether this TikTok post is *the exact same media file* as the user-uploaded Google Flow video is **not independently verified**. A related creative has been archived in `content/production/2026-10-12-living-poster-steam-leaves.md`; don't falsely equate file identity across platforms.
- **Unknown:** TikTok Studio-native view count; video privacy scope; public account setting; video For You eligibility/notification; Account check state; For You traffic breakdown; muted/rights-related notices; age of native counts / API reporting delay; eligibility for ads/boost. No evidence of a “shadowban”; do not promise that a reupload, new hashtags or a particular hour will fix distribution.

**Instagram — latest user-supplied Reel**  
- User link: https://www.instagram.com/p/DeXlqySIUxl/  
- **Native Instagram screenshot** supplied 2026-10-12: 500 views; 343 `المشاهدون` (label means viewers, not independently confirmed reach); 56% of views nonfollowers, 44% followers; 3 total interactions: 2 likes, 1 share, no saves/comments; 2 engaged accounts; **zero profile activity and zero follows**. Facebook separately displayed 96 views; do not add them as unique Instagram viewers.
- Simple 3/500 = 0.6% interactions per view, **not the Instagram platform's official engagement rate**. Nonfollower distribution exists. Watch duration/retention not provided; cannot establish exact cause. Instagram Metricool OAuth is connected but per-Reel analytics were still absent at last check; don't treat missing provider rows as zeros.
- Primary evidence is `data/reports/social/2026-10-12/instagram-last-reel-user-insights.json` and `data/reports/social/2026-10-12/instagram-tiktok-metricool.json`.

## Diagnostic order: avoid guessing TikTok algorithm

1. **Check account & post visibility in native TikTok**: Profile → ☰ → Settings and privacy → Privacy → Private account (confirm OFF if the business intends public access). On this exact video → ⋯ → Privacy settings → **Who can watch this video: Everyone**. A public TikTok link alone doesn't prove the desired in-app settings.
2. **Check TikTok Studio → More tools → Account check**, and account Inbox/profile notices. Note any actual restriction/warning. Do not infer account penalties from 2 views.
3. **Check exact video → More insights → Analytics** (enable TikTok Studio Analytics first if necessary). If “Not eligible for For You” appears, inspect the *specific stated reason* and use **Appeal** if mistaken. If none appears, record `no notice shown`, not `eligible` unless TikTok explicitly labels it.
4. **Compare native views and traffic source with Metricool**; record capture time, video URL and date for both. If they disagree, classify **connector lag** separately from distribution. Inspect video sound state and any copyright/visibility notification, **without assuming** either.
5. **Do not delete/reupload, repeatedly upload identical videos, boost or buy views** while diagnosing. Preserve post and screenshots as evidence. Review again after 24–72h, then at day 7 if appropriate.
6. If 2–3 future **distinct, original, verified-public and eligible** videos also remain near zero after 48–72h (test criterion, not a platform rule), investigate support/account-level issues and document TikTok Studio evidence. This is a repeatability experiment, not a guarantee.

**TikTok primary official references:**
- Account check: https://support.tiktok.com/en/safety-hc/account-and-user-safety/account-status
- Appeal a For You-ineligible post (with native Analytics): https://support.tiktok.com/en/safety-hc/account-and-user-safety/content-violations-and-bans
- Individual video visibility: https://support.tiktok.com/en/account-and-privacy/account-privacy-settings/video-visibility

## Creative diagnosis (hypotheses, NOT proven causal explanations)

- **Format risk:** 8-second poster mostly static with steam and lightly swaying leaves may look like a moving ad image rather than real footage. TikTok and Instagram outcomes differ; this creative-level explanation is untested, and must not be used to rationalize a potential eligibility/privacy issue.
- **Weak platform action:** Instagram reached nonfollowers but did not generate profile actions; the hook/CTA may not offer enough reason to follow, save or visit.
- **Measurement gap:** Missing TikTok native analytics, Instagram retention and verified source-to-first-paid attribution. No defensible conclusion about the opening 2 seconds or ROI.
- **Brand trust risk:** AI resynthesis previously changed genuine food textures/ingredients or logo; prefer actual approved meal/kitchen footage. No unsupported current menu/prices, nutrition or weight claims.

## Three *materially different* next creative pilots — all CONDITIONAL on approved authentic assets

| Idea | Distinct mechanism | 0–2 second Saudi hook | 3–12 second body | CTA | Primary diagnostic |
| --- | --- | --- | --- | --- | --- |
| A. Kitchen reality (Trust) | **Real** raw kitchen preparation/boxing in close-up with natural sounds; no face unless authorized | `هذي وجبتك قبل ما توصل لك` (only if verified delivery path) or safer `شوف تجهيز الوجبة` | Three true clips: real serving, real packing, final real plate with correct logo | `شوف المنيو في البايو` (after verifying link) | Qualified saves/shares and watch seconds |
| B. Decision-in-app (Product clarity) | **Actual app screen recording** of choosing a package, selecting portions/meals, total price from current working app, without invented UI | `كيف تختار اشتراكك؟` | Hands-free native screen capture highlights exact live selectors; avoid prices/promos unless verified | `تفاصيل الباقات في التطبيق` | Profile/link taps and qualified questions |
| C. Lunch problem solved (Lifestyle) | Short real-world sequence, **real workday lunch** in hand, no AI person, source footage with consent | `الغدا وسط الدوام؟` | 2s work context → 5s actual food reveal → 3s optional verified pickup/delivery facts | `شوف الوجبات المتاحة` | Average watch time and profile visits |

**Selection:** A (authentic kitchen/plate footage) is the first *candidate if footage and rights exist*. If footage is unavailable, use B with a verified app recording. C needs more production work and should remain conditional. Do not present scenes as already filmed. For Instagram, a secondary carousel may be appropriate; do **not** simply repost the same graphic as 8-second TikTok video.

## Test design / operational decisions

- First *resolve technical account/post eligibility* before explaining poor TikTok delivery as a hook failure.
- Compare **same-platform** new posts after exactly 24h/72h/7d, never compare raw 2 TikTok views with 500 Instagram views as equivalent exposure tests.
- Capture video URL, posted time (Riyadh), duration, native visibility/eligibility, view count, source (For You/followers/profile), views from nonfollowers where available, average watch seconds, retention, shares/saves/profile taps. Null means unavailable, not zero.
- **Do not publish** or buy/promote any experiment without explicit owner/user approval and verified real media/menu/commercial rights. Do not insert unverifiable creative performance into `content/winners.md` or `data/analytics/creative-performance.json`.
- **Status to advance:** account check and video analytics screenshot obtained; root-cause category known or genuinely unknown after checks; first replacement original Reel tested, then retrospective learning recorded.
- **First required user evidence:** two TikTok Studio screenshots for **this specific video**: (a) Analytics / traffic source and eligibility notice, (b) Account check or video visibility screen. The user can hide account identifiers unrelated to this post.

## Communication to future marketing agents

Treat this incident as **current priority**. The user rejected recycling the previously proposed living-poster animation as a main Reel, and wants fresh authentic content ideas with platform-specific performance review. Maintain the calm provenance and uncertainty: **user dissatisfaction is verified, algorithm penalty is not verified**. The saved living-poster creative remains a record, not a reusable “winner.”
