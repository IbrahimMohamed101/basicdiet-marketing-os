#!/usr/bin/env python3
"""Rebuild the review-only 2026-10-12 still from locally downloaded Drive originals.

Optional production dependencies: Pillow, numpy, opencv-python-headless,
playwright and installed Google Chrome. No network, generation or publication.
Run from the repository root. Originals/output remain gitignored.
"""
from pathlib import Path
import base64
import hashlib
import io
import json
import shutil

import cv2
import numpy as np
from PIL import Image, ImageOps, ImageDraw
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/creative-pilot-2026-10-12"
ORIGINALS = OUT / "originals"
GREEN, ORANGE, CREAM = "#107F55", "#E95D2C", "#F7F4E6"
SOURCE_HASHES = {
    "butter-chicken.png": "4e4c803afec810255d17673e5da982f479d302c0d978331f9db6c7d7f6cd2b44",
    "logo.png": "a47d33b0ff2e657c592b59ea251e3e293157fbcecbafd2d1a245c233c719c98f",
}


def uri(data, mime="image/png"):
    return f"data:{mime};base64," + base64.b64encode(data).decode()


def png_uri(im):
    stream = io.BytesIO()
    im.save(stream, format="PNG")
    return uri(stream.getvalue())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, expected in SOURCE_HASHES.items():
        if hashlib.sha256((ORIGINALS / name).read_bytes()).hexdigest() != expected:
            raise ValueError(f"Source differs from visually inspected Drive original: {name}")
    photo = Image.open(ORIGINALS / "butter-chicken.png").convert("RGB")
    assert photo.size == (896, 1200), "Expected the inspected Drive original"
    rgb = np.array(photo)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    threshold = np.uint8(gray < 45) * 255
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)
    plate = np.zeros_like(gray)
    cv2.drawContours(plate, [contour], -1, 255, cv2.FILLED)
    # Expand only the boundary; never remove white rice/highlights inside the plate.
    plate = cv2.dilate(plate, np.ones((5, 5), np.uint8))
    # Preserve original continuous photographic shadow outside the protected plate.
    # White background becomes transparent; shadow becomes black with its original
    # luminance as opacity. Food/plate interior RGB remains byte-for-byte unchanged.
    alpha = 255 - gray
    alpha[gray > 251] = 0
    alpha[plate == 255] = 255
    layer_rgb = rgb.copy()
    layer_rgb[plate == 0] = 0
    cutout = Image.fromarray(np.dstack([layer_rgb, alpha]))
    crop_box = (8, 300, 888, 1040)
    cutout = cutout.crop(crop_box)
    cutout.save(OUT / "meal-cutout.png")
    # All source RGB values remain exact; mask transparency affects background only.
    assert np.array_equal(layer_rgb[plate == 255], rgb[plate == 255])
    logo = Image.open(ORIGINALS / "logo.png").convert("RGBA")
    logo_box = logo.getbbox()
    logo = logo.crop(logo_box)  # Trim transparent padding, not mark artwork.
    logo.save(OUT / "logo-trimmed.png")

    font_dir = Path("/usr/share/fonts/truetype/noto")
    shutil.copyfile("/usr/share/doc/fonts-noto-core/copyright", OUT / "font-license.txt")
    bold = uri((font_dir / "NotoKufiArabic-Bold.ttf").read_bytes(), "font/ttf")
    regular = uri((font_dir / "NotoSansArabic-Regular.ttf").read_bytes(), "font/ttf")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
 <title>غدا يفتح النفس — Basic Diet — review draft</title>
 <desc>Original Drive chicken-and-rice photograph and original logo. Editable Arabic type. No generated food.</desc>
 <defs>
  <style>
   @font-face{{font-family:BDKufi;src:url('{bold}')}}
   @font-face{{font-family:BDArabic;src:url('{regular}')}}
   .headline{{font-family:BDKufi;font-weight:700;direction:rtl;unicode-bidi:plaintext}}
   .arabic{{font-family:BDArabic;direction:rtl;unicode-bidi:plaintext}}
  </style>
  <filter id="soft-shadow" x="-30%" y="-100%" width="160%" height="300%"><feGaussianBlur stdDeviation="22"/></filter>
 </defs>
 <g id="background">
  <rect width="1080" height="1350" fill="{CREAM}"/>
  <path d="M-150 490 C310 460 265 51 530 -100" fill="none" stroke="#eeebdc" stroke-width="126"/>
  <path d="M-110 590 C270 550 390 242 567 -80" fill="none" stroke="#e7e7d6" stroke-width="2"/>
  <path d="M790 1170 C990 1030 865 780 1210 590" fill="none" stroke="#eeebdc" stroke-width="170"/>
 </g>
 <g id="authentic-logo">
  <image x="82" y="76" width="153" height="163" href="{png_uri(logo)}"/>
 </g>
 <g id="headline">
  <text x="987" y="203" class="headline" font-size="100" fill="{GREEN}">غدا يفتح</text>
  <text x="987" y="368" class="headline" font-size="153" fill="{ORANGE}">النفس</text>
  <path d="M666 401 Q803 419 970 397" fill="none" stroke="{ORANGE}" stroke-width="4" stroke-linecap="round"/>
  <text x="983" y="469" class="arabic" font-size="32" fill="{GREEN}">دجاج بالزبدة</text>
 </g>
 <g id="food-hero">
  <image x="23" y="474" width="1034" height="869.5" href="{png_uri(cutout)}"/>
 </g>
 <g id="cta">
  <path d="M0 1181 Q531 1161 1080 1181 L1080 1350 L0 1350Z" fill="{GREEN}"/>
  <text x="981" y="1235" class="arabic" font-size="39" fill="{CREAM}">شوف الوجبات والباقات</text>
  <text x="981" y="1290" font-family="Arial,sans-serif" font-size="30" text-anchor="end" fill="{CREAM}" letter-spacing="1">basicdietksa.com</text>
  <circle cx="130" cy="1240" r="43" fill="{ORANGE}"/>
  <path d="M148 1240 H112 M126 1226 L112 1240 L126 1254" fill="none" stroke="{CREAM}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 </g>
