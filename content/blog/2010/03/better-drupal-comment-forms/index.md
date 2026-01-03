---
nid: 2267
title: "Better Drupal Comment Forms"
slug: "better-drupal-comment-forms"
date: 2010-03-06T15:40:51+00:00
drupal:
  nid: 2267
  path: /blogs/geerlingguy/better-drupal-comment-forms
  body_format: full_html
  redirects: []
tags:
  - comments
  - css
  - drupal
  - drupal planet
  - style
  - user experience
---

<p class="rtecenter">
	{{< figure src="./comment-form-new.png" alt="New Comment form - Drupal - More user-friendly" width="600" height="251" class="noborder" >}}</p>
<p>
	Put this in one of your theme&#39;s stylesheets - it&#39;ll change a clunky, large, and unweildy comment form into a more compact and user-friendly form:</p>
<!--break--><pre>/* Comment Form */
#comment-form {
	padding: 1em;
	margin: 1em;
	background: #FFF;
	position: relative;
}

#edit-name-wrapper {
	margin-top: 0;
}

#edit-homepage-wrapper {
	width: 8em;
	top: 0em;
	left: 25em;
	position: absolute;
}

#edit-homepage-wrapper,
#edit-homepage {
	color: #777;
}

#comment-form .form-actions {
	margin-bottom: 0;
}

#comment-form input.form-text,
#comment-form textarea,
#comment-form input {
	margin: 0;
}</pre>
