---
nid: 2850
title: "How to upgrade the SSD hard drive in a Dell XPS 13 (9360)"
slug: "how-upgrade-ssd-hard-drive-dell-xps-13-9360"
date: 2018-05-30T16:30:08+00:00
drupal:
  nid: 2850
  path: /blog/2018/how-upgrade-ssd-hard-drive-dell-xps-13-9360
  body_format: markdown
  redirects: []
tags:
  - dell
  - easeus
  - hard drive
  - macrium
  - microsoft
  - nvme
  - partition
  - replacement
  - ssd
  - tutorial
  - windows
  - windows 10
  - xps
---

**June 6, 2018 Update**: I've also posted a video of the SSD replacement process, embedded below:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/xFIE2SKst-s" frameborder='0' allowfullscreen></iframe></div>

I recently purchased a used Dell XPS 13 (model 9360), and I chose to purchase the base option (with 128 GB SSD) since it was cheaper to do that and upgrade the SSD to a larger model (500 GB) aftermarket than to buy a higher model XPS (I bought this model: [WD Blue 3D NAND 500GB PC SSD](https://www.amazon.com/gp/product/B073SBX6TY/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=55e55d1b802491a6a693144ff4ef3f4c)).

I've upgraded drives in many Macs and on Linux PCs over the years, and the process is pretty painless, with a plethora of freely available options for disk cloning (e.g. Disk Utility on macOS, `dd` on Linux or macOS, etc.). But on Windows, it seems there's nothing built-in for cloning or imaging a disk—instead you have to download and/or purchase a utility to help with this process. Annoying, but in the end it worked out, so I won't get too angry about it.

{{< figure src="./tools-for-dell-xps-13-ssd-replacement.jpg" alt="Tools used for Dell XPS 13 SSD replacement - spudger phillips #000 and Torx T5" width="650" height="435" class="insert-image" >}}

<p style="text-align: center;"><em>Tools used: Spudger, #000 phillips screwdriver, T5 Torx screwdriver.</em></p>

I tried both [Macrium Reflect Free](https://www.macrium.com/reflectfree) and [EaseUS Todo Backup](https://www.easeus.com/download/backup.html), and found Macrium Reflect to be a little easier to work with. There are countless tutorials on the Internet for how to do a disk clone, but I wanted to point out the process I used since there were a few gotchas:

  1. I tried cloning the internal drive to my new M.2 SSD mounted inside an SATA-to-NVMe/M.2 adapter, which was then plugged into a USB 3.1-to-SATA adapter... apparently that was one adapter too many, because the clone seemed to fail at random places.
  2. I then cloned the internal drive to a second external USB 3.0 hard drive I had sitting around (this drive was larger than the internal SSD so it had enough space to clone all the partitions).
  3. I created a 'Restore Media' USB boot drive using Macrium Reflect, so I could boot the XPS 13 off of it once I replaced the SSD.
  4. I opened the XPS 13, replaced the NVMe SSD with the new one, and closed it back up.
  5. I plugged in the Restore Media I created in step 3, as well as the USB 3.0 external drive that had the internal drive clone (from step 2).
  5. I booted the XPS 13 and pressed the 'F12' key when the Dell logo appeared, to access the boot menu.
  6. I chose to boot from the Restore Media (a SanDisk USB flash drive).
  7. This booted into Macrium Reflect, where I cloned the USB 3.0 external drive to the new internal drive.
  8. I booted the Dell and let it do it's hardware checks (it seems to have detected that there was a hardware change, so it did some system integrity checks then made a really loud BEEP!).

As an illustration of step 4, here's how easy it is to access the SSD once the back cover is removed:

{{< figure src="./upgraded-500gb-wd-blue-nvme-ssd-inside-dell-xps-13.jpg" alt="Upgraded 500GB WD Blue NVMe SSD inside Dell XPS 13 laptop" width="650" height="435" class="insert-image" >}}

At the end of this process, Windows 10 booted back up just like it was before—including showing me a 128 GB system boot drive!

> **Important Note**: When opening the bottom cover of the XPS 13, there are two **very important** things you should do to make sure you don't break anything:
> 
>   1. Remove the phillips screw under the magnetic 'XPS' cover (just lift that cover to reveal the screw). If you don't... SNAP, it will break!
>   2. Use the spudger or a guitar pick to gently pry apart the case from the _front_ edge of the XPS, then pull up on the _front_ edge. Don't try to pry the cover from the back (where the larger gap is or near the ports), because there are thicker retaining clips back there (see illustration below), and one of them is likely to break if you pry too hard!
> 
> {{< figure src="./retaining-tab-in-bottom-cover-dell-xps-13.jpg" alt="Retaining tab in bottom cover of Dell XPS 13" width="488" height="318" class="insert-image" >}}
> 
> The key is: If you're bending the cover to get it to pop off... you're probably prying up in the wrong place. I wish Dell weren't so aggressive with the retaining clips, but since they are, make sure you pry up the cover _gently_ using a plastic spudger or guitar pick, and do it from the front of the laptop, _not_ the back!

So the next step was to get all the 'Unallocated space' on the end of the new 500 GB SSD to be part of the `C:` OS boot partition. I pressed Windows Key + X to get to Disk Management... then I realized you can't merge partitions unless they are contiguous, and Windows 10's built-in Disk Management utility can't move partitions at all!

Oh well, off to download yet _another_ freeware utility to do a basic system operation... this time I chose [EaseUS Partition Master Free](https://www.easeus.com/partition-manager/epm-free.html), which seemed to be the recommended way based on a bunch of random forum topics.

I opened up the partition Master, then dragged the partitions to the right of the `C:` partition all the way to the right of the 'Unallocated space', so the free space was to the right of the `C:` partition. Then I right clicked on the `C:` partition and chose 'Move/Merge', and merged it with the 'Unallocated space'.

Finally, I hit 'Apply', which required a reboot, and waited for EaseUS to do it's work moving around the partitions and making the larger `C:` partition a reality. After the reboot, the hard rive reports "417 GB free of 454 GB", so it looks like everything worked out in the end!

{{< figure src="./dell-xps-13-new-partition-size.png" alt="Dell XPS 13 NVMe SSD upgrade - 500 GB SSD works" width="650" height="490" class="insert-image" >}}
