---
nid: 67
title: "Building a Theme for Drupal 7"
slug: "building-a-theme-drupal-7"
date: 2010-01-15T21:45:05+00:00
drupal:
  nid: 67
  path: /articles/web-design/building-a-theme-drupal-7
  body_format: full_html
  redirects: []
tags:
  - articles
  - css
  - design
  - drupal
  - drupal planet
  - html
  - php
  - theming
aliases:
  - /articles/web-design/building-a-theme-drupal-7
---

After having built out many themes for Drupal 6 (and a couple for Drupal 5), I'm going to start from scratch on a couple designs and build a theme in Drupal 7, which will be released sometime in 2010. I'll take you along my journey in this article.

Please note, <em>this article is a work in progress</em>, and I'll be updating it as I go. Hopefully, within a couple weeks, I'll have the article complete, and a nice new theme to release on Drupal.org (maybe), only for Drupal 7.

To get things kicked off, here are a few articles that have good background information on Drupal 7 theming:

<ul>
	<li><a href="http://www.midwesternmac.com/blogs/jeff-geerling/state-drupal-themes">On the State of Drupal Themes and Theming</a></li>
	<li><a href="http://drupal.org/node/394612">Create a CSS-only Theme</a></li>
	<li><a href="http://www.midwesternmac.com/blogs/geerlingguy/closer-ever-closer-pure-css-bliss-drupal">Closer, Ever Closer, to Pure-CSS Bliss in Drupal</a></li>
	<li><a href="http://drupal.org/documentation/theme">Drupal Theming Guide</a></li>
</ul>

<h3>Building the Site (Step 1)</h3>

With Drupal 7, you get a new, easier to use installer, and a much nicer administrative interface than Drupal 6/5/4/etc. The admin interface uses a new theme, <a href="http://drupal.org/project/seven">Seven</a>, which is pretty nice on its own (almost good enough that I might build a quick blog-style site using that theme). Additionally, the Bartik theme included with core is good enough to stand on its own, maybe with a few tweaks here or there (for instance, I designed <a href="http://www.hardonsj.org/">hardonsj.org</a> from Bartik with only a few custom rules in an additional stylesheet I added).

I set up a test Drupal 7 installation on my Hot Drupal hosting account (same account on which this site is currently running), and went through the preliminaries; setting up a few user accounts, using <a href="http://drupal.org/project/devel">Devel</a> to generate some test content, and moving around some blocks.

<h3>Structuring Your Theme (Step 2)</h3>

Next, I followed the directions I wrote up in the Drupal.org Handbooks, outlining <a href="http://drupal.org/node/394612">how to create a CSS-only Theme for Drupal</a>. Basically, create a folder in sites/<em>sitename</em>/themes with your theme name, then an .info file inside that folder to describe the theme to Drupal, and then make some CSS stylesheets to insert your own styles (I typically try to stick to one or two stylesheets, but you can add as many as you want*).

Here's what your file structure should look like (something like this):

<p class="rtecenter">{{< figure src="./filesystem-layout-theme-d7.png" alt="Filesystem layout for a Simple Drupal 7 Theme" class="blog-image" >}}</p>

Note that your theme's .info file name (before the .info part) and folder name must match exactly. Additionally, they should only use lowercase letters, and the only allowed character, other than a-z, is an underscore (_).

My theme's name will be 'simple_css' (short name), and so I name my theme's folder 'simple_css', and the .info file 'simple_css.info'. I have placed the simple_css folder into my /sites/all/ folder so that all my Drupal 7 sites can see it when I go to administer the site's appearance.

<h3>Telling Drupal About Your Theme (Step 3)</h3>

