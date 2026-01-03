---
nid: 2549
title: "Should I disable PHP warnings and notices?"
slug: "should-i-disable-php-warnings-and-notices"
date: 2016-08-07T19:52:08+00:00
drupal:
  nid: 2549
  path: /blog/2016/should-i-disable-php-warnings-and-notices
  body_format: markdown
  redirects: []
tags:
  - coding
  - debugging
  - development
  - drupal
  - php
---

> This is a reposting of what I wrote on the Acquia Dev Center blog in 2016, [Should I disable PHP warnings and notices?](https://dev.acquia.com/blog/-should-i-disable-php-warnings-and-notices/30/06/2016/15786).

<p style="text-align: center;">{{< figure src="./array-to-string-conversion-errors-drupal-shrink.png" alt="Drupal onscreen logged PHP error messages and warnings" width="550" height="270" class="insert-image" >}}</p>

Many developers who work on Drupal (or other web/PHP) projects have error reporting disabled in their local or shared dev environments, for a variety of reasons—some don't know how to enable it, some are annoyed by the frequency of notices, warnings, and errors, and some don't like to be reminded of how many errors are logged!

There are a few important reasons you should make sure to [show all errors when developing](https://www.drupal.org/node/1056468), though:

  - When there's a major issue on your production site, you will need to go into the logs and look for clues as to what's going wrong. And when you do, the fewer 'noisy' log messages you have, the better.
  - At a certain level, the volume of messages being logged will [harm your site's performance](http://2bits.com/drupal/avoid-excessive-disk-writes-avoiding-php-errors-your-code.html) (even if you're using syslog instead of database logging!). I've heard of cases where page load performance was 1.5x or 2x slower due simply to the volume of logged PHP messages!
  - Some of the most pernicious bugs are those related to variables not being instantiated, objects being accessed as arrays, etc.—all things that are explicitly logged as notices and warnings (but won't break a site).
  - Notices and warnings help you to identify areas of your site where your PHP code style might be wanting, and you should start using [PHP CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) or [PHP Mess Detector](https://phpmd.org/) to help improve the quality of your code.
  - One of the easiest ways to see if a contributed module is up to snuff is to enable it and make sure no new notices/warnings/errors start popping up all over your site.

Unfortunately, for many Drupal sites, the damage is already done, and if you wade into the system logs or the watchdog log, you'll find dozens or even hundreds of errors _for every page request_. Or, worse, you'll find that the site administrators _completely disabled logging_ because the volume of errors caused severe performance issues.

## What NOT to do

If you're doing any of these things, change these things immediately to start making your site better!

  - **Don't [silence PHP errors](http://drupal.stackexchange.com/q/15415)** — on production, tell Drupal to not log message to the screen, but at least log them in either syslog or the database (syslog preferred for performance reasons—plus it integrates with Acquia Cloud logs and tools like ELK or SumoLogic).
  - **Don't use `@` to silence PHP errors** (see [should I use @ to hide errors in PHP?](http://www.reddit.com/r/PHP/comments/1w7cc7/is_that_bad_to_use_to_hide_errors_in_php/cezcrgv)) — you're just masking a problem; instead fix it when you discover it.
  - **Don't turn off all error logging** — some people disable error logging entirely, on dev, local, and production. This is a very bad idea, and will result in a ton of technical debt!

Silencing errors or disabling all logging is a very bad idea; user berkes on Drupal Answers has a great analogy:

> Errors have a very important role: _they indicate that something is wrong_. Supressing that does not solve the underlying problem. This is also called the "Russian Method": When the alarm-light in a nuclear plant starts blinking, just remove the lightbulb. Alarm-light no longer blinks; no problems. ([Source](http://drupal.stackexchange.com/questions/15415/how-do-i-silence-php-errors#comment14696_15415))

This comment refers to the [Chernobyl disaster](https://en.wikipedia.org/wiki/Chernobyl_disaster); [a cascading set of warnings were intentionally silenced](http://articles.chicagotribune.com/1986-08-16/news/8603010325_1_reactor-control-rods-chernobyl-nuclear-plant), resulting in one of the greatest man-made disasters of the 20th century! There's a reason PHP has an error logging mechanism—it's so you can fix your fragile site _before it ends in disaster_!

## What TO do

You can't fix what you can't see, so the most important thing is to **show _all_ errors while developing** on local and shared development environments. Drupal.org has a documentation page showing how to do this: [Show all errors while developing](https://www.drupal.org/node/1056468). Drupal VM includes a [log viewing utility](http://docs.drupalvm.com/en/latest/extras/pimpmylog/) you can use to see errors. Most web hosts have an interface where you can view logs either live or in downloadable form. Know them, use them.

You should **have an error budget**: "if there are ever _X_ logged notices/warnings/errors or more during _Y_ period of time, we will stop working on new features on the site and work instead to fix those problems". For some teams, X is one or more; for others, they can live with a few errors or notices on certain pages. The key is to make sure you keep a lid on it—you don't want to have a super-fragile site that has tons of logs you have to wade through when things go wrong!

If your site is already over your error budget (e.g. if you see more errors on your home page than home page in your development environment), make an effort to fix errors _now_—the ROI is huge, because most of the time, one small fix (e.g. making sure a variable is set correctly somewhere) can solve dozens or even thousands of errors!

**Hide messages on the screen in production, but log them to syslog.** On `/admin/config/development/logging`, set 'None' for "Error messages to display"), make sure you have the Syslog module enabled. If you have a low-traffic site, or just need a really simple interface for viewing logged messages (and can live with the potentially-severe performance impact when there's a lot of activity), you can consider using Database Logging instead of Syslog. Acquia Cloud even streams and aggregates your logs when you use Syslog; see [about About Acquia Cloud Logging](https://docs.acquia.com/cloud/configure/logging).

## The Drupal 6 conundrum

One of the reasons I finally wrote this blog post (I've had a draft sitting in my files for over six years!) was because a few recent incidents have highlighted a major problem for those still running Drupal 6 websites—Drupal 6 core, and many Drupal 6 contributed modules, throw a _lot_ of notices and warnings if you run them with an actively-supported PHP version (currently only PHP 5.6 or 7.0). Since PHP 5.3 and 5.4 are rarely supported these days, and PHP 5.5 is getting harder to find, there are many cases where you have to run a Drupal 6 site on PHP 5.6 servers... meaning your logs get quite full!

I'd argue first that you should take this as reason #1284 why you should upgrade to Drupal 7 or 8 ASAP, but secondly, in rare circumstances where you absolutely must keep a Drupal 6 site up and running, you might have to break some of the rules I outlined above—either run an older, insecure, outdated, and slow version of PHP so the logged messages aren't to an extreme level, or turn off error logging. This should be seen as the 'nuclear option', and should probably motivate you to either drop any modules on an old Drupal site that cause lots of messages, or push for upgrading sooner rather than later!
