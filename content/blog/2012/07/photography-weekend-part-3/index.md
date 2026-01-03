---
nid: 2113
title: "Photography Weekend Part 3 - Backup Strategies and Disaster Preparedness"
slug: "photography-weekend-part-3"
date: 2012-07-29T19:09:41+00:00
drupal:
  nid: 2113
  path: /blog/2012/photography-weekend-part-3
  body_format: full_html
  redirects: []
tags:
  - backup
  - disaster avoidance
  - photo-weekend
  - photography
  - steubenville
---

See previous posts:

<ul>
	<li><a href="/blog/2012/photography-weekend-part-2">Photography Weekend Part 2 - Taking Photos</a></li>
	<li><a href="/blog/2012/photography-weekend-part-1">Photography Weekend Part 1 - Packing My Gear</a></li>
</ul>

<h3>An Ounce of Prevention...</h3>

When you work on a project where every piece of work (in this case, every photograph) needs to be cataloged, backed up, and sent to production as it's created, you have to plan things out pretty well in advance, but also be ready to fix problems and adapt to difficulties as they arise.

During my weekend of photography at Steubenville St. Louis, I was quite prepared for most difficulties that could crop up in photography:

<ul>
	<li>I had a <strong>second/backup camera body</strong>: I always bring two cameras to important events. Some photographers bring three. Even though my backup body was a lowly D40, it's a heck of a lot more effective for low-light images and quality picture making than my iPhone! Plus it will still use my nice lenses without trouble.</li>
	<li>I had <strong>seven extra 8-16 GB SD cards</strong>: Plan on at least one failing or having write errors at some point. Get the photos off of it, and ditch that card.</li>
	<li>I had an <strong>external hard drive</strong> that I would keep a backup copy of every photo I took in an Aperture vault.</li>
	<li>I set the camera to store the RAW file on the primary card, and a JPEG on the secondary (Eye-Fi), so if one card failed while shooting, the second was a backup.</li>
</ul>

Because of this preparation, I always had at least <strong>two copies of every photo I took</strong>, and I wouldn't erase an SD card and re-use it until a photo was completely processed, and backed up three times (once on main drive, once on backup drive, and once on Flickr). (Also, after the event, I burned three DVDs—one for my archives, and two for the client).

<h3>...is worth a pound of Cure</h3>

Of course, things can and do go wrong. I had two annoying experiences that I had to deal with—one which was (relatively) minor, the other which could've been quite a disaster!

<h4>Eye-Fi Failure (Flaky Connections)</h4>

{{< figure src="./eye-fi-in-d7000.jpg" alt="Eye-Fi Pro X2 in D7000 2nd slot" width="300" height="205" class="blog-image" >}}I was having some interesting problems with my <a href="http://www.amazon.com/gp/product/B002UT42UI/ref=as_li_ss_tl?ie=UTF8&amp;tag=mmjjg-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B002UT42UI">Eye-Fi Pro X2 SD card</a> during the full Saturday of shooting that were tough to fix; the major problem was a 'write error' bug that seemed to crop up every 200-300 shots. The card would not allow any further writing until I ran back to the computer, dumped off the photos, and formatted it in-camera.

Well, one of the times I formatted the card in my laptop instead of the camera, and I think the card lost some of its proper WiFi settings, because I couldn't get it to connect to the Internet through my iPhone anymore. It took an hour or two of debugging and plugging, unplugging, formatting, etc. before I could get it to work reliably in my D7000.

But, during that time, I switched over to using a second normal SD card while shooting, still with JPEGs, so I could quickly upload them to Flickr (albeit, manually) when I ran back to my laptop.

It was annoying, but after I got the card fixed again, not too much of a bother.

<h4>Memory Failure (Formatting woes)</h4>

These are the mistakes for which you really need to watch out! I purposely follow a very routine workflow when I dump pictures to my computer, and if I get interrupted, I can easily forget which card is active, which card I can format and re-use, etc.

One time, when I was concentrating on a conversation with someone else while importing, I mistakenly placed the wrong SD card in my camera's number 1 slot and hit the 'Format' button, erasing about 60 RAW pictures from a pretty important event that I hadn't yet imported.

Of course, I still had the JPEGs on the Eye-Fi, but having the RAW files for this particular event was important, because the contrast required post processing and some color balancing (which are a pain on lossy JPEGs).

<p style="text-align: center;">{{< figure src="./sd-cards-pileup.jpg" alt="SD and CF Flash Memory Cards in pile" width="500" height="331" class="blog-image" >}}
You never know which one will fail next! (<em>D7000, 17-55mm DX, ISO 1600, f/2.8, 1/50</em>)</p>

Luckily, I realized what I did right away, and quickly pulled the card from the camera (after the format), and set it on the desk with a label of 'DO NOT USE'. You see, when you format a memory card, the actual files aren't written over/removed, just the references on the card's file system. So, knowing that I could later come back and restore the files (hopefully—nothing's a given when it comes to file recovery!), I set down the card with the hope of restoring the photos I just formatted later. (If I would've used the card again, the missing files would've been written over, irrecoverable forever).

When I finally had time to restore the photos, I was going to re-purchase an app like <a href="http://www.datarescue.com/photorescue/">PhotoRescue</a>, which I had sucessfully used from time to time to restore photos. But, since I am comfortable working with lower-level tools, and knew there had to be an open source solution to this problem, I dug around and found the excellent tool <strong><a href="http://www.cgsecurity.org/wiki/PhotoRec">PhotoRec</a></strong>, which is GPL-licensed, but requires some knowlege of using the command line (tutorial coming soon!). No problem, though, and after scrubbing the SD card, it came up with every missing photo in the .nef/RAW format. Very nice!

<h3>Lessons Learned</h3>

I wouldn't be a very smart photographer if I didn't try to change my ways to make things better after having these two problems. I've decided to try to (within reason) have enough memory cards so I can shoot an entire event/weekend without needing to format any—and then at the end of the event, after all photos have been processed, I can wipe the cards.

I can't do much about the Eye-Fi troubles I was having, but I can simply hope that Eye-Fi improves its software so it's not quite as fickle, and Nikon and other camera manufacturers work on better solutions for photo storage, transfer, and backup in the camera bodies themselves.

Besides these two problems, I didn't really have a stressful weekend—but much of that was because I came prepared for the worst! Always do the same, and your photography experiences will be more enjoyable.
