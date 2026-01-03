---
nid: 2660
title: "Fixing ERR_SPDY_INADEQUATE_TRANSPORT_SECURITY SSL error in Chrome"
slug: "fixing-errspdyinadequatetransportsecurity-ssl-error-chrome"
date: 2016-06-11T03:49:08+00:00
drupal:
  nid: 2660
  path: /blog/2016/fixing-errspdyinadequatetransportsecurity-ssl-error-chrome
  body_format: markdown
  redirects: []
tags:
  - Chrome
  - error
  - hosted apache solr
  - http2
  - nginx
  - performance
  - spdy
---

Recently, I was upgrading the infrastructure for [Hosted Apache Solr](https://hostedapachesolr.com/), and as part of the upgrade, I jumped from Nginx 1.8.x to 1.10.x, which [includes HTTP/2 support](https://www.nginx.com/blog/nginx-1-9-5/). I had previously used SPDY support in my server configuration to help the site run better/faster on modern browsers with SPDY support:

```
server
{
    listen 443 ssl spdy;
    server_name hostedapachesolr.com;
    ...
}
```

After the server upgrades, I was getting the following error on Nginx restarts:

```
nginx: [warn] invalid parameter "spdy": ngx_http_spdy_module was superseded by ngx_http_v2_module in /etc/nginx/conf.d/hostedapachesolr.conf:10
```

So I switched the configuration to use `http2` instead of `spdy` on the `listen` line, and restarted nginx.

Everything worked great in Safari and FireFox, but when I tried loading the page in Chrome, I was greeted with the following error:

<p style="text-align: center;">{{< figure src="./chrome-site-cannot-be-reached-error.png" alt="Chrome - Site cannot be reached, ERR_SPDY_INADEQUATE_TRANSPORT_SECURITY" width="601" height="346" class="insert-image" >}}</p>

It reads:

```
This site can’t be reached
The webpage at https://hostedapachesolr.com/ might be temporarily down or it may have moved permanently to a new web address.
ERR_SPDY_INADEQUATE_TRANSPORT_SECURITY
```

Looking further into the problem, it seems the HTTP/2 cipher suites are a little more strict than older protocols, and you need to make sure one of the supported ciphers is listed first in your `ssl_ciphers` configuration. In my case, I ended up using:

```
server
{
    listen 443 ssl http2;
    server_name hostedapachesolr.com;
    ...
    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:AES256+EECDH:AES256+EDH';
    ...
}
```

You can also look at the [recommended cipher configuration provided by CloudFlare](https://support.cloudflare.com/hc/en-us/articles/200933580-What-cipher-suites-does-CloudFlare-use-for-SSL-) for more ideas.

After letting Ansible reprovision the server with the new settings, the site's working great in Chrome (as well as other browsers), the [Qualys SSL test score is A+](https://www.ssllabs.com/ssltest/analyze.html?d=hostedapachesolr.com), and HTTP/2 support is working great!
