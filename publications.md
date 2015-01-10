---
layout: page
title:  "Publications"
date:   2015-01-08 22:58:06
categories: cv
---
{% for paper in site.data.papers %}
   ___{{forloop.rindex}}.___   {{ paper.authors }}, _{{paper.journal}}_, __{{paper.volume}}__, {{paper.page}} ({{paper.year}})
     [["{{paper.title}}"|{{paper.url}}]]
{% endfor %}
