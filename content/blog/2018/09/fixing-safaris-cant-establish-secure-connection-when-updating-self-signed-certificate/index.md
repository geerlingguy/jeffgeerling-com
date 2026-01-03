---
nid: 2872
title: "Fixing Safari's 'can't establish a secure connection' when updating a self-signed certificate"
slug: "fixing-safaris-cant-establish-secure-connection-when-updating-self-signed-certificate"
date: 2018-09-18T16:27:01+00:00
drupal:
  nid: 2872
  path: /blog/2018/fixing-safaris-cant-establish-secure-connection-when-updating-self-signed-certificate
  body_format: markdown
  redirects: []
tags:
  - apple
  - certificate
  - mac
  - safari
  - security
  - self-signed
  - ssl
  - tls
---

I do a lot of local development, and since almost everything web-related is supposed to use SSL these days, _and_ since I like to make local match production as closely as possible, I generate a lot of self-signed certificates using OpenSSL (usually [using Ansible's openssl_* modules](//www.jeffgeerling.com/blog/2017/generating-self-signed-openssl-certs-ansible-24s-crypto-modules)).

This presents a problem, though, since I use Safari. Every time I rebuild an environment using my automation, and generate a new certificate for a domain that's protected with [HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security), I end up getting this fun error page:

{{< figure src="./safari-cant-open-page-establish-secure-connection.jpg" alt="Safari Can&#39;t Open the Page - Safari can&#39;t open the page because Safari can&#39;t establish a secure connection to the server servername." width="650" height="437" class="insert-image" >}}

_Safari Can't Open the Page – Safari can't open the page because Safari can't establish a secure connection to the server 'servername'._

There's no possible way of adding an exception, or deleting the old cert from Keychain Access, or really any way to get around this—at least none exposed via Safari's UI.

There are only three ways to get around this annoying issue—one is good for one-off use cases, one requires the deletion of the HSTS cache, the other requires wiping _all_ your web history:

## Method 1 - Private browsing session

  1. Open a new Private Browsing window (Shift + ⌘ + N)
  2. You should see the link to add an exception for the site.

Note that this exception only persists during that private browsing session. This definitely works in a pinch, or when you're doing a bunch of HTTPS testing.

## Method 2 - Clear HSTS cache

This is the easiest method which doesn't require to to re-login to every single site and service you use but allows more permanent exceptions to be stored. Basically:

  1. `killall nsurlstoraged` to stop the HTTP storage manager (since it has an in-memory cache of the HSTS hosts).
  2. `rm -f ~/Library/Cookies/HSTS.plist` to delete the HSTS cache file.
  3. `launchctl start /System/Library/LaunchAgents/com.apple.nsurlstoraged.plist` to start up `nsurlstoraged` again.

I'd rather have the ability to drop just one domain, but it's really annoying trying to edit plist files (it basically has to be done in Xcode nowadays).

## Method 3 - Clear all browsing history

This method will log you out of all websites and sessions in Safari, and also wipe out local storage, etc. Not a horrible thing to do every now and then, but it can be really annoying if you do it a few times a day!

  2. Go to Safari > Clear History... > all history.

There's apparently also a way to force the cert by [copying it into Keychain Access manually, then trusting it via Terminal command](https://stackoverflow.com/a/47492154), but that's super annoying for projects where I rebuild them sometimes dozens of times a day.

The self-signed certs you add exceptions for are also added to Keychain Access, but deleting them from there and restarting Safari doesn't do the trick.

After using one of the methods above, I am able to see the options to add an exception by clicking the 'visit the website' link:

{{< figure src="./this-connection-is-not-private-safari-https-exception-security-certificate.jpg" alt="Safari HTTPS Certificate exception - This Connection is not Private" width="650" height="426" class="insert-image" >}}
