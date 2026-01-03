---
nid: 2299
title: "WYSIWYG Force Linebreaks - a Module for Input Format/WYSIWYG Zen"
slug: "wysiwyg-force-linebreaks"
date: 2011-01-11T04:29:08+00:00
drupal:
  nid: 2299
  path: /blogs/jeff-geerling/wysiwyg-force-linebreaks
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - filters
  - input formats
  - modules
  - wysiwyg
aliases:
  - /blogs/jeff-geerling/wysiwyg-force-linebreaks
---

A few months ago, I was starting to get fed up with having to manually re-patch the <a href="http://drupal.org/project/wysiwyg">WYSIWYG</a> module on about five of my sites every time it was due for an update, to incorporate functionality that I had hoped would make it into WYSIWYG as a regular button/plugin (<a href="http://drupal.org/node/513998">see issue</a>).

Well, after months of that issue's inactivity, I decided to take the bull by its horns and write up a proper module that would hook into WYSIWYG and allow me to (a) provide the functionality I needed to a wider audience, and (b) save me an extra minute of time per site upgrade (no more patches!).

Thus, <strong><a href="http://drupal.org/project/wysiwyg_linebreaks">WYSIWYG Force Linebreaks</a></strong> was born.

This module helps me with many of my sites - for many different reasons.

<ul>
	<li>On some of my sites, I had a lot of content that I had originally entered like I would any comment on drupal.org - two returns for a new paragraph, and don't use any markup (no ugly &lt;p&gt; or &lt;br /&gt;'s for me!). This created a problem when I enabled WYSIWYG with TinyMCE or CKEditor—instead of showing the content with paragraphs and line breaks, the whole node would be a jumbled mess of line after contatenated line.</li>
	<li>On some of my sites, I frequently switch between 'Full HTML' (with WYSIWYG profile) and 'Filtered HTML' or 'PHP code', and having a ton of extra tags in the markup that did nothing other than tell Drupal to make a new paragraph (when the filter system already recognizes new paragraphs using line breaks) made my inner zen off-balance.</li>
	<li>On other sites, I had to import tons of legacy content, without any proper markup, and when users would edit content in their WYSIWYG editors, all the content would be in one messy paragraph—they'd have to reformat everything.</li>
</ul>

This module fixes all these problems, and works in Drupal 6 AND Drupal 7, right now.

The image on the <a href="http://drupal.org/project/wysiwyg_linebreaks">module page</a> explains everything rather succinctly:
<p style="text-align: center;">{{< figure src="./dont-mess-up-text.png" alt="Don't let your text get messed up - wysiwyg force linebreaks" width="430" height="303" >}}</p>
