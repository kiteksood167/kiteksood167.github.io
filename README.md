# GadgetGyaan

A tech and gadgets blog for Indian buyers, built with Jekyll and hosted free on GitHub Pages.

## Put it online (one time, ~10 minutes)

1. On GitHub, create a new **public** repository. Name it `YOUR-USERNAME.github.io` to get the simplest web address.
2. Upload all these files to the repository (drag and drop on "Add file → Upload files" works).
3. Open **Settings → Pages**. Under "Build and deployment", choose **Deploy from a branch**, branch **main**, folder **/ (root)**, then Save.
4. Wait 1–2 minutes. Your blog is live at `https://YOUR-USERNAME.github.io`.
5. Open `_config.yml` and change the lines marked `<-- CHANGE` (your site URL and contact email).

## Using your own domain (recommended before applying for AdSense)

1. Buy a domain such as `gadgetgyaan.in` from any registrar.
2. In **Settings → Pages → Custom domain**, enter it and save. Follow GitHub's DNS instructions.
3. Tick **Enforce HTTPS**.
4. Update `url:` in `_config.yml` to `https://yourdomain.in`.

## Turning on money features

- **AdSense:** Apply at adsense.google.com when you have roughly 20–30 good posts. After approval, paste your `ca-pub-…` ID into `adsense_client` in `_config.yml`, and add an `ads.txt` file with the line Google gives you.
- **Amazon Associates:** Sign up at affiliate-program.amazon.in and put your tag (e.g. `gadgetgyaan-21`) into `amazon_tag`. Every "Check price on Amazon" button will then earn commission.
- **Google Search Console:** Add your site and submit `/sitemap.xml` so Google finds your posts faster.

## Writing a new post

Create a file in `_posts/` named `YYYY-MM-DD-short-title.md`:

```markdown
---
title: "Your post title"
description: "One or two sentences shown on cards and in Google results."
date: 2026-10-20 10:00:00 +0530
category: Phones        # Phones, Laptops, Audio or Guides
tags: [tag1, tag2]
affiliate: true         # only if the post has affiliate links
---

Intro paragraph.

<!--more-->

## First heading
...
```

To add an Amazon button inside a post:

```liquid
{% include buy.html name="Product name" query="amazon search words" note="short note" %}
```

See `WRITING_GUIDE.md` for the style rules every post follows.
