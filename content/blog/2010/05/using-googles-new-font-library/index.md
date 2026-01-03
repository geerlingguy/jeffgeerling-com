---
nid: 1893
title: "Using Google's New Font Library for Headings..."
slug: "using-googles-new-font-library"
date: 2010-05-20T05:15:25+00:00
drupal:
  nid: 1893
  path: /blog/2010/using-googles-new-font-library
  body_format: full_html
  redirects: []
tags:
  - design
  - fonts
  - google
  - web development
---

<p>Today Google announced they&#39;d help advance web typography by hosting open-sourced fonts on their CDN, and by giving the code to easily embed fonts on websites on a new website, the <a href="http://code.google.com/webfonts">Google Font Directory</a>.</p>
<p>It was amazingly simple: just copy the &lt;link&gt; code and paste it in your template&#39;s header, then set any element on your page to use the Google-provided font(s). I started using <a href="http://code.google.com/webfonts/family?family=OFL+Sorts+Mill+Goudy+TT">OFL Sorts Mill Goudy TT</a>, and I like the look (except for the lower-case y, which seems to be cut off).</p>
<p>(The code simply adds an @font-face declaration via a Google-hosted CSS file... I wonder if it&#39;s legit to self-host the CSS and font file; I haven&#39;t read through the terms and conditions yet).</p>
<p>I&#39;m thinking of using this library for a few other projects on which I&#39;m working. Much easier than Typekit, and it doesn&#39;t require any javascript or flash overhead, like alternatives such as Cufon and sIFR do.</p>
