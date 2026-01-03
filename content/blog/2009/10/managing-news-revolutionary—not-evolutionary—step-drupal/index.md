---
nid: 2257
title: "Managing News - Revolutionary\u2014not Evolutionary\u2014Step for Drupal"
slug: "managing-news-revolutionary\u2014not-evolutionary\u2014step-drupal"
date: 2009-10-23T04:58:15+00:00
drupal:
  nid: 2257
  path: /blogs/geerlingguy/managing-news-revolutionary—not-evolutionary—step-drupal
  body_format: full_html
  redirects: []
tags:
  - aggregation
  - drupal
  - feeds
  - managing news
aliases:
  - /blogs/geerlingguy/managing-news-revolutionary—not-evolutionary—step-drupal
---

<p>I noticed a post from the excellent folks over at <a href="http://developmentseed.org/">Development Seed</a> in the drupal.org Planet feed on a new Drupal installation profile they've been working on called <a href="http://managingnews.com/">Managing News</a>. Having tried (and loved) their Drupal-based installation of <a href="http://openatrium.com/">Open Atrium</a> (a great package for quick Intranets), I had pretty high expectations.</p>
<p>Those expectations were pretty much blown out of the water; this install profile basically sets up a Drupal site (with all the Drupal bells and whistles) that is focused on one thing, and does it well: <strong>news aggregation via feeds</strong> (Atom, RSS).</p>
<p class="rtecenter"><a href="http://catholicnewslive.com/">{{< figure src="./catholic-news-live-screenshot.jpg" alt="Catholic News Live.com - Catholic News Aggregator" width="450" height="351" class="noborder" >}}</a></p>
<p>I decided to quickly build out an aggregation site, <a href="http://catholicnewslive.com/">Catholic News Live</a>. The site took about 4 hours to set up, and it's already relatively customized to my needs. One thing I still don't know about is whether Drupal's cron will be able to handle the site after a few months and a few hundred more feeds... but we'll see!</p>
<!--break-->
<h4>How does it work?</h4>
<p>Managing News uses a few nice new modules to get most of it's work done. The excellent, and almost-brand-new, feeds module enlivens the feed aggregation (I've used FeedAPI, Feed Element Mapper, etc. before, but they were kind of a mess to use). The context, features, and extra 'mn' modules provide a lot of the layout and functionality for the site.</p>
<p>To add a feed, you simply click the 'Add feed' button while logged in. To add a channel, go to the channels page (or click on the 'active channel' button on the bottom right) and click 'Add channel.' The maps page and block is automagically location-aware, and updates itself whenever new stories are posted. It's pretty accurate, to boot!</p>
<h4>Revolutionary Step for Drupal</h4>
<p>Why would I say this is 'revolutionary'? Well, basically, Managing News, along with other install profiles (like Open Atrium) will open up Drupal, unwittingly, to thousands of people who need quick, turnkey solutions to different problems on the web. The more install profiles, the better for Drupal, imo. Who will make a Flickr-like install profile? A forum profile? Etc.</p>
<p>Drupal is slowly but surely reaching critical mass, imo.</p>
<h4>Conclusion</h4>
<p>When something works so well and so easily, you'd think it's an Apple product! I wonder, sometimes, if Development Seed is a secret project of Steve Jobs ;-)</p>
<p>For now, go ahead and download Managing News, install it (just like you would Drupal), and have fun! There's a lot of promise for install profiles in Drupal 7, if Development Seed's work is any indication.</p>
