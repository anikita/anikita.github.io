---
layout: default
title: Home
---

# Welcome to Antonis Nikitakis Personal Blog

Hello! This is a self-reflective, philosophical view of my world.. with a bit of cynicism.

Who am I?
LinkedIn: https://www.linkedin.com/in/antonis-nikitakis-62544120/

## Latest Posts

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url }})
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more...]({{ post.url }})

---

{% endfor %}

**[View all posts →]({{ "/archive/" | relative_url }})**

## About

This blog is where I share my thoughts, experiences, and discoveries. Topics include technology, programming, and personal projects.

Stay tuned for more content!

---

*Built with Jekyll and hosted on GitHub Pages*
