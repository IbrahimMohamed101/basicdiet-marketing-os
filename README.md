# Basic Diet Marketing OS

**Status:** Phase 0 — foundation scaffold, 2026-10-08. **Published in the private GitHub repository.**

A private, version-controlled operating system for Basic Diet marketing. It holds durable decisions, current state, source references, editorial activity and instructions for AI assistants. It is **not** the restaurant's transactional backend, a database, or an autonomous advertising bot.

## Quick start

1. Read [`AGENTS.md`](AGENTS.md), then [`STATE.md`](STATE.md).
2. For marketing tasks, read [`.agents/skills/basic-diet-marketing/SKILL.md`](.agents/skills/basic-diet-marketing/SKILL.md).
3. Read the smallest task-specific sources from `knowledge/`, `content/`, `data/`, `experiments/`, or `decisions/`.
4. Execute → Verify → Document. Only document completed actions as completed.

## Trigger commands

- `Basic Diet Mode — ننزل إيه النهارده؟`
- `Basic Diet Mode — راجع الأسبوع`
- `Basic Diet Mode — اعمل حملة`
- `Basic Diet Mode — حلل النتائج`
- `Basic Diet Mode — حالة المشروع`

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md`, `STATE.md` | Agent boot sequence and current truth |
| `.agents/skills/` | Native agent skill and future selected external skills |
| `.agents/workflows/` | Repeatable manual workflows |
| `agents/` | Role contracts, **not deployed autonomous agents** |
| `knowledge/` | Verified brand, audience, offer and positioning facts |
| `content/` | Backlog, planned and actually published content |
| `data/` | Source inventory and aggregate snapshots only |
| `campaigns/`, `experiments/`, `decisions/` | Paid plans, hypotheses, and rationale |
| `docs/` | Source map, safeguards, roadmap, and migration checklist |
| `scripts/` | Local validation and GitHub bootstrapping |

## Source boundaries

- Live business facts: Basic Diet backend/dashboard (**read-only, permissioned exports** in later phases).
- Brand assets: Google Drive / approved asset storage. Store links and indexes, **not large media** here.
- Archived marketing records: [`basicdiet145/marketing`](https://github.com/IbrahimMohamed101/basicdiet145/tree/main/marketing) until verified migration.
- Original Basic Diet marketing skill: [`basicdiet145/skills/basic-diet-marketing`](https://github.com/IbrahimMohamed101/basicdiet145/tree/main/skills/basic-diet-marketing).
- External framework: [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills); selected components may be imported in Phase 2 with license preservation.

**Do not** upload customer identities, payment records, credentials, tokens, private support messages, or unverified medical claims. Repository is intended to be private even when documents contain only sanitized information.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for phase boundaries and [`docs/BOOTSTRAP.md`](docs/BOOTSTRAP.md) for repository setup and verification.
