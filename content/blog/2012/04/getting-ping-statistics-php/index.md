---
nid: 2384
title: "Getting Ping statistics with PHP"
slug: "getting-ping-statistics-php"
date: 2012-04-03T22:23:48+00:00
drupal:
  nid: 2384
  path: /blogs/jeff-geerling/getting-ping-statistics-php
  body_format: full_html
  redirects: []
tags:
  - code
  - exec
  - php
  - ping
  - snippets
aliases:
  - /blogs/jeff-geerling/getting-ping-statistics-php
---

[<strong>Note:</strong> Since writing this post, I've created the <a href="https://github.com/geerlingguy/Ping">Ping class for PHP</a>, which incorporates three different ping/latency/uptime methods for PHP, and is a lot more robust than the script I have posted below.]

I recently needed to display some ping/server statistics on a website using PHP. The simplest way to do something like this is to use the built-in linux utility <code>ping</code>, and then parse the results. Instead of doing complex regex with the entirety of ping's output, though, I also used a couple other built-in linux utilities to get just what I needed.

Here's how I got just the response time of a given IP address:

```
<?php
$ip_address = '123.456.789.0'; // IP address you'd like to ping.
exec("ping -c 1 " . $ip_address . " | head -n 2 | tail -n 1 | awk '{print $7}'", $ping_time);
print $ping_time[0]; // First item in array, since exec returns an array.
?>
```

The above script will ping the given IP address, and simply pull out the response time in milliseconds. You can further parse the response time to just be the numeric value by running it through <code>substr($ping_time[0], 5)</code>.

Note that some systems <code>ping</code> will output things a little differently, so you may need to adjust which line you grab (<code>head</code> first grabs just the first two lines of <code>ping</code>'s output, <code>tail</code> cuts it down to the last line of that, then <code>awk</code> prints out the 7th item in the string, which is the <code>time=</code> value).

Changing the awk statement to print different parts of the result will allow you to get different information, should the need arise.

<h3>Important Notes</h3>

<ul>
<li>Note that ping times (especially) vary a bit, so this script is just helpful for general needs; if you were building a solid monitoring system, you should probably ping every second or two, then average the results, and store that value, rather than pinging just once every now and then...</li>
<li>I typically avoid using <code>exec()</code> when possible, especially if writing something more general, because not every PHP installation will have access to any or all of the command line utilities used, and <code>exec()</code> usage isn't often advisable if there's another way to accomplish something, but in this case, the code is going to only be used on a site running on a custom LAMP box that shouldn't ever have trouble with ping, tail, head, and awk.</li>
</ul>
