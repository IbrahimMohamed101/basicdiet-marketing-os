# Basic Diet Marketing OS — current state

## 2026-10-12 — PRIORITY INCIDENT: latest TikTok Reel 2 views; change creative approach

- **Read first:** `docs/INCIDENT_2026-10-12_NEW_REELS_LOW_DISTRIBUTION.md`. The user explicitly reports that the new three-meal living-poster idea performed far below expectation and asks for different concepts and TikTok troubleshooting rather than more variants of the same static-animated poster.
- **TikTok latest (Oct 11 video; checked again Oct 12):** Metricool still reports **2 views, 0 likes, 0 comments, 0 shares** for `https://www.tiktok.com/@basicdiet.sa/video/7695519331622456596`. Low distribution is observed, **NOT** a proven shadowban/content penalty. Need the user's TikTok Studio video Analytics/For You eligibility, privacy and Account check screenshots.
- **Instagram user screenshot:** `https://www.instagram.com/p/DeXlqySIUxl/` showed 500 views; 56% from nonfollowers, 3 interactions and no profile activity or new follows. Retention unavailable; do not infer precise causal mechanism.
- **Creative course correction:** stop automatically selecting three-plate posters with steam/leaf motion as TikTok Reels. Test (A) true kitchen preparation/packing, (B) real app-screen package explainer, (C) workday lunch problem with authentic footage. Choose **A** only when genuine approved footage exists; else prioritize verified **B**. Only approved foods/logo/rights; no false testimonial or fabricated scene. Content optimization cannot fix an eligibility/privacy restriction if it exists.
- **Posting strategy:** hold delete/reupload/boost of the weak TikTok post pending Studio checks. No publishing/scheduling/spend action authorized. Existing dated plan `plans/2026-10-12-social-content-pilot.md` is a proposal, **not** a committed publish schedule; its initial convenience-Reel direction is suspended pending this incident.
- **Evidence:** incident document plus `data/reports/social/2026-10-12/instagram-last-reel-user-insights.json` and TikTok source rows. No proof exact user-uploaded Flow MP4 equals the published TikTok file; maintain careful media identity separation.

## 2026-10-12 — First-party Instagram insights on latest Reel (more reliable than missing Metricool rows)

- **Current new-content focus:** user provided canonical Instagram post URL `https://www.instagram.com/p/DeXlqySIUxl/` and a *native Instagram View Insights screenshot*. Preserve the screenshot-derived **500 views**, **343 viewers** (screen calls these `المشاهدون`, not explicitly 'reach'), **56% of views from nonfollowers**, **44% followers**, **3 interactions** (2 likes, 1 share, 0 comments, 0 saves), **2 engaged accounts**, **0 follows / 0 profile activity**, and **96 separately reported Facebook views** (0 Facebook engagement). Recorded verbatim with source limitations in `data/reports/social/2026-10-12/instagram-last-reel-user-insights.json`.
- **Diagnosis:** Instagram provided distribution beyond the followers, but engagement and subsequent profile action are small. Retention/watch time unavailable. The 3/500 = 0.6% is a descriptive interaction-per-view ratio, **not** Meta's official engagement rate. Do not claim account shadowban or that a first-second hook is proven the cause.
- **TikTok latest:** Metricool returned just **2 views**, 0 reactions and a conflicting/non-comparable reach reading for the 8-sec Oct 11 post `https://www.tiktok.com/@basicdiet.sa/video/7695519331622456596`. Check TikTok Studio's public visibility, For You eligibility and actual native video insights before any deletion/reupload; avoid guessing about algorithm or account restrictions.
- **Important source distinction:** Metricool Instagram is OAuth-connected but historical per-post API queries are empty. First-party screenshot is **valid evidence for that single reel**, not proof of broader account trends. User explicitly wants focus on *their newly posted content*, not September TikTok promotional videos. Next analysis should focus on this Instagram Reel and the October TikTok video, documenting new 24h/72h/7d results.
- **Next creative iteration:** test actual unaltered food footage with a compelling first 1–2s visual, short Saudi copy, a clear relevant CTA and correct logo; compare matched post snapshots, not aggregate reach from overlapping date windows.
- No verified Instagram-to-paid conversions or posting authorization was produced by this screenshot review.

## 2026-10-12 — Instagram newly connected; social analysis refreshed

