---
nid: 57
title: "Share a Proxied Network Connection via WiFi to your iPad/iPhone/iPod"
slug: "share-a-proxied-network"
date: 2010-05-28T19:13:03+00:00
drupal:
  nid: 57
  path: /articles/computing/2010/share-a-proxied-network
  body_format: full_html
  redirects: []
tags:
  - authentication
  - ipad
  - iphone
  - ipod touch
  - networking
  - ntlm
  - proxy
aliases:
  - /articles/computing/2010/share-a-proxied-network
---

<p>For the past six weeks that I&#39;ve had my iPad, I&#39;ve fought with my office network, because it uses a Microsoft/NTLM authenticated proxy server which wreaks havoc on the iPhone OS&#39;s ability to use the Internet effectively (especially for third party apps).</p>
<p>After reading through countless forum support requests for people asking the same questions, I&#39;ve finally found a (mostly) workable solution for this problem&mdash;at least for most apps and browsing on the iPad.</p>
<h3>Doubling the Proxy</h3>
<p>Since the iPhone OS seems to have a pretty hard time dealing with proxy authentication (most apps don&#39;t act like there&#39;s even an internet connection, even if Safari will work through the proxy), I used a solution I often use on my Macs at work: doubling up the proxy.</p>
<p>Basically, you can use an application like <strong><a href="http://www.hrsoftworks.net/Products.php#authoxy">Authoxy</a></strong> on the Mac to make the Mac translate all its web traffic through a special internal connection, which gets messaged correctly by Authoxy to work with your company&#39;s proxy server.</p>
<p>For the iPad, however, you will need a different way of funneling your connection through your Mac to your iPad. First, you need to turn on Internet Sharing with your Mac (<a href="http://docs.info.apple.com/article.html?path=Mac/10.5/en/8156.html">instructions</a>), then you will need to download and run <strong><a href="http://ntlmaps.sourceforge.net/">NTLMaps</a></strong>, which is a little command-line python script that works similarly to Authoxy, but is a little more efficient in what it does, and works better with the iPad.</p>
<p>To run NTLMaps, all you need to do is open up the Terminal and type in <code>/path/to/main.py</code></p>
<p>This will run the python script that kicks off the appropriate connections on your Mac. To configure NTLMaps for your network, you need to open up the included server.cfg file (in the same folder as main.py) in your favorite text editor, and read through it to make the changes for your network environment.</p>
<p>For my purposes, I edited the following:</p>
<ul>
<li># The port on which your computer will act as a proxy server<br />
LISTEN_PORT: 8082</li>
<li># Your office&#39;s proxy server<br />
PARENT_PROXY: 10.1.1.3</li>
<li># Your office&#39;s proxy server port<br />
PARENT_PROXY_PORT: 8080</li>
<li># Set this to 1 to allow your iPad to connect<br />
ALLOW_EXTERNAL_CLIENTS: 1</li>
<li># The domain of your windows network<br />
NT_DOMAIN: domain.org</li>
<li># Your network username<br />
USER: username</li>
<li># Your network password<br />
PASSWORD: password</li>
</ul>
<p>You can read through the other options, but these are what are necessary to get you started.</p>
<h3>Connecting on your iPad/iPhone/iPod</h3>
<p>Once you have the NTLMap script running on your Mac (you&#39;ll see <code>Now listening at your-computer-name.domain.org on port 8082</code> in the Terminal window), and you have Internet Sharing turned on, you can connect to your Mac&#39;s shared WiFi connection on the iPad.</p>
<p>Under the HTTP Proxy settings for your wifi network (click the blue right arrow next to your wifi connection&#39;s name to get to the settings for that network), enter the following information:</p>
<p class="rtecenter">{{< figure src="./proxy-settings-ipad.jpg" alt="iPad Proxy Settings - Authentication through NTLMap" width="650" height="488" class="blog-image" >}}</p>
<ul>
<li>Tap on &#39;Manual&#39; for the HTTP Proxy type.</li>
<li>Enter your Mac&#39;s IP address (look above at the &#39;Router&#39; value) for &#39;Server.&#39;</li>
<li>Enter the port you have set as &quot;LISTEN_PORT&quot; in NTLMap.</li>
<li>Leave &#39;Authentication&#39; set to OFF.</li>
</ul>
<p>You should now be able to open up Safari, Twitteriffic, WeatherBug, Dropbox, and any other Internet-enabled app and get online pretty easily.</p>
<p>I&#39;m still working on finding a way to get my mail to route correctly to the iPad&#39;s built-in Mail app, but for now, most everything works great!</p>
