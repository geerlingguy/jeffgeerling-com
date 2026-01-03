---
nid: 2343
title: "Drupal 6.x and PHP 5.3.x - Date Timezone warnings"
slug: "drupal-6x-and-php-53x-date"
date: 2011-11-08T17:48:10+00:00
drupal:
  nid: 2343
  path: /blogs/jeff-geerling/drupal-6x-and-php-53x-date
  body_format: full_html
  redirects: []
tags:
  - apache
  - date
  - drupal
  - drupal 6
  - errors
  - logging
  - munin
  - mysql
  - timezone
---

This morning, I was presented with quite the conundrum: one of my servers suddently started having about 4x the normal MySQL traffic it would have in a morning, and I had no indication as to why this was happening; traffic to the sites on the server was steady (no spikes), and I couldn't find any problems with any of the sites.

<p style="text-align: center;">{{< figure src="./munin-mysql_queries-timezone.png" alt="munin mysql traffic spike" >}}</p>

However, after inspecting the Apache (httpd) error logs for the Drupal 6 sites, I found a ton of PHP warnings on almost all the sites. Something like the following:

```
[Tue Nov 08 11:25:51 2011] [error] [client IP] PHP Warning:  date_default_timezone_get(): It is not safe to rely on the system's timezone settings. You are *required* to use the date.timezone setting or the date_default_timezone_set() function. In case you used any of those methods and you are still getting this warning, you most likely misspelled the timezone identifier. We selected 'America/Chicago' for 'CST/-6.0/no DST' instead in /path/to/drupal6/sites/opensourcecatholic.com/settings.php on line 149
```

As it turns out, the fix for date.timezone problems with PHP 5.3.x and Drupal 6.x mentioned in http://drupal.org/node/325827 (namely, adding <code>ini_set('date.timezone', date_default_timezone_get());</code> to the other ini_set() functions in settings.php) doesn't work that well for daylight savings time.

So, I've changed all those ini_set() functions in my Drupal 6 sites' settings.php files to explicitly set the default server timezone (in my case, <code>ini_set('date.timezone','America/Chicago');</code>), and now the error logs and watchdog errors written to the database are much more compact :)

I always leave watchdog database logging on for one or two of the sites on a server for precisely this reason: if something goes haywire, I can quickly notice something's awry in my server's munin stats. Then I hop over to the apache error logs and see exactly what's up.
