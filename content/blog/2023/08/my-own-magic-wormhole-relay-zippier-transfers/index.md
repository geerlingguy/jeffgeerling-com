---
nid: 3304
title: "My own magic-wormhole relay, for zippier transfers"
slug: "my-own-magic-wormhole-relay-zippier-transfers"
date: 2023-08-19T02:55:02+00:00
drupal:
  nid: 3304
  path: /blog/2023/my-own-magic-wormhole-relay-zippier-transfers
  body_format: markdown
  redirects:
    - /blog/2023/my-own-magic-wormhole-relay-zippy-gigabit-transfers
aliases:
  - /blog/2023/my-own-magic-wormhole-relay-zippy-gigabit-transfers
tags:
  - fiber
  - files
  - ftp
  - internet
  - magic-wormhole
  - open source
  - rsync
  - sftp
  - ssh
  - tor
---

If you've ever had to transfer a file from one computer to another over the Internet, with minimal fuss, there are a few options. You could use `scp` or `rsync` if you have SSH access. You could use [Firefox Send](https://support.mozilla.org/en-US/kb/send-files-anyone-securely-firefox-send), or Dropbox, or iCloud Drive, or Google Drive, and upload from one computer, and download on the other.

But what if you just want to zap a file from point A to point B? Or what if—like me—you want to see how fast you can get an individual file from one place to another over the public Internet?

{{< figure src="./rsync-40-mbps-p2p.jpg" alt="rsync 40 MB/second" width="700" height="394" class="insert-image" >}}

I first attempted to do this over SSH using `scp` and `rsync`, but for some reason (even though both computers could get 940 Mbps up and down to speedtest or Cloudflare), that maxed out around 312 Mbps (about 39 MB/s). I even [tunneled `iperf3` through SSH](/blog/2023/testing-iperf-through-ssh-tunnel) and could only get a maximum around 400 Mbps. I'm not sure if it was something on the ISP level (either Bell Canada or AT&T throttling non-HTTP traffic?), but the CPU on both machines was only hitting 10-13% max, so I don't think it was an inherent limitation of SSH encryption.

> Why should I care about getting speeds greater than 300 Mbps for single-file transfers? That question will be answered soon ;)

Short of running an open FTP server, or Samba over the Internet, my next favorite option is [magic-wormhole](https://github.com/magic-wormhole/magic-wormhole-transit-relay).

If you've never used it, it truly is _magic_:

```
# On both computers:
[apt|dnf|snap|brew|choco] install magic-wormhole

# On the source computer:
wormhole send file-a

# On the recipient computer:
wormhole receive [paste phrase generated on source computer here]
```

It's worked great for years, and yes—it does rely on a public relay to send data from computer to computer, so you have to trust the relay (and the encryption). There are [Known Vulnerabilities](https://magic-wormhole.readthedocs.io/en/latest/attacks.html), so I wouldn't think about sending over state secrets... but for most other types of data, I'm not worried. I just want to send a file to another computer.

## The Problem

{{< figure src="./magic-wormhole-42mb-per-second.jpg" alt="Magic wormhole 42 MB/second" width="700" height="323" class="insert-image" >}}

But magic wormhole was _also_ only giving me speeds around 42 MB/s, only a slight improvement over SSH-based transfer. And that speed wasn't stable—it would fluctuate, presumably as others were using the public relay.

Wormhole _can_ do direct encrypted P2P transfers, but that requires fairly open networks between the machines (NAT and such can make this very tricky to pull off). So usually it falls back to the public relay.

So I thought... I wonder if I could run my _own_ relay, on a faster, dedicated server, and use _that_? Well, it turns out, you can! Enter [magic-wormhole-transit-relay](https://github.com/magic-wormhole/magic-wormhole-transit-relay).

## Setting up my own transit-relay server

The documentation was a tiny bit sparse for someone unfamiliar with Python's [Twisted](https://pypi.org/project/Twisted/) library, so I [submitted a PR](https://github.com/geerlingguy/magic-wormhole-transit-relay/pull/1) to remedy that.

Basically, you need a machine that can handle whatever link speeds you need (in my case, I was hoping for symmetric 1 Gbps up and down over a public IP), and I chose to run a DigitalOcean Droplet—a 4GB Basic droplet—with Ubuntu 22.04.

Once it was up, I ran a `dist-upgrade`, rebooted, then:

```
# Install Python 3 pip and twist
apt install python3-pip python3-twisted

# Install magic-wormhole-transit-relay
pip3 install magic-wormhole-transit-relay

# Run transit-relay in the background
twistd3 transitrelay

# Check on logs
cat twistd.log  # or `tail -f twistd.log`

# (Once finished) kill transit-relay
kill `cat twistd.pid`
```

So I ran it, and instead of just `wormhole send file-a`, I specified my custom transit-relay server:

```
wormhole send --transit-helper=tcp:[server public ip here]:4001 file-a
```

I copied the receive command, pasted it on the destination server, and got... about 50 MB/s. It would jump up to 60-70 MB/sec for a minute, then slow back down to 50, and kept going back and forth. _Better_, but not amazingly stable, and still far from a full gigabit (about 110 MB/s). I really wanted to max out my gigabit connection!

Using `iftop`, I could see the Droplet seemed to equalize the send and receive over the public interface, both around 500-600 Mbps.

DigitalOcean says the maximum throughput on a standard Droplet is "up to 2 Gbps", but maybe they try to limit the public interface to 1 Gbps total? Not sure.

## Going Faster

Next I spun up an 8 GB CPU-optimized 'premium' droplet, since this class is reported to have 10 Gbps connections, and I set up transit-relay on _it_.

This time, my transfer stabilized at 75 MB/sec (about 600 Mbps) and stayed there. Not an amazing speed improvement, but at least it was stable! I'm wondering now if there's any way to direct transfer a file, encrypted, between two consumer Internet connections at a full gigabit short of proxying it through HTTP!

{{< figure src="./bgw320-att-internet-gateway-fiber.jpg" alt="BGW320 AT&amp;amp;T Internet Gateway - Fiber" width="700" height="518" class="insert-image" >}}

Maybe it's just Bell/AT&T, or something in the router on one end or another. I wish I didn't have to use the AT&T-provided Fiber router, because I don't have a lot of insight into what it's doing. My own router was not having any trouble, and could've put through the full gigabit easily.

I'd love to hear what other people do for direct gigabit+ file transfer from one location to another (outside of data centers, where the connections and configuration are reliable and fast as a rule!). In the end, I have learned a good deal about magic-wormhole, and about testing consumer-to-consumer ISP connections—and there's always much more to do!

> Edit: Many have recommended [`croc`](https://github.com/schollz/croc), which seems to be very similar to `wormhole`, but written in Go instead of Python. I have tried it a few times with files varying from 5-10 GB, and sometimes it seems to settle in around 54 MB/second:
>
> ```
> Sending (->1.2.3.4:49860)
> chuck.MP4 100% |████████████████████| (7.7/7.7 GB, 54 MB/s)
> ```
>
> Other times it can saturate my gigabit connection using compression:
>
> ```
> chuck.MP4 100% |████████████████████| (7.7/7.7 GB, 107 MB/s)   
> ```
>
> But if I use `--no-compress`, I end up getting very spiky behavior at least over public relay (Getting between 15-30 MB/sec over long term average.)
>
> You can skip the lengthy default hash algorithm and use [imohash](https://github.com/kalafut/imohash) (`croc send --hash imohash`) if you're working on massive files like I am.
>
> Definitely something to consider trying, though! Running your own relay seems like it may be a little easier, too (`croc relay`), but I was having some trouble with the sender quitting once I tried using my own relay.
