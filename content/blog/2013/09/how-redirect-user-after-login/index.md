---
nid: 2432
title: "How to redirect a user after login to a specific page"
slug: "how-redirect-user-after-login"
date: 2013-09-30T13:13:28+00:00
drupal:
  nid: 2432
  path: /blogs/jeff-geerling/how-redirect-user-after-login
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal_goto
  - login
  - redirect
aliases:
  - /blogs/jeff-geerling/how-redirect-user-after-login
---

There are some simple Drupal modules that help with login redirection (especially <a href="https://drupal.org/project/login_destination">Login Destination</a>), but I often need more advanced conditions applied to redirects, so I like being able to do the redirect inside a custom module. You can also do something similar with Rules, but if the site you're working on doesn't have Rules enabled, all you need to do is:

<ol>
<li>Implement <code>hook_user_login()</code>.</li>
<li>Override <code>$_GET['destination']</code>.</li>
</ol>

The following example shows how to redirect a user logging in from the 'example' page to the home page (Drupal uses <code><front></code> to signify the home page):

```php
<?php
/**
 * Implements hook_user_login().
 */
function mymodule_user_login(&$edit, $account) {
  $current_path = drupal_get_path_alias($_GET['q']);

  // If the user is logging in from the 'example' page, redirect to front.
  if ($current_path == 'example') {
    $_GET['destination'] = '<front>';
  }
}
?>
```

Editing <code>$edit['redirect']</code> or using <code>drupal_goto()</code> inside hook_user_login() doesn't seem to do anything, and setting a Location header using PHP is not best practice. Drupal uses the destination parameter to do custom redirects, so setting it anywhere during the login process will work correctly with Drupal's built in redirection mechanisms.
