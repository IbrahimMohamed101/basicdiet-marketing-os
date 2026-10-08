# Six role contracts, one executable workflow

Research → strategy → creative → analytics → media-buyer → operations are deterministic stages in `scripts/daily_brief.py`. They are not autonomous agents. Each role file defines inputs, outputs, skills, permissions, verification and JSON handoff fields. Native Basic Diet instructions apply first; see [AGENTS](../AGENTS.md).

The runtime selects/validates records and uses curated editorial profiles. It records routed skill paths but does not execute their Markdown or call six LLMs. The supervising Codex session applies the relevant skills, verifies evidence and improves the profiles when needed. Optional AI is one bounded creative suggestion request, separate from this pipeline.

This remains deliberately lightweight until separate tools, concurrency or role-specific evaluation justify independent execution. Current handoffs are inspectable in every brief's `agents` array. Scope and recovery: [runbook](../docs/PHASE3_RUNBOOK.md), [data contracts](../docs/DATA_CONTRACTS.md).
