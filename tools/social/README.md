# Social graphics

Makes the Pinterest pin (1000x1500) and the Instagram/Facebook/WhatsApp graphic (1080x1350) for a post, using the post's cover image from `assets/images/<slug>.jpg`.

```
cd <any output folder>
python3 <repo>/tools/social/make_pin.py <slug> "<LABEL>" "<short title>" "<subtitle>"
python3 <repo>/tools/social/make_ig.py  <slug> "<LABEL>" "<short title>" "<subtitle>"
```

Example:

```
python3 tools/social/make_pin.py best-tws-earbuds-under-3000 "BUYING GUIDE" "Best TWS earbuds under ₹3,000" "Top picks with ANC and long battery"
```

Outputs `pin-<slug>.jpg` and `ig-<slug>.jpg` in the current folder. Needs Pillow (`pip install pillow --break-system-packages`).
Labels used so far: BUYING GUIDE, COMPARISON, LAUNCH, UPDATE, NEWS, HOW-TO. Keep the title short (about 30 characters) so it fits in two lines.

Fonts: Inter, by Rasmus Andersson, SIL Open Font License 1.1 (https://github.com/rsms/inter).
