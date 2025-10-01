---
layout: default
title: Home
---

{% include custom-header.html %}

# Welcome to Antonis Nikitakis Personal Blog

Hello! This is a self-reflective, philosophical view of my world.. with a bit of cynicism.

Who am I?
[LinkedIn](https://www.linkedin.com/in/antonis-nikitakis-62544120/)

## Important Disclaimer

⚠️ **About Content Creation**: The articles on this blog are developed through an iterative process that combines Large Language Models (LLMs) with extensive human (my) oversight and refinement. Given the broad scientific and philosophical scope of topics covered, it is impossible for me to fact-check every detail comprehensively. Therefore, **mistakes or inaccuracies may be present**. Please read with a critical eye and consider cross-referencing important information from authoritative sources.

## Latest Posts

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url }})
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more...]({{ post.url }})

---

{% endfor %}

## View All Posts

**[View all posts →]({{ "/archive/" | relative_url }})**

## About

This blog is where I share my thoughts, experiences, and discoveries. Topics include technology, philosophy and society.

Stay tuned for more content!

{% include custom-footer.html %}
