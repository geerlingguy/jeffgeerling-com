---
nid: 2699
title: "How to get your server's emails through Gmail's spam filter with Exim"
slug: "how-get-your-servers-emails-through-gmails-spam-filter-exim"
date: 2016-09-29T14:57:01+00:00
drupal:
  nid: 2699
  path: /blog/2016/how-get-your-servers-emails-through-gmails-spam-filter-exim
  body_format: markdown
  redirects: []
tags:
  - delivery
  - dkim
  - dns
  - email
  - mail
  - spf
  - tutorial
---

There's one thing that most first-time server administrators have in common: they have to either learn a lot about how email and spam filters work, or they offload email delivery entirely to a third party.

The latter option is often the best option, since successful email delivery is a _crazy_ complicated endeavor. I know, because I've worked on two separate medium-volume email delivery systems in the past (over 1,000,000 emails/month, to hundreds of thousands of recipients), and for both of them, I spent likely 1,000+ hours on email delivery problems.

But for many smaller sites, non-profits, and side projects, there's no budget for a reliable 3rd party email delivery service.

Recently, I was rebuilding a personal photo sharing website (just used for myself and my family and friends), and I decided to wipe the server clean and start over with an Ansible-based configuration that I could deploy locally and to any cloud environment. For email delivery, I decided to install Exim on top of a CentOS 7 minimal base image, and I used Drupal/PHP's mail functionality to pass messages to Exim.

With all the defaults, I was informed that none of the site users were receiving emails anymore. So I started digging. For the benefit of anyone who hasn't dealt with Exim, SPF, DKIM, reverse DNS, TXT records, or raw message bodies in the past, this is more-or-less the same debugging technique I use whenever I notice emails hitting spam filters:

  1. Check `/var/log/exim/main.log` to see what's happening when Exim tries to send emails (sometimes this will be rather obvious, like "Gmail didn't see the IPv4 or IPv6 address your server advertised when it pinged your domain").
  2. Open up the raw source of the email message (which may be in your junk mailbox) to find the `Received` headers in the email, which will indicate whether Gmail, iCloud, etc. think it's junk.
  3. Realize you didn't set up an SPF `TXT` record for the domain in question.
    1. Simple format for a single server with both IPv4 and IPv6 addresses: `v=spf1 a mx ip4:168.235.99.48 ip6:2604:180:2:25d:4:3:2:1 -all`
    2. Read more about the [SPF record syntax](http://www.openspf.org/SPF_Record_Syntax).
  4. Realize you didn't set up IPv6 DNS records for the domain in question.
    1. In my case, the server had both IPv4 and IPv6 configured locally, but I had only added an A record for the IPv4 address. I had to login to Name.com and add an AAAA record with the server's advertised IPv6 address, since that's what Exim was defaulting to when sending email.
  5. Once you have your TXT and AAAA records configured, test the response with:
    1. `dig +short example.com txt` (for SPF)
    2. `dig +short example.com AAAA` (for IPv6)
  6. Make sure there are Reverse DNS entries for both your IPv4 and IPv6 addresses.
    1. In my case, with RamNode as my host, I logged into SolusVM and set these up in the control panel.
  7. Send another email from the server to yourself, then view the raw source/headers.
    1. If you see that SPF is flagged as `none`, restart your server and also wait for DNS TXT record to propagate (some mail hosts seem to cache this for a while).
    2. If you see that SPF is flagged as `neutral`, check to make sure Exim is picking up the right hostname. In my case it was showing emails as from `apache@example` (without the .com).
  8. If Exim isn't delivering with the right hostname, and you see the right hostname by running `hostname -f` on your server, fix Exim by manually overriding the `primary_hostname`
    1. `sudo vi /etc/exim/exim.conf` (on RedHat; other OSes may differ in the config path).
    2. Uncomment the `primary_hostname` and set it to your server's primary domain (should be same as Reverse DNS entry you added earlier).
    3. `sudo systemctl restart exim` (Restart Exim so the change takes effect.

After following through this entire process, I now get the following in the headers in the delivered message:

```
Received-SPF: pass (mr21p00im-spfmilter001.me.com: domain of
 apache@example.com designates 173.192.7.98 as permitted sender)
 receiver=mr21p00im-spfmilter001.me.com; client-ip=173.192.7.98;
 helo=mx3.name.com; envelope-from=apache@example.com;
```

> Note that I had to add multiple `ip4` addresses to the TXT SPF record—one for my server's IP, and then an additional one for each of the name.com MX servers (mx1.name.com, mx2.name.com, etc.). Gmail didn't complain about this, but iCloud did.

> Note that these are the basic steps for getting emails with otherwise high-quality content delivered. If you have spammy _message content_ (e.g. "Click this email link to win a million dollars!"), it's very likely your message will get flagged as spam regardless of how well you set up your domain and email server.

> Also note that for more important and high-volume email delivery, you should also implement [DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) for your messages; but I find that it's not alway necessary to use DKIM for smaller sites and lower email volumes.