- **Live Metricool account `basicdiet.sa` verified:** both `instagramData` and `tiktokData` exist for brand `7299230`. TikTok analytics is readable, but Instagram evolution returned a zero-like aggregate and Instagram posts, Reels, Stories, countries, cities and age/gender datasets returned **no historical rows**, so **do not report Instagram followers/views/reach as 0**. Facebook network remains absent. Metricool syncs daily; recheck Instagram after the next overnight import, preserving connection method if troubleshooting.
- **Latest dated sanitized evidence:** `data/reports/social/2026-10-12/instagram-tiktok-metricool.json` (Metricool direct read). TikTok showed five dated videos from Sep 1–Oct 11, 2026 with 76,748 cumulative post views *as of the read*, 4.9s average watch time in provider summary and 78.7% Saudi follower share. A new 8-second video posted Oct 11 exists with an actual TikTok canonical URL in that report. The *visual* identity of that TikTok upload was not matched to the user's in-chat Google Flow MP4. Do not auto-merge that post into creative record `BD-20261012-001` or infer advertising origin.
- **Commerce bridge:** signed production backend report `data/reports/commerce/2026-10-08/30d.json` covers Sep 9–Oct 8: 157 registrations, 65 app paid transactions and 43 first-time paid subscribers. The 26-day, 150g, two-meal plan accounts for 21 app transactions (about 32%). These are not attributable to social content and should not be treated as current-day KPIs.
- **Actionable organic experiment:** `plans/2026-10-12-social-content-pilot.md` describes 12–18 Oct content mix, a next convenience-style Reel distinct from the recently posted three-meal poll, factual/rights gates and 24h/7d diagnostics. Test post times around 10:00 and 18:00 Riyadh as modeled hypotheses. No social posts were scheduled, generated, approved, or published by this analytics run; no campaign spend.
- **Priority:** publish only approved original visual assets; wait for Instagram ingestion and compare platform-specific performance before naming 'winners'. Continue to record confirmed canonical posts and source-to-first-paid measurement separately. Older sections below saying Instagram not connected are historical and **superseded** by this block.

## 2026-10-12 — new user-produced three-meal living-poster Reel (supersedes older 'no generated video' note)

- **Creative created in chat on 2026-10-11:** user selected a cream/green/orange branded three-meal poster featuring butter chicken, steak and Alfredo pasta with the hook **«وش تختار اليوم؟»**, then supplied an **8-second 720×1280 Google Flow-generated MP4** with gentle food steam/leaf motion. The user wants the **concept + actual video existence** remembered by the agent.
- **Durable canonical brief and exact media fingerprint:** `content/production/2026-10-12-living-poster-steam-leaves.md` (record `BD-20261012-001`). It contains sources, SHA-256 of the user-uploaded MP4, caption, full Flow prompt, negative constraints, learnings, review/publishing blockers.
- **Design preference now explicit:** animate existing steam and gently swaying green leaves only; leaves **stay in place**, and the **entire original poster always stays fully framed**. No zoom, reframing, cropping, new elements, color change, altered Arabic, changed logo or resynthesized food. Reject Flow frames that violate the source image.
- **Truth labels:** source photo inspection is AI-only, official logo/menu/usage rights are not human-approved. The AI-generated poster may deviate from true meal pixels. The video was user-produced and uploaded in conversation; **there is no durable cloud video URL and no verified Instagram/TikTok publication URL**. No post was added to the publication ledger and no performance was invented. Structured creative status remains `CONCEPT_DRAFT` until approval gates are satisfied.
- **TikTok:** Metricool has been connected for read-only analytics, but this does not grant permission to post; Instagram/Meta connectivity was not confirmed. After actual publication, verify canonical links and seven-day results. Prior 2026-10-09 statements denying newly produced media are historical and are superseded by this section.

**TikTok connected via Metricool (2026-10-09):** Verified brand @basicdiet.sa with TikTok analytics and last 90-day published video data; 361 followers reported at 8 Oct; three videos published during the latest 30 days total 76,000 cumulative post views. See `docs/TIKTOK_INSIGHTS_2026-10-09.md`. Instagram/Facebook not connected; social-to-paid attribution and posting approval missing. The previous statements about no connected social networks in historical sections are superseded by this update.

**Current as checked 2026-10-09:** Phase 4 read-only signed commercial sync succeeded for 2026-10-08 (report captured 2026-10-09). AI-in-chat is the creative engine; no independent autonomous creative model or social-account connector is deployed. See latest CI workflow for current test count; older counts later in this file are historical, **not current totals**.

