---
nid: 2819
title: "Stripping the 'Vary: Host' header from an Apache response using Varnish"
slug: "stripping-vary-host-header-apache-response-using-varnish"
date: 2017-11-21T17:07:30+00:00
drupal:
  nid: 2819
  path: /blog/2017/stripping-vary-host-header-apache-response-using-varnish
  body_format: markdown
  redirects: []
tags:
  - apache
  - headers
  - http
  - proxy
  - varnish
  - vary
  - vcl
---

A colleague of mine found out that many static resource requests which _should've_ been cached upstream by a CDN were _not_ being cached, and the reason was an extra `Vary` http header being sent with the response—in this case `Host`.

It was hard to reproduce the issue, but in the end we found out it was related to [Apache bug #58231](https://bz.apache.org/bugzilla/show_bug.cgi?id=58231). Basically, since we used some `RewriteCond`s that evaluated the `HTTP_HOST` value before a `RewriteRule`, we ran into a bug where Apache would dump a `Vary: Host` header into the request response. When this was set, it effectively bypassed Varnish's cache, as well as our upstream CDN... and since it applied to all image, css, js, xml, etc. requests, we saw a _lot_ of unexpected volume hitting the backend Apache servers.

To fix the issue, at least until the upstream bug is fixed in Debian, we decided to strip `Host` from the `Vary` header inside our Varnish default.vcl. Inside the `vcl_backend_response`, we added:

```
# Instruct Varnish what to do in the case of certain backend responses (beresp).
sub vcl_backend_response {
    # Remove 'Host' if set in the Vary header (see Apache bug #58231).
    if (beresp.http.Vary ~ "Host") {
        set beresp.http.Vary = regsub(beresp.http.Vary, ",? *Host *", "");
        set beresp.http.Vary = regsub(beresp.http.Vary, "^, *", "");
        if (beresp.http.Vary == "") {
            unset beresp.http.Vary;
        }
    }

    ...
}
```

Then, after a Varnish restart, we saw `Host` stripped out of the Vary header (no matter whether it was the first item in the header, the last item, in the middle, or the only item).

I needed to also test whether this was working correctly locally, and for that, I brought up Nginx, and added a quick server that Varnish could target as the backend. In my Nginx config file for the test backend, I set:

```
server {
    listen 8080;
    server_name localhost;

    # Use a root dir with a plain index.html file.
    root /var/www/html;

    location / {
        # Add one or more Vary headers for testing.
        add_header "Vary" "Host";
        add_header "Vary" "Accept-Encoding";
    }
}
```

And in Varnish's default.vcl, I pointed to this backend and restarted:

```
backend default {
    .host = "127.0.0.1";
    .port = "8080";
    .first_byte_timeout = 60s;
}
```

Then I could either use Safari/Chrome's web inspector to see the response headers, or use `curl --head varnish-server-url-here` to see what the `Vary` header outputs.