Before Drupal can recognize your theme appropriately, you'll need to enter a little metadata into your theme's .info file. You'll need to tell Drupal your theme's name, give it a description, and add in a few other options (I'll describe everything below).

simple_css.info (file contents):


```
name = Simple CSS
description = This is a simple CSS theme for Drupal.
core = 7.x
stylesheets[all][] = style.css
```

The lines should be pretty self-explanatory. You need to include the 'core' line so Drupal knows this theme will work with Drupal 7, and you need to tell Drupal that you'd like to use your 'style.css' stylesheet for all media.

<h3>Designing/Theming – A.K.A. Being Creative</h3>

The rest is really up to you! You should probably have a baseline of styles for your theme so the structure of the site is laid out correctly. I've included a few styles that I typically begin using for my Drupal 7 sites, but don't let them limit you. Drupal's core HTML output is well-structured quite versatile—the Drupal 7 community worked hard to make it that way!

First, let's take a look at what we have so far. Enable your theme by visiting the admin/appearance page (click 'Appearance' in the top menu), and set it as the default. Go to your site's home page, and it will probably look something like this:

<p class="rtecenter">{{< figure src="./screen-picture-unthemed-drupal.png" alt="Naked and Unstyled Drupal 7 HTML" width="575" height="458" class="blog-image" >}}</p>

Obviously, unless you're participating in <a href="http://naked.dustindiaz.com/">CSS Naked Day</a>, you'll want to re-style that page! You should at least style things like headings, menus, blocks, and tabs.

<h4>Tips and Inspiration for Theming &amp; Creativity</h4>

Here are a few different tips and tidbits from my creative design process that might help you in your own process:

<ul>
	<li>Need to find a class, element tag, or ID for something on the page that you'd like to style? If you're not already, you need to use FireFox, Safari, or Chrome. If you use FireFox, download the <a href="http://getfirebug.com/">Firebug</a> extension. If you use Safari or Chrome, the tool's built in... just right click on anything on the page, and click 'Inspect Element.'</li>
	<li>Looking for inspiration? Search Google for '<a href="http://www.google.com/search?q=great%20css%20designs">great CSS designs</a>' or '<a href="http://www.google.com/search?q=top%20website%20designs%202010">top website designs &lt;current year&gt;</a>' - if nothing else, you can find a few striking elements for your inspiration. Of course, there will be a ton of duds in there, too... I just sometimes need a spark of inspiration for colors, navigation styles, etc.</li>
	<li>Speaking of colors... I use the <a href="http://www.nikhef.nl/pub/computing/WebColors.php">RGB/Hexadecimal Color Chart</a> from nikhef.nl extensively, just because of its elegant simplity, and I use <a href="http://colorschemedesigner.com/">Color Scheme Designer</a> to try out some palettes, based on a specific color I choose for my design.</li>
</ul>

You can build out some pretty awesome themes using nothing but CSS. Include a few images here and there (as CSS backgrounds or <a href="http://www.alistapart.com/articles/sprites">sprites</a>, of course!), and you have some top-notch designs.

<h3>Adding a Screenshot</h3>

To add a screenshot of your theme, so Drupal will display it when you're on the Appearance administration page (instead of a boring "no screenshot" white space), simply take a screenshot of your theme in a browser (preferably after it's been completed), and resize/crop it to 294px x 219px, and save it as a png. Name the file "screenshot.png" and put it in the same folder as your .info file.

<h3>Further Steps</h3>

In light of all this, you'll probably have to go a bit deeper at some point, if you have special requirements or need to change the actual HTML that you are theming.

Luckily, Drupal makes all of this very easy.

You can add a file called 'template.php' and hook into Drupal's rendering processes to change variables, change the way things like lists and tables are printed, add a class to a page, a block, or a specific piece of content, and do many other powerful things.

One thing I often do when making a 'responsive' design (one that works well on mobile phones, tablets, and desktop browsers) is use <a href="http://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_page_alter/7">hook_page_alter()</a> to add in a special meta tag. See:&nbsp;<a href="http://www.midwesternmac.com/blogs/jeff-geerling/making-your-current-drupal">Making your current Drupal theme responsive, simply</a>.

Another thing I do quite often is override a specific template, for example, node.tpl.php, to change the default markup for my site (sometimes I like having an extra wrapper div around a specific piece of content, or I need to change the order of elements on a page). To do this, just find the template file (common ones are present for comments, nodes, pages, user profiles, etc.) you need in drupal's core modules directory, and make a copy in your theme's folder. Then clear all of Drupal caches, and your own copy of the template will start being used instead. Read more about <a href="http://drupal.org/node/173880">overriding theme functions and templates</a>.

For more reading, and a vast array of information about Drupal 7 Theming, please visit and read through the <a href="http://drupal.org/documentation/theme">Drupal Theming Guide</a> handbook on drupal.org.
