# Decision log

## 2026-10-08 — Repository separation (user-approved intent)

- **Decision:** Build an independent Basic Diet Marketing OS repository instead of keeping marketing operating files inside the app's backend repository.
- **Phase gate:** Initialize only Phase 0 structure; subsequent implementation will proceed phase-by-phase.
- **Architecture:** Private repository for durable docs and agent contracts; live backend/database and Google Drive stay external sources.
- **Status:** Private GitHub repository created; Phase 0 structure published to main.
- **Why:** Version control, reproducible agent instructions, preserved marketing context and clear ownership.
