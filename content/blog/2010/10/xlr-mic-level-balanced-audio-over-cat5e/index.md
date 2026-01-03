---
nid: 51
title: "XLR over Cat5 - Balanced XLR Mic-Level & Line-Level Audio over Cat5 & Cat5e Cabling"
slug: "xlr-mic-level-balanced-audio-over-cat5e"
date: 2010-10-25T05:04:37+00:00
drupal:
  nid: 51
  path: /articles/audio-video/xlr-mic-level-balanced-audio-over-cat5e
  body_format: full_html
  redirects: []
tags:
  - audio
  - cat5
  - microphone
  - networking
  - recording
  - wiring
  - xlr
aliases:
  - /articles/audio-video/xlr-mic-level-balanced-audio-over-cat5e
---

<p class="rtecenter"><br />
{{< figure src="./cat5-cable-xlr-audio.jpg" alt="Cat5 Cable with XLR Audio Jacks" width="535" height="147" class="blog-image" >}}</p>
<p><strong>The challenge</strong>: Run two 200&#39; cable runs for VOX (2-way communication via headsets) and an ambient microphone. Mics and headsets to be used for broadcast of major event via satellite, web, and all major local news outlets.</p>
<p><strong>Limitations</strong>: Extremely tight budget for cable + installation, two weeks to install and test, 100 year old stone/masonry building, skeleton crew of volunteers.</p>
<p><strong>Solution</strong>:</p>
<ul>
<li>Run readily-available Cat5e (shielded, solid) network cable to two VOX/mic locations (we had a box with a few hundred feet left inside, and we bought another 500&#39; box (extra == always better) for $100. (Check Amazon for <a href="http://ttp://www.amazon.com/gp/product/B000067RFV?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B000067RFV">bulk Cat5e cable</a>).</li>
<li>Use <a href="http://www.amazon.com/gp/product/B0002BG31C?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B0002BG31C">custom faceplates with two XLR jacks</a>&mdash;female for VOX headsets, female for Mic input</li>
<li>Cross fingers, and hope it works.</li>
</ul>
<!--break-->
<h3>The Story</h3>
<p>I was asked in 2009 to help set up the Cathedral Basilica of St. Louis&mdash;a huge, stone, early 20th century Church&mdash;for a Mass of Installation, which would be broadcast via satellite to four local news stations, two international cable stations, and a few online streaming stations.</p>
<p class="rtecenter">{{< figure src="./mic-locations-in-cathedral-basilica.jpg" alt="Mic Locations in Cathedral Basilica of St. Louis" width="675" height="446" class="blog-image" >}}<br />
The Cathedral Basilica of St. Louis is <em>huge</em>.</p>
<p>We would be using two built-in HD cameras, along with three other cameras brought in by local media. Two of the locations would need the ability to communicate with the producer&#39;s desk in the back of Church via headsets (requiring a send/receive balanced connection), and both of these locations would also have mics to record ambient sound in the Church.</p>
<p>I have worked on a few other mic and cabling installations in the past few years, and, with a lot of volunteered help from my Father (a lifelong broadcast radio engineer, and electronics genius), successfully sent a clean, line-level signal through about 300&#39; of unshielded Cat5 cable a year prior.</p>
<p>We decided to try the same thing here, but we wanted to run balanced mic-level audio over the wire, and not one, but three(!) signals per cable.</p>
<h3>Using Cat5e Cable for Balanced Audio Signals</h3>
<p>Since balanced audio helps cancel out much of the interference that would be caused by things like radio waves and power lines, shielded twisted pair cabling (like that found in Cat5e&mdash;or &#39;Category 5e&#39;&mdash;cable) is not a bad choice for balanced audio signals.</p>
<p>However, microphone level audio is a very low-power signal, and we thought it might not survive the length of our cable runs. We had successfully tested the length with a 500&#39; of cable sitting on the floor, but we didn&#39;t know if running the wire the length of a football field, through many different areas of the Cathedral, would work.</p>
<p>As it turns out, our worries were unfounded.</p>
<p>Along with the associate pastor of the Cathedral, and another helper or two from time to time, I ran a Cat5e cable down one side of the Cathedral (we also ran a couple more to locations where we set up TVs via Cat5-&gt;Composite video baluns), and then the other... this was the most frustrating part of the process, as there were a great deal of areas where patience was the only thing that kept us from giving up and breaking something... Plus, we thought we had kinked the wire maybe four or five times, so kept our fingers crossed after finishing the cable runs.</p>
<p class="rtecenter">{{< figure src="./xlr-pinout-diagram.png" alt="XLR Male and Female Pinout Diagram (from Wikipedia)" width="300" height="178" class="blog-image" >}}</p>
<table border="0" cellpadding="5" cellspacing="1" style="width: 70%; margin: 0 auto 1em;">
<tbody>
<tr>
<td><strong>Pin #</strong></td>
<td><strong>Wires (Cat5e twisted pair)</strong></td>
</tr>
<tr>
<td>1</td>
<td>Ground / Shield | Ground / Shield</td>
</tr>
<tr>
<td>2</td>
<td>(A) White blue + white green | (B) White orange + white brown&nbsp;</td>
</tr>
<tr>
<td>3</td>
<td>(A) Blue + green | (B) Orange + brown</td>
</tr>
</tbody>
</table>
<p>After de-greasing our hands, cutting the cable, and finishing up the boxes that would hold the XLR jacks, my Dad helped with the soldering (actually, he did most of it!) of the twisted pairs to the XLR jacks. We used one pair for each jack, and used the solid wires (two twisted together) for positive (+) on pin 2, and the striped/spotted wires (two twisted together) for negative (-) on pin 3. We put the ground/shield into pin 1:</p>
<p>Control Room wiring shown below:</p>
<p class="rtecenter">{{< figure src="./control-wiring.jpg" alt="Control Room XLR Cat5e Wiring" width="625" height="466" class="blog-image" >}}</p>
<p>Nave wiring shown below (sorry it&#39;s so dark!):</p>
<p class="rtecenter">{{< figure src="./nave-wiring.jpg" alt="Nave XLR Cat5e Wiring" width="625" height="466" class="blog-image" >}}</p>
<h3>Results</h3>
<p>You can <a href="http://stlouisreview.com/installation/2009/homily-of-archbishop-carlson">hear for yourself</a> a part of the Mass (on the St. Louis Review news website); the producers mixed in just enough of the ambient to allow for the choir/organ/orchestra to be heard, and for some crowd noise.</p>
<p>In our simple headphone testing, only the slightest amount of noise was heard (pretty much what you&#39;d expect out of a standard 100&#39;+ mic cable), and all frequencies could be heard clearly. Signal level was very strong. (Unfortunately, we didn&#39;t have any measurement equipment with us, and we were on a tight schedule, so we couldn&#39;t find the distortion, freq response, noise floor, or anything like that).</p>
<p>Plus, our finished wiring looked nice, to boot!</p>
<table border="0" cellpadding="5" cellspacing="1" style="width: 100%; ">
<tbody>
<tr>
<td class="rtecenter" style="vertical-align: middle; ">
<p>{{< figure src="./control-room-jacks.jpg" alt="Control Room XLR and Coaxial Jacks" width="300" height="170" class="blog-image" >}}</p>
<p>Finished wiring - control room</p>
</td>
<td class="rtecenter" style="vertical-align: middle; ">
<p>{{< figure src="./nave-jacks.jpg" alt="Nave XLR Jacks" width="220" height="143" class="blog-image" >}}</p>
<p>Finished wiring - nave</p>
</td>
</tr>
</tbody>
</table>
<h3>Afterword</h3>
<p>Enjoy knowing that you can always find some cheap cable to run microphone and line-level signals in a pinch! (I strongly recommend only using shielded cable, and trying to use a balanced signal if at all possible&mdash;this will help minimize interference).</p>
<p>Here is a link to more <a href="http://business.virgin.net/tom.baldwin/pinout-3xlr.html">XLR pinout configurations</a>, for your viewing pleasure.</p>
<p>I&#39;m also building a new site, <a href="http://everythingovercat5.com/">Everything Over Cat5</a>, to compile my different projects/experiences with Category 5 copper cabling. It&#39;s awesome&mdash;check it out!</p>
<p>What else do you run over Cat5e? I&#39;m also running full HD video: <a href="/articles/audio-and-video/2011/sending-high-definition-video">Sending High-Definition Video over Long Distances</a>.</p>
