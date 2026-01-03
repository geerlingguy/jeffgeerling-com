---
nid: 43
title: "Secure Your Files: Create an Encrypted Disk on Which to Store Private Files"
slug: "secure-your-files-create"
date: 2010-05-02T03:28:06+00:00
drupal:
  nid: 43
  path: /articles/computing/2010/secure-your-files-create
  body_format: full_html
  redirects: []
tags:
  - articles
  - encryption
  - file management
  - security
---

<p>{{< figure src="./secure-disk-image.png" alt="Secure Disk Image" class="blog-image" >}}The popularity of &#39;cloud file management&#39; software such as Dropbox and SugarSync has made me re-evaluate my security practices for files on my computers; in the past, I have not put any of my private files (for instance, files with sensitive passwords, or scans of important legal documents) on my shared folders (Dropbox, iDisk, etc.), but I finally came up with an ideal solution to storing and syncing these files. It&#39;s like using FileVault, but without the extra overhead of securing <em>every file</em> in your home directory.</p>
<p>I have created a &#39;Secure Disk Image&#39; (.dmg file) using Apple&#39;s Disk Utility (built into Mac OSX) that uses a password and 128-bit encryption for any files stored inside. I simply store that .dmg file on my Dropbox (or whatever other shared folder/system I&#39;m using), and when I need a file inside, I open the .dmg file and grab the file, then when I&#39;m finished, I eject the drive.</p>
<p>Here&#39;s how you can make your own encrypted .dmg file:</p>
<ul>
<li>Open Disk Utility (in Applications&gt;Utilities)</li>
<li>Click the &#39;Image&#39; menu, select &#39;New&#39; and choose &#39;Create Image...&#39;</li>
<li>In the window that pops up, choose what size you want (you can choose &#39;custom&#39; if you want and enter whatever amount of space you&#39;ll need), make sure &#39;AES 128 (recommended)&#39; is selected next to &quot;Encryption:&quot;, make sure &quot;Format:&quot; is &#39;read/write&#39;</li>
<li>Type in a name, select a location (anywhere on your HD), then click the &#39;Create&#39; button</li>
<li>The image will be created (as a file), and a virtual &#39;drive&#39; (white thing) will mount on your Desktop. Copy files you want protected onto this &#39;drive&#39;, and when you are finished (and want it password protected), drag the white &#39;drive&#39; from your Desktop to the trash</li>
<li>Every time you want to re-access the files, double click on the disk image wherever you created it, and it will ask you for your password and then mount the white &#39;drive&#39; on your desktop</li>
</ul>
<p>Note: <strong>Always make sure you eject the disk image when you&#39;re finished</strong>, or you could possibly mess up the synchronization of the disk image from computer to computer.</p>
