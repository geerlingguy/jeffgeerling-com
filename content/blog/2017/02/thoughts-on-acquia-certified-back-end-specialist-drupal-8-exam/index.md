---
nid: 2748
title: "Thoughts on the Acquia Certified Back end Specialist - Drupal 8 Exam"
slug: "thoughts-on-acquia-certified-back-end-specialist-drupal-8-exam"
date: 2017-02-22T21:37:50+00:00
drupal:
  nid: 2748
  path: /blog/2017/thoughts-on-acquia-certified-back-end-specialist-drupal-8-exam
  body_format: markdown
  redirects: []
tags:
  - acquia
  - backend
  - certification
  - drupal
  - drupal 8
  - drupal planet
  - exam
---

Continuing along with my series of reviews of Acquia Developer Certification exams (see the previous one: [Drupal 8 Site Builder Exam](/blog/2017/thoughts-on-acquia-certified-drupal-8-site-builder-exam), I recently took the [Back End Specialist – Drupal 8 Exam](https://www.acquia.com/customer-success/learning-services/acquia-certified-back-end-specialist-d8-exam-blueprint), so I'll post some brief thoughts on the exam below.

{{< figure src="./drupal-8-back-end-specialist-acquia-certified-badge.png" alt="Acquia Certified Back End Specialist - Drupal 8 Exam Badge" width="175" height="175" class="insert-image" >}}

Acquia finally updated the full suite of Certifications—Back/Front End Specialist, Site Builder, and Developer—for Drupal 8, and the toughest exams to pass continue to be the Specialist exams. This exam, like the Drupal 7 version of the exam, requires a deeper knowledge of Drupal's core APIs, layout techniques, Plugin system, debugging, security, and even some esoteric things like basic webserver configuration!

## A lot of new content makes for a difficult exam

Unlike the other exams, this exam sets a bit of a higher bar—if you don't do a significant amount of Drupal development and haven't built at least one or two custom Drupal modules (nothing crazy, but at least some block plugins, maybe a service or two, and some other integrations), then it's likely you won't pass.

There are a number of questions that require at least working knowledge of OOP, Composer, and Drupal's configuration system—things that an old-time Drupal developer might know absolutely nothing about! I didn't study for this exam at all, but would've likely scored higher if I spent more time going through some of the awesome [Drupal ladders](http://drupalladder.org/ladders) or other study materials. The only reason I passed is I work on Drupal 8 sites in my day job, and have for at least 6 months, and in my work I'm exposed to probably 30-50% of Drupal's APIs.

Unlike in Drupal 7, there are no CSS-related questions and few UI-related questions whatsoever. This is a completely new and more difficult exam that covers a lot of corners of Drupal 8 that you won't touch if you're mostly a site builder or themer.

## My Results

I scored an 73%, with the following section-by-section breakdown:

  - Fundamental Web Concepts: 80.00%
  - Drupal core API : 55.00%
  - Debug code and troubleshooting: 75.00%
  - Theme Integration: 66.66%
  - Performance: 87.50%
  - Security: 87.50%
  - Leveraging Community: 100.00%

I am definitely least familiar with Drupal 8's core APIs, as I tend to stick to solutions that can be built with pre-existing modules, and have as yet avoided diving too deeply into custom code for the projects I work on. Drupal 8 is really streamlined in that sense—I can do a lot more just using Core and a few Contrib modules than I could've done in Drupal 7 with thousands of lines of custom code!

Also, I'm still trying to wrap my head around the much more formal OOP structure of Drupal (especially around caching, plugins, services, and theme-related components), and I bet that I could score 10% or more higher in another 6 months, just due to familiarity.

I also scored fairly low on the 'debug code and troubleshooting' section, because it dealt with some lower-level debugging tools than what I prefer to use day-to-day. I use Xdebug from time to time, and it really is necessary for some things in Drupal 8 (where it wasn't so in Drupal 7), but I stick to Devel's `dpm()` and Devel Kint's `kint()` as much as I can, so I can debug in the browser where I'm more comfortable.

In summary, this exam was by far the toughest one I've taken, and the first one where I'd consider studying a bit before attempting to pass it again. I've scheduled the D8 Front End Specialist exam for next week, and I'll hopefully have time to write a 'Thoughts on it' review on this blog after that—I want to see if it's as difficult (especially regarding to twig debugging and the render system changes) as the D8 Back End Specialist exam was!