**Static image skill and brand consistency (2026-10-09):** New native `basic-diet-image-creative` skill, own-asset visual design system, static/carousel/Story playbook and candidate identity data. Two existing Basic Diet design references were visually reviewed; competitor Instagram grid unavailable, only site promo art/third-party Reel index seen. Palette/logo/font are NOT owner-approved. No social account connected, and no new visual published.

**P1 pilot:** A logo variant and one menu photo were visually inspected via the authenticated Drive connector. Their usage rights and current menu verification remain pending. One original creative draft is prepared in content/production/ (not approved, generated, posted or measured). No real publication evidence or 7-day performance was created.


## 2026-10-09 — implemented AI-first creative protocol (with P1 quality improvements)

- The canonical original-content workflow is docs/CREATIVE_AGENT_PROTOCOL.md plus .agents/workflows/ai-creative-production.md, gated in AGENTS.md and the native skill. It instructs a supervising capable AI to generate and evaluate distinct creative options; it does not transform deterministic Python into autonomous model workers.
- Authenticated Google Drive folder listing found the Basic Diet materials child 1ZplIhzIZKcK5ZCoe454exU445cL-Vhz-, logo variants, a 49-entry New meal-photo folder, three direct MP4s and existing social designs. Exact selected IDs are indexed in assets/drive-source-index.json. **Filename/ID access only; visual quality, logo approval, up-to-date menu and legal rights are not verified.**
- Video prompt guidance: docs/GOOGLE_FLOW_PRODUCTION.md (used after installed video skill; detailed storyboard skill only for explicit requests). No video was generated, no social accounts connected, and no campaign changes performed. Short entry is docs/BOOT.md; source status and pilot follow knowledge/brand-visual-review.md and content/production/.
- Next: visually inspect/approve the real Drive source files and brand marks, choose one AI-originated creative pilot, verify its claims and official CTA, then review before any production or publication.

## Business and evidence

Basic Diet is a Saudi meal-subscription restaurant. North star: first-time **paid** subscribers → retention/repeat → profitable revenue. Historical positioning: **الطعم، الاختيار، الراحة**; familiar food, portion choice and convenience. Audience segments are hypotheses. The 7/26/30-day plans, portions, menu, prices, promos and Jeddah coverage are 2026-10-07 historical context, requiring fresh official verification before claims. See `knowledge/` and `docs/SOURCE_MAP.md`.

## Verified implementation

- Historical migration: 23 archive originals retain source blob hashes; 20 mapped working paths exist and still match their initial bytes at audit time. Working knowledge can evolve; archive content cannot.
- 13 vendor skills + 67 references, MIT license and static creative template retain pinned upstream hashes. Native Basic Diet and storyboard entry points make 15 skills. Original user storyboard text is preserved and never auto-activates.
- Daily CLI: versioned JSON ideas/publications/reservations/performance, lossless 30-idea migration, 30 editorial adaptations, source hashes, structured six-role handoffs and offline Arabic briefs.
- Normal local runs reserve ideas; `--dry-run` and Actions produce drafts without reservation. Output is ignored by Git; reviewed ledger changes must be committed for future sessions.
- Optional AI: one bounded explicit request, separate unverified output, safe failure status; no paid request executed in this audit.
- Validation and 44 unit/integration tests passed locally during the audit. Final evidence and any remote CI result belong in `docs/AUDIT_2026-10-08.md` / the PR checks, not an assumed deployment claim.

## Current operating records

- Ideas: `content/ideas/backlog.json`; original Markdown preserved.
- Editorial scripts: `content/ideas/creative.json`; proposals, not approved product facts.
- Reservations: `content/drafts/runs.json` (empty at audit; realistic test used `--dry-run`).
- Publications: `content/published/publications.json` (empty); legacy Markdown template still consulted.
- Performance: `data/analytics/creative-performance.json` (empty); no measured creative winners.
- Adopted architecture: `decisions/log.md`; contracts/recovery: `docs/DATA_CONTRACTS.md`.

## Dry-run outcome

The realistic offline Instagram run selected **C003**, awareness: **«إذا قلت أكل دايت… وش أول طبق يجي في بالك؟»**. It produced a 15-second Reel plan, Saudi Arabic caption, three Stories, audience/funnel, Reach as a diagnostic KPI and explicit review gates. No exact media file, current menu, destination link or rights were verified. Paid suitability remains NOT_READY. No publication, reservation, message, asset generation or advertising action occurred.

