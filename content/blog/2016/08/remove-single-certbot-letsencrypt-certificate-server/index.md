---
nid: 2687
title: "Remove a single Certbot (LetsEncrypt) certificate from a server"
slug: "remove-single-certbot-letsencrypt-certificate-server"
date: 2016-08-19T00:44:42+00:00
drupal:
  nid: 2687
  path: /blog/2016/remove-single-certbot-letsencrypt-certificate-server
  body_format: markdown
  redirects: []
tags:
  - certbot
  - certificate
  - how-to
  - letsencrypt
  - ssl
  - tutorial
---

I've been using [Certbot](https://certbot.eff.org/) to generate and renew [Let's Encrypt](https://letsencrypt.org/) certificates for most of my smaller sites and services, and recently I needed to move a site from one server to another. It was easy enough to build the new server, then generate the certificate on the new server and use it in Apache or Nginx's configuration.

However, on the old server I no longer wanted to have the old certificate get renewed every week/month/etc. during the `certbot-auto` cron runs, so I looked to see if there was a way to simply have Certbot delete a certificate. It turns out there's not, but there _is_ an issue—[adding `-delete` option to remove the cert files](https://github.com/certbot/certbot/issues/2551)—to add this functionality.

In the mean time, after you've moved the site off your old server, and made sure Apache's not looking for the certificate for that site anymore, the process for manually removing the certificate is straightforward—just delete the relevant files inside `/etc/certbot` (or `/etc/letsencrypt` if you have an older server that used the `letsencrypt` tool before it was changed to `certbot`):

    rm -rf /etc/certbot/archive/[sitename]/
    rm -rf /etc/certbot/live/[sitename]/
    rm -rf /etc/certbot/renewal/[sitename].conf

After removing those directories and files, future runs of `certbot-auto` will no longer attempt to renew those certificates. Note that _technically_ you only need to remove the `.conf` file inside `/etc/certbot/renewal`, but I don't like leaving valid keys/certs hanging around on any of my servers.

For even better security, you can _revoke_ the certificate before deleting the configuration, with something like `certbot revoke -d [sitename]`.
