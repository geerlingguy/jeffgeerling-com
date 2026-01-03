---
nid: 2330
title: "jQuery Code to Select Textarea or Text Input Field when Selected"
slug: "jquery-code-select-textarea-or"
date: 2011-08-19T18:49:58+00:00
drupal:
  nid: 2330
  path: /blogs/jeff-geerling/jquery-code-select-textarea-or
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - hook_form_alter
  - javascript
  - jquery
  - usability
aliases:
  - /blogs/jeff-geerling/jquery-code-select-textarea-or
---

On one Drupal site I'm developing, there is an 'embed code generator' in one of the site's forms. This embed code capability is similar to Twitter's embeddable timeline widget, in that a user can select some parameters (colors, mostly), then some code (usually an iframe with the contents provided by an external site) is printed in a textarea, which the user can select, and paste into his own site's HTML.

To help the user in the task of selecting the code, the entire contents of the textarea or textfield is highlighted when the user clicks any part, which ensures that the user will get every last bit of code without having to select and drag his mouse around the text box (sometimes I've seen people missing part of a tag, which makes the embed fail to load). That's what we want to do, inside our own Drupal form.

First, in the drupal form itself (or via an hook_form_alter()), we need to attach a javascript file in our custom module (in this example, I assume you have a module called custom.module, and a js file named 'custom.select-helper.js' in your custom module's directory, inside a 'js' folder):

```
<?php
  // Attach the javascript inside a form definition or hook_form_alter().
  $form['#attached']['js'][] = drupal_get_path('module', 'custom') . '/js/custom.select-helper.js';
?>
```

Then, for the javascript file, we'll need to do two steps (the JS below assumes you're using Drupal 7 - it would need modification to work properly in Drupal 6). First, we select all the text inside the textarea or textfield (as selected via a CSS-style descendant selector), then we disable the browser's default behavior on the mouseup event (because of <a href="">this WebKit bug</a>):

<pre>
(function ($) {
Drupal.behaviors.customEmbed = {
  attach: function(context, settings) {

    // Select the contents of the embed code textareas.
    $('.embed-form .form-textarea-wrapper textarea, .embed-form .form-type-textfield input').focus(function() {
      this.select();
    });

    // preventDefault required for Chrome/Safari/WebKit due to bug:
    // https://bugs.webkit.org/show_bug.cgi?id=22691
    $(".embed-form .form-textarea-wrapper textarea, .embed-form .form-type-textfield input").mouseup(function(e){
      e.preventDefault();
    });

  }
};
})(jQuery);
</pre>
