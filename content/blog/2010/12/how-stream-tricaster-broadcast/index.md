---
nid: 55
title: "How to Stream from Tricaster Broadcast/Pro to Ustream.tv or Watershed"
slug: "how-stream-tricaster-broadcast"
date: 2010-12-29T16:31:51+00:00
drupal:
  nid: 55
  path: /articles/computing/2010/how-stream-tricaster-broadcast
  body_format: full_html
  redirects: []
tags:
  - flash
  - streaming
  - tricaster
  - ustream
  - video
  - watershed
---

<p>How to Stream from Tricaster Broadcast/Pro to Ustream.tv</p>
<p>The following instructions are based on <a href="http://www.ustream.tv/recorded/1452173">this video</a>, embedded below:</p>
<p class="rtecenter"><object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" height="296" width="480"> <param name="flashvars" value="vid=1452173&amp;autoplay=false" /> <param name="allowfullscreen" value="true" /> <param name="allowscriptaccess" value="always" /> <param name="src" value="http://www.ustream.tv/flash/viewer.swf" /> <embed allowfullscreen="true" allowscriptaccess="always" flashvars="vid=1452173&amp;autoplay=false" height="296" src="http://www.ustream.tv/flash/viewer.swf" type="application/x-shockwave-flash" width="480"></embed> </object></p>
<p>Preliminary Notes:</p>
<ul>
<li>&nbsp;You need at least version 2.5 of Tricaster software.</li>
<li>&nbsp;Download 2.5 or later at register.newtek.com (go to my downloads).</li>
<li>&nbsp;For Watershed, the process is similar, but you need to get the Flash XML file from Watershed directly.</li>
</ul>
<p>First, you&#39;ll need to turn on the Tricaster, and make sure it&#39;s connected to the Internet. You should also try to make sure you have a relatively decent (and stable) Internet connection, for obvious reasons. Some problems may be caused by a restrictive firewall, as well, so watch out for that. (Check your Internet upload speed using <a href="http://speedtest.net/">Speedtest.net</a>&nbsp;- you should have at least 300-500 kbps upload).</p>
<!--break-->
<h3>On the Tricaster computer, on the Internet</h3>
<ol>
<li>Click the X on the right side of the screen and select &#39;Admin mode&#39; to go to the Desktop.</li>
<li>Go to Ustream.tv, and login.</li>
<li>Go to your account on Ustream, and click on the &#39;Manage Your Show&#39; button, then under that, &#39;Settings.&#39;</li>
<li>Click to expand the &#39;Advanced settings&#39; at the bottom of the Settings page, and click the link to &quot;Download the Flash Media Encoder XML file.&quot;</li>
</ol>
<h3>On the Tricaster computer</h3>
<ol>
<li>Go to Start &gt; Run..., and type &quot;winrtme&quot; and hit Enter</li>
<li>Go to Start &gt; Programs &gt; Adobe &gt; Flash Media Encoder 3 (ignore any errors).</li>
<li>Go to File &gt; Open Profile, and open the flash file (XML) that you downloaded earlier.</li>
<li>Copy out the &quot;FMS URL&quot; and &quot;Stream&quot; values so you can paste those into Tricaster Studio later.</li>
<li>Close Flash Encoder.</li>
</ol>
<h3>On the Tricaster computer, in Tricaster Studio</h3>
<ol>
<li>Click Launch Tricaster</li>
<li>Click on the &#39;Record Stream&#39; tab.</li>
<li>Choose one of the two &#39;Flash Ustream&#39; stream types from the &quot;Stream Type&quot; dropdown menu.</li>
<li>Paste in the values for the &quot;FMS URL&quot; (begins with rtmp://), and &quot;Stream ID.&quot;</li>
<li>Click &quot;Stream Live Output&quot; to begin streaming to Ustream.</li>
</ol>
<h3>On another Internet-connected computer, on the Internet</h3>
<ol>
<li>Log into Ustream.tv and click &quot;Broadcast&quot; to start broadcasting LIVE...</li>
<li>The Ustream console will appear (if you have multiple shows, you need to select which one to broadcast first).</li>
<li>Manage your Ustream broadcast using the Ustream console on this computer.</li>
</ol>
<p>That&#39;s it! You should be able to stream from your TriCaster now. Happy broadcasting!</p>
<p>Read more about <a href="http://www.opensourcecatholic.com/wiki/117/live-streaming-event">streaming your live events via Ustream.tv or Watershed</a> on Open Source Catholic.</p>
