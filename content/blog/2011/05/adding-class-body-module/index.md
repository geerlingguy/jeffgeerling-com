---
nid: 2321
title: "Adding a class to <body> in a module in Drupal 7"
slug: "adding-class-body-module"
date: 2011-05-27T23:22:00+00:00
drupal:
  nid: 2321
  path: /blogs/jeff-geerling/adding-class-body-module
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - hook_preprocess
  - modules
  - templates
  - variables
aliases:
  - /blogs/jeff-geerling/adding-class-body-module
---

In Drupal 6, I would often resort to using my theme's template.php file to implement <a href="http://api.drupal.org/api/drupal/includes--theme.inc/function/template_preprocess/6">template_preprocess()</a>, and add in the class to Drupal's $body_classes array. In Drupal 7, some new hooks were introduced that allow me to do this more easily, and inside my .module files.

Introducing <code>hook_preprocess_HOOK()</code>

```
<?php
/**
 * Implements hook_preprocess_HOOK().
 */
function custom_preprocess_html(&$vars) {
  $vars['classes_array'][] = 'my-class-here';
}
?>
```

You can literally hook into any hook's preprocess function. In the code above (inside a custom.module for one of my sites), I added a class to the html.tpl.php 'classes_array,' but you can manipulate any variable going to any template_preprocess function by simply hooking into it using <code>hook_preprocess_html()</code>. If you want to see all the different hooks available on a given page (that you can hook into), put the following code into your own custom.module:

```
<?php
/**
 * Implements hook_preprocess().
 */
function custom_preprocess(&$variables, $hook) {
  // Print out all the preprocess_ hooks available on a given page.
  dpm($hook); // dpm() requires devel.module to be enabled.
}
?>
```

Apparently hook_preprocess() worked somewhat in Drupal 6, but I didn't find much documentation for the hook :-/
