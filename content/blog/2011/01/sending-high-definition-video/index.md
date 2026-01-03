---
nid: 52
title: "Sending High-Definition Video over Long Distances"
slug: "sending-high-definition-video"
date: 2011-01-11T02:09:08+00:00
drupal:
  nid: 52
  path: /articles/audio-and-video/2011/sending-high-definition-video
  body_format: full_html
  redirects: []
tags:
  - baluns
  - component
  - hd
  - video
aliases:
  - /articles/audio-and-video/2011/sending-high-definition-video
---

<p>I&#39;m working on increasing the quality of video sent through the Cathedral Basilica of St. Louis&#39; in-house video distribution system (right now they use passive composite video connections over Cat5 cabling, and video is very blurry with lots of ghosting), and I thought I&#39;d briefly share my findings in this area.</p>
<p>I&#39;ve decided to go with an &#39;active&#39; (powered) video send/receive unit, from Knoll Systems:</p>
<table border="0" cellpadding="10" cellspacing="1" style="width: 95%; margin: 0 auto 1em;">
<tbody>
<tr>
<td class="rtecenter">
<p><a href="http://www.amazon.com/gp/product/B001ARVS58?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B001ARVS58">{{< figure src="./knoll-us-v3-sender.jpg" alt="Knoll US-V3 Sender" width="175" height="175" class="blog-image" >}}</a></p>
<p><a href="http://www.amazon.com/gp/product/B001ARVS58?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B001ARVS58">Knoll US-V3 Sender</a>{{< figure src="http://www.assoc-amazon.com/e/ir?t=mmjjg-20&amp;l=as2&amp;o=1&amp;a=B001ARVS58" alt="" width="1" height="1" >}}</p>
</td>
<td class="rtecenter">
<p><a href="http://www.amazon.com/gp/product/B001ARSBQM?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B001ARSBQM">{{< figure src="./knoll-ur-v3-receiver.jpg" alt="Knoll UR-V3 Receiver" width="175" height="175" class="blog-image" >}}</a></p>
<p><a href="http://www.amazon.com/gp/product/B001ARSBQM?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B001ARSBQM">Knoll UR-V3 Receiver</a>{{< figure src="http://www.assoc-amazon.com/e/ir?t=mmjjg-20&amp;l=as2&amp;o=1&amp;a=B001ARSBQM" alt="" width="1" height="1" >}}</p>
</td>
<td class="rtecenter">
<p><a href="http://www.amazon.com/gp/product/B001E5PJK6?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B001E5PJK6">{{< figure src="./knoll-power-supply.jpg" alt="Knoll 12V Power Supply" width="175" height="175" class="blog-image" >}}</a></p>
<p><a href="http://www.amazon.com/gp/product/B001E5PJK6?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B001E5PJK6">Knoll 12V Power Supply</a>{{< figure src="http://www.assoc-amazon.com/e/ir?t=mmjjg-20&amp;l=as2&amp;o=1&amp;a=B001E5PJK6" alt="" width="1" height="1" >}}</p>
</td>
</tr>
</tbody>
</table>
<p>The basic principle is this: To get high-quality video from point A to point B, you need a good signal. The longer the distance of the cable, the weaker the signal will be.</p>
<p>While it&#39;s possible to run three individual coaxial or RCA-type cables over a 100&#39;+ distance, this would be a hassle, and would be prohibitively expensive. Rather, most wiring projects these days involve Cat5e and Cat6 networking cables, which can be used for a variety of purposes, especially since the use of Baluns has increased.</p>
<p>(Another example of sending non-data/network traffic over Cat5e cabling is detailed in my article elsewhere:&nbsp;<a href="/articles/audio-video/xlr-mic-level-balanced-audio-over-cat5e">XLR over Cat5 - Balanced XLR Mic-Level &amp; Line-Level Audio over Cat5 &amp; Cat5e Cabling</a>).</p>
<h3>Send High-Definition Video Over Long Distances</h3>
<p>The basic plan for a project like this involves:</p>
<ol>
<li>Run Cat5e or Cat6 network cable from point A to point B (use cable grease, gloves, and get dirty!). Run an extra cable or two if you think you&#39;ll need it. (Pick up some <a href="http://www.amazon.com/gp/product/B000067RFV?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B000067RFV">bulk Cat5e cable</a>{{< figure src="http://www.assoc-amazon.com/e/ir?t=mmjjg-20&amp;l=as2&amp;o=1&amp;a=B000067RFV" alt="" width="1" height="1" >}} from Amazon for a good price).</li>
<li>Terminate both ends of the cable in <a href="http://www.amazon.com/gp/product/B000067SC4?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B000067SC4">RJ-45 connectors</a>{{< figure src="http://www.assoc-amazon.com/e/ir?t=mmjjg-20&amp;l=as2&amp;o=1&amp;a=B000067SC4" alt="" width="1" height="1" >}} (you&#39;ll need a <a href="http://www.amazon.com/gp/product/B0000AZK4G?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B0000AZK4G">RJ-45 crimp tool</a>{{< figure src="http://www.assoc-amazon.com/e/ir?t=mmjjg-20&amp;l=as2&amp;o=1&amp;a=B0000AZK4G" alt="" width="1" height="1" >}} to finish off the cables).</li>
<li>Buy a send and a receive video balun (see links at top of this page), and wire everything together.</li>
</ol>
<p>Once you&#39;re done with the wiring, you should have a relatively clean (up to) 1080p signal. It&#39;s a lot cheaper (and easier to run over long distances) than pre-made HDMI or component video cables.</p>
<h3>Review of Knoll Systems Component Video Baluns</h3>
<p>These baluns definitely look good on paper: They use a 12V power supply (sold separately - order links above), so they give a stronger signal over longer distances than traditional/cheaper &#39;passive&#39; baluns. Additionally, the Knoll Systems components can distribute video to more than one device with the use of one of their hubs (or any non-switching &#39;dumb&#39; network hub).</p>
<p><em>I will post a full review of these baluns when they arrive (I just ordered them!).</em></p>
<h3>Alternatives</h3>
<p>You can, of course, use one of the many unpowered baluns (which are usually anywhere from $40-60), or opt out of high definition (especially if your TV/projection system doesn&#39;t support HD!), but if you want to go higher quality than this, you&#39;ll have to look into digital systems (TV over IP), which cost a bit more.</p>
<p>I&#39;m also building a new site, <a href="http://everythingovercat5.com/">Everything Over Cat5</a>, to compile my different projects/experiences with Category 5 copper cabling. It&#39;s awesome&mdash;check it out!</p>
<p>Any questions? Any better ideas or experiences with other baluns?</p>
