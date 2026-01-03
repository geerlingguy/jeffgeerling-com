---
nid: 2386
title: "Trouble sending emails from localhost or MAMP? Check your SPF"
slug: "trouble-sending-emails"
date: 2012-10-09T17:50:42+00:00
drupal:
  nid: 2386
  path: /blogs/jeff-geerling/trouble-sending-emails
  body_format: filtered_html
  redirects: []
tags:
  - dns
  - domain
  - email
  - spf
---

Email is hard. In fact, it's so hard that I probably have five or so blog posts half-written on this blog that I've abandoned simply because I don't think I could distill them down into something worthy of posting (I like being able to explain things understandably or not at all!).

I don't think there's anyone involved in administering a domain name and email who hasn't gotten burned by SPF (TXT) records at least once. <a href="http://www.openspf.org/SPF_Record_Syntax">Here's a good overview of how to build a proper SPF record for your domain</a>. SPF records are used by many (if not most) ISPs these days to evaluate whether an email is coming from a particular domain or not.

Email providers like Google, Apple, Hotmail, etc. will evaluate every email they receive against your domain name's (<em>example.com</em>) SPF record, and if the email didn't originate from the IP address specified, or doesn't match up to any other SPF parameters, the email will be silently deleted. And this will cause you to pull your hair out.

I noticed recently that test emails I have set up through my local development machine (running MAMP) were not being delivered to my email inbox. I checked the log file in /var/logs/mail.log (using the Console app), and was seeing the emails delivered successfully:

```
Oct  9 12:29:01 Computer.local postfix/smtp[9110]: EFCC31C04A53: to=<[redacted]@mac.com>, relay=mx4.mac.com.akadns.net[17.172.36.32]:25, delay=6.8, delays=0.36/0.03/1.1/5.3, dsn=2.5.0, status=sent (250 2.5.0 Ok, envelope id [redacted]@[redacted]-smtpin203.mac.com)
```

So, I knew that something was causing the email to be deleted before arriving in my inbox, and it wasn't a problem with sendmail, postfix, or other local settings.

I remembered that I had updated the sending domain's SPF records recently, though, because some AOL, Comcast, and Charter users were complaining about emails not being delivered. I had to add my server IP address to the SPF record to make sure those hosts (among others) would accept emails from my domain. But I also switched <code>~all</code> to <code>-all</code> in the SPF record, and this caused the me.com mail servers to reject my emails from localhost. Switching that back while in development mode fixed the issue for me.

When you notice that emails are sending properly from your local computer, but not arriving in an inbox, check your SPF records to see if the inbox ISP may be rejecting emails from your domain.
