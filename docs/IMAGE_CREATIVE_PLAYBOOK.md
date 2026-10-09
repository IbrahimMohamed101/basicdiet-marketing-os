# Basic Diet — still-image creation and editing playbook

Follow project skill \`.agents/skills/basic-diet-image-creative/SKILL.md\` and \`docs/BRAND_VISUAL_SYSTEM.md\` for **every** static feed post, Story or carousel cover. Video remains governed by the separate video/Google Flow skill.

## Task route

**A. Product still using actual meal:** inspect exact source photo from Drive → select 1–3 product IDs → reuse untouched pixels by masking/cropping/resizing → apply clean brand background/logo/text as independent overlay → render → visually compare with original. This route minimizes product fidelity failures.

**B. Ordinary branded text post:** design a beautiful text-led layout with cream/green/orange and motifs, add real logo pixels. AI may generate *background only* or neutral decoration; Arabic and logo are placed separately. Avoid unnecessary stock-food invention.

**C. Conceptual editorial image:** AI may generate an illustration when it does not claim to depict a real Basic Diet product/customer/branch. Label conceptual and still use project brand frame/logo/text separately.

**D. Verified offer:** block numeric price/code/delivery promises until a dated official offer source is inspected. Don't copy competitor promotions.

## Structured briefing template

- Objective / placement / audience hypothesis:
- Selected visual family \`product_hero | choice_comparison | editorial_statement | offer_card | story_micro\`:
- Real asset IDs and visual QA dates:
- Actual logo candidate/owner approval:
- One headline (Saudi Arabic), one subline max, one CTA:
- Approved palette vs logo-sampled/provisional palette:
- Layout/crop and mobile safe space (e.g., 1080x1350):
- Claims/menu/rights status:
- Source-backed competitor mechanism only (not copied layout):
- Output needed: editable layers / background / flattened rendered post / prompt-only.
- Publication: requires separate approval, not included.

## Paste-ready prompt: generate an empty backdrop only

"Create a refined premium social graphic **background only**, Instagram feed 4:5, inspired by Basic Diet's **own** inspected past designs: warm cream surface, faint soft organic wave or curved leaf-like shapes, restrained deep-green and warm-orange accent areas, balanced generous space for an RTL Arabic headline at the upper center, and a large photo area below. Consistent editorial restaurant feel, fresh and unpretentious. No food, no logos, no text, no letters, no numbers, no badges, no fake packaging. Do not reference or resemble another brand's mark or layout. Leave precise clean safe zones for separately composited real photo and brand overlays."

## Paste-ready prompt: image edit preserving actual product

"Edit the supplied authentic Basic Diet food photograph as a photo composite only, never reimagine the dish. Keep every ingredient, portion, rice, original plate, container, highlights and food geometry recognizable and unchanged. Crop or resize the original pixels to fit a product-hero card against a minimal warm-cream branded background. Leave RTL headline space and logo-safe space. Do not write any Arabic inside the generated image: overlays will be manually typeset afterward. Negative: AI food substitutions, extra garnish, fake steam, fake hands, invented delivery boxes, counterfeit logos, plastic food, medical/nutritional claims, oversized discount stickers."

If an image generator cannot preserve exact food/logotype identity, discard its output and use original-image compositing, as demonstrated by the 2026-10-09 pilot failure.

## Source + prompt fidelity acceptance

Check (1) real pixel source retained (2) accurate logo original (3) 4:5 or 9:16 target (4) foreground hierarchy (5) cream/green/orange identity consistency (6) readable mobile Arabic (7) one CTA (8) no invented dish/menu/price (9) no unverified health claims (10) actual evidence/permission status. Critical failures 1, 2, 6, 8 or 9 reject the whole post.

## Production output

For feed: final 1080×1350 PNG, crop-friendly thumbnail, exact Drive asset IDs, caption, CTA, source status. For Story: a separately laid out native 1080×1920 export (never stretch feed into Story). For carousel: repeated canvas/brand rails across all slides. Archive only successful, human-accepted briefs and genuine publication/performance records.

A Markdown skill cannot automatically enforce pixel alignment or detect hallucination. AI editor + final human visual QA are mandatory; this playbook is an operational guide, not a guaranteed renderer.
