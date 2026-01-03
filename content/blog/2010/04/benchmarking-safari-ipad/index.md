---
nid: 1875
title: "Benchmarking Safari on the iPad"
slug: "benchmarking-safari-ipad"
date: 2010-04-06T16:35:08+00:00
drupal:
  nid: 1875
  path: /blog/2010/benchmarking-safari-ipad
  body_format: full_html
  redirects: []
tags:
  - benchmarks
  - css
  - html5
  - ipad
  - javascript
  - standards
  - sunspider
  - testing
---

<p>
	Since purchasing the iPad, I&#39;ve constantly been amazed by how fast everything works&mdash;switching between large apps is no longer a game of roulette, and browsing the web is a breeze.</p>
<p>
	I ran some tests on Safari on my iPad, just to see how things compare to my MacBook Pro...</p>
<h3>
	SunSpider Javascript Benchmark</h3>
<p>
	Here&#39;s the screenshot from my iPad (14068.6ms):</p>
<p class="rtecenter">
	{{< figure src="./sunspider-ipad.png" alt="Sunspider Results - iPad" class="imagecache-article-image-large blog-image" >}}</p>
<p>
	And from my Mac (406.8ms):</p>
<p class="rtecenter">
	{{< figure src="./sunspider-macbook-pro.png" alt="Sunspider Results - Macbook Pro" class="imagecache-article-image-large blog-image" >}}</p>
<p>
	The MacBook Pro (2.53 Ghz 15&quot; with 4 GB of RAM) is about 34x faster than the iPad in raw JavaScript performance... not too surprising, but I&#39;d guess this margin will be trimmed in the next five years, when everyone&#39;s carrying around a tablet :-)</p>
<h3>
	Acid3 Test</h3>
<p>
	Here&#39;s the screenshot from my iPad (took about 5 seconds):</p>
<p class="rtecenter">
	{{< figure src="./acid3-ipad.png" alt="Acid3 Results - iPad" class="imagecache-article-image-large blog-image" >}}</p>
<p>
	And from my Mac (took about .5 seconds):</p>
<p class="rtecenter">
	{{< figure src="./acid3-macbook-pro.png" alt="Acid3 Results - Macbook Pro" class="imagecache-article-image-large blog-image" >}}</p>
<p>
	It looks like, in terms of raw power, the iPad isn&#39;t anything amazing, but it isn&#39;t nearly as slow as my iPhone (iPhone took SDFJSOIFJD ms). On most sites, I don&#39;t notice any lag while browsing on the iPad. Every once in a while a JS-heavy page takes about 2-3 extra seconds to load up all its widgets, but this is definitely tolerable. The decision to ditch my personal laptop is getting easier and easier...</p>
<h3>
	The Bottom Line</h3>
<p>
	Just basing things off the SunSpider test on Safari across my Mac, iPhone and iPad, you can see a very large gap between a &#39;desktop&#39; Mac vs. the iPhone OS devices. This is understandable, as the iPad and iPhone are built for a completely different purpose than a laptop&mdash;they are not &#39;desktop replacement&#39; computers, but rather mobile computing devices.</p>
<ul>
	<li>
		iPhone (Cortex 600 Mhz A8): <strong>17002.6 ms (baseline)</strong></li>
	<li>
		iPad (Apple 1 Ghz A4): <strong>14068.6 ms</strong></li>
	<li>
		MacBook Pro (2.53 Ghz Intel Core 2 Duo): <strong>406.8 ms</strong></li>
</ul>
<p>
	<strong>Also be sure to check out my comprehensive <a href="/reviews/2010/review-apples-ipad-32gb-tested">review of Apple&#39;s iPad</a>.</strong></p>
