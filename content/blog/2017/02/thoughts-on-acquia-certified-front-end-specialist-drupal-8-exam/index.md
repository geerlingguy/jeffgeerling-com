---
nid: 2750
title: "Thoughts on the Acquia Certified Front end Specialist - Drupal 8 Exam"
slug: "thoughts-on-acquia-certified-front-end-specialist-drupal-8-exam"
date: 2017-02-24T16:58:16+00:00
drupal:
  nid: 2750
  path: /blog/2017/thoughts-on-acquia-certified-front-end-specialist-drupal-8-exam
  body_format: markdown
  redirects: []
tags:
  - acquia
  - certification
  - drupal
  - drupal 8
  - drupal planet
  - exam
  - frontend
---

Another day, another Acquia Developer Certification exam review (see the previous one: [Certified Back end Specialist - Drupal 8](/blog/2017/thoughts-on-acquia-certified-back-end-specialist-drupal-8-exam), I recently took the [Front End Specialist – Drupal 8 Exam](https://www.acquia.com/customer-success/learning-services/acquia-certified-front-end-specialist-d8-exam-blueprint), so I'll post some brief thoughts on the exam below.

{{< figure src="./acquia-front-end-specialist-drupal-8-exam-badge.png" alt="Acquia Certified Front End Specialist - Drupal 8 Exam Badge" width="175" height="175" class="insert-image" >}}

Now that I've completed all the D8-specific Certifications, I think the only Acquia Certification I _haven't_ completed is the 'Acquia Cloud Site Factory' Exam—one for which I'm definitely not qualified, as I haven't worked on a project that uses Acquia's 'ACSF' multisite setup (though I do a _lot_ of other multisite and install profile/distribution work, just nothing specific to Site Factory!). Full disclosure: Since I work for Acquia, I am able to take these Exams free of charge, though many of them are worth the price depending on what you want to get out of them. I paid for the first two that I took (prior to Acquia employment) out of pocket!

## Some old, some new

This exam feels very much in the style of the Drupal 7 Front End Specialist exam—there are questions on theme hook suggestions, template inheritance, basic HTML5 and CSS usage, basic PHP usage (e.g. how do you combine two arrays, in what order are PHP statements evaluated... really simple things), etc.

The main difference with this exam centers on the little differences in doing all the same things. For example, instead of PHPTemplate, Drupal 8 uses Twig, so there are questions relating to Twig syntax (e.g. how to chain a filter to a variable, how to print a string from a variable that has multiple array elements, how to do basic if/else statements, etc.). The question content is the same, but the syntax is using what would be done in Drupal 8. Another example is theme hook suggestions—the general functionality is identical, but there were a couple questions centered on how you add or use suggestions specifically in Drupal 8.

The main thing that tripped me up a little bit (mostly due to my not having used it too much) is new Javascript functionality and theme libraries in Drupal 8. You should definitely practice adding JS and CSS files, and also learn about differences in Drupal 8's Javascript layer (things like using `'use strict';`, how to make sure `Drupal.behaviors` are available to your JS library, and the like).

I think if you've built at least one custom theme with a few Javascript and CSS files, and a few custom templates, you'll do decently on this exam. Bonus points if you've added a JS file that shouldn't be aggregated, added translatable strings in both Twig files and in JS, and worked out the differences in Drupal's stable and classy themes in Drupal 8 core.

For myself, the only preparation for this exam was:

  - I've helped build two Drupal 8 sites with rather complex themes, with many libraries, dozens of templates, use of Twig `extends` and `include` syntax, etc. Note that I was probably only involved in theming work 20-30% of the time.
  - I built one really simple Drupal 8 custom theme for a photo sharing website (closed to the public): https://jeffgpix.com/
  - I read through the _excellent_ [Drupal 8 Theming Guide](https://sqndr.github.io/d8-theming-guide/index.html) by Sander Tirez ([sqndr](https://www.drupal.org/u/sqndr))

## My Results

I scored an 83.33% (10% better than the Back End test... maybe I should stick to theming :P), with the following section-by-section breakdown:

  - Fundamental Web Development Concepts : 92.85%
  - Theming concepts: 73.33%
  - Templates and Pre-process Functions: 87.50%
  - Layout Configuration: 66.66%
  - Performance: 100.00%
  - Security: 100.00%

I'm not surprised I scored worst in Layout Configuration, as there were some questions about defining custom regions, overriding region-specific markup, and configuring certain things using the Breakpoints and Responsive Images module. I've done all these things, but only rarely, since you generally set up breakpoints only when you initially build the theme (and I only did this once), and I only deal with Responsive Images for a few specific image field display styles, so I don't use it enough to remember certain settings, etc.

It's good to know I keep hitting 90%+ on performance and security-related sections—maybe I should just give up site building and theming and become a security and performance consultant! (Heck, I do a lot more infrastructure-related work than site-building outside of my day job nowadays...)

This exam was not as difficult as the Back End Specialist exam, because Twig syntax and general principles are very consistent from Drupal 7 to Drupal 8 (and dare I say _better_ and _more comprehensible_ than in the Drupal 7 era!). I'm also at a slight advantage because almost all my [Ansible](https://www.ansiblefordevops.com) work touches on Jinja2, which is the templating system that inspired Twig—in most cases, syntax, functions, and functionality are identical... you just use {{.j2}} instead of {{.twig}} for the file extension!
