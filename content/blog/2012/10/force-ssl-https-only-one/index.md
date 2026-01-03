---
nid: 2385
title: "Force SSL (https://) for only one virtual host with .htaccess"
slug: "force-ssl-https-only-one"
date: 2012-10-03T21:43:09+00:00
drupal:
  nid: 2385
  path: /blogs/jeff-geerling/force-ssl-https-only-one
  body_format: filtered_html
  redirects: []
tags:
  - apache
  - htaccess
  - ssl
  - virtualhosts
aliases:
  - /blogs/jeff-geerling/force-ssl-https-only-one
---

Many servers I help administer host many websites; and every now and then, someone wants me to set up a secure (SSL) certificate for one of the websites on the server. Once the certificate is working in Apache, and users can access the site at https://example.com/, they also request that all traffic that was originally destined for either http://www.example.com/ or http://example.com/ be routed to the secure site.

This can be slightly tricky if you're using multiple VirtualHosts on the same server/multisite installation with something like WordPress or Drupal, because if you just add in something like below with multiple sites routed through the same .htaccess file, ALL sites will be routed to the https version (which is not what's desired):

```
RewriteEngine On 
RewriteCond %{SERVER_PORT} 80 
RewriteRule ^(.*)$ https://example.com/$1 [R,L]
```

The above rewrite will tell ANY requests coming into ANY virtual host with <code>http://</code> to redirect to https://example.com/. Instead, you need to add in a little bit more logic to make sure that only the SSL-enabled virtual host gets SSL traffic rerouted:

```
  RewriteEngine On 

  # Redirect to non-www for better SEO.
  RewriteCond %{HTTP_HOST} ^www\.example\.com$ [NC]
  RewriteRule ^(.*)$ http://example.com/$1 [L,R=301]

  # SSL
  RewriteCond %{HTTP_HOST} ^example\.com$ [NC]
  RewriteCond %{SERVER_PORT} 80
  RewriteRule ^(.*)$ https://example.com/$1 [R,L]
```

This is telling Apache to first do a www/non-www redirect, then, after that, only find requests to example.com that are also on port 80 (unsecured), and reroute just <em>those</em> requests to the SSL-enabled site.
