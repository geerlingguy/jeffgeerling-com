---
nid: 56
title: "Removing a Stuck Disc (CD/DVD) from a Mac - EVERY Way Possible"
slug: "removing-a-stuck-disc-cddvd-a"
date: 2011-01-23T04:15:36+00:00
drupal:
  nid: 56
  path: /articles/computing/2011/removing-a-stuck-disc-cddvd-a
  body_format: full_html
  redirects:
    - /computing/2011/removing-a-stuck-disc-cddvd-a
aliases:
  - /computing/2011/removing-a-stuck-disc-cddvd-a
  - /articles/computing/2011/removing-a-stuck-disc-cddvd-a
tags:
  - cd
  - drive
  - dvd
  - eject
  - hardware
  - imac
  - mac
  - mac mini
  - macbook
  - slot-load
---

<p>{{< figure src="./CD.JPG" alt="CD" class="blog-image" >}}Most of the time, I&#39;m extremely happy with Apple&#39;s decision to make all their physical media (CD/DVD) drives slot-loading, as it means there&#39;s one less part to accidentally break off my Mac, and it just looks so darn pretty! But every now and then, I have a hellish experience with the drive. This usually happens when:</p>
<ul>
<li>A CD/DVD disc is warped or really thick (like most discs with homemade labels)</li>
<li>I&#39;m given a mini CD (business card size) or DVD (this rarely happens anymore)</li>
<li>A CD/DVD is way out of balance... usually it&#39;s just slightly warped</li>
</ul>
<p>That&#39;s the hardware side. Sometimes, I just want to get a dratted disc out of the computer, but dragging it to the trash, or pressing the &#39;Eject&#39; key won&#39;t work. Often a dialog pops up and says &quot;the disc is in use&quot; (but it doesn&#39;t specify what application is using it!), or worse, there is no error&mdash;the disc just won&#39;t come out.</p>
<p>Here are the steps I usually take in trying to eject a CD or DVD&mdash;in order from least likely to damage the disc and/or my Mac, to most likely... always try the steps in order!</p>
<!--break-->
<h3>Plan A - Disc Doesn&#39;t Eject after Dragging to Trash</h3>
<ol>
<li>Try waiting a minute or so, and do it again.</li>
<li>Press the &#39;Eject&#39; key on your keyboard.</li>
<li>Quit all open applications, and restart the Finder (Apple menu, Force quit, then restart Finder), and try again.</li>
<li>Open Disk Utility, click on the CD in the list of drives, and click Eject.</li>
<li>Open Terminal, and enter in the following command: <code>drutil tray eject 0</code> (then press return)</li>
<li>Restart the computer and hold down the Mouse until the disc is ejected. (NOTE: Use a USB mouse to do this - Bluetooth mice might not always be detected during Mac startup).</li>
</ol>
<h3>Plan B - Disc is Physically Stuck in Drive</h3>
<p>MAKE SURE you&#39;ve tried every other solution above, and don&#39;t hold me responsible for any damage done to your drive as a result of your following these directions... any of the following steps could (and probably will) cause damage to your disc and/or your Mac, even if done carefully!</p>
<h4>Method 1 - The Sticky Credit Card</h4>
<p>I originally learned about this technique from <a href="http://www.ecstaticist.com/mac/how-i-removed-a-cd-stuck-in-my-macbook-pro/comment-page-5/">this post on Ecstaticist</a>. Basically, you use a credit card and some tape to try to grip the CD hard enough and use that friction to pull it out of your Mac:</p>
<p class="rtecenter">{{< figure src="./tape-and-credit-card.jpg" alt="Double-sided tape and a credit card" width="400" height="241" class="blog-image" >}}<br />
Tools of the Trade: Credit card and double-sided tape.</p>
<ol>
<li>Stick a small patch of sticky tape onto a corner of the credit card (it&#39;s a good idea to NOT do this over the magnetic strip...)</li>
<li>Put the credit card just into the drive (through the little dust flap) so you can see a little bit inside the drive. There&#39;s a lever that lets the disc eject. You&#39;ll need to hold the card over that lever, and try to get the sticky tape onto the disc, then pull out the disc with the card.</li>
<li>Profit? It&#39;s a little tricky; you just have to be brave... and maybe use a flashlight to see inside if you can.</li>
</ol>
<p>I sometimes use a mini screwdriver to see inside, as well.</p>
<h4>Method 2 - Screw it&mdash;Break the Disc</h4>
<p>Before trying this method, think long and hard over whether you really want to use the disc you&#39;re trying to remove again... if so, you might want to resort to Method 3 below. If not, go ahead and screw your CD or DVD out of the computer:</p>
<p class="rtecenter">{{< figure src="./cd-removal-tools.jpg" alt="Physical CD Removal Tools" width="400" height="283" class="blog-image" >}}<br />
Tools of the Trade: Mini flat-head screwdrivers (2) and a paperclip. Borked CD shown for scale.</p>
<ol>
<li>Repeatedly try using the &#39;drutil&#39; Terminal command to eject the disc (if it&#39;s not coming out all the way), and try to catch the disc with either a paperclip or flathead screwdriver.</li>
<li>Use a second flathead screwdriver to clamp down on the CD (a tweezers *might* work, but is usually too thick), and then pull out. Try to not damage or scratch your Mac&mdash;It&#39;s a lot more valuable than a disc!</li>
</ol>
<h4>Method 3 - Take Apart the Mac</h4>
<p>If your Mac is still under warranty, consider bringing it in or calling Apple for service. If not, you can attempt to take it apart so you can get to the drive and figure out what&#39;s holding the disc in. This is risky, and there&#39;s no way I can include the steps to do this here... there are far too many different Mac models, with far too many little details in the teardown process.</p>
<p>I only recommend you take apart your own Mac if you have steady hands, are prepared to lose your Mac, and are foolhardy. I am all three, so I&#39;ve done this a few times... and I&#39;ve been lucky :-)</p>
