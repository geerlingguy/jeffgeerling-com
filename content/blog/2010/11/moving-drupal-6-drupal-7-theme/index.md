---
nid: 2294
title: "Moving from Drupal 6 to Drupal 7 - A Themer's Perspective"
slug: "moving-drupal-6-drupal-7-theme"
date: 2010-11-18T06:25:25+00:00
drupal:
  nid: 2294
  path: /blogs/jeff-geerling/moving-drupal-6-drupal-7-theme
  body_format: full_html
  redirects: []
tags:
  - design
  - drupal
  - drupal 7
  - drupal planet
  - theming
aliases:
  - /blogs/jeff-geerling/moving-drupal-6-drupal-7-theme
---

<p>The transition from Drupal 6 to Drupal 7 has taken a bit of time, and I (like many others) simply haven't had enough time in the past few months to do D7 testing while in the midst of tens of other D6 projects.</p>
<p>I've committed, though, to building out three Drupal sites in Drupal 7, now that we're at beta-3, and I will be posting a few reflections, mostly from a themer's perspective on some changes—the good, the bad, and the confusing.</p>
<h2>A New Default Theme - Bartik</h2>
<p>Just like Drupal 5/6's default theme, Garland (which is in use on this site right now :-/), Bartik will be seen on thousands of quickly-built sites around the web, and I think the theme is robust enough for this purpose. I'm actually building one site's theme directly on top of Bartik, just modifying CSS through a single stylesheet added by a custom module.</p>
<p>But it's nothing amazing, in my opinion. I think it would've been awesome to have some sort of dropdown menu support in core by this point—but it looks like <a href="http://drupal.org/node/777930">that will wait until Drupal 8 at least</a>. This is probably the number one most requested feature I get on a lot of the smaller sites I'm asked to build, and having the feature in core would be über-cool.</p>
<!--break-->
<h2>API Changes Everywhere</h2>
<p>Developers have a large set of API changes that they'll need to discover and learn anew, such as the DBTNG changes, file handling changes, etc... but themers also have a few changes to contend with.</p>
<p>Two quick ones that I encounter on most sites are:</p>
<!--break-->
<p><strong><a href="http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_set_html_head/6">drupal_set_html_head()</a> --&gt; has been changed to <a href="http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_add_html_head/7">drupal_add_html_head()</a></strong></p>
<p>What used to be a simple "fill in the first argument with the code you'd like to output in the &lt;head&gt; section of your page" has now turned into a somewhat more complicated, but ultimately more flexible and 'hook-into-able' affair. You need to feed the HTML into drupal_add_html_head() as an array. See the docs page linked above for more info (and see, specifically, <a href="http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_add_html_head/7#comment-8429">the comment I added to that page</a>.</p>
<p><strong><a href="http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_add_css/7">drupal_add_css()</a> gets simpler, more complex</strong></p>
<p>In Drupal 6, you could throw a quick CSS file at drupal_add_css(), along with a couple other simple arguments to define what kind of stylesheet they've added. In Drupal 7, you can do all of this, but in a somewhat more robust way. There are some nice new options, like telling drupal you'd like the stylesheet to load for every page, or setting a weight for your CSS so you can have it appear lower in the list (to override other stylesheets, for instance).</p>
<p>Also, you can now call drupal_static_reset('drupal_add_css'); to quickly wipe out all other stylesheets added before yours. This can be nice for debugging purposes, or if you just want to simplify to one stylesheet that you (or your module) provide(s).</p>
<p>These are just two of the functions I interact with on a regular basis that will be a bit different and afford more flexibility. What are some of your favorites / most often used?</p>
