# Phase 1 migration checklist — Not started

- [ ] Verify old repo `main` commit SHA, record it in this file.
- [ ] Inventory every file under `marketing/` and `skills/basic-diet-marketing/` (see `SOURCE_MAP.md`).
- [ ] Check each legacy file for customer PII, proprietary credentials, and internal endpoints before copying.
- [ ] Copy historical decisions, experiments, analytics definitions, content logs, content backlog and product context into correct new locations.
- [ ] Preserve provenance (`legacy_path`, source commit SHA, source date); do not imply historical snapshots are live.
- [ ] Compare imported file count and content hashes; keep archive or manifest if changes were required.
- [ ] Update all paths from `marketing/*` to new root layout.
- [ ] Verify `Basic Diet Mode — ننزل إيه النهارده؟` reads migrated backlog, no content repetition, no false publication claims.
- [ ] Do not delete legacy material until migration is verified and explicitly approved.

**Phase 0 deliberately does not tick these boxes.**
