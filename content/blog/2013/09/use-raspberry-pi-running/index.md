---
nid: 2429
title: "Use a Raspberry Pi running Raspian OS behind a proxy server"
slug: "use-raspberry-pi-running"
date: 2013-09-25T01:44:09+00:00
drupal:
  nid: 2429
  path: /blogs/jeff-geerling/use-raspberry-pi-running
  body_format: full_html
  redirects: []
tags:
  - chromium
  - linux
  - midori
  - proxy
  - raspberry pi
  - raspbian
aliases:
  - /blogs/jeff-geerling/use-raspberry-pi-running
   - /blogs/jeff-geerling/use-raspberry-pi-running
---

I've been working on figuring out some interesting ways to use my revision A Raspberry Pi, and one of the things I'm doing with it requires it to work correctly behind a corporate proxy server. If you're in a similar situation, and need your Pi to work with a proxy server, it's simple to get set up:

You need to edit the <code>~/.profile</code> file (where <code>~</code> is your home folder, e.g. <code>/home/jeffgeerling</code>, adding the following lines to the bottom of the file:

```
# Proxy server (example: http://username:password@10.0.0.1:8080). User/pass optional.
export http_proxy=http://[user]:[pass]@[proxy_server_address]:[port]

# Proxy exclusions (don't use the proxy server for these hostnames and IP addresses).
export no_proxy=localhost,127.0.0.0/8
```

If you'd also like the proxy to apply when running <code>sudo</code> commands and when using your Pi as the root user, you need to add the same configuration to <code>/root/.profile</code> (this would be helpful if you need to use <code>sudo apt-get</code> to install or update software packages).

After you edit and save the file, you can either enter <code>source ~/.profile</code> to get the new proxy settings to stick for your current session, or log out and log back in.

One caveat: proxy support varies widely by browser—Midori is configured to use the proxy you set up by default, but <a href="http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=540308">doesn't honor the no_proxy environment variable</a>. I tend to use Chromium instead, so it's not an issue for me.
