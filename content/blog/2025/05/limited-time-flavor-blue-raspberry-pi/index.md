---
nid: 3466
title: "A limited-time flavor: Blue Raspberry Pi"
slug: "limited-time-flavor-blue-raspberry-pi"
date: 2025-05-30T14:08:54+00:00
drupal:
  nid: 3466
  path: /blog/2025/limited-time-flavor-blue-raspberry-pi
  body_format: markdown
  redirects: []
tags:
  - linux
  - raspberry pi
  - sbc
  - video
  - youtube
---

{{< figure src="./blue-raspberry-pi-with-cert.jpeg" alt="Blue Raspberry Pi with certificate" width="700" height="467" class="insert-image" >}}

The most unique Raspberry Pi I own is a limited-time flavor: _blue raspberry_. And no, this isn't the [Brazilian version](https://www.raspberrypi.com/news/raspberry-pi-brazil/), or the [red Chinese version](https://www.raspberrypi.com/news/red-pi-at-night/). This blue version is [one of 1000](https://www.raspberrypi.com/news/blue-pi/) blue Pis that were made to celebrate Raspberry Pi's first anniversary, 12 years ago.

What's crazy is this original Pi (well technically the 2nd revision of the original Pi...)? It's _still supported_. Apple usually [stops supporting their Macs after 5-7 years](https://9to5mac.com/apple-intel-mac-support/). And Microsoft, well, [it's complicated](https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e), but generally you're gonna get 8 to 10 years, if you're lucky and picked the right hardware.

But my goal today is to learn a little more about this blue Pi, and see if I can boot it up with modern Linux, and maybe actually do something useful with a 12 year old computer.

## A Controversial Signature

I found this limited edition Pi via [this Reddit post](https://www.reddit.com/r/raspberry_pi/comments/1kk60jl/limited_edition_blue_raspberry_pis_only_1000_ever/), and bought it from the OP via eBay. You probably won't find too many these days, but I did track down a few:

  - 001: [Jenifire - Pi Forums](https://forums.raspberrypi.com/viewtopic.php?p=2196558#p2196558) (_supposedly_, no proof offered)
  - 041: [RasPi.TV](https://raspi.tv/2014/the-raspberry-pi-family)
  - 080: [James Dawson - blog](https://web.archive.org/web/20221206035941/https://blog.jmdawson.co.uk/the-pi-you-couldnt-buy-blue-pi/)
  - 107: [DJ Beardsall](https://x.com/Beardy/status/1928476140072542328)
  - 433: [Gregory Fenton - youtube](https://www.youtube.com/watch?v=EiCJsz-Jg2k) (also showed certificate from 505, probably a mixup)
  - 732: [eBay - sold in 2025](https://www.ebay.com/itm/187214010703)
  - 878: [eBay - sold in 2025](https://www.ebay.com/itm/187214007645) (this is now mine)
  - 929: [leepspvideo - youtube](https://blog.jmdawson.co.uk/the-pi-you-couldnt-buy-blue-pi/)

Leepspsvideo, in his YouTube video, tried comparing the 'Eben' signature against James' certificate, and said it was inconclusive whether the signature was 'real' (meaning signed in pen, not printed).

The Raspberry Pi blog post said:

> They come with a certificate of authenticity **signed by Eben** and a matching blue case from One Nine Design in Wales

Well, I pulled out my 50mm macro lens and had a close look:

{{< figure src="./eben-upton-signature-halftoning.jpg" alt="Eben Upton halftoning signature on Blue Raspberry Pi" width="700" height="467" class="insert-image" >}}

And that's definitely [halftone print](https://en.wikipedia.org/wiki/Halftone), not pen. Having done some things over 100 times in a row, I know how much of a pain it is. Signing something 1,000 times is also a pain. But I would say, if someone didn't actually sign it, it isn't "signed by"... rather they could say it "has his signature" :)

So we can put that controversy (which is not really much of a controversy, just an interesting aside) to rest.

At the time (2013), RS Components was one of two manufacturers and distributors of Raspberry Pi hardware (the other being Element14). RS Components [stopped manufacturing Raspberry Pis in 2022](https://www.tomshardware.com/news/raspberry-pi-manufacturer-rs-group-ends-license-after-a-decade), after a decade-long partnership.

Anywho... that's a bit of an aside.

## A Blue Pi

This blue Pi happens to be identical to other 'normal' green Raspberry Pi model B Rev 2 boards—it contains 512 MB of RAM, two USB ports, one 10/100 Ethernet port, Composite video out, analog audio out, and _full-size HDMI_!

{{< figure src="./blue-raspberry-pi-power-and-hdmi.jpeg" alt="Blue Raspberry Pi power and HDMI" width="700" height="394" class="insert-image" >}}

It used to be quite easy to plug these things into any old TV or display. Nowadays, I finally bought like 15 micro HDMI to HDMI dongles to help plug my consumer Sony cameras and Raspberry Pis into TVs and monitors. I hate micro HDMI :(

And speaking of 'micro', all Raspberry Pis shipped with a micro _USB_ port for power input until the Pi 4 generation in 2019. These early Pis sipped power, comparatively, and thus, cooling requirements were quite minimal. So much so, early cases barely had anything in the way of cooling/airflow:

{{< figure src="./blue-raspberry-pi-plugged-in.jpeg" alt="Blue Raspberry Pi in blue case" width="700" height="394" class="insert-image" >}}

This is the case that was shipped with the limited edition blue Pi, and it's not _bad_, but it was a bit finicky getting the Pi installed. The quality of third party Pi cases has come a long way since that first million Pi mark was crossed.

The interesting thing is this blue case was made by [One Nine Design](https://www.oneninedesign.co.uk) in Wales, who seems to do product, packaging, and PCB design work, and is located in Pencoed, the same building as the Sony factory where Raspberry Pis are made nowadays.

They haven't posted any updates to their social media accounts since 2020, when they launched the [PiPAD](https://www.raspberrypiplastics.com/pipad), and even the [forum](https://www.raspberrypiplastics.com/forum-1/general-discussions/welcome-to-the-forum) on their raspberrypiplastics website hasn't seen any activity besides a lone post in 2019. So I'm not sure if they're still active, or were absorbed into some other organization.

_Anyway_, that's another little rabbit hole I went down digging into this entire Blue Pi affair.

Getting back to the Pi itself, the back of these limited edition Pis had the serial number etched under where the SD card goes:

{{< figure src="./blue-raspberry-pi-sd-card-slot.jpeg" alt="Blue Raspberry Pi SD Card Slot and number" width="700" height="394" class="insert-image" >}}

And boy, that slot brings back memories. _Many_ original Pis would wind up disused because the SD card slot was ripped off. Those SD cards were _massive_ compared to today's tiny microSD cards, though at the time you could find faster, cheaper, more resilient SD cards, so it was a downgrade both in size and value, in the B+ generation.

Luckily, today there are many reliable microSD cards (I've been running some SanDisk Extremes for years now, with no issue, and [Raspberry Pi even has their own microSD cards](https://www.youtube.com/watch?v=JpDprtmSVtU) now—along with their own SSDs, which work with newer Compute Modules and Pi 5s.

## How does it run?

But I demonstrated modern Pi OS (based on Debian 12) running with a full graphical interface on this old Pi, in today's video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/vBqDCH_Yx4w" frameborder='0' allowfullscreen></iframe></div>
</div>

In summary:

  - Both Chromium and Firefox require newer Pi models to even launch
  - Midori _runs_, but at a snail's pace, even for simpler websites
  - Even launching a settings window is a many-seconds affair, with the old Pi's solitary CPU core maxed out at 100% the entire time
  - Booting into the console is actually quite bearable. The system is slow, still, but responsive.
  - I was able to install [Pi-hole](https://pi-hole.net) without a hitch, and DNS responsiveness was snappy on my network. It probably isn't as good as the Pi 4 I normally have set on this task, but it was fine for my own network.
  - Many libraries are finally dropping 32-bit support, so the number of 'new' applications you can run on older Pi hardware gets a little smaller every year. (e.g. [Unifi Controller](https://github.com/linuxserver-archive/docker-unifi-controller/issues/154)).

Unless you have very modest needs, it is a bit painful running modern software on a Pi this old. But it is _very_ cool that Raspberry Pi still supports 13-year-old hardware. I wish other vendors would do the same.
