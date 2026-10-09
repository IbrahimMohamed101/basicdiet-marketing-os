"""Optional reproducible RGB color counts for *local* PNG supplied by authorized Drive connector.
Usage: pip install Pillow; python scripts/sample_brand_colors.py path/to/Logo-High-Qualty.png
No network access, no mutation, no font download.
"""
import collections
import sys
try:
    from PIL import Image
except ImportError:
    raise SystemExit("Install Pillow locally: pip install Pillow")


def main(path):
    img=Image.open(path).convert("RGBA")
    counts=collections.Counter((r,g,b) for r,g,b,a in img.getdata()
                               if a==255 and max(r,g,b)-min(r,g,b)>40)
    print("Dimensions:",img.size)
    for rgb,n in counts.most_common(10):
        print("#%02X%02X%02X"%rgb, n)


if __name__=="__main__":
    if len(sys.argv)!=2:raise SystemExit("Usage: python scripts/sample_brand_colors.py FILE.png")
    main(sys.argv[1])
