---
nid: 2590
title: "rsync in Vagrant 1.5 improves file performance and Windows usage"
slug: "rsync-vagrant-15-file-performance-windows-dev"
date: 2014-03-17T13:57:06+00:00
drupal:
  nid: 2590
  path: /blog/rsync-vagrant-15-file-performance-windows-dev
  body_format: full_html
  redirects:
    - /blog/vagrant-15-makes-team-based-development-1000x
    - /blog/vagrant-15-vastly-improves-filesystem-performance
aliases:
  - /blog/vagrant-15-makes-team-based-development-1000x
  - /blog/vagrant-15-vastly-improves-filesystem-performance
tags:
  - development
  - performance
  - rsync
  - vagrant
  - windows
---

I've been using Vagrant for almost all development projects for the past two years, and for projects where I'm the only developer, Vagrant + VirtualBox has worked great, since I'm on a Mac. I usually use NFS shared folders so I can keep project data (Git/SVN repositories, assets, etc.) on my local computer, and share them to a folder on the VM, and <a href="http://mitchellh.com/comparing-filesystem-performance-in-virtual-machines">not suffer the performance penalty</a> of using VirtualBox's native shared folders.

However, this solution only scaled well to other Mac and Linux users with whom I shared development responsibilities. Windows users were left in a bit of a lurch. To extend an olive branch, I hackishly added SMB support by installing and configuring an SMB share from within the VM only on windows hosts, so Windows devs could mount the SMB share and work on files in their native editors.

This solution was pretty shoddy, as SMB performance isn't amazing (searching across a directory with a couple thousand files is slow). Not only that, since the folder was shared from within the VM <em>to</em> the host machine, Git and other file operations were much easier to do within the machine, meaning Windows users had to learn some linux basics and use <code>vagrant ssh</code> quite often.

While Vagrant 1.5 <em>also</em> <a href="https://www.vagrantup.com/blog/feature-preview-vagrant-1-5-hyperv.html">threw a few bones to Windows users</a> in the form of Hyper-V support and native SMB shared folder support, what really excited me (for both Mac/Linux and Windows use) was <em>rsync</em> shared folder support.

<h2>rsync <del>shared</del> synced folders</h2>

Accessing files on VirtualBox's native VM file system is the fastest way to use complex, file-heavy applications like Drupal. I've tested native shared folders, SMB shared folders (not using Vagrant's method, but the performance should be similarly disappointing), native filesystem storage (the fastest), and NFS shared folders (noticeably slower than native, but not by much, and kludgy to get set up). By far, the simplest and fastest way of handling files in a VM is through use of the native filesystem. But until Vagrant 1.5, this was also a bit kludgy.

With Vagrant 1.5's <a href="https://www.vagrantup.com/blog/feature-preview-vagrant-1-5-rsync.html">rsync synced folder support</a>, setup is easy, performance is blazing fast, one sharing method works on both Mac, Linux, and Windows. The only downsides (and these are minor) is that the initial <code>vagrant up</code> takes a little longer, since the first time it has to <code>rsync</code> your entire shared folder to the VM, basically doubling your project's disk space usage, and you have to run <code>vagrant rsync</code> (for ad-hoc syncing) or <code>vagrant rsync-auto</code> (for continuous syncing) while the VM is running. But since most codebases aren't too large, space/extra time for the initial sync is usually a non-issue, and <code>vagrant rsync-auto</code> doesn't seem to be too processor/disk intense after the first minute or two.

Before 1.5, my typical Vagrantfile had a section like the following:

```
if is_windows
  # - run a shell provisioner which runs ansible provisioner within vm
  # - in provisioner, install samba and configure a share
  # - rely on user to connect to share manually
else
  # - run ansible provisioner
  # - add a normal shared folder
  # - rely on user to comment out shared folder and uncomment nfs shared folder
  #   after the first `vagrant up`
end
```

It was fairly messy, though I was proud of the solution in the end—it was the best possible scenario for our particular use case pre-1.5.

Now, I have the following:

```
if is_windows
  # - run a shell provisioner which runs ansible provisioner within vm
else
  # - run ansible provisioner
end
# create an rsync synced folder for everyone
```

What does the shared folder setup look like, inside a <code>Vagrantfile</code>? It's really simple:

```
# Set up a shared folder using a path defined in the user's environment.
shared_folder_path = ENV['XYZ_SHARED_FOLDER_PATH'] ? ENV['XYZ_SHARED_FOLDER_PATH'] : "~/Sites/xyz"

config.vm.synced_folder shared_folder_path, "/xyz",
  # Tell Vagrant to use rsync for this shared folder.
  type: "rsync",
  rsync__auto: "true",
  rsync__exclude: ".git/",
  id: "shared-folder-id"
```

The <code>shared_folder_path</code> was added so team members could stick their code repositories wherever they liked, rather than be forced to put their repos in one rigid location, or hack the shared/version-controlled Vagrantfile. This is especially helpful when working between platforms, as Windows pathing is much different than Mac/Linux.
