---
nid: 2694
title: "Change the displayed username in Drupal 8 ala Realname"
slug: "change-displayed-username-drupal-8-ala-realname"
date: 2016-09-22T01:04:48+00:00
drupal:
  nid: 2694
  path: /blog/2016/change-displayed-username-drupal-8-ala-realname
  body_format: markdown
  redirects: []
tags:
  - code
  - drupal
  - drupal 8
  - drupal planet
  - php
  - realname
  - site builder
  - users
---

Recovering from surgery finally gave me time to update my _last_ D6 site—a 7 year old private photo and media sharing site with nearly 10,000 nodes and 20+ GB of content—to Drupal 8. Drupal 8 has become a _lot_ more mature lately, to the point where I'm comfortable building a site and not having the foundation rot out from beneath as large ecosystem shifts have mostly settled down.

One thing that I thought would have the simplest implementation actually took a little while to figure out. I needed to have users' _full_ name display instead of their usernames throughout the site. For D6 (and for similar D7 use cases), the easiest way to do this was to enable the [Realname](https://www.drupal.org/project/realname) module, configure it a tiny bit, and be done with it.

In Drupal 8, however, Realname doesn't yet have a full release (see [this issue](https://www.drupal.org/node/2611306) for progress), and the way usernames are generated has changed slightly (see change record [`hook_username_alter()` changed to `hook_user_format_name_alter()`](https://www.drupal.org/node/1408514)).

So it took a few minutes' fiddling around before I came up with the following hook implementation that reformats the user's display name using a 'Name' field (machine name `field_name`) added to the user entity (you can add the field at `/admin/config/people/accounts/fields`), but only if there's a value for that user:

```
<?php
/**
 * Implements hook_user_format_name_alter().
 */
function custom_user_format_name_alter(&$name, $account) {
  // Load the full user account.
  $account = \Drupal\user\Entity\User::load($account->id());
  // Get the full name from field_name.
  $full_name = $account->get('field_name')->value;
  // If there's a value, set it as the new $name.
  if (!empty($full_name)) {
    $name = $full_name;
  }
}
?>
```

Note that there's ongoing discussion in the Drupal core issue queue about whether to [remove `hook_user_format_name_alter()`](https://www.drupal.org/node/2575213), since there are some caveats with its usage, and edge cases where it doesn't behave as expected or isn't used at all. I'm hoping this situation will be a little better soon—or at least that there will be a Realname release so people who don't like getting their hands dirty with code don't _have_ to :)
