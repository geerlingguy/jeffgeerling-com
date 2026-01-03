---
nid: 2585
title: "3 Small Tweaks to make Apache fly"
slug: "3-small-tweaks-make-apache-fly"
date: 2013-04-06T04:38:01+00:00
drupal:
  nid: 2585
  path: /blog/3-small-tweaks-make-apache-fly
  body_format: full_html
  redirects: []
tags:
  - allowoverride
  - apache
  - keepalive
  - maxclients
  - performance
  - web development
---

Apache is the venerable old-timer in the http server world. There are many younger siblings like <a href="http://nginx.com/">Nginx</a>, <a href="http://www.lighttpd.net/">Lighttpd</a>, and even <a href="http://nodejs.org/api/http.html">Node.js</a>, which are often touted as being faster, lighter, and more scalable alternatives than Apache.

<p style="text-align: center;">{{< figure src="./old-computer-and-man-resized.jpg" alt="Old computer and man" width="250" height="175" >}}
Apache probably looks like this to many Nginx and Lighty users.</p>

Though many alternatives are more lightweight and <em>can be</em> faster in certain circumstances, Apache offers many benefits (not the least of which is abundant documentation and widespread support) and is still a top-notch web server that can be tuned to <em>fly</em>.

Below I describe a few seemingly innocuous Apache configuration settings that can make a huge difference for your site's performance, and help Apache run as fast or faster than alternative servers in many circumstances.

<h2>KeepAlive</h2>

<p style="text-align: center;">{{< figure src="./stayin-alive-resized.jpg" alt="Stayin Alive" width="225" height="225" >}}
There is no need to dance to stay alive.</p>

<em>Note</em>: There is a <a href="http://www.reddit.com/r/webdev/comments/1bs4t0/3_small_tweaks_to_make_apache_fly/">good discussion on Reddit</a> about situations when KeepAlive may be helpful and may, in fact, help Apache (or your server in general) perform better, like if you have an AJAX-heavy site, or if you are serving many requests to mobile or international users. Additionally, if you use a reverse proxy like squid, Varnish, or Nginx in front of Apache, KeepAlive doesn't have the same cost in terms of memory and process usage.

KeepAlive does one simple thing: destroy Apache's ability to handle many concurrent requests. Well, that and speed up existing connections by allowing them to download all assets before closing a TCP connection between a browser and your server (see note above).

This feature was designed to help ensure a browser could load the HTML, some images, stylesheets, etc. from your server all within one connection. Before people started using CDNs like CloudFlare or Amazon S3 for static content, and when most people had internet connections with hundreds of milliseconds of latency, this setting was much more valuable. (It still could be, in some circumstances, for mobile clients on 3G or LTE networks, or if you have an AJAX-heavy site.)

However, for many websites today, either setting the KeepAliveTimeout to a lower value like 1-5 seconds or switching KeepAlive off altogether will be a much better option.

<strong>Real-world example</strong>: When I launched Server Check.in with <a href="https://news.ycombinator.com/item?id=4901350">this thread on Hacker News</a>, the post made the HN front page, meaning I was getting upwards of 10-20 requests per second for an hour or so. I noticed quickly that the server's load was under 1.00, and nothing seemed awry, but trying to access http://www.jeffgeerling.com/ was taking 30 seconds or longer!

Turning off KeepAlive allowed the server to serve more users more quickly, since I didn't have a bunch of httpd threads sitting connected to browsers that had already received all the content they needed. If I want to turn it back on at some point, I'll make sure to set it lower than the default of 30 seconds!

<strong>Caveat</strong>: Now, in my case, I have the MaxClients directive set to <em>45</em>, because with Drupal, I've made sure I don't spawn more threads than my server's limited memory can handle (I'll get to the why's for this below). If you are serving only static/cached content, and don't need to have a bunch of memory-hogging httpd threads for a PHP application like Drupal, you may be able to live with KeepAlive (make sure the timeout is low, still!), and a much larger MaxClients setting.

<h2>MaxClients</h2>

<p style="text-align: center;"><a href="http://www.flickr.com/photos/hktang/4243300265/" title="Queue by hktang, on Flickr">{{< figure src="https://farm3.staticflickr.com/2634/4243300265_cbc0d09155_n.jpg" alt="Queue" width="320" height="213" >}}</a>
Queuing requests may save your server from swapping.</p>

This setting helps Apache fly when your server is getting hit hard, say by a post from Reddit, Hacker News, or some fast and furious marketing campaign.

MaxClients is pretty self-descriptive: it's a setting that tells Apache the maximum number of clients it should serve simultaneously. It's important that you choose a sane value for this setting to prevent any number of bad things from happening:

<ul>
<li>Set it too low and you might cause people to wait for Apache to respond to their request while your server is almost sitting idle, with plenty of RAM and CPU to spare.</li>
<li>Set it too high and watch your server die in a slow, painful death as Apache runs out of RAM and starts swapping to disk. And watch page response times go from milliseconds to seconds or even <em>minutes</em>.</li>
</ul>

There's a really simple way you can know exactly how high to set MaxClients:

<p style="text-align: center;"><strong>(Total RAM - RAM used for Linux, MySQL, etc.) / Average httpd process size</strong>.</p>

