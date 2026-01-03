---
nid: 2617
title: "Using SMB with symlinks instead of native synced folders with Vagrant and VirtualBox"
slug: "using-smb-symlinks-instead-native-synced-folders-vagrant-and-virtualbox"
date: 2016-02-19T19:28:27+00:00
drupal:
  nid: 2617
  path: /blog/2016/using-smb-symlinks-instead-native-synced-folders-vagrant-and-virtualbox
  body_format: markdown
  redirects: []
tags:
  - drupal
  - drupal vm
  - smb
  - symlinks
  - unix
  - vagrant
  - virtualbox
  - windows
---

VirtualBox's native shared folders will be used by default on Windows with the `type` of your synced folder set to `nfs`, or if it's not set. This method works great in many cases, but can be fairly slow when doing work with projects with many files in a synced folder, as is often the case with Drupal sites that I work with in [Drupal VM](http://www.drupalvm.com/).

Another option is to switch the `type` to `smb`. This is often a plug-and-play change (`vagrant reload` to make the change take effect—you'll likely need to enter in your Windows username and password during the startup process. However, symlinks inside the synced folder will likely break, and so we need to make one more important change:

The synced folder configuration needs to have:

```
mount_options: ["mfsymlinks,dir_mode=0755,file_mode=0755"]
```

This uses `mfsymlinks`, or 'Minshall+French Symlinks', which are able to store Unix-like symlinks in SMB filesystems. I found out about this technique from [this Reddit post](https://www.reddit.com/r/devops/comments/440v0c/vagrant_windows_smb_and_symlinks/), and the only caveat is that the symlinks are stored a little differently on disk than the normal Unix-style symlinks, so you have to recreate symlinks after a `vagrant reload`, otherwise the existing symlinks won't work correctly.
