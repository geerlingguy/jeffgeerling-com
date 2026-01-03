---
nid: 2711
title: "Remove ALL your local Vagrant Boxes via this bash command"
slug: "remove-all-your-local-vagrant-boxes-bash-command"
date: 2016-10-30T19:26:16+00:00
drupal:
  nid: 2711
  path: /blog/2016/remove-all-your-local-vagrant-boxes-bash-command
  body_format: markdown
  redirects: []
tags:
  - bash
  - box
  - cut
  - terminal
  - vagrant
  - xargs
---

Assuming you have only one box per provider, this command will delete ALL Vagrant boxes you currently have on your system:

    $ vagrant box list | cut -f 1 -d ' ' | xargs -L 1 vagrant box remove -f

This command does the following:

  1. `vagrant box list`: Prints out a list of all installed vagrant boxes (with two columns—box name or path, and meta info)
  2. `cut -f 1 -d ' '`: Cuts the list and takes out just the first column (using spaces to delimit the columns)
  3. `xargs -L 1 vagrant box remove -f`: Use `xargs` to run one command per line, running the command `vagrant box remove -f [box name from list/cut]`.

You can use `xargs`' `-t` option to output the commands being run just before they're executed. And if you have multiple boxes per provider, or if you have multiple versions of the same box, you'll likely need to modify the command a bit.

Since I maintain a half-dozen open-source Vagrant boxes, and use a few dozen other boxes frequently in testing and building software, I like being able to clean out old boxes quickly to conserve disk space (same thing with Docker—I frequently delete ALL downloaded images). This also forces me to make sure that all my infrastructure is _100%_ automated—if I have _any_ special snowflakes around that I'd be afraid to delete by removing its base box... then that's a bug :)
