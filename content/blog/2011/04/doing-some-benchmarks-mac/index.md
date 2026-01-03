---
nid: 2419
title: "Doing Some Benchmarks - Mac Processor Speed"
slug: "doing-some-benchmarks-mac"
date: 2011-04-08T18:25:28+00:00
drupal:
  nid: 2419
  path: /blogs/jeff-geerling/doing-some-benchmarks-mac
  body_format: full_html
  redirects: []
tags:
  - benchmarking
  - cpu
  - imac
  - mac
  - macbook air
  - macbook pro
  - performance
aliases:
  - /blogs/jeff-geerling/doing-some-benchmarks-mac
---

I currently own or use a variety of Macs, and am approaching the end of a 'cycle' of Mac usage, where I need to decided what Mac I'd like to purchase next. Currently, I'm using a 27" iMac at work, an 11" MacBook Air (from work) for travel, and a 24" iMac at home. They're all great computers in their own right, and using Dropbox, MobileMe, and a couple other helper services, I can operate simultaneously on all three Macs, without any hiccups.

So, I'm thinking about getting a new Mac for hardcore development work (web and app), some graphic design, and possible portability. I have an iPad for lighter computing (reading, browsing, email, videos...), so even though the MacBook Air is probably the best thing to happen to a laptop in a very long time, I'm shying away from it as my primary personal computer.

