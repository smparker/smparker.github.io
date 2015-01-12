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

### Invited Lectures
{% for lecture in site.data.lectures %}
  - {{lecture.institution}} <br>
    {{lecture.location}} <br>
    {{lecture.time}}
{% endfor %}

### Posters
{% for poster in site.data.posters %}
  - _{{poster.title}}_ <br>
    {{poster.authors}} <br>
    presented at {{poster.event}} <br>
    {{poster.location}}
    ({{poster.time}})
{% endfor %}
