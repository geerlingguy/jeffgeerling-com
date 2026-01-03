---
nid: 2476
title: "2013 MacBook Air WiFi Problems (high latency, dropped connections) [Updated]"
slug: "2013-macbook-air-wifi-problems"
date: 2014-01-10T20:11:08+00:00
drupal:
  nid: 2476
  path: /blogs/jeff-geerling/2013-macbook-air-wifi-problems
  body_format: full_html
  redirects: []
tags:
  - 802.11g
  - 802.11n
  - apple
  - bluetooth
  - interference
  - mac
  - macbook air
  - wifi
---

<blockquote><strong>Update (3/4/14)</strong>: Mac OS X 10.9.2 seems to fix at least the latency issue—and possibly dropped connections as well, at least for most users I've spoken with... We'll see!</blockquote>

<blockquote><strong>Update 2 (11/25/14)</strong>: If you're having trouble with iOS 8 and/or Yosemite, it could be related to AirDrop services over WiFi. Please see <a href="https://medium.com/@mariociabarra/wifried-ios-8-wifi-performance-issues-3029a164ce94">WiFried: iOS 8 WiFi Issue</a></blockquote>

<p>For the past few months, I've been battling my 2013 11" MacBook Air's WiFi problems. I've taken the MacBook to the Genius Bar twice, and have attempted dozens of fixes. Judging by the number of individuals who have posted to <a href="https://discussions.apple.com/thread/5100655">this thread</a> on Apple's Support Communities forum, among many other similar threads, I'm not the only MacBook Air owner suffering from WiFi issues like high latency, slow throughput, connection dropouts, and other random problems.</p>

<p>Here are some of the symptoms I and others have encountered:</p>

<ul>
<li>
<strong>Terrible latency</strong>: while sitting in one location, the Air might have ping times ranging from 30-4000ms, with many dropped packets. This makes things like connecting to a remote server (either with SSH or via VNC or RDC) a painful experience, and causes some applications (like streaming video or VPN connections) to drop and reload, also contributing to the pain.</li>
<li>
<strong>Dropped packets</strong>: sometimes, when loading a web page, part of the page will load, then the connection seemingly drops for 5-30 seconds, then finally, the rest of the page loads. It's almost worse than being connected to a 56kbps dial-up modem!</li>
<li>
<strong>Unstable throughput</strong>: When using a bandwidth-measuring tool like <a href="http://www.speedtest.net/">SpeedTest.net</a>, bandwidth on a very stable connection can vary between 5-40 Mbps (while another Mac or PC sitting right next to the Air reliably gets 40 Mbps).</li>
<li>
<strong>Dropped Network Connections</strong>: Sometimes, WiFi signals can simply drop off for no reason, even if the connection seems very strong (full bars in the menubar, and RSSI &gt; -50).</li>
</ul><p>I've done literally hundreds of tests to diagnose, reproduce, and (in some situations) solve these problems, and I'll recount some of these things here, for the benefit of the many others having these issues, and possibly for an Apple engineer tasked with fixing the issues.</p>

These two graphics below show some of the investigation I've done (using <code>ping</code> and Apple's Wireless Diagnostics tool:

<p style="text-align: center;">{{< figure src="./bluetooth-chrome-g-network-wifi.jpg" alt="Bluetooth affecting Google Chrome WiFi Connectivity" width="575" height="277" >}}
This graph shows signal strength over time, with Bluetooth enabled (but not paired with anything), on a 2.4 Ghz 802.11g network.</p>

<p style="text-align: center;">{{< figure src="./google-standard-ping-2.jpg" alt="Gogle varying latency ping times on AirPort 802.11g network" width="450" height="373" >}}
This graph shows the latency for a 1 second ping to google.com—and this was one of the best runs—while connected to an 802.11g network with Bluetooth enabled. If I DoS my router, this evens out to around 31ms.</p>

<p>Also, as a point of reference, I had my wife's 2011 13" MacBook Air and an old Dell Latitude laptop next to me for almost all these tests—they never showed any drop in performance (throughput, latency, or connectivity)—not once. So I can guarantee it's not the network that's having trouble.</p>

<h2>
<a name="theories" class="anchor" href="#theories"><span class="octicon octicon-link"></span></a>Theories</h2>

<p>After trying many of the 'fixes' below, my best bet is that this issue is related to the power management Apple is using in Mavericks (or possibly in the driver used for the AirPort card). Additionally, antenna location may be a contributing factor, since disabling or changing the way Bluetooth works can have an affect on signal strength.</p>

