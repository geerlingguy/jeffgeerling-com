---
nid: 73
title: "WiFi for a Small Tech Conference/Meetup"
slug: "wifi-a-small-tech"
date: 2012-08-15T21:39:29+00:00
drupal:
  nid: 73
  path: /articles/computing/2012/wifi-a-small-tech
  body_format: full_html
  redirects:
    - /computing/2012/wifi-a-small-tech
aliases:
  - /computing/2012/wifi-a-small-tech
   - /articles/computing/2012/wifi-a-small-tech
tags:
  - events
  - networking
  - wifi
---

<p style="text-align: center;">{{< figure src="./routers-200-users-airport.jpg" alt="WiFi Routers - AirPort Extreme and AirPort Express" width="325" height="142" class="blog-image" >}}</p>

WiFi is awesome for homes and small businesses. Stick a router in a closet somewhere near where you have a cable modem or DSL router, and—boom!—easy Internet and Network access for all 5-10 people/devices within the building.

But, try bringing this setup to a small conference or a meeting of 25+ (or 200+) computer-using people, and you're in for a world of hurt. Some people will get slower-than-dialup access, some people won't be able to connect at all, and others will have strange issues that never happen when you're just using the network by yourself.

<h3>The problem(s)</h3>

There are many problems that cause WiFi to fail in any setting with more than a few people/devices:

<ol>
	<li>Most people actually have more than one device, and many will connect multiple devices to your network (figure 2-2.5 devices per person—laptop, iPad, and mobile phone).</li>
	<li>Most WiFi routers aren't made to support more than 5-10 concurrent devices, especially not with an encrypted connection (you <em>are</em> using WPA encryption, right?).</li>
	<li>6 Mbps bandwidth might be fine for one or two people at a time, but when 20+ people have Twitter, email, YouTube, Google Docs, and a hundred other sites and services running, that bandwidth is gone <em>fast</em>.</li>
	<li>The physics of wireless signals (especially in the saturated 2.4 Ghz range) cause a lot of problems when many devices are trying to communicate on the same channel and on the same access point (or even on the same channel on different access points).</li>
	<li>Wireless networking was never built with 1,000+ gatherings in mind, much less 100+.</li>
</ol>

However, all these problems can be overcome... and for gatherings where you have less than a few hundred devices (100-200 people), it's usually not rocket science getting reliable and fast WiFi going for everyone.

<h3>Solution: Planning and Equipment</h3>

<strong>A good connection:</strong> You should try to have at least 200 kbps of data (up and down, if at all possible) for each user—meaning if you have 100 users, you should get a reliable connection with at least 20 mbps bandwidth up and down. More is better, and less will make people very impatient.

<p style="text-align: center;">{{< figure src="./airport-express-table.jpg" alt="Airport Express on table" width="500" height="326" class="blog-image" >}}</p>

<strong>A good router and good access points:</strong> If you have fewer than 250 users, a single good router (like the <a href="http://www.amazon.com/Airport-Extreme-802-11N-5TH-GEN/dp/B0057AVXJA/ref=sr_1_1?ie=UTF8&amp;creative=390957&amp;creativeASIN=B0000AZK4G&amp;linkCode=as2&amp;tag=mmjjg-20">Airport Extreme</a>) can handle the routing of up to that many IP addresses, and can connect to three additional <a href="http://www.amazon.com/gp/product/B008ALA2RC/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B008ALA2RC&amp;linkCode=as2&amp;tag=mmjjg-20">AirPort Expresses</a> configured as access points (<a href="http://superuser.com/a/361228/80658">turn off their DHCP services and set them in 'bridge' mode</a>). If you keep them spread out, and set each access point (and the router) to a separate channel (try to keep at least 2-3 channels difference for contiguous access points), you could serve about 200 simultaneous devices—but not more.

