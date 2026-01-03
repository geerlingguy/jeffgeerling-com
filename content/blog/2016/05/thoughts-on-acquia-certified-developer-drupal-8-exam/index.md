---
nid: 2648
title: "Thoughts on the Acquia Certified Developer - Drupal 8 Exam"
slug: "thoughts-on-acquia-certified-developer-drupal-8-exam"
date: 2016-05-10T19:21:36+00:00
drupal:
  nid: 2648
  path: /blog/2017/thoughts-on-acquia-certified-developer-drupal-8-exam
  body_format: markdown
  redirects:
    - /blog/2016/thoughts-on-acquia-certified-developer-drupal-8-exam
aliases:
  - /blog/2016/thoughts-on-acquia-certified-developer-drupal-8-exam
tags:
  - acquia
  - certification
  - drupal
  - drupal 8
  - drupal planet
  - exam
---

Another year, another Acquia Certification exam...

{{< figure src="./acquia-certified-developer-drupal-8.png" alt="Acquia Certified Developer - Drupal 8 Exam Badge" width="177" height="177" class="insert-image" >}}

I'm at DrupalCon New Orleans, the first North American DrupalCon since the release of Drupal 8. In addition, this is the first DrupalCon where the [Acquia Certified Developer - Drupal 8 Exam](https://www.acquia.com/customer-success/learning-services/acquia-certified-developer-drupal-8-exam-blueprint) is being offered, so I decided to swing by the certification center (it's on the 3rd floor of the convention center, in case you want to take any of the certification exams this week!) and take it.

I've taken all the other exams up to this point, including the [general developer exam](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-drupal), the [front end](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-certified-front-end-exam) and [back end](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-certified-back-end-exam) specialist exams, and the [site builder](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-certified-site-builder-exam) exam, and I've posted short reviews of each of those exams (click the links to read the reviews), so I thought I'd post a review of this exam as well, for the benefit of others who will take it in coming months!

> Note: If you'd like a good overview of my perspective on the Acquia Certifications in general, please read my post on the [general developer exam](//www.jeffgeerling.com/blogs/jeff-geerling/thoughts-acquia-drupal), which was written prior to my Acquia employment. Not that I bias my posts here based on my employer, but I do realize there are many who are conflicted over the value of a Drupal certification (or of any software certifications in general), and there are pros and cons to taking the actual exams. I'm of the opinion that the exams are a good thing for the Drupal community, but probably not a great way to judge individual developers (e.g. for hiring purposes), unless taken as one data point in the evaluation process.

## A little bit of the old...

For anyone who's taken one of the previous exams, this exam should feel familiar. Probably half of the questions (mostly the 'foundational web development' and 'site building' ones) could be used on any of the Drupal Certification exams. This is because Drupal 8 _does_ carry over a lot of the same content and admin architecture of Drupal 7, even if things underlying the architecture have changed dramatically.

Things like adding fields, managing content types, adding relationships, displaying lists of content, etc. are fundamentally the same as they were in Drupal 7, though all the modules for performing these operations are included in Drupal 8 core.

Additionally, many parts of the theming realm (preprocess functions and the Render API, mostly) are the same.

## ...A good dose of the new

However, there are maybe 5-10 questions that are a little trickier for me (and would be for anyone working with both Drupal 7 and Drupal 8 sites), because the questions deal with APIs or bits of Drupal that have changed only subtly, or were only halfway re-architected in Drupal 8. For example, there are a few things in Drupal 8 that use Symfony's [Event Dispatcher](https://api.drupal.org/api/drupal/core!core.api.php/group/events/8.2.x). But wouldn't you know, nodes still use the old-school hooks! As I have only worked on a couple custom modules that tie into node operations, I wasn't sure what the status of conversion to the new system was... but if you're wondering, [HookEvent is still not part of Drupal 8 core](https://www.drupal.org/node/1972304).

Besides those ambiguous questions (most of which I'm sure I answered incorrectly), there were a number of questions related to basic Twig syntax (e.g. how do you print variables, how do you filter variables, how do you structure a template, how do you add a template suggestion, etc.), and thankfully, there wasn't anything super-deep, like how Twig blocks (not Drupal blocks) work!

You'll want to have at least a basic understanding of creating a route, creating a block plugin, defining a service, adding a CSS or JS file as a library, and using annotations properly in custom modules. You can look at some core modules (like the Book module) for simple implementation examples.

## A few errors

Since this is a relatively new exam (I think it was 'officially' launched this week!), there are a few rough edges (grammatical issues, question style issues) that will be ironed out in the next few months; when I had taken the other exams, those little issues had already been worked out, so all my thought could focus on the question at hand, and the potential solutions, and not on style, phrasing, or content.

There was one question that seems to have been partially cut off, as it had a statement, a code block, then some answers... but no actual question! I inferred what the question would be based on context... but I also let the facilitator know, and by the time _you_ take the exam, the erroneous questions will likely be fixed.

These are common issues with the launch of a new exam, since the exam questions are built up from a large number of contributed questions, and the tool (webassessor) doesn't always seem to offer the best interface/input for technical questions. The same caveats apply to this exam as the others—make sure you read through the question a couple times if it's unclear, and whenever there are code samples (especially in answers), make sure you're parsing things correctly!

## My Results

I took the exam early in the week, but didn't have a lot of caffeine yet, so I may have been able to score marginally higher. But I'm happy with my overall 81.66%, broken down into the following:

  - Fundamental Web Development Concepts: 100%
  - Site Building: 77%
  - Front end Development: 80%
  - Back end Development: 80%

I'm guessing that after I have a few more Drupal 8 sites under my belt (especially ones that don't use the default Bartik theme, like the [Raspberry Pi Dramble](http://www.pidramble.com/) site), I can bump up some of the other scores a bit. There are a lot of subtle differences between Drupal 7 and Drupal 8 that can trip a seasoned Drupalist up in these questions!
