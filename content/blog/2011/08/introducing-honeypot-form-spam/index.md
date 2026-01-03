---
nid: 2378
title: "Introducing the Honeypot form spam protection module for Drupal"
slug: "introducing-honeypot-form-spam"
date: 2011-08-17T14:45:15+00:00
drupal:
  nid: 2378
  path: /blogs/jeff-geerling/introducing-honeypot-form-spam
  body_format: full_html
  redirects: []
tags:
  - contributions
  - drupal
  - drupal 6
  - drupal 7
  - drupal planet
  - honeypot
  - modules
---

Now that I've released a Drupal 6 backport of what I originally wrote as a Drupal 7 module, I figured I would write a little bit in the way of introducing one of the simpler, and more user-friendly ways of controlling spam in Drupal (as opposed to other also-helpful methods, like <a href="http://drupal.org/project/mollom">Mollom</a>, <a href="http://drupal.org/project/captcha">CAPTCHA</a>, etc.).

I'd like to thank <a href="http://www.flocknote.com/">Flocknote</a> for giving me the development time to work on this module, as we needed something like it for the new 'version 3' launch of www.flocknote.com.

<h3>The Honeypot Method</h3>

<a href="http://drupal.org/project/honeypot">Honeypot</a> is aptly named because, just like Pooh bear is drawn towards honey jars, spam bots are drawn towards form fields—especially form fields they think will give them the ability to link back to their own websites. So, the Honeypot method basically inserts a hidden form field to Drupal (or other) forms with a field name like 'homepage' (you can set it to whatever you want). End users don't see the field, so they don't fill it out. But spam bots (usually using prewritten scripts) do see the field (usually), and add something to it. The Honeypot module detects this and blocks the form submission if there's something in the field.

Additionally, the Honeypot module adds in a Timestamp-based deterrent. Usually, forms take at least a few seconds to fill out when a human is entering data into them—especially surveys, user registration forms, etc. Spam bots try to fill out as many forms as they can in as little time as possible, so they will often fill out a form within a couple seconds at most. The Honeypot module requires at least 5 seconds to pass (by default - you can adjust this too!) before a form can be submitted.

The Honeypot + Timestamp form protection method is a very good defense against spam bots, <del>but not against actual humans who fill out forms for spammers</del> (<strong>update</strong>: there are now some ways you can configure the module to deter 'real' spammers; see honeypot.api.php). If you start having serious spam problems, you might need to add in Mollom or another more intelligent spam prevention service to the mix. The greatest advantage of the Honeypot method is that the user is given no extra obstacles to completing a form. In my opinion, it's the most user-friendly way of preventing spam, even if it's not the most effective in every situation.

<h3>Other Niceties</h3>

You can also bypass the Honeypot protection for certain user roles—say, for instance, site administrators, who just might be able to fill out a form in less than 5 seconds—and you can set which forms on which Honeypot protection will be enabled. You can also tell Honeypot to protect all forms on the site. Finally, you can use honeypot protection in any of your own forms by simply including a little code snippet included on the module's project page.

The module is currently undergoing development, but is stable, and in use on a few Drupal 7 and Drupal 6 sites. <a href="http://drupal.org/project/honeypot">Download Honeypot for Drupal 6 or Drupal 7 »</a>

<del><em>Does anyone want to make a neat little open-sourced graphic of a honey pot that I could use on the module's home page? I want to do one myself, but just don't have the time to do illustration much ;-)</em></del>
