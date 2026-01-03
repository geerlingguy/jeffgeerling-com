---
nid: 2677
title: "Hide the page title depending on a checkbox field in a particular content type"
slug: "hide-page-title-depending-on-checkbox-field-particular-content-type"
date: 2016-08-01T22:55:45+00:00
drupal:
  nid: 2677
  path: /blog/2016/hide-page-title-depending-on-checkbox-field-particular-content-type
  body_format: markdown
  redirects: []
tags:
  - content
  - drupal
  - drupal 8
  - drupal planet
  - theming
---

In Drupal 8, many small things have changed, but my willingness to quickly hack something out in a few lines of code/config instead of installing a relatively large module to do the same thing hasn't :-)

I needed to add a checkbox to control whether the page title should be visible in the rendered page for a certain content type on a Drupal 8 site, and there are a few different ways you can do this (please suggest alternatives—especially if they're more elegant!), but I chose to do the following:

  1. Add a 'Display Title' boolean field (checkbox, using the field label as the title, and setting off to `0` and on to `1` in the field settings) to the content type (`page` in this example).
      
      {{< figure src="./page-title-display-checkbox-drupal-8.png" alt="Drupal 8 Basic Page &#39;Display Title&#39; checkbox" width="387" height="150" class="insert-image" >}}
  2. Make sure this field is not set to be displayed in the content type's display settings.
  3. In my theme's `hook_preprocess_page` (inside `themename.theme`), add the following:

```
<?php
/**
 * Implements hook_preprocess_page().
 */
function themename_preprocess_page(&$variables) {
  // Hide title on basic page if configured.
  if ($node = \Drupal::routeMatch()->getParameter('node')) {
    if ($node->getType() == 'page') {
      if (!$node->field_display_title->value) {
        unset($variables['page']['content']['mysite_page_title']);
      }
    }
  }
}
?>
```

`mysite_page_title` is the machine name of the block that you have placed on the block layout page (`/admin/structure/block`) with the page title in it.

After doing this and clearing caches, the page title for Basic Page content was easy to show and hide based on that simple checkbox. Or you can use the [Exclude Node Title](https://www.drupal.org/project/exclude_node_title) module, if you don't want to get your hands dirty!
