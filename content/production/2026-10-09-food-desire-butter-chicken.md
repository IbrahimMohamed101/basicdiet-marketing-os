---
schema_version: 2
record_id: "BD-20261009-001"
date: "2026-10-09"
status: "CONCEPT_DRAFT"
platform: "instagram"
format: "Reel"
concepts:
  - angle: "food_desire"
    hook: "وش رايك نبدأ بالغدا قبل الكلام عن الدايت؟"
    visual: "Macro push-in across the real chicken-and-rice photograph"
    asset_ids: ["1H2InhiMdECMrs8bsf6L_h9yM-rOfYqw6"]
    feasible_now: true
    rejected_reason: null
    score_breakdown: {brand_fit: 4, hook: 4, asset_fit: 5, execution: 5}
  - angle: "convenience"
    hook: "يومك زحمة؟ شوف وجبتك قبل ما تبدأ الدوام."
    visual: "Simple workday clock graphics around the same original photographed plate"
    asset_ids: ["1H2InhiMdECMrs8bsf6L_h9yM-rOfYqw6"]
    feasible_now: true
    rejected_reason: null
    score_breakdown: {brand_fit: 4, hook: 3, asset_fit: 4, execution: 4}
  - angle: "choice"
    hook: "يوم رز، ويوم تختار اللي يشهيك."
    visual: "Split frame contrasting a second dish with the current photographed plate"
    asset_ids: ["1H2InhiMdECMrs8bsf6L_h9yM-rOfYqw6"]
    feasible_now: false
    rejected_reason: "Needs an inspected second dish image; no verified matching second photo yet."
    score_breakdown: {brand_fit: 4, hook: 3, asset_fit: 1, execution: 2}
selected_angle: "food_desire"
selection_reason: "Chosen angle is feasible as a draft today with one visually inspected actual image; its buyer appeal is a hypothesis, not tested results."
asset_ids: ["1H2InhiMdECMrs8bsf6L_h9yM-rOfYqw6"]
brand_logo_asset_id: null
copy:
  caption: "أحيانًا صورة الوجبة تخلّيك تقرر أسرع من الكلام. وش أول شيء شدّك في الطبق؟ شوف خيارات بيسك دايت من القناة الرسمية. #بيسك_دايت"
  on_design_text: "وش رايك نبدأ بالغدا؟"
  cta: "تصفّح المنيو"
  stories: ["تبدأ من الرز ولا الدجاج؟", "تحب تشوف خيارات غدا أكثر؟", "شوف المنيو من الرابط الرسمي بعد التحقق"]
primary_kpi:
  name: "first_time_paid_attributed"
  threshold: null
  baseline: null
  window_days: 7
  measurement_source: "Source-to-paid tracking unavailable; requires platform connection and attribution implementation."
  source_status: "disconnected"
  evidence: null
approvals: []
generated_asset_url: null
publication: null
---

# First creative pilot — photograph-led Instagram Reel (draft only)

**Objective:** Awareness that can feed first paid subscriptions, not established purchase attribution. **Audience hypothesis:** prospective customer who expects repetitive diet food; not confirmed from live customer research.

**Actual source:** Google Drive `دجاج بالزبدة.png` (ID above); inspected as pixels 2026-10-09 and documented in `knowledge/brand-visual-review.md`. Black plate, white rice, orange/golden pieces on white; **current dish availability and commercial usage permission not verified**.

**Opening 0–2s:** Slow close-up of real chicken/rice; on-screen Arabic text added by editor: **"وش رايك نبدأ بالغدا؟"**

**2–6s:** Gentle 2D crop/reveal from plate left to rice right. No fabricated hands, packaging or serving footage. **6–9s:** Return to full real photograph, leave negative space at top. Overlay separately: **"شوف وجبات بيسك دايت"**. **9–11s:** Approved logo after owner chooses final version, CTA separately typeset **"تصفّح المنيو"**. The current landing destination must be checked before publication.

**Saudi caption draft:**

> أحيانًا صورة الوجبة تخلّيك تقرر أسرع من الكلام.
> وش أول شيء شدّك في الطبق؟
>
> شوف خيارات بيسك دايت من القناة الرسمية.
> #بيسك_دايت

**Story 1:** "تبدأ من الرز ولا الدجاج؟" Poll. **Story 2:** crop of same approved photo; "تحب تشوف خيارات غدا أكثر؟". **Story 3:** link to currently confirmed official menu after verification.

**Google Flow image-to-video prompt (only if user elects to generate):**

Use the provided real photograph of the Basic Diet plated meal as the exact source frame. Vertical 9:16, 7–9 seconds, premium realistic food photography. Perform a gentle cinematic push-in and subtle stable camera drift from the orange/golden food pieces toward the white rice. Preserve every visible portion, original black plate geometry, bright white background and actual ingredient shapes. Do not invent steam, utensils, hands, packaging, additional food, logos or textual overlays. Do not morph/churn the plate or replace the food; if the model cannot preserve fidelity, keep it a motion-graphics edit of the original still. Leave top negative space for separately typeset Arabic overlay. Soft natural light, true-to-photo color and restrained pace. **Negative:** no AI Arabic lettering, no swapped dishes, no ingredient changes, no fake logo, no plastic texture, no impossible camera move. Overlay all Arabic and official logo in the editor only.

**Fallback (preferred for fidelity):** use a 2.5D slow pan/zoom of the actual static image with manual typography; no generative food alteration.

**Blocked before production/publication:** owner approval of actual logo, asset commercial rights, dish currently on menu, official CTA destination, recent Instagram content review, and authorized posting. No video was generated, no social post scheduled/published, no seven-day metrics collected. Primary KPI is currently unmeasurable and has no target or baseline; it must be connected and defined before a ready-to-publish status.
