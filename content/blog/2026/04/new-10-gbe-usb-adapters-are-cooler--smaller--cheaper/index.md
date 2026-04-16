---
date: '2026-04-18T09:00:00-05:00'
tags: ['youtube', 'video', '10g', '10gbe', 'ethernet', 'networking', 'homelab', 'wisdpi', 'usb', 'reviews']
title: 'New 10 GbE USB adapters are cooler, smaller, cheaper'
slug: 'new-10-gbe-usb-adapters-cooler-smaller-cheaper'
---
For years, the best way to get 10 gigabit networking on laptops was to buy an expensive, large, and hot 10 GbE Thunderbolt adapter. With new RTL8159-based 10G USB 3.2 adapters coming onto the market, the bulky adapters might be a thing of the past. Just look at the size of the thing in comparison to my Thunderbolt adapters.

{{< figure
  src="./thunderbolt-and-usb-c-10g-ethernet-adapters.jpg"
  alt="10 Gbps Ethernet adapters for Thunderbolt and USB"
  width="700"
  height="auto"
  class="insert-image"
>}}

[2.5G](https://amzn.to/3QIkfFm) and even [5G USB adapters](https://amzn.to/4mytCmZ) have been out for a while, but sometimes you need more bandwidth, and most computers have at least one high-speed USB port.

The 10G adapter I'm testing is [this $80 model from WisdPi](https://www.wisdpi.com/products/usb-c-to-10gb-ethernet-adapter). That's double the price of most 5G/2.5G adapters, but less than half what I paid for my Thunderbolt 10G adapters.

If you _need_ 10 gigs, this might be the best option now. At least if you're using RJ45 and not SFP+. But if you _don't_ need 10 gigs, a 2.5 or 5 gig adapter's still gonna be the best value.

Also, you might not even _get_ 10 gigs with these new adapters, depending on your computer. Why? Well, I'll demonstrate that using my _own_ computers.

This blog post is a lightly edited transcript of today's video, posted below if you'd like to watch instead of read:

<div class="yt-embed">
  TODO.
</div>

## Framework 13 AMD

TODO: SUMMARIZE ALL THE COMPUTERS AND DRIVER SITUATIONS QUICKLY, THEN PRINT A CHART OF ALL THE DATA, FOR COMPARISON. THEN GET TO SUMMARY/CONCLUSIONS.

Starting with my Framework 13, I'm running AMD's Ryzen AI 5 340, which has USB 4 and USB 3.2 Gen 2 ports, the latter of which run at 10 gigabits, so "by 1".

{{< figure
  src="./framework-13-amd-ryzen-ai-5-340-10g-usb-ethernet-test.jpg"
  alt="Framework 13 with AMD Ryzen AI 5 340 running 10G USB Ethernet Test over USB 3.2 Gen 2x1"
  width="700"
  height="auto"
  class="insert-image"
>}}

We'll see how much that affects speeds, but for this test I'm gonna try using Windows 11. Now, Windows 11 comes with a Realtek USB Ethernet driver, but that one's not new enough to work with this 10 gig adapter.

So here I downloaded and installed the driver from Realtek's website. After a minute or two, the interface looks like it's working correctly. It's saying it's 10 gigabits, and I have an IP address, so I'll go ahead and turn off WiFi so I can be sure the laptop's only using this Ethernet connection.

To test the maximum bandwidth I can get in Windows, I'm gonna install iperf3.

One quick tip, if you're on Windows, make sure you're downloading a newer release for high-bandwidth testing. For me, I downloaded it from the [iperf3-win-builds project](https://github.com/ar51an/iperf3-win-builds).

But with that installed, I ran a bunch of speed tests, testing upload, download, and simultaneous upload and download speeds.

It looks like, on the 10 gig USB 3.2 Gen 2 port on my Framework, I can get up to about 7.4 Gigabits one way, or about 9 gigabits bidirectional, which means we're definitely maxing out the USB bandwidth. There's always a little overhead, especially when you're going through USB.

But I wanted to confirm what _USB_ speeds Windows negotiated for the adapter, but Device Manager didn't seem to have any clues, and when I went into the Device settings, it just said "USB 3.0", which I _know_ is a lie, because that would only get a maximum of _five_ gigabits.

## MacBook Neo

Maybe Apple reports on this better in macOS?

To test that, I plugged this thing into my MacBook Neo. And apparently I did it in the wrong port, which macOS reminded me of. So I plugged it into the _other_ port on the Neo, and went into the settings.

I didn't install any driver, but it looks like it was already getting a connection. Of course, the hardware page says it's 2500Base-T, which seems wrong. It correctly identifies as a 10/100/1G/2.5G/5G and 10G LAN adapter, so maybe it's just a display bug?

I fired up iperf3, and got about 6.3 Gigabits. So a little slower than on Windows, but definitely a lot more than 2.5! So Apple probably has a display bug in their Network Settings.

What's better though, is when I tested bidirectional traffic, the MacBook's bandwidth was symmetrical. I got 5.5 gigs up and down at the same time, which was more consistent than on Windows.

And look at this, Apple gives me all the stats I need in System Information, including the negotiated link speed, right there.

## Ryzen Desktop with USB 3.2 Gen 2 20 Gbps

But so far, we haven't gotten the advertised '10 gigs', we've only gotten less than 8. So what gives? Well, before I try out USB 4, I have _one_ computer in here that has a USB 3.2 Gen 2 20 Gigabits port. And yes, I hate USB's naming standards. They're still confusing, no matter how many things they tack on!

But I plugged in the adapter there, found that Windows detected it but wouldn't connect, installed the Realtek driver, and got a connection. Again, it just says "10 gigabits", so let's use iperf3 see what we get.

Ah, _here_ I finally got the full 10 gigabits. Well, 9.5 with a little overhead.

And testing bidirectional traffic, I could get 9.5 up and 5 gigs down for minutes at a time, without any hiccups. It was extremely consistent on this machine.

## M4 MacBook Air

So now I know this thing can perform, at least if you have a 20 gigabits USB 3.2 Gen 2 port at 20 gigs. What about USB 4?

I plugged it into my M4 MacBook Air, which has two of those ports, and yeah... still just getting 6.3 gigs. What gives? USB 4 does _40 gigs_, which is double the 20 gigs on my PC.

Well, the PC is using USB 3.2 Gen 2 2x2 for that 20 gigabits. And Apple's USB 4 controller tunnels USB over Thunderbolt. For anything that's not USB-4-rated, you wind up with only _1_ 10 gig lane, thus with overhead, I can only get around 6-7 gigabits.

So if you wanna get the full potential, make absolutely sure you have a USB 3.2 Gen 2 2x2 20 Gbps port. Which... good luck trying to figure that out without a detailed spec sheet for whatever computer you're using. 'Cuz, Microsoft sure doesn't make it easy.

But even with slower speeds, would this still be a useful upgrade over 2.5 or 5 gig adapters?

## Compared to 5G Ethernet Adapter

Well, I tried out the 5 gig adapter on my Air, and it got 4.6 gigabits. So you're getting about 1.4x faster speed with the 10 gig adapter, even if you don't have the right port.

Is that worth it? Well, considering [the 5 gig adapter is $30](https://www.wisdpi.com/products/wisdpi-usb-3-2-5g-ethernet-adapter-wp-ut5-wired-lan-network-connection-for-mac-os-linux-windows-backward-compatible-on-5g-2-5g-1g-100mbps-ideal-for-gaming), versus [$80 for the 10 gig](https://www.wisdpi.com/products/usb-c-to-10gb-ethernet-adapter)... maybe, maybe not.

And heck, how many of you even have 10 gig capable networks. If you don't have a 10 gig switch and a use case that needs a full 10 gigs of bandwidth, you're better off with 2.5 or 5 gigs. I mean, some of you are probably content with 1 gig, or even WiFi!

## Thermals and Power Draw

To wrap things up, I also checked thermals and power draw. Now, neither of these tests are comprehensive. In fact, measuring the absolute power draw is kinda hard for me because all my power measurement devices downgrade the connection to USB 2, which means I'm not testing it at full performance.

But at USB 2 speeds, this thing uses about .86 Watts of power.

And it doesn't get that hot, which was surprising to me. All my Aquantia-based 10 gig adapters turn into little ovens, and that's a big reason they're so... big. The enclosures are giant heatsinks.

But this one only got up to like 42 degrees celsius after I was running a bidirectional test for a few minutes.

That's warm, for sure, but not so hot that I'd burn myself touching it like I have with some of my other 10 gig adapters.

## Conclusion

And if $80 is too rich, this isn't the only option that uses the new chip; AliExpress is [littered with options now](https://www.aliexpress.us/w/wholesale-realtek-10gbps-usb-nic.html). And you can get it on PCI Express cards too, pretty cheap.

We'll see how long it takes to get to other manufacturers outside of China, but I'm excited to see the price, power, and heat requirements for 10 gig Ethernet getting better.

In the midst of all the inflation in the computing space, it's nice to have something cheaper, faster, and better again.

Until next time, I'm Jeff Geerling.

