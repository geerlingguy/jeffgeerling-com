---
nid: 2883
title: "Jeff Geerling.com now supports Dark Mode in macOS 10.14"
slug: "jeff-geerlingcom-now-supports-dark-mode-macos-1014"
date: 2018-10-25T19:08:53+00:00
drupal:
  nid: 2883
  path: /blog/2018/jeff-geerlingcom-now-supports-dark-mode-macos-1014
  body_format: markdown
  redirects: []
tags:
  - css
  - dark mode
  - design
  - night
  - safari
  - webkit
  - website
---

Over the years my site has evolved quite a bit; I started this site (well, one form of it at least) around 2004, when table based web design was still a thing. I've evolved the design from table-based to CSS, to semantic CSS, to CSS + RDF, then to mobile-first... and now that macOS 10.14 Mojave is here, with a snazzy (and _way_ easier on my eyes) dark mode, I have made the design work well in both normal (light) and dark mode on macOS.

It's using a new feature in the [Webkit](https://webkit.org) nightly builds (er, now called [Safari Technology Preview](https://developer.apple.com/safari/download/)), a media query named (at least, for now) `prefers-color-scheme`.

And here's how the site looks when you're using Safari Technology Preview 68+ in macOS Mojave with Dark Mode:

{{< figure src="./jeff-geerling-dark-mode.png" alt="Jeff Geerling.com in dark mode on macOS Mojave" width="650" height="513" class="insert-image" >}}

It was pretty easy to add—just check out my [dark-mode.css](https://www.jeffgeerling.com/sites/jeffgeerling.com/themes/jeffgeerling/css/dark-mode.css) file. At its simplest, I started with:

```
@media (prefers-color-scheme: dark) {
  body {
    color: #ddd;
    background-color: #222;
  }
}
```

But you can also default everything to a dark theme, then use the inverse query (`prefers-color-scheme: light`). There is a [W3C proposal](https://drafts.csswg.org/mediaqueries-5/#prefers-color-scheme) to make this new media query a standard adopted by all browsers—hopefully it gets adopted soon!

The key to using this setting _well_ is being thorough in testing future color changes I make to the theme. Any change should be tested in both light and dark mode. If I don't test every element, every hover, every click, etc., I might make some elements unreadable or harder to use when changing colors between light and dark mode!

See Webkit.org's [Release Notes for Safari Technology Preview 68](https://webkit.org/blog/8475/release-notes-for-safari-technology-preview-68/) for more details on Safari's implementation.
