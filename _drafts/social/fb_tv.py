from PIL import Image, ImageDraw, ImageFont, ImageOps
R = "/home/claude/kiteksood167.github.io/"
F = R + "tools/social/fonts/"
OUT = "/tmp/claude-0/-home-claude/d519c818-5092-5511-8552-fae66ef4d73d/scratchpad/"
W, H = 1080, 1350
BG = (14, 14, 18); ORANGE = (255, 90, 31); LIME = (200, 230, 80); GREY = (200, 200, 210); CARD = (28, 28, 36)
def font(n, s): return ImageFont.truetype(F + n, s)
im = Image.new("RGB", (W, H), BG)
cov = Image.open(R + "assets/images/best-43-inch-smart-tv-india.jpg").convert("RGB")
cov = ImageOps.fit(cov, (W, 430), Image.LANCZOS, centering=(0.5, 0.35))
im.paste(cov, (0, 0))
fade = Image.new("L", (W, 180))
for y in range(180): ImageDraw.Draw(fade).line([(0, y), (W, y)], fill=int(255 * y / 179))
im.paste(Image.new("RGB", (W, 180), BG), (0, 250), fade)
d = ImageDraw.Draw(im)
lab = "DIWALI BUYING GUIDE"; fc = font("Inter-Bold.otf", 28)
d.rounded_rectangle([60, 345, 60 + d.textlength(lab, font=fc) + 44, 397], radius=26, fill=ORANGE)
d.text((82, 353), lab, font=fc, fill="white")
d.text((60, 415), "Best 43-inch smart TVs", font=font("InterDisplay-ExtraBold.otf", 74), fill="white")
d.text((60, 505), "5 picks from ₹22,800, prices checked this week", font=font("Inter-Medium.otf", 36), fill=GREY)
rows = [("Xiaomi FX 43", "Best under ₹25,000", "₹22,800"),
        ("Hisense E75Q 43", "Best sound, 48W", "₹29,990"),
        ("Philips 8100 Series 43", "Our top pick", "₹29,999"),
        ("Xiaomi X Pro 43", "Google TV + Dolby Vision", "₹30,999"),
        ("Samsung UE86AH 43", "For Samsung fans", "₹33,990")]
y = 568
for i, (n, tag, p) in enumerate(rows):
    top = i == 2
    d.rounded_rectangle([60, y, W - 60, y + 104], radius=22, fill=CARD, outline=ORANGE if top else None, width=4 if top else 0)
    d.text((95, y + 16), n, font=font("Inter-Bold.otf", 40), fill="white")
    d.text((95, y + 62), tag, font=font("Inter-Medium.otf", 30), fill=ORANGE if top else GREY)
    fp = font("InterDisplay-ExtraBold.otf", 46)
    d.text((W - 95 - d.textlength(p, font=fp), y + 26), p, font=fp, fill=LIME)
    y += 116
d.text((60, y + 2), "Approx. Amazon.in / Flipkart prices, Nov 2026. They change during sales.", font=font("Inter-Medium.otf", 26), fill=(150, 150, 160))
logo = Image.open(R + "assets/logo-full-dark-bg.png").convert("RGBA")
logo = logo.resize((330, int(330 * logo.height / logo.width)), Image.LANCZOS)
im.paste(logo, (52, H - 140), logo)
fr = font("Inter-Bold.otf", 34); t = "thegadgetgyaan.com"
d.text((W - 60 - d.textlength(t, font=fr), H - 112), t, font=fr, fill=LIME)
d.rectangle([0, H - 10, W, H], fill=ORANGE)
im.save(OUT + "fb-best-43-inch-smart-tv-india.jpg", quality=90, optimize=True)
print("ok")
