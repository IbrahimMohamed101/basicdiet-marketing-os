# Basic Diet — Reliable 5-stage scheduled creative pipeline (v2)

**Date:** 2026-10-13. **Status:** scheduled tasks configured; end-to-end overnight generation and persistent image upload still **unproven**. This protocol increases recoverability but does not provide guaranteed completion, runtime length or image-tool access. User authorizes creation and review of **drafts**, not posting, social scheduling, spending paid external API/credits, customer contact, or commercial rights approval.

## Canonical sources and schedule

Repository: `IbrahimMohamed101/basicdiet-marketing-os`.
Read `AGENTS.md` → `docs/BOOT.md` → current `STATE.md` → native marketing + image-creative skills → needed specific source records. Use actual Google Drive images for real products and logos; never invent logo, meal, label, packaging, app UI or people and imply real Basic Diet products.
All date calculations use **Asia/Riyadh** (not account UI timezone). Run at 04:00, 05:30, 07:00, 08:30 and 10:00 Saudi time, daily. The 90-minute intervals space *starts*, not guaranteed durations or process limits.

Daily handoff path: `automation/daily/YYYY-MM-DD/` (the date each task is executing in Riyadh).
Stage files (in execution order):
1. `01-ideas.md` — selection & asset references.
2. `02-critique.md` — independent editorial criticism, alternatives, choice.
3. `03-approved-brief.md` — production directions; *automation-ready*, never human-approved for publishing.
4. `04-draft-images.md` — **real verified draft image links** and actual dimensions or explicit technical blocker.
5. `05-final-review.md` — pixel-inspected critique, repairs, final *review* link if genuinely available, caption and unresolved permissions.

Every stage file has an unambiguous header:
```text
date: YYYY-MM-DD
stage: 01|02|03|04|05
status: COMPLETED|BLOCKED|NEEDS_USER_REVIEW
run_key: YYYY-MM-DD:0X
source_refs: [actual paths/IDs]
predecessor_refs: [same-day verified stage links]
attempts: 1|2|3
generated_at_riyadh: YYYY-MM-DDTHH:MM:SS+03:00
next_action: ...
```
Status `COMPLETED` requires the actual stage output **and a successful refetch from GitHub**. Image stage requires accessible and visually inspected image files, not descriptions. Never turn a missing/failed predecessor into a fictitious completion.

## Retry + recovery rules (mandatory EACH task)

1. **Idempotency:** Read today's own stage file first. If a complete, valid `COMPLETED` file exists, don't regenerate/call paid services; reuse its URL and report success. If existing file is `BLOCKED`, assess and attempt recovery only if the blocker has changed or was transient.
2. **Bounded retries:** On intermittent GitHub/Drive/asset-reading or saving errors (temporary network/5xx/429/timeout), try **up to 3 total attempts within the same scheduled run**; re-fetch source and detect any previously successful write before retrying. On SHA conflicts reread the latest file and reconcile rather than overwriting another run. Do not spin endlessly. Count attempts and write reason to stage report. No timer/sleep functionality should be assumed.
3. **Dependency self-repair:** Check same-day predecessor status. If missing or invalid, re-fetch up to 3 times. If still absent, **attempt to complete the missing upstream stage(s) in order within THIS run**, only if their source facts/tools are actually available; save and refetch each stage before proceeding. Cap catch-up to the day's five defined stages, never go into previous-day artifacts. If catch-up is impossible, create a `BLOCKED` note for current stage with precise remedy and deliver useful partial results. Never pretend a scheduled run was triggered or has completed.
4. **Write verification:** Use GitHub update_file/create_file with the actual SHA, then **fetch_file** and verify date, stage, status, content and original source links. On transient failure retry within bounds. If write cannot be verified, tell the user it is unsaved; never claim persistence.
5. **External generation safety:** Do not blindly retry image submission or billed jobs on timeout. Outcome may be unknown; inspect returned job ID/status or destination first, and only resubmit if confirmed no generation occurred and user-approved budget permits. Two separate *visual revisions* maximum after successful render; do not conflate design iteration with network retry.
6. **Fallback:** On missing premium generation features/permissions, source rights, actual media, or persistent network failure, prepare the best useful next artifact (strong verified brief, source list, caption and QA checklist), mark `BLOCKED`, and notify clearly instead of inventing image links. **Never bypass critical quality gates** to produce a falsely approved design.
7. **Limit repeated work:** Use stable `run_key`, the exact same-day stage names, and do not create duplicate selected ideas or files when retrying; never infer `PUBLISHED` from draft status.

