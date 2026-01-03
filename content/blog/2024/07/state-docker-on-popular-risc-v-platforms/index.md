---
nid: 3392
title: "The state of Docker on popular RISC-V platforms"
slug: "state-docker-on-popular-risc-v-platforms"
date: 2024-07-22T20:32:40+00:00
drupal:
  nid: 3392
  path: /blog/2024/state-docker-on-popular-risc-v-platforms
  body_format: markdown
  redirects: []
tags:
  - arm
  - docker
  - jupiter
  - linux
  - milk-v
  - risc-v
---

I've been testing a [Milk-V Jupiter](https://github.com/geerlingguy/sbc-reviews/issues/47) this week, and have tested a number of other RISC-V development boards over the past two years.

As with any new CPU architecture, software support and ease of adoption are extremely important if you want to reach a wider audience. I wouldn't expect every developer and SBC hobbyist to be able to compile the Linux kernel, and the need to compile much of anything these days is getting rare. So having any instance where one _has_ to know how to tweak a Makefile or pass in different flags to a compiler is a bit of a turn-off for platform adoption.

So one thing I've followed closely is how easy it is for me to get my own software running on RISC-V boards. It's one thing to run some vendor-provided demos. It's another entirely to take my real-world applications and infrastructure apps, and get them to work without hassle.

And to that end, Docker and Ansible, two tools I use extensively for dev/ops work, both run stably—though with plenty of caveats since RISC-V is still so new.

I covered [how I install Ansible on RISC-V Linux](/blog/2024/installing-ansible-on-risc-v-computer) earlier, but today I'll go through my first time testing Docker on the Jupiter (which has an 8-core Spacemit CPU).

## Installing Docker

Spacemit seems to have everything under the sun working on their Bianbu Linux distro—and they've been [partnering with Ubuntu since earlier this year](https://canonical.com/blog/canonical-enables-ubuntu-on-milk-v-mars) for well-supported Ubuntu releases as well.

Installing Docker is as easy as:

```
sudo apt install docker.io
```

After that, it's just... Docker. So `hello-world` works too:

```
root@milkv-jupiter:~# docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (riscv64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

Many base images, like [Debian](https://hub.docker.com/_/debian/tags), already provide working `riscv64` builds for all their images. But many don't. Like [`httpd`](https://hub.docker.com/_/httpd) (Apache) doesn't, so if you try running it or building an image off it, you'll get:

```
root@milkv-jupiter:~# docker build -t my-apache2 .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  165.8MB
Step 1/2 : FROM httpd:2.4
2.4: Pulling from library/httpd
no matching manifest for linux/riscv64 in the manifest list entries
```

Other images advertise support for `riscv64`, but it's not in the main Hub image, it's in a separate image hosted elsewhere (which can sometimes be annoying to track down).

One case is Redis, where the [main image](https://hub.docker.com/_/redis) lists:

> **Supported architectures**: (more info⁠)
> `amd64`, `arm32v5`, `arm32v6`, `arm32v7`, `arm64v8`, `i386`, `mips64le`, `ppc64le`, `riscv64`, `s390x`

If you click on the link, you'll end up on the [`riscv64/redis`](https://hub.docker.com/r/riscv64/redis/) page, where it says:

> Start a redis instance
>
> `$ docker run --name some-redis -d riscv64/redis`

But running that results in an error:

```
root@milkv-jupiter:~# docker run --name some-redis -d riscv64/redis
Unable to find image 'riscv64/redis:latest' locally
docker: Error response from daemon: manifest for riscv64/redis:latest not found: manifest unknown: manifest unknown.
See 'docker run --help'.
```

Indeed, there is no `latest` tag on that repo, but rather tons of [tags for specific versions](https://hub.docker.com/r/riscv64/redis/tags). Trying one of those, it does work:

```
root@milkv-jupiter:~# docker run --name some-redis -d riscv64/redis:7.4-rc-alpine3.20
5d0cb96008de00fea6bc394953fb4a19526921b87f991944a7c894d633c9509e
root@milkv-jupiter:~# docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS          PORTS      NAMES
5d0cb96008de   riscv64/redis:7.4-rc-alpine3.20   "docker-entrypoint.s…"   25 seconds ago   Up 24 seconds   6379/tcp   some-redis

root@milkv-jupiter:~# docker exec -it 5d0 redis-cli INFO keyspace
# Keyspace
```

A couple years ago, RISC-V was in a very rough space, where I would run into crashes, weird boot issues, etc. Today it feels a lot like Arm Linux in 2016 or so... there is some support out there, most things _work_, but you have to do a lot of manual tweaking to run real-world applications.

It's nearing the threshold where things _just work_, though, and I think that's key to wider RISC-V adoption. Arm devices really paved the way, here, though. Before the rise in popularity, it was common to have pre-built images and packages for `amd64`, but rarely `armv6`, `armv7`, or `arm64`. Now, almost any widely-used project has builds for at least `amd64` and `arm64`, and once you go from "only 1" to "n+1", the build processes are usually in place to the point adding another "+1" is not that hard.

Especially when vendors are willing to chip in and help, as it seems many of the RISC-V players are doing eagerly right now.