To get the average httpd process size, log into your server and run the following on the command line: <code>ps aux | grep 'httpd' | awk '{print $6/1024 " MB";}'</code>. This will output a list of process sizes. If you want to calculate the average on-the-fly, try the command <code>ps aux | grep 'httpd' | awk '{print $6/1024;}' | awk '{avg += ($1 - avg) / NR;} END {print avg " MB";}'</code>. It's best to run this a few different times throughout a normal day to see if there's any major fluctuation in process size.

Let's say your average process is 50 MB (fairly common if you're using PHP and a CMS like Wordpress or Drupal!). You have a VPS with 2 GB of RAM, and you have about .5 GB allocated to MySQL (you can find the full amount with the command <code>ps aux | grep 'mysql' | awk '{print $6/1024 " MB";}'</code>). Let's leave a little overhead for Linux and other bits on the server, say .4 GB:

(2000 MB - 900 MB) / 50 MB = <strong>22</strong>

You should set the MaxClients directive to <em>22</em>, maybe even a little lower to allow for more overhead when your server is getting hammered. Apache's default is usually > 200—this means if your server gets hit by a more than 22 people in a short period of time, it will slow to a crawl, since Apache will gobble up all the RAM!

Setting the MaxClients value lower will allow Apache to simply queue up further requests until it gets a free thread (remember, also, that if you have KeepAlive on, threads will be locked up for [KeepAliveTimeout] seconds!). This might seem like a bad thing... but it's a lot better doing this and serving queued requests quickly (since Apache is working from RAM and not swap space), than trying to serve a hundred requests at once and having massive slowdowns for everyone!

<strong>Real-world example</strong>: One site I work with had a page pick up tons of traffic over the course of a few hours, and the web server (a small 2 GB VPS running LAMP) was getting hammered by up to 100 separate requests <em>per second</em>. We had the MaxClients setting a bit too high, and the server immediately started swapping. It was hard even connecting to the server via SSH, and when I checked <code>top</code>, the server was using about 4 GB of swap (yikes!), and the CPU was spiking around 45 (normally around .2-.3). Once we set MaxClients to a sane amount and restarted Apache, the server was able to get most pages served in 2-3 seconds (instead of 2-3 minutes—if <em>ever</em>). Once traffic died down, we were serving pages in less than 1 second again.

<h2>AllowOverride</h2>

<p style="text-align: center;"><a href="http://www.flickr.com/photos/lifeisaprayer/2210276921/" title="Stephen Colbert Portrait in National Portrait Gallery by geerlingguy, on Flickr">{{< figure src="https://farm3.staticflickr.com/2036/2210276921_5386f41a81_n.jpg" alt="Stephen Colbert Portrait in National Portrait Gallery" width="243" height="320" >}}</a>
Prevent recursion from slowing down Apache.</p>

AllowOverride is basically Apache's way of allowing developers to be lazy. Instead of using a global configuration file and includes, Apache lets you stick an '.htaccess' file in <em>any</em> directory, <em>anywhere</em>, and every time anyone requests any page through Apache, Apache will recursively scan every directory from the site's root to apply rules in .htaccess files.

This is very convenient—especially in situations like shared hosting, where the hosting provider can't be bothered to include hundreds of extra configuration directives in the main <code>httpd.conf</code> file, or (for security purposes) allow everyone on the server to have their own configuration files included via httpd.conf!

However, if you are running only one or two websites on a server, or you generally have full control of the server, you can turn off this convenient feature and simply add the rules into httpd.conf or an include (to add an include, just use something like <code>Include /home/user/public_html/.htaccess</code> inside the VirtualHosts directive for your server, along with the rule <code>AllowOverride None</code>.

<strong>Real-world example</strong>: The impact of this change on server performance varies greatly, and depends mostly on how many directory-levels deep you have files that are served on a given page request. For most people, though, there may be a file in something like <code>/home/user/public_html/sites/sitename/files/images/cached/large/thumbnail/image.jpg</code>. In this case, Apache has to recurse through <em>10</em> levels of directories, parsing all found .htaccess files, just to serve this one image file. For one Drupal site, though, which is a VPS with a virtualized disk on a SAN, I've measured 7-10% faster individual page loads.

<strong>Caveat</strong>: Many CMSes like Wordpress and Drupal rely on .htaccess rules for certain functionality, like 'Clean URLs', www-to-non-www redirects, file upload protections, and static content caching. Make sure you include any relevant .htaccess files in your VirtualHosts directive if you set AllowOverrides to None. See more: <a href="http://knackforge.com/blog/sivaji/how-make-apache-faster-drupal">How to make Apache faster for Drupal</a>.

Also, the real-world speedup you'll get when using a server that has a dedicated, real hard drive or SSD will be much smaller than a server that has a slow drive or uses NAS/SAN storage.

<h2>Conclusion</h2>

These are just three of 'low-hanging fruit' performance-related settings buried in your Apache httpd.conf file; many others will have a big impact on your site's performance as well. With proper tuning, and an eye towards memory usage, you can make Apache as scalable, fast and lightweight as almost any web server.

<em>Photo of <a href="http://www.flickr.com/photos/hktang/4243300265/">queue</a> by hktang on Flickr.</em>
