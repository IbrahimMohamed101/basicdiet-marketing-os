# Phase 1 migration — completed 2026-10-08

## Provenance

- Source: https://github.com/IbrahimMohamed101/basicdiet145
- Source **pinned commit:** `5241bfb0fe8fe4d2a15b15ed85d13648b8a7be37` (do not use moving `main` when validating history).
- Destination: https://github.com/IbrahimMohamed101/basicdiet-marketing-os, private repository.
- Source files: **23** = 22 from `marketing/` plus the original `skills/basic-diet-marketing/SKILL.md`.
- **23 byte-identical archive copies**, **20 working copies** in the new architecture. Working copies are deliberately identical to original documents at migration (historical cross-references are resolved by this manifest, not silently altered).
- Working `AGENTS.md`, `STATE.md`, and `README.md` are new repository operating documents; historical versions are retained in the archive.
- Legacy marketing source files were **not deleted or edited**.

## File manifest

| Original path | Exact archive copy | New working path | Git blob SHA (original / archive / initial working copy) |
| --- | --- | --- | --- |
| `marketing/CHANGELOG.md` | `archive/basicdiet145-2026-10-07/marketing/CHANGELOG.md` | archive only (replaced by new root docs) | `405925997d2377d19abccc024af28bd1dbf79ca2` |
| `marketing/FRAMEWORKS.md` | `archive/basicdiet145-2026-10-07/marketing/FRAMEWORKS.md` | `docs/FRAMEWORKS.md` | `5c69faf38c24a18d28022169cd8216c7f26e05ee` |
| `marketing/README.md` | `archive/basicdiet145-2026-10-07/marketing/README.md` | archive only (replaced by new root docs) | `454f2ebdb76fadd47e5df51d407f95f983cc8e66` |
| `marketing/STATE.md` | `archive/basicdiet145-2026-10-07/marketing/STATE.md` | archive only (replaced by new root docs) | `27f4594e7f507bc7e2250a19e9e69961c4d7fb8a` |
| `marketing/analytics/baseline-status.md` | `archive/basicdiet145-2026-10-07/marketing/analytics/baseline-status.md` | `data/analytics/baseline-status.md` | `ce2f34cb8de50093e21dc20664bef9e00806d436` |
| `marketing/analytics/implemented-analytics.md` | `archive/basicdiet145-2026-10-07/marketing/analytics/implemented-analytics.md` | `data/analytics/implemented-analytics.md` | `c3efae9711ed8caf11696b2d1b1dc1fe485ccfc4` |
| `marketing/analytics/measurement-framework.md` | `archive/basicdiet145-2026-10-07/marketing/analytics/measurement-framework.md` | `data/analytics/measurement-framework.md` | `48e2a8cbdca7d18f6c939cae5f5fd1aabe16bc85` |
| `marketing/content/asset-catalog.md` | `archive/basicdiet145-2026-10-07/marketing/content/asset-catalog.md` | `assets/catalog.md` | `977d8d52d51953c8a0d149b85694f83994cd1795` |
| `marketing/content/backlog.md` | `archive/basicdiet145-2026-10-07/marketing/content/backlog.md` | `content/ideas/backlog.md` | `43f0e3f7cfecad7680d74b5f096ea16bd1b10bd3` |
| `marketing/content/content-log.md` | `archive/basicdiet145-2026-10-07/marketing/content/content-log.md` | `content/published/content-log.md` | `23dfb8a448b9f3ac93d98771293179d643fb70ee` |
| `marketing/content/strategy.md` | `archive/basicdiet145-2026-10-07/marketing/content/strategy.md` | `content/strategy.md` | `fbf789130f7d0b6e6bbbabadacc291e1f432fdf4` |
| `marketing/content/winners.md` | `archive/basicdiet145-2026-10-07/marketing/content/winners.md` | `content/winners.md` | `391f442b6ff90f668491dff0ee7820f98a89ed92` |
| `marketing/context/audience-voc.md` | `archive/basicdiet145-2026-10-07/marketing/context/audience-voc.md` | `knowledge/audience-voc.md` | `0075236650d463ad8da9c5fb5b854f41d986e7c7` |
| `marketing/context/competitors.md` | `archive/basicdiet145-2026-10-07/marketing/context/competitors.md` | `knowledge/competitors.md` | `ba01147a2edf6f932f2674edaae7ca3891882036` |
| `marketing/context/data-sources.md` | `archive/basicdiet145-2026-10-07/marketing/context/data-sources.md` | `data/sources.md` | `271f458af87b70bc79cc226945593ba6f232266d` |
| `marketing/context/offers-pricing.md` | `archive/basicdiet145-2026-10-07/marketing/context/offers-pricing.md` | `knowledge/offers-pricing.md` | `316a46a337be2a51980460cf8b85c50488052379` |
| `marketing/context/positioning-messaging.md` | `archive/basicdiet145-2026-10-07/marketing/context/positioning-messaging.md` | `knowledge/positioning-messaging.md` | `f797d6b527365ff6822d485b90fda0760a02d069` |
| `marketing/context/product-marketing.md` | `archive/basicdiet145-2026-10-07/marketing/context/product-marketing.md` | `knowledge/product-marketing.md` | `1b70ba520dabdcf01fd29945587f8eed0e95bdc7` |
| `marketing/context/voc-findings.md` | `archive/basicdiet145-2026-10-07/marketing/context/voc-findings.md` | `knowledge/voc-findings.md` | `46b467b0994b5747fc0833588580200bdec8d8ae` |
| `marketing/decisions/decisions.md` | `archive/basicdiet145-2026-10-07/marketing/decisions/decisions.md` | `decisions/history.md` | `87a5f29c4f397e67252b1c96af0be90a57efd362` |
| `marketing/experiments/experiments.md` | `archive/basicdiet145-2026-10-07/marketing/experiments/experiments.md` | `experiments/history.md` | `64fea4cd0d37eaa090104f62cbbe0d3abf646bde` |
| `marketing/plans/current-week.md` | `archive/basicdiet145-2026-10-07/marketing/plans/current-week.md` | `plans/archive/2026-10-07-current-week.md` | `45d4c4401f38e0a747ad4fa46d68ac547a58a6a8` |
| `skills/basic-diet-marketing/SKILL.md` | `archive/basicdiet145-2026-10-07/skills/basic-diet-marketing/SKILL.md` | `.agents/skills/basic-diet-marketing/references/original-2026-10-07.md` | `d6b4b5b439152bc7eb3b6e6de1f4b1cba08bf3ba` |

