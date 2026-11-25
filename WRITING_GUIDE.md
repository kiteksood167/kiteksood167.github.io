---
layout: null
sitemap: false
permalink: /writing-guide-internal.txt
published: false
---
# GadgetGyaan writing guide

Every post (written by a person or by the scheduled writing task) follows these rules.

## Quality first: NEW RULES — READ BEFORE ANYTHING ELSE (owner's decision, 25 Nov 2026)

On 25 Nov 2026 Search Console showed 10 pages indexed and 82 not indexed (60 "Crawled - currently not indexed", 19 "Discovered - currently not indexed"). A Diamond Product Expert in the Google Search Central Community looked at the site and said: "every article looks like AI-generated commodity content", and pointed to Google's guide on creating valuable content. The owner agreed to change how the blog works. These rules override anything below that conflicts with them.

1. **At most 3 new posts a week, on Monday, Wednesday and Friday (IST).** No new posts on other days, from any task. On the other days, improve existing posts instead (rule 7).
2. **No new post goes live without the owner's own input.** A scheduled task never publishes a new post into `_posts/` any more. It writes the researched draft to `_drafts_queue/<slug>.md` (this folder is excluded from the site) with the same front matter a post would have, minus `date`, and puts 6–8 short questions for the owner at the very top of the file inside an HTML comment (`<!-- OWNER QUESTIONS: ... -->`). The questions ask about his real use, choices and opinions on this topic (what he uses, what went wrong, what he would buy and why, what he would tell a friend). The task's summary lists those questions.
3. **Publishing a draft is done in an interactive session with the owner.** He answers the questions in Hindi; the answers are translated word for word into his simple, old-school Indian English (no fancy words), shown to him, and added only after he says yes. His answers become a big `## Our take` section (the main part of the post, not 3 lines), and the rest of the draft is cut down so that it supports his experience instead of repeating what every other site says. Then the file is moved to `_posts/YYYY-MM-DD-<slug>.md` with the real publish date. If he doesn't answer, the draft waits. Never invent or "fill in" his experience.
4. **Pick topics the owner can add something to from his own life.** He is a web and app developer in Mohali, Punjab; his phone history is on the About page (Nokia 2626, Motorola, Redmi Note 4, POCO, OnePlus 6T, and a OnePlus 9RT since January 2022). Good: buying decisions he has made, problems he has fixed, things he uses for work (laptops, chargers, phones, accessories), mistakes buyers make in India. Avoid: pure spec lists, "best X under Y" roundups with nothing personal, deal lists, products he can't say anything about.
5. **No new Launches posts and no new news posts.** Launch and news items only go into existing posts as `**Update, <Month Day>:**` notes. Pure launch/news pages are exactly the "commodity content" Google is not indexing.
6. **Global posts: at most 1 a week**, and only on a topic where the owner's answers make sense for US/UK readers (for example laptops, chargers, earbuds, apps). Rule 8 below (US-sold products only) still applies.
7. **Improve and consolidate existing posts.** When two or more posts cover nearly the same thing (for example the three Black Friday posts), propose merging them to the owner: move the useful parts into the strongest post and give the weaker ones `noindex: true` + `sitemap: false` and a one-line link to the stronger post. Never delete or rename post files and never change their dates. Old posts with no `## Our take` get owner questions too, so his answers can be added later.
8. **Honesty in public.** The site already says on /how-we-research/ that AI tools help with research and drafts. In forums, emails, bios or replies, never claim the owner wrote every word of every post. Say the posts are researched and drafted with AI help, checked by him, and the "Our take" opinions are his own.
9. **Write less, but specific.** 700–1,200 words is enough. Cut generic intros, filler and repeated spec tables. Every section should say something a reader can't get from the product page.

## Publishing pace (owner's decision, 10 Nov 2026; rule 1 replaced on 25 Nov 2026, see above)

Google indexed only 10 of ~70 pages on 10 Nov 2026 ("Crawled - currently not indexed": 58). There is no technical block; the site is new and was publishing 2–3 posts a day, many of them launch news that bigger sites already cover. From now on:

