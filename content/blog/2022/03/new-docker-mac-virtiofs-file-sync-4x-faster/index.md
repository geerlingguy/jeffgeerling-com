---
nid: 3193
title: "New Docker for Mac VirtioFS file sync is 4x faster"
slug: "new-docker-mac-virtiofs-file-sync-4x-faster"
date: 2022-03-19T20:28:45+00:00
drupal:
  nid: 3193
  path: /blog/2022/new-docker-mac-virtiofs-file-sync-4x-faster
  body_format: markdown
  redirects:
    - /blog/2022/new-docker-mac-virtiofs-file-sync-x-faster
    - /blog/2022/new-docker-mac-virtiofs-file-sync-114-faster
aliases:
  - /blog/2022/new-docker-mac-virtiofs-file-sync-x-faster
  - /blog/2022/new-docker-mac-virtiofs-file-sync-114-faster
tags:
  - docker
  - file
  - mac
  - performance
  - sync
  - virtiofs
  - volumes
---

Docker for Mac's shared volume performance saga continues!

After monitoring the issue [File system performance improvements](https://github.com/docker/for-mac/issues/1592) for years (discussion has moved to [this issue](https://github.com/docker/roadmap/issues/7) now), it seems like the team behind Docker Desktop for Mac has finally settled on the next generation of filesystem sync.

For years, the built-in `osxfs` sync performance has been abysmal. For a Drupal developer like me, running a default shared volume could lead to excruciating slowdowns as PHP applications like Symfony and Drupal scan thousands of files when building app caches.

Or God forbid you ever have to install dependencies using Composer or NPM over a shared volume!

It got to the point where [I started using NFS to speed up volume performance](/blog/2020/revisiting-docker-macs-performance-nfs-volumes). Heck, the Docker team _almost_ added Mutagen sync, which [I tested successfully](https://github.com/docker/for-mac/issues/1592#issuecomment-634960996), but it caused problems for too many projects.

But (hopefully) no more! The latest version of Docker Desktop for Mac includes new toggles under the 'Experimental Features' section:

{{< figure src="./docker-mac-virtiofs-file-sync.png" alt="Docker for Mac Preferences - VirtioFS volume mount file synchronization option" width="700" height="397" class="insert-image" >}}

I tested with the defaults (both features disabled, and 'Use gRPC FUSE for file sharing' under the 'General' tab), and then with VirtioFS enabled, and the results speak for themselves:

  - Defaults (gRPC FUSE): 93.750s
  - Enable VirtioFS: 25.461s

**That's a 114% speedup**, and it makes a _huge_ difference for my PHP development workflows using Docker on my Mac.

> Update: Adding a note that on my new M1 Max Mac Studio, with Enable VirtioFS, the install completes in just **15.020s**!

And this isn't a synthetic filesystem test benchmark, I tested installing [my Drupal codebase](https://github.com/geerlingguy/jeffgeerling-com) three times in each condition, and those are the averages. I do this regularly, and a 4x speedup in this part of the workflow is huge.

Some users have reported issues with file permissions or running git operations from within the container, but since I manage my codebase on the Mac side, and don't do anything too exotic inside the running container, I haven't encountered an issue yet.

So far I'm not sure if similar improvements are on their way for Windows, but this longstanding issue's permanent resolution should bring more users across (even in the midst of some abandoning Docker Desktop because of their [licensing changes](https://www.servethehome.com/docker-abruptly-starts-charging-many-users-for-docker-desktop/)).
