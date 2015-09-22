---
layout: post
title: GitHub as academic publisher?
---

What would academic publishing technology look like if we could set it up
from scratch today?
We'd start by making HTML the primary document format instead of PDFs.
PDFs are slow, static, don't use responsive design, and get converted to web
documents anyway in modern browsers.
For mathematical notation in HTML, we can use MathJax or KaTeX:
These are JavaScript libraries that can provide numerous mathematical
symbols, equation numbering, etc. with LaTeX syntax within HTML.
We wouldn't want to write bare HTML though, we'd write in a human-friendly
plain-text document language like markdown or Asciidoc.
Markdown can be converted to HTML directly or we could add a bit more
structure and use a static site generator such as [Jekyll](https://jekyllrb.com/),
which not only converts markdown but provides templates and configuration data
for multi-webpage documents.
Academic papers are public and collaborative projects, so we could
expect each document to be hosted in a GitHub repository.
The html output of these markdown documents needs to be hosted on the web too,
and luckily GitHub [automatically](https://pages.github.com/)
builds and hosts static site repos on github.io!
Such GitHub repositories can even be assigned a [DOI](https://guides.github.com/activities/citable-code/).
Over a year ago, when I was pondering this situation, I created a
static site [starter template](https://github.com/amacfie/jekyll_site) suitable
for academic writing, including custom CSS written by designer
[Naomi Cui](http://nowme.ca).

There are some drawbacks to this approach.
An obvious one is that journals don't accept articles written in markdown or
HTML.
[Some academics](http://www.math.rutgers.edu/~zeilberg/Opinion77.html) are in a
position where they are not under pressure to publish their work in top
journals, but the majority are not.
Also, current markdown options on GitHub pages don't support bibtex,
so there's no elegant way to include references except for hyperlinks to
webpages, which may [rot](http://www.gwern.net/Archiving%20URLs#fn3).
Finally, this solution is centralized; if GitHub goes down, anything stored
there may be lost.
There is a [project](https://www.githubarchive.org/) to archive some GitHub
data.

