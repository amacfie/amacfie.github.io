---
layout: post
title: GitHub as academic publisher? (Part 2)
---

[A follow up of [part 1](http://amacfie.github.io/2015/09/22/github-publishing/)]

Pandoc is a markdown converter that isn't supported by GitHub Pages but has
a lot of useful features for academic writing such as bibtex support.
Pandoc also converts markdown to LaTeX so it's a good solution if you have
to build PDF "releases" of your documents for some reason.
Multiple people have reported writing theses in Pandoc.

It turns out
[Travis CI can be used](http://eshepelyuk.github.io/2014/10/28/automate-github-pages-travisci.html)
to allow Pandoc or any other converter to generate GitHub pages.
And Pandoc can run quite well
[without a static site generator like Jekyll](http://www.carlboettiger.info/2014/10/28/jekyll-free.html).
I made a small test site with Pandoc on GitHub
[here](https://github.com/amacfie/ci_pandoc_test).

