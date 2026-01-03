---
nid: 2772
title: "How to make Safari accept Google search strings in the Location bar quickly"
slug: "how-make-safari-accept-google-search-strings-location-bar-quickly"
date: 2017-05-04T02:55:04+00:00
drupal:
  nid: 2772
  path: /blog/2017/how-make-safari-accept-google-search-strings-location-bar-quickly
  body_format: markdown
  redirects: []
tags:
  - browser
  - google
  - mac
  - safari
  - search
  - tutorial
---

A few months ago, I switched to Safari after having used Google Chrome exclusively for the past four years (before that it was a mix of Safari and FireFox). Safari is lean and fast, but the one thing that _really_ bothered me was the fact that I would often try searching for something by entering keywords in the location/address bar, then hit enter, and nothing would happen.

I quickly realized that if I did this and nothing happened, I could jump back into the location bar (⌘-L), press the left arrow key to get my cursor in the beginning of the string, then hit space and enter to perform the search.

Until today, I've begrudgingly used that workaround. But then I was checking Safari's preferences to see if I might be missing something obvious, when I decided to uncheck some options and see if it made a difference. _And it did!_

{{< figure src="./search-preferences-safari.png" alt="Safari Search Preferences" width="650" height="246" class="insert-image" >}}

Through the process of elimination, I found that **unchecking "Include Safari Suggestions"** in Safari's Search preferences made the location bar search reliably, every time, the first time I entered text and hit enter.

So something in "Include Safari Suggestions" must've been timing out or finding some other way to mess up the location bar.

Something to try if you find yourself stymied by Safari's address bar functionality!
