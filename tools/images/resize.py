"""Resize the owner's images for the blog.

Cover (makes 4 sizes):   python3 tools/images/resize.py cover  <source image> <slug>
Inline image (1200x675): python3 tools/images/resize.py inline <source image> <file-name-without-.jpg>

Run from the repo root. Afterwards add the files to assets/images/index.yml
(file, about, credit, used_by) and, for inline images, add this markup in the post:

<figure class="inline-figure">
  <img width="1200" height="675" src="/assets/images/NAME.jpg" alt="..." loading="lazy">
  <figcaption>Illustration</figcaption>
</figure>
"""
import sys
from PIL import Image

def fit(src, w, h):
    im = Image.open(src).convert("RGB"); r = w / h; W, H = im.size
    if W / H > r:
        nw = int(H * r); im = im.crop(((W - nw) // 2, 0, (W - nw) // 2 + nw, H))
    else:
        nh = int(W / r); im = im.crop((0, (H - nh) // 2, W, (H - nh) // 2 + nh))
    return im.resize((w, h), Image.LANCZOS)

def save(im, path, q):
    im.save(path, quality=q, optimize=True, progressive=True); print("saved", path)

if len(sys.argv) != 4 or sys.argv[1] not in ("cover", "inline"):
    sys.exit(__doc__)
kind, src, name = sys.argv[1:]
d = "assets/images/"
if kind == "cover":
    f = name + ".jpg"
    save(fit(src, 1600, 900), d + f, 82)
    save(fit(src, 720, 405), d + "thumbs/" + f, 80)
    save(fit(src, 1080, 608), d + "md/" + f, 80)
    save(fit(src, 400, 225), d + "sm/" + f, 78)
else:
    save(fit(src, 1200, 675), d + name + ".jpg", 82)
