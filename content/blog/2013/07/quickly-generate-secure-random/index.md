---
nid: 2415
title: "Quickly generate secure, random passwords (Mac)"
slug: "quickly-generate-secure-random"
date: 2013-07-02T18:09:51+00:00
drupal:
  nid: 2415
  path: /blogs/jeff-geerling/quickly-generate-secure-random
  body_format: full_html
  redirects: []
tags:
  - 1password
  - mac
  - openssl
  - password
  - profile
  - security
  - terminal
---

If you use Mac OS X, add the following line to your <a href="http://redfinsolutions.com/blog/creating-bashprofile-your-mac">.bash_profile</a>:

```
alias passme='openssl rand 48 -base64 | pbcopy'
```

Whenever you need a password (like when you're registering a new account or resetting your password because yet another online service you used was hacked), just fire up the Terminal and type in <code>passme</code>. Then paste the password that's copied to your clipboard into the password fields, and into your password manager (I use <a href="https://agilebits.com/onepassword">1Password</a>).

This alias simply uses <a href="http://www.openssl.org/docs/apps/openssl.html">openssl</a> to generate a random base64-encoded string with 48 characters (you can change that value to whatever you want). If the online service you use doesn't allow 48 characters in the password field, you should file a support request with that online service, telling them they're being silly only allowing <em>X</em> characters in a password.