</svg>'''
    (OUT / "design-source.svg").write_text(svg, encoding="utf-8")
    # Live text and separately editable layers, embedded font/photo/logo; no remote URLs.
    html = '<!doctype html><meta charset="utf-8"><style>html,body{margin:0;width:1080px;height:1350px;overflow:hidden}svg{display:block}</style>' + svg
    (OUT / "design-source.html").write_text(html, encoding="utf-8")
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    if not chrome:
        raise RuntimeError("Install Chrome/Chromium to render RTL with browser shaping")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome, headless=True, args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page.goto((OUT / "design-source.html").as_uri())
        page.evaluate("document.fonts.ready")
        page.screenshot(path=str(OUT / "basicdiet-instagram-post.png"))
        boxes = page.locator("text").evaluate_all("es=>es.map(e=>({text:e.textContent,x:e.getBBox().x,y:e.getBBox().y,w:e.getBBox().width,h:e.getBBox().height}))")
        browser.close()
    final = Image.open(OUT / "basicdiet-instagram-post.png").convert("RGB")
    assert final.size == (1080, 1350)
    final.save(OUT / "basicdiet-instagram-post.png", optimize=True)
    final.resize((270, 338), Image.Resampling.LANCZOS).save(OUT / "instagram-grid-preview.png")
    final.resize((360, 450), Image.Resampling.LANCZOS).save(OUT / "mobile-preview.png")
    # Crop stress tests, not a claim about a current account's grid crop settings.
    ImageOps.fit(final, (270, 360)).save(OUT / "grid-3x4-crop.png")
    ImageOps.fit(final, (270, 270)).save(OUT / "grid-square-crop.png")
    compare = Image.new("RGB", (1200, 750), "#f7f4e6")
    orig_preview = ImageOps.contain(photo, (550, 700))
    compare.paste(orig_preview, ((600-orig_preview.width)//2, 35))
    final_preview = ImageOps.contain(final, (550, 700))
    compare.paste(final_preview, (600+(600-final_preview.width)//2, 35))
    draw = ImageDraw.Draw(compare)
    draw.text((20, 10), "ORIGINAL DRIVE PHOTO", fill="black")
    draw.text((620, 10), "REVIEW COMPOSITE", fill="black")
    compare.save(OUT / "source-vs-final.png")
    evidence = {
        "canvas": [1080, 1350], "meal_crop_xyxy": list(crop_box),
        "logo_transparent_padding_crop": list(logo_box),
        "food_rgb_unchanged_before_resizing": True,
        "image_generation_used": False,
        "text_engine": "Chrome Chromium / HarfBuzz RTL, embedded Noto fonts",
        "text_boxes": boxes,
        "source_sha256": {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in ORIGINALS.glob("*.png")},
        "output_sha256": hashlib.sha256((OUT / "basicdiet-instagram-post.png").read_bytes()).hexdigest(),
        "note": "Mask/pixel assertions are technical checks; visual and human approval remain separate."
    }
    (OUT / "render-evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"output": str(OUT), "dimensions": final.size, "text_boxes": boxes}, ensure_ascii=False))


if __name__ == "__main__":
    main()