## Stage-specific deliverables

**1 / 04:00 — Selection.** Cross-check actual publication ledger, accepted and rejected visual feedback, current source asset metadata vs inspected pixels, menu availability. Select 1 primary *new* idea and 2 backups, distinct from recently published and C034 rejected treatment, with ID, objective, authentic asset IDs, blockers, expected audience. Persist `01-ideas.md`.

**2 / 05:30 — Critique.** Read verified Stage 1 (or backfill) and challenge all three ideas. Score originality, brand truth, real asset quality, audience relevance, caption hook and practicality. Choose 1 winner, 1 fallback and precise changes. Persist `02-critique.md`.

**3 / 07:00 — Revised art direction.** Read verified Stages 1–2 (or backfill). Convert criticism into final **production brief**, NOT a publicly approved post: exact real Drive photo/logo/label IDs and status, 1080×1350 layout, textual overlay with proper Saudi Arabic RTL, hook, short caption, CTA, explicit negative constraints (no invented food or branding), what visual inspection must confirm. Persist `03-approved-brief.md`.

**4 / 08:30 — Image creation.** Read verified Stages 1–3 (or backfill). Check what native image editing/compositing tools actually exist **in this scheduled run** and whether persistent authorized Google Drive/GitHub upload is possible. Produce up to 2 truly distinct 4:5 draft images from original brand assets, not fabricated product identities. If files created, verify size, visually review pixels, ensure durable URLs (not ephemeral sandbox paths), and persist `04-draft-images.md` with those accessible links. If image tools not available, optionally inspect an existing connected image-generation provider **but do not spend paid credits or buy an API** without separate approval; do not claim that provider is available just because it is listed. Otherwise mark `BLOCKED` and provide exact composition recipe/source IDs.

**5 / 10:00 — Visual QA / correction.** Read verified Stages 1–4 (or backfill) and **actually open each real image**. Score /10 for originality, photographed-food fidelity, exact logo/label, accurate claims, RTL type legibility on phone, composition and CTA. Reject automatically on fake logo/meal/label, counterfeit app screens, invented promotional claim or broken Arabic. Choose strongest, correct up to **2** times if editing is really supported, reinspect pixels, and persist `05-final-review.md` with final real image URL + caption + detailed QA. Require overall >=8.5/10 and no critical failures for `NEEDS_USER_REVIEW`; note remaining human rights/menu approvals. If no qualifying image, mark `BLOCKED` and attach diagnosis rather than claim final output.

## Reliability limitations and user notification

- ChatGPT Tasks do not guarantee other separate tasks finished on time; catch-up only works if the scheduled runner has enough runtime and tool access. These prompts **do not install a persistent background worker or queue**.
- Stage 4 & 5 cannot promise a created image until *actual tool access*, real asset processing and durable upload are verified during a run. A text prompt is not a completed visual.
- No formal fixed-duration sleep or future rerun within the same day is available to these 5 schedules; bounded retry happens **within the task execution**. On hard failure record and report a blocker. A sixth scheduled watchdog is not installed.
- Check task notifications in ChatGPT Settings: currently notifications were observed **disabled**; only the user can enable push/email in the UI.
- Report one completed daily review with real links or accurate BLOCKED details; never auto-post, spend or claim a customer subscription outcome.
