---
layout: page
title: Archive
---

## Blog Posts

<ul>
{% for post in site.posts %}
      <li>
      {{ post.date | date_to_string }} &raquo; 
      <a href="{{ post.url }}">  {{ post.title }} </a>
{{ post.excerpt }}
    </li>
{% endfor %}
</ul>
