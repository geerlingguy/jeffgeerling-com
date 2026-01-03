---
nid: 2906
title: "Rendering Twig templates programmatically in Drupal 8"
slug: "rendering-twig-templates-programmatically-drupal-8"
date: 2019-01-28T20:59:36+00:00
drupal:
  nid: 2906
  path: /blog/2019/rendering-twig-templates-programmatically-drupal-8
  body_format: markdown
  redirects: []
tags:
  - contributions
  - drupal
  - drupal 8
  - drupal planet
  - templates
  - twig
---

From time to time, I have the need to take a Twig template and a set of variables, render the template, replacing all the variables within, and then get the output as a string. For example, if I want to have a really simple email template in a custom module which has a variable for `first_name`, so I can customize the email before sending it via Drupal or PHP, I could do the following in Drupal 7:

```
<?php
$body = theme_render_template(drupal_get_path('module', 'my_module') . '/templates/email-body.tpl.php', array(
  'first_name' => 'Jane',
));
send_email($from, $to, $subject, $body);
?>
```

In Drupal 8, there is no `theme_render_template()` function, since the template engine was switched to Twig in [this issue](https://www.drupal.org/node/1696786). And until today, there was no change record indicating the fact that the handy `theme_render_template()` had been replaced by a new, equally-handy `twig_render_template()` function! Thanks to some help from Tim Plunkett, I was able to find this new function, and after he pushed me to do it, I created a new change record to help future-me next time I go looking for `theme_render_template()` in Drupal 8: [theme_render_template changed to twig_render_template](https://www.drupal.org/node/3029053).

In Drupal 8, it's extremely similar to Drupal 7, although there are two additions I made to make it functionally equivalent:

```
<?php
$markup = twig_render_template(drupal_get_path('module', 'my_module') . '/templates/email-body.html.twig', array(
  'my-variable' => 'value',
  // Needed to prevent notices when Twig debugging is enabled.
  'theme_hook_original' => 'not-applicable',
));
// Cast to string since twig_render_template returns a Markup object.
$body = (string) $markup;
send_email($from, $to, $subject, $body);
?>
```

If you are rendering a template outside of a normal page request (e.g. in a cron job, queue worker, Drush command, etc.) the Twig theme engine might not be loaded. If that's the case, you'll need to manually load the Twig engine using:

```
<?php
// Load the Twig theme engine so we can use twig_render_template().
include_once \Drupal::root() . '/core/themes/engines/twig/twig.engine';
?>
```

I shall go forth templating ALL THE THINGS now!
