---
nid: 2324
title: "Disabling Autocomplete on forms in Drupal 6 or 7 - Forms API"
slug: "disabling-autocomplete-forms"
date: 2011-07-06T17:06:32+00:00
drupal:
  nid: 2324
  path: /blogs/jeff-geerling/disabling-autocomplete-forms
  body_format: full_html
  redirects: []
tags:
  - autocomplete
  - drupal
  - drupal 6
  - drupal 7
  - forms api
  - hook_form_alter
  - ux
aliases:
  - /blogs/jeff-geerling/disabling-autocomplete-forms
---

With the awesome new #states implementation in Drupal 7, and for form usability in general, it's often good to be able to selectively, or completely, disable form autocompletion for your users. One example I just encountered was a form that has two fields that are alternatively shown or hidden depending on the value of a checkbox earlier in the form. However, Google Chrome, in its infinite wisdom, was autofilling the hidden field, which shouldn't have a value if hidden, so I had to set the input's 'autocomplete' value to 'off.'

For simple textfields, here's how you could do that in a hook_form_alter() (in this example, I was disabling autocomplete on the user registration form's email field):

```
<?php
  // Disable autocomplete on the 'mail' field.
  $form['account']['mail']['#attributes']['autocomplete'] = 'off';
?>
```

There are a few fields where you'll need to do a bit more work, though, including the 'password' or 'change password' fields, a 'cck phone' field, etc. To turn off autocomplete via the forms API, you'll need to do two steps: first, add a process function to the field, then, in the process function, add your autocomplete value to the $element. For example:

```
<?php
  // Add our custom module's element process function (this would be in hook_form_alter).
  $form['field_phone']['und'][0]['#process'][] = '_custom_cck_phone_process';
  
// ... later in your module ...
  
function _custom_cck_phone_process($element, &$form_state, $form) {
  // Add 'autocomplete="off"' to the input field.
  $element['number']['#attributes']['autocomplete'] = 'off';
  return $element;
}
?>
```

You should be able to selectively disable autocomplete on any given form field using one of the two above methods. Now, what if you want to disable autocomplete on a whole form? (I sometimes do this for more security-conscious sites, even though it's more of a ux concern, in my mind, than a security concern—people are typically more comfortable filling out the form themselves).

Easy peasy. Put this inside your hook_form_alter():

```
<?php
  // Disable autocomplete for the entire form.
  $form['#attributes']['autocomplete'] = 'off';
?>
```

