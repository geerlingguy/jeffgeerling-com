---
date: '2026-09-18T09:00:00-05:00'
tags: ['ntp', 'clock', 'time', 'vcf', 'midwest', 'retro', 'macs', 'youtube', 'video']
title: "NTP, an atomic clock, and having a great time at the world's largest VCF"
slug: 'vcf-midwest-21-ntp-time'
---
I'm back from [VCF Midwest 21](https://vcfmw.org), arguably the largest vintage computer festival on the planet.

{{< figure
  src="ntp-time-booth-vcf-midwest.jpg"
  alt="Jeff Geerling's NTP Time booth at VCF Midwest 21"
  width="700"
  height="auto"
  class="insert-image"
>}}

After being [blown away](/blog/2025/vcf-midwest-was-even-better-i-expected/) last year, I decided to get a table of my own this year, to demonstrate NTP Time on a bunch of old Macs, representing every era up to the pinnacle of the PowerPC, an Xserve G5 (serving duty as a Stratum 2 `ntpd` server).

Attending as an exhibitor is a _lot_ different. In some ways better (I got to interact face-to-face with at least 200 people—after that I ran out of my 'time tokens'), and in some ways worse (I only got to see about 10% of the exhibits—if that).

But I made this video summarizing my experience:

<div class="yt-embed">
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/oW-Hp8-DAB0' frameborder='0' allowfullscreen></iframe></div>
</div>

## My NTP Time exhibit

{{< figure
  src="jeff-geerling-ntp-time-booth.jpg"
  alt="Jeff Geerling's NTP Time demo table layout"
  width="700"
  height="auto"
  class="insert-image"
>}}

Pictured above is the table layout going into day one of VCF Midwest. I demonstrated NTP Stratum 0, 1, 2, and 3 across three generations of Macs. And I was tracking NTP access on the Xserve G5, which was exposed through a Ubiquiti router to the show's internal network on the domain `time.vcf`, on port 123. As an easter egg, I was also serving [`Time` and `Daytime`](/blog/2026/rfc-867-868-time/) from the TrueTime Pi over the show's network, and local Wi-Fi.

