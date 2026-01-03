---
nid: 2395
title: "Setting a max_execution_time limit for PHP CLI"
slug: "setting-maxexecutiontime-limit"
date: 2013-02-14T22:38:19+00:00
drupal:
  nid: 2395
  path: /blogs/jeff-geerling/setting-maxexecutiontime-limit
  body_format: full_html
  redirects: []
tags:
  - config
  - drupal
  - drupal planet
  - drush
  - performance
  - php
---

PHP's command line interface doesn't respect the <code>max_execution_time</code> limit within your php.ini settings. This can be both a blessing and a curse (but more often the latter). There are some drush scripts that I run concurrently for batch operations that I want to make sure don't run away from me, because they perform database operations and network calls, and can sometimes slow down and block other operations.

<p style="text-align: center;">{{< figure src="./memory-graph-spike-threads.jpg" alt="Memory usage - PHP and MySQL locked from runaway threads" width="414" height="220" >}}
Can you tell when the batch got backlogged? CPU usage spiked to 20, and threads went from 100 to 400.</p>

I found that some large batch operations (where there are hundreds of thousands of items to work on) would hold the server hostage and cause a major slowdown, and when I went to the command line and ran:

```
$ drush @site-alias ev "print ini_get('max_execution_time');"
```

I found that the execution time was set to 0. Looking in PHP's <a href="http://www.php.net/manual/en/info.configuration.php#ini.max-execution-time">Docs for max_execution_time</a>, I found that this is by design:

<blockquote>
This sets the maximum time in seconds a script is allowed to run before it is terminated by the parser. This helps prevent poorly written scripts from tying up the server. The default setting is 30. <strong>When running PHP from the command line the default setting is 0.</strong>
</blockquote>

I couldn't set a max_execution_time for the CLI in php.ini, unfortunately, so I simply added the following to my site's settings.php:

```
<?php
ini_set('max_execution_time', 180); // Set max execution time explicitly.
?>
```

This sets the execution time explicitly whenever drush bootstraps drupal. And now, in my drush-powered function, I can check for the max_execution_time and use that as a baseline to measure against whether I should continue processing the batch or stop. I need to do this since I have drush run a bunch of concurrent threads for this particular batch process (and it continues all day every day).

Now the server is much happier, since I don't get hundreds of threads that end up locking the MySQL server during huge operations. I can set drush to only run every 3 minutes, and it will only create a few threads that die around the next time another drush operation is called.
