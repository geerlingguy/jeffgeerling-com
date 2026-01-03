---
nid: 2725
title: "Thoughts on the Acquia Certified Drupal 8 Site Builder Exam"
slug: "thoughts-on-acquia-certified-drupal-8-site-builder-exam"
date: 2017-01-04T22:01:18+00:00
drupal:
  nid: 2725
  path: /blog/2017/thoughts-on-acquia-certified-drupal-8-site-builder-exam
  body_format: markdown
  redirects: []
tags:
  - acquia
  - certification
  - drupal
  - drupal 8
  - drupal planet
  - exam
  - site builder
---

Another year, another Acquia Certification exam... (wait—I think [I've said that before](//www.jeffgeerling.com/blog/2016/thoughts-on-acquia-certified-developer-drupal-8-exam)).

{{< figure src="./acquia-certified-site-builder-drupal-8.png" alt="Acquia Certified Site Builder - Drupal 8" width="177" height="177" class="insert-image" >}}

The latest of the updated Acquia Certification Exams is the [Acquia Certified Drupal 8 Site Builder](https://www.acquia.com/customer-success/learning-services/acquia-certified-drupal-8-site-builder-exam). It's meant for the average Drupal site builder to test and evaluate familiarity with building websites using Drupal 8, and it's the same as all the previous exams in style: a series of 40 questions posed in the conversational manner, with answers you would provide if you were telling a project manager or site owner how you would implement a feature.

As an example, one of the questions mentioned the site is having trouble with spam on one of its forms; you are tasked with the best solution to cut down on the spam, and options include things like limiting form access to authenticated users or enabling a module like CAPTCHA. Sometimes the answers can be slightly ambiguous (just like in real life), as multiple solutions _could_ be correct. In this case, I wish there were a write-in answer, because I'd suggest something a little less user-hostile for spam reduction... like [Honeypot](https://www.drupal.org/project/honeypot) ?

I've taken all the other exams up to this point, including the [Drupal 8 developer exam](//www.jeffgeerling.com/blog/2016/thoughts-on-acquia-certified-developer-drupal-8-exam), the [general developer exam](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-drupal), the [front end](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-certified-front-end-exam) and [back end](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-certified-back-end-exam) specialist exams, and the [site builder](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-certified-site-builder-exam) exam, and I've posted short reviews of each of those exams (click the links to read the reviews), so I thought I'd post a review of this exam as well, for the benefit of others who will take it in coming months!

> Note: If you'd like a good overview of my perspective on the Acquia Certifications in general, please read my post on the [general developer exam](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-drupal), which was written prior to my Acquia employment. Not that I bias my posts here based on my employer, but I do realize there are many who are conflicted over the value of a Drupal certification (or of any software certifications in general), and there are pros and cons to taking the actual exams. I'm of the opinion that the exams are a good thing for the Drupal community, but probably not a great way to judge individual developers (e.g. for hiring purposes), unless taken as one data point in the evaluation process.

## A little bit of the old...

Just like the [Drupal 8 developer exam](//www.jeffgeerling.com/blog/2016/thoughts-on-acquia-certified-developer-drupal-8-exam), this exam is quite similar to the original Site Builder exam (which covered Drupal 7). Most of the questions surround how you would build certain features or display content on a Drupal 8 site. There are questions covering views content listings, block placement, user roles and permissions configuration, and content types.

Thankfully, though, there aren't any questions on the Aggregator module (which is thankfully gone from Drupal core ?).

There are no questions dealing with CSS, JS, PHP, or Composer; it's strictly site building here. If you can't do it in Drupal's UI, it's likely not covered in the exam (though there was one question dealing with configuration management—how to export and import configuration between different environments, and two dealing with module and theme updates).

## A few errors

Like other Drupal 8 exams, this exam still seems a little rough around the edges in a couple areas. There were two questions which had typos causing a little back-and-forth between the answers and the question to try to figure out what was being asked, and there was one question where I think the way it was worded was way too ambiguous—_technically_ any of the four answers could've been correct, depending on the project priorities and appetite for technical debt.

So, just like in real life, the exam can be a little ambiguous and messy—but the exam tries to force you into picking one 'correct' choice, and dings you in the report card at the end if you didn't pick what the question writer chose as the 'most correct'!

Make sure you read through the question a couple times if it's unclear, and mark questions for review if you have to spend a lot of time deciphering it's meaning.

## My Results

I scored an 86%, with the following section-by-section breakdown:

  - Understanding Drupal: 100%
  - Working with a Drupal Site : 100%
  - Content Modeling : 75%
  - Site Display: 66%
  - Site Configuration: 85%
  - Community and Contributed Projects: 100%
  - Module and Theme management: 100%
  - Security & Performance: 75%

I've built and launched four Drupal 8 sites so far (and am working on two more, currently), so I'm guessing if you have some D8 experience under your belt, you can score similarly. There are definitely a few tricky questions like which option to select for a given view mode or content type display... but I've encountered almost all the use cases featured in the questions at least once or twice before. And many things are similar if not exactly the same in Drupal 7/Views/Content Types/Permissions, so even if you don't have much D8 experience, you may be able to get a passing grade.
