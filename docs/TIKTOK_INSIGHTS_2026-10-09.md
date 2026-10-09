# Connected TikTok analytics — Basic Diet — 2026-10-09

**Status: authenticated Metricool read-only access confirmed.** Account: [@basicdiet.sa](https://www.tiktok.com/@basicdiet.sa). Brand ID 7299230. Metricool account timezone Africa/Cairo. The audience and reach are TikTok metrics, not new paid subscriptions or all-channel revenue.

## Key reported observations

- **Follower count:** 361 (Metricool evolution last explicit observation 2026-10-08).
- **TikTok posts published in the selected 30-day window (9 Sep–9 Oct):** 3 videos, **76,000** accumulated video views at query time, **249** likes, **6** comments, **21** shares. Note: video-specific views may be lifetime accumulated, not views *generated* inside the selected window.
- **90-day query 11 Jul–9 Oct:** 4 published videos, **76,662** summed reported views. The previous post was 1 September, then 17/20/23 September; **no video after 23 Sep surfaced** in the provider results.
- **TikTok follower mix:** Saudi Arabia about **78.87%**, male 63%, female 37%; this describes followers, **not** viewer or paying-customer makeup.
- **Source of video impressions:** For You 96.54%, personal profile 1.12%, search 0.15% in Metricool's distribution. The account reaches outside its known followers, but the platform's denominator requires cautious comparison.
- **Reported average watch time:** about 4.89 sec versus average video length about 24.67 sec (provider summary, not a full-video-completion probability). Improving first 1–3 sec is a testable hypothesis.
- **Best-time heatmap:** strongest modeled windows include 10:00 and 18:00 (Metricool brand timezone Africa/Cairo = Riyadh UTC+03 on query date). Use as **test hypotheses**, not proven posting times.
- **Metricool planner:** no posts scheduled for Oct 2026 at fetch time. This is not proof of no independently scheduled TikTok posts elsewhere.

## Actual four published videos (URLs verified from TikTok provider)

| Date | Content topic per source caption | Video length | Views | Likes | Comments | Shares |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2026-09-01 | Generic subscription CTA | 18s | 662 | 15 | 3 | 1 |
| 2026-09-17 | Saudi National Day promotion | 26s | **53,580** | 130 | 5 | 15 |
| 2026-09-20 | Taste/convenience and KSA96 | 34s | **22,120** | 113 | 1 | 5 |
| 2026-09-23 | National Day offer with a deadline now past | 14s | **300** | 6 | 0 | 1 |

Full canonical post URLs and per-video measurements in `data/reports/social/2026-10-09/tiktok-metricool.json`. We observed captions and metrics, **not the actual full video visuals**. Don't describe their exact opening frames/audio/cuts or infer why a video got 53K versus 300. We also have **no data on paid boosts or content-specific paid subscriptions**.

## What the chat AI Creative Engine should do differently now

1. **Weekly vertical video pilot:** evaluate 3 separate concepts before production; make one 12–20 sec (working test range, not a fixed algorithm truth) video showing actual dishes/real service, with visually gripping 0–2 sec, one clear audience problem and short Saudi CTA. Keep Basic Diet identity consistent. Use the native video/Google Flow rules and real Drive sources; never fabricate food or health outcomes.
2. **Content contrast:** test `food_appetite` versus `choice/convenience` versus `offer` **only when current terms are verified**. The high-view September videos are promotional, but the data does not establish the discount *caused* those views.
3. **Retention diagnostics:** compare average seconds watched, shares per 1,000 views, and qualified comments per 1,000 views for matched organic videos. Never call views or shares a paid-customer KPI. Avoid treating TikTok's weak/unreliable completion-rate API fields as verified without independent review.
4. **Publish-time experiment:** alternate approximately 10:00 versus 18:00 Riyadh for similar creative styles and measure post-period after controlling for age and external boosts. Heatmap is not proof.
5. **Commerce bridge:** use labelled `creative_id` and source tags for dashboard-assisted subscription creation only after separately approved backend/privacy changes; build verified content-to-first-time-paid event joins before ROAS or CAC claims.
6. **Social expansion:** TikTok is now connected. Instagram/Facebook are not confirmed connected in the latest Metricool brand settings; no automatic publishing/spend authorization.

## Honest limits

Only **4** source posts surfaced within the 90-day published-post interval, so individual viral examples do not define repeatable winners. Follower geography must not be applied to the 76K video viewers. The observed averages are provider outputs, not reproducible first-three-second retention curves. Don't reuse any National Day offer from Sept as if still current.

## Next action

Choose two short-form video briefs using authentic Drive food and one non-video Instagram creative. Wait for owner rights/current-menu validation before publishing. Re-check posts and audience metrics after the first new upload, record canonical URLs + 7-day actual performance, and only then update `content/winners.md`.
