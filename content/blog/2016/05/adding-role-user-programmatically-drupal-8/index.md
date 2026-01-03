---
nid: 2652
title: "Adding a role to a user programmatically in Drupal 8"
slug: "adding-role-user-programmatically-drupal-8"
date: 2016-05-18T14:18:04+00:00
drupal:
  nid: 2652
  path: /blog/2016/adding-role-user-programmatically-drupal-8
  body_format: markdown
  redirects: []
tags:
  - drupal 8
  - drupal planet
  - drush
  - oop
  - php
  - roles
  - users
---

Since a quick Google search didn't bring up how to do this in Drupal 8 (there are dozens of posts on how to do it in Drupal 7), I thought I'd post a quick blog post on how you can modify a user's roles in Drupal 8. Hint: It's a lot easier than you'd think!

In Drupal 7, `$user` was an object... but it was more like an object that acted like a dumb storage container. You couldn't really do anything with it directly—instead, you had to stick it in functions (like `user_multiple_role_edit()`) to do things like add or remove roles or modify account information.

In Drupal 8, `$user` is a real, useful object. Want to modify the account name and save the change?

```
<code>
<?php
$user->setUsername('new-username');
$user->save();
?>
```

</code>

There are now dozens of simple methods you can call on a user object to get and set information on a `$user` object, and what used to be a little annoying in Drupal 7 (modifying a user's roles) is now very straightforward. Let's say I want to add the 'administrator' role to a user account:

```
<code>
<?php
$user->addRole('administrator');
$user->save();
?>
```

</code>

Done!

Want to remove the role?

```
<code>
<?php
$user->removeRole('administrator');
$user->save();
?>
```

</code>

Added bonus—you no longer need to retrieve a role ID using `user_role_load_by_name()`, because in Drupal 8 [role IDs are now machine readable strings](https://www.drupal.org/node/1619504)!

I often need to add a drush command that can be run in non-production environments that will make certain users administrators (e.g. developers who need full access in non-prod, but shouldn't have full access on production), and using this new logic, it's extremely easy to build a drush command to do this.

First, create a drush command file (I generally create them in the `drush` folder in the site's docroot, titled `[command].drush.inc`). In my case, I created `npadmin.drush.inc` (for "Non-Prod Admin"), with the following contents:

```
<code>
<?php

/**
 * @file
 * Non-production admins drush command.
 */

/**
 * Implements hook_drush_command().
 */
function npadmin_drush_command() {
  $items = [];

  $items['non-prod-admins'] = [
    'description' => "Makes certain users administrators in non-prod environments.",
    'examples' => [
      'drush npadmin' => 'Make certain users admins in non-prod environments.',
    ],
    'aliases' => ['npadmin'],
  ];

  return $items;
}

/**
 * Implements drush_hook_COMMAND().
 */
function drush_npadmin_non_prod_admins() {
  $users_changed = 0;

  // List of users who should be made administrators in non-prod environments.
  $users_to_make_admin = [
    'jeff.geerling',
    'etc...',
  ];

  foreach ($users_to_make_admin as $name) {
    $user = user_load_by_name($name);
    if ($user) {
      $user->addRole('administrator');
      $user->save();
      $users_changed++;
    }
  }

  drush_log(dt('Assigned the administrator role to !count users.', ['!count' => $users_changed]), 'ok');
}
?>
```

</code>

After creating the Drush command file, clear Drush's cache (`drush cc drush`), and then run `drush npadmin` in whichever environments should have these users become administrators.

Going further, you could turn `$users_to_make_admin` into a configuration item, so you could change it without changing code (in Drupal 7, I often used a variable for this purpose).

Programmatically managing a user's roles is a great example of OOP code in Drupal 8 making programming more simple and logical. Check out [UserInterface](https://api.drupal.org/api/drupal/core%21modules%21user%21src%21UserInterface.php/interface/UserInterface/8.2.x) for many more methods you can call on a user object!
