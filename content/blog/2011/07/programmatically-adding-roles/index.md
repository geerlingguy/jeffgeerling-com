---
nid: 2338
title: "Programmatically adding and removing roles to users in Drupal"
slug: "programmatically-adding-roles"
date: 2011-07-01T20:37:20+00:00
drupal:
  nid: 2338
  path: /blogs/jeff-geerling/programmatically-adding-roles
  body_format: markdown
  redirects: []
tags:
  - code
  - drupal
  - drupal 6
  - drupal 7
  - drupal planet
  - users
---

[UPDATE: <a href="http://www.computerminds.co.uk/articles/quick-tips-adding-role-user-drupal-7">Here is a much simpler method for editing a user's roles</a>.]

I thought there might be some sort of API function that allows me to add a user role to a user object by the role id (rid), but after looking at user_save() and some other information around the Drupal universe (<a href="http://drupal.org/node/28379#comment-4277052">like this thread</a>), it looks like it's not as easy as I'd hoped. Definitely not like node_save(), where you just modify the node object, save it, and you're done!

I wrote this helper function that you could stick in your own custom module (tested with Drupal 7), which lets you add roles as simply as:

```
  custom_add_role_to_user($user->uid, 'role name here');
```

Here's the function:

```
/**
 * Add a role to a user.
 *
 * @param $user
 *   User object or user ID.
 * @param $role_name
 *   String value of role to be added.
 *
 * @see http_://drupal.org/node/28379#comment-4277052
 * @see http_://api.drupal.org/api/drupal/modules--user--user.module/function/user_save
 */
function custom_add_role_to_user($user, $role_name) {
  // For convenience, we'll allow user ids as well as full user objects.
  if (is_numeric($user)) {
    $user = user_load($user);
  }
  // If the user doesn't already have the role, add the role to that user.
  $key = array_search($role_name, $user->roles);
  if ($key == FALSE) {
    // Get the rid from the roles table.
    $roles = user_roles(TRUE);
    $rid = array_search($role_name, $roles);
    if ($rid != FALSE) {
      $new_role[$rid] = $role_name;
      $all_roles = $user->roles + $new_role; // Add new role to existing roles.
      user_save($user, array('roles' => $all_roles));
    }
  }
}
```

Hopefully, for Drupal 8, the user_save() function will be cleaned up (<a href="http://api.drupal.org/api/drupal/modules--user--user.module/function/user_save">see the @todo</a>), and this won't be such a chore.

[Edit: I've also written a handy function to remove user roles, which was made more robust in the way it removes roles using the $edit array of user_save() instead of modifying the user object's existing roles array, by g-hennux (see comments below). It's pasted below.]

```
/**
 * Remove a role from a user.
 *
 * @param $user
 *   User object or user ID.
 * @param $role_name
 *   String value of role to be removed.
 */
function custom_remove_role_from_user($user, $role_name) {
  // For convenience, we'll allow user ids as well as full user objects.
  if (is_numeric($user)) {
    $user = user_load($user);
  }
  // Only remove the role if the user already has it.
  $key = array_search($role_name, $user->roles);
  if ($key == TRUE) {
    // Get the rid from the roles table.
    $roles = user_roles(TRUE);
    $rid = array_search($role_name, $roles);
    if ($rid != FALSE) {
      // Make a copy of the roles array, without the deleted one.
      $new_roles = array();
      foreach($user->roles as $id => $name) {
        if ($id != $rid) {
          $new_roles[$id] = $name;
        }
      }
      user_save($user, array('roles' => $new_roles));
    }
  }
}
```
