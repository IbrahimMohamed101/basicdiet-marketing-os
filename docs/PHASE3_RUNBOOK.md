# Phase 3 — Daily Marketing Workflow

**Status:** First executable, manually triggered, read-only workflow installed. Six roles are deterministic handoffs and decision stages, NOT independent autonomous LLM agents.

## Local use

    python3 scripts/validate.py
    python3 -m unittest discover -s tests -v
    python3 scripts/daily_brief.py --channel instagram --goal auto --out-dir output/daily

Outputs: output/daily/daily-brief.md and .json, status DRAFT_REVIEW_REQUIRED. Use --idea-id C003 to select a specific unused idea.

## GitHub Actions manual run

Go to Actions > Basic Diet - draft content (manual) > Run workflow. Select channel, goal, optional idea ID. Download artifact from the run. It never commits drafts or touches social/media accounts. Permissions are contents:read only. No schedule is enabled.

## Optional AI

The --ai switch (or use_ai=true when manually dispatching Actions) is OFF by default. It requires a separately configured repository secret OPENAI_API_KEY, transmits the selected brief to the model provider, and may incur API charges. The response is kept in ai-suggestions.md as UNVERIFIED suggestions, separate from the standard review-only draft. Do not activate it without deliberately authorizing API usage.

## Truth and safety rules

- The 30 backlog items are historical proposals from 2026-10-07, not current facts.
- Only content log entries with a real Post URL and Published status count as verified publication in this tool; posts not recorded in that log might exist, so a human must check platforms.
- Verify the precise asset in Drive, usage rights, current menu, plans, nutrition, offers, delivery coverage and CTA link before any publication.
- No verified live conversion data, campaign CAC/ROAS or automatic media generation is included.
- A planning draft is never authorization to publish, schedule, change prices, message customers or spend on ads.

This fulfills a first runnable Phase 3 pilot, not complete autonomous multi-agent delegation or live integrations.