1. **(Replaced on 25 Nov 2026: at most 3 new posts a week, Mon/Wed/Fri, each with the owner's input. See the rules at the top.)** Old rule: at most ONE new post per day, counted across all tasks (morning, midday news, evening launch). Before creating a post, run `ls _posts | grep "^$(TZ=Asia/Kolkata date +%Y-%m-%d)"` (the container clock is UTC, so always use the IST date). If a post already exists for today, do NOT create another one.
2. **The morning post from `_data/content_plan.yml` is the default daily post.** Buying guides, comparisons and how-tos are the priority.
3. **Midday news task: do not create new posts.** Put the news into the most relevant existing post as an `**Update, <Month Day>:**` note (plus `last_modified_at` and `update_note` in the front matter). If there is no relevant post, skip it.
4. **Evening launch task: update first, new post only for a major launch.** First check `grep -ril "<model name>" _posts` (including China/global names of the same phone). If a post exists, add an Update note instead. A NEW launch post is allowed only for a major launch from a big brand (Apple, Samsung, Google, OnePlus, Xiaomi, Vivo, Oppo, Motorola, Realme, Nothing and similar) with official price or an officially confirmed date, AND only if no other post was published that day. If today's slot is taken, add the launch to the November upcoming-launches post as an update instead.
5. **Never post the owner's "Our take" answers yourself.** Leave the section out; the owner adds his answers later.
6. **Future-dated posts are fine.** `.github/workflows/scheduled-publish.yml` rebuilds the site every hour at :05 UTC (:35 IST), so a post with a future `date:` goes live by itself shortly after that time. Always use IST (`+0530`) in `date:`.
7. **Search Console (rule changed by the owner, 22 Nov 2026):** the interactive assistant requests indexing for each new post (URL Inspection -> Request indexing), once per URL, max ~10 a day, and logs it in seo-log.md. Scheduled tasks still don't touch Search Console, and nobody clicks "Validate fix" unless the owner asks.
8. **China-only launches: no posts; global launches: only if US buyers can buy it (owner's rule, 16 Nov 2026).**
   - A phone or gadget launched **only in China**: never write a post about it (no Launches post, no Global post). Write about it only once its India launch is officially confirmed (date or price), or once it is officially sold in the US.
   - A **global launch** (US/UK) is fine as a Global post (`category: Global`), but only for products officially sold in the US, ideally on Amazon.com, so the post can carry a `store="us"` buy button once it is on sale (Apple, Samsung, Google, Motorola, OnePlus, Nothing, Sony, Bose, Anker and similar). Skip brands that don't sell officially in the US (for example Xiaomi, Vivo, OPPO, Realme, iQOO phones); cover them only when they launch in India.
   - Global buying guides and comparisons of products already on Amazon.com earn more than launch news, so prefer those on Global days. The one-post-per-day limit still applies to everything.
9. **Category balance (owner's rule, 20 Nov 2026).** Every category in the menu should keep getting posts, not just Global and Phones. Before choosing or planning a topic (daily post with no plan entry, and the weekly topic plan), count posts per category for the last 14 days:
   `c=$(TZ=Asia/Kolkata date -d '-14 days' +%Y-%m-%d); for f in _posts/*.md; do [ "$(basename $f | cut -c1-10)" \> "$c" ] && grep -m1 '^category:' "$f"; done | sort | uniq -c | sort -n`
   - **India days rotate through the India categories with the fewest recent posts:** Laptops, Audio, Wearables, Tablets, Gaming, Accessories, Smart Home, Guides, Phones. Don't repeat a category on two India days in a row, and give each of these at least one post every two weeks.
   - **Global: at most 3 posts a week.** On Global days, vary the product type too (audio, laptops, wearables, smart home, tablets, gaming, not only phones), and set `also_in:` to the matching category so the post also shows on that category page.
   - The weekly topic plan must spread the coming week's entries in `_data/content_plan.yml` across categories this way.
10. Spend spare effort on **improving existing posts**: refresh prices, add internal links between related posts, fix outdated facts. That helps indexing more than new posts.

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
The main daily task alternates India and Global days. The launch and news tasks mostly update existing posts now (see "Publishing pace" at the top): at most one new post per day in total.

## Launch posts (category Launches)
- Only cover a launch confirmed by the brand or by at least two reliable tech news sources. Never report leaks or rumours as facts; if a detail is rumoured, say so or leave it out.
- Title format: "<Product> Launched in India: Price, Specs and Sale Date" (or "...Launching on <date>: What We Know" for confirmed upcoming launches).
- Include: official India price for each variant, launch/sale date, where to buy, launch offers, 5–8 key specs in a table, who it's for, and 1–2 close rivals at similar prices.
- 500–900 words is fine for launch posts.
- Add a buy button only once the product is actually on sale.
- Never write a post about a phone or gadget launched only in China. Global (US/UK) launches go in category Global only if the product is officially sold in the US (see "Publishing pace", rule 8).

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

## Sources box (required on every post, added Oct 2026)
Every post must list the sources its facts came from in the front matter, so the "Sources" box shows at the end of the post:
```
sources:
  - name: "Site: short article title"
    url: "https://full-link-to-the-exact-article-or-official-page"
```
- Use the exact article or official page you used (brand page, support page, official spec, or a named news article), not a homepage or a vague "rollout reports".
- Every entry needs a working `url`. Only price-list entries may go without one, written like `name: "Prices: Amazon.in and Flipkart listings, October 2026"`.
- 2–5 sources per post is normal. Evergreen guides should cite official pages (for example Apple/Google support, USB-IF, Bluetooth SIG, JEDEC).

## Owner's take
Kitek may add his own opinion to a post. Put it under a `## Our take` heading exactly as he approves it (grammar fixed only), never invented by the writer.
