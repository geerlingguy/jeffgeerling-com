---
nid: 2381
title: "Questions about Wordpress"
slug: "questions-about-wordpress"
date: 2012-09-28T03:54:55+00:00
drupal:
  nid: 2381
  path: /blogs/jeff-geerling/questions-about-wordpress
  body_format: filtered_html
  redirects: []
tags:
  - cms
  - development
  - dx
  - plugin
  - wordpress
aliases:
  - /blogs/jeff-geerling/questions-about-wordpress
---

Having been away from the WordPress scene since version 2.x days (I think the last time I launched a WordPress website was around 2009), I recently had reason to develop some WordPress plugins, and I wanted to ask some questions about the WordPress coding standards and API that I hope will help enlighten me (and, maybe, other PHP developers coming from other frameworks/platforms to WordPress).

Here are some questions I've had while working on my first WordPress plugin (coming purely from the development side—I'm deliberately ignoring any mention of WordPress's UI, as I don't want to inspire any trolling along the lines of 'WordPress vs. [Another CMS]'):

<ul>
<li>Is it really necessary to mix HTML and PHP all over the place (especially with forms), or are there any documented ways to use templating and preprocessing functions so I can separate my markup from my code?</li>
<li>Is there anything like Drupal's Form API? Writing all the form HTML (not to mention form validation, and layout) by hand is tedious.</li>
<li>Is it recommended that PHP files include a closing tag? I found a lot of files that did this, but in almost every other system I've used, this is highly discouraged, as it introduces extra whitespace (and other unforeseen consequences) if you end your files with an extra line (as many do).</li>
<li>Is it okay to not include a bunch of space around logical statements and array/function parameters <code>like( 'so' );</code> and <code>if ( ! empty( $title ) )</code>, or is that a strict rule in WordPress's coding standards.</li>
<li>According to the Coding Standards doc, it's okay to have a one-line if statement without brackets—in all my experience, in every language (except Python, of course), experience has taught me this is one of the worst ideas <em>ever</em>. Is this an anachronism, or is it actually recommended? Some parts of the Codex contain examples of this strange and never-recommended if statement syntax.</li>
<li>For a new contributor, where should I start? I'd like to get some code up on WordPress.org and start figuring out how bug tracking, versioning, and plugin development works, but there's nothing like Drupal.org's developer sandboxes that I've found yet.</li>
</ul>

I have some thoughts about other odd conventions, like method, class, and parameter naming, but I can understand simple style differences there and in some other areas. The main questions I have (above) are not meant to denigrate WordPress or anything like that, I'm just wondering (a) what the rationale is behind some of those coding standards/conventions, and (b) if I'm just seeing outdated documentation in the Codex, API, and other sites...

[Edit: I've also posted a question with some more detail on the WordPress.org forums: <a href="http://wordpress.org/support/topic/wordpress-development-coming-from-drupal">WordPress Development (Coming from Drupal)</a>].
