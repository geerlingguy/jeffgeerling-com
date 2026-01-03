---
nid: 2336
title: "Prefill the Subject of a Privatemsg Message"
slug: "prefill-subject-privatemsg"
date: 2011-10-19T00:51:11+00:00
drupal:
  nid: 2336
  path: /blogs/jeff-geerling/prefill-subject-privatemsg
  body_format: full_html
  redirects: []
tags:
  - code
  - drupal
  - drupal 7
  - drupal planet
  - modules
  - php
  - privatemsg
  - snippets
aliases:
  - /blogs/jeff-geerling/prefill-subject-privatemsg
---

I've had a nice go at making private messaging capabilities for <a href="http://www.flocknote.com/">flockNote</a> work a lot nicer than the out-of-the-box <a href="http://drupal.org/project/privatemsg">Privatemsg</a> module experience, by simplifying everything to the point that it's closer to the Facebook Direct Message system than the normal Privatemsg UX. (Privatemsg is the premiere way of handling private messaging in Drupal. It's already awesome out of the box... just needed a bit more help for our particular site ;-).

One thing I had wanted to do for a while is prefill the subject field of certain messages. I already have the new private message page appear inside an overlay popup after a user clicks on a link to send a private message to another user on the site.

<p style="text-align: center;">{{< figure src="./privatemsg-example-prefill-subject.png" alt="Privatemsg prefill subject" width="410" height="272" >}}</p>

I wanted users sending direct messages regarding certain comments or nodes to have a subject line of 'RE: [node title]' or 'RE: [comment title]' in them so they didn't have to write out a subject on their own. I was prepared to implement a hook_form_alter for the privatemsg form, send a query fragment containing the private message subject in the URL to the new private message page, and then check for it in my form alter to fill it in as the subject... but it turns out the Privatemsg module already has this capability built in!

All you need to do is throw in the subject as an extra argument in the url like so: <code>messages/new/[uid]/[subject]</code>. (You can still throw on query fragments to the end if you need to. In my case, I put a destination on the end so the overlay closes after a message is sent).

Or, in code...

```
<?php
  $account = user_load($node->uid);
  $pm_link_text = t('Send a PM to Author');
  $pm_url = privatemsg_get_link($account) . '/' . t('RE: @title', array('@title' => $node->title));
  $pm_link = l($pm_link_text, $pm_url, array('query' => array(drupal_get_destination())));
?>
```

