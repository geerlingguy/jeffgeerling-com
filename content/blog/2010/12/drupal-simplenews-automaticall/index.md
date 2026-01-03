---
nid: 2291
title: "Drupal Simplenews: Automatically Subscribe New Users to a Newsletter"
slug: "drupal-simplenews-automaticall"
date: 2010-12-03T02:34:40+00:00
drupal:
  nid: 2291
  path: /blogs/jeff-geerling/drupal-simplenews-automaticall
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - email
  - simplenews
aliases:
  - /blogs/jeff-geerling/drupal-simplenews-automaticall
---

<p>One of the sites I am setting up requires that all users be subscribed to a certain newsletter (or maybe two, depending on who they are) via <a href="http://drupal.org/project/simplenews">Simplenews</a> when they create their accounts (actually, their accounts are automatically created via LDAP... but that&#39;s another story).</p>
<p>Looking around, I found <a href="http://drupal.org/node/119592#comment-238913">this post explaining how you might be able to auto-subscribe new users</a>, and it led me to look up Simplenews&#39;&nbsp;simplenews_subscribe_user() function.</p>
<p>Basically, you can add a line like the following in your custom module&#39;s hook_user() function, on the &#39;insert&#39; $op (for Drupal 6):</p>

```
<?php
  // simplenews_subscribe_user(<email>, <tid_of_newsletter>, <send_confirmation_email_boolean>, <source_of_subscription>, <language>)
  simplenews_subscribe_user($account->mail, 45, $confirm = FALSE, $source = 'action', NULL);
?>
</code><p>Additionally, you can subscribe ALL of your site&#39;s users (or whatever subset you choose, via your own logic) to a Simplenews newsletter using the following PHP snippet (you can just paste this in <a href="http://drupal.org/project/devel">Devel</a>&#39;s &#39;Execute PHP Code&#39; block):</p>
<code>
<?php
$uids_to_update = array(0, 1, 2);

foreach ($uids_to_update as $uid) {
  $account = user_load($uid);
  simplenews_subscribe_user($account->mail, 45, $confirm = FALSE, $source = 'action', NULL);
}
?>
```

<p>I grabbed a list of all the active uids on the site using views, turned them into an array (used quick regex in TextMate to turn a line-broken list into value, value, value...), then used the code above (with my own array in it) to subscribe all active users to the newsletter.</p>
