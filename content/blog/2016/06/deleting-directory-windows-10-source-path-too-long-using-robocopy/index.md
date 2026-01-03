---
nid: 2662
title: "Deleting a directory in Windows 10 with 'Source path too long' using robocopy"
slug: "deleting-directory-windows-10-source-path-too-long-using-robocopy"
date: 2016-06-13T19:05:25+00:00
drupal:
  nid: 2662
  path: /blog/2016/deleting-directory-windows-10-source-path-too-long-using-robocopy
  body_format: markdown
  redirects: []
tags:
  - composer
  - drupal vm
  - npm
  - robocopy
  - windows
  - windows 10
  - windows 8
---

> **2016-10-04 Update**: Microsoft finally allows long paths, provided you are running the latest version of Windows 10; you have to [opt-in by editing a group policy](https://mspoweruser.com/ntfs-260-character-windows-10/) for now—maybe by 2050 or so this will be the default, once all the old legacy Windows apps are finally dead!

For some reason, Windows doesn't play well with deep folder hierarchies. Often, when building Drupal projects inside VMs with synced directories, I end up with folders with 10+ levels of hierarchy, and when I try to delete the directory within windows, I get the error "Source path too long" (or "File path too long"). This happens a lot with npm, composer, or other package/dependency managers, and I'm amazed there's no easy workaround... but I figured I'd document what I do here, because I've had to look up the process too many times.

## 1 - Download robocopy

First, download and install the [Windows Server 2003 Resource Kit Tools](https://www.microsoft.com/en-us/download/details.aspx?id=17657), which includes a CLI utility, `robocopy`.

## 2 - Use robocopy to move the folders into a deletable folder

1. In `cmd` or PowerShell, cd into the parent directory of the folder you need to delete.
2. Create an empty directory (`mkdir empty`).
3. Copy the directory to be deleted into the empty directory (`robocopy empty DELETE_ME /mir`).

## 3 - Delete both directories

`rmdir DELETE_ME`, then `rmdir empty`, and the directory should be gone!

There may be other ways to do this, but I haven't seen any other reliable method. [Credit where it's due](http://superuser.com/a/296241/80658).
