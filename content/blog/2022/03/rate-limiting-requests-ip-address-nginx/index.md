---
nid: 3179
title: "Rate limiting requests per IP address in Nginx"
slug: "rate-limiting-requests-ip-address-nginx"
date: 2022-03-08T20:11:06+00:00
drupal:
  nid: 3179
  path: /blog/2022/rate-limiting-requests-ip-address-nginx
  body_format: markdown
  redirects: []
tags:
  - configuration
  - ddos
  - nginx
  - php
  - protection
  - rate limit
  - security
---

Just wanted to post this here, since I've had to do this from time to time, and always had to read through the docs and try to build my own little example of it...

If you're trying to protect an Nginx server from a ton of traffic (especially from a limited number of IP addresses hitting it with possibly DoS or DDoS-type traffic), and don't have any other protection layer in front, you can use `limit_req` to rate limit requests at whatever rate you choose (over a given time period) for any location on the server.

```
# Add this to your virtual host config file.
limit_req_zone $binary_remote_addr zone=mylimit:10m rate=10r/s;

# Later, in a `server` block:
server {
    location ~ \.php$ {
        limit_req zone=mylimit;
        ...
    } 
    ...
}
```

I have had to do this sometimes when I noticed a few bad IPs attacking my servers. You can adjust the `rate` and `zone` settings to your liking (the above settings limit requests to any PHP script to 10 per second over a 10 minute period).

You may also be interested in [selectively blocking POST requests for certain IP addresses/ranges](https://www.cyberciti.biz/faq/nginx-block-post-requests-urls-for-spammer-ip-address-cidr/).