## Phase 4 measurement intake — implemented 2026-10-08

- Existing backend analytics contract inspected: admin-only `GET /api/dashboard/accounting/marketing-analytics`, Riyadh calendar-day reporting, count/rate/revenue metrics returned as aggregates.
- Added `scripts/marketing_baseline.py` and `tests/test_marketing_baseline.py`: safe import of three period reports or explicit authenticated read-only GETs, with strict exact period and currency checks.
- Outputs contain only selected aggregate KPIs and provenance, **not** raw response arrays, customer data, bearer tokens or invented values.
- Outputs stay ignored locally until independently reviewed and explicitly documented as source-verified.
- The offline importer remains available. A separate signed OIDC workflow now retrieves official aggregated 30/60/90-day reports without a dashboard token; successful production evidence in `data/reports/commerce/2026-10-07/VERIFICATION.md`.

## Asset discovery status — 2026-10-08

- Authenticated Drive browse located C003 candidate images with exact file IDs under `صور الوجبات / New` (butter chicken, steak meal, Alfredo pasta). Index: `assets/c003-asset-candidates.md`.
- File metadata access confirmed; image content, current menu eligibility and commercial reuse rights are **not yet verified**.
- Drive metadata reports `anyone: writer` on these assets; owner should review permissions before relying on them for approved campaigns. No permissions changed.
- Metricool brand connector currently has no social network connected, so platform publication history cannot yet be corroborated there.

## Blockers and next actions

0. Owner to approve final logo variant and usage rights; recheck named dish in current menu. Review prepared pilot and verify publishing destination before generation or posting.
1. Verify recent actual social history and an exact approved media file/rights for the first reviewed idea; populate publication records only from real evidence.
2. Commercial 30/60/90-day baseline is now available under `data/reports/commerce/2026-10-07/`. Use and compare it with official dashboard records; verify next scheduled run before claiming recurring updates are proven.
3. Reconcile source-to-first-paid attribution. Install/first-open counts, CAC and ROAS are not established here; historical backend capability claims were not reverified.
4. Run a small human-approved organic pilot, capture URLs and seven-day measurements, then adjust creative hypotheses. Posting itself still requires explicit action authorization.

Only the signed commercial read-only data integration is active; no autonomous LLM workers, social account posting, public publishing or paid ad campaigns are deployed. Existing user authorization governs requested local coding/review work; root `AGENTS.md` owns permissions and precedence.

## Signed agent / dashboard bridge (live commercial data enabled)

- Backend PR #143 was merged and the authenticated GET-only marketing reporting endpoint is active with GitHub Actions OIDC.
- Marketing OS workflow `sync-commerce.yml` and `scripts/sync_commerce.py` wrote three aggregate-only daily snapshots for 2026-10-07 to the private repository after successful end-to-end production authentication.
- Backend Railway service contains the enabled `MARKETING_AGENT_OIDC_ENABLED` configuration, and its deployment is successful; no dashboard admin token was shared.
- Verified production OIDC roundtrip: [GitHub Actions run #37805596216, attempt 2](https://github.com/IbrahimMohamed101/basicdiet-marketing-os/actions/runs/37805596216) succeeded, and the three snapshots plus a verification note are committed.
- Social account status: Metricool connection inspection found no connected network. Instagram/Facebook OAuth authorization still needs account owner action.
- Data source and operator runbook: docs/LIVE_AGENT_CONNECTOR.md.

## Live connector verification — 2026-10-08

- Backend GitHub PR #143 merged, production Railway basicdiet145 deployment marked SUCCESS; dedicated OIDC contract test succeeded.
- Marketing OS PR #3 merged; 65 tests passed on the branch and main quality CI is green.
- Initial signed sync GitHub Actions run #37805596216 attempt 1 failed while Railway flag was disabled; **attempt 2 succeeded** after the user enabled the variable. The three 2026-10-07 snapshots are present.
- Backend production Railway variable `MARKETING_AGENT_OIDC_ENABLED` is now present, and the Railway production deployment completed successfully.
- Verified: the workflow wrote `data/reports/commerce/2026-10-07/{30d,60d,90d}.json`. Integrity details and limitations: `data/reports/commerce/2026-10-07/VERIFICATION.md`. Next scheduled day's automation has not run yet.
- Instagram/Facebook OAuth is not connected; do not infer social metrics from the backend commercial totals.
