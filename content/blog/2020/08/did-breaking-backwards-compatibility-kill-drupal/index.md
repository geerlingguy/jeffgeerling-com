---
nid: 3034
title: "Did breaking backwards compatibility kill Drupal?"
slug: "did-breaking-backwards-compatibility-kill-drupal"
date: 2020-08-19T18:27:15+00:00
drupal:
  nid: 3034
  path: /blog/2020/did-breaking-backwards-compatibility-kill-drupal
  body_format: markdown
  redirects: []
tags:
  - compatibility
  - drupal
  - drupal 8
  - drupal 9
  - drupal planet
  - programming
---

First of all, Drupal is not dead. But I would argue it's not in healthy place relative to competing projects as it was in its heyday, in the early 2010s.

In this blog post, I will explore the problem the Drupal community finds itself in five years after a major release that **broke backwards compatibility** in almost every subsystem, forcing a laborious upgrade process and process shift that left many users in the dust.

I've written about this in the past, most famously in my post [Drupal 8 successes and failures](/blog/2019/drupal-8-successes-and-failures). I'm not going to rehash the details from that post, but I did want to focus on what I think is the primary reason for this graph's downward trajectory since 2016:

{{< figure src="./usage-statistics-drupal-core-2020.png" alt="Usage Statistics for Drupal Core from 2013 to 2020" width="647" height="208" class="insert-image" >}}

Unlike past releases like Drupal 5, 6, and 7, the release of Drupal 8 did not result in many 7-to-8 upgrades _and_ new Drupal sites. Rather, there began a gradual decline in Drupal 7 sites, along with a very low rate of new Drupal 8 sites to replace them.

Looking at the usage graph for the years _prior_ to Drupal 8's release, you can see Drupal's overall usage _doubled_ from 2011 to 2014:

{{< figure src="./usage-staticistics-drupal-2010-2014.png" alt="Usage Statistics for Drupal Core from 2010 to 2014" width="666" height="166" class="insert-image" >}}

For the first time since 2014, the Drupal project is likely to see less than one million active installations reporting back in to Drupal.org later this year.

> Note: These graphs do not show every single Drupal site that's running in production. But they are the best approximation and on relative time scales, and they show relevant trends, since in Drupal 7, 8, and 9, the 'Update Status' module (which is key to this data on Drupal.org) is enabled in the standard installation.

## Breaking Backwards Compatibility

The main motivation for this blog post was the constant 'yin and yang' in the software industry for encouraging radical design departure and adoption of new paradigms vs. the pragmatic "we will never break your code" approach of something like Microsoft Windows.

Each has its ups and downs, and each has wildly successful—and wildly disastrous—examples.

  - **Radical departure**: Apple has reinvented its OS and application ecosystem multiple times, switching entire platforms (68k to PPC to Intel and now to ARM) and programming languages (Pascal, C/C++, Objective C, Swift) along the way. Some developers drop off with each shift, but Apple has now built one of the most profitable app ecosystems and is the most valuable corporation in the world by market cap.
  - **We'll never break your code**: PHP itself seems to be a shining example. With the exception of small changes every decade or so to fix new fatal errors, I have many scripts and libraries written for PHP 5.0 which work unmodified on PHP 7.4 and PHP 8!

When I was reading the post [Dear Google Cloud: Your Deprecation Policy is Killing You](https://medium.com/@steve.yegge/dear-google-cloud-your-deprecation-policy-is-killing-you-ee7525dc05dc) by Steve Yegge, I think I realized why some projects are successful one way and some are successful the other:

_Consistency_ in deprecation policies.

Drupal, since its inception, was an 'island'. It was written in PHP, but generally there weren't efforts to make Drupal a part of the growing PHP ecosystem, like newer, framework-oriented projects like Symfony or Laravel. It stayed this way for over a decade.

A similar case is the Python language. It is a full-featured programming language, with solid and reliable core APIs. CS graduates were taught one of Java or Python (or both), and Python-based courses, books, and software basically worked the same for almost ten years.

But in both cases, a major change decimated the implicit trust developers had built around the project over a decade: an **unspoken promise** the project wouldn't make sweeping changes that require _major_ rewrites or rearchitecture in one major version.

In Drupal's case, a major effort was made in Drupal 8 to "get off the island", and replace many core APIs and systems with Symfony and other PHP ecosystem libraries. It was an ambitious effort, and Drupal today is a pretty well-architected PHP application.

But it broke the implicit trust developers built over many prior releases.

The upgrade process was no longer a case of "a few hours or a few weeks," but instead "a few months," since in many cases upgrading meant a full redesign, and in many cases, complete site rearchitecture.

In Python's case, Python 3 made breaking changes which were not adopted by many popular libraries and frameworks for many years, and it took _twelve years_ before the community deemed it safe to once and for all drop Python 2 support.

## What is the takeaway?

Well, on the positive side, the Drupal community seems to be learning from the massive misstep in Drupal 8—Drupal 9, which was just released earlier this year, has _no_ major refactorings, only removals of old, deprecated APIs. If you have a site that works in the latest version of Drupal 8, it's highly likely the upgrade process will take minutes, or at most a few hours.

And Drupal 10 seems to be on a similar path.

But, as someone who spent _ten years_ earning the majority of my income from Drupal development, and is still a somewhat invested member of the Drupal open source community, I am left wondering where to go from here.

Many of the features of Drupal 8, 9, and now 10, seem to be focused on high-dollar enterprise projects competing with multi-million dollar Adobe Experience Manager or Sitecore projects, as the lower ('less profitable') end of the CMS market has been abandoned or left to Wordpress and online site builders like Wix or Squarespace.

But that's not the thing that worries me most.

I don't think it's a stretch to say developers like me have a sort of 'PTSD' after a foundational shift in the trend of backwards compatibility breaks, and I personally feel less enthusiastic about supporting open source code that I fear may need more major rewrites just to 'keep up with the Joneses'.

If you build in an ecosystem that often breaks backwards compatibility (Apple's OSes, Google Cloud, and especially most of the Javascript ecosystem), then you are conditioned to expect it, and that's part of the 'cost of living' in that ecosystem.

But if you work with an ecosystem that is stable for long periods, then makes multiple major BC breaks in one release, it feels like you're getting hoodwinked.

## Conclusion

Take the real-world experience of the Drupal community to heart: figure out if your project is more like an Apple or more like a Microsoft.

Do you have a reputation of breaking backwards compatibility frequently? Or do you typically make sure you have BC layers that allow people using your software to be more lazy when it comes to upgrades?

Neither is necessarily _wrong_. But making a radical departure in one major release may harm your project in the long term.
