---
nid: 2410
title: "Wrapper function for simple drupal_mail() sending in Drupal 7"
slug: "wrapper-function-simple"
date: 2011-08-31T16:16:55+00:00
drupal:
  nid: 2410
  path: /blogs/jeff-geerling/wrapper-function-simple
  body_format: full_html
  redirects: []
tags:
  - development
  - drupal
  - drupal 7
  - drupal_mail
  - drupal_mail_send
  - email
  - ux
---

Email is such a pain (I should know, as I'm currently working on a site that's sending 10-20,000 emails per day to 40,000+ users. Spam prevention, SPF records, bounce handling, abuse reports, deliverability, send rates, etc. are all huge hassles that must be dealt with when handling more than a few hundred emails a day.

For testing, I often like throwing in a quick bit of code to send me or someone else a simple email with a few bits of information when something happens on the site, or to test email addresses or formatting. Therefore I like having a quick one-line function call to send an email. In Drupal 6, there was a handy <a href="http://api.drupal.org/api/drupal/includes--mail.inc/function/drupal_mail_send/6">drupal_mail_send()</a> function that would use some default settings and allow you to quickly shoot off a simple email (not translated, not pluggable, etc., but easy to implement).

Drupal 7 did away with that function, and instead, the <a href="http://api.drupal.org/api/drupal/includes--mail.inc/function/drupal_mail_system/7#comment-16454">simplest way to send an email in Drupal 7</a> requires some 20+ lines of code. Not fun when I'm trying to set up a few quick one-off emails that just need a 'from', 'to', 'subject', and 'message'. For these emails, I don't care about message translation, mail altering, etc. I just want an email shot off as quickly and simply as possible.

So, I wrote a quick wrapper function that I've placed in a custom.module that lets me just throw in the four default parameters, and sends an email. It doesn't hook into any of the system's mail handling capabilities, and isn't super-robust, but it lets me develop much faster:

```
<?php
/**
 * Simple wrapper function for drupal_mail() to avoid extraneous code.
 */
function custom_drupal_mail($from = 'default_from', $to, $subject, $message) {
  $my_module = 'custom';
  $my_mail_token = microtime();
  if ($from == 'default_from') {
    // Change this to your own default 'from' email address.
    $from = variable_get('system_mail', 'My Email Address <example@example.com>');
  }
  $message = array(
    'id' => $my_module . '_' . $my_mail_token,
    'to' => $to,
    'subject' => $subject,
    'body' => array($message),
    'headers' => array(
      'From' => $from, 
      'Sender' => $from, 
      'Return-Path' => $from,
    ),
  );
  $system = drupal_mail_system($my_module, $my_mail_token);
  $message = $system->format($message);
  if ($system->mail($message)) {
    return TRUE;
  }
  else {
    return FALSE;
  }
}
?>
```

Now, sending an email is as simple as:

```
<?php
  custom_drupal_mail('default_from', 'John Doe <jdoe@example.com>', 'Test Email Subject', 'Test Email Body.');
?>
```

[Edit: Updated with some suggestions from API comments and RichardLynch on IRC. Additionally, if you want to find a simple way to send <em>HTML emails</em> with Drupal and a custom module, see <a href="http://drupal.stackexchange.com/a/27103/26">this answer about HTML email sending in D7</a> on Stack Exchange].