<p>It seems to me that the WiFi driver and/or Mavericks' power-saving features might be too aggressive—it seems the WiFi chip is put into some low-power state if it doesn't have constant activity (like a ping every 1/5th of a second), and this is causing signal strength and stability issues.</p>

<p>Also, perhaps the WiFi antenna(s?) is too close, or oriented poorly, in comparison to the Bluetooth antennna(s?). Disabling Bluetooth often leads to a more stable connection, and some Bluetooth applications (like Knock, which keeps a constant low-power connection to an iPhone) can practically disable WiFi.</p>

<p>Finally, these are the three major reasons I <strong>know</strong> there is a problem with WiFi/AirPort in my 2013 MacBook Air running Mavericks, and it's not just my imagination:</p>

<ol>
<li>I have tried using an external USB WiFi adapter, and never had any of the issues I have with built-in WiFi.</li>
<li>I have tried using Apple's USB wired Ethernet adapter, and never had any of the issues I have with built-in WiFi.</li>
<li>I have done all these tests while sitting next to a 2011 MacBook Air and a 2010-era Dell Latitude, and neither laptops ever experienced any drop in bandwidth or latency.</li>
</ol><p>Now, on to the fixes...</p>

<h2>
<a name="band-aid-fix-1-dos-a-router-to-keep-the-connection-stable" class="anchor" href="#band-aid-fix-1-dos-a-router-to-keep-the-connection-stable"><span class="octicon octicon-link"></span></a>Band-aid fix #1: DoS a router to keep the connection stable</h2>

<p>The most telling fix I found, and the reason I think this entire problem could be power-management-related, is that, by simply pinging some external address at least 5 times per second (every 0.2 seconds), latency goes from wildly random (anywhere from &lt;1ms to 1,000+ms), to extremely stable (a ping to my router stablized at ~0.3ms, and a ping to <a href="http://www.google.com">www.google.com</a> stabilized at ~31ms, at least on my home network).</p>

<p>To test if this fixes the latency problem for you, open up Terminal (inside Applications &gt; Utilities), and enter the following command:</p>


```
ping -i 0.2 [your router IP address]
```

<p>Your router IP address can be found by going to the Network preference pane, clicking on WiFi, then clicking the Advanced... button, and then clicking on the TCP/IP tab.</p>

<p>Open a separate Terminal window and type in <code>ping www.google.com</code> (this will ping Google's server every second). It should be a stable amount of latency for each ping (the last value in the line). If you go back to your first window and type in Control-C (to exit the ping utility), then see if the latency times for your Google ping start varying again.</p>

<p>This fix could work for a home network, maybe, but definitely not in a corporate environment—you're effectively sending tons of junk traffic at the router, for no good reason (except to tell your Mac's AirPort card to stay in some higher-power state).</p>

<h2>Band-aid fix #1-a: Do something else that saturates your wireless connection</h2>

Another way to keep the latency low is to use your Mac with an Apple TV and mirror your display (this will keep a constant, high-bandwidth connection to your Apple TV, keeping the wireless interface happy), or to download giant files (like when you run a Speedtest.net speed test)—both of these activities keep your wireless card in a normal/on state, and make it work like it should.

<h2>
<a name="band-aid-fix-2-switch-your-router-to-80211n--5ghz-only" class="anchor" href="#band-aid-fix-2-switch-your-router-to-80211n--5ghz-only"><span class="octicon octicon-link"></span></a>Band-aid fix #2: Switch your router to 802.11n / 5 Ghz-only</h2>

