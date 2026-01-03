---
nid: 2297
title: "Using hook_init() to include CSS and JS files"
slug: "using-hookinit-include-css-and"
date: 2010-12-28T20:21:20+00:00
drupal:
  nid: 2297
  path: /blogs/jeff-geerling/using-hookinit-include-css-and
  body_format: full_html
  redirects: []
tags:
  - css
  - drupal
  - javascript
  - modules
---

<p>For some time, I've been using the most hackish ways of including custom CSS and Javascript in my site via themes and custom modules. The problem has been (at least, in Drupal 6) that the hook_preprocess_page() function, inside which I'd really like to include my drupal_add_css() and drupal_add_js() functions, due to the fact that it's easy to see what page I'm on, or what kind of page I'm on, is not able to add CSS or JS to the page, due to the order in which the hooks are fired.</p>
<p>I've often just put my JS and CSS includes (via the drupal hooks) into the end of my custom module file, instead of inside a function at all.</p>
<p>However, a much cleaner way to include your CSS and JS is inside your own implementation of hook_init(). For example:</p>
<pre>

```
<?php
/**
 * Implementation of hook_init().
 */
function custom_init() {

  // Add custom CSS & JS to front page.
  if (drupal_is_front_page()) {
    drupal_add_css(drupal_get_path('theme', 'custom') .'/css/sample.css', 'theme', 'screen,projection', FALSE);
    drupal_add_js(drupal_get_path('theme', 'custom') .'/js/sample.js', 'theme', 'header', FALSE, TRUE, FALSE);
  }

  // Add Javascript to a specific Context
  if (context_isset('context', 'blog')) {
    drupal_add_js(drupal_get_path('theme', 'custom') .'/js/blog-sample.js', 'theme', 'header', FALSE, TRUE, FALSE);
  }

}
?>
```

</pre>
<p>There! Much nicer. (This code is adapted from a sample sent to me by Joel Stein).</p>
