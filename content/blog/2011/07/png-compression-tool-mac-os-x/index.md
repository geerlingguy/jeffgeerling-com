---
nid: 2329
title: "PNG Compression Tool for Mac OS X Lion"
slug: "png-compression-tool-mac-os-x"
date: 2011-07-22T23:40:58+00:00
drupal:
  nid: 2329
  path: /blogs/jeff-geerling/png-compression-tool-mac-os-x
  body_format: full_html
  redirects: []
tags:
  - compress
  - png
---

Since the main use I have for PNG image files is as website graphical elements (button backgrounds, background images, style elements, etc., and they are usually loaded on every page of a website I design, it's important for me to be able to compress every byte out of the file that is possible. Most utilities that generate PNGs (besides the latest Photoshop CS5 edition, it seems) like to add about 5-15% of overhead to the file that actually doesn't make the image higher quality.

For the longest time, I had a great relationship with the simple <a href="http://www.macupdate.com/app/mac/17768/pngcrusher">PNGCrusher</a> app. Just drag an image over the icon, and presto! The file goes from something like 7,000 bytes to 6,000 bytes. Sadly, though, Mac OS X Lion stopped supporting Rosetta / PowerPC apps, and PNGCrusher hasn't been updated in a very long time. So, after looking around for a time, I finally found <a href="http://www.kainjow.com/pngshrink.htm">PNGshrink</a>, by an independent Mac developer <a href="http://www.kainjow.com/">kainjow</a>, and it seems to work exactly the same way (nice!), and be compiled for 10.6 or later, Intel only... it's actually a bit faster for larger PNGs than PNGCrusher was, which is nice.

The icon's the default OS X app icon, which is ugly, so I just copied PNGCrusher's magic question box icon over to PNGShrink, and all is well.

I thought I'd post this here for my future reference, and for anyone who doesn't want to use the command line to compress a PNG (using something like <a href="http://optipng.sourceforge.net/">OptiPNG</a>).
