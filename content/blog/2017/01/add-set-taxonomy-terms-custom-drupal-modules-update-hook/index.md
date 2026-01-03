---
nid: 2729
title: "Add a set of Taxonomy terms via a custom Drupal module's update hook"
slug: "add-set-taxonomy-terms-custom-drupal-modules-update-hook"
date: 2017-01-10T03:06:48+00:00
drupal:
  nid: 2729
  path: /blog/2017/add-set-taxonomy-terms-custom-drupal-modules-update-hook
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal 8
  - drupal planet
  - php
  - taxonomy
---

From time to time, I've needed to have a default set of Taxonomy terms created at the same time as a content type, as in the case of a field with a required Taxonomy term reference, using a Taxonomy that is not 'free tag' style.

Instead of requiring someone to go in and manually add all the terms after code is deployed, you can add terms in a custom module's update hook, like so:

```
<?php
// Put the following line in the top of the .install file:
use Drupal\taxonomy\Entity\Term;

/**
 * Add some terms to the Category vocabulary.
 */
function modulename_update_8001() {
  // Machine name of the Taxonomy vocabulary.
  $vocab = 'category';

  // Term names to be added.
  $items = [
    'Blue',
    'Red',
    'Hot Pink',
  ];
  foreach ($items as $item) {
    $term = Term::create(array(
      'parent' => array(),
      'name' => $item,
      'vid' => $vocab,
    ))->save();
  }
}
?>
```

This assumes you want to add terms to a Taxonomy with machine name `category`, and your module's machine name is `modulename`. If you're using Core CMI for configuration management, and you need to deploy a new custom module to do an update like this, you could create the module locally, enable it on your local site, then export the configuration locally so the module gets enabled automatically through the `core.extension.yml` configuration file.

> If you just created the module and this is the first thing you're doing with it (e.g. if this is a brand new custom module), you'll also need to add a `hook_install()` invocation, and inside it, call the update hook that installs the taxonomy terms (`modulename_update_8001()`). Otherwise, you could even put the code that creates the terms directly in `mymodulename_install()`.

A quick note on `hook_update_N()` functions in Drupal 8: make sure you start the sequence of update hooks with `8001` and not `8000`, otherwise strange things can happen to your module's schema!
