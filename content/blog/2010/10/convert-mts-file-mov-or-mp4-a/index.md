---
nid: 1979
title: "Convert .MTS file to .MOV or .MP4 on a Mac (for iMovie, etc.)"
slug: "convert-mts-file-mov-or-mp4-a"
date: 2010-10-15T13:06:18+00:00
drupal:
  nid: 1979
  path: /blog/2010/convert-mts-file-mov-or-mp4-a
  body_format: full_html
  redirects: []
tags:
  - conversion
  - handbrake
  - mov
  - mp4
  - mts
  - quicktime
  - video
---

<p>I recently received a few .mts files from a friend. These files are AVCHD high-definition video files from consumer-grade HD video cameras, and they&#39;ve traditionally been a pain to work with.</p>
<p>If you have the files on your camcorder or an SD card from your camcorder, you can just open up iMovie &#39;08 or iMovie &#39;09 and click &#39;import from camera.&#39; It&#39;ll take forever to transcode the files into something iMovie can use, but it will work. If, however, you&#39;re like me and you just have the files (no camcorder), you&#39;ll need to transcode the files before you can edit them or compress them further.</p>
<p>The easiest way to do this, in my experience, is to use <strong><a href="http://handbrake.fr/">Handbrake</a></strong>, the best/simplest transcoding software you can get on the Mac... and <strong>it&#39;s free</strong>! Don&#39;t pay any money for fancy GUI wrappers like the ones you&#39;ll find on mtsconverter.com, applemacvideo.com, mtsconvertermac.biz, etc... these are all ripoffs of ffmpeg, a free and open source video transcoding library.</p>
<p>In Handbrake, click on &#39;Source,&#39; and choose the .mts file you need to convert. It will scan the file, then you can choose what settings you want to use (defaults are fine&mdash;sometimes I switch to &#39;high profile&#39; in the &#39;Toggle Presets&#39; pane), and click Start. A few hours later, you should have a usable file.</p>
<p>While you&#39;re at it, go ahead and download <strong><a href="http://www.videolan.org/vlc/">VLC</a></strong> as well. VLC will let you easily play back .mts files in full-HD glory, as long as your Mac has the power to do so (you need not convert the files first!). VLC also includes some libraries Handbrake can use to do some nice things like convert DVDs to video files on your computer.</p>
<p>There you have it! I just saved you $10-20 and a few hours&#39; time searching on various Mac forums for this answer :)</p>
<p><em>If you liked this post, you might also be interested in reading my workflow for <a href="http://www.jeffgeerling.com/articles/audio-and-video/2010/ripping-movies-blu-ray-and-dvd"><strong>ripping movies from Blu-Ray discs and DVDs</strong>, and getting them to play on all my Apple devices - Apple TV, iPhone, iPod touch, and Mac</a>.</em></p>
