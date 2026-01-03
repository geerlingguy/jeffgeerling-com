---
nid: 2604
title: "Lessons Learned building the Raspberry Pi Dramble"
slug: "lessons-learned-building-raspberry-pi-dramble"
date: 2015-03-22T02:15:38+00:00
drupal:
  nid: 2604
  path: /blog/lessons-learned-building-raspberry-pi-dramble
  body_format: full_html
  redirects: []
tags:
  - ansible
  - bramble
  - cluster
  - dramble
  - drupal
  - drupal planet
  - essay
  - php
  - raspberry pi
---

<p style="text-align: center;">{{< figure src="./raspberry-pi-dramble-contrast_1.jpg" alt="Raspberry Pi Dramble Bramble Cluster" width="450" height="337" >}}</p>

<blockquote><strong>Edit</strong>: Many people have been asking for more technical detail, benchmarks, etc. There is <em>much</em> more information available on the <a href="http://www.pidramble.com/wiki">Raspberry Pi Dramble Wiki</a> (e.g. <a href="http://www.pidramble.com/wiki/benchmarks/power-consumption">Power Consumption</a>, <a href="http://www.pidramble.com/wiki/benchmarks/microsd-cards">microSD card benchmarks</a>, etc.), if you're interested.</blockquote>

<p>After the Raspberry Pi 2 model B was released, I decided the Pi was finally a fast enough computing platform (with its 4-core 900 MHz ARMv7 architecture) with enough memory (1 GB per Pi) to actually use for web infrastructure. If not in a production environment (I would definitely avoid putting the Pi into a role as a high-load 24x7x365 server), then for development and/or testing purposes. And for some fun!</p>

<p>I built a 6-Pi cluster, a.k.a. a 'bramble', and am using it to benchmark different infrastructure layouts, trying to see how I can get a few more requests per second out of Drupal 8 (which is a fairly heavy PHP application still in early and active development).</p>

<p>In the course of building the bramble—which I nicknamed the <a href="https://github.com/geerlingguy/raspberry-pi-dramble">Dramble</a> ('<strong>Dr</strong>upal' on a <strong>bramble</strong>... get it?), I've learned a few things. The most important lesson, which I learn quite often: fun diversions like building a cluster of 6 Raspberry Pis and soldering some RGB LEDs keeps the mind flexible and is a good counter-balance to the day-to-day development activities that can lead to boredom, and ultimately, burnout!</p>

<p>The first presentation I did with the Dramble was <a href="http://2015.midcamp.org/session-proposal/ansible-drupal-fortuitous-devops-match">Ansible + Drupal: A Fortuitous DevOps Match</a> at MidCamp in Chicago. I'm hoping to do more presentations demonstrating infrastructure management with an improved revision of the Dramble.</p>

<h2>
<a id="user-content-constraints-give-more-clarity-to-the-decisionmaking-process" class="anchor" href="#constraints-give-more-clarity-to-the-decisionmaking-process" aria-hidden="true"><span class="octicon octicon-link"></span></a>Constraints give more clarity to the decisionmaking process</h2>

<p>When you run a resource-heavy application like Drupal in a very constrained environment (disk access speeds from the late 90s, and network access like the early 00s), it forces you to look at performance in a new way—holistically, on the entire stack. Simple choices like the microSD card you use can make an order-of-magnitude difference.</p>

<p>You realize quickly that benchmarking, and comparing <em>real, hard data</em>, is the best and fastest way to decide which of two routes to take. And it is also freeing to realize certain hardware limitations mean some micro-optimizations (e.g. which load balancing software can eke out 1.2% more requests per second on a given network?) don't really matter at all (if your network speed equalizes the performance of the two apps, choose the one that's easiest to set up and maintain).</p>

<h2>
<a id="user-content-small-problems-are-magnifiedand-easier-to-analyze" class="anchor" href="#small-problems-are-magnifiedand-easier-to-analyze" aria-hidden="true"><span class="octicon octicon-link"></span></a>Small problems are magnified—and easier to analyze</h2>

<p>Seemingly small problems (a few extra seconds in a setup process, a little extra memory used during cache rebuilding operations or server restarts, etc.) can become amplified much larger when you run a beefy interpreted application like Drupal on a set of small servers. For some operations, all 4 cores of one of the Pis can be giving 100% while the database server sits idle. For other operations, a disk-heavy process slows things down exponentially, and what takes 10 seconds on a modern SSD-backed database server can take a minute or two on a Pi.</p>

<p>Not only does this force you to think of 'how could I optimize the Pis to avoid this disk access here or this CPU-heavy operation there', but it also sheds light on areas of Drupal itself that could be improved; do we really need to access the disk five hundred times in this one spot of code, or can we cache an operation and save 499 of those file checks?</p>

<p>It's the same conundrum many front-end web developers face when they test the whiz-bang new animations they've been developing on their workstation (with 4 fast CPU cores and 16GB of RAM) on a common smartphone the first time. If you are always developing and testing in environments with best-in-class performance, you can easily overlook seemingly insignificant optimizations that will help save zillions of CPU cycles on the majority of hosting environments!</p>

<h2>
<a id="user-content-the-network-is-never-reliable" class="anchor" href="#the-network-is-never-reliable" aria-hidden="true"><span class="octicon octicon-link"></span></a>The network is <em>never</em> reliable</h2>

