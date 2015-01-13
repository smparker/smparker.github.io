---
layout: page
title:  "vita"
date:   2015-01-11 15:19:00
categories: cv
---
<table cellpadding="5">
  <tr>
    <td span="2"><h1>Positions</h1></td>
  </tr>
{% for position in site.data.positions %}
  <tr>
    <td valign="top" style="white-space: nowrap;" align="right"> {{position.time}} </td>
    <td>
      <b> {{position.title}} </b> <br>
      {{position.institution}} ({{position.location}}) <br>
      Advisor: {{position.advisor}} <br>
      Interest: {{position.interest}} <br>
    </td>
  </tr>
{% endfor %}

  <tr>
    <td span="2" valign="bottom"><h1><br>Awards</h1></td>
  </tr>
{% for award in site.data.awards %}
    <tr>
      <td valign="top" style="white-space: nowrap;" align="right"> {{award.year}} </td>
      <td><i> {{award.name}} </i></td>
    </tr>
{% endfor %}

  <tr>
    <td colspan="2" valign="bottom"><h1><br>Invited Lectures</h1></td>
  </tr>
{% for lecture in site.data.lectures %}
    <tr>
      <td valign="top" style="white-space: nowrap;" align="right"> {{lecture.time}} </td>
      <td>
        {{lecture.institution}} <br>
        {{lecture.location}}
      </td>
    </tr>
{% endfor %}

  <tr>
    <td colspan="2" valign="bottom"><h1><br>Posters</h1></td>
  </tr>
{% for poster in site.data.posters %}
    <tr>
      <td valign="top" style="white-space: nowrap;" align="right"> {{poster.time}} </td>
      <td>
        <b>{{poster.title}}</b><br>
        {{poster.authors}} <br>
        presented at {{poster.event}} <br>
        {{poster.location}}
      </td>
    </tr>
{% endfor %}
</table>
