---
date: '2026-11-17T09:00:00-06:00'
tags: ['ntp', 'ntp pool', 'time', 'video', 'youtube', 'raspberry pi', 'open source']
title: 'I joined the NTP Pool, but not with my Stratum 1 Pi'
slug: 'i-joined-the-ntp-pool'
---
TODO Photo of my clock rack.

Before I get _too_ deep into the [time-nuts](http://www.leapsecond.com/time-nuts.htm) rabbit hole, I figured I should share a little bit of the good time I now have in my studio, with everyone _else_.

Thus, I've finally joined the [NTP Pool](TODO), offering one public Stratum 2 NTP time server ([`ntp-01.jeffgeerling.com`](https://www.ntppool.org/scores/207.244.255.245)), which gets its time from my Straum 1 time server ([`time.jeffgeerling.com`](https://time.jeffgeerling.com)) in the studio.

TODO: Photo of Stratum 1 Pi

My [Time Pi](TODO) is connected to an outside GNSS antenna through a [TimeHAT](TODO), which includes a high quality timing-grade GNSS module, the [u-blox ZED-F9T](https://www.u-blox.com/en/product/zed-f9t-module).

I posted a video about the setup today on YouTube:

<div class="yt-dlp">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/fWXB5u4lXk0' frameborder='0' allowfullscreen></iframe></div>
</div>

I'd encourage anyone else interested in network time to contribute to the NTP Pool. However, there are some things you should know before contributing your own time services:

## Time Commitment

You don't need to go all out with a timing-grade GNSS module like I'm using. Heck, you don't even need GNSS-backed time at all!

The main requirements for hosting a node in the global NTP pool are:

  1. Keeping the system online (servers are only made active in the pool if they're online and serving a decent time over a long period of time)
  2. Maintaining a good time—which can mean Stratum 1 GNSS service, but could also mean pulling time from a few other reliable time servers, and running as Stratum 2 or 3
  3. A stable IP address (IPv4 and/or IPv6), and a long-term commitment

Just 'testing the waters' in the Pool wastes resources—when you bring a new server online, it will take at least a few hours just to spin up all the tests to verify the server's providing a good time.

If you just want to operate your own time server, that's fine; the NTP Pool is a shared global resource, so joining it is a _little_ more of a commitment.

Two other important caveats:

  1. Your NTP server's IP address will be public
  2. NTP traffic will slowly decay, and some misconfigured systems could take months or even _years_ before they'll stop sending NTP traffic at your IP

The first caveat matters a lot to me: back when I exposed my home IP address trying to self-host this website on a cluster of Raspberry Pis, [some doofus decided to DDoS my website](/blog/2022/three-ddos-attacks-on-my-personal-website/)—and was persistently doing so for the better part of a month.

I had to [cycle my home IP](/blog/2022/getting-new-ip-address-dhcp-spectrum-internet/), then put my site behind Cloudflare, just to protect my poor Pis (and eventually the VPS I now host it on).

## Secure and Measurable Time

For those reasons, I chose to have two layers to my public time services:

  - **Stratum 1**: I have my Time Pi running in the studio, running a WireGuard tunnel to:
  - **Stratum 2**: A VPS I host with a cloud provider in St. Louis, to keep the latency down (ideally with fewer hops across the Internet, which leads to better time sync via NTP)

I include the Stratum 2 time server in my Stratum 1 time server's `chrony` config as a `noselect` refclock, so I can easily compare the Internet delay between the two servers, outside the WireGuard tunnel:

```
server ntp-01.jeffgeerling.com noselect
```

This provides me with the following graph:

TODO: ntp-server-comparison-graph.png

I've been tracking my time in comparison to an NTP time server hosted at WWV in Ft. Collins, CO, as well as one of NIST's NTP servers in Boulder, CO.

For typical NTP configurations, you shouldn't single out time servers like this; I'm only doing it for long-term measurement (and I only poll the servers every 1024 seconds). Most systems should use pool addresses, [as documented here](https://www.ntppool.org/en/use.html).

The line for Cloudflare steps up and down sometimes, most likely due to BGP routing: as routes and servers change, packets between St. Louis and `time.cloudflare.com` can take very different paths there and back.

> Note: You might be looking for info on NTS, or [Network Time Security](https://developers.cloudflare.com/time-services/nts/)—I haven't explored it much, so expect more on that at a later time. Currently the NTP Pool doesn't support NTS, though [some have experimented with it](https://community.ntppool.org/t/nts-pool-experiments/4147/29). I'm okay with basic NTP and would recommend anyone with critical timing needs to use other time sources as well (don't _only_ rely on NTP!).

## Chrony and GPS time tweaks

My Time Pi is not only serving as a Stratum 1 timing reference for my public NTP server, it's also my primary reference for local time in the studio.

TODO: Photo of TimeHAT closer.

The TimeHAT on top does most of the heavy lifting, with it's built-in Intel i226 NIC (with hardware timestamping, essential for accurate PTP timing on the LAN) and a timing-grade GNSS module.

The entire configuration (for both servers) is managed by Ansible in my [time-pi](https://github.com/geerlingguy/time-pi) project.

Using the i226, I'm able to discipline the NIC's hardware clock (called the 'PHC', or 'PTP Hardware Clock') _in hardware_, directly from the GPS module's PPS (Pulse Per Second) pin. Using Linux's `ts2phc` tool, I can discipline the PHC to within tens-of-ns of UTC, and distribute that time to other PTP-aware computers on the LAN.

The time on the PHC is shared to my Pi's system clock using `refclock PHC` inside Chrony, instead of `phc2sys`, because I was experiencing a weird 200ms jump every so often. Chrony then disciplines the quartz oscillator on the Pi itself, but this can only be accurate to within a microsecond or less, because the pulse goes through the Linux kernel, and adds a little latency.

> I'm actually trying to make this latency more measurable, since GPIO is routed through the RP1 chip deterministically. See [ahmadexp's rp1-ptp-pps utility PR](https://github.com/raspberrypi/utils/pull/214). [PTM](https://pcisig.com/PCIExpress/ECN/Base/PrecisionTimeMeasurement_1.0a) could reduce the error between the NIC's PHC and the system clock to a few ns, but the BCM2712 SoC on the Pi doesn't support it.

One other quirk I ran into was Debian's default `sourcedir /run/chrony-dhcp` directive, which was picking up another NTP server via DHCP, causing `chrony` to stampede my _extremely_ accurate GNSS-derived time from `phc2sys` with a far-less-accurate time from a public NTP server! (This was another motivation behind moving clock steering to `chrony` instead of `phc2sys`.)

## Time for an Outage

I'm hosting my public Stratum 2 server with [Oxtrys](https://www.oxtrys.com), a VPS provider I'd never used before—and one thing I was nervous about was how they'd react to a VPS handling only UDP packets like this.

Some automated firewalls shut down public NTP servers because they can _look_ like abuse vectors. I wondered if that was the case late on the night November 16, as I was _writing this blog post_:

TODO: ntp-01-server-offline-pool-score.png

I tried SSH'ing to the server, and found it inaccessible.

TODO: I emailed oxtrys support... todo todo

## Conclusion

I've certainly learned a lot, every stage of this journey: NTP is loaded with utility, and is currently an essential piece of global timing infrastructure. I think I know about 1% (probably less) of what there is to know about hosting a public NTP server, and hopefully I can share more as I increase that to a few more percentage points!

I'm thankful to all the other NTP Pool operators, as well as all the timelords who built and manage massive NTP endpoints like `time.apple.com`, `time.cloudflare.com`, etc.