<p>One solution which is amenable at home (but impossible at work, because I have no control over my employer's access points or purchasing decisions) is to upgrade the WiFi network to 802.11n-only (or 802.11ac, if you have a fancy—and expensive—new ac-enabled router) on the 5 Ghz band.</p>

<p>I have a few older devices at my house that only work on 802.11g, so I was fortunate to have an extra g-only WiFI router sitting around; I now use my AirPort Express as an 802.11n-only 5 Ghz router, and set the old router to 802.11g-only on the 2.4 Ghz band.</p>

<p>As long as I set my MacBook Air to only use the 802.11n network, I have good throughput, and low latency. However, this comes with a major downside; WiFi range is reduced dramatically, and I can only get about 40-50' away from the router before the connection drops (or gets very slow). On the 802.11g network, I can get up to 80-90' away before the connection drops (meaning I'm covered in every corner of my house).</p>

<p>I'm considering buying an <a href="http://www.amazon.com/dp/B00DB9WCR6/?tag=mmjjg-20">AirPort Extreme</a> and then having it in one part of the house, and my existing Express in another part, but that's a fairly expensive fix for this problem!</p>

<h2>
<a name="band-aid-fix-2-disable-most-bluetooth-accessoriesapplications" class="anchor" href="#band-aid-fix-2-disable-most-bluetooth-accessoriesapplications"><span class="octicon octicon-link"></span></a>Band-aid fix #2: Disable most Bluetooth accessories/applications</h2>

<p>At work, my desk seems to be close to one of the 802.11g-only routers, so the signal strength is usually great (at least, as it is reported by the MacBook Air!). However, I found that certain Bluetooth-enabled applications caused the WiFi to be excruciatingly slow.</p>

<p>One app, in particular, that caused this issue was <a href="http://www.knocktounlock.com/">Knock</a>, an app that keeps a constant, low-power connection to your phone so you can tap it twice to unlock your Mac. With the app running and connected to my iPhone, download bandwidth over WiFi went down to ~0.8 Mbps on a network that usually gets 15-20 Mbps. If I quit the app, the bandwidth went up to 6-8 Mbps.</p>

<p>Sadly, due to this behavior, I have had to stop using Knock. It was a handy convenience app, but alas, it is not for me :(</p>

<h2>
<a name="band-aid-fix-3-disable-bluetooth-entirely" class="anchor" href="#band-aid-fix-3-disable-bluetooth-entirely"><span class="octicon octicon-link"></span></a>Band-aid fix #3: Disable Bluetooth entirely</h2>

<p>Some people have reported that disabling Bluetooth entirely fixed their problems. Unfortunately, that's not an option for me; I would take a slower internet connection over not being able to use my <a href="http://www.amazon.com/dp/B002TLTGM6/?tag=mmjjg-20">Magic Mouse</a>. Also, I sometimes use an external Bluetooth keyboard, or some other Bluetooth accessory, and that convenience is worth a ding in my Internet speed (sadly... because usually, with Apple products, I can have it all).</p>

<p>With Bluetooth disabled, my connection does seem to be perfectly stable, though it's usually stable even if I just have my mouse paired with my Air. I'm not sure why Knock's pairing with my iPhone harms the connection more than a mouse (which is constantly sending tracking feedback wirelessly), but that's how it is, at least in my testing, so I guess I'm glad the mouse works better than Knock.</p>

<h2>
<a name="things-that-dont-work" class="anchor" href="#things-that-dont-work"><span class="octicon octicon-link"></span></a>Things that <em>don't</em> work</h2>

<p>I also tried a bunch of other things that had no effect whatsoever, but seemed promising:</p>

<ul>
<li>Deleted all WiFi networks in System Preferences, then added them back in.</li>
<li>Disabled Power Nap (in the Energy Saver preference pane).</li>
<li>Tried using an AirPort Express in mixed mode (b/g/n - 5 Ghz + 2.4 Ghz); in this case, the Air seemed to prefer using 2.4 Ghz connections because that signal was usually stronger.</li>
<li>Tried using a Netgear WRT54G router (b/g - 2.4 Ghz).</li>
<li>Completely erased hard drive and did a fresh reinstall of Mavericks. Didn't help at all.</li>
<li>Had the Genius Bar completely replace the AirPort card with a new one. Didn't help at all.</li>
</ul><h2>
<a name="troubleshooting-tools" class="anchor" href="#troubleshooting-tools"><span class="octicon octicon-link"></span></a>Troubleshooting tools</h2>

<p>In troubleshooting these problems, I've found the following tools and methods to be the most helpful:</p>

<ol>
<li>
<code>ping</code> in the terminal.</li>
<li>Hold down the option key while clicking on the AirPort menu—this way you can see what frequency WiFi is using, as well as the channel and <a href="http://en.wikipedia.org/wiki/Received_signal_strength_indication">RSSI</a> for your connection (often useful for troubleshooting).</li>
<li>
<a href="http://support.apple.com/kb/HT5606">Apple's Wireless Diagnostics</a> (option-click the AirPort menu, then select "Open Wireless Diagnostics...", type in your admin password, and click View &gt; "Hide Utilities Toolbar", then show it again, to open up the WiFi Performance graph).</li>
<li>
<a href="http://istumbler.net/">iStumbler</a> helps identify all the WiFi signals your computer can see, in excruciating detail.</li>
</ol><h2>
<a name="summary-and-non-conclusion" class="anchor" href="#summary-and-non-conclusion"><span class="octicon octicon-link"></span></a>Summary and non-Conclusion</h2>

<p>I'm still (as of early 2014) trying to find a permanent fix for this issue—as are hundreds of people in various Apple Support threads (one fix that some have reported to work is to roll back the AirPort driver to an older version, downloaded from some random forum, but I'm not trusting enough to try that). I will continue to update this post with more info as I can find it, and please feel free to comment with any findings of your own!</p>
