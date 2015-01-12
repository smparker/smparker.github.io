---
layout: page
title:  "vita"
date:   2015-01-11 15:19:00
categories: cv
---
### Positions
{% for position in site.data.positions %}
- _{{position.title}}_ <br>
  {{position.institution}} ({{position.location}}) <br>
  Advisor: {{position.advisor}} <br>
  Interest: {{position.interest}} <br>
  {{position.time}}
{% endfor %}

### Awards
{% for award in site.data.awards %}
 - _{{award.name}}_ ({{award.year}})
{% endfor %}
