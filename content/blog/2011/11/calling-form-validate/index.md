---
nid: 2348
title: "Calling form validate functions in include files from other modules"
slug: "calling-form-validate"
date: 2011-11-30T21:52:24+00:00
drupal:
  nid: 2348
  path: /blogs/jeff-geerling/calling-form-validate
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - forms api
  - validation
aliases:
  - /blogs/jeff-geerling/calling-form-validate
---

<strong>Update:</strong> See comments below, and completely ignore this post. Nothing to see here...


```
module_load_include()</code> is a great way to add code from other module's include files, but it doesn't always work as you'd expect. Recently, I was building a form in one module that pulled up a validation function from another module when a particular submit button was pressed:

<code>
<?php
  module_load_include('inc', 'another_module', 'includes/another_module.forms');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Awesome Submit Button'),
    '#validate' => array('another_module_form_validate_function'),
  );
?>
```

I thought just adding in the module_load_include() would work, but alas, there was more to it than that. Instead of going about it this way, I had to call a local form validation function, and in <em>that</em> function, I could load the include from another module and call it's validation function:

```
<?php
    '#validate' => array('same_module_form_validate'),
...
function same_module_form_validate($form, &$form_state) {
  // Pass off validation to other module.
  module_load_include('inc', 'another_module', 'includes/another_module.forms');
  another_module_form_validate_function($form, $form_state);
}
?>
```

This helps me uphold DRY principles, and reuse specific form validation functions from other module's include files. (Typically, though, if I were going to be validating a particular element, or a bunch of different forms, using the same validation function, I would include that validation in the .module file itself so I could call it anywhere without a module_load_include()... but in this case, I didn't want that particular validation function to have to be in memory on every Drupal page request :).