As a _further_ bonus, I was running [`netatalk`](https://netatalk.io) on the Pi inside the TrueTime Pi server on the far left, which includes [Timelord](https://macintoshgarden.org/apps/tardis-and-timelord), an AppleTalk-based time server which is accessible through the companion Tardis Chooser plugin.

I covered a few parts of the setup in previous videos:

  - [Building a mini homelab that fits in my carry-on](/blog/2026/mini-homelab-network-fits-in-carry-on/)\
  This was positioned under the table, and ran the LAN and Wi-Fi for my NTP demo.
  - [Rebuilding a 1995 GPS Time Server](/blog/2026/truetime-xl-gps-time-server-restomod/)\
  This was the 'TrueTime Pi' that ran as a Stratum 0 GNSS reference and Stratum 1 NTP server.
  - [I'm completely out of time](https://www.youtube.com/watch?v=h3RW3bSp9v8)\
  A video going over the Xserve G5 Stratum 2 server setup, as well as a Stratum 3 Mac SE/30 running 'BigMaclock' and an iBook G3 on Mac OS 9.2.

But generally, from right to left:

  1. The TrueTime Pi is receiving time from multiple GNSS satellite constellations through an antenna Meinberg generously donated to ShadyTel. It was positioned about 50m away through the loading dock door.
  2. The Xserve G5 (with a clear acrylic lid to reveal the great industrial design inside) is running Mac OS X 10.3 Server and `ntpd`, serving time as a Stratum 2 NTP server.
  3. The iBook G3 and Mac SE/30 are recieving time using Apple's built-in NTP service (Mac OS 9.2) and the [Network Time](https://macintoshgarden.org/apps/network-time) control panel, respectively. (The SE/30 is also running Tardis, which only set the time once at system startup).
  4. A Maclock and NTP PoE time display showed free-running and close-to-NTP time for comparison with the other two Stratum 3 Macs.
  5. The Mac IIcx on the right side demonstrated the tragedy of the 'battery bomb', as its motherboard, floppy drive, hard drive, and power supply were all completely ruined by an explosive 1/2 AA battery. If you ever find an old Mac, and it hasn't already been battery bombed, rip out the battery immediately—it's only a matter of time!

## A few highlights at VCF Midwest 21

I wasn't the only one having a good time this year; I was told to head over to [Pumping Station One's](https://pumpingstationone.org) table, where not only did they have a clock made out of a 60MB hard drive platter (much larger than a dinner plate!), with the seconds ticking by on the read/write arm[^actuator]... they also had a Cesium Atomic Clock!

Apparently they brought a GPS disciplined clock too, and set the time from it on Friday. There was also a cool multi-mode radio base station, with a custom tuned RF circuit and some cabling that'd fit right in even in the cleanest broadcast facilities.

{{< figure
  src="jeff-geerling-and-stevensons-tektronix-scopes.jpg"
  alt="Jeff Geerling visits the Stevensons' booth with Tektronix oscilloscopes"
  width="700"
  height="auto"
  class="insert-image"
>}}

But back on the topic of time, I found the Stephenses, a father-son duo maintaining a fleet of old Tektronix analog scopes, and one of them had a custom analog clock face with 'VCF MIDWEST' emblazoned on it. I found out about the [AVR Oscilloscope Clock](http://www.dutchtronix.com/ScopeClockH3-1-Enhanced.htm) PCB from Duchtronix, and now I want to dig up an old analog scope and make one myself.

Also on the floor were not one but _two_ WarGames-related projects. There was a custom WOPR you could dial into over the show's phone network, and then [Tattler Solutions](https://tattlersolutions.com) was selling [1U WOPR LED boards](https://tattlersolutions.com/wopr/). One version fits in a 10" rack, and I couldn't resist, so I picked one up (and thanked the maker):

{{< figure
  src="jeff-geerling-tattler-solutions-wopr-1u.jpg"
  alt="Jeff Geerling bought a WOPR board from Tattler Solutions"
  width="700"
  height="auto"
  class="insert-image"
>}}

Speaking of hasty purchases, I also bought a [MacMesh](https://macmesh.xyzzy.computer) to put one of my compact Macs on Meshtastic (it works with MeshCore too). It's a little radio you plug into any old Mac via the modem port. It ships with software to interface with the LoRa radio on System 6 or 7, delivering modern mesh communications to a 1980s Mac!

(I should really stick to the free pile to save some cash next year...)

A rack full of every Xserve Apple made caught my eye, and upon further inquiry, I found out [Mr. Macintosh](https://www.youtube.com/c/MrMacintoshBlog) had a [prototype Apple Network Server 300](https://www.youtube.com/watch?v=tupEO0mrf0c) that was never released. A smaller 5U rackmount version of the behemoth that was the [Apple Network Server](https://everymac.com/systems/apple/network_server/index-network-server.html).

I found a number of folks with projects bridging new hardware and emulation with older tech:

  - danifunker showed off his [Quadra 800 MiSTer FPGA core](https://github.com/danifunker/MacQuadra800_MiSTer) running Prince of Persia in full color on an Analogue Pocket
  - YYZKevin brought his close-to-final versions of the [PicoPCMCIA](https://www.yyzkevin.com/picopcmcia/), which emulates tons of old cards laptops like my PowerBook G3 could run.
  - Ahmad Byagowi brought his now-complete reverse-engineered [10-layer IBM PC110 motherboard](https://github.com/ahmadexp/Open-Source-PC110), a labor of love if I've ever seen one.
  - [dosdude1](https://www.youtube.com/@dosdude1) built [an entire GSM network](https://x.com/dosdude1/status/2097443070333555161) (running on a modern SDR) to allow calling between over a dozen phones from the era of the original iPhone (I tested out a call from an old Nokia and Motorola 'dumb' phone to the iPhone, and the clarity was as good as can be on a crowded show floor!).

I didn't get to see even like 10% of the floor this year for two reasons:

  1. The festival takes the _entire_ Schaumburg Convention Center hall now (all 100,000 square ft), so there are even more tables. 
  2. As an exhibitor and panelist for a Saturday talk, I only had a few minutes to sneak away and see other things outside my immediate vicinity in the back corner!

{{< figure
  src="retro-tech-foundation-apple-garage.jpg"
  alt="Retro Tech Foundation's Apple Garage exhibit"
  width="700"
  height="auto"
  class="insert-image"
>}}

The [Retro Tech Foundation](https://www.retrotechfoundation.org) built a faithful replica of Steve Jobs' garage, during the time where they were producing the first Apple Computer boards. I didn't get into the nitty-gritty but [Ron's Computer Videos did](https://www.youtube.com/watch?v=dy8ZiCCLi0I), it's worth a watch.

## Sharing a good time with everyone

At one point Sunday, a bunch of the folks from Pumping Station One carted over the cesium atomic clock they brought—complete with a drill-battery-to-dc-24v-power-supply-battery-backup—and compared times with my 'TrueTime Pi' GNSS receiver. After a little calibration with a [34-year-old TIC](https://tomverbeure.github.io/2022/12/18/Setting-Up-a-GPIB-Communication-with-a-Racal-Dana-1992-Counter.html), we determined their cesium clock was < 20ns off my GNSS reference.

I couldn't determine accuracy to the Pi's own Linux kernel PPS timestamping capabilities, though, as I wasn't able to get PPS passthrough working like [James Clark's 'Measuring Systematic PPS Bias' blog post](https://satpulse.net/2026/09/06/measuring-systematic-pps-bias-on-the-raspberry-pi-5.html) details. But it was fun nonetheless.

Since we couldn't determine who had _better_ time (we only had two clocks...), we agreed to just have a great time _together_. And that extended out to everyone I met at VCF.

{{< figure
  src="initech-laptop-ntp-time-over-vcf-shadytel-adsl.jpg"
  alt="Initech laptop getting NTP time over ADSL"
  width="700"
  height="auto"
  class="insert-image"
>}}

In fact, I was able to share my NTP time through the Xserve with a number of people:

  - Initech was able to grab NTP time from the Xserve over ShadyTel's internal ADSL network. ([Read more about ShadyTel's VCFMW 21 ADSL2 setup](http://www.dms-100.net/computers/VCFMW/21/network/#adsl))
  - One Meshtastic node (an ESP32-based node) grabbed NTP time on my local Wi-Fi network right after load-in.
  - Two Android users were able to use `telnet` and `nc` to query Time and DayTime services running on the TrueTime Pi.
  - Mr. Macintosh retrieved NTP time from the Xserve over the exhibitor Wi-Fi network (I wish Apple still had a UI button for 'Set time now' like they did in Mac OS 9).

In the end, the Xserve was available at `time.vcf` on port 123 for about 168,000 seconds, or just under 47 hours. Offset and jitter were stable under 100 microseconds, so I'm pretty confident my local setup remained less than 1 ms off UTC, at least on my local LAN. Probably sub-10ms over ADSL, though I'm considering ways to measure and monitor this in the future, with era-appropriate hardware...

{{< figure
  src="ibook-mac-se30-ntp-time-poe-clock.jpg"
  alt="iBook G3 Tangerine and Macintosh SE/30 keeping time with NTP clocks"
  width="700"
  height="auto"
  class="insert-image"
>}}

Not that my Mac SE/30 or iBook G3 would need that much precision—their clocks wandered up to a second or two at times!

Some people see exhibits like my NTP time demo or ShadyTel's POTS, T1, ADSL, and other services and wonder, 'Why?' But I look at things like this and say, 'Why _not_'? I certainly learned a lot about NTP, networking, `chrony`, Apple's history with network time, and GNSS through this project[^learning].

[^actuator]: Technically an _actuator arm_.

[^learning]: Or maybe I'm just making excuses for going further down the rabbit hole of being a [time-nut](http://www.leapsecond.com/time-nuts.htm).
