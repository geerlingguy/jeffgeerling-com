---
nid: 2963
title: "Migrating JeffGeerling.com from Drupal 7 to Drupal 8 - How-to video series"
slug: "migrating-jeffgeerlingcom-drupal-7-drupal-8-how-video-series"
date: 2020-02-04T21:18:14+00:00
drupal:
  nid: 2963
  path: /blog/2020/migrating-jeffgeerlingcom-drupal-7-drupal-8-how-video-series
  body_format: markdown
  redirects:
    - /d8-migrate
aliases:
  - /d8-migrate
tags:
  - drupal
  - drupal 8
  - drupal planet
  - migrate
  - migration
  - tutorial
  - youtube
---

{{< figure src="./drupal-live-migration-blog-image.png" alt="Drupal 8 Live migration YouTube series image for JeffGeerling.com" width="650" height="366" class="insert-image" >}}

This website is currently (as of February 2020) running on Drupal 7. Drupal 8 was released in November 2015—half a decade ago. Drupal 7 support has been extremely long-lived, as it will not be end-of-life'd until November 2021. As with all software, once it is out of date, and security patches are no longer provided, it becomes harder to ensure the software is secure, much less running well on the latest servers and PHP versions!

Therefore, I decided it was time to start migrating JeffGeerling.com to Drupal 8. And I figured instead of fumbling through the process all by myself, and maybe posting a couple blog posts about the process at the end, I'd adopt a new mantra: _Let's fail together!_ (Just kidding—sorta.)

So for this migration, I'm going to be live-streaming the entire process, end-to-end! Every Tuesday (starting today, February 4, 2020), at 10 a.m. US Central time (4 p.m. UTC), I will be live streaming part of the migration process for one hour. The videos will all be visible after the fact on [my YouTube account](https://www.youtube.com/channel/UCR-DXc1voovS8nhAvccRZhg).

There are a few caveats to get out of the way going into this project:

  - This is the first time doing any Drupal 8 migration work since Drupal 8.2, in 2016. A _lot_ has changed in Drupal 8 since then, so I'll be learning some of this as I go—I figure some people might enjoy seeing how I learn new processes and techniques (hint: lots of Google).
  - This is the first Drupal 8 work I've worked on since upgrading the theme of the [Raspberry Pi Dramble](https://www.pidramble.com) website in late 2018, so my Drupal 8 is a little rusty as well.
  - This is the first time I've ever tried live-streaming, and I'm doing it on a four year old 13" MacBook Pro; the CPU might not be up to the task at times, but we'll see how it holds up!

