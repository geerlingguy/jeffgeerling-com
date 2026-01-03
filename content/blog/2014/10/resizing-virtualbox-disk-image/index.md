---
nid: 2468
title: "Resizing a VirtualBox Disk Image (.vmdk) on a Mac"
slug: "resizing-virtualbox-disk-image"
date: 2014-10-20T16:27:55+00:00
drupal:
  nid: 2468
  path: /blogs/jeff-geerling/resizing-virtualbox-disk-image
  body_format: full_html
  redirects: []
tags:
  - disk
  - resize
  - vagrant
  - vdi
  - virtualbox
  - vmdk
---

Every now and then, a project I'm managing through Vagrant (using either a box I built myself using Packer, or one of the many freely available <a href="http://www.vagrantbox.es/">Vagrant Boxes</a>) needs more than the 8-12 GB that's configured for the disk image by default. Often, you can find ways around increasing the disk image size (like proxying file storage, mounting a shared folder, etc.), but sometimes it's just easier to expand the disk image.

Unfortunately, VBoxManage's <code>modifyvm --resize</code> option doesn't work with .vmdk disk images (the default format used with Vagrant boxes in VirtualBox). Luckily, you can easily clone the image to a .vdi image (which can be resized), then either use <em>that</em> image, or convert it back to a .vmdk image. Either way, you can expand your virtual disk image however large you want (up to the available free space on your physical drive, of course!).

Here's how:

<h2>1 - Convert and resize the disk image</h2>

First, <code>vagrant halt</code>/shutdown your VM, then in Terminal or on the command line:

```
# Clone the .vmdk image to a .vdi.
vboxmanage clonehd "virtualdisk.vmdk" "new-virtualdisk.vdi" --format vdi
# Resize the new .vdi image (30720 == 30 GB).
vboxmanage modifyhd "new-virtualdisk.vdi" --resize 30720
# Optional; switch back to a .vmdk.
VBoxManage clonehd "cloned.vdi" "resized.vmdk" --format vmdk
```

The third step is not absolutely required—you could update your VM in VirtualBox or via the command line to use the .vdi, and then discard your original .vmdk—but it's simple enough to switch back to a .vmdk, and doesn't require any further configuration changes.

<h2>2 - Resize the disk image using gparted</h2>

<ol>
<li><a href="http://gparted.org/download.php">Download the gparted .iso</a></li>
<li>Mount the .iso as a CD/DVD drive in VirtualBox for your VM</li>
<li>Start your VM, and on the boot screen, hit F12 to select the gparted iso image for boot</li>
<li>Follow the instructions for gparted's startup, then in the GUI (or on the command line) <a href="http://askubuntu.com/a/269072">resize the partition</a> on your new disk image so it uses all the unallocated free space).</li>
</ol>

Now shut down the VM again, unmount the gparted ISO, and reboot with your newly-expanded disk image.

<em>Thanks to <a href="http://stackoverflow.com/a/11659046/100134">this SO post</a> and <a href="http://blog.lenss.nl/2012/09/resize-a-vagrant-vmdk-drive/">this post</a> for the details.</em>
