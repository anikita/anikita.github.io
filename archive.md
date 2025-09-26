---
layout: default
title: "All Posts"
permalink: /archive/
---

# All Posts

A complete archive of all blog posts, sorted by publication date.

---

{% for post in site.posts %}
## [{{ post.title }}]({{ post.url }})

**{{ post.date | date: "%B %d, %Y" }}**

{{ post.excerpt }}

**[Read the full post →]({{ post.url }})**

---

{% endfor %}

---

*Back to [home]({{ "/" | relative_url }})*
