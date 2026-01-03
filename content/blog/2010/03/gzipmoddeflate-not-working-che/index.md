---
nid: 2270
title: "Gzip/mod_deflate not Working? Check your Proxy Server"
slug: "gzipmoddeflate-not-working-che"
date: 2010-03-23T17:07:27+00:00
drupal:
  nid: 2270
  path: /blogs/geerlingguy/gzipmoddeflate-not-working-che
  body_format: full_html
  redirects: []
tags:
  - apache
  - gzip
  - mod_deflate
  - performance
  - proxy
---

<p>
	Recently, I was troubleshooting performance issues on a few different websites, and was stymied by the fact that YSlow repeatedly reported an F for &quot;Compress components with gzip,&quot; even though online sites like <a href="http://www.gidnetwork.com/tools/gzip-test.php">GIDNetwork&#39;s Gzip test</a> were reporting successful Gzipping of text components on the site.</p>
<p class="rtecenter">
	{{< figure src="./compress-with-gzip-failure.jpg" alt="Gzip Failed" width="500" height="160" class="noborder" >}}<br />
	Yslow results - not very happy.</p>
<p>
	After scratching my head for a while, I finally figured out the problem, hinted at by a comment on a <a href="http://stackoverflow.com/questions/973969/yslow-gives-f-grade-to-files-compressed-with-mod-deflate">question on Stack Overflow</a>. Our work&#39;s proxy server was blocking the &#39;Accept-Encoding&#39; http header that is sent along with every file request; this prevented a gzipped transfer of any file, thus Yslow gave an F.</p>
<p>
	I set up a secure tunnel (using SSH) from my computer to the web server directly, and then reloaded the page in FireFox, and re-ran YSlow:</p>
<p class="rtecenter">
	{{< figure src="./gzip-works.jpg" alt="Gzip Works Again - Grade A" width="500" height="158" class="noborder" >}}</p>
<p>
	Much happier now. I&#39;ve contacted our IT department to see if it&#39;s possible to allow the proxy server to pass through the Accept-Encoding headers, but for now, I&#39;ll know to watch out for false positives on the YSlow test, and check from multiple locations.</p>
