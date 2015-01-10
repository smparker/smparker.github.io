---
layout: page
title:  "Publications"
date:   2015-01-08 22:58:06
categories: cv
---
{% for paper in site.data.papers %}
___{{forloop.rindex}}.___
&nbsp;&nbsp;       {{ paper.authors }},
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   _{{paper.journal}}_, __{{paper.volume}}__, {{paper.page}} ({{paper.year}})
<br> &nbsp;&nbsp;&nbsp;&nbsp;   ["{{paper.title}}"]({{paper.url}})
{% endfor %}
