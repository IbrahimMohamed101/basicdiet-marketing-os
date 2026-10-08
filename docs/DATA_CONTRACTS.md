# Operating data contracts — version 1

Python 3.11+ runtime uses the standard library. `scripts/records.py` is the executable schema;
invalid/missing/empty input, unknown versions and duplicate JSON keys fail before output or API calls.
Unknown record fields or wrong types also fail. Every collection is an object with integer `schema_version: 1` and a named array. Empty arrays explicitly mean no records; absent files do not.

| File / collection | Required record fields | Rules |
| --- | --- | --- |
| `content/ideas/backlog.json` / `ideas` | `id`, `pillar`, `format`, `hook`, `grounding`, `goal` | Nonempty strings; unique C###; goal Awareness/Consideration/Trust/Conversion/Engagement. Original 30 records must remain exact; add new IDs instead of rewriting history. |
| `content/ideas/creative.json` / `profiles` | `id`, `hook`, `shots`, `stories`, `caption`, `subject`, `audience`, `asset_group`, `verification_required` | One profile per idea; ≥3 nonempty scene/card instructions and ≥3 Story instructions. Editorial hypotheses, not verified product claims. Edit these adaptations when improving copy. |
| `content/published/publications.json` / `publications` | `id`, `date`, `channel`, `status`, `url`, `verified_by`, `verified_on`, `verification_source` | status `published`; known idea; canonical HTTPS post URL on the declared platform; no signed/query URLs; dates YYYY-MM-DD, not future; verification at/after publication. Reviewer role is sufficient; no personal contact details. |
| `content/drafts/runs.json` / `runs` | `run_id`, `date`, `idea_id`, `channel`, `status` | Unique run; `reserved` prevents re-selection on all platforms; `released` makes an unpublished idea eligible again. A reservation is never publication. |
| `data/analytics/creative-performance.json` / `performance` | `idea_id`, `publication_url`, `channel`, `metric`, `numerator`, `denominator`, `window_days`, `measured_on`, `source` | Must reference recorded publication; metric `saves_per_reach` or `landing_visits_per_reach`; integers 0 ≤ numerator ≤ denominator and denominator > 0; seven-day window completed before measurement. One observation per URL/metric. Aggregate-only. |

`channel` is instagram/tiktok/facebook/snapchat. `source`/`verification_source` must identify an authorized observation or sanitized report, not secrets or raw exports. Structural validation cannot prove that a human's evidence is true. The offline tool does not fetch URLs, verify media rights or reconcile commercial attribution.

## Selection and output

Published and reserved ideas are excluded globally. The next priority is avoiding the last three published pillars, then a comparable same-channel/goal/pillar performance signal (at least two seven-day observations measured within the last 90 days), then the preserved seven-idea starting sequence and ID. In auto mode the historical/rotation choice establishes the comparison goal first; metrics from different goals are never compared as one score. Performance is a tie-break hypothesis, not a winner declaration; it never converts engagement into revenue. Explicit `--idea-id` must also match `--goal`.

`daily-brief.json` contains version, DRAFT_REVIEW_REQUIRED, date/timezone, idea, channel, objective, audience with hypothesis label, funnel_stage, creative, selection rationale, performance availability, six stage handoffs, checks, source paths and SHA-256 hashes, run_id and AI status. `validate_packet()` checks the output contract before writing. Markdown is rendered from the same object.

Outputs are placed in a new `output/daily/<run_id>/` directory via staging/rename. Existing runs are never overwritten. Default local execution locks the shared ledger through selection/write, then atomically reserves the idea. A crash can leave an orphan output or lock: inspect it, confirm no process is running, reconcile the ledger, then remove only the stale lock. Never auto-expire locks or infer publication from output. Output+ledger are not one filesystem transaction; failures return nonzero.

## Backward-compatible migration

`python3 scripts/migrate_backlog.py --source legacy.md --destination new.json` reads whitespace-tolerant six-column tables (including escaped pipes), validates IDs/goals and refuses to overwrite the destination. All 30 rows were migrated without changing fields. `backlog.md`, all 23 archive originals, the 20 initial working copies, 13 vendor skills and storyboard source remain byte-identical to their manifests.

Legacy `content-log.md` is still consulted to avoid reviving older published ideas. New records belong in `publications.json`. Legacy Published entries require a valid date, C### and platform post URL; damaged entries stop the workflow instead of silently selecting them again. A legacy URL is recorded evidence, not fresh API verification. Do not duplicate a legacy publication in JSON; migrate it deliberately with verification and archive its old entry first.

## Durable memory

After a useful local draft, commit its reservation and retain a reviewed brief in a deliberate campaign/plan document if future editing needs the full text. Raw generated output is ignored. Update `STATE.md` only when priorities change, `decisions/log.md` for adopted decisions, `experiments/` for hypotheses and dated results, `content/winners.md` only with evidence, and `data/reports/` for sanitized dated aggregates. Preserve links between run ID, publication URL and performance observation.

GitHub Actions uses `--dry-run`: artifacts do not reserve ideas across runs. Download/review and run locally to reserve the selected ID, or record a reviewed reservation through a PR. Do not mistake an artifact for durable repository state.
