---
name: basic-diet-image-creative
description: >
  Mandatory for Basic Diet Instagram or Facebook static feed posts, carousel covers,
  Stories, food photo ads, image generation/editing, branded graphics and matching
  design families. Applies to ordinary posts as well as paid creatives. Work from
  real Basic Diet Drive photos and a stable but owner-provisional visual system.
metadata:
  version: 1.0.0
---

# Basic Diet image creative — production skill

**When triggered:** Any still-image brief, static post, Story, carousel, social cover, image prompt, photo retouch or food visual. A still post does **not** require a Reel/video. The chat AI creates original concepts; this file is the design operating method, not an autonomous renderer.

## Required lightweight reads

1. \`AGENTS.md\` → \`docs/BOOT.md\` → current top of \`STATE.md\` → native \`basic-diet-marketing\` skill.
2. This skill → \`docs/BRAND_VISUAL_SYSTEM.md\` → \`docs/IMAGE_CREATIVE_PLAYBOOK.md\`; check \`assets/visual-identity.json\`.
3. Read \`docs/CREATIVE_AGENT_PROTOCOL.md\` for factual/approval gates. Load \`content-strategy\`, \`social\`, or \`ad-creative\` original vendor references **only** when their specialist detail affects the task. Preserve upstream file hashes.
4. Resolve exact candidate photo/logo IDs in \`assets/drive-source-index.json\`. Read actual image pixels. Look at previous approved Basic Diet designs; indexed metadata is not visual proof.

## Invariant identity (across the entire feed)

- **Design DNA from actual Basic Diet Drive artwork, currently PROVISIONAL:** warm cream background, soft organic abstract motifs, restrained green/orange accents, real untouched circular brand mark, clear Arabic hierarchy and breathing room.
- **Color:** green \`#107F55\` and orange \`#E95D2C\` were sampled from one source logo; *not approved official tokens*. Cream \`#F7F4E6\` is a provisional design proposal; match visually to actual inspected previous posts and ask owner to approve. Never say officially approved.
- **Consistent placement logic:** safe top brand zone, one dominant Arabic hook, optional source photograph, tiny stable footer or CTA. Logo appears at readable size and retains its original art/aspect. No fake or regenerated logotype.
- **Visual diversity:** same type hierarchy, palette, corner/radius language and motif style, but rotate composition, photo crops and selected format. Do not repeat the same three-photo tile every day.
- **RTL:** proper shaping, short Saudi-Arabic headline, no distorted letters. Generate backgrounds and food imagery separately if using an AI renderer; type text using an Arabic-capable design engine/editor.

## Five reusable families (choose ONE per creative, not all)

| Family | When | Stable brand features | Variable element |
| --- | --- | --- | --- |
| \`product_hero\` | Appetite, one real dish | cream/green/orange, brand strip, 1 hook | large dish crop, angle & garnish **only as photographed** |
| \`choice_comparison\` | 2–3 actual products, comment poll | numbered cards, simple hook/footer | card geometry and true selected meal sources |
| \`editorial_statement\` | Educational/brand voice/ordinary post | cream motif, original logo, bold Arabic | oversized headline, one verified proof or illustration; may have no food photo |
| \`offer_card\` | Verified current plan/offer only | green/orange typography system | offer number, footnote, CTA; block until fresh backend evidence |
| \`story_micro\` | Story, quiz, poll, quick reminder | same motifs/colors and original logo | vertical framing, one direct interaction with mobile safe zone |

## Design-first creative decision

- Define audience question and the exact attention mechanism. Brainstorm three genuinely different concepts, score for distinctive visual, photographed asset availability, Saudi-market language, clarity and brand coherence.
- For a real food product, prioritize existing photo **compositing** over wholesale generative resynthesis. Content generation may create an empty lifestyle backdrop, but must not alter food shape, ingredients, portions or logo.
- For editorial/nonfood graphics, a background-first AI image is allowed; any unverifiable brand claim or fake customer/location is blocked.
- Determine 1080×1350 feed (4:5), 1080×1080 when specifically needed, 1080×1920 Story (9:16); carousel slides use one consistent canvas and visual rail. No forced 9:16 crop from 4:5.
- Exports: crisp true-photo areas; Arabic title legible on mobile; no photo stretched, cut off, artificial serving size, unsupported nutrition, or invisible footer. Check real rendered image visually, not just prompt text.

## Mandatory output per chosen draft

1. Reference sources and confidence (Drive IDs + direct visual inspection dates; note rights, menu, and owner brand status).
2. Selected design family, creative angle and originality reason; concise headline / subline / CTA / caption in Saudi Arabic.
3. Production recipe: source image crop, layout, contrast zone, logo safe area, text-safe area, colors with approval status, feed/story or carousel dimensions.
4. Paste-ready image generation **or** compositing prompt + negative prompt. For food: explicitly demand exact image-pixel fidelity or fallback to photo compositing.
5. Preview or draft asset if requested and technically generated; never claim publish-ready before independent approval. Store durable prompt/asset IDs only for accepted tracked drafts.
6. Quality gate: score 0–5 for product fidelity, brand continuity, mobile clarity, Arabic typography, claim accuracy, composition and call-to-action. **Fail** any product substitution, AI-faked logo, material health claim, unreadable Arabic or fake proof regardless of average.

## Competition and learning

\`research/competitors/healthy-corner-2026-10-09.md\` is a **limited** source record: Instagram grid could not be viewed in this run. Do not claim inspection of all posts or competitor feed uniformity. Use general mechanisms learned from verified public ads (food prominence, one-message promotion) without copying layouts, photos, slogans or protected identity.

## Approval / persistence

AI visual review is NOT human logo approval, commercial rights or current-menu approval. Keep \`CONCEPT_DRAFT\` for unsupported claims. Reviewer-approved use of media requires external evidence and actual branch rules/CODEOWNERS where available. Update \`assets/visual-identity.json\` only with verified or explicitly provisional change provenance; record accepted creative in \`content/production/\`. Publication must have a real canonical platform URL; no write to published/performance logs without proof.
