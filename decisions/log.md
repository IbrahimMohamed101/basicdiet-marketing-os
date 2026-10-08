# Decision log

## 2026-10-08 — Independent private marketing repository

- **Decision:** Basic Diet marketing guidance and history live in an independent private repository, separate from app backend runtime code.
- **Reason:** keep context recoverable across agents/chats, distinguish live metrics from retained research, and enable phased work.
- **Status:** executed in Phase 0.

## 2026-10-08 — Lossless historical import (Phase 1)

- **Decision:** Keep every original marketing document and original skill under a pinned-commit archive; expose working copies under new domain paths without rewriting historical facts.
- **Scope:** 23 originals + 20 active/reference copies; root README/STATE/AGENTS remain modern operating docs.
- **Result:** Historical marketing strategy, analytics spec, 30-item idea backlog, competitor research, VOС, experiments and past decisions can be retrieved directly in the new repository.
- **Guardrail:** the historical working docs remain dated; the historic 'current week' plan is archived, not adopted as current. Original source stays untouched.
- **Source:** `docs/MIGRATION.md`.

## Future decisions

Only add decisions when explicitly adopted or validated. A drafted idea or experiment is not an approved execution result.
