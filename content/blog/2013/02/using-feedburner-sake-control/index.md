---
nid: 2394
title: "Using FeedBurner? For the sake of control, enable MyBrand service"
slug: "using-feedburner-sake-control"
date: 2013-02-13T18:26:16+00:00
drupal:
  nid: 2394
  path: /blogs/jeff-geerling/using-feedburner-sake-control
  body_format: full_html
  redirects: []
tags:
  - dns
  - feedburner
  - feeds
  - google
  - marketing
  - url
aliases:
  - /blogs/jeff-geerling/using-feedburner-sake-control
---

We use and recommend <a href="http://feedburner.google.com/">FeedBurner</a> for RSS feed stats, podcasting, and the other helpful services it provides. However, one downside of redirecting your website's users to your FeedBurner feed is the fact that you have no control over FeedBurner's URL for your feed.

Say, for instance, you burned a feed at http://feeds.feedburner.com/midwesternmac. If, in a year or two, you need to change the shortcut, or you would like to switch back to your own feed, you can cancel your FeedBurner account, but FeedBurner will only give you 30 days during which they'll redirect their shortcut to your new feed address.

Unfortunately, a lot of people won't switch their feed reader to your new URL, and you'll be stuck with a bunch of subscribers who unwittingly abandoned your RSS feed. Additionally, any feed aggregation services like <a href="http://catholicnewslive.com/">Catholic News Live</a> won't be getting stories from your site anymore unless they manually update your URL, since there will be no redirect after 30 days.

You could simply leave the old URL/FeedBurner account intact and create a new one, but that's not very neat.

<h2>The Solution</h2>

<p style="text-align: center;">{{< figure src="./mybrand-google-feedburner.png" alt="MyBrand from Google" width="350" height="237" >}}</p>

The solution is to turn on and configure FeedBurner's free <a href="http://feedburner.google.com/fb/a/mybrand">MyBrand</a> service for your feed. What this does is allow you to use your own domain name (like http://feeds.jeffgeerling.com/midwesternmac) instead of FeedBurner's domain name, and redirect users there when they click on an RSS feed.

You simply need to add a CNAME record for the subdomain <strong>feeds</strong><em>.yourdomain.com</em> and point it at the server Google displays in your 'My Account' area in FeedBurner.

Once you've done this, you have control over the URL, and if you want to change it in the future, you can simply switch the CNAME record to a server you control, and then do your own permanent redirect. Plus, it just looks better to have your own domain for your own feed.

If you've been using FeedBurner for a long time, you can still do this now, and then hopefully when the time comes to change your URL, most of your users will be using the new URL—and for those who haven't, be sure to put up a post that warns them they're using an old URL and should update it.
