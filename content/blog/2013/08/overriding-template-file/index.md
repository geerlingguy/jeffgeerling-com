---
nid: 2422
title: "Overriding a template file (.tpl.php) from a module"
slug: "overriding-template-file"
date: 2013-08-21T13:44:06+00:00
drupal:
  nid: 2422
  path: /blogs/jeff-geerling/overriding-template-file
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - modules
  - templates
  - theme
---

There are many times when a custom module provides functionality that requires a tweaked or radically altered template file, either for a node, a field, a view, or something else.

While it's often a better idea to use a preprocess or alter function to accomplish what you're doing, there are many times where you need to change the markup/structure of the HTML, and modifying a template directly is the only way to do it. In these cases, if you're writing a generic custom module that needs to be shared among different sites with different themes, you can't just throw the modified template into each theme, because you'd have to make sure each of the sites' themes has the same file, and updating it would be a tough proposition.

I like to keep module-based functionality inside modules themselves, so I put all templates that do specific things relating to that module into a 'templates' subdirectory.

In my example, I'd like to override <code>field-collection-item.tpl.php</code>, which is included with the Field collection module. To do so, I copy the default template into my custom module's 'templates' folder, and modify it how I like. Then I implement <a href="https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_theme_registry_alter/7"><code>hook_theme_registry_alter()</code></a> to tell Drupal where my template exists:

```
<?php
/**
 * Implements hook_theme_registry_alter().
 */
function custom_theme_registry_alter(&$theme_registry) {
  // Override the default field-collection-item.tpl.php with our own.
  if (isset($theme_registry['field_collection_item'])) {
    $module_path = drupal_get_path('module', 'custom');
    $theme_registry['field_collection_item']['theme path'] = $module_path;
    $theme_registry['field_collection_item']['template'] = $module_path . '/templates/field-collection-item';
  }
}
?>
```

This presumes my module's machine name is 'custom'. Make sure you clear all caches after adding this hook, so Drupal will pick up the hook and your new template!

Note that there are sometimes other/better ways of overriding templates in your module—for example, the views module lets you set a template directory path in <code>hook_views_api()</code>, and will automatically pick up templates from your module. And note again that preprocess and alter hooks are often a better way to go to accomplish small tweaks to content and markup for nodes, fields, views, etc.
