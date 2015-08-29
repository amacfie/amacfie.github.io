---
layout: page
title: Archive
---

<ul>
{% for post in site.posts %}
      <li>
      {{ post.date | date: "%Y.%b.%d" }} &raquo;
      <a href="{{ post.url }}">  {{ post.title }} </a>
      {{ post.excerpt }}
      <p id="ellipsis"> &hellip;</p>
    </li>
{% endfor %}
</ul>