One of the very few things that I really notice when switching from either of the iMacs (both with 2.8 Ghz processors - work with a quad core, home with core 2 duo) to the MacBook Air is the processor speed difference. (The MBA's SSD <a href="http://forkbombr.net/ssd-life-in-the-fast-lane/">blows away</a> the disk performance of either iMac—but that just masks the lower processor performance in many situations). Examples of times where it's painful to use the MacBook Air: Heavy Photoshop processing, Aperture photo adjustments (especially with a hundred or two photos on the road—the processor's pegged at 100% the whole time!), and building an App in Xcode for testing/debugging.

I'm thinking of going one of two routes:

<ol>
	<li>Simply purchase a monster 15" MacBook Pro (core i7, maxed out) with the high-res display, max out the RAM, and put in a <a href="http://eshop.macsales.com/shop/internal_storage/Mercury_Extreme_SSD_Sandforce/Solid_State_Pro">115 GB SSD drive</a>, and stick the HDD drive into the Optical Drive slot with <a href="http://eshop.macsales.com/search/data+doubler">this nifty cage</a> from OWC.</li>
	<li>iMac 21" middle-of-the-road, for heavier work, and 13" MacBook Air with 4GB RAM for travel.</li>
</ol>

No matter what route I go, I'm going to get very nice results—better than my current setup. But I think what it comes down to—for me—is whether I can suffer through a slow experience of batch-editing a few hundred Aperture photos, or waiting 1.5 minutes every time I build an iPhone app for testing...

So, for the rest of this post, I'm simply going to post some benchmarks (to be updated as I get time on friends' Macs, at the Apple Store, etc.) of processor speed, as tested using the nifty <a href="http://www.macupdate.com/app/mac/9641/power-fractal">Power Fractal</a> app that was written quite a long time ago, and is one of the only constant apps I've been able to trust for a processor-intense test throughout the G4-&gt;G5-&gt;Intel transition. I remember eeking every last bit of CPU out of my old G4/400 MHz to try to break the 1,000 Mflop barrier, by quitting every service that was running on that old Mac (10.1 or 10.2 at the time!).

For each Mac, I used '65536' for 'Maximum Count,' '10' for 'Color speed,' '2' for 'Zoom Factor,' and ran the test three times. Posted below are the averages for three tests.

Here goes:

<table style="font-size: 0.82em; width: 80%;" border="0">
<tbody>
<tr>
<td style="background-color: #eeeeee;"><strong> Mac Model </strong></td>
<td style="background-color: #eeeeee;"><strong> Processor Speed </strong></td>
<td style="background-color: #eeeeee;"><strong> Cores </strong></td>
<td style="background-color: #eeeeee;"><strong> Price </strong></td>
<td style="background-color: #eeeeee;"><strong> Gigaflops </strong></td>
<td style="background-color: #eeeeee;"><strong> Dollars per GFlop </strong></td>
</tr>
<tr>
<td><strong> MacBook Air 11” 1.3 i5 (2013)</strong></td>
<td>1300</td>
<td>2</td>
<td>999</td>
<td>23.7</td>
<td>42</td>
</tr>
<tr>
<td><strong> MacBook Air 11” 1.7 i7 (2013)</strong></td>
<td>1700</td>
<td>2</td>
<td>1445</td>
<td>29.8</td>
<td>49</td>
</tr>
<tr>
<td><strong> MacBook Air 11” 1.4 c2d (2010)</strong></td>
<td>1400</td>
<td>2</td>
<td>999</td>
<td>9.6</td>
<td>104</td>
</tr>
<tr>
<td><strong> MacBook Air 11” 1.6 c2d (2010)</strong></td>
<td>1600</td>
<td>2</td>
<td>1299</td>
<td>11.1</td>
<td>117</td>
</tr>
<tr>
<td><strong>MacBook Air 11" 1.6 i5 (2011)</strong></td>
<td>1600</td>
<td>2</td>
<td>999</td>
<td>19.7</td>
<td>51</td>
</tr>
<tr>
<td><strong> MacBook Air 13” 1.86 c2d </strong></td>
<td>1860</td>
<td>2</td>
<td>1299</td>
<td>12.8</td>
<td>101</td>
</tr>
<tr>
<td><strong> MacBook Air 13” 2.13 c2d </strong></td>
<td>2130</td>
<td>2</td>
<td>1699</td>
<td>?</td>
<td>0</td>
</tr>
<tr>
<td><strong> MacBook 13” 2.4 c2d </strong></td>
<td>2400</td>
<td>2</td>
<td>999</td>
<td>16.6</td>
<td>60</td>
</tr>
<tr>
<td><strong> MacBook Pro 13” 2.3 i5 </strong></td>
<td>2300</td>
<td>2</td>
<td>1199</td>
<td>26.5</td>
<td>45</td>
</tr>
<tr>
<td><strong> MacBook Pro 13” 2.7 i7 </strong></td>
<td>2700</td>
<td>2</td>
<td>1499</td>
<td>31.4</td>
<td>48</td>
</tr>
<tr>
<td><strong>Mac Mini 2.3 i5</strong></td>
<td>2300</td>
<td>2</td>
<td>599</td>
<td>25.4</td>
<td>24</td>
</tr>
<tr>
<td><strong> iMac 24” 2.8 c2d (2008)* </strong></td>
<td>2800</td>
<td>2</td>
<td>1199</td>
<td>19.2</td>
<td>62</td>
</tr>
<tr>
<td><strong> iMac 27” 2.66 i5q (2009)* </strong></td>
<td>2660</td>
<td>4</td>
<td>1499</td>
<td>40.8</td>
<td>37</td>
</tr>
<tr>
<td><strong> iMac 21” 3.2 i3 </strong></td>
<td>3200</td>
<td>2</td>
<td>1499</td>
<td>29.1</td>
<td>52</td>
</tr>
<tr>
<td><strong> iMac 27” 2.8 i5q </strong></td>
<td>2800</td>
<td>4</td>
<td>1999</td>
<td>43.2</td>
<td>46</td>
</tr>
<tr>
<td><strong>MacBook Pro 15" 1.83 cd (2006)*</strong></td>
<td>1830</td>
<td>2</td>
<td>350</td>
<td>3.6</td>
<td>97</td>
</tr>
<tr>
<td><strong> MacBook Pro 15” 2.0 i7q </strong></td>
<td>2000</td>
<td>4</td>
<td>1799</td>
<td>50.3</td>
<td>36</td>
</tr>
<tr>
<td><strong> MacBook Pro 15” 2.2 i7q </strong></td>
<td>2200</td>
<td>4</td>
<td>2199</td>
<td>51.8</td>
<td>42</td>
</tr>
<tr>
<td><strong> MacBook Pro 15” 2.3 i7q </strong></td>
<td>2300</td>
<td>4</td>
<td>2449</td>
<td>53.9</td>
<td>45</td>
</tr>
<tr>
<td><strong>MacBook Pro 15" Retina 2.3 i7q</strong></td>
<td>2300</td>
<td>4</td>
<td>1999</td>
<td>64.7</td>
<td>31</td>
</tr>
<tr>
<td><strong>Macbook Pro 15" Retina 2.6 i7q</strong></td>
<td>2600</td>
<td>4</td>
<td>2599</td>
<td>71.3</td>
<td>36</td>
</tr>
<tr>
<td><strong> MacBook Pro 17” 2.2 i7q </strong></td>
<td>2200</td>
<td>4</td>
<td>2499</td>
<td>57.4</td>
<td>44</td>
</tr>
<tr>
<td><strong> MacBook Pro 17” 2.3 i7q </strong></td>
<td>2300</td>
<td>4</td>
<td>2749</td>
<td>58.9</td>
<td>47</td>
</tr>
<tr>
<td><strong> Mac Pro 2.8 Xeon quad </strong></td>
<td>2800</td>
<td>4</td>
<td>2499</td>
<td>53.6</td>
<td>47</td>
</tr>
</tbody></table>

*Prices are estimates from eBay, as of the writing of this post

Also for reference, <a href="http://www.primatelabs.ca/geekbench/mac-benchmarks/">here are the Geekbench results listings for Mac performance</a>. The Geekbench benchmarks test a variety of things, not just CPU, so those benchmarks are slightly less relevant for <em>my</em> purchasing decision...
