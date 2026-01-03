---
nid: 2424
title: "Ensuring Drupal email doesn't get sent from a local development environment"
slug: "ensuring-drupal-email-doesnt"
date: 2013-08-30T12:53:26+00:00
drupal:
  nid: 2424
  path: /blogs/jeff-geerling/ensuring-drupal-email-doesnt
  body_format: full_html
  redirects: []
tags:
  - devel
  - development
  - drupal
  - drupal planet
  - email
---

It seems most developers I know have a story of running some sort of batch operation on a local Drupal site that triggers hundreds (or thousands!) of emails that are sent to the site's users, causing much frustration and ill will towards the site the developer is working on. One time, I accidentally re-sent over 9,000 private message emails during a test user migration because of an email being sent via a hook that was invoked during each message save. Filling a user's inbox is not a great way to make that user happy!

With Drupal, it's relatively easy to make sure emails are either rerouted or directed to temp files from local development environments (and any other environment where actual emails shouldn't be sent to end users). Drupal.org has a very thorough page, <a href="https://drupal.org/node/201981">Managing Mail Handling for Development or Testing</a>, which outlines many different ways you can handle email in non-production environments.

However, for most cases, I like to simply redirect all site emails to my own address, or route them to a figurative black hole.

<h3>Rerouting Emails to an Arbitrary Email Address</h3>

There's a simple module, <a href="https://drupal.org/project/reroute_email">Reroute Email</a>, which allows you to have all emails sent through Drupal to be rerouted to a configured email address. This module is simple enough, but for even more simplicity, if you have a custom module, you can just invoke hook_mail_alter() to force all messages to a given email address. Example (assuming your module's name is 'custom' and you want to send emails to the configured 'site_mail' address):

```
<?php
/**
 * Implements hook_mail_alter().
 */
function custom_mail_alter(&$message) {
  // Re-route emails to admin when override_email variable is set.
  if (variable_get('override_email', 0)) {
    $message['to'] = variable_get('site_mail');
  }
}
?>
```

Now you can just add <code>$conf['override_email'] = 1;</code> to settings.php for any environment where you want all emails to be sent to the 'site_mail' configured email address. Pretty simple!

<h3>Directing emails to text files in /tmp</h3>

Another simple option, if you still don't want emails to be sent to the end user, but still want to see them in some form (in this case, a text file), is to enable the <a href="https://drupal.org/project/devel">Devel</a> module, then set your site's mail system to 'DevelMailLog' (like the following inside settings.php):

```
<?php
$conf['mail_system'] = array('default-system' => 'DevelMailLog');
?>
```

Devel will now re-route all emails to .txt files inside your server's /tmp folder.
