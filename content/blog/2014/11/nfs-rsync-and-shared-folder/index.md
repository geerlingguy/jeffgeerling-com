---
nid: 2475
title: "NFS, rsync, and shared folder performance in Vagrant VMs"
slug: "nfs-rsync-and-shared-folder"
date: 2014-11-24T14:28:18+00:00
drupal:
  nid: 2475
  path: /blogs/jeff-geerling/nfs-rsync-and-shared-folder
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - filesystem
  - nfs
  - performance
  - php
  - rsync
  - vagrant
  - virtualbox
  - xhprof
aliases:
  - /blogs/jeff-geerling/nfs-rsync-and-shared-folder
   - /blogs/jeff-geerling/nfs-rsync-and-shared-folder
---

It's been a well-known fact that using native VirtualBox or VMWare shared folders is a terrible idea if you're developing a Drupal site (or some other site that uses thousands of files in hundreds of folders). The most common recommendation is to switch to NFS for shared folders.

NFS shared folders are a decent solution, and using NFS does indeed speed up performance quite a bit (usually on the order of 20-50x for a file-heavy framework like Drupal!). However, it has it's downsides: it requires extra effort to get running on Windows, requires NFS support inside the VM (not all Vagrant base boxes provide support by default), and is not actually all that fast—in comparison to native filesystem performance.

I was developing a relatively large Drupal site lately, with over 200 modules enabled, meaning there were literally thousands of files and hundreds of directories that Drupal would end up scanning/including on <em>every page request</em>. For some reason, even simple pages like admin forms would take 2+ seconds to load, and digging into the situation with XHProf, I found a likely culprit:

<p style="text-align: center;">{{< figure src="./is_dir-xhprof-drupal.png" alt="is_dir xhprof Drupal" width="451" height="219" >}}</p>

There are a few ways to make this less painful when using NFS (since NFS incurs a slight overhead for every directory/file scan):

<ul>
<li>Use APC and set stat=0 to prevent file lookups (this is a non-starter, since that would mean every time I save a file in development, I would need to restart Apache or manually flush the PHP APC cache).</li>
<li>Increase PHP's <code>realpath_cache_size</code> ini variable, which defaults to '16K' (this has a small, but noticeable impact on performance).</li>
<li>Micro-optimize the NFS mounts by basically setting them up on your own outside of Vagrant's shared folder configuration (another non-starter... and the performance gains would be almost negligible).</li>
</ul>

I wanted to benchmark NFS against rsync shared folders (which I've <a href="https://servercheck.in/blog/rsync-vagrant-15-file-performance-windows-dev">discussed elsewhere</a>), to see how much of a difference using VirtualBox's native filesystem can make.

For testing, I used a Drupal site with about 200 modules, and used XHProf to measure the combined Excl. Wall Time for calls to <code>is_dir</code>, <code>readdir</code>, <code>opendir</code>, and <code>file_scan_directory</code>. Here are my results after 8 test runs on each:

<strong>NFS shared folder:</strong>

<ul>
<li>1.5s* (realpath_cache_size = 16K - PHP default)</li>
<li>1.0s (realpath_cache_size = 1024K)</li>
<li>Average page load time: 1710ms (realpath_cache_size = 1024K, used admin/config/development/devel)</li>
</ul>

*Note: I had a two outliers on this test, where the time would go to as much as 6s, so I discarded those two results. But realize that, even though this NFS share is on a local/internal network, the fact that every file access goes through the full TCP stack of the guest VM, networking issues can make NFS performance unstable.

<strong>Native filesystem (using rsync shared folder):</strong>

<ul>
<li>0.15s (realpath_cache_size = 16K - PHP default)</li>
<li>0.1s (realpath_cache_size = 1024K)</li>
<li>Average page load time: 900ms (realpath_cache_size = 1024K, used admin/config/development/devel)</li>
</ul>

Tuning PHPs <code>realpath_cache_size</code> makes a meaningful difference (though not too great), since the default 16K cache doesn't handle a large Drupal site very well.

As you can see, there's really no contest—just as NFS is an order of magnitude faster than standard VirtualBox shared folders, native filesystem performance is an order of magnitude faster than NFS. Overall site page load times for the Drupal site I was testing went from 5-10s to 1-3s by switching from NFS to rsync!

I've updated my <a href="https://github.com/geerlingguy/drupal-dev-vm">Drupal Development VM</a> and <a href="https://github.com/geerlingguy/acquia-cloud-vm">Acquia Cloud VM</a> to use rsync shares by default (though you can still configure NFS or any other supported share type), and to use a <code>realpath_cache_size</code> of 1024K). Hopefully Drupal developers everywhere will save a few minutes a day from these changes :)

<em>Note that other causes for abysmal filesystem performance and many calls to is_dir, opendir, etc. may include things like <a href="https://www.drupal.org/node/1080330">a missing module</a> or major networking issues. Generally, when fixing performance issues, it's best to eliminate the obvious, and only start digging deeper (like this post) when you don't find an obvious problem.</em>

<h2>Notes on using rsync shared folders</h2>

Besides the comprehensive <a href="https://docs.vagrantup.com/v2/synced-folders/rsync.html">rsync shared folder documentation</a> in Vagrant's official docs, here are a few tips to help you get up and running with rsync shared folders:

<ul>
<li>Use <code>rsync__args</code> to pass CLI options to <code>rsync</code>. The defaults are <code>["--verbose", "--archive", "--delete", "-z"]</code>, but if you want to preserve the files created within the shared folder on the guest, you can set this option, but without <code>--delete</code>.</li>
<li>Use <code>rsync__exclude</code> to exclude directories like <code>.git</code> and other non-essential directories that are unneccessary for running your application within the VM. While not incredibly impactful, it could shave a couple seconds off the rsync process.</li>
</ul>

Not all is perfect; there are a few weaknesses in the rsync model as it is currently implemented out-of-the-box:

<ol>
<li>You have to either manually run <code>vagrant rsync</code> when you make a change (or have your IDE/editor run the command every time you save a file), or have <code>vagrant rsync-auto</code> running in the background while you work.</li>
<li>rsync is currently one-way only (though there's <a href="https://github.com/mitchellh/vagrant/issues/3062">an issue to add two-way sync support</a>).</li>
<li>Permissions can still be an issue, since permissions inside the VM sometimes require some trickery; read up on the <code>rsync__chown</code> option in the docs, and consider passing additional options to the <code>rsync__args</code> to manually configure permissions as you'd like.</li>
</ol>
