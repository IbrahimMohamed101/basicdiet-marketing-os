# AI Creative Production — mandatory guided workflow

**Trigger:** user asks to think up or produce Basic Diet content: caption, hook, product photo creative, designed post, Reel, Google Flow prompt, carousel, story, creative test or ad creative.

**This workflow belongs to a supervising AI assistant.** It is not executed automatically by Python, GitHub Actions or six independent agents.

1. Read AGENTS.md → STATE.md → .agents/skills/basic-diet-marketing/SKILL.md → docs/CREATIVE_AGENT_PROTOCOL.md.
2. Read .agents/skills/README.md and the task-mandatory skill files. For any post: content-strategy + social. For image: ad-creative. For video: video + docs/GOOGLE_FLOW_PRODUCTION.md. For detailed boards, storyboard-to-video only when explicitly requested. Paid creative adds ads + attribution.
3. Ground in the exact Drive file IDs from assets/drive-source-index.json and fresh relevant business records, current menu/claim checks, actual platform history when available and the audience hypothesis.
4. Create three distinct ideas **using AI reasoning**. Do not copy the deterministic scripts/daily_brief.py output as the final creative. Select one with a short, transparent rationale.
5. Deliver the source-backed creative package (hook, visuals, Saudi caption, Stories, CTA, image/video prompts, negatives, source links, KPI, checks). Prefer authenticity and visual retention of real product assets.
6. Do not publish, buy ads, contact customers, alter permissions or run billable generation just because this workflow was read. Explicitly authorized actions only.
7. If approved for tracking, create content/production/<date>-<slug>.md following content/production/CREATIVE_RECORD_TEMPLATE.md. Log only real approvals, actual media outputs and actual platform results; use existing dedicated records for actual publications and performance.
8. Validate and test modified code/contracts; report actual outcomes, blockers and next step.

Daily deterministic pilot remains available at scripts/daily_brief.py --dry-run; its curated templates are **not** the creative director.
