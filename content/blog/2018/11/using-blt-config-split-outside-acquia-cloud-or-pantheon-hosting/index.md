---
nid: 2885
title: "Using BLT with Config Split outside Acquia Cloud or Pantheon Hosting"
slug: "using-blt-config-split-outside-acquia-cloud-or-pantheon-hosting"
date: 2018-11-02T20:09:05+00:00
drupal:
  nid: 2885
  path: /blog/2018/using-blt-config-split-outside-acquia-cloud-or-pantheon-hosting
  body_format: markdown
  redirects: []
tags:
  - blt
  - config split
  - configuration management
  - drupal
  - drupal 8
  - drupal planet
  - kubernetes
---

I am currently building a Drupal 8 application which is running outside Acquia Cloud, and I noticed there are a few 'magic' settings I'm used to working on Acquia Cloud which don't work if you aren't inside an Acquia or Pantheon environment; most notably, the automatic Configuration Split settings choice (for environments like `local`, `dev`, and `prod`) don't work if you're in a custom hosting environment.

You have to basically reset the settings BLT provides, and tell Drupal which config split should be active based on your own logic. In my case, I have a site which only has a local, ci, and prod environment. To override the settings defined in BLT's included `config.settings.php` file, I created a `config.settings.php` file in my site in the path `docroot/sites/settings/config.settings.php`, and I put in the following contents:

```
<?php
/**
 * Settings overrides for configuration management.
 */

// Disable all splits which may have been enabled by BLT's configuration.
foreach ($split_envs as $split_env) {
  $config["$split_filename_prefix.$split_env"]['status'] = FALSE;
}

$split = 'none';

// Local env.
if ($is_local_env) {
  $split = 'local';
}
// CI env.
if ($is_ci_env) {
  $split = 'ci';
}
// Prod env.
if (getenv('K8S_ENVIRONMENT') == 'prod') {
  $split = 'prod';
}

// Enable the environment split only if it exists.
if ($split != 'none') {
  $config["$split_filename_prefix.$split"]['status'] = TRUE;
}
```

The `K8S_ENVIRONMENT` refers to an environment variable I have set up in the production Kubernetes cluster where the BLT Drupal 8 codebase is running. There are a few other little tweaks I've made to make this BLT project build and run inside a Kubernetes cluster, but I'll leave those for another blog post and another day :)
