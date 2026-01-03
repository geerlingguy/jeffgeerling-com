---
nid: 3154
title: "Making sure symlinks work on CIFS/SMB mounted shares"
slug: "making-sure-symlinks-work-on-cifssmb-mounted-shares"
date: 2021-12-02T18:57:49+00:00
drupal:
  nid: 3154
  path: /blog/2021/making-sure-symlinks-work-on-cifssmb-mounted-shares
  body_format: markdown
  redirects: []
tags:
  - cifs
  - linux
  - nas
  - samba
  - smb
  - symlinks
  - windows
---

I was recently working on some backup scripts to make sure I could clone all my GitHub repositories to my NAS, which I have mounted to a Raspberry Pi that handles all my backups.

I'm using [gickup](https://github.com/cooperspencer/gickup) to run through all my GitHub repos and clone them locally, and I configured it to clone each repo directly into my NAS share, which is mounted over CIFS using something like:

```
sudo mount -t cifs -o uid=pi,username=myuser,password=mypass //my-nas-server/Backups /Volumes/Backups
```

Most repositories cloned correctly, but a few had symlinks inside, and when git was cloning them, the process would error out with:

```
6:42PM INF cloning community.digitalocean path=/Volumes/Backups stage=locally
6:42PM PNC symlink digital_ocean_account_info.py community.digitalocean/plugins/modules/digital_ocean_account_facts.py: operation not supported path=/Volumes/Backups stage=locally
panic: symlink digital_ocean_account_info.py community.digitalocean/plugins/modules/digital_ocean_account_facts.py: operation not supported
```

And indeed, if I tried manually creating a symlink, it would fail in the same way:

```
pi@backup:/Volumes/Git-Backups $ touch a.txt
pi@backup:/Volumes/Git-Backups $ ln -s a.txt b.sl
ln: failed to create symbolic link 'b.sl': Operation not supported
```

As it turns out, since my NAS supports only SMB2 and SMB3, I had to add `mfsymlinks` to the `opts` so I would be able to create symlinks in the mounted shares:

```
sudo mount -t cifs -o uid=pi,mfsymlinks,username=myuser,password=mypass //my-nas-server/Backups /Volumes/Backups
```

Now git can happily clone repos with symlinks, and my backups are just a little more complete!
