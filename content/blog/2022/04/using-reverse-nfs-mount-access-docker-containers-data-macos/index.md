---
nid: 3200
title: "Using a reverse-NFS mount to access Docker container's data from macOS"
slug: "using-reverse-nfs-mount-access-docker-containers-data-macos"
date: 2022-04-13T18:59:21+00:00
drupal:
  nid: 3200
  path: /blog/2022/using-reverse-nfs-mount-access-docker-containers-data-macos
  body_format: markdown
  redirects: []
tags:
  - docker
  - docker compose
  - linux
  - mac
  - nfs
  - tutorial
  - volumes
---

For years, Mac users have dealt with [slow filesystem performance for Docker volumes](https://github.com/docker/for-mac/issues/1592) when using Docker for Mac. This is because the virtualized filesystem, which used `osxfs` for a while and will soon be upgraded to use `VirtioFS`.

But if you need to do large operations on huge codebases inside a shared directory, even [using NFS](/blog/2020/revisiting-docker-macs-performance-nfs-volumes) to share from the Mac into Docker is a _lot_ slower than running a native Docker volume or just using files inside the container's own filesystem.

{{< figure src="./macos-disk-utility-case-sensitive.jpg" alt="macOS Disk Utility APFS Case Insensitive filesystem" width="700" height="300" class="insert-image" >}}

What finally forced me to come up with a better 'reverse volume' solution was the fact that my macOS APFS filesystem is _not_ case sensitive, meaning working with large codebases like the Linux kernel source tree is infeasible inside my main Mac filesystem (due to it [having files with the same name](https://stackoverflow.com/a/10020483/100134), just different casing).

> If you're on Linux, all this extra complexity isn't needed—you could just mount a volume from your local filesystem at full speed.
>
> _But why don't you just run Linux, then, Jeff?_ Yeah. Well... we won't get into that in _this_ post.

Since I'm [rebuilding the Linux kernel](https://redshirtjeff.com/listing/linux-recompile-shirt?product=211) on a daily basis, having the kernel source checked out inside a Docker container (in my [kernel cross-compile Docker environment](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/master/extras/cross-compile)) for compile time speed is essential.

But getting access to those files from my preferred IDE (Sublime Text) on my Mac host system is well nigh impossible. Some older versions of Docker for Mac on Intel Macs had a way of mounting the Docker VM's storage in a weird and hacky way, but that's not possible on M1 Macs with the newest versions of Docker.

So I went about building a 'reverse NFS' mount.

## Reverse NFS Mount

My idea was to use a named volume for the Linux repository checkout inside the container, then have a separate container running NFS server, which I could then mount on my Mac using NFSv4:

{{< figure src="./docker-compose-reverse-nfs-share.png" alt="Reverse NFS Share in Docker on Mac with Linux volume" width="500" height="295" class="insert-image" >}}

So I spent a couple hours hacking together a solution, and came up with the following:

  1. In [my `docker-compose` file](https://github.com/geerlingguy/raspberry-pi-pcie-devices/blob/master/extras/cross-compile/docker-compose.yml), I added a named volume:

     ```
     volumes:
       linux:
     ```

  2. I mount that into the `/build` directory inside the cross-compile container:

     ```
         volumes:
           - linux:/build
     ```

  3. Then I set up a _separate_ container that runs NFS server in the same `docker-compose` file:

     ```
       cross-compile-nfs:
         image: gists/nfs-server
         container_name: cross-compile-nfs
         environment:
           - "NFS_OPTION=fsid=0,rw,sync,insecure,all_squash,anonuid=0,anongid=0,no_subtree_check,nohide"
         ports:
           - "2049:2049"
         volumes:
           - linux:/nfs-share
         cap_add:
           - SYS_ADMIN
           - SETPCAP
     ```

When I bring up my environment (`docker-compose up -d`), I then have an NFS share I can connect to, to mount the contents of the `linux` named volume.

> Note: This configuration requires port 2049 to be unused on your host machine. Macs don't have NFS running out of the box, so for most use cases, this shouldn't be a problem.

When I tried connecting via the macOS Finder's 'Connect to Server' dialog, I couldn't get it to work, so I resorted to the Terminal instead:

```
$ mkdir nfs-share
$ sudo mount -v -t nfs -o vers=4,port=2049 127.0.0.1:/ nfs-share
```

NFS support in macOS has always had its ups and downs. One of the most annoying things is if I forget to _unmount_ the share before I stop my Docker environment, Finder can sometimes hang indefinitely, even if I bring up the Docker environment again. Usually I reboot the entire machine to get back into a normal state again.

The part that took the longest to debug was this unhelpful error message:

```
$ sudo mount -v -t nfs -o vers=4,port=2049 127.0.0.1:/ nfs-share
Password:
mount_nfs: can't mount / from 127.0.0.1 onto /Users/jgeerling/Downloads/nfs-share: Permission denied
mount: /Users/jgeerling/Downloads/nfs-share failed with 13
```

As it turns out, I was adding single quotes around the `NFS_OPTION` value in my `docker-compose` file, like this:

```yaml
    environment:
      - "NFS_OPTION='fsid=0,rw,sync,insecure,all_squash,anonuid=0,anongid=0,no_subtree_check,nohide'"
```

And doing that resulted in the following `/etc/exports` file contents:

```
/ # cat /etc/exports
/nfs-share *('fsid=0,rw,sync,insecure,all_squash,anonuid=0,anongid=0,no_subtree_check,nohide')
```

Apparently, that string breaks NFS's export. Oops.

But after I figured that out, I committed my work and [committed it to my Linux cross-compile environment](https://github.com/geerlingguy/raspberry-pi-pcie-devices/tree/c8e6dd0e99d932eaf325039a1cc74b85e155a75c/extras/cross-compile) so I can easily mount my Linux code checkout from my Mac using NFS, and work on the code in my graphical IDE instead of navigating through it with vim inside the running container.

Why am I doing all this? If you want to find out, [subscribe to my YouTube channel](https://www.youtube.com/c/JeffGeerling)—I'll be posting an update on the status of using external graphics cards on a Raspberry Pi (which requires frequent Linux kernel compilation) soon!
