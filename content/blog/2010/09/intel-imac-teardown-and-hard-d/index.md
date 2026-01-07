---
nid: 82
title: "Intel iMac Teardown and Hard Drive Replacement - DIY/How-to Guide"
slug: "intel-imac-teardown-and-hard-d"
date: 2010-09-16T15:24:22+00:00
drupal:
  nid: 82
  path: /articles/computing/2010/intel-imac-teardown-and-hard-d
  body_format: full_html
  redirects:
    - /computing/2010/intel-imac-teardown-and-hard-dIn
    - /computing/2010/intel-imac-teardown-and-hard-d
aliases:
  - /computing/2010/intel-imac-teardown-and-hard-dIn
  - /articles/computing/2010/intel-imac-teardown-and-hard-d
  - /computing/2010/intel-imac-teardown-and-hard-d
tags:
  - apple
  - diy
  - guide
  - hard drive
  - hardware
  - how-to
  - imac
---

<p class="rtecenter">{{< figure src="./fsck-y-nope.png" alt="FSCK -y didn't help." width="260" height="34" class="blog-image" >}}<br />
Yeah... that was a no-go.</p>
<p>My iMac&#39;s hard drive was recently borked (I was getting node errors and i/o errors when I ran fsck in single-user mode, and I couldn&#39;t format and reinstall OS X), so I had to replace it. Rather than spend a few hundred dollars to get the drive replaced, or using an external FireWire drive to boot the iMac, I decided to replace the drive with a larger/faster model myself.</p>
<p class="rtecenter">{{< figure src="./imac-guts-exposed.jpg" alt="iMac - Guts Exposed" width="500" height="312" class="blog-image" >}}<br />
The 24&quot; iMac is large. VERY large. I can&#39;t imagine repairing the 27&quot;!!</p>
<p>I used the instructions found on <a href="http://www.amfiteatar.org/content/view/155/57/lang,en/">the Amfiteatar website</a> to compile my more condensed instructions here. I won&#39;t go into any gory details of hard drive types, speeds, recommendations, etc. I&#39;ll simply inform you of my decision to use a <a href="http://www.amazon.com/dp/B0088PUEPK/?tag=mmjjg-20">1 TB WD Caviar Black drive (7200 rpm, 32 MB cache)</a>. I don&#39;t need a ton of storage space on the internal drive, as I have multiple externals for different uses.</p>
<p class="rtecenter"><object width="640" height="385"><param name="movie" value="http://www.youtube.com/v/tfQx-kpbL7o?fs=1&amp;hl=en_US&amp;rel=0&amp;hd=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/tfQx-kpbL7o?fs=1&amp;hl=en_US&amp;rel=0&amp;hd=1" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="640" height="385"></embed></object></p>
<!--break-->
<h3>Tools Required</h3>
<ul>
<li>#1 Phillips screwdriver (<a href="http://www.amazon.com/gp/product/B0000302VX/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B0000302VX&linkCode=as2&tag=mmjjg-20">here's a nice one</a>)</li>
<li>Multiple Torx size screwdrivers (I think T6 &amp; T8, mostly - just get a multi-tool torx driver like <a href="http://www.amazon.com/gp/product/B001T5MNVY/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B001T5MNVY&linkCode=as2&tag=mmjjg-20">this one</a>)</li>
<li>Jeweler&#39;s-size flat-head screwdriver (for help in prying cables loose)</li>
<li>Suction cups (some good, strong ones &mdash; 1.5-2&quot; diameter preferred - I used <a href="http://www.amazon.com/gp/product/B002OJC1J8/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B002OJC1J8&linkCode=as2&tag=mmjjg-20">these</a>)</li>
</ul>
<h3>Repair Guide</h3>
<p><span style="color:#ff0000;"><strong>CAVEAT</strong></span>: I take no responsibility for your computer getting messed up as a result of your own repair work. This whole operation is rather tricky, and could result in your iMac being inoperable. Consider yourself warned ;-)</p>
<p>Here&#39;s the simple man&#39;s guide for replacing the hard drive inside an Intel iMac (the ones with the glass-covered screens) &ndash; refer to the video above for illustration:</p>
<ol>
<li>Clear a large, flat surface, either on a table top or the ground, and consider using a large towel or something soft and large on which to place parts as you go. Also have a little tray or paper and scotch tape ready for the screws you&#39;ll be removing.</li>
<li>With the iMac laying down facing up (you should see the screen), secure two large suction cups (2&quot; or larger is good) on opposite corners of the screen, and pull up to get the glass removed via its magnetic mount. NOTE: Be careful when lifting the glass&mdash;glass can crack pretty easily!</li>
<li>Remove the 12 torx screws around the border of the screen with a Torx wrench. Place them either in a bin or on a piece of paper in the order in which you removed them.</li>
<li>Lift up on the bottom of the iMac and remove the RAM/memory access door.</li>
<li>Pull up slowly along the top of the casing, being careful to not yank on the small cable that goes between the aluminum and the main case, then pull the case towards the iMac&#39;s base a little bit to get the frame detached from the bottom casing. Place the aluminum frame upside down above the main case to get it out of the way.</li>
<li>Remove the 8 screws on the left and right side of the LCD display assembly using a Torx wrench. Set them aside as in step 3.</li>
<li>Remove the screws from the right side display connector, and carefully pry the connector loose (refer to illustration below).<br />
{{< figure src="./iMac-LCD-Connections.jpg" alt="iMac LCD Display Connections - to Disconnect" class="blog-image" >}}</li>
<li>Pry the LCD temperature connector loose (the rightmost of two connectors to the right of the left-side speaker assembly&mdash;it&#39;s labeled on the motherboard) (refer to illustration above).</li>
<li>Pull up on the LCD assembly slowly and carefully, starting from the right side and bottom. Pull it completely off the main casing, but don&#39;t set it aside until you&#39;ve pulled back some of the plastic protective tape over the power connector on the backside of the display and pried loose the LCD&#39;s power connector.</li>
<li>Pull off the hard drive temperature monitor transistor (the little cover for it is glued on with some light adhesive) and let it hang away from the hard drive.</li>
<li>Pull the plastic bar (it will require some force, but be careful to not damage anything inside!) on the top side of the hard drive toward the hard drive to release the drive from its carrier assembly, then slide the hard drive towards the top of the computer. Pry loose the two cables (power and SATA data) from the old drive.</li>
<li>Unscrew the hard drive mounting assembly (two pins on one side, and two screws holding a bracket on the other) from the old drive, and attach it to the new drive.</li>
<li>Place the new drive in the computer, and follow these directions in reverse to make your computer new again. One thing you might want to do while putting everything back together is have an air duster handy so you can blow off any particles that collect on the LCD (if you&#39;re in a dusty environment, this is a MUST).</li>
</ol>
<p>That&#39;s it! You should have a happily-upgraded iMac now, with a much better drive. If you have any comments, suggestions, or questions, please post them below.</p>
