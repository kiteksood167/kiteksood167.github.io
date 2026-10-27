---
layout: null
sitemap: false
permalink: /writing-guide-internal.txt
published: false
---
# GadgetGyaan writing guide

Every post (written by a person or by the scheduled writing task) follows these rules.

## Audience
Two audiences, one per post:
- **India posts** (Launches, Phones, Laptops, Audio, Wearables, Tablets, Gaming, Accessories, Smart Home, Guides): Indian buyers, prices in rupees (₹), Amazon.in links, Indian sale seasons, brands and availability in India.
- **Global posts** (category Global): readers in the US, UK, Canada and Australia. Prices in US dollars (add £ where it helps), products widely sold in the US/UK, Amazon.com links using store="us", American spelling, no India-specific references.
Plain English, short sentences, no jargon without an explanation.

## Topics that work
- Buying guides by budget ("best X under ₹Y") — must be researched against current prices and models.
- Explainers (what a spec means and whether it matters).
- How-tos and fixes for common problems.
- Comparisons of two or three specific products.

## Accuracy rules (most important)
- Every product name, price, spec and launch claim must come from a current, reliable source checked on the day of writing.
- Prices change: say "around ₹X at the time of writing" and include the month.
- Never invent test results, personal use, benchmarks or quotes. Do not claim "we tested" unless a person actually did.
- No copied text from other sites. No product images unless the owner gives permission.

## Structure
- Title with the main search phrase, under 70 characters where possible.
- `description` of 1–2 sentences.
- Intro of 2–3 sentences, then `<!--more-->`.
- `##` section headings, a table where it helps comparison, one `>` tip box.
- 700–1,400 words.
- End with "The bottom line" summary.

## Money
- Use the `buy.html` include for product links and set `affiliate: true`.
- Recommend what is genuinely best for the reader, including cheaper options.

## Categories
Exactly one per post:
- **Launches**: news-style posts on newly launched (or officially confirmed upcoming) phones and gadgets in India: official price, key specs, sale date, offers, and who it suits. Written by the daily launch task.
- India topic categories: Phones, Laptops, Audio, Wearables, Tablets, Gaming, Accessories, Smart Home, Guides.
- **Global**: worldwide readers (US/UK), any gadget topic.
The main daily task alternates India and Global days; the launch task posts separately every evening.

## Launch posts (category Launches)
- Only cover a launch confirmed by the brand or by at least two reliable tech news sources. Never report leaks or rumours as facts; if a detail is rumoured, say so or leave it out.
- Title format: "<Product> Launched in India: Price, Specs and Sale Date" (or "...Launching on <date>: What We Know" for confirmed upcoming launches).
- Include: official India price for each variant, launch/sale date, where to buy, launch offers, 5–8 key specs in a table, who it's for, and 1–2 close rivals at similar prices.
- 500–900 words is fine for launch posts.
- Add a buy button only once the product is actually on sale.

## News posts (midday task, added Oct 2026)
- Written by the midday news task. Covers gadget news that is NOT a new launch: price cuts and new prices in India, big sale announcements with confirmed dates, major software updates (Android, iOS, One UI and similar) and which phones get them, new features rolled out to popular devices, recalls or safety warnings, and policy or rule changes that affect gadget buyers. New launches stay with the evening launch task.
- Use the topic category the news is about (Phones, Laptops, Audio, Wearables, Tablets, Gaming, Accessories, Smart Home, Guides; Global for US/UK news), never Launches, and add `news: true` to the front matter. The morning task ignores `news: true` posts when it balances categories and alternates India/Global days.
- Facts must come from the official source (brand, company or government) or at least two reliable news sites. Never report leaks or rumours as facts.
- 400–800 words: what happened, what it means for readers, who is affected, what to do next, and "The bottom line". Title states the news plainly, without clickbait.

## SEO checklist for every new post (added Oct 2026)

- **title** can be long and descriptive. If it is over 55 characters, also add a short `seo_title:` (max ~50 characters, main keyword first). It is used for the browser tab and Google title.
- **description** must be 120–155 characters. Don't go over 160.
- **Related reading:** before the final `## The bottom line` heading, add one line with 2 links to older related posts:
  `**Related reading:** [Post title](/post-slug/) · [Post title](/post-slug/)`
  Use relative links (`/slug/`), never the full https://thegadgetgyaan.com address.
- **Inline images:** include `width="1200" height="675"` (or the real size) and `loading="lazy"` on every `<img>`.
- **Mobile cover copy:** also save a 1080px-wide copy (JPEG quality ~78) at `assets/images/md/<same-file-name>.jpg`; phones load it instead of the 1600px original.
- **Card thumbnail:** after adding a cover image, also save a 720x405 copy (JPEG quality ~78) at `assets/images/thumbs/<same-file-name>.jpg`. The homepage uses it for speed. If it's missing, the full image is used, so nothing breaks.

## Extra categories (also_in)

Every post has ONE main `category` (used for the breadcrumb, the card label and the Pinterest board). If the post clearly belongs in other sections too, add them with `also_in`, right under `category`, so readers find it there as well:

    category: Launches
    also_in: [Phones, Global]

Rules: use only these names: Launches, Phones, Laptops, Audio, Wearables, Tablets, Gaming, Accessories, Smart Home, Guides, Global. Use at most 3 extra categories, and only real fits. Typical pairings: phone launches → Phones (+ Global if launched outside India or worldwide); phone how-tos → Phones and/or Guides; laptop/tablet comparisons → both Laptops and Tablets; buying-guide explainers → Guides; Global phone posts → Phones.

## Link the new post from older posts (added Oct 2026)

A new post with no links pointing to it is found and ranked more slowly. After writing a new post, open 1–2 older posts on a closely related topic and add the new post to their `**Related reading:**` line (keep at most 3 links on that line; replace the least related one if it is full). Use the exact title and a relative link `/slug/`. Never link a post to itself and never invent a slug.

## Updating an existing post (added Oct 2026)
When you change facts in a published post (official price announced, price change, sale date, new update rollout), readers must be able to see it:
- Set `last_modified_at: YYYY-MM-DD HH:MM:00 +0530` (current India time). Post cards then show "· Updated <date>" for 7 days.
- For an important change, also add `update_note: "One plain sentence saying what changed"` in double quotes, for example `update_note: "Infinix GT 50 Pro is now official in India at ₹69,999, with the first sale on October 30 on Flipkart."`. It shows as a green "Updated" box at the top of the post and, for 3 days, in the slim bar at the top of every page (readers can close it). Keep it under about 110 characters and only state confirmed facts.
- Don't add `update_note` for small fixes like typos or extra internal links.
- If several posts change because of the same news (for example a launch price that also appears in a roundup), add `update_note` only to the main post, so the update bar doesn't repeat the same news. All updated posts still appear on /updates/ (Recent updates page) for 30 days.
