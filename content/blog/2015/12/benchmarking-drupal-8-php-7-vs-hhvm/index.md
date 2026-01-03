---
nid: 2517
title: "Benchmarking PHP 7 vs HHVM - Drupal and Wordpress"
slug: "benchmarking-drupal-8-php-7-vs-hhvm"
date: 2015-12-23T23:21:28+00:00
drupal:
  nid: 2517
  path: /blogs/jeff-geerling/benchmarking-drupal-8-php-7-vs-hhvm
  body_format: full_html
  redirects: []
tags:
  - benchmarking
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - hhvm
  - php
aliases:
  - /blogs/jeff-geerling/benchmarking-drupal-8-php-7-vs-hhvm
---

[<strong>Multiple updates</strong>: I've added results for concurrencies of 1 and 10, results on bare metal vs. VMware instances, tested Drupal 8 vs Drupal 7 vs Wordpress 4.4, and I've also retested every single benchmark at least twice! Please make sure you're read through the <em>entire</em> post prior to contesting these benchmark results!]

<blockquote><strong>tl;dr</strong>: Always test your <em>own</em> application, and trust, but verify every benchmark you see. PHP 7 is actually faster than HHVM in many cases, neck-in-neck in others, and slightly slower in others. Both PHP 7 and HHVM blow PHP &le; 5.6 out of the water.</blockquote>

Skip to benchmark results:

<ul>
<li><a href="#d8c10">Drupal 8 Results (concurrency 10)</a></li>
<li><a href="#d8c1">Drupal 8 Results (concurrency 1)</a></li>
<li><a href="#d8bmc1">Drupal 8 Results ('bare metal', concurrency 1)</a></li>
<li><a href="#wpbmc1">Wordpress 4.4 Results ('bare metal', concurrency 1)</a></li>
<li><a href="#d7c10">Drupal 7 Results (concurrency 10)</a></li>
</ul>

<h2>Introduction and Methodology</h2>

As PHP 7 became a reality through this past year, there were scores of benchmarks pitting PHP 7 against 5.6 and HHVM using applications and frameworks like Drupal, Wordpress, Joomla, Laravel, October, etc.

One benchmark that really stood out to me (in that it seemed so wrong for Drupal, based on my experience) was <a href="https://kinsta.com/blog/the-definitive-php-7-final-version-hhvm-benchmark/">The Definitive PHP 7.0 & HHVM Benchmark</a> from Kinsta. Naming a benchmark that way certainly makes the general PHP populace take it seriously!

The results are pretty damning for PHP 7:

<p style="text-align: center;">{{< figure src="./php7-hhvm-benchmark-definitive-screenshot.png" alt="PHP 7 HHVM Definitive Benchmark screenshot by Kinsta" width="325" height="274" >}}</p>

In the comments on that post, Thomas Svenson mentioned:

<blockquote>
Standard installation for Drupal 8 has cache on as default. If you did not turn that off, then it is probably a reason to why the PHP 7 boost isn't bigger.

Would be interesting to see the result comparing the benchmark with/without caching enabled in Drupal 8. Should potentially reveal something interesting.
</blockquote>

This was my main concern too, as there wasn't enough detail in the benchmarking article to determine what <em>exactly</em> was the system under test. Therefore, I'll submit my own PHP 7 vs HHVM benchmark here, using the following versions:

<ul>
<li>Ubuntu 14.04</li>
<li>Drupal 8.0.1</li>
<li>Nginx 1.4.6</li>
<li>MySQL 5.5.46</li>
<li>PHP 5.6.16, PHP 7.0.1, or HHVM 3.11.0</li>
</ul>

All tests were run using <a href="http://www.drupalvm.com/">Drupal VM</a> version 2.1.2 with VMware Fusion 8.1.0, on my mid-2013 MacBook Air 13" 1.7 GHz i7 with 8GB of RAM. Using the above notes, you can <em>exactly</em> replicate this benchmarking environment should you desire. All tests were run five times, the first two results were discarded (because they often reflect times when some caches are still warming), and the latter three were averaged.

After installing Drupal 8.0.1 with the standard installation profile (this is done automatically by Drupal VM), I logged in as the admin user (user 1), then grabbed the admin user's session cookie, and ran the following two commands:

```
# Benchmark Drupal 8 home page out of the box with default caching options enabled.
ab -n 750 -c 10 http://drupalvm.dev/

# Benchmark Drupal 8 /admin page logged in as user 1.
ab -n 750 -c 10 -C "SESSxyz=value" http://drupalvm.dev/admin
```

<h2 id="d8c10">Drupal 8 results (concurrency 10)</h2>

<table>
<thead>
<tr>
  <th>Environment</th>
  <th>D8 Caching</th>
  <th>Requests/second</th>
  <th>Percent difference</th>
</tr>
</thead>
<tr>
  <td>PHP 5.6.16</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>214.39 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>407.10 req/s</strong></td>
  <td>62% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>260.19 req/s</strong></td>
  <td>19% faster than 5.6</td>
</tr>
<tr>
  <td>PHP 5.6.16</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>20.09 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>39.26 req/s</strong></td>
  <td>65% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>34.41 req/s</strong></td>
  <td>53% faster than 5.6</td>
</tr>
</table>

...and some graphs of the above data:

<h3>PHP 5.6, PHP 7, and HHVM running Drupal 8.0.1, cached</h3>

<p style="text-align: center;">{{< figure src="./php-7-5-hhvm-cached-requests-benchmark.png" alt="PHP 5, PHP 7, HHVM benchmark cached Drupal 8 home page request" width="416" height="276" >}}</p>

<h3>PHP 5.6, PHP 7, and HHVM running Drupal 8.0.1, uncached</h3>

<p style="text-align: center;">{{< figure src="./php-7-5-hhvm-uncached-requests-benchmark.png" alt="PHP 5, PHP 7, HHVM benchmark uncached Drupal 8 admin request" width="416" height="276" >}}</p>

<h2 id="d8c1">Drupal 8 results (concurrency 1)</h2>

Sometimes, the use of concurrency (<code>-c 10</code> in the above case)(to simulate concurrent users hitting the site at the same time, can cause benchmarks to be slightly inaccurate. The reason I usually use a level of concurrency is so the benchmark more closely mirrors real-world usage, and tests the full stack a little better (because PHP by itself is nice to benchmark, but very few sites are run on top of PHP alone!).

Anyways, I re-ran all the tests using <code>-c 1</code>, and am publishing the results below:

<table>
<thead>
<tr>
  <th>Environment</th>
  <th>D8 Caching</th>
  <th>Requests/second</th>
  <th>Percent difference</th>
</tr>
</thead>
<tr>
  <td>PHP 5.6.16</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>171.34 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>242.00 req/s</strong></td>
  <td>34% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>192.92 req/s</strong></td>
  <td>12% faster than 5.6</td>
</tr>
<tr>
  <td>PHP 5.6.16</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>19.89 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>30.07 req/s</strong></td>
  <td>41% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>23.37 req/s</strong></td>
  <td>16% faster than 5.6</td>
</tr>
</table>

In all my benchmarking, I care more about <em>deltas</em> and <em>reproducibility</em> than measuring raw, clean-room-scenario performance, because unless a result is absolutely reproducible, it's of no value to me. Therefore if I can prove that there's no particular difference to testing with certain concurrency levels, I typically move the benchmark to a level that mirrors traffic patterns I actually see on my sites :)

Absolute numbers mean nothing to me—it's the comparison between test A and test B, and how reproducible that comparison is, that matters. That's why I enjoy benchmarking on the incredibly slow Raspberry Pi model 2 sometimes, because though it's much slower than my i7 laptop, it sometimes exposes surprising results!

<h2 id="d8bmc1">Drupal 8 Results ('bare metal', concurrency 1)</h2>

Some people argue that running benchmarks in a VM is highly unreliable and leads to incorrect benchmarks, so I've also sacrificed a partition of a Lenovo T420 core i5 laptop (it has 3 SSDs inside, so I just formatted one, installed Ubuntu desktop 15.10, then installed PHP, MySQL, and Nginx exactly the same as with Drupal VM (same settings, same apt repos, etc.), and re-ran all the tests in that environment—so-called 'bare metal', where there's absolutely no overhead from shared filesystems, the hypervisor, etc.

<table>
<thead>
<tr>
  <th>Environment</th>
  <th>D8 Caching</th>
  <th>Requests/second</th>
  <th>Percent difference</th>
</tr>
</thead>
<tr>
  <td>PHP 5.6.16</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>152.35 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>230.67 req/s</strong></td>
  <td>41% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>142.50 req/s</strong></td>
  <td>7% slower than 5.6</td>
</tr>
<tr>
  <td>PHP 5.6.16</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>11.37 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>13.13 req/s</strong></td>
  <td>14% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>11.40 req/s</strong></td>
  <td>0.3% faster than 5.6</td>
</tr>
</table>

After running these benchmarks with an identical environment on 'bare metal' (e.g. a laptop with a brand new/fresh install of Ubuntu 15.10 running the same software, with 8 GB of RAM and an SSD), it seems HHVM for some reason performed <em>even worse than PHP 5.6.16</em> for Drupal 8.

Since this result is wildly different than the Kinsta post (basically the opposite of their results for Drupal 8), I decided to test Wordpress 4.4 as well.

<h2 id="wpbmc1">Wordpress 4.4 Results ('bare metal', concurrency 1)</h2>

For Wordpress, I ran the test using the exact same Lenovo T420 environment as the test above, and tested an anonymous user (no cookie value) hitting the default home page, and an admin logged in (using a valid session cookie—actually all five of the cookies wordpress uses to track valid sessions) visiting the admin Dashboard page (/wp-admin/index.php).

<table>
<thead>
<tr>
  <th>Environment</th>
  <th>WP 4.4 Caching</th>
  <th>Requests/second</th>
  <th>Percent difference</th>
</tr>
</thead>
<tr>
  <td>PHP 5.6.16</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>18.76 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>40.45 req/s</strong></td>
  <td>73% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>40.14 req/s</strong></td>
  <td>73% faster than 5.6</td>
</tr>
<tr>
  <td>PHP 5.6.16</td>
  <td>Bypassed (/wp-admin/index.php, admin)</td>
  <td><strong>13.45 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Bypassed (/wp-admin/index.php, admin)</td>
  <td><strong>28.10 req/s</strong></td>
  <td>71% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Bypassed (/wp-admin/index.php, admin)</td>
  <td><strong>35.43 req/s</strong></td>
  <td>90% faster than 5.6</td>
</tr>
</table>

...and some graphs of the above data:

<h3>PHP 5.6, PHP 7, and HHVM running Wordpress 4.4, anonymous home page</h3>

<p style="text-align: center;">{{< figure src="./wordpress-hhvm-php7-php56-benchmark-home.png" alt="PHP 5 7 and HHVM benchmark comparison of Wordpress 4.4 home page anonymous" width="436" height="319" >}}</p>

<h3>PHP 5.6, PHP 7, and HHVM running Wordpress 4.4, admin dashboard</h3>

<p style="text-align: center;">{{< figure src="./wordpress-hhvm-php7-php56-benchmark-admin.png" alt="PHP 5 7 and HHVM benchmark comparison of Wordpress 4.4 admin dashboard" width="438" height="319" >}}</p>

These results highlight to me how much the particular project's architecture influences the benchmark. Wordpress still uses a traditional quasi-functional-style design, while Drupal 8 is heavily invested in OOP and a bit more formal data architecture. While I'm not as familiar with Wordpress's quirks as I am Drupal, I know that it's no speed demon, and also benefits from added caching layers in front of the site! It's interesting to see that PHP 7 and HHVM are practically neck-and neck for front-facing portions of Wordpress (and FAR faster than 5.6), while HHVM runs even a little faster than PHP 7 for administrative tasks.

<h2 id="d7c10">Drupal 7 Results (concurrency 10)</h2>

I also benchmarked Drupal 7 on Drupal VM for another point of comparison (using <code>-c 10</code>):

<table>
<thead>
<tr>
  <th>Environment</th>
  <th>D7 Caching</th>
  <th>Requests/second</th>
  <th>Percent difference</th>
</tr>
</thead>
<tr>
  <td>PHP 5.6.16</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>511.40 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>736.90 req/s</strong></td>
  <td>36% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Enabled (home, anonymous)</td>
  <td><strong>585.71 req/s</strong></td>
  <td>14% faster than 5.6</td>
</tr>
<tr>
  <td>PHP 5.6.16</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>93.78 req/s</strong></td>
  <td>~</td>
</tr>
<tr>
  <td>PHP 7.0.1</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>169.95 req/s</strong></td>
  <td>57% faster than 5.6</td>
</tr>
<tr>
  <td>HHVM 3.11.0</td>
  <td>Bypassed (/admin, user 1)</td>
  <td><strong>143.25 req/s</strong></td>
  <td>42% faster than 5.6</td>
</tr>
</table>

For these tests, I went to the Performance configuration page prior to running the tests, and enabled anonymous page cache, block cache, and CSS and JS aggregation (to make D7 match up to D8 cached anonymous user results a little more evenly).

Some people point out benchmarks like these and say "Drupal 8 is slow"... and they're right, of course. But Drupal 8 trades performance for better architecture, much more pluggability, and the inclusion of many more essential 'out-of-the-box' features than Drupal 7, so there's that. Having built a few Drupal 8 sites, I don't ever want to go back to 7 again—but it's nice to know that PHP 7 can still accelerate all my existing D7 sites quite a bit!

<h2>Summary</h2>

<blockquote>
<strong>tl;dr</strong>: For Drupal 7 and Drupal 8 at least, PHP 7 takes the performance crown—by a wide margin.
</blockquote>

After running the benchmarks, I scratched my head, because almost <em>every</em> other benchmark I've seen either puts HHVM neck-and-neck with PHP 7 or makes it seem HHVM is still the clear victor. Maybe other people running these benchmarks didn't have PHP's opcache turned on? Maybe something else was missing? Not sure, but if you'd like to reproduce the SUT and find any results <em>different</em> than the above (in terms of percentages), please let me know!

I ran the HHVM benchmarks <em>three</em> times with fresh new VM instances just because I was surprised PHP 7 stepped out in front. PHP 5.6's performance is as expected... it's better than 5.3, but that's not saying much :)

<strong>The moral of the story</strong>: Trust, but verify... <em>especially</em> for benchmarks which compare a plethora of totally different applications, each result can tell a completely different story depending on the test process and system under test! Please run your <em>own</em> tests with your <em>own</em> application before definitively stating that one server is faster than another.

<h2>Installing HHVM in Drupal VM</h2>

Just for posterity, since I want people to be able to reproduce the steps <em>exactly</em>, here's the process I used after using Drupal VM's default config.yml (with Ubuntu 14.04) to build the VM:

<ol>
<li>Log into Drupal VM with <code>vagrant ssh</code></li>
<li><code>$ sudo su</code></li>
<li><code># service php5-fpm stop</code></li>
<li><code># apt-get install -y python-software-properties</code></li>
<li><code># curl http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add -</code></li>
<li><code># add-apt-repository http://dl.hhvm.com/ubuntu</code></li>
<li><code># apt-get update && apt-get install -y hhvm</code></li>
<li><code># update-rc.d hhvm defaults</code></li>
<li><code># /usr/share/hhvm/install_fastcgi.sh</code></li>
<li><code># vi /etc/nginx/sites-enabled/drupalvm.dev.conf</code> and inside the <code>location ~ \.php$|^/update.php</code> block:
<ol>
  <li>Clear out the contents of this configuration block.</li>
  <li>Replace with <code>include hhvm.conf;</code></li>
</ol></li>
<li><code># service hhvm restart</code></li>
<li><code># service nginx restart</code></li>
</ol>

Visit the <code>/admin/reports/status/php</code> page after logging in to confirm you're running HHVM instead of PHP.