<strong>Wired infrastructure:</strong> Make sure you have enough Cat5 (or Cat5e) shielded network cable to run to each access point from the central wired router. A <a href="http://www.amazon.com/gp/product/B000067RWR/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B000067RWR&amp;linkCode=as2&amp;tag=mmjjg-20">500ft box</a> should be enough for most events, if you want to make your own cables (just buy the <a href="http://www.amazon.com/gp/product/B000067RWR/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B000067RWR&amp;linkCode=as2&amp;tag=mmjjg-20">cable</a>, a bunch of <a href="http://www.amazon.com/gp/product/B000I20AJ6/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B000I20AJ6&amp;linkCode=as2&amp;tag=mmjjg-20">RJ-45 connectors</a>, and a <a href="http://www.amazon.com/gp/product/B0000AZK4G/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B0000AZK4G&amp;linkCode=as2&amp;tag=mmjjg-20">crimp tool</a>—it'll save you a bit of money to make the cables yourself). Also, make sure no single Ethernet cable exceeds 300' in length (otherwise, you could have flaky network connections between routers).

<strong>A good plan for locations:</strong> Try to space the routers about 50' from each other (at least), and don't set them to their highest power setting. If you're in a large room, try to put the routers a little lower than head height so they'll saturate enough of the crowd to cover the middle of the room, but not interfere with each other much. Alternatively, if you have to have all routers in the back of the room, put them above head height so they can get to the far side of the room. (Be ready to move the routers during the conference if you encounter dead spots—this is kind of an art!)

<strong>Important notes:</strong>

<ul>
	<li>Even the best plans fail.</li>
	<li>People don't distribute themselves evenly... meaning you could have one access point with 100 people trying to connect, and another access point with only 10 users. Can you guess which access point will have trouble? Try to get people to spread out and not crowd the front (or back) of a room.</li>
	<li>If you're not using professional equipment, and didn't hire a company to build your WiFi and bandwidth for your event, don't expect 100% reliability. Consumer-level equipment fails, so either have backups of everything, or accept that you're flying by the seat of your pants. If everything goes off without a hitch, that was just good luck :)</li>
	<li>Since most consumer-level routers only serve about 255 IP addresses total, and don't have very configurable routing/subnet options, ~250 devices is the maximum you'll ever be able to get on one network without knowing a lot about networking. If you want to go beyond 250 devices, you should either hire someone else to build your network, or start reading up on networking and expanding your budget a little.</li>
</ul>

<h3>Solution: Testing and Fixing</h3>

Before the conference, make sure your router and all your access points are working, make sure you can connect to each one individually, and make sure they're all getting Internet access. Then put them in their final locations, run the cabling to them, tape the cables down securely with <a href="http://www.amazon.com/gp/product/B000QDRRIE/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B000QDRRIE&amp;linkCode=as2&amp;tag=mmjjg-20">gaffer's tape</a>, and walk around, testing the signal strength throughout the room(s).

If the signal's good (80%+) everywhere, you're set for the beginning of the conference... but once the conference starts, have some people in the place report to you from various locations how their connection is holding up, and have them run something like <a href="http://speedtest.net/">Speedtest</a> and see what kind of bandwidth they're getting.

But, if there are problems, you may need to move one of the access points, or raise it up higher, or lower it... testing is key, and you'll never know exactly how your setup performs until many bodies are in the room, blocking and redirecting the signals. Be flexible, and make sure you have someone in charge of the network who knows at least a little bit about what he's doing.

<h3>Critical problems</h3>

It won't always come out roses; if there are problems with the network, there are a few things you can do:

<ol>
	<li><strong>Hire a company to come in and build your network</strong>—professional event WiFi companies can do a much better job than you or I since they have a ton of experience. Heck, if you have the budget, why not hire them to plan and build your conference network from the get-go? Saves you a lot of headache...</li>
	<li><strong>Ask attendees to be kind and only connect one device</strong> (or none, if they're not actively using them) to the network. Most people at tech events are sympathetic to the extreme frustration of slow Internet that others experience, and they'll at least switch their iPhones from WiFi to 3G :)</li>
	<li><strong>Power-cycle everything.</strong> Turn off the main router and the base stations; this will disconnect everyone, and then when they reconnect, their devices may reconnect to a different router, giving them better signal.</li>
	<li><strong>Get more bandwidth.</strong> If everyone can connect, but things seem really, really slow, make sure you (a) have good access points with dual-band radios that serve 802.11n on a separate frequency (5Ghz) from 802.11g/b (2.4Ghz), and (b) you have enough RAW bandwidth to serve all the clients. You might also want to try to get people to turn off torrent downloading and any kind of video or audio streaming services (or block those services outright).</li>
</ol>
