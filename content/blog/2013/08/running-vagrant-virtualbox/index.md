---
nid: 2418
title: "Running Vagrant + VirtualBox from an External Drive"
slug: "running-vagrant-virtualbox"
date: 2013-08-07T18:41:00+00:00
drupal:
  nid: 2418
  path: /blogs/jeff-geerling/running-vagrant-virtualbox
  body_format: full_html
  redirects: []
tags:
  - development
  - space
  - ssh
  - vagrant
  - virtualbox
---

I have a MacBook Air with a 128 GB SSD, so I'm always in a bit of a crunch for space on my hard drive. Developing with local VMs provisioned by Vagrant and VirtualBox makes my Drupal (and other) development experience great, but it also quickly fills up the (tiny amount of) remaining space on my SSD!

Here's how you can move your Vagrant files and VirtualBox VMs out of your home folder onto an external hard drive:

<ol>
<li>Copy the <code>.vagrant.d</code> folder from your home folder (<code>~/.vagrant.d</code>) to your external drive (I renamed the folder to <code>vagrant_home</code>:
<code>cp -R ~/.vagrant.d /Volumes/[VOLUME_NAME]/vagrant_home"</code></li>
<li>Delete the <code>.vagrant.d</code> folder from your home folder:
<code>rm -rf ~/vagrant.d</code></li>
<li>Edit your <code>.bash_profile</code> file, and add the following line (example for Mac OS X):
<code>export VAGRANT_HOME="/Volumes/[VOLUME_NAME]/vagrant_home"</code></li>
<li>Open VirtualBox, go to Preferences, and set the Default Machine Folder to a location on your external hard drive (I created a new folder called 'VirtualBox VMs').</li>
</ol>

At this point, if you download new base boxes, or provision new VMs, they should be on your external drive. (This assumes that you didn't have any existing VMs that you needed to move; in that case, read <a href="http://emptysqua.re/blog/moving-virtualbox-and-vagrant-to-an-external-drive/">Moving VirtualBox and Vagrant to an external drive</a>.

<h2>Caveats</h2>

Unfortunately, there are a couple of downsides to storing VMs externally like this:

<ul>
<li>You have to have your hard drive plugged in at all times when running your VMs. (A quick <code>vagrant suspend</code>, at a minimum, is required before unmounting a drive).</li>
<li>You will need to set the VAGRANT_HOME variable differently for home and work if you use different drives at home and work.</li>
</ul>

One more note: if you're on a Mac or Linux machine, make sure you <a href="http://docs.vagrantup.com/v2/synced-folders/nfs.html">use NFS instead of the native folder syncing method</a>. When running a drupal codebase with thousands of files under a shared directory, you'll easily notice at least a 10x or 100x speedup!
