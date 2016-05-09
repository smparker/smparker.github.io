---
layout: page
title:  notes
category: notes
date:   2016-05-08 16:24:00
header_order: 3
permalink: /notes/
---

I have collected here some general notes that might be interesting to quantum chemists.

<ul class="post-list">
  {% for post in site.notes %}
    <li>
      <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

      <h2>
        <a class="post-link" href="{{post.url | prepend: site.basurl}}">{{ post.title }}</a>
      </h2>
    </li>
  {% endfor %}
</ul>
