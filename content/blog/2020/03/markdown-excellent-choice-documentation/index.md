---
nid: 2983
title: "Markdown is an excellent choice for documentation"
slug: "markdown-excellent-choice-documentation"
date: 2020-03-24T19:21:28+00:00
drupal:
  nid: 2983
  path: /blog/2020/markdown-excellent-choice-documentation
  body_format: markdown
  redirects:
    - /blog/2020/use-markdown-documentation
aliases:
  - /blog/2020/use-markdown-documentation
tags:
  - documentation
  - markdown
  - rants
  - writing
---

Every few months, it seems a new post decrying the use of markdown for documentation (or other things) rises to the top of Hacker News.

There are often good reasons for preferring a more structured option, like [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html), [LaTeX](https://www.latex-project.org), or [Asciidoc](http://asciidoc.org). Especially in projects where more formal text is required, or where you need to support specialized and structured text formatting.

But for 98% of software projects (and in my experience, 95% of all other text I've ever written), markdown suffices, and it is truly a low barrier compared to the alternatives. It's basically plain text (which anyone can learn to write in a few seconds) with extra features.

I've written [two](https://www.ansiblefordevops.com) [books](https://www.ansibleforkubernetes.com) entirely in markdown—specifically, [LeanPub-flavored markdown](https://leanpub.com/lfm/read)—and besides plain text, it is the easiest language for general content authoring.

The fact that Markdown's lowest common denominator is 'I can write plain text,' coupled to the fact that there are very good libraries for markdown in every conceivable language, means it is the simplest way to make sure you have a basic level of maintainable documentation, no matter who contributes to your codebase. Getting people to contribute plain text changes to documentation is a heck of a lot easier than getting people to contribute in a specific format which is less popular and requires more specificity.

All 5,000+ posts on this blog are written in Markdown, and there are times when I drop back to HTML for advanced formatting. No problem. And if you want to mix LaTeX into Markdown, there are [ways to do that](https://stackoverflow.com/a/2552701/100134), too.

The truth is, the simplicity and ubiquity of Markdown is the reason it is the best choice for most projects.

It may not be as fully-featured or structured as [insert your favorite format here], but it's [_good enough_](https://news.ycombinator.com/item?id=11292670).
