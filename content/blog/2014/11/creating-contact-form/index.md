---
nid: 2473
title: "Creating a contact form programmatically in Drupal 8"
slug: "creating-contact-form"
date: 2014-11-14T18:24:23+00:00
drupal:
  nid: 2473
  path: /blogs/jeff-geerling/creating-contact-form
  body_format: full_html
  redirects: []
tags:
  - contact
  - drupal
  - drupal 8
  - drupal planet
  - entity api
aliases:
  - /blogs/jeff-geerling/creating-contact-form
---

Drupal 8's expanded and broadly-used Entity API extends even to Contact Forms, and recently I needed to create a contact form programmatically as part of <a href="https://www.drupal.org/project/honeypot">Honeypot's</a> test suite. Normally, you can export a contact form as part of your site configuration, then when it's imported in a different site/environment, it will be set up simply and easily.

However, if you need to create a contact form programmatically (in code, dynamically), it's a rather simple affair:

First, <code>use</code> Drupal's ContactForm class at the top of the file so you can use the class in your code later:

```
<?php
use Drupal\contact\Entity\ContactForm;
?>
```

Then, <code>create()</code> and <code>save()</code> a ContactForm entity using:

```
<?php
    $feedback_form = ContactForm::create([
      'id' => 'help',
      'label' => 'Help',
      'recipients' => ['somebody@example.com'],
      'reply' => '',
      'weight' => 0,
    ]);
    $feedback_form->save();
?>
```

If you also want to update the default contact form so you can set your new form as the default sitewide contact form category, you can do so by updating the global <code>contact.settings</code>.

```
<?php
$contact_settings = \Drupal::config('contact.settings');
$contact_settings->set('default_form', 'help')->save();
?>
```

One of the things I'm most excited about in Drupal 8 is how this entire process is the same (or almost exactly so) for every kind of entity—and almost everything's an entity! Need to create a content type? A configuration entity? A node? User? Almost everything follows this pattern now, and Drupal 8's APIs are so much more easy to learn as a side effect.
