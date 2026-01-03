---
nid: 2891
title: "Nginx serving up the wrong site content for a Drupal multisite install with https"
slug: "nginx-serving-wrong-site-content-drupal-multisite-install-https"
date: 2018-11-26T01:07:42+00:00
drupal:
  nid: 2891
  path: /blog/2018/nginx-serving-wrong-site-content-drupal-multisite-install-https
  body_format: markdown
  redirects: []
tags:
  - cache
  - drupal
  - drupal planet
  - https
  - multisite
  - nginx
  - proxy
---

I had a 'fun' and puzzling scenario present itself recently as I finished moving more of my Drupal multisite installations over to HTTPS using Let's Encrypt certificates. I've been running this website—along with six other Drupal 7 sites—on an Nginx installation for years. A few of the multisite installs use bare domains, (e.g. jeffgeerling.com instead of _www._ jeffgeerling.com), and because of that, I have some http redirects on Nginx to make sure people always end up on the _canonical_ domain (e.g. example.com instead of _www._ example.com).

My Nginx configuration is spread across multiple .conf files, e.g.:

```
abacus.com.conf
example.com.conf
www.jeffgeerling.com.conf
www.example-two.com.conf
```

The problem occurred soon after I started serving "example.com" (not the actual site... just using demo domains) using HTTPS. From time to time, my monitoring (courtesy of [Server Check.in](https://servercheck.in/)) would alert me that the content on the site was different. As it turns out, every time this happened, it would be serving up the HTML from "abacus.com" instead of "example.com".

It seems there were a variety of contributing factors:

  - I am using Nginx's [HTTP Proxy module](http://nginx.org/en/docs/http/ngx_http_proxy_module.html) (the `proxy_cache` directives), which stores a cached copy of pages matching certain conditions (e.g. no cookies in the user session) on the disk for faster repeat accesses (kind of like Varnish-lite).
  - I have "example.com" loading with HTTPS, while "abacus.com" is still loading without HTTPS (just due to my laziness ?).
  - I have each domain's configuration in its own config file inside `/etc/nginx/sites-enabled` (this is on an Ubuntu server).

From some trial-and-error, I found that Nginx is loading the config files alphabetically, and then—since I don't have any particular `server` set as the Nginx-wide `default`, it will try to load whatever directive most closely matches by `server_name`. And if you don't have a certificate for the non-bare domain for a bare-domain URL, or vice-versa, Nginx will go back to the first `server` and proxy that request to the backend/upstream for that server.

Also, it will cache that result with Nginx's default `proxy_cache_key`, which is basically `$scheme$proxy_host$request_uri;`. But note the _basically_. As it turns out, the docs state:

> By default, the directive’s value is close to the string:
> 
>     proxy_cache_key $scheme$proxy_host$uri$is_args$args;

The actual hashed value seems to use the proxy _backend_/_upstream_ name, not necessarily the _host_... meaning when future requests come in that match the hash of the backend/upstream name, it _can_ result in the wrong cache being served for certain _subdomains_ of a root domain. So if you are trying to serve up "example.com", but someone already loaded "www.example.com" and it had the wrong HTML returned (because Nginx matched it to another server), then future requests to "example.com" will serve up the incorrect HTML as well.

I'm still digging a little bit to try to figure out if there's a more elegant way to solve the problem of serving proxied, HTTPS traffic to a root domain without a wildcard cert (therefore I can't do an HTTPS redirect from www to non-www). But for now, what _seems_ to be working is specifically overriding the `proxy_cache_key` to include the actual `$host` instead of the not-actually-the-host as mentioned in the docs:

    proxy_cache_key $scheme$host$uri$is_args$args;

I'll update this post if I find any downsides to using this solution. After applying the configuration change across all `server` configs, I emptied the Nginx cache directory (`sudo rm -f /var/cache/nginx/*`) and restarted Nginx (`sudo systemctl restart nginx`).
