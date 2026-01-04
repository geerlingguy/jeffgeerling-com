---
nid: 2977
title: "Revisiting Docker for Mac's performance with NFS volumes"
slug: "revisiting-docker-macs-performance-nfs-volumes"
date: 2020-03-13T22:23:02+00:00
drupal:
  nid: 2977
  path: /blog/2020/revisiting-docker-macs-performance-nfs-volumes
  body_format: markdown
  redirects: []
tags:
  - development
  - docker
  - drupal
  - drupal planet
  - local development
  - mac
  - nfs
  - performance
  - volumes
aliases:
  - /comment/reply/node/2977/comment_node_blog_post
---

> **tl;dr**: Docker's default bind mount performance for projects requiring lots of I/O on macOS is abysmal. It's acceptable (but still very slow) if you use the `cached` or `delegated` option. But it's actually fairly performant using the barely-documented NFS option!

> **July 2020 Update**: Docker for Mac may soon offer built-in Mutagen sync via the `:delegated` sync option, and I [did some benchmarking here](https://github.com/docker/for-mac/issues/1592#issuecomment-634960996). Hopefully that feature makes it to the standard Docker for Mac version soon.

> **September 2020 Update**: Alas, Docker for Mac will not be getting built-in Mutagen support at this time. So, read on.

Ever since Docker for Mac was released, shared volume performance has been a major pain point. It was _painfully_ slow, and the community finally got a `cached` mode that offered a 20-30x speedup for common disk access patterns around 2017. Since then, the [File system performance improvements](https://github.com/docker/for-mac/issues/1592) issue has been a common place to gripe about the lack of improvements to the underlying `osxfs` filesystem.

Since around 2016, support has been around (albeit barely documented) for NFS volumes in Docker (see [Docker `local` volume driver-specific options](https://docs.docker.com/engine/reference/commandline/volume_create/#driver-specific-options#driver-specific-options)).

As part of my site migration project, I've been [testing different local development environments](https://github.com/geerlingguy/jeffgeerling-com/issues/18), and as a subset of that testing, I decided to [test different volume/sync options for Docker](https://github.com/geerlingguy/jeffgeerling-com/issues/22) to see what's the fastest—and easiest—to configure and maintain.

Before I drone on any further, here are some benchmarks:

{{< figure src="./docker-nfs-benchmark-time-to-install-d8.png" alt="Time to install Drupal 8 - different Docker volume sync methods" width="455" height="266" class="insert-image" >}}

{{< figure src="./docker-nfs-benchmark-time-to-page-load-d8.png" alt="Time to first Drupal 8 page load - different Docker volume sync methods" width="455" height="270" class="insert-image" >}}

## Benchmarks explained

The first benchmark installs Drupal, using the JeffGeerling.com codebase. The operation requires loading thousands of code files from the shared volume, writes a number of files back to the filesystem (code, generated templates, and some media assets), and does a decent amount of database work. The database is stored on a separate Docker volume, and not shared, so it is plenty fast on its own (and doesn't affect the results).

The second benchmark loads the home page (`/`) immediately after the installation; this page load is entirely uncached, so Drupal again reads all the thousands of files from the filesystem and loads them into PHP's opcache, then finishes its operations.

Both benchmarks were run four times, and nothing else was open on my 2016 MacBook Pro while running the benchmarks.

## Using the different sync methods

### NFS

To use NFS, I had to do the following (note: this was on macOS Catalina—other systems and macOS major versions may require modifications):

I edited my Mac's NFS exports file (which was initially empty):

    sudo nano /etc/exports

I added the following line (to allow sharing any directories in the Home directory—under older macOS versions, this would be `/Users` instead):

    /System/Volumes/Data -alldirs -mapall=501:20 localhost

(When I saved the file macOS popped a permissions prompt which I had to accept to allow Terminal access to write to this file.)

I also edited my NFS config file:

    sudo nano /etc/nfs.conf

I added the following line (to tell the NFS daemon to allow connections from any port—this is required otherwise Docker's NFS connections may be blocked):

    nfs.server.mount.require_resv_port = 0

Then I restarted `nfsd` so the changes would take effect:

    sudo nfsd restart

Then, to make sure my Docker Compose service could use an NFS-mounted volume, I added the following to my `docker-compose.yml`:

```yaml
---
version: '3'

services:
  drupal:
    [...]
    volumes:
      - 'nfsmount:/var/www/html'

volumes:
  nfsmount:
    driver: local
    driver_opts:
      type: nfs
      o: addr=host.docker.internal,rw,nolock,hard,nointr,nfsvers=3
      device: ":${PWD}"
```

Note that I have my project in `~/Sites`, which is covered under the `/System/Volumes/Data` umbrella... for older macOS versions you would use `/Users` instead, and for locations outside of your home directory, you have to grant 'Full Disk Access' in the privacy system preference pane to `nfsd`.

Some of this info I picked up from [this gist](https://gist.github.com/seanhandley/7dad300420e5f8f02e7243b7651c6657) and it's comments, especially the [comment from egobude](https://gist.github.com/seanhandley/7dad300420e5f8f02e7243b7651c6657#gistcomment-3049542) about the changes required for Catalina.

So, for NFS, there are a few annoying steps, like having to manually add an entry to your `/etc/exports`, modify the NFS configuration, and restart NFS. But at least on macOS, everything is built-in, and you don't have to install anything extra, or run any extra containers to be able to get the performance benefit.

### docker-sync.io

[`docker-sync`](http://docker-sync.io) is a Ruby gem (installed via `gem install docker-sync`) which requires an additional configuration file (`docker-sync.yml`) alongside your `docker-compose.yml` file, which then requires you to `start` docker-sync prior to starting your docker-compose setup. It also ships with extra wrapper functions that can do it all for you, but overall, it felt a bit annoying to have to manage a 2nd tool on top of Docker itself in order to get syncing working.

It also took almost two minutes (with CPU at full bore) the first time I started the environment for an initial sync of all my local files into the volume docker-sync created that was mounted into my Drupal container.

It _was_ faster for most operations (sometimes by 2x) than NFS (which was 2-3x faster than `:cached`/`:delegated`), but for some reason the initial Drupal install was actually a few seconds _slower_ than NFS. Not sure the reason, but might have to do with the way unison sync works.

### docker bg-sync

[bg-sync](https://github.com/cweagans/docker-bg-sync) is a container that syncs files between two directories. For my Drupal site, since there are almost 40,000 files (I know... that's Drupal for you), I had to give this container `privileged` access (which I'm leery of doing in general, even though I trust bg-sync's maintainer).

It works with a volume shared from your Mac to _it_, then it syncs the data from there into your destination container using a separate (faster) local volume. The configuration is a little clunky (IMO), and requires some differences between Compose v2 and v3 formats, but it felt a little cleaner to manage than `docker-sync`, because I didn't have to install a rubygem and start a separate process—instead, all the configuration is managed inside my `docker-compose.yml` file.

bg-sync offered around the same performance as `docker-sync` (they both use the same unison-based sync method, so that's not a surprise), though for some reason, the initial sync took closer to three minutes, which was a bit annoying.

## Summary

I wanted to write this post after spending a few hours testing all these different volume mount and sync tools, because so many of the guides I've found online are either written for older macOS versions or are otherwise unreliable.

In the end, I've decided to stick to using an NFS volume for my personal project, because it offers _nearly_ native performance (certainly a major improvement over the Docker for Mac `osxfs` filesystem), is not difficult to configure, and doesn't require any extra utilities or major configuration changes in my project.

### What about Linux?

I'm glad you asked! I use the exact same Docker Compose config for Linux—all the NFS configuration is [stored in a `docker-compose.override.yml` file](https://github.com/geerlingguy/jeffgeerling-com/blob/master/docker-compose.override.yml) I use for my Mac. For Linux, since normal bind mounts offer native performance already (Docker for Linux doesn't use a slow translation layer like `osxfs` on macOS), I have a [separate `docker-compose.override.yml` file](https://github.com/geerlingguy/jeffgeerling-com/blob/master/.github/docker-compose.override.yml) which configures a standard shared volume.

And in production, I bake my complete Docker image (with the codebase inside the image)—I don't use a shared volume at all.
