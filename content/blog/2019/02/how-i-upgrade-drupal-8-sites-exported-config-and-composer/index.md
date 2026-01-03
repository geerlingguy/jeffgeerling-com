---
nid: 2909
title: "How I upgrade Drupal 8 Sites with exported config and Composer"
slug: "how-i-upgrade-drupal-8-sites-exported-config-and-composer"
date: 2019-02-20T20:03:39+00:00
drupal:
  nid: 2909
  path: /blog/2019/how-i-upgrade-drupal-8-sites-exported-config-and-composer
  body_format: markdown
  redirects: []
tags:
  - composer
  - deployment
  - drupal
  - drupal 8
  - drupal planet
  - update
  - upgrade
---

> **tl;dr**: See the video below for a run-through of my process upgrading Drupal core on the real-world open source Drupal 8 site codebase [Drupal Example for Kubernetes](https://github.com/geerlingguy/drupal-for-kubernetes).

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/5ZpKCx3Zbcc" frameborder='0' allowfullscreen></iframe></div>

Over the years, as Drupal has evolved, the upgrade process has become a bit more involved; as with most web applications, Drupal's increasing complexity extends to _deployment_, and whether you end up running Drupal on a VPS, a bare metal server, in Docker containers, or in a Kubernetes cluster, you should formalize an update process to make sure upgrades are as close to non-events as possible.

Gone are the days (at least for most sites) where you could just download a 'tarball' (.tar.gz) from Drupal.org, expand it, then upload it via SFTP to a server and run Drupal's update.php. That workflow (and even a workflow like `drush up` of old) might still work for some sites, but it is fragile and prone to cause issues whether you notice them or not. Plus if you're using Drush to do this, it's no longer supported in modern versions of Drush!

So without further ado, here is the process I've settled on for all the Drupal 8 sites I currently manage (note that I've [converted all my non-Composer Drupal codebases to Composer](/blog/2018/converting-non-composer-drupal-codebase-use-composer) at this point):

  1. Make sure you local codebase is up to date with what's currently in production (e.g. `git pull origin master` (or `upstream` or whatever git remote has your current production code)).
  1. Reinstall your local site in your local environment so it is completely reset (e.g. `blt setup` or `drush site-install --existing-config`).
     _I usually use a local environment like [Drupal VM](https://www.drupalvm.com) or a Docker Compose environment, so I can usually just log in and run one command to reinstall Drupal from scratch._
  1. Make sure the local site is running well. Consider running `behat` and/or `phpunit` tests to confirm they're working (if you have any).
  1. Run `composer update` (or `composer update [specific packages]`).
  1. On your local site, run database updates (e.g. `drush updb -y` or go to `/update.php`).
     _This is important because the next step—exporting config—can cause problems if you're dealing with an outdated schema.
  1. Make sure the local site is still running well after updates complete. Run `behat` and/or `phpunit` tests again (if you have any).
  1. If everything passed muster, export your configuration (e.g. `drush cex -y` if using core configuration management, `drush csex -y` if using [Config Split](https://www.drupal.org/project/config_split)).
  1. (Optional but recommended for completeness) Reinstall the local site again, and run any tests again, to confirm the fresh install with the new config works perfectly.
  1. If everything looks good, it's time to commit all the changes to `composer.lock` and any other changed config files, and push it up to `master`!
  1. Run your normal deployment process to deploy the code to production.

All done!

That last step ("Run your normal deployment process") might be a little painful too, and I conveniently don't discuss it in this post. Don't worry, I'm working on a few future blog posts on that very topic!

For now, I'd encourage you to look into [how Acquia BLT builds shippable 'build artifacts'](https://blt.readthedocs.io/en/latest/deploy/), as that's by far the most reliable way to ship your code to production if you care about stability! Note that for a few of my sites, I use a more simplistic "pull from master, run `composer install`, and run `drush updb -y` workflow for deployments. But that's for my smaller sites where I don't need any extra process and a few minutes' outage won't hurt!
