---
nid: 2416
title: "Migrating Drupal 7 users from site to site while preserving password hashes"
slug: "migrating-drupal-7-users-site"
date: 2013-07-14T03:26:00+00:00
drupal:
  nid: 2416
  path: /blogs/jeff-geerling/migrating-drupal-7-users-site
  body_format: full_html
  redirects: []
tags:
  - drupal 7
  - drupal planet
  - migrate
  - password
---

From time to time, I use the incredibly powerful <a href="https://drupal.org/project/migrate">Migrate</a> module to migrate a subset of users from one Drupal 7 site to another.

Setting up the user migration class is pretty straightforward, and there are some great examples out there for the overall process. However, I couldn't find any particular documentation for how to preserve user passwords when migrating users from D7 to D7. It's simple enough to set the 'md5_passwords' boolean for Drupal 6 to Drupal 7 user migrations, so passwords will be updated when a user logs in the first time on the D7 site... but it's not as straightforward if you want to simply move the salted/hashed passwords from D7 to D7.

During the migration, when the user account is saved, Drupal will re-salt and re-hash the already-hashed-and-salted password you pass in through your field mappings, and users will have to reset their passwords to log in again.

To override this behavior, you need to implement the <code>complete()</code> function in your user migration, and manually overwrite the just-saved user account password field:

```
<?php
  public function complete($entity, $row) {
    // Reset password hash back to the source hash; when Migrate saves the user
    // entity after the prepare() method is complete, Drupal hashes the hash,
    // meaning we need to set it back to the original hash.
    // SEE: https://drupal.org/node/1349758
    db_update('users')
      ->fields(array('pass' => $row->pass))
      ->condition('uid', $entity->uid)
      ->execute();
  }
?>
```

Granted, there are far fewer Drupal 7 -> Drupal 7 user migrations happening than migrations from Drupal 5 or 6 to 7, or other systems into Drupal 7... but I wanted to post this so someday, when I'm scratching my head over this same issue again (why are my hashes changing???), I can find the answer in a few seconds via Google :)
