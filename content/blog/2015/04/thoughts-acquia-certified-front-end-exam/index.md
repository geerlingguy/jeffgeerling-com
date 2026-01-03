---
nid: 2489
title: "Thoughts on the Acquia Certified Developer - Front End Specialist Exam"
slug: "thoughts-acquia-certified-front-end-exam"
date: 2015-04-16T20:34:55+00:00
drupal:
  nid: 2489
  path: /blogs/jeff-geerling/thoughts-acquia-certified-front-end-exam
  body_format: full_html
  redirects: []
tags:
  - acquia
  - certification
  - drupal
  - drupal planet
  - exam
  - frontend
---

Previously, I posted my <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-certified-back-end-exam">thoughts on the Acquia Certified Developer - Back End Specialist exam</a> as well as my <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-drupal">thoughts on the Certified Developer exam</a>. To round out the trifecta of developer-oriented exams, I took the Front End Specialist exam this morning, and am posting some observations for those interested in taking the exam.

<p style="text-align: center;">{{< figure src="./front-end-specialist.png" alt="Acquia Certified Developer - Front End Specialist badge" width="162" height="157" >}}</p>

<h2>My Theming Background</h2>

I started my Drupal journey working on design/theme-related work, and the first few Drupal themes I built were in the Drupal 5 days (I inherited some 4.7 sites, but I only really started learning how Drupal's front end worked in Drupal 5+). Luckily for me, a lot of the basics have remained the same (or at least similar) from 5-7.

For the past couple years, though, I have shied away from front end work, only doing as much as I need to keep building out features on sites like <a href="https://hostedapachesolr.com/">Hosted Apache Solr</a> and <a href="https://servercheck.in/">Server Check.in</a>, and making all my older Drupal sites responsive (and sometimes, mobile-first) to avoid <a href="http://googlewebmastercentral.blogspot.com/2015/02/finding-more-mobile-friendly-search.html">penalization in Google's search rankings</a>... and to build a more usable web :)

<h2>Exam Content</h2>

A lot of the questions on the exam had to do with things like properly adding javascript and CSS resources (both internal to your theme and from external sources), setting up theme regions, managing templates, and working with theme hooks, the render API, and preprocessors.

In terms of general styling/design-related content, there were few questions on actual CSS and jQuery coding standards or best practices. I only remember a couple questions that touched on breakpoints, mobile-first design, or responsive/adaptive design principles.

There were also a number of questions on general Drupal configuration and site building related to placing blocks, menus, rearranging content, configuring views etc. (which would all rely on a deep knowledge of Drupal's admin interface and how it interacts with the theme layer).

<h2>Results</h2>

On this exam, I scored an 86.66%, and (as with the other exams) a nice breakdown of all the component scores was provided in case I want to brush up on a certain area:

<ul>
<li>Fundamental Web Development Concepts : 90%</li>
<li>Theming concepts: 80%</li>
<li>Sub-theming concepts: 100%</li>
<li>Templates: 75%</li>
<li>Template functions: 87%</li>
<li>Layout Configuration: 90%</li>
<li>Performance: 80%</li>
<li>Security: 100%</li>
</ul>

Not too surprising, in that I hate using templates in general, and try to do almost all work inside process and preprocess functions, so my templates just print the markup they need to print :P

I think it's somewhat ironic that the Front End and general Developer exams both gave me pretty good scores for 'Fundamentals', yet the back-end exam (which would target more programming-related situations) gave me my lowest score in that area!

<h2>Summary</h2>

I think, after taking this third of four currently-available exams (the Site Builder exam is the only one remaining—and I'm planning on signing up for that one at DrupalCon LA), I now qualify for being in Acquia's <a href="http://training.acquia.com/registry/grand-masters">Grand Master Registry</a>, so yay!

If you'd like to take or learn about this or any of the other Acquia Certification exams, please visit the <a href="https://www.acquia.com/customer-success/learning-services/acquia-certification-program-overview">Acquia Certification Program overview</a>.
