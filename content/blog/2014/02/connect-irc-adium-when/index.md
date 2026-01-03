---
nid: 2444
title: "Connect to IRC via Adium when connected through an LTE hotspot"
slug: "connect-irc-adium-when"
date: 2014-02-11T21:12:25+00:00
drupal:
  nid: 2444
  path: /blogs/jeff-geerling/connect-irc-adium-when
  body_format: full_html
  redirects: []
tags:
  - 6667
  - adium
  - irc
  - mac
  - proxy
  - ssh
aliases:
  - /blogs/jeff-geerling/connect-irc-adium-when
---

When I'm on the go, I like to use my iPhone 5s as a hotspot, as I get 10-20 Mbps up and down (much better than any public WiFi I've used), and it's a more secure connection than a public, unsecured hotspot.

However, when I open Adium, I'm greeted with:

```
Notice -- You need to identify via SASL to use this server
```

To fix this, I forward port 6667 on my Mac to one of my remote servers using SSH, then tell Adium to use that server's connection with my Mac as a SOCKS5 proxy. If you need to do this, you can do the following:

<ol>
<li>We need to forward port 6667 from your local Mac to a remote server ('example.com') to which you have SSH access. In Terminal, enter: <code>ssh -D 6667 username@example.com</code></li>
<li>In Adium, go to the IRC connection settings, and under Proxy, check the 'Connect using proxy' checkbox, choose 'SOCKS5' for Type, enter 'localhost' for Server, and '6667' for Port (see screenshot below).</li>
</ol>

<p style="text-align: center;">{{< figure src="./adium-socks5-proxy.png" alt="Adium SOCKS5 proxy settings for IRC tunnel on port 6667" width="665" height="549" >}}</p>
