---
nid: 2320
title: "Moving Scheduler Module's 'Scheduling Options' Out of the Vertical Tabs in D7"
slug: "moving-scheduler-modules"
date: 2011-05-23T20:07:00+00:00
drupal:
  nid: 2320
  path: /blogs/jeff-geerling/moving-scheduler-modules
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - forms api
  - hook_form_alter
  - scheduler
  - vertical tabs
aliases:
  - /blogs/jeff-geerling/moving-scheduler-modules
---

<em>...or, "Always Check Your Module Weights when form_alter'ing"</em>

{{< figure src="./scheduling-options.jpg" alt="Scheduling options from Scheduler module" width="521" height="191" >}}

I spent about half an hour today trying to use <code>hook_form_alter()</code> to move the 'Scheduling options' fieldset (provided by the Scheduler module) out of my node form's vertical tabs (down where URL path settings, comment settings, etc. are jumbled together).

I couldn't even see the 'scheduler_settings' form settings when I looked at the form's array, even though I knew it existed (since it was being displayed, and the scheduler.module defined it using its own hook_form_alter().

After scratching my head and almost throwing in the towel, I finally noticed <a href="http://drupal.org/node/1131786">this thread</a>, in which Dave Reid mentioned the priority and heirarchy of form_alter calls (<code>hook_form_alter()</code>, <code>hook_form_BASE_FORM_ID_alter()</code>, then finally <code>hook_form_FORM_ID_alter()</code>). <a href="http://drupal.org/node/1131786#comment-4457358">Later</a> in the thread, Dave also mentioned the fact that the module weights (in the system table) also affect the order in which forms are altered...

Since my custom.module was weighted the same as scheduler.module (both were '0'), scheduler.module ran later, so I couldn't see the field it added. I simply popped over to Sequel Pro, updated my custom.module's weight in the system table to 9 (don't ask), and voila! I could form_alter the 'Scheduling options' fieldset to my heart's content. To get it to appear above the vertical tabs in a node form, do something like the following in your custom.module:

```
<?php
/**
 * Implements hook_form_FORM_ID_alter().
 */
function custom_form_note_node_form_alter(&$form, $form_state, $form_id) {
  unset($form['scheduler_settings']['#group']);
}
?>
```