If you want to follow along as it happens, please **[subscribe to my YouTube channel](https://www.youtube.com/channel/UCR-DXc1voovS8nhAvccRZhg)** and sign up for notifications—that way YouTube can notify you when a live stream is about to begin (I will try to remember to have them pre-scheduled every Tuesday). Otherwise, I will also be embedding all the live streams after the fact on this blog post (so check back again later to see them if you miss a week!).

## Supporting this project

I'm not being paid or sponsored for any of the work involved in producing these videos; if you like them, and have the ability, please consider sponsoring my work on one of the following platforms:

  - [Patreon](https://www.patreon.com/geerlingguy)
  - [GitHub Sponsors](https://github.com/sponsors/geerlingguy)

If I get enough, maybe I can afford a faster computer and stream with a better frame rate :-)

## Episode 1 - Setting up a new Drupal project, installing Drupal the first time

Streamed on: February 4, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/EyI_OwhufNk" frameborder='0' allowfullscreen></iframe></div>

Summary: I created a new GitHub repository called `jeffgeerling-com`, then I created a new Drupal 8 codebase. I added a `.gitignore` file since Drupal's composer template doesn't currently ship with one, and made sure to not add the `vendor` directory or other Composer-managed files to the Git codebase. I committed all the code, and pushed it to the master branch of the `jeffgeerling-com` repository on GitHub. Then I created a simple Docker image for local development, brought up a local environment using Docker Compose (with a Drupal/Apache/PHP container and a MySQL container), and finally installed Drupal using `drush site:install`. I logged in and verified the site is working correctly (if a bit sparse—I installed the minimal profile!).

Resources:

  - [drupal-for-kubernetes Drupal project setup guide](https://github.com/geerlingguy/drupal-for-kubernetes/blob/master/docs/starting-new-project.md).
  - [Using drupal/recommended-project to create a Drupal codebase](https://www.drupal.org/docs/develop/using-composer/using-composer-to-install-drupal-and-manage-dependencies#s-using-drupalrecommended-project)
  - [Arch Linux memes](https://twitter.com/archlinuxmemes)

## Episode 2 - Getting the Configuration and Content Migration Ready

Streamed on: February 11, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/yS1qIcpWZZI" frameborder='0' allowfullscreen></iframe></div>

Summary: I downloaded the [Upgrade Status](https://www.drupal.org/project/upgrade_status) module and went through which modules did or did not have upgrade paths for Drupal 8. I found that most modules I use are now in Drupal core, and most of the contributed modules I use have a stable Drupal 8 version available. There are a couple modules that might need some special tweaks to make sure I don't lose data—like making sure Redirects are migrated correctly from Drupal 7 to Drupal 8—but most things should just work in Drupal 8 without much effort. I then read through the [Upgrading from Drupal 6 or 7 to Drupal 8](https://www.drupal.org/docs/8/upgrade/upgrading-from-drupal-6-or-7-to-drupal-8) documentation guide, and chose to [use Drush for the migration](https://www.drupal.org/docs/8/upgrade/upgrade-using-drush). So I installed the appropriate modules, and tried connecting my site to the legacy Drupal 7 database by adding a database to the `$databases` array in the Drupal 8 site's `settings.php` file. Unfortunately, I was unable to get the Drupal 8 site to see the Drupal 7 database before the episode's time ran out, so we'll get that working in the next episode, and run the `drush migrate-upgrade` command for the first time!

Resources:

  - [Drupal Upgrade Status module](https://www.drupal.org/project/upgrade_status)
  - [Upgrading from Drupal 6 or 7 to Drupal 8](https://www.drupal.org/docs/8/upgrade/upgrading-from-drupal-6-or-7-to-drupal-8)
  - Migration modules for Drush-based migration: [Migrate Upgrade](https://www.drupal.org/project/migrate_upgrade), [Migrate Plus](https://www.drupal.org/project/migrate_plus), [Migrate Tools](https://www.drupal.org/project/migrate_tools).

## Episode 3 - Fixing bugs, exporting configuration, and running the first migrations

Streamed on: February 18, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/lP7RHTu7K0k" frameborder='0' allowfullscreen></iframe></div>

Summary: After figuring out we had to use `docker.for.mac.localhost` as the hostname to connect our new Drupal 8 site to the old Drupal 7 site's MySQL database, we were able to run the `drush migrate-upgrade` command! But then it failed, because [Drush 10 is currently incompatible with `migrate-upgrade`](https://www.drupal.org/project/migrate_upgrade/issues/3093652). So we downgraded to Drush 9, then got `migrate-upgrade` to work! Once it was done, we were able to see all the available Drupal 7 to 8 migrations, and run them, but we ran into a few errors. We used [these instructions](https://github.com/geerlingguy/drupal-for-kubernetes/blob/master/docs/configure-and-reproduce.md#adding-a-module-and-exporting-drupals-configuration) to export the site's configuration to the codebase, and pushed the changes to the site's git repository. Then we reinstalled the site from scratch, to prove the configuration export and import worked well, and ran the migrations again, running into a new error, "Field discovery failed for Drupal core version 7," which we'll debug on _next week's_ episode!

## Episode 4 - Setting up CI with GitHub Actions and Overcoming Field Migration Issues

Streamed on: February 25, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/dE7IksPs9EY" frameborder='0' allowfullscreen></iframe></div>

Summary: We started off by setting up GitHub Actions for some basic Continuous Integration (CI) tests for Drupal, but quickly ran into a wall as GitHub experienced an outage and the Issue queue and Actions stopped working. So we switched back over to the migrations and found that all the issues like `Attempt to create a field storage field_project_images with no type.` meant that a field-related module was not enabled in Drupal 8. So we enabled the right modules (e.g. Date, Link, Taxonomy, Comment, Options, etc.), and ran the `migrate-upgrade` command again... which started generating duplicate migration entities, named like `upgrade_upgrade_upgrade_d7_thing.yml`. So to prevent confusion, I deleted _all_ migration configuration, reinstalled the site, re-exported the configuration, then ran `migrate-upgrade` yet again. It now created the migration entities with a single `upgrade_` prefix, which is much nicer to manage. I kicked off the migrations, and it got further along, and started migrating images (which took some time, as it had to download each image, save it to the Docker shared filesystem (which is slow) and create the file entity in the database (which is slow). So we cut off the episode there and will get back into running the migration again _next_ week!

## Episode 5 - Migrations (mostly) working, setting up CI on GitHub Actions

Streamed on: March 3, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/PMFSv5B4Z20" frameborder='0' allowfullscreen></iframe></div>

Summary: We installed a few new modules and re-ran a few migrations to try to get content to work correctly in the Drupal 8 site after it was migrated. GitHub was actually working today, so we were able to work on the CI process to install the site from configuration on every commit, and we now have some content ready for theming next week! Tune in next week to see how we start upgrading the theme from Drupal 7 to 8 with Twig, and see if Jeff could ever figure out what was causing the Drupal install to fail on GitHub Actions!

Resources:

  - [geerlingguy's dotfiles](https://github.com/geerlingguy/dotfiles)
  - [Using MySQL service with GitHub actions](https://firefart.at/post/using-mysql-service-with-github-actions/)

## Episode 6 - Setting up admin theme and jeffgeerling theme

Streamed on: March 10, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/o-LmI6PVKHc" frameborder='0' allowfullscreen></iframe></div>

Summary: We set up an admin theme after discussing Seven and Claro. We added the Admin Toolbar module for a nicer admin UI experience. Then we copied the 'jeffgeerling' theme over from my Drupal 7 site to Drupal 8, and started updating the theme components like the .info.yml and CSS libraries to work with Drupal 8! GitHub Actions is running now, so every time we push a new commit it is tested in a CI environment, yay!

Resources:

  - [Tina Mrak: Creating a custom theme in Drupal 8 livestream](https://www.youtube.com/watch?v=SiTo1cmipnA)
  - [Running Drupal 8.8 with the Symfony Local Server](https://www.oliverdavies.uk/articles/running-drupal-with-symfony-local-server/)
  - [Defining a theme with an .info.yml file](https://www.drupal.org/docs/8/theming-drupal-8/defining-a-theme-with-an-infoyml-file)
  - [Adding stylesheets (CSS) and JavaScript (JS) to a Drupal 8 theme](https://www.drupal.org/docs/8/theming/adding-stylesheets-css-and-javascript-js-to-a-drupal-8-theme)

## Episode 7 - Faster local dev environment, coronavirus, and theming the blog

Streaming on: March 17, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/T7gSB9as6DM" frameborder='0' allowfullscreen></iframe></div>

Summary: We mentioned the importance of coming together during the strange (and sometimes lonely!) times we live in with coronavirus and quarantines. We summarized a few things worked on between last episode and today, like a faster local development environment (trying Drupal VM, DDEV Local, and Symfony Local Server too!). We also ran through some pragmatic choices with regard to switching modules in Drupal 8 (and why I chose to stick with the older but working code filter module). Finally, we spent a half an hour working on making blog posts look the same on the Drupal 8 site as the Drupal 7 site.

Resources:

  - The [jeffgeerling-com codebase](https://github.com/geerlingguy/jeffgeerling-com) is now OPEN SOURCE on GitHub!
  - My books Ansible for DevOps and Ansible for Kubernetes are [free for the month of March](/blog/2020/you-can-get-my-devops-books-free-rest-month), to help those affected by coronavirus and the market downturn.
  - [Revisiting Docker for Mac's performance using NFS volumes](/blog/2020/revisiting-docker-macs-performance-nfs-volumes).

## Episode 8 - Migrating the Blog view from Drupal 7 to Drupal 8

Streaming on: March 24, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/v7S0BB6V7eA" frameborder='0' allowfullscreen></iframe></div>

Summary: Following the [weekly livestream agenda](https://github.com/geerlingguy/jeffgeerling-com/issues/34), we manually migrated the Blog view (which included a Blog landing page, a blog.xml RSS feed, and a 'Recent Blog Posts' block) from Drupal 7 to Drupal 8. Then we worked on styling and theming the Blog landing page, incorporating a theme hook suggestion to add a 'visually-hidden' class to the Blog landing page's title so it would not display but would still be present for those using screen readers.


we upgraded Drupal core from 8.8.2 to 8.8.4 using Composer. We also discussed some migration struggles with the naming of the database connection key (hint: it should be 'migrate'). Then we worked on theming the blog comments, and upgrading a template_preprocess_hook() function from Drupal 7 to Drupal 8.

## Episode 9 - Upgrade Drupal with Composer and Theming

Streaming on: March 31, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/VwFMx8vm8Rs" frameborder='0' allowfullscreen></iframe></div>

Summary: Following the [weekly livestream agenda](https://github.com/geerlingguy/jeffgeerling-com/issues/41), we upgraded Drupal core from 8.8.2 to 8.8.4 using Composer. We also discussed some migration struggles with the naming of the database connection key (hint: it should be 'migrate'). Then we worked on theming the blog comments, and upgrading a template_preprocess_hook() function from Drupal 7 to Drupal 8.

Resources:

  - [Update core via composer](https://www.drupal.org/docs/8/update/update-core-via-composer)
  - [Tips for Managing Drupal 8 projects with Composer](/blog/2017/tips-managing-drupal-8-projects-composer)
  - [Updating drupal/core with Composer - but Drupal core doesn't update](/blog/2018/updating-drupalcore-composer-drupal-core-doesnt-update)

## Episode 10 - Projects view and home page blocks migration

Streaming on: April 7, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/pX_5k0mO3sU" frameborder='0' allowfullscreen></iframe></div>

Summary: We mentioned the #DrupalCares effort to sustain the Drupal Association, we showed a brief clip of the 2007 rendering of the Drupal Song (https://www.youtube.com/watch?v=lZ-s3DRZJKY), we migrated the Projects listing, block, and feed from a View in Drupal 7 to Drupal 8, and we worked on finishing the Home Page migration from Drupal 7 to Drupal 8.

Resources:

  - [#DrupalCares - Sustaining the DA through the COVID-19 crisis](https://www.drupal.org/association/blog/drupalcares-sustaining-the-da-through-the-covid-19-crisis)
  - [How to attach a CSS or JS library to a View in Drupal 8](https://www.jeffgeerling.com/blog/2016/how-attach-css-or-js-library-view-drupal-8)

## Episode 11 - Redirects and... a slow laptop!

Streaming on: April 14, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Le82L7EAcaY" frameborder='0' allowfullscreen></iframe></div>

Summary: We worked on migrating redirects (using the [Redirect module](https://www.drupal.org/project/redirect) to preserve URLs and prevent link rot, and quickly realized how much OBS streaming software hurt the performance of Jeff's laptop, to the point where opening files was taking many seconds!

Resources:

  - [Every Day I'm Drupalin'](https://www.youtube.com/watch?v=PWjcqE3QKBg)
  - [Migrating path aliases into Drupal 8 redirects: Part 1](https://deninet.com/blog/2018/04/03/migrating-path-aliases-drupal-8-redirects-part-1)
  - [GitHub Issue: Ensure redirects are migrated into Drupal 8 site](https://github.com/geerlingguy/jeffgeerling-com/issues/1)

## Episode 12 - Pathauto and redirect SEO migration and config split

Streaming on: April 21, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Ql_-krnxv3U" frameborder='0' allowfullscreen></iframe></div>

Summary: We finished migrating redirects to preserve URLs and prevent link rot, added the pathauto module and a migration of pathauto patterns and settings, and started working on configuring a Configuration Split for the local development environment!

Resources:

  - [Episode Agenda](https://github.com/geerlingguy/jeffgeerling-com/issues/57)
  - [Drupal Song cover by NewHelix in the Philippines](https://www.youtube.com/watch?v=-Sw47x4UwdA)
  - [Redirect Metrics](https://www.drupal.org/project/redirect_metrics) module
  - [Trusted Host Settings documentation](https://www.drupal.org/docs/8/install/trusted-host-settings)
  - [Creating a simple dev environment configuration split](https://www.drupal.org/docs/8/modules/configuration-split/creating-a-simple-split-configuration-dev-modules-only-in-dev)

## Episode 13 - Config Split and Site Search

Streaming on: April 28, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/-FC68Sds-TE" frameborder='0' allowfullscreen></iframe></div>

Summary: We finished configuring a Configuration Split for the local development environment, and integrated the site with Hosted Apache Solr for site search!

Resources:

  - [Episode Agenda](https://github.com/geerlingguy/jeffgeerling-com/issues/60)
  - [Hosted Apache Solr](https://hostedapachesolr.com)

## Episode 14 - Dark Mode and Accessibility

Streaming on: May 5, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/gjNxY_5q7Xc" frameborder='0' allowfullscreen></iframe></div>

Summary: We touched up the Jeff Geerling.com theme, and made sure it's as accessible as we can make it!

Resources:

  - [How to do an accessibility review?](https://www.drupal.org/docs/8/accessibility/how-to-do-an-accessibility-review)
  - [Color contrast checker](https://contrast-ratio.com)
  - [Find accessibility problems using Firefox](https://hacks.mozilla.org/2019/10/auditing-for-accessibility-problems-with-firefox-developer-tools/)

## Episode 15 - Prepping for Go-Live!

Streaming on: May 12, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/SxR4N9inlYA" frameborder='0' allowfullscreen></iframe></div>

Summary: We did the final run-through of all the manual migration steps. Then we worked on setting up a new temporary domain for the site to run on, on the live production server—and accidentally took down the current production site! Whoops! Luckily, that was right at the end of the stream, and I was able to get it back up within about 5 minutes.

## Episode 16 - THE FINAL EPISODE - Live migration!

Streaming on: May 19, 2020

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/4ehIIFGtMRg" frameborder='0' allowfullscreen></iframe></div>

Summary: TBD.
