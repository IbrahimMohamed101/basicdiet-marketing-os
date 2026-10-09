# Basic Diet — compact cold start

**Scope:** AI in chat is the creative engine; this repo is the source-of-truth for instructions, persistent decisions, asset IDs and historical evidence. This page is a compact routing map; read root AGENTS.md for non-negotiable permissions. Last edited 2026-10-09.

## Business in one minute

Saudi healthy meal-subscription restaurant. Brand hypothesis: **الطعم + الاختيار + الراحة**. Primary commercial metric is **first-time paid subscribers**, not engagement or registrations. Accurate paid attribution is not yet available. Discounts, menu, delivery regions, calories, price and subscription eligibility must be verified against current official backend/admin/menu before public claims.

**Connected:** read-only signed daily backend aggregate snapshots in `data/reports/commerce/YYYY-MM-DD/{30d,60d,90d}.json`; authenticated Google Drive access to assets. **Not connected:** Metricool social network OAuth; no verified post history or creative results. Never treat empty local logs as proof of zero published posts.

The main Drive source: https://drive.google.com/drive/folders/1ZplIhzIZKcK5ZCoe454exU445cL-Vhz- ; exact verified IDs and human checks in `assets/drive-source-index.json`. Brand logo and one food source photograph had an **AI visual inspection on 2026-10-09**, but official logo choice, usage rights and current item availability remain unapproved. See `knowledge/brand-visual-review.md`.

## Lightweight routing

| When asked | Read next |
| --- | --- |
| “ننزل إيه النهاردة؟” / creative idea or caption | `docs/CREATIVE_AGENT_PROTOCOL.md`, `docs/SKILL_DIGEST.md`; actual `social` and `content-strategy` skills only for deeper guidance |
| Static branded post, Story, carousel or image design | native `basic-diet-image-creative` skill, `docs/BRAND_VISUAL_SYSTEM.md`, `docs/IMAGE_CREATIVE_PLAYBOOK.md`, `assets/visual-identity.json`; `ad-creative` vendor only when helpful |
| Google Flow/Reel | above + `video` skill and `docs/GOOGLE_FLOW_PRODUCTION.md`; storyboard skill only on request |
| Commerce / paid media / attribution | latest relevant aggregate report and `analytics`/`attribution` skills as needed; preserve channel/window definitions |
| Previous decisions / content use | `decisions/log.md`, `content/production/`, `content/published/publications.json` selectively; search IDs rather than loading full `creative.json` |
| Historical research | `docs/SOURCE_MAP.md`, relevant `knowledge/`; no automatic full-directory load |

**Prior creatives:** 30 editorial seeds under `content/ideas/`; they're not winning AI copy and must not anchor new output. Read only relevant IDs/angles for duplication checking. `scripts/daily_brief.py` is a separate deterministic offline regression pilot.

## One creative cycle

1. Confirm platform, funnel goal, audience hypothesis, available assets and a measurable KPI.
2. Propose **3 distinct visual mechanisms/angles** and select one using a transparent lightweight score/rationale; avoid ungrounded predictions.
3. Produce specific Saudi Arabic hook, visual/shot plan, caption, CTA, Stories and appropriate image/Flow prompts. Ground in real pixel-inspected Drive source IDs.
4. Review brand, rights, current menu/claims, destination and actual platform history. If missing, label it and keep draft-only.
5. Record accepted pilot in `content/production/` using validated YAML frontmatter. Do **not** record publication until real platform URL/verification exists; do not invent seven-day results.
6. Record any adoption/learning in canonical decisions/state/measurement logs. No automatic publishing or ad spend.

**Own visual identity evidence:** previously created Basic Diet images (not just logo) were visually inspected 2026-10-09. Cream patterned background, green/orange titles, and real circular logo repeat. Details in `docs/BRAND_VISUAL_SYSTEM.md` and `assets/visual-identity.json`. Final colors/fonts/logo remain owner-provisional. Competitor Instagram grid access remains unavailable; only an official site banner and a third-party indexed Reel were confirmed.

**Canonical files:** root `AGENTS.md`, `STATE.md`, native skill, `docs/CREATIVE_AGENT_PROTOCOL.md`, `docs/GOOGLE_FLOW_PRODUCTION.md`, `assets/drive-source-index.json`, `knowledge/brand-visual-review.md`, `knowledge/saudi-voice.md`, `knowledge/claims-register.md`, `content/production/`, `data/reports/`.

**Date/status caveat:** Historical test counts in CHANGELOG/AUDIT files describe old runs. For current tests, inspect the latest GitHub Actions quality workflow; do not manually freeze a count in STATE.
