---
nid: 2286
title: "Allowing anonymous IP-based access to content with Boost, subscription model"
slug: "allowing-anonymous-ip-based-ac"
date: 2010-09-22T21:05:27+00:00
drupal:
  nid: 2286
  path: /blogs/jeff-geerling/allowing-anonymous-ip-based-ac
  body_format: full_html
  redirects: []
tags:
  - access control
  - boost
  - drupal
  - drupal planet
  - tcp/ip
aliases:
  - /blogs/jeff-geerling/allowing-anonymous-ip-based-ac
   - /blogs/jeff-geerling/allowing-anonymous-ip-based-ac
---

<p>On the <a href="http://stlouisreview.com">St. Louis Review</a> website (<a href="http://www.jeffgeerling.com/blogs/geerlingguy/case-study-saint-louis-review-st-louis-based-newspaper">case study here</a>), which offers much of its content based on a subscription model (you must be a subscriber to access the &#39;premium&#39; content), we wanted to allow those inside our network access to nodes that were marked &#39;subscribers-only&#39;, without having to log in to the website and maintain a user account. Here&#39;s how we did it:</p>
<h2>1 - Modification of Custom Subscriber Access Code</h2>
<p>Our site uses hook_nodeapi() to limit access to &#39;premium&#39; or &#39;subscribers-only&#39; content. We simply added in a check to see if users were coming from a certain IP address (the IP address for our corporate network):</p>

```
<?php
/**
* Implementation of hook_nodeapi().
*/
function slr_subscription_nodeapi(&$node, $op, $a3 = NULL, $a4 = NULL) {

  // Get the user's IP address - we'll later check if it's in an array of
  // allowed Archdiocesan IP addresses. If so, the user should be able to
  // see subscribers-only content. We will need to set up an array of IP
  // addresses in the 12.34.56.78/27 block, then use !in_array() for
  // the check.
  $user_ip = $_SERVER['REMOTE_ADDR'];

  // Viewing an "subscribers only" article, full-page, by a user without
  // "subscribers only" permission
  if ($node->type == 'article' and $op == 'view' and $node->field_subscription_status[0]['value'] == SLR_SUBSCRIPTION_SUBSCRIBERS_ONLY and $a4 and !user_access("view subscribers only content") and !($user_ip == '12.34.56.78')) {
    // Only show teaser and subscription invitation
    $node->content['body']['#value'] = $node->teaser . theme('slr_subscription_message');
  }
}
?>
```

<h2>2 - Modification of .htaccess to prevent Apache from serving Boost-cached page</h2>
<p>We had to add the following line in our ###BOOST### code in .htaccess, inside the &#39;Caching for anonymous users&#39; section. This code tells Apache to skip the boost cache if the user is coming from a certain IP address... without it, Drupal would never even be bootstrapped if a cached copy of the requested page existed!</p>

```
# Archdiocesan Curia main IP address
RewriteCond %{REMOTE_ADDR} ^12\.34\.56\.78 [OR]
```

<h2>3 - Tell Boost to not cache pages if anonymous visitor is from our corporate network</h2>
<p>Finally, in order to prevent Boost from caching the full page (and thus, allowing any anonymous visitors access to the premium content) when an anonymous visitor arrives from our network, we implement&nbsp;hook_boost_is_cacheable():</p>

```
<?php
/**
* Implementation of hook_boost_is_cacheable().
*/
function slr_subscription_boost_is_cacheable($path) {
  $normal_path = drupal_get_normal_path($path); // normalize path

  // Do not cache if user coming from Archdiocesan network
  if ($_SERVER['REMOTE_ADDR'] == '12.34.56.78') {
    return FALSE;
  }

  else {
    $page_match = TRUE;
  }

  return $page_match;
}
?>
```

<p>One of the things I&#39;m trying to figure out is the best way to match any IP in a block of IP addresses. I could maybe set up an array of addresses in PHP and do a match to that, but I think that might have some performance implications. For the .htaccess portion, I could just do a regex, which wouldn&#39;t be too bad, though.</p>
