# Basic Diet — 5-stage daily creative pipeline

## Purpose and authority

Daily **review-only** social creative pipeline, Asia/Riyadh timezone. User-authorized: research, critique, revise, produce visual drafts if a supported tool is actually available, review them, and document outputs. **NOT authorized:** publishing or scheduling social posts, buying ads, editing actual customer data, changing prices/offers, or falsely claiming brand/menu/asset approval.

This document is an execution contract for scheduled ChatGPT tasks, **not proof that connectors or image generation are usable in the scheduled runtime**. Each run must explicitly report the truth. Source of truth: `AGENTS.md`, current `STATE.md`, `.agents/skills/basic-diet-marketing/SKILL.md`, `.agents/skills/basic-diet-image-creative/SKILL.md`, `docs/CREATIVE_AGENT_PROTOCOL.md`, `docs/BRAND_VISUAL_SYSTEM.md`, original Google Drive files and accepted/rejected `plans/` entries. Actual publication is proved only by a real platform URL, not by a concept/brief, scheduled task, or repost intention.

## Run identity / durable handoff

- Compute **today's date in Asia/Riyadh** (`YYYY-MM-DD`) at each execution.
- The single shared handoff directory for that date is `automation/daily/YYYY-MM-DD/`.
- For each stage, **read all predecessor stage files that exist for exactly that day**. Never substitute old-day results when today's predecessor is absent or failed.
- Stage outputs are short complete Markdown files on GitHub, one per date, with one of these exact filenames:
  1. `01-ideas.md`
  2. `02-critique.md`
  3. `03-approved-brief.md` (this means approved for automated draft production ONLY, not owner-approved)
  4. `04-draft-images.md`
  5. `05-final-review.md`
- Header of each file: `date`, `stage`, `status=COMPLETED|BLOCKED|NEEDS_USER_REVIEW|READY_FOR_USER_REVIEW`, `source_refs`, `predecessor_refs`, `generated_at_riyadh`, `next_action` with timestamps or links. Add factual outputs below.
- Do not overwrite good evidence with conjecture. If the GitHub connector cannot write, clearly report the stage text and the error; **later stages must not claim the handoff was saved**.
- Every stage shall state whether connected Drive, GitHub, image tools and latest social data were actually available in that run.

## Stages

1. **04:00 Riyadh — Research/selection.** Inspect state, existing and rejected concepts, publications (verify whether posts are actually published vs only discussed), pending drafts and genuine image/video sources. Select one primary new idea and two backups (not a repeated recent post); include ID, audience, goal, source media IDs, factual/rights gaps, rationale. Save `01-ideas.md`.
2. **05:30 — Critical review.** Only proceed if today's `01-ideas.md` is `COMPLETED`. Critically score 3 concepts for originality, actual source availability, Saudi relevance, claim truth and plausibility; find weaknesses and choose strongest, not merely echo previous praise. Save `02-critique.md`.
3. **07:00 — Art direction revision.** Only proceed if today's 1 and 2 are complete. Apply the criticisms and previous user rejections, especially C034 meeting-poster rejection; design 4:5 static production brief with source-specific stills, realistic layout, short Arabic type, one CTA, strict rejection gates, and caption. Save `03-approved-brief.md`. No fake product, app UI, reviews, labels or sponsorship.
4. **08:30 — Production.** Only proceed if today's `03-approved-brief.md` completed. Use live authentic Drive media as source. If the scheduled runtime has an image-generation/editing/compositing tool, produce **up to two** substantially different 1080x1350 visual draft(s), inspect actual image pixels, and save stable accessible media links or authorized Drive uploads; record actual dimensions and links in `04-draft-images.md`. Never use fake generated restaurant logo/food/packaging as authentic. If unavailable or if outputs cannot persist, mark **BLOCKED**, state exactly what failed, and provide a truthful production-ready asset assembly plan instead of fabricated image links. Do not spend on a separate paid image API without budget approval.
5. **10:00 — Image critique/final candidate.** Only proceed if today's 4 exists with actual inspectable images. Inspect rendered pixels visually (not prompt descriptions). Score product/logo/source fidelity, legible Arabic, mobile hierarchy, aesthetics, composition, clarity, claim accuracy and CTA out of 10. Hard reject any invented product/logo, fake app UI, unsupported material claim, or broken Arabic. Select best and repair with supported tools if available, up to **two** fixes, then re-check actual result; include a stable image link and short Saudi caption. If score <8.5/10 or critical gate unmet, status `NEEDS_USER_REVIEW` or `BLOCKED`, never invent a publish-ready claim. Use `READY_FOR_USER_REVIEW` status only if actual image inspection scores at least 8.5/10 without hard blockers, otherwise `NEEDS_USER_REVIEW` or `BLOCKED`. Save `05-final-review.md`. No social upload.

## General safeguards

- Each stage may run without its predecessor: **STOP / BLOCKED** rather than reconstruct or assume the missing stage completed.
- 90 minutes is spacing between **scheduled start times**, not a guaranteed runtime duration, service level or completion deadline. The next stage must check file status even if the schedule time has passed.
- Assets from project chat attachments are not reliably accessible from scheduled tasks. Retrieve original media through authenticated **Google Drive** or persisted authorized links; never assume a sandbox link survives.
- Labels and authentic logo must be copied faithfully; use native source pixels and typeset Arabic separately with RTL support. If a desired branded packaging type is conceptual, call it concept art, not real current packaging.
- Respect plan/tool limits, permissions, source rights and financial approvals; no posting, marketing spend or customer data exports without explicit permission.
- Notify the user of stage result or blocker, with direct links to the real handoff file and produced media when available; avoid false success language.

