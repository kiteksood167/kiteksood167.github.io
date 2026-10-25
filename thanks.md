---
layout: page
title: Almost done! Check your inbox
permalink: /thanks/
description: Confirm your GadgetGyaan newsletter subscription.
noindex: true
sitemap: false
---
Thanks for subscribing to the GadgetGyaan newsletter.

**One last step:** we've sent you a confirmation email. Open it and click the confirm button to start getting our weekly email. If you can't find it in a couple of minutes, check your Spam or Promotions folder.

While you wait, here's what's new on the blog:

<ul>
{% for p in site.posts limit: 5 %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}</ul>
