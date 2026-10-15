date: 2026-10-15
stage: 03
status: COMPLETED
run_key: 2026-10-15:03
source_refs: [AGENTS.md, docs/BOOT.md, STATE.md, docs/AUTOMATED_CREATIVE_PIPELINE.md, docs/BRAND_VISUAL_SYSTEM.md, docs/IMAGE_CREATIVE_PLAYBOOK.md, .agents/skills/basic-diet-image-creative/SKILL.md, assets/visual-identity.json, Drive:1Jk3Xg_v-3dQRVx41KNlq_cr5F3aGYZHC, Drive:1I8-a2wQiP26JnHRblQYdM3fgE0WEQnAg]
predecessor_refs: [automation/daily/2026-10-15/01-ideas.md, automation/daily/2026-10-15/02-critique.md]
attempts: 3
generated_at_riyadh: 2026-10-15T08:34:00+03:00
next_action: Stage 04 create two genuinely different 1080x1350 composited image drafts from the original sandwich and logo; verify pixels and persistent uploads, and record only real URLs. Stage 05 independent visual QA. No publication.

# Stage 03 — C039 approved-for-automated-draft-only production brief

**Recovery evidence:** Stage 03 file absent on three same-day GitHub reads during Stage 04, despite completed and fetched 01 + 02 for 2026-10-15. Reconstructed Stage 03 strictly from those two same-day predecessors; no prior-day stage substituted. This status does NOT imply restaurant-owner approval.

## Verified source material

- **Sandwich source:** Google Drive `1Jk3Xg_v-3dQRVx41KNlq_cr5F3aGYZHC`, `دجاج مشوي.png`, original RGB 1024×1024, visibly one seeded-bread long chicken sandwich on a neutral light-gray background. Both ends and filling visible. Original pixels must remain food source; do not hallucinate extra ingredients or enlarge portion.
- **Logo source:** Google Drive `1I8-a2wQiP26JnHRblQYdM3fgE0WEQnAg`, `Logo-High-Qualty.png`, original 2880×2880 RGBA, circular leaf/dumbbell and Arabic/English brand mark; composite actual transparent source only. Logo variant not owner-approved.
- **Brand palette provisional:** green #107F55, orange #E95D2C, cream #F7F4E6. Use only as sampled/proposed design language.
- **No real sandwich label or packaging verified:** do not invent one. No prices, macros, health claims, discounts, delivery times, availability or meal-plan inclusion.

## Target and hook

- **Audience:** Saudi workday food-choice audience; awareness/appetite, not a claim that the pictured sandwich is currently available.
- **Placement:** Instagram feed still 1080×1350, 4:5.
- **Headline (single only):** «الغدا له شكل ثاني»
- **CTA:** «شوف الخيارات من الرابط في البايو» (requires profile destination verification before publication).
- **Caption draft:** «مو كل وجبة لازم تكون في صحن. وش تفضّل: ساندوتش ولا طبق؟ شوف الخيارات من الرابط في البايو.»
- **Do not print an item name or sales claim on the poster** until current menu eligibility is independently confirmed.

## Two materially distinct art directions

**A — Editorial appetite:** warm off-white editorial field, compact genuine logo upper right, short deep-green RTL title upper left/center, authentic sandwich photograph large and fully visible in central/lower space (retain source photo geometry and neutral background as a deliberate studio image window); small orange accent and CTA at bottom. Use a photo-led look, not giant UI card.

**B — Asymmetric green window:** dominant rich deep-green editorial backdrop with a clean photographic light window angled or off-center containing the complete real sandwich image. Cream Arabic title in a distinct side/top band; genuine logo in a high-contrast quiet corner; understated orange rule and CTA. Distinct spatial hierarchy, not simply recolor A.

## Mandatory QA and rejection gates

- 1080×1350 exact pixels, no stretched original.
- Real sandwich pixels, intact both ends, no extra garnish, food resynthesis, fake labels or packaging.
- Exact source logo artwork with full mark, no retyping, stretching, cropping or fake logo.
- Arabic text must be independently typeset with Arabic shaping + RTL and remain readable on mobile.
- Clear visual focus, no overlapping type, photo, or CTA; use safe inset >=72 px.
- Real output file opened and visually inspected; durable verified destination URLs; do not use temporary sandbox URLs as sole persistence.
- Critical failures: source-food substitution, altered logo, clipped sandwich, malformed Arabic, fake product claim, fake app UI, user-rejected C034 calendar/card aesthetic.
- **Publication blockers:** exact sandwich currently on menu and included in relevant plans? Photo/logo commercial rights? final logo variant? profile link destination? Owner review? All unverified; draft only.

## Composition / implementation recipe

Use Pillow (or equivalent deterministic compositor) to place **the original source photograph** into two photo treatments without generative resynthesis; crop or resize the source as a whole, and preserve both sandwich ends. Typeset Arabic with a real Arabic font and shaping (e.g. Noto Sans Arabic with libraqm/harfbuzz) and inspect actual glyphs; put logo as original transparent PNG. Export two flattened PNGs at native 1080×1350, inspect visually and optionally persist an accessible SVG/HTML vector package only if it actually renders and preserves genuine photo/logo. Verify permanent image URLs before marking Stage 04 completed.
