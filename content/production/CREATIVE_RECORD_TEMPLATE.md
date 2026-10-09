---
schema_version: 1
record_id: "BD-YYYYMMDD-001"
date: "YYYY-MM-DD"
status: "CONCEPT_DRAFT"
platform: "instagram"
format: "Reel"
concepts:
  - angle: "food_desire"
    hook: "Insert original hook A"
    visual: "Specific visual mechanism A"
    score: 4
  - angle: "convenience"
    hook: "Insert original hook B"
    visual: "Distinct visual mechanism B"
    score: 3
  - angle: "choice"
    hook: "Insert original hook C"
    visual: "Distinct visual mechanism C"
    score: 3
selected_angle: "food_desire"
selection_reason: "Explain evidence, specificity and feasibility. Scores are editorial judgement, not measured impact."
asset_ids: []
primary_kpi:
  name: "reach"
  threshold: 200
  window_days: 7
  measurement_source: "Instagram Insights, when connected"
approvals: []
generated_asset_url: null
publication: null
---

# Creative — replace with actual subject

**This is a template, not an active creative.** The validation scanner ignores this file. Replace all placeholders before creating a dated creative Markdown file in \`content/production/\`.

## Evidence and audience
- Audience/hypothesis:
- Source and as-of date:
- Current menu, asset visual quality and rights independently checked:

## Selected creative
- Hook:
- Scene-by-scene visual/shot plan:
- Saudi Arabic caption:
- CTA and destination verification:
- Stories:
- Paste-ready image prompt + negatives:
- Google Flow/video prompt + negatives if video:
- Fallback using original food image:

## Readiness and results
- Verification blockers:
- Human owner approval evidence (if any):
- Generated artifact (only if real):
- Publication URL (only if verified):
- Performance (only when real and measured):
- Next action:

The YAML frontmatter is machine-validated against \`schemas/creative-record.schema.json\` plus semantic rules in \`scripts/validate_creative.py\`. Allowed statuses: CONCEPT_DRAFT → NEEDS_ASSET_VISUAL_REVIEW → READY_FOR_HUMAN_APPROVAL → APPROVED_BY_OWNER → PRODUCED → PUBLISHED_VERIFIED. A record cannot jump ahead without the required evidence; a YAML claim alone never independently proves approval or publication.
