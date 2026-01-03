---
nid: 2285
title: "\"Licensing for this product has stopped working\" - Adobe CS3/CS4 on a Mac"
slug: "licensing-product-has-stopped"
date: 2010-09-19T18:48:07+00:00
drupal:
  nid: 2285
  path: /blogs/jeff-geerling/licensing-product-has-stopped
  body_format: full_html
  redirects: []
tags:
  - adobe
  - creative suite
  - cs3
  - cs4
  - illustrator
  - licensing
  - photoshop
aliases:
  - /blogs/jeff-geerling/licensing-product-has-stopped
   - /blogs/jeff-geerling/licensing-product-has-stopped
---

<p>Recently, I had to recover my iMac from a Time Machine backup and a hard drive replacement (my old drive flaked out&mdash;<a href="http://www.jeffgeerling.com/computing/2010/intel-imac-teardown-and-hard-d">see how I repaired my hard drive here (video included!)</a>).</p>
<p>Upon trying to open any Adobe Creative Suite 3 app (I use Photoshop and Illustrator daily...), I got the following error window:</p>
<p class="rtecenter">{{< figure src="./licensing-stopped-working-adobe-cs3.jpg" alt="Adobe Illustrator - Licensing for this product has stopped working" >}}</p>
<p>I was taken to <a href="http://kb2.adobe.com/cps/401/kb401528.html">this Adobe Support page</a>, which suggests a variety of options for fixing the problem&mdash;all of which didn&#39;t work for me.</p>
<p>The solution, it turns out, was for me to simply delete the entire folder &quot;FLEXNet Publisher&quot; folder at the following location:&nbsp;<strong>/[startup disk]/Library/Preferences/FLEXnet Publisher</strong>.</p>
<p>After I deleted that folder, I opened Adobe Illustrator, and it took me through the activation process (it had save my license key, so all I had to do was click &#39;Next&#39; until the app was working again).</p>
