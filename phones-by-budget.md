---
layout: page
title: "Best Phones by Budget in India (November 2026)"
seo_title: "Best Phones by Budget in India"
permalink: /phones-by-budget/
description: "Every phone in our Phone Finder, sorted by budget from under ₹15,000 to over ₹1 lakh, with chip, battery and camera at a glance, plus our buying guides."
noindex: true
sitemap: false
---
{% assign pf = site.data.phone_finder %}
Looking for a new phone? This page lists every phone we track, sorted by budget, with the specs that matter most. Prices are what we saw on Amazon and Flipkart in **{{ pf.updated }}**, and they change often, so check the live price before you buy.

> **Not sure where to start?** Take our free [Phone Finder quiz](/phone-finder/). Answer 4 questions about your budget and what you care about, and it ranks these phones for you.

**Jump to:** [Under ₹15,000](#under-15000) · [₹15,000–₹20,000](#15000-20000) · [₹20,000–₹30,000](#20000-30000) · [₹30,000–₹40,000](#30000-40000) · [₹40,000–₹60,000](#40000-60000) · [₹60,000–₹1 lakh](#60000-100000) · [Above ₹1 lakh](#above-100000)

{% assign bands = "under-15000|Under ₹15,000|0|14999;15000-20000|₹15,000–₹20,000|15000|19999;20000-30000|₹20,000–₹30,000|20000|29999;30000-40000|₹30,000–₹40,000|30000|39999;40000-60000|₹40,000–₹60,000|40000|59999;60000-100000|₹60,000–₹1 lakh|60000|99999;above-100000|Above ₹1 lakh|100000|9999999" | split: ";" %}
{% assign sorted = pf.phones | sort: "price" %}
{% for b in bands %}{% assign f = b | split: "|" %}{% assign lo = f[2] | plus: 0 %}{% assign hi = f[3] | plus: 0 %}
<h2 id="{{ f[0] }}">{{ f[1] }}</h2>
<div class="table-wrap"><table>
<thead><tr><th>Phone</th><th>Price*</th><th>Chip</th><th>Battery</th><th>Camera</th></tr></thead>
<tbody>
{% for p in sorted %}{% if p.price >= lo and p.price <= hi %}<tr><td><strong>{% if p.post %}<a href="{{ p.post }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</strong></td><td>{% include inr.html n=p.price %}</td><td>{{ p.chip }}</td><td>{% if p.mah %}{{ p.mah }}mAh, {{ p.charge }}{% else %}{{ p.charge }}{% endif %}</td><td>{{ p.cam }}</td></tr>
{% endif %}{% endfor %}</tbody></table></div>
{% endfor %}

<p class="muted">*Around the lowest price we saw for the base variant in {{ pf.updated }}. Bank offers not included.</p>

## Our phone buying guides

- [How to Choose a Smartphone Under ₹20,000](/how-to-choose-a-smartphone-under-20000/)
- [Best Gaming Phones Under ₹30,000](/best-gaming-phones-under-30000/)
- [Pixel 10a vs iPhone 17e](/pixel-10a-vs-iphone-17e/)
- [Upcoming Phones Launching in India in November 2026](/upcoming-phones-launching-india-november-2026/)

## Before and after you buy

- [How to Check a New Phone Is Genuine Before Accepting Delivery](/check-new-phone-genuine-before-accepting-delivery/)
- [How to Sell Your Old Phone Safely in India](/sell-old-phone-safely-india-steps/)
- [12 Simple Ways to Make Your Phone Battery Last Longer](/make-phone-battery-last-longer/)
- [How to Improve Gaming Performance on Your Android Phone](/improve-gaming-performance-android-phone/)

Want a printable version? Sign up for our weekly newsletter at the bottom of this page and get our free 25-point phone buying checklist (PDF).
