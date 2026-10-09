---
schema_version: 2
record_id: "BD-YYYYMMDD-001"
date: "YYYY-MM-DD"
status: "CONCEPT_DRAFT"
platform: "instagram"
format: "Reel"
concepts:
  - angle: "food_desire"
    hook: "Describe the real hook"
    visual: "Specific scene mechanism"
    asset_ids: []
    feasible_now: false
    rejected_reason: "No specific verified asset selected"
    score_breakdown: {brand_fit: 1, hook: 1, asset_fit: 1, execution: 1}
  - angle: "convenience"
    hook: "Different hook B"
    visual: "Different mechanic B"
    asset_ids: []
    feasible_now: false
    rejected_reason: "No source asset"
    score_breakdown: {brand_fit: 1, hook: 1, asset_fit: 1, execution: 1}
  - angle: "choice"
    hook: "Different hook C"
    visual: "Different mechanic C"
    asset_ids: []
    feasible_now: false
    rejected_reason: "No source asset"
    score_breakdown: {brand_fit: 1, hook: 1, asset_fit: 1, execution: 1}
selected_angle: "food_desire"
selection_reason: "Use a reason after evaluating viability and score breakdown."
asset_ids: []
copy:
  caption: "Write original Saudi Arabic caption"
  on_design_text: "Arabic overlay separate from AI image/video"
  cta: "Actual verified CTA"
  stories: ["One real story", "Another real story"]
primary_kpi:
  name: "first_time_paid_attributed"
  threshold: null
  baseline: null
  window_days: 7
  measurement_source: "No verified attribution or connected platform."
  source_status: "disconnected"
  evidence: null
approvals: []
generated_asset_url: null
publication: null
---

# Human-facing creative production notes

This template is ignored by the validator and does not constitute an approved or measured campaign.

- Distinguish draft feasibility (assets available to make a draft) from publication readiness (owner-approved rights, menu, logo/brand and measurement).
- Human approval only counts as a documented external owner action and a reviewed commit/PR, never as a model-written name in a field.
- YAML alone **cannot authenticate** human identity; enable branch rules requiring CODEOWNERS approval and restrict GitHub direct-write access.
- For a draft with unavailable measurement, leave KPI baseline/threshold null. READY or later requires an actual connected/verifiable source, non-null baseline and measurable threshold.
- Keep exact selected image IDs, actual visual and menu evidence, source period, any paid code restrictions, editable caption, Stories, video prompt and constraints in body.
- Publication logs require real canonical platform URL; never write a fake result just to pass CI.
