from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
R = "/home/claude/kiteksood167.github.io/"
F = R + "tools/social/fonts/"
OUT = "/tmp/claude-0/-home-claude/d519c818-5092-5511-8552-fae66ef4d73d/scratchpad/"
W, H = 1080, 1350
BG = (14, 14, 18); ORANGE = (255, 90, 31); LIME = (200, 230, 80); GREY = (200, 200, 210); CARD = (28, 28, 36)
def font(n, s): return ImageFont.truetype(F + n, s)
def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines
logo = Image.open(R + "assets/logo-full-dark-bg.png").convert("RGBA")
logo = logo.resize((300, int(300 * logo.height / logo.width)), Image.LANCZOS)

def footer(im, d, n, total):
    im.paste(logo, (52, H - 130), logo)
    t = f"{n}/{total}"
    fr = font("Inter-Bold.otf", 32)
    d.text((W - 60 - d.textlength(t, font=fr), H - 105), t, font=fr, fill=LIME)
    d.rectangle([0, H - 10, W, H], fill=ORANGE)

picks = [
    ("BEST UNDER ₹25,000", "Xiaomi FX 43", "about ₹22,800",
     ["4K LED, 60Hz", "Fire TV with Alexa", "24W speakers", "HDR10 only, no Dolby Vision"],
     "Cheapest good 4K TV from a big brand."),
    ("BEST SOUND", "Hisense E75Q 43", "about ₹29,990",
     ["4K QLED, 60Hz", "48W, 4 speakers, DTS:X", "HDMI 2.1 ports", "VIDAA software (fewer apps)"],
     "Loudest TV here, may not need a soundbar."),
    ("OUR TOP PICK", "Philips 8100 Series 43", "about ₹29,999",
     ["4K QLED", "Dolby Vision + HDR10+", "30W with Dolby Atmos", "Google TV + Chromecast"],
     "The most complete TV under ₹30,000."),
    ("GOOGLE TV + DOLBY VISION", "Xiaomi X Pro 43", "about ₹30,999",
     ["4K QLED, 60Hz", "Dolby Vision + HDR10+", "30W speakers", "Google TV"],
     "Close rival to the Philips."),
    ("FOR SAMSUNG FANS", "Samsung UE86AH 43", "about ₹33,990",
     ["4K LED, 60Hz", "Tizen, works well with Galaxy phones", "30W speakers, HDR10+", "HDMI eARC for a soundbar"],
     "Big brand and service network."),
]
total = len(picks) + 2

# slide 1: existing IG cover
cov = Image.open(OUT + "ig-best-43-inch-smart-tv-india.jpg").convert("RGB")
cov.save(OUT + "carousel-tv-01.jpg", quality=88)

for i, (label, name, price, specs, verdict) in enumerate(picks, start=2):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 14], fill=ORANGE)
    fc = font("Inter-Bold.otf", 32)
    tw = d.textlength(label, font=fc)
    d.rounded_rectangle([60, 110, 60 + tw + 48, 170], radius=30, fill=ORANGE)
    d.text((84, 120), label, font=fc, fill="white")
    ft = font("InterDisplay-ExtraBold.otf", 88)
    y = 220
    for ln in wrap(d, name, ft, W - 120):
        d.text((60, y), ln, font=ft, fill="white"); y += 104
    d.text((60, y + 10), price, font=font("InterDisplay-ExtraBold.otf", 64), fill=LIME); y += 120
    d.rounded_rectangle([60, y, W - 60, y + 4 * 96 + 40], radius=28, fill=CARD)
    fs = font("Inter-Medium.otf", 44); yy = y + 32
    for s in specs:
        d.ellipse([100, yy + 18, 116, yy + 34], fill=ORANGE)
        d.text((140, yy), s, font=fs, fill="white"); yy += 96
    y = y + 4 * 96 + 90
    for ln in wrap(d, verdict, font("Inter-Bold.otf", 46), W - 120):
        d.text((60, y), ln, font=font("Inter-Bold.otf", 46), fill=GREY); y += 60
    footer(im, d, i, total)
    im.save(OUT + f"carousel-tv-{i:02d}.jpg", quality=88, optimize=True)

# last slide: tips + CTA
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, 14], fill=ORANGE)
d.text((60, 110), "Before you buy", font=font("InterDisplay-ExtraBold.otf", 88), fill="white")
tips = ["Get 4K, not Full HD", "QLED is worth a small premium", "Dolby Vision helps on OTT apps",
        "Check the exact model number", "Ask if wall mount is included"]
y = 270; fs = font("Inter-Medium.otf", 46)
for t in tips:
    d.text((60, y), "✓", font=font("Inter-Bold.otf", 50), fill=LIME)
    d.text((130, y), t, font=fs, fill="white"); y += 100
y += 40
d.rounded_rectangle([60, y, W - 60, y + 230], radius=30, fill=ORANGE)
d.text((100, y + 40), "Full guide with prices", font=font("InterDisplay-ExtraBold.otf", 60), fill="white")
d.text((100, y + 130), "thegadgetgyaan.com", font=font("Inter-Bold.otf", 50), fill="white")
d.text((60, y + 280), "Prices from Amazon.in and Flipkart, Nov 2026.", font=font("Inter-Medium.otf", 34), fill=GREY)
d.text((60, y + 330), "They change often during sales.", font=font("Inter-Medium.otf", 34), fill=GREY)
footer(im, d, total, total)
im.save(OUT + f"carousel-tv-{total:02d}.jpg", quality=88, optimize=True)
print("done", total)
