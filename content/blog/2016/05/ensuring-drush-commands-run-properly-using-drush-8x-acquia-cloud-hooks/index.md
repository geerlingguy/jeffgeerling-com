---
nid: 2657
title: "Ensuring Drush commands run properly using Drush 8.x via Acquia Cloud Hooks"
slug: "ensuring-drush-commands-run-properly-using-drush-8x-acquia-cloud-hooks"
date: 2016-05-27T20:56:53+00:00
drupal:
  nid: 2657
  path: /blog/2016/ensuring-drush-commands-run-properly-using-drush-8x-acquia-cloud-hooks
  body_format: markdown
  redirects: []
tags:
  - acquia
  - cloud hooks
  - drupal 8
  - drupal planet
  - drush
---

Any time there are major new versions of software, some of the tooling surrounding the software requires tweaks before everything works like it used to, or as it's documented. Since Drupal 8 and Drush 8 are both relatively young, I expect some growing pains here and there.

One problem I ran into lately was quite a head-scratcher: On Acquia Cloud, I had a cloud hook set up that was supposed to do the following after code deployments:

```
# Build a Drush alias (e.g. [subscription].[environment]).
drush_alias=${site}'.'${target_env}

# Run database updates.
drush @${drush_alias} updb -y

# Import configuration from code.
drush @${drush_alias} cim vcs
```

This code (well, with `fra -y` instead of `cim`) works fine for some Drupal 7 sites I work on in Acquia Cloud, but it seems that database updates were detected but never run, and configuration changes were detected but never made... it took a little time to see what was happening, but I eventually figured it out.

**The tl;dr fix?**

```
# Add --strict=0 to resolve the error Drush was throwing due to alias formatting.
drush @${drush_alias} updb -y --strict=0

# I forgot a -y, so Drush never actually executed the changes!
drush @${drush_alias} cim -y vcs
```

For the first issue, Acquia cloud generates its own Drush alias files, and in all the aliases, it includes some options like `site` and `env`. It seems that Drush < 8 would just ignore extra options like those... but Drush 8.x throws an error and stops execution for the current task because of those extra variables. Using `--strict=0` tells Drush to squelch any erros thrown by those extra options. Eventually, I'm guessing Acquia Cloud's Drush aliases will be made to be fully-compatible with Drush 8.x, but this workaround is fine for now.

For the second issue, it was just my boneheadedness... if you're running any command that requires a prompt non-interactively (e.g. through an automated system like cloud hooks), you have to add the 'assume-yes' option, `-y`, just like I used to with `fra -y` in Drupal 7!

Before, I would get the following error message on every Cloud deployment:

```
The following updates are pending:

custom module : 
  8001 -   Add customizations. 

Do you wish to run all pending updates? (y/n): y
Unknown options: --site, --env.  See `drush help                         [error]
updatedb-batch-process` for available options. To suppress this
error, add the option --strict=0.
Unknown options: --site, --env.  See `drush help cache-rebuild` for      [error]
available options. To suppress this error, add the option --strict=0.
Finished performing updates.                                                [ok]
```

Even though it says 'Finished performing updates', they didn't actually get run. Now it runs the updates without any issue:

```
The following updates are pending:

custom module : 
  8001 -   Add customizations. 

Do you wish to run all pending updates? (y/n): y
Performing custom_update_8001                                                                              [ok]
Cache rebuild complete.                                                                                      [ok]
Finished performing updates.                                                                                 [ok]
```

