from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(HERE, "..", "..")) + "/"
F = os.path.join(HERE, "fonts") + "/"
W, H = 1000, 1500
BG = (14, 14, 18); ORANGE = (255, 90, 31); LIME = (200, 230, 80)

if len(sys.argv) != 5:
    sys.exit("Usage: python3 %s <slug> <LABEL> <title> <subtitle>" % sys.argv[0])
PINS = [tuple(sys.argv[1:5])]

IMG = {}

def font(n, s): return ImageFont.truetype(F + n, s)

def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

logo = Image.open(R + "assets/logo-full-dark-bg.png").convert("RGBA")
logo = logo.resize((380, int(380 * logo.height / logo.width)), Image.LANCZOS)

for slug, cat, title, sub in PINS:
    im = Image.new("RGB", (W, H), BG)
    cov = Image.open(R + "assets/images/" + IMG.get(slug, slug + ".jpg")).convert("RGB")
    cov = ImageOps.fit(cov, (W, 860), Image.LANCZOS, centering=(0.5, 0.5))
    im.paste(cov, (0, 0))
    # fade bottom of photo into background
    fade = Image.new("L", (W, 260))
    for y in range(260): ImageDraw.Draw(fade).line([(0, y), (W, y)], fill=int(255 * y / 259))
    im.paste(Image.new("RGB", (W, 260), BG), (0, 600), fade)
    d = ImageDraw.Draw(im)
    fc = font("Inter-Bold.otf", 30)
    tw = d.textlength(cat, font=fc)
    d.rounded_rectangle([60, 800, 60 + tw + 44, 856], radius=28, fill=ORANGE)
    d.text((82, 809), cat, font=fc, fill="white")
    ft = font("InterDisplay-ExtraBold.otf", 78)
    y = 890
    for ln in wrap(d, title, ft, W - 120):
        d.text((60, y), ln, font=ft, fill="white"); y += 92
    d.text((60, y + 14), sub, font=font("Inter-Medium.otf", 40), fill=(200, 200, 210))
    im.paste(logo, (52, H - 150), logo)
    fr = font("Inter-Bold.otf", 34)
    t = "thegadgetgyaan.com"
    d.text((W - 60 - d.textlength(t, font=fr), H - 120), t, font=fr, fill=LIME)
    d.rectangle([0, H - 10, W, H], fill=ORANGE)
    out = os.path.join(os.getcwd(), f"pin-{slug}.jpg")
    im.save(out, quality=88, optimize=True)
    print("saved", out)
