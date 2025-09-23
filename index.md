---
layout: default
title: Home
---

# Welcome to Antonis Nikitakis Personal Blog

Hello! This is my personal blog built with GitHub Pages.

## Latest Posts

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url }})
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more...]({{ post.url }})

---

{% endfor %}

## About

This blog is where I share my thoughts, experiences, and discoveries. Topics include technology, programming, and personal projects.

Stay tuned for more content!

---

*Built with Jekyll and hosted on GitHub Pages*
