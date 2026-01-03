---
nid: 2359
title: "\"You have inserted a Blank DVD\" \u2013 Opening discs from Windows on a Mac"
slug: "you-have-inserted-blank-dvd-\u2013"
date: 2012-03-14T17:16:00+00:00
drupal:
  nid: 2359
  path: /blogs/jeff-geerling/you-have-inserted-blank-dvd-–
  body_format: full_html
  redirects: []
tags:
  - burn
  - cd
  - compatibility
  - disc
  - dvd
  - mac
  - windows
---

A few times in my life, I've received DVD-Rs or CD-Rs that a Windows user burned and gave to me, and popped them in my Mac, only to receive a message, "You inserted a blank DVD [or CD]. Choose an action from the pop-up menu or click Ignore."

<p style="text-align: center;">{{< figure src="./inserted-blank-dvd-disc.png" alt="" width="521" height="309" >}}</p>

The problem is, there's no way to read the data from the disc on the Mac; you can try burning stuff onto it or simply ignoring it, but you can't read the pictures off the disk. I checked the data side of the disc, and, sure enough, there's a different color band where data was written. But it's a no-go on the Mac.

The problem here is that Microsoft/Windows decided to implement it's 'Drag to Disc' file copying feature in a somewhat annoying way; people with Windows computers can copy individual files to a burnable disc, eject the disc, and put it back in and copy more files to it. But they can't delete files from the disc, and this kinda breaks the way write-once media is supposed to work. (To Windows users: Make sure that you finalize/burn the disc completely before you hand it off to someone. Otherwise only Windows users can read the files).

So, the only real way to get files off discs like this is to use the CD/DVD in Windows. I have <a href="http://www.amazon.com/gp/product/B005FDK7J6/ref=as_li_ss_tl?ie=UTF8&tag=mmjjg-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B005FDK7J6">Parallels Desktop</a> installed on my Mac (<a href="http://www.amazon.com/gp/product/B005LTV8G0/ref=as_li_ss_tl?ie=UTF8&tag=mmjjg-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B005LTV8G0">VMWare Fusion</a> works just as well), and I can load the CD/DVD into Windows XP and read the files off of it there, copying them over to a Shared folder on my Mac. The only other way to get the files would be to find a Windows PC, insert the disc, and copy the files off to a flash drive, or to finalize/burn the disc using Windows.

On the Mac, when you eject any burnable media to which you have copied files, the Mac requires you to completely burn/finalize the disc, so this isn't a problem for Mac users.
