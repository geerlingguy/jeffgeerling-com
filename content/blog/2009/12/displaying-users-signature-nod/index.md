---
nid: 2263
title: "Displaying a User's Signature on a Node Page in Drupal"
slug: "displaying-users-signature-nod"
date: 2009-12-21T23:49:40+00:00
drupal:
  nid: 2263
  path: /blogs/geerlingguy/displaying-users-signature-nod
  body_format: full_html
  redirects: []
tags:
  - drupal
  - node
  - profile
  - signature
---

<p>
	A project I&#39;m working on required a user&#39;s signature be displayed on the user&#39;s blog posts (only on the page&mdash;not in blog teaser listings), and after much wrangling, I figured out how to put the &#39;Biography&#39; (one of the user profile fields) into the nodes when they were viewed individually.</p>
<p>
	Here&#39;s the snippet (to be placed into node.tpl.php or node-blog.tpl.php):</p>

```
<code>
<?php if (!$teaser): ?>
```

```
<?php $account = user_load(array('uid' => $node->uid)); if (!empty($account->profile_bio)) { ?>
```

    <div class="blogger-bio"><code>
<?php print check_plain($account->profile_bio); ?>
</code></div>

```
<?php } ?>
```

```
<?php endif; ?>
```

</code>
<p>
	The code basically checks if the user&#39;s account has a bio filled out, and if so, it will place it at the end of the node if the node is viewed by itself (if it&#39;s not showing the teaser).</p>
<p>See comments below this post for some important security considerations and alternate options.</p>
