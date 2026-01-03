---
nid: 2747
title: "Adding Configuration Split to a Drupal site using BLT and Acquia Cloud"
slug: "adding-configuration-split-drupal-site-using-blt-and-acquia-cloud"
date: 2017-02-15T14:23:08+00:00
drupal:
  nid: 2747
  path: /blog/2017/adding-configuration-split-drupal-site-using-blt-and-acquia-cloud
  body_format: markdown
  redirects: []
tags:
  - blt
  - config
  - config split
  - configuration management
  - drupal
  - drupal 8
  - drupal planet
  - modules
---

> **Note**: As of Config Split beta4, you no longer need to use `drush csex/csim` to export and import config accounting for splits. You instead install both Config Filter and Config Split, then use the normal Drush commands (`drush cex/cim`). There are also a few other tweaks to the guide below; I may update it when I get more time.

I've been looking at a ton of different solutions to using Drupal 8's Configuration Management in a way that meets the following criteria:

  1. As easy (or almost as easy) as plain old `drush cex -y` to export and `drush cim -y` to import.
  2. Allows a full config export/import (so you don't have to use update hooks to do things like enable modules, delete fields, etc.).
  3. Allows environment-specific configuration and modules (so you don't have to have some sort of build system to tweak things post-config-import—Drupal should manage its own config).
  4. Allows certain configurations to be ignored/not overwritten on production (so content admins could, for example, manage Webforms or Contact Forms on prod, but not have to have a developer pull the database back and re-export config just to account for a new form).

The [Configuration Split](https://www.drupal.org/project/config_split) module checks off the first three of those four requirements, so I've been using it on a couple Drupal 8 sites that I'm building using Acquia's BLT and hosting on Acquia Cloud. The initial setup poses a bit of a challenge due to the 'chicken-and-egg' problem of needing to configure Config Split before being able to _use_ Config Split... therefore this blog post!

## Installing Config Split

{{< figure src="./config-split-setup.png" alt="Configuration Split setup - Drupal 8" width="650" height="282" class="insert-image" >}}

The first time you get things set up, you might already be using core CMI, or you might not yet. In my case, I'm not set up with config management at all, and BLT is currently configured out of the box to do a `--partial` config import, so I need to do a couple specific things to get started with Config Split:

  1. Add the module to your project with `composer require drupal/config_split:^1.0`.
  2. Deploy the codebase to production with the module in it (push a build to prod).
  3. On production, install the module either through the UI or via Drush (assuming you're not already using core CMI to manage extensions).
  4. On production, create one config split per Acquia Cloud environment, plus another one for `local` and `ci` (so I created `local`, `ci`, `dev`, `test`, and `prod`).
    - For each split, make sure the machine name matches the Acquia Cloud environment name, and for the path, use `../config/[environment-machine-name]`).
    - For Local, use `local`, for CI (Travis, Pipelines, etc.), use `ci` (for the machine names).
  5. Pull the production database back to all your other Acquia Cloud environments so Config Split will be enabled and configured identically in all of them.
  6 On your local, run `blt local:refresh` to get prod's database, which has the module enabled.

Note that there may be more efficient (and definitely more 'correct') ways of getting Config Split installed and configured initially—but this way works, and is quick for new projects that don't necessarily have a custom install profile or module where you can toss in an update hook to do everything automated.

## Configuring the Splits

Now that you have your local environment set up with the database version that has Config Split installed—and now that Config Split is installed in all the other environments using the same configuration, it's time to manage your first split—the local environment!

  1. Enable a module on your local environment that you only use for local dev (e.g. Devel).
  2. Configure the 'Local' config split (on http://local.example.com/admin/config/development/configuration/config-split/local/edit)
  3. Select the module for the Local split (e.g. select Devel in the 'Modules' listing).
  4. Select all the module's config items in the 'Blacklist' (use Command on Mac, or Ctrl on Windows to multi-select, e.g. select `devel.settings`, `devel.toolbar.settings`, and `system.menu.devel`).
  5. Click 'Save' to save the config split.

Now comes the important part—instead of using Drush's `config-export` command (`cex`), you want to make it a little... _spicier_:

    drush @project.local csex -y local

This command (`configuration-split-export`, `csex` for short) will dump all the configuration just like `cex`... but it splits out all the blacklisted config into the separate `config/local` directory in your repository!

> **Note**: If you get `Command csex needs the following extension(s) enabled to run: config_split.`, you might need to run `drush @project.local cc drush`. Weird drush bug.

Next up, you need to create a blank folder for each of the other splits—so create one folder each for ci, dev, test, and prod, then copy the `.htaccess` file that Config Split added to the `config/local` folder into each of the other folders.

We're not ready to start deploying config yet—we need to modify BLT to make sure it knows to run `csim` (short for `config-split-import`) instead of `cim --partial` when importing configuration on the other environments. It _also_ needs to know which `split` to use for each environment.

## Modifying BLT

For starters, see the following BLT issue for more information about trying to standardize the support for Configuration Split in BLT: [Support Config Split for environment-specific Core CMI](https://github.com/acquia/blt/issues/965).

  1. You need to override some BLT Phing tasks, so first things first, replace the `import: null` line in `blt/project.yml` with `import: '${repo.root}/blt/build.xml'`.
  2. Add a file in the `blt/` directory named `build.xml`, and paste in the contents of this gist: [https://gist.github.com/geerlingguy/1499e9e260652447c8b5a936b95440fa](https://gist.github.com/geerlingguy/1499e9e260652447c8b5a936b95440fa)
  3. Since you'll be managing all the modules via Config Split, you don't want or need BLT messing with modules during deployment, so clear out all the settings in `blt/project.yml` as is shown in this gist: [https://gist.github.com/geerlingguy/52789b6489d338cb3867e325e2e0a792](https://gist.github.com/geerlingguy/52789b6489d338cb3867e325e2e0a792)

Once you've made those two changes to BLT's `project.yml` and added a `blt/build.xml` file with your custom Phing tasks, it's time to test if this stuff is all working correctly! Go ahead and run:

    blt local:refresh

And see if the local environment is set up as it should be, with Devel enabled at the end of the process. If it is, congratulations! Time to commit this stuff and deploy it to the Cloud!

Once you deploy some code to a Cloud environment, in the build log, you should see something like:

```
The following directories will be used to merge configuration to import:
/mnt/www/html/project/docroot/../config/default
../config/dev
Import the configuration? (y/n): 
y
Configuration successfully imported from:                              [success]
/mnt/www/html/project/docroot/../config/default
../config/dev.
```

This means it's importing the default config, mixed in with all the dev config split directory. And that means it worked.

## Start deploying with impunity!

The great thing about using Drupal 8's core CMI the way it is _meant_ to be used (instead of using it with `--partial`) is that configuration management becomes a _total afterthought_!

Remember in Drupal 7 when you had to remember to export certain features? And when `features-revert-all` would sometimes bring with it a six hour debugging session as to what happened to your configuration?

Remember in Drupal 7 when you had to write hundreds of update hooks to do things like add field, delete a field, remove a content type, enable or disable a module?

With CMI, all of that is a distant memory. You do whatever you need to do—delete a field, add a view, enable a dozen modules, etc.—then you export configuration with `drush csex local`. Commit the code, push it up to prod, _et voilà_, it's magic! The same changes you made locally are on prod!

The _one_ major drawback to this approach (either with Config Split or just using core CMI alone without `--partial`) is that, at least at this time, it's an all-or-nothing approach. You can't, for example, allow admins on prod to create new Contact forms, Webforms, blocks, or menus without also pulling the database back, exporting the configuration, then pushing the exported config back to prod. If you forget to do that, CMI will happily delete all the new configuration that was added on prod, since it doesn't exist in the exported configuration!

If I can find a way to get that working with Config Split (e.g. say "ignore configuration for the `webform.` config namespace" without using `--partial`), I think I'll have found configuration nirvana in Drupal 8!
