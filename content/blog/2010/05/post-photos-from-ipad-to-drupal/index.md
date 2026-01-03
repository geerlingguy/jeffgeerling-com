---
nid: 47
title: "Post Photos/Images to Your Drupal Site from the iPad"
slug: "post-photos-from-ipad-to-drupal"
date: 2010-05-14T00:19:52+00:00
drupal:
  nid: 47
  path: /articles/web-design/post-photos-from-ipad-to-drupal
  body_format: full_html
  redirects: []
tags:
  - articles
  - blogs
  - dropbox
  - drupal
  - drupal planet
  - ipad
  - photography
---

<p>Now that I have effectively replaced my laptop with an iPad, I need an easy/quick way to post a photo or two from my iPad to my blog. I use <a href="http://itunes.apple.com/us/app/photogene-for-ipad/id363448251?mt=8">Photogene</a> as a simple Photoshop replacement on the iPad (it actually works pretty well, for being limited to 256 MB of RAM and a 1024x768 display).</p>
<p>I originally tried using an FTP program to transfer the file to my website, into a drop box folder I created, but <a href="http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=364869840&amp;cc=us&amp;mt=8&amp;alreadyRedirected=1">FTPWrite</a>, one of the very few FTP apps for the iPad, doesn&#39;t support uploading from my photo library. Not wanting to pay for any more weak FTP editors until Coda or something equivalent is released for the iPad, I decided to go about this task in a rather unorthodox way. Here&#39;s how I post photos to my Drupal site from my iPad:</p>
<h3>Prerequisites</h3>
<p>On your iPad:</p>
<ul>
<li><a href="https://www.dropbox.com/"><strong>Dropbox</strong></a> - This app/service allows (free or for pay) you to upload a photo from your library and quickly grab a link to the uploaded file (you&#39;ll need to make sure you use the &#39;Public&#39; folder&mdash;other folders will throw a 405 HTTP error... but I&#39;m getting ahead of myself).</li>
<li><strong>Safari</strong> - But you already have this. No worries.</li>
</ul>
<p>On your Drupal site:</p>
<ul>
<li><strong><a href="http://drupal.org/project/filefield">FileFile</a> + <a href="http://drupal.org/project/imagefield">ImageField</a></strong> - set up an imagefield on one of your content types, as you normally would.</li>
<li><strong><a href="http://drupal.org/project/filefield_sources">FileField Sources</a></strong> - An excellent module which will allow you to import an image from a remote URL.</li>
</ul>
<h3>Posting the Image</h3>
<p>Here&#39;s how you get a photo from your iPad to your Drupal site (on any kind of content type)&mdash;this presumes you have a photo on the iPad already (I&#39;m not going to cover getting the photo from your camera or iPhone to the iPad&#39;s photo library&mdash;all you need is the <a href="http://store.apple.com/us/product/MC531ZM/A">iPad Camera Connection Kit</a>).</p>
<ol>
<li>Open up Dropbox on your iPad, and navigate to the &#39;Public&#39; folder.</li>
<li>Tap the little &#39;+&#39; icon at the bottom of the file list, and click the button to add an &#39;Existing Photo or Video.&#39;<br />
{{< figure src="./upload-to-dropbox-existing.jpg" alt="Tap the Choose Existing Photo or Video button." class="imagecache-article-image-large blog-image" >}}<br />
&nbsp;</li>
<li>Select the photo you&#39;d like to upload, and wait for it to upload.</li>
<li>Tap the photo you just uploaded, then tap the &#39;link&#39; icon, and select &quot;Copy Link to Clipboard.&quot;<br />
{{< figure src="./tap-upload-button.jpg" alt="Copy Link to Clipboard in Dropbox." class="imagecache-article-image-large blog-image" >}}<br />
&nbsp;</li>
<li>Now switch over to Safari, visit your Drupal site&#39;s content type with the ImageField / FileField Sources.</li>
<li>Tap on &#39;Remote URL,&#39; and tap in the URL field. Tap once again to paste the URL you copied from Dropbox, then click &#39;Transfer&#39; to put the file on your Drupal site.<br />
{{< figure src="./filefield-remote-url-transfer.jpg" alt="Tap Remote URL then transfer the file to your site." class="imagecache-article-image-large blog-image" >}}</li>
</ol>
<p>That&#39;s it! You have successfully beaten Mobile Safari&#39;s file uploading limitations, albeit in a less-than-ideal fashion. Someday Mobile Safari might simply allow for direct file uploads, in which case, steps 1-4 could be taken out of the process. Bu don&#39;t hold your breath :-/</p>
