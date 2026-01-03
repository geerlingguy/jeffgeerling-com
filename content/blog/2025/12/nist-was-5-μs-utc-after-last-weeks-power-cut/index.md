---
nid: 3523
title: "NIST was 5 \u03bcs off UTC after last week's power cut"
slug: "nist-was-5-\u03bcs-utc-after-last-weeks-power-cut"
date: 2025-12-22T16:28:05+00:00
drupal:
  nid: 3523
  path: /blog/2025/nist-was-5-μs-utc-after-last-weeks-power-cut
  body_format: markdown
  redirects:
    - /blog/2025/nist-was-5-μs-after-last-weeks-power-cut
aliases:
  - /blog/2025/nist-was-5-μs-after-last-weeks-power-cut
tags:
  - bps
  - clock
  - gps
  - internet
  - nist
  - ntp
  - time
  - timing
---

If you were 5 microseconds late today, blame it on NIST.

Their facility in Boulder Colorado just had its power cut for multiple days. After a backup generator failed, their main ensemble clock lost track of UTC, or Universal Time Coordinated.

But even if you used the [NTP timing servers they run](https://tf.nist.gov/tf-cgi/servers.cgi), they were never off by more than 5 microseconds.

5 μs might seem insignificant. But it _is_ significant for scientists and universities who rely on NIST's more [specialized timing signals](https://wsts.atis.org/wp-content/uploads/2023/03/04-Judah-Levine.The-NIST-Fiber-Based-Time-Service.pdf).

But no, you don't need to panic. And yes, they have it under control now.

But I thought I'd go over what happened, what it means, and what we can learn from NIST's near-outage.

## Video

This blog post is a lightly-edited transcript of my most recent YouTube video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/ZRB7pjRVVkI" frameborder='0' allowfullscreen></iframe></div>
</div>

## What happened

The NIST campus, which distributes Internet time on six of the most popular NTP servers, [lost power last Wednesday](https://groups.google.com/a/list.nist.gov/g/internet-time-service/c/o0dDDcr1a8I).

The power company was forced to cut power because of [wind gusts over 100 mph](https://www.youtube.com/watch?v=E4dMRgPIY_s) (160 km/h). Power lines were coming down and they didn't want to risk starting a wildfire.

The whole campus was locked down for safety, so nobody could enter or exit.

They have backup generators. And those were working... but apparently one of the generators failed after a couple days. Specifically, the generator that powered the main [ensemble clock](https://navi.ion.org/content/67/2/333) that's used by the NTP servers.

Things were dicey last Friday, and they couldn't get any more staff in to fix it.

It got to the point Jeff Sherman, the Group Leader for NIST's Time Realization and Distribution Group, considered shutting down the backup generator that powered the time servers. That would've prevented them from sending out inaccurate time, which would be worse than no time at all for a lot of applications.

NTP's designed so you have [multiple servers](https://access.redhat.com/solutions/58025) you look at, and if one fails, it won't cause you to lose time.

And luckily for NIST, they have _another_ building in their Boulder campus with more clocks, and that building could transfer time back to the one that had the power failure, if they needed to.

But yesterday Jeff posted [another update](https://groups.google.com/a/list.nist.gov/g/internet-time-service/c/OHOO_1OYjLY): power was restored, and _apparently_ there were still some staff on-site who saved the clocks.

They were able to re-route emergency power after the main backup generator went down.

Battery backups, I'm assuming some big UPSes, were able to bridge the gap, until they got the _backup_ backup power going.

When all was said and done, their monitoring showed deviation from UTC was less than 5 μs.

Seeing all that, Jeff and the team at NIST decided to keep their time servers online.

But why would they do that, if they were off? Well, time scales are important here. If you're on a Mac like I am, go in the Terminal and run `sntp time-a-b.nist.gov`.

This or a command like `ntpdate` on Linux gives back an error bound, that shows latency between your computer and the [NTP time servers](https://tf.nist.gov/tf-cgi/servers.cgi).

```
$ sntp time-a-b.nist.gov
+0.005771 +/- 0.035081 time-a-b.nist.gov 132.163.96.1
```

In my case, it's showing 0.035 seconds. That's 35 _milliseconds_, or 35 _thousand_ microseconds. 5 microseconds isn't even a blip there.

So instead of taking down the servers, which [could cause _more_ problems](https://community.ntppool.org/t/status-page-not-working/3907/5), NIST kept them online.

But Jeff said NIST's time is usually about 5,000x more accurate. And if you're one of the universities or aerospace companies that relies on NIST for timing, a 5 μs difference probably _does_ matter.

So they'll be working with those groups directly. But for most people, they'll never even notice.

Jeff finished off the email mentioning the US GPS system failed over successfully to the WWV-Ft. Collins campus. So again, for almost everyone, there was zero issue, and the redundancy designed into the system worked like it's supposed to.

## Time is fragile

{{< figure src="./rack-room-jeff-geerling-timing.jpg" alt="Jeff Geerling studio timing rack" width="700" height="394" class="insert-image" >}}

I was following this closely over the weekend. I have two Raspberry Pi GPS clocks in the studio. One runs my main Stratum 0 NTP server, and the other one I have running as a backup for testing. (Yes I know I should have 4+ going for [good quorum](https://en.wikipedia.org/wiki/Segal%27s_law).)

They both run off my [outdoor GPS antenna](/blog/2025/installing-outdoor-gps-antenna-more-accurate-time), which is distributed in my rack room _and_ in my studio for time research.

Like my studio, _most_ places that need precise time rely on GPS. And that could be a problem!

I'm glad redundancies kept GPS from drifting—I don't know what would happen if GPS time goes away, but it wouldn't be good! But the main takeaway I think is this: _timing infrastructure is fragile_.

CISA identified [a lot of risk in the US's over-dependence on GPS](./AdvisoryMeetings_Roskind_May2023.pdf).

Because of that, the US announced it's trying to [find good alternatives](https://docs.fcc.gov/public/attachments/DOC-410031A1.pdf) for PNT (Position, Navigation, and Timing) earlier this year.

I was actually at a meeting at the NAB where Jeff Sherman, the scientist who wrote the two NIST updates, was talking about BPS. The [Broadcast Positioning System](/blog/2025/bps-gps-alternative-nobodys-heard) would give us redundancy even if GPS was down.

But even _with_ multiple time sources, some places need more. I have two Rubidium atomic clocks in my studio, including the one inside a fancy GPS Disciplined Oscillator (GPSDO). That's good for _holdover_. Even if someone were jamming my signal, or my GPS antenna broke, I could keep my time accurate to nanoseconds for a while, and milliseconds for months. That'd be good enough for _me_.

(If I'm being truthful, it's actually overkill, but I'm in the [time-nut rabbit hole](http://www.leapsecond.com/time-nuts.htm) now—if you know, you know.)

But some places _do_ need nanoseconds, for science experiments, RF, media, or finance. And they might run their own even more precise clocks. But they still trace things back to NIST, at least most do here in the US.

So when NIST's disaster response is tested, everyone's watching.

Last week, when we were microseconds from disaster, the team at NIST fixed it so almost nobody noticed.
