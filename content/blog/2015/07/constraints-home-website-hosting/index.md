---
nid: 2212
title: "The Constraints of in-home Website Hosting"
slug: "constraints-home-website-hosting"
date: 2015-07-31T17:21:02+00:00
drupal:
  nid: 2212
  path: /blog/2015/constraints-home-website-hosting
  body_format: markdown
  redirects:
    - /blog/2016/constraints-home-website-hosting
aliases:
  - /blog/2016/constraints-home-website-hosting
tags:
  - bandwidth
  - dramble
  - drupal
  - hosting
  - power
  - raspberry pi
  - redundancy
  - residential
  - uptime
---

I run dozens of websites, and help build and maintain many others. Almost every one of these sites is served on a server in one of the giant regional data centers in New York, Atlanta, Seattle, LA, Dallas, Chicago, and other major cities in the US and around the world.

These data centers all share some very important traits that are key to hosting high-performing, highly-available websites:

  - Power redundancy (multiple power feeds, multiple backup power sources)
  - 1 Gbps+ upload/download bandwidth (usually with many redundant connections)
  - 24x7 physical security, environmental controls, hardware monitoring etc.

When I choose to host the [Raspberry Pi Dramble website](http://www.pidramble.com/) in my basement, I get almost none of these things. Instead:

  - The fastest Internet connection I can possibly buy at my current home has only a few measly Mbps uplink.
  - I don't have the money to build a triple-redundant power feed or an extra UPS, so I'm just plugging the Pi into my wall and hoping for the best.
  - I have a lock on my door, and the Dramble is in the basement... so I guess physical security is decent enough. But I hope the cluster never goes offline while I'm away!

Living with these constraints doesn't mean disaster, though. There are many ways to mitigate each of the risks and potential disaster scenarios. I'll run through some of the main things I've done, and some things I'm still working on, to see if I can practically host the site at home, and even potentially keep it running during an onslaught of traffic!

## Power Redundancy

One of the simplest things that helps the Dramble stay up during short power outages, brownouts, and the like, is having a small UPS dedicated to the cluster of Pis, the network switch they use to interconnect, and another separate UPS connected to my router and cable modem. In my informal testing, I can keep the entire thing up and running for at least 1-2 hours.

I've also chosen to live in a part of St. Louis that has underground electric service and relatively modern infrastructure, meaning I've only experienced one or two brief outages in the time I've lived here—much better than the average in the rest of the city, where strong thunderstorms frequently knock out overhead power lines.

## Keeping the site up, even when it's down

One thing I'm working on currently, but don't yet have in place, is a mirror of the site on a cloud VPS, along with a form of dynamic DNS, so the domain 'www.pidramble.com' cuts over to the mirror server during outages.

The dynamic DNS configuration is the most pressing need, since my residential Internet connection does _not_ have a static IP address. If my house IP changes, then I'll need to reconfigure the domain name's A records anyways. And if I build this setup in a flexible way, I can integrate with a service like [Server Check.in](https://servercheck.in/) and cutover to a mirrored site when the site's down!

## Network Security

Opening up _any_ access from the outside world into your home network is tempting fate. There are three basic things I'm doing to mitigate any disasters, in this regard:

  1. **Severely limit traffic that gets through the NAT**: I configured my network router to _only_ allow traffic in on port 80, and _only_ to one particular host on my network, which gets a static internal IP address that's mapped to its hardware MAC address.
  2. **Lock down the servers themselves**: In addition to configuring firewalls on all devices on my network, and only installing the minimal set of packages required, I have the Raspberry Pis configured in such a way that someone would need to get full root access to the load balancer (which is the only device reachable from the outside world) to do anything remotely nasty.
  3. **Try to not offend people**: Seriously, this is probably the biggest risk for most sites today—if you offend some terrorist group or organization, or even some random guy who has some free time on his hands, he can take down your site in a bunch of different ways (even if not permanently). I usually keep a low profile, and don't do anything that would make me a target for a hack attempt (hopefully)!

All these points being made—no device that's connected to the Internet is ever 100% safe, this cluster of Raspberry Pis included! I am monitoring traffic and authorization attempts on the cluster of Pis, and have some munin monitoring enabled on other devices on my home network so I can generally see when strange things are happening.

## Overcoming Bandwidth Limitations

With severely limited upstream bandwidth (I generally get 4-5 Mbps on a _good_ day), and only ~100 Mbps downstream, every bit counts. Therefore I'm doing the following to conserve bandwidth usage (especially considering I also need to use the same shared bandwidth for my personal and work needs!):

  - Host images and other 'heavy' resources, when possible, on external domains (so those requests don't need to be served through my home connection).
  - Configure Nginx to gzip resources and send traffic in as efficient a manner as possible.
  - Set caching correctly for all elements, so browsers (and potentially CDNs in the future) can cache content and static resources effectively. The fastest request possible is the one that's served from the end-user's browser cache!

I hope someday to get much, much better Internet upload speeds, as that's my biggest pain point. I don't do 'bundles' so I can't get something like AT&T U-verse with the higher upload speeds (but much slower download), and so far nobody offers fiber-to-the-home in this area of St. Louis :(

## Other Considerations

There are some other things that I can (and may someday) do to make this site even more reliable and highly available, like use a CDN like CloudFlare (**edit**: I'm not using CloudFlare!) to host a distributed cache. That way, even if the site goes down momentarily, most people will still see all the content. For the purposes of this site, and my own fun, that's a little like cheating, though. What's the fun in hosting a site in your house if 99% of the traffic never reaches your house?

I may also be able to get a secondary ISP and figure out a good way to either share bandwidth or configure a failover so the Dramble can serve traffic over either ISP's connection. This costs a bit of extra money, though, and would be a lot of hassle for a feature that I don't care about _too_ much.
