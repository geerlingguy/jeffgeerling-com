---
nid: 2362
title: "Running a Windows XP VM in Parallels (Mac) from a USB Flash Drive"
slug: "running-windows-xp-vm"
date: 2012-01-17T23:40:13+00:00
drupal:
  nid: 2362
  path: /blogs/jeff-geerling/running-windows-xp-vm
  body_format: full_html
  redirects: []
tags:
  - flash
  - format
  - parallels
  - performance
  - usb
  - windows
---

I thought I'd post my experience here, for the benefit of others, because I couldn't find a whole lot of information about this specific use of an external USB flash drive.

I have a MacBook Air with a dainty 128GB SSD drive, so I try to keep large files that I rarely use on external drives. I have plenty of external USB and FireWire storage (over 6 TB), and running VMs in either Parallels or VMWare Fusion works great (very highly performant) off any of these external drives.

However, there's no way I'm going to lug around an external hard drive and USB cable (and maybe power adapter) just so I can test things in Internet Explorer (basically, the only use I have for Windows).

<h3>Flash Drive to the Rescue!</h3>

I found a cheap 32GB USB flash drive that only sticks out of my MacBook Air half an inch, and copies at a consistent rate of 30MB/second (which is quite sufficient for most tasks). Also, the little drive should have very good read performance, since it's not a spinning platter. Write speed wouldn't be anything to brag about, but writing shouldn't happen all that often when simply opening up Internet Explorer—I hope!

<h3>...not so fast!</h3>

Anyways, for my first crack, I tried formatting the drive as an ExFAT drive, with a Master Boot Record, thinking it would be nice to also be able to use the drive with the occasional PC I run into... but that provided abysmal performance for a VM in Parallels; right-clicking on the desktop would take seconds to simply pop up the contextual menu (and this was about 10 minutes <em>after</em>&nbsp;the machine had completely finished launching). So, ExFAT was out.

I then reformatted the drive as Mac OS Extended (Journaled) (though I wish I could've formatted it as not journaled, since I could sacrifice data integrity for the little performance boost in this case). I copied the VM back over to the flash drive, and that copy transferred solidly at 10.5 MB/sec (not as good as my HDDs, but still nothing horrible).

This format didn't seem to help too much, either, though. While monitoring Disk Activity in Activity Monitor, I noticed that, any time Windows XP did anything, the read/sec and write/sec statistics both went down to the low-KB range, while CPU usage was almost idle. Memory wasn't really a problem, either.

As a further stress test, I decided to copy a 20 MB file to the flash drive while Windows XP was purring along. The file copy took about 10 seconds, which is way slower than a normal file copy when nothing else is going on (in that case, the copy took a total of 1 second).

<h3>I/O - Miserable</h3>

Tom's Hardware did an excellent story (multi-page, but worth reading) on <a href="http://www.tomshardware.com/reviews/usb-hard-drive,2015.html">flash drive performance</a> (I/O, write speed, read speed, throughput writing and reading over entire drive, etc) vs. an older hard drive's performance. I'm guessing that a lot of the lagginess I was encountering was due to the <a href="http://www.tomshardware.com/reviews/usb-hard-drive,2015-8.html">miserable I/O throughput</a> with complex read/write operations.

So, in the end, it looks like I won't be able to have a true go-anywhere flash-drive-based virtual machine setup... unless maybe something about the way Parallels accesses the data is screwy.

<h3>End notes</h3>

A few other notes about my attempts at getting this to work:

<ul>
	<li>The MacBook Air has two separate USB 2.0 busses: one on the right side port shared with the Bluetooth interface and FaceTime camera, and the other on the left side port that seems independent. I've tried using the drive on both sides, and that didn't make any difference in performance at all. Plus, based on my I/O observations, the USB interface wasn't at all the limiting factor.</li>
	<li>I was going to try formatting the drive as FAT(32), but ExFAT should've been better regardless, so I didn't take the 20 minutes to reformat and recopy the virtual disk.</li>
	<li>I also tried <a href="http://www.codinghorror.com/blog/2005/10/running-xp-with-the-pagefile-disabled.html">disabling Windows XP's pagefile on C:/</a>, but that didn't seem to help at all.</li>
	<li>I've <a href="http://superuser.com/questions/379639/">posted a question on SuperUser</a> asking more about this situation, to see if anyone else has any ideas.</li>
</ul>