## Verification contract

- Compare archived blob SHAs with the source blob SHAs shown in the manifest. Git SHA is derived from raw file bytes; equal hashes verify exact copies.
- Check the 20 working-copy paths exist. The manifest hashes describe their initial migration bytes. Current working copies may evolve with dated evidence; only archive copies are immutable. The validator reports how many working copies still match without blocking legitimate updates.
- Check all 23 listed sources are accounted for (22 marketing documents + 1 skill).
- Review potential personal data, credentials, signed links before every future public export; the initial source scan did not identify clear customer phone numbers, emails, private-key blocks or access tokens. **This automated scan is not a guarantee**.
- Historic `marketing/...` references within the imported files refer to original source paths. Resolve them through this manifest when operating in this repository.
- `content/published/content-log.md` is a historic template, **not evidence of any actual publication**. `experiments/history.md` contains hypotheses, **not proven experiments**.
- Historical plan `plans/archive/2026-10-07-current-week.md` is archived; do not treat it as the current week.
- Real-time pricing, campaigns, app downloads and paid conversion metrics remain subject to official live sources.

## Scope boundary

Phase 1 migrates **repository marketing knowledge only**. It does not import Drive media, MongoDB customer data, analytics exports or install external third-party skills. Those require later phases and explicit access/approval.
