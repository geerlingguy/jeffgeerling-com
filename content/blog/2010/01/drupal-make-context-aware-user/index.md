---
nid: 2265
title: "Drupal: Make a Context-Aware User Login Link (PHP Snippet)"
slug: "drupal-make-context-aware-user"
date: 2010-01-20T20:51:38+00:00
drupal:
  nid: 2265
  path: /blogs/geerlingguy/drupal-make-context-aware-user
  body_format: full_html
  redirects: []
tags: []
aliases:
  - /blogs/geerlingguy/drupal-make-context-aware-user
---

<p>
	Many of the sites I design don&#39;t require a user login form on every page, especially if there are only a few people that will ever need to login. Instead, I like to simply provide a &quot;User Login&quot; link somewhere on the page (most often in the footer), so it&#39;s unobtrusive but there for those who might not remember to type in /user after the URL.</p>
<p>
	This presents a new problem, though: if you put a link to &quot;example.com/user,&quot; then the person who clicks the link will be taken away from the page he was viewing to login, then he&#39;ll be directed to his user account page.</p>
<p>
	Luckily, Drupal lets you set a login destination in the URL, so you can redirect the user back to the page he was viewing after he logged in.</p>
<p>
	To do so, create a block with PHP as the input format (or insert this snippet somewhere in your .tpl.php template files), and use the code below:</p>


```
<a href="/user?destination=<code>
<?php echo $_GET['q']; ?>
</code>">User Login</a>
```

<p>
	Now you have a handy little link that will redirect a user back to the page he was viewing before he logged in.</p>
