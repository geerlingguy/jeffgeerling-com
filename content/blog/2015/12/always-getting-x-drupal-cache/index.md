---
nid: 2518
title: "Always getting X-Drupal-Cache: MISS? Check for messages"
slug: "always-getting-x-drupal-cache"
date: 2015-12-30T15:39:27+00:00
drupal:
  nid: 2518
  path: /blogs/jeff-geerling/always-getting-x-drupal-cache
  body_format: full_html
  redirects: []
tags:
  - cache
  - drupal
  - drupal 7
  - drupal 8
  - drupal planet
  - varnish
aliases:
  - /blogs/jeff-geerling/always-getting-x-drupal-cache
---

I spent about an hour yesterday debugging a Varnish page caching issue. I combed the site configuration and code for anything that might be setting <code>cache</code> to <code>0</code> (effectively disabling caching), I checked and re-checked the <code>/admin/config/development/performance</code> settings, verifying the 'Expiration of cached pages' (<code>page_cache_maximum_age</code>) had a non-zero value and that the 'Cache pages for anonymous users' checkbox was checked.

After scratching my head a while, I realized that the headers I was seeing when using <code>curl --head [url]</code> were specified as the defaults in <a href="https://api.drupal.org/api/drupal/includes%21bootstrap.inc/function/drupal_page_header/7">drupal_page_header()</a>, and were triggered any time there was a message displayed on the page (e.g. via <code>drupal_set_message()</code>):

```
X-Drupal-Cache: MISS
Expires: Sun, 19 Nov 1978 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, post-check=0, pre-check=0
X-Content-Type-Options: nosniff
```

On this particular site, the <code>error_level</code> was set to <code>1</code> to show all errors on the screen, and the page in question had a PHP error displayed on every page load.

After setting <code>error_level</code> to <code>0</code> ('None' on the <code>/admin/config/development/logging</code> page), Drupal sent the correct cache headers, Varnish was able to cache the page, and my sanity was restored.

Kudos especially to <a href="https://coderwall.com/p/cdg9ha/drupal-page-not-caching-in-varnish">this post</a> on coderwall, which jogged my memory.

Other potential reasons a page might not be showing as cacheable:

<ul>
<li>A form with a unique per-user token may be present.</li>
<li>An authenticated user is viewing the page (Drupal by default marks any page view with a valid session as no-cache).</li>
<li>Someone set <code>\Drupal::service('page_cache_kill_switch')->trigger();</code> (Drupal 8), or <code>drupal_page_is_cacheable()</code> (Drupal 7).</li>
<li>Some configuration file that's being included is either setting <code>cache</code> or <code>page_cache_maximum_age</code> to <code>0</code>.</li>
</ul>
