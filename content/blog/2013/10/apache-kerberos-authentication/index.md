---
nid: 2434
title: "Apache Kerberos Authentication and basic authentication fallback"
slug: "apache-kerberos-authentication"
date: 2013-10-16T18:53:21+00:00
drupal:
  nid: 2434
  path: /blogs/jeff-geerling/apache-kerberos-authentication
  body_format: full_html
  redirects: []
tags:
  - apache
  - authentication
  - config
  - kerberos
  - ux
---

Many businesses and organizations use Active Directory or other LDAP-based authentication systems, and many web applications (like Drupal) can easily integrate with them for authentication and user account provisioning.

The <a href="http://modauthkerb.sourceforge.net/">Kerberos Module for Apache</a> allows users to be automatically logged into your web application, by passing through their credentials behind the scenes. This makes for a seamless user experience—the user never needs to log into your web application if the user is authenticated on his local machine.

A standard configuration for Kerberos authentication inside your Apache configuration file looks like:

```
<Directory "/path/to/site/root">
    # By default, allow access to anyone.
    Order allow,deny
    Allow from All

    # Enable Kerberos authentication using mod_auth_kerb.
    AuthType Kerberos
    AuthName "Your Web Application"
    KrbAuthRealm example.com
    Krb5KeyTab "/path/to/krb5.keytab"
    KrbMethodNegotiate on
    KrbSaveCredentials on
    KrbVerifyKDC on
    KrbServiceName Any
    Require valid-user
</Directory>
```

However, if you use this configuration, users who <em>aren't</em> authenticated via Kerberos will be prompted to log in using basic authentication by their browser:

<p style="text-align: center;">{{< figure src="./http-basic-authentication-dialog.jpg" alt="HTTP Basic Authentication Dialog Window Prompt" width="400" height="237" >}}</p>

This browser-based auth dialog is not very user-friendly, and can't contain any branding or other information besides the string you define as the <code>AuthName</code>. Your web application probably has it's own login screen that looks nicer, allows users to manage passwords like they do with other websites, and already integrates with LDAP/AD behind the scenes.

So, to disable/ignore the basic authentication when automatic Kerberos authentication fails, you need to modify your config to be like the following:

```
<Directory "/path/to/site/root">
    # By default, allow access to anyone.
    Order allow,deny
    Allow from All
    # Require authentication for internal private network users.
    Deny from 10.0.0.0/8

    # Enable Kerberos authentication using mod_auth_kerb.
    AuthType Kerberos
    AuthName "Your Web Application"
    KrbAuthRealm example.com
    Krb5KeyTab "/path/to/krb5.keytab"
    KrbMethodNegotiate on
    KrbSaveCredentials on
    KrbVerifyKDC on
    KrbServiceName Any
    Require valid-user

    Satisfy Any
</Directory>
```

Removing <code>Require valid-user</code> and adding <code>Satisfy Any</code> tells Apache to still attempt Kerberos authentication, but if that fails, allow access anyways. Then your web application can take care of the authentication using it's own screen/mechanism.

Read more:
<ul>
<li><a href="http://httpd.apache.org/docs/2.2/mod/core.html#require">Apache Require directive</a></li>
<li><a href="http://httpd.apache.org/docs/2.2/mod/core.html#satisfy">Apache Satisfy directive</a></li>
<li><a href="http://modauthkerb.sourceforge.net/">mod_auth_kerb - Kerberos Module for Apache</a></li>
</ul>
