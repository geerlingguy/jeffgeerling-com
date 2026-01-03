---
nid: 2836
title: "A modern way to build and develop Drupal 8 sites, using Composer"
slug: "modern-way-build-and-develop-drupal-8-sites-using-composer"
date: 2018-04-10T03:27:47+00:00
drupal:
  nid: 2836
  path: /blog/2018/modern-way-build-and-develop-drupal-8-sites-using-composer
  body_format: markdown
  redirects:
    - /blog/2018/starting-new-drupal-8-project-quick-way-using-composer
aliases:
  - /blog/2018/starting-new-drupal-8-project-quick-way-using-composer
tags:
  - composer
  - docker
  - drupal
  - drupal planet
  - drupal vm
  - local development
---

The Drupal community has been on an interesting journey since the launch of Drupal 8 in 2015. In the past three years, as the community has started to get its sea legs 'off the island' (using tools, libraries, and techniques used widely in the general PHP community), there have been growing pains.

One area where the pains have been (and sometimes still are) highly visible is in how Drupal and Composer work together. I've written posts like [Composer and Drupal are still strange bedfellows](//www.jeffgeerling.com/blog/2017/composer-and-drupal-are-still-strange-bedfellows) in the past, and while in some ways that's still the case, we as a community are getting closer and closer to a nirvana with modern Drupal site building and project management.

For example, in preparing a hands-on portion of my and Matthew Grasmick's upcoming DrupalCon Nashville lab session on Composer and Drupal, I found that we're already to the point where you can go from literally _zero_ to a fully functional and complete Drupal site codebase—along with a functional local development environment—in about 10 or 15 minutes:

  1. Make sure you have PHP, [Composer](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-osx), and [Docker CE](https://store.docker.com/search?type=edition&offering=community) installed (Windows users, [look here](//www.jeffgeerling.com/blog/2018/installing-php-7-and-composer-on-windows-10)).
  2. Create a Drupal codebase using the Drupal Composer Project: `composer create-project drupal-composer/drupal-project:8.x-dev drupal8 --stability dev --no-interaction`
  3. Open the project directory: `cd drupal8`
  4. Add a plugin to build a quick and simple local dev environment using [Drupal VM Docker Composer Plugin](https://github.com/geerlingguy/drupal-vm-docker): `composer require --dev geerlingguy/drupal-vm-docker`
  5. Start the local dev environment: `docker-compose up -d`
  6. Open a browser and visit [http://localhost/](http://localhost/)

I'm not arguing that Drupal VM for Docker is the ideal local development environment—but accounting for about one hour's work last night, I think this shows the direction our community can start moving once we iron out a few more bumps in our Composer-y/Drupal-y road. Local development environments as Composer plugins. Development tools that automatically configure themselves. Cloud deployments to any hosting provider made easy.

Right now a few of these things are possible. And a few are kind of pipe dreams of mine. But I think this year's DrupalCon (and the follow-up discussions and issues that will result) will be a catalyst for making Drupal and Composer start to go from being often-frustrating to being extremely slick!

If you want to follow along at home, follow this core proposal: [Proposal: Composer Support in Core initiative](https://www.drupal.org/project/ideas/issues/2958021). Basically, we might be able to make it so Drupal core's own Composer usage is good enough to not need a shim like [drupal-composer/drupal-project](https://github.com/drupal-composer/drupal-project), or a bunch of custom tweaks to a core Composer configuration to build new Drupal projects!

Also, I will be working this DrupalCon to help figure out new and easier ways to make local development easier and faster, across Mac, Linux and Windows (I even brought my clunky old Windows 10/Fedora 26 laptop with me!). There are a number of related BoFs and sessions if you're here (or to watch post-conference), for example:

  - **Tuesday**
    - [Improving Drupal's Evaluator experience](https://events.drupal.org/nashville2018/bofs/improving-drupals-evalutator-experience) - BoF, 10:45-11:45 a.m. Tuesday
    - [Top 8 considerations for choosing a local development environment](https://events.drupal.org/nashville2018/sessions/top-8-considerations-choosing-local-development-environment) - Session, 10:45-11:45 a.m. Tuesday
    - [2018 Drupal Developer Survey Results](https://events.drupal.org/nashville2018/bofs/2018-drupal-developer-survey-results) - BoF, 12:00-1:00 p.m. Tuesday
    - [Drupal Core Auto-Update Architecture](https://events.drupal.org/nashville2018/sessions/drupal-core-auto-update-architecture) - Session, 1:00-2:00 p.m. Tuesday
  - **Wednesday**
    - [An official Drupal local development environment?](https://events.drupal.org/nashville2018/bofs/official-drupal-local-develop-environment) - BoF, 10:45-11:45 a.m.
    - [How to build a Drupal site with Composer AND keep all of your hair](https://events.drupal.org/nashville2018/sessions/how-build-drupal-site-composer-and-keep-all-your-hair) - Session, 3:45-6:00 p.m.
