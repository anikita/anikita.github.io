---
layout: default
title: Home
---

{% include custom-header.html %}

# Welcome to Antonis Nikitakis Personal Blog

Hello! This is a self-reflective, philosophical view of my world.. with a bit of cynicism.

Who am I?
[LinkedIn](https://www.linkedin.com/in/antonis-nikitakis-62544120/)

## Disclaimer

⚠️ About Content Creation: The articles on this blog are developed through an iterative procedure that combines a multi-step Large Language Models (LLMs) process with human (my) oversight and refinement. Given the broad scientific and philosophical scope of topics covered, it is impossible for me to fact-check every detail comprehensively. Therefore, mistakes or inaccuracies may be present. Please read with a critical eye and consider cross-referencing important information from authoritative sources.

For me, the articles serve mostly as a conversation with myself.

For the reader, what I would like the takeaway from each piece to be is the core philosophical argument. The details may be less polished from time to time, but that's what it is.

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
