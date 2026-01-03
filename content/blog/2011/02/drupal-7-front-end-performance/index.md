---
nid: 2306
title: "Drupal 7 Front-End Performance - Shared Hosting Recommendations"
slug: "drupal-7-front-end-performance"
date: 2011-02-22T04:42:41+00:00
drupal:
  nid: 2306
  path: /blogs/jeff-geerling/drupal-7-front-end-performance
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - hosting
  - performance
  - shared hosting
aliases:
  - /blogs/jeff-geerling/drupal-7-front-end-performance
---

<p>{{< figure src="./speedometer-boost-drupal.png" alt="Speedometer - Boosted" width="125" height="125" >}}I've spent a lot of time working on making sure my smaller Drupal sites (mostly run on shared hosts or very small VPSes) run lean and mean. This helps the pages load faster, users are happier, and my hosting providers don't have to shut down any of my sites, even when they're under pretty heavy load.</p>

<p>Here are my three recommendations for making your Drupal 7 website run great on a shared (or low-end VPS) host:</p>

<ol>
	<li><strong>Enable <a href="http://drupal.org/project/boost">Boost</a>. It's a life-saver.</strong>
Boost caches your pages as plain ol' HTML files, so Apache can serve them up almost as quickly as people can request them. This will greatly improve your site's performance if you serve mostly anonymous users. If you care about stats, don't bother with the Statistics or Tracker module (they don't play nice with caching/Boost). Instead, use Google Analytics or another JS-based service. Or use your server's built-in apache log stats (most shared hosts provide AWStats or something similar).</li>
	<li><strong>Enable all the performance options on the Configuration &gt; Performance page.</strong>
Specifically, check the boxes next to "Cache pages for anonymous users," "Cache blocks," "Compress cached pages," "Aggregate and compress CSS files," and "Aggregate JavaScript files."</li>
	<li><strong>Add the rules below to your .htaccess file (if possible).</strong>
The rules don't do a ton, but they'll improve front-end performance a little, if your hosting company allows .htaccess overrides (most do). If you use the mod_deflate rule, you don't necessarily need to check the "Compress cached pages" checkbox on the Performance settings page.</li>
</ol>

<p>Rules to be added to the .htaccess file (I add this little block of code to the top of the file, just under the "Apache/PHP/Drupal settings:" comments):</p>

```
##### Midwestern Mac-recommended additions #####

# Use mod_deflate to gzip components
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/css application/x-javascript application/javascript text/plain text/html text/xml application/xml
</IfModule>

# Disable ETags (can help if you're using multiple servers, or use cloud hosting)
# see: http_://www.askapache.com/htaccess/apache-speed-etags.html for more info
FileETag None

################################################
```

<p>The last thing I'll mention is that you should definitely consider disabling any module that you're not actively using... and maybe even some that you are. If the module is not essential to your website's core purpose/functionality, consider whether it's more important for pages to load quickly, or for that module's functionality to be present. The less modules, the faster your site will go (and, often, the less cluttered it will be!).</p>

<p>Happy fast page-loading!</p>

<p><em>P.S. I'm working on a more authoritative <a href="http://www.jeffgeerling.com/articles/web-design/2010/drupal-performance-white-paper">Drupal Performance White Paper</a>, on my personal website—I'll be compiling thoughts on performance and Drupal, from the perspective of a guy who maintains many Drupal sites, running on dedicated servers, VPSes, and the cheapest shared hosting available, with varying amounts of traffic/popularity. <a href="http://www.jeffgeerling.com/articles/web-design/2010/drupal-performance-white-paper" rel="nofollow">Check it out!</a></em></p>
