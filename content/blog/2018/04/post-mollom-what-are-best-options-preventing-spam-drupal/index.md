---
nid: 2843
title: "Post-Mollom, what are the best options for preventing spam for Drupal?"
slug: "post-mollom-what-are-best-options-preventing-spam-drupal"
date: 2018-04-23T19:14:53+00:00
drupal:
  nid: 2843
  path: /blog/2018/post-mollom-what-are-best-options-preventing-spam-drupal
  body_format: markdown
  redirects: []
tags:
  - akismet
  - captcha
  - cleantalk
  - drupal
  - drupal planet
  - honeypot
  - mollom
  - spam
---

{{< figure src="./mollom-eol-announcement-homepage.png" alt="Mollom End of Life Announcement from their homepage" width="403" height="295" class="insert-image" >}}

Earlier this month, [Mollom was officially discontinued](https://www.mollom.com/index.php?q=eol). If you still have the Mollom module installed on some of your Drupal sites, form submissions that were previously protected by Mollom will behave as if Mollom was offline completely, meaning any spam Mollom _would've_ prevented will be passed through.

For many Drupal sites, especially smaller sites that deal mostly with bot spam, there are a number of great modules that will help prevent 90% or more of all spam submissions, for example:

  - [Honeypot](https://www.drupal.org/project/honeypot): One of the most popular and effective bot spam prevention modules, and it doesn't harm the user experience for normal users (disclaimer: I maintain the Honeypot module).
  - [CAPTCHA](http://drupal.org/project/captcha) or [reCAPTCHA](http://drupal.org/project/recaptcha): Modules that use a sort of 'test' to verify a human is submitting the form. Some tradeoffs in either case, but they do a decent job of deterring bots.
  - [Antibot](https://www.drupal.org/project/antibot): An even simpler method than what Honeypot or CAPTCHA uses... but might not be adequate for some types of bot spam.

There are many other modules that use similar tricks as the above, but many modules only exist for Drupal 7 (or 8, and not 7), and many don't have the long-term track record and maintenance history that these other more popular modules have.

But there's a problem—all the above solutions are primarily for mitigating _bot_ spam, not _human_ spam. Once your Drupal site grows beyond a certain level of popularity, you'll notice more and more spam submissions coming through even if you have all the above tools installed!

This is the case with this website, JeffGeerling.com. The site has many articles which have become popular resources for all things Ansible, Drupal, photography, etc., and I get enough traffic on this site that I get somewhere between 5,000-10,000 spam comment submissions per day. Most of these are bots, and are caught by Honeypot. But 2% or so of the spam is submitted by humans, and they go right through Honeypot's bot-targeted filtering!

## Filtering Human Spam with CleanTalk

Mollom did a respectable job of cleaning up those 100 or so daily human spam submissions. A few would get through every day, but I have a custom module whipped up that shoots me an email with links to approve or deny comments, so it's not a large burden to deal with less than 10 spam submissions a day.

The day Mollom reached EOL, the number of emails started spiking to 50-100 every day... and that _was_ a large burden!

So I started looking for new solutions, fast. The first I looked into was [Akismet](https://akismet.com), ostensibly 'for Wordpress', but it works with many different CMSes via connector modules. For Drupal, there's the [AntiSpam](https://www.drupal.org/project/antispam) module, but it has no Drupal 8 release yet, so it was kind of a non-starter. The [Akismet](https://www.drupal.org/project/akismet) module has been unmaintained for years, so _that's_ a non-starter too...

Looking around at other similar services, I found [CleanTalk](https://cleantalk.org), which has an [officially-supported CleanTalk module](https://www.drupal.org/project/cleantalk) for both Drupal 7 and Drupal 8, and it checks all the boxes I needed for my site:

  - No CAPTCHAs
  - Well-maintained module for Drupal 7 and 8
  - Easy SaaS interface for managing settings (better and more featureful than Mollom or Akismet, IMO)
  - Free trial so I could see how well it worked for my site (which I used, then opted for a paid plan after 3 days)
  - Blacklist and IP-based filtering features for more advanced use cases (but only if you want to use them)

I installed CleanTalk in the first week of April, and so far have only had 5 actual human spam comment submissions make it through the CleanTalk filter; 4 of them were marked as 'possible spam', and one was approved (there's a setting in the module to auto-approve comments that look legit, or have all comments go into an approval queue using Drupal's built-in comment approval system).

So CleanTalk worked better than Mollom did, and it was a little simpler to get up and running. The one tradeoff is that CleanTalk's Drupal module isn't quite as 'Drupally' as Mollom or Honeypot. By that, I mean it's not built to be a flexible "turn this on for any kind of form on your site" solution, but it's more tailored for things like:

  - Drupal comments and comment entities
  - User registration
  - Webform

To be fair, those are probably the top three use cases for spam prevention—but as of right now, CleanTalk can't easily be made to work with generic entity submissions (e.g. forum nodes, custom node types, etc.), so it works best on sites with simpler needs.

CleanTalk's [pricing](https://cleantalk.org/price) is pretty simple (and IMO pretty cheap) too: for one website, it's currently $8/year, or cheaper if you pay for multiple years in advance.

> **Disclaimer**: CleanTalk offers a free year of service for those who post a review of CleanTalk on their websites, and I'll probably take them up on that offer... but I had actually written the first draft of this blog post over a month ago, before I found out about this offer, when I was initially investigating using CleanTalk for my DrupalCon Nashville session submission [Mollom is gone. Now what?](https://events.drupal.org/nashville2018/sessions/mollom-gone-now-what). I would still write the review exactly the same with or without their offer—it's been _that_ good in my testing! Heck, I already paid for 3 years of service!

## Summary

If you have a Drupal site and are disappointed by the uptick in user registration, webform, and comment spam since Mollom's end of life, check out CleanTalk for a potentially better solution!

> **Edit**: Also see some excellent suggestions and ongoing work in integrating other spam prevention services into Drupal in the comments below!
