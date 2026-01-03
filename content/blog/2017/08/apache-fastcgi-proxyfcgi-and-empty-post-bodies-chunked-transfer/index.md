---
nid: 2802
title: "Apache, fastcgi, proxy_fcgi, and empty POST bodies with chunked transfer"
slug: "apache-fastcgi-proxyfcgi-and-empty-post-bodies-chunked-transfer"
date: 2017-08-25T03:45:57+00:00
drupal:
  nid: 2802
  path: /blog/2017/apache-fastcgi-proxyfcgi-and-empty-post-bodies-chunked-transfer
  body_format: markdown
  redirects: []
tags:
  - apache
  - chunked
  - drupal
  - drupal planet
  - fastcgi
  - http
  - open source
  - php
  - post
  - proxy
  - transfer
---

I've been working on building a reproducible configuration for [Drupal Photo Gallery](https://github.com/geerlingguy/drupal-photo-gallery), a project [born out of this year's Acquia Build Hackathon](https://dev.acquia.com/blog/building-an-open-source-photo-gallery-with-face-and-object-recognition-part-1/17/07/2017/18466).

We originally built the site on an [Acquia Cloud CD environment](https://docs.acquia.com/tutorials/getting-started-acquia-cloud-cd/cd-environments), and this environment uses a pretty traditional LAMP stack. We didn't encounter any difficulty using AWS Lambda to post image data back to the Drupal site via Drupal's [RESTful Web Services API](https://www.drupal.org/docs/8/api/restful-web-services-api/restful-web-services-api-overview).

The POST request is built in Node.js using:

```
var reqPost = http.request(options_post, function(res) {
    res.on('data', function (chunk) {
        body += chunk;
    });
});
reqPost.write(JSON.stringify(jsonObject));
reqPost.end();
```

The way this kind of HTTP request works is using `Transfer-Encoding: chunked`. [Chunked encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding#Chunked_encoding) is used in many cases when you need to send potentially large request bodies, and don't necessarily know the full size beforehand (e.g. you can't provide a `Content-Length` in the request).

Apache handles non-chunked transfers without issue, but in many cases, it seems Apache can't correctly pass on the request body if using `Transfer-Encoding: chunked`. Specifically, using PHP-FPM as the backend, I could not get the request body using either:

  - [`mod_proxy_fcgi`](https://httpd.apache.org/docs/2.4/mod/mod_proxy_fcgi.html)
  - [`mod_fcgid`/`fastcgi`](https://httpd.apache.org/mod_fcgid/)

I was using the test PHP script and cURL command listed in [this comment](https://github.com/geerlingguy/drupal-photo-gallery/issues/15#issue-251447688) to test—basically, make a POST or PUT request with chunked encoding, and see what PHP gets via `file_get_contents('php://input')`.

To verify the server _itself_ (pre-Apache) was receiving the request body, I used `sudo ngrep "POST" tcp and port 80` to monitor incoming POST requests... and it indicated the data was definitely reaching the server (ruling out any AWS, DigitalOcean, or on-server firewall or proxy eating the data):

```
$ sudo ngrep "POST" tcp and port 80
interface: eth0 (165.227.96.0/255.255.240.0)
filter: (ip or ip6) and ( tcp and port 80 )
match: POST
####
T 54.237.220.121:40842 -> 165.227.102.121:80 [AP]
  POST /test.php HTTP/1.1..Content-Type: application/json..Host: gallery.jeffgeerling.com..Connection:
  close..Transfer-Encoding: chunked....2d..{"Bucket":"test-bucket","Name":"Test Object"}..
#######
```

So then I decided maybe something in Apache was eating the data. I had been using `proxy_fcgi` to route requests to PHP using CGI, as it seems to be the most modern and efficient approach when running Apache 2.4 and later, but I realized maybe that mod was breaking things.

So I switched to the older (but often-used) Apache `fastcgi` mod and configured _it_ to route to PHP... and instead of having the POST body completely disappear, it gave a warning (so at least that was more helpful...):

```
<title>411 Length Required</title>
</head><body>
<h1>Length Required</h1>
<p>A request of the requested method POST requires a valid Content-length.<br />
</p>
<hr>
<address>Apache/2.4.18 (Ubuntu) Server at gallery.jeffgeerling.com Port 80</address>
```

So finally, I decided to switch to the old but reliable `mod_php`, which runs PHP inside Apache's process forks. And what do you know? The chunked request body arrived intact, and my problem was solved!

I'm guessing I could've also just switched to Nginx, which doesn't seem to suffer from the same CGI bug when proxying requests to PHP-FPM, but in this particular case, I wanted to make sure I was coming closer to replicating the earliest test environment we were using on Acquia Cloud.

During the course of my research on this issue, I ran into a few bug reports that seem slightly circular in nature:

  - [PHP Bug #60826: raw POST data missing with chunked encoding, FastCGI](https://bugs.php.net/bug.php?id=60826) (which points to the next bug...)
  - [Apache Bug #53332: Requests with chunked encoding have no body available to FCGI backend](https://bz.apache.org/bugzilla/show_bug.cgi?id=53332)

The PHP bug comments are correct—it's not an issue with PHP, since PHP-FPM seems to handle things correctly with other web frontends (Nginx, maybe others?). But it's not encouraging seeing the Apache issue has been open since 2012, and even has a patch, but has zero reviews and only one comment in the past 5 years ?.

So the takeaway? If you need to handle chunked content transfer, don't rely on Apache with `mod_proxy_fcgi` or `mod_fastcgi`!

For more background and debugging on the issue, check out the original GitHub issue after which this blog post was written: [Requests from Lambda logging "POST body is: null"](https://github.com/geerlingguy/drupal-photo-gallery/issues/15).
