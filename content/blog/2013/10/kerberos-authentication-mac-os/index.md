---
nid: 2435
title: "Kerberos authentication on a Mac OS X workstation with Chrome"
slug: "kerberos-authentication-mac-os"
date: 2013-10-21T18:00:13+00:00
drupal:
  nid: 2435
  path: /blogs/jeff-geerling/kerberos-authentication-mac-os
  body_format: full_html
  redirects: []
tags:
  - authentication
  - Chrome
  - FireFox
  - kerberos
  - mac
  - mac os x
  - safari
---

<a href="http://web.mit.edu/kerberos/www/">Kerberos authentication</a> allows your computer to log into certain services automatically without you having to enter (and re-enter) your password (it's a SSO—single sign-on—service). Kerberos v5 is baked into Windows and Internet Explorer and works great with many LDAP-enabled services (for example, Drupal's <a href="https://drupal.org/project/ldap">LDAP module</a> allows includes a submodule for SSO support).

Kerberos is built into Mac OS X as well, but isn't as simple to use and configure with Chrome and FireFox as it is with Explorer on a Windows workstation. You need to do two things before you can use Kerberos for authentication in Chrome/FireFox:

<ol>
<li>Create a Kerberos ticket with the Ticket Viewer application (/System/Library/CoreServices/Ticket Viewer) or via the command line (<code>kinit username@example.com</code>, then enter your password). See <a href="http://computing.help.inf.ed.ac.uk/kerberos-mac-os-x">this article</a> for more detailed instructions.</li>
<li>Configure Chrome's whitelist to allow authentication against any domains you will be using (along with the domain you used with kinit above). In the Terminal, run the following commands:


```
$ defaults write com.google.Chrome AuthServerWhitelist "*.example.com"
```

<code>$ defaults write com.google.Chrome AuthNegotiateDelegateWhitelist "*.example.com"</code></li>
</ol>

> **2019 Update**: For newer versions of Chrome (~68+), you might need to use the same commands above, but without the double quotes.

In all the above examples, replace 'example.com' with your domain. Also, for the Chrome defaults, you can add multiple domains with commas separating each. The asterisk is a wildcard, so any subdomain would work.

Safari works out of the box if you've created a Kerberos ticket as outlined in step 1; FireFox just needs a couple settings configured on the <code>about:config</code> page.