<p>You'd think running a small cluster of six Raspberry Pis through a local gigabit private network would mean there are no real networking issues—and you'd be wrong!</p>

<p>Those who've built distributed systems know intuitively to not rely on the network—whether it be the Internet, inside a datacenter, inside one rack of servers, or heck, even <em>a virtual network on the server itself</em>! Networking is unreliable, and you should always build your automation, infrastructure, and application to be fault-tolerant as much as you can. Assume that any one of your servers or connections could go down at any time, and you'll be much better off.</p>

<p>You pay a price for building greater redundancy, and that price may or may not be worth it for your particular application, but never trust that your network will perform flawlessly.</p>

<p>On Raspberry Pis specifically, there are often little software bugs in Raspbian, configuration issues with <code>/etc/resolv.conf</code> or <code>/etc/network/interfaces</code>, or even strange hardware issues that only arise after you've been saturating a built-in LAN port's 100 Mbps connection for an hour. Be prepared for these little issues, and learn from them. Even the best networking gear on the fastest servers has strange issues from time to time!</p>

<h2>
<a id="user-content-anything-that-can-go-wrong-will-go-wrong" class="anchor" href="#anything-that-can-go-wrong-will-go-wrong" aria-hidden="true"><span class="octicon octicon-link"></span></a>Anything that can go wrong, will go wrong</h2>

<p>Along the same thing, mix a bunch of time-sensitive protocols together with a cluster of servers that have no built-in clocks and aren't connected to the Internet (so, no easy NTP), and weird issues crop up at the wrong time.</p>

<p>In my case, the night before I gave my first presentation with the Dramble, I was running through the presentation without an Internet connection, and after two tense hours, I finally figured out that a time drift of three seconds made Drupal 8's twig caching system hit a weird bug that caused all the webservers to return 500 errors. Luckily, simply resetting the time using Ansible so it was &lt; 1 second apart on all the servers got everything back up and running.</p>

<h2>
<a id="user-content-cheapfree-servers-free-you-to-have-fun-and-experiment" class="anchor" href="#cheapfree-servers-free-you-to-have-fun-and-experiment" aria-hidden="true"><span class="octicon octicon-link"></span></a>Cheap/free servers free you to have fun and experiment</h2>

<p>Having cheap, almost free, resources (little Pi's or cheap hourly VM instances) gives you freedom: to experiment, to break things, to try new things and do them ten different ways.</p>

<p>I used to do some video work as a hobby; I came into the field of video production at a perfect time, when cameras, editing equipment, audio recording devices, and everything in the pipeline was digitized and started the democratization of the video process. What used to cost a hundred thousand dollars cost mere hundreds. It still takes much more than inexpensive equipment to produce a great video, but easier access to the tools required to tinker opens up the realm of video production to a much wider, more diverse audience.</p>

<p>Similarly, the Raspberry Pi—and all the similar inexpensive credit-card sized computers—is one key to democratizing programming and infrastructure development. Whereas it cost thousands of dollars and required large-scale power and cooling to build an infrastructure to be used for research, testing, and development, these new systems can acheive some decent performance, have built-in hardware GPIO interfaces for doing even more interesting things than typical servers), and cost $20-35 each!</p>

<p>When computing is this inexpensive, having some fun, doing new things—generally, <em>hacking</em>—becomes easier and more accessible.</p>

<h2>
<a id="user-content-building-hardware-is-fun" class="anchor" href="#building-hardware-is-fun" aria-hidden="true"><span class="octicon octicon-link"></span></a>Building hardware is fun</h2>

<p>Pulling out the soldering iron brought me back to my gradeschool days when my Dad bought me my first soldering iron and an electronics kit. After he taught me how to solder a simple circuit, I remember building a few Radio Shack kits (including an FM radio transmitter and even a multimeter I still use today!).</p>

<p>With the Raspberry Pi (and also the Arduino to a greater extent), prototyping software-controlled circuits is simple and fun. It feels great to build a small circuit, turn on the Pi, and see that I can manipulate the circuit through a few lines of code. Measuring voltages, amperage, and continuity brings out a little bit of a boyish excitement.</p>

<p style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/rRJQiHydVG4" frameborder="0" allowfullscreen></iframe>
Demonstration of Ansible deployments using RGB LEDs on the Raspberry Pi</p>

<p>I primarily develop software, but building the <a href="http://www.pidramble.com/wiki/hardware/rgb-led-gpio">six RGB LED boards</a> that plug into each Pi in the Dramble was a fun diversion and makes me want to spend more time refining my circuits to use fewer connections, less board space, and less power. Just like it's often fun to debug and optimize my software, it's fun to do some real-world debugging on a small electric circuit!</p>

<p>Many of the lessons I've learned building the Dramble have helped to refine content in my book <em>Ansible for DevOps</em>, available on <a href="https://leanpub.com/ansible-for-devops">LeanPub</a>, <a href="http://www.amazon.com/Ansible-DevOps-Server-configuration-management-ebook/dp/B016G55NOU/">Amazon</a>, or <a href="https://itunes.apple.com/us/book/ansible-for-devops/id1050383787?ls=1&mt=11">iTunes</a></em>.</p>
