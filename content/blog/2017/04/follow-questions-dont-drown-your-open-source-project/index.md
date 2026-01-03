---
nid: 2770
title: "Follow up questions to 'Don't drown in your open source project'"
slug: "follow-questions-dont-drown-your-open-source-project"
date: 2017-04-29T15:36:43+00:00
drupal:
  nid: 2770
  path: /blog/2017/follow-questions-dont-drown-your-open-source-project
  body_format: markdown
  redirects: []
tags:
  - architecture
  - essay
  - open source
  - software
---

After I posted my presentation slides, transcript, and video from my presentation [Don't drown in your open source project!](//www.jeffgeerling.com/blog/2017/dont-drown-your-open-source-project), I received two follow-up questions ([1](https://twitter.com/daggerhart/status/858047361716817920), [2](https://twitter.com/daggerhart/status/858048228826152960)) on Twitter that I thought deserved a little better response than what I could do in 140 characters. So, here goes:

> Do you ever abandon old projects? Thoughts on right/wrong ways?

Yes, in fact I've abandoned probably a dozen or so projects. The simplest examples:

  1. Projects like [acquia-cloud-vm](https://github.com/geerlingguy/acquia-cloud-vm) (which was superseded by [Drupal VM](https://www.drupalvm.com)). In this case, the best solution is to leave the existing project in the same namespace/location, but put a bold notice in the README, on the first page of docs, etc. marking it as deprecated.
  2. Projects like my [Tomcat 6 Ansible Role](https://github.com/geerlingguy/ansible-role-tomcat6), where the software itself has been deprecated or marked unsupported. Much like the first case, you should notify people through messages in the README, home page, etc.

In both of these cases, you may also consider building one more release which is basically the same as the last release, but somehow pops a notification to the user saying it's no longer supported/maintained.

In cases where the software is still relevant, but you just don't have the time or passion for maintaining it, I would say choose one of the following:

  1. Find or choose a new maintainer/owner, and cede control to that person. Sometimes it's harder to do this than just not touch it, but if there are active users, this is often a nicer way of abandoning the project (instead of leaving your users in a lurch).
  2. Put a notice in the README/home page saying that you are not maintaining currently (e.g. use at your own risk), but you might someday pick it back up again.
  3. Just stop touching the project and disable all your notifications. This option isn't the best... but it's typical in open source, and you wouldn't be blamed for not maintaining software as long as the license is an open license, allowing people to fork/clone it if they want to maintain their own version.

A lot of times, option 3 is unknowingly chosen as you start working on new things and forget about (or intentionally ignore) an old project.

> How do you fight the urge to do full rewrites all the time? I'm always wanting to overhaul entire projects after learning something new.

I fight the urge by treating all of my projects like I would a paid project—I set a level of technical debt I'm comfortable with, and then manage it by sometimes saying no to new features while a short or long-term refactoring takes place.

You do have to refactor software over time. But you can end up doing a full rewrite incrementally by simply managing technical debt, splitting work into small, manageable chunks (I usually try to make every individual task take 2 hours or less, with few exceptions).

And you can always create an experimental branch for major rewrites, and slowly migrate the codebase to the experimental branch once it's reaching feature parity with the main branch.

It's pretty rare that there's a successful (e.g. mostly seamless) complete rewrite of any software (e.g. Mac OS 6/7/8/9 to Mac OS X), but even in those cases, it was an incremental change, including many backwards compatible layers to ease with the transition.
