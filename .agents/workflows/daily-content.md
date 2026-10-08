# Daily content workflow — Basic Diet Mode

**Trigger:** `Basic Diet Mode — ننزل إيه النهارده؟`

1. Read root `AGENTS.md`, `STATE.md`, native `basic-diet-marketing` skill and `content/ideas/backlog.md` (30 grounded ideas).
2. Read `content/strategy.md`, `content/published/content-log.md`, `knowledge/offers-pricing.md`, `assets/catalog.md`; refresh prices/offers and source assets from official systems when necessary.
3. Apply **`content-strategy` + `social`** for a post, optionally **`video` + `ad-creative`** for a video/ad concept. Only apply **`storyboard-to-video`** if the user explicitly requests complex image/reference boards/storyboards or that particular production method.
4. Check prior published evidence. Choose an unused grounded idea, with no unsupported health/weight-loss claims.
5. Draft an approval-ready result: objective, audience/funnel, channel/format, hook, script and shots, caption, CTA, stories, precise approved asset/source, one KPI, paid potential.
6. Obtain permission for any actual generation, posting, sending, scheduling, or ad spend as appropriate. No external automation is enabled by reading this file.
7. After verified publication, write platform URL/date/results to `content/published/` and update state/learning log. Do not invent performance or attribution.

No posting integration, scheduler or live advertising account is connected by Phase 2.

## Executable manual pilot

Run `python3 scripts/daily_brief.py --channel instagram --goal auto` or manually dispatch `.github/workflows/daily-content-brief.yml`. The result is an offline approval-only creative brief in output/daily or a GitHub Actions artifact. Optional AI suggestions require explicit opt-in and OPENAI_API_KEY. This does not publish, schedule, spend or verify current live pricing/media.
