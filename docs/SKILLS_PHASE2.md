# Phase 2 — AI Marketing Skill Integration

**Status:** Completed 2026-10-08. This phase installs reusable **instructions and reference documents**, not live agents or paid service access.

## Upstream and integrity

- Upstream: https://github.com/coreyhaines31/marketingskills
- Pinned upstream **commit:** `b9ba399dd88b082b926e261e8ccfb843d20aa066`.
- Selected: **13 upstream skills**, `SKILL.md` plus **67 linked Markdown references**, with zero content rewrites at installation.
- Extra non-executable vendor material: one optional ad creative HTML review template (for manual inspection).
- MIT license copied verbatim: `.agents/licenses/marketingskills-MIT-LICENSE`.
- Exact Git blob SHA for each file: [UPSTREAM_MANIFEST.json](UPSTREAM_MANIFEST.json).
- Not imported: unrelated upstream skills, automated eval fixtures, executable scripts, and optional media; some B2B/SaaS reference text remains as upstream context and must not override Saudi restaurant constraints.

## User-submitted video workflow

The user uploaded `تم لصق markdown (1).md` (284 lines, ~37 KB original CRLF text) on 2026-10-08.

- Text preserved at `.agents/skills/storyboard-to-video/references/user-submitted-2026-10-08.md` (newlines normalized; all 284 logical lines retained).
- Task-scoped entry point: `.agents/skills/storyboard-to-video/SKILL.md`.
- Creative pipeline: idea → story → minimal assets → neutral reference boards → storyboard → final video generation prompt.
- The document opens with a strong "activate immediately upon receipt" instruction. That behavior is **not enabled**: uploading/reading a file must not start the pipeline or send unrelated language questions. Activate **only when the user requests video preproduction**, consistent with native Basic Diet mode.
- Keep visual identities, packaging, and scene geography consistent. Actual image/video generation requires a user-requested deliverable and appropriate approvals.

## Routing

| User request | Selected skills |
| --- | --- |
| "ننزل إيه النهارده؟" | native + `content-strategy`, `social`; `video` for video content |
| "حلل المنافسين" | native + `competitor-profiling`, `customer-research` |
| "اعمل فكرة فيديو" | native + `video`, `social` |
| "اعمل Storyboard وفيديو AI" | native + `storyboard-to-video`, `video` |
| "جهز إعلان ممول" | native + `ads`, `ad-creative`, `attribution` |
| "راجع النتائج" | native + `analytics`, `attribution` |
| "خطة نمو/عروض" | native + `product-marketing`, `offers`, `marketing-loops` |
| "اختبر فكرتين" | native + `ab-testing`, `analytics` |

Use task-specific files; don't blindly read all skills at once.

## Acceptance and safeguards

1. Pinned source SHA and all vendor paths match `UPSTREAM_MANIFEST.json`.
2. Vendor license and optional static asset match pinned blobs.
3. All 13 imported skills have accessible `SKILL.md`, references and name/front matter; the two native skills are separately identifiable.
4. Existing **23 archived marketing source files** and **20 mapped working copies** remain byte-identical to their Phase 1 record.
5. New video skill is present and user source is preserved. It does not auto-run when reading the attachment.
6. **No autonomous agent runtime, publishing integration, paid campaign execution or live data access** has been activated in this phase.

For local checks: `python3 scripts/validate.py` (phase-1 and phase-2 structure/hash validations). For actual agent behavior, Phase 3 must implement a permissioned, reviewable pilot and run scenario tests.
