---
nid: 2678
title: "How to attach a CSS or JS library to a View in Drupal 8"
slug: "how-attach-css-or-js-library-view-drupal-8"
date: 2016-08-04T15:21:37+00:00
drupal:
  nid: 2678
  path: /blog/2020/how-attach-css-or-js-library-view-drupal-8
  body_format: markdown
  redirects:
    - /blog/2016/how-attach-css-or-js-library-view-drupal-8
aliases:
  - /blog/2016/how-attach-css-or-js-library-view-drupal-8
tags:
  - cache
  - css
  - drupal
  - drupal 8
  - drupal planet
  - libraries
  - render api
  - views
---

File this one under the 'it's obvious, but only after you've done it' category—I needed to attach a CSS library to a view in Drupal 8 via a custom module so that, wherever the view displayed on the site, the custom CSS file from my module was attached. The process for CSS and JS libraries is pretty much identical, but here's how I added a CSS file as a library, and made sure it was attached to my view:

## Add the CSS file as a library

In Drupal 8, [`drupal_add_css()`, `drupal_add_js()`, and `drupal_add_library()` were removed](https://www.drupal.org/node/2169605) (for various reasons), and now, to attach CSS or JS assets to views, nodes, etc., you need to use Drupal's `#attached` functionality to 'attach' assets (like CSS and JS) to rendered elements on the page.

In my custom module (`custom.module`) or custom theme (`custom.theme`), I added the CSS file `css/custom_view.css`:

```
.some-class {
  color: #000;
}
```

Then, to tell Drupal about the CSS file, I added it as a library inside `custom.libraries.yml` (alongside the `.module` or `.theme` file):

```
custom_view:
  css:
    component:
      css/custom_view.css: {}
```

In this case, the library's name is the top-level element (`custom-view`), so when I later want to attach this new library to a page, node, view, etc., I can refer to it as `custom/custom_view` (basically, `[module_name]/[library_name]`).

## Attach the library to your view

Thank goodness for tests! I was looking through the Drupal core issue queue for issues mentioning views using #attached, and eventually found a patch that referred to the test <a href="https://api.drupal.org/api/drupal/core!modules!views!tests!modules!views_test_data!views_test_data.views_execution.inc/function/views_test_data_views_pre_render/8.2.x">`views_test_data_views_pre_render()`</a>, which tests the ability to alter a view using the pre-render hook, and thankfully includes an example for attaching a library.

In my case, learning from that test, I want to attach the library to my view by the view ID (in my case `super_awesome_view`), so I added the following hook in my `.module` file (you can also add it in a theme via the `.theme` file):

```
// Put this line near the top of your .module or .theme file.
use Drupal\views\ViewExecutable;

/**
 * Implements hook_views_pre_render().
 */
function custom_views_pre_render(ViewExecutable $view) {
  if (isset($view) && ($view->storage->id() == 'super_awesome_view')) {
    $view->element['#attached']['library'][] = 'custom/custom_view';
  }
}
```

You may be wondering, "What was wrong in the old days with the simplicity of `drupal_add_css()`? Well, the main reason why much of [Drupal 8's awesome caching abilities](/blog/2016/yes-drupal-8-slower-drupal-7-heres-why) are possible is due to the fact that all rendered markup can have cacheability metadata attached, and attaching CSS and Javascript like this allows that caching system to work automatically. In Drupal 7, it was just too messy when any code anywhere could toss in a random stylesheet or JS file outside of Drupal's more rigid Render API.
