---
nid: 2777
title: "Drupal VM does Docker"
slug: "drupal-vm-does-docker"
date: 2017-05-24T13:57:23+00:00
drupal:
  nid: 2777
  path: /blog/2017/drupal-vm-does-docker
  body_format: markdown
  redirects: []
tags:
  - containers
  - docker
  - drupal
  - drupal planet
  - drupal vm
---

{{< figure src="./drupal-vm-docker-hub.png" alt="Drupal VM on Docker Hub" width="650" height="495" class="insert-image" >}}

Drupal VM has used Vagrant and (usually) VirtualBox to run Drupal infrastructure locally since its inception. But ever since Docker became 'the hot new thing' in infrastructure tooling, I've been asked when Drupal VM will convert to using Docker.

The answer to that question is a bit nuanced; Drupal VM has been using Docker to run its own integration tests for over a year (that's how I [run tests on seven different OSes using Travis CI](//www.jeffgeerling.com/blog/2016/how-i-test-ansible-configuration-on-7-different-oses-docker)). And technically, Drupal VM's core components have always been able to run inside Docker containers (most of them use Docker-based integration tests as well).

But Docker usage was always an undocumented and unsupported feature of Drupal VM. But no longer—with 4.5.0, Drupal VM now supports Docker as an _experimental_ alternative to Vagrant + VirtualBox, and you can use Drupal VM with Docker in one of two ways:

  1. Use the [drupal-vm](https://hub.docker.com/r/geerlingguy/drupal-vm/) Docker Hub container.
  2. Use Drupal VM to build a custom Docker image for your project.

The main benefit of using Docker instead of Vagrant (at least at this point) is speed—not only is provisioning slightly faster (or nearly _instantaneous_ if using the Docker Hub image), but performance on Windows and Linux is decidedly better than with VirtualBox.

Another major benefit? The Drupal VM Docker image is only ~250 MB! If you use VirtualBox, box files are at least twice that size; getting started with Drupal VM using Docker is even faster than Vagrant + VirtualBox!

## Use the Docker Hub image

The simplest option—if you don't need much customization, but rather need a quick LAMP stack running with all Drupal VM's defaults—is to use [the official Drupal VM docker image](https://hub.docker.com/r/geerlingguy/drupal-vm/). Using it with an existing project is easy:

  1. Copy Drupal VM's [example Docker Compose file](https://github.com/geerlingguy/drupal-vm/blob/master/example.docker-compose.yml) into your project's root directory.
  2. Customize the Docker Compose file for your project.
  3. Add an entry to your computer's hosts file.
  4. Run `docker-compose up -d`.

If you're using a Mac, there's an additional step required to make the container's IP address usable; you currently have to create an alias for the IP address you use for the container with the command `sudo ifconfig lo0 alias 192.168.88.88/24` (where the IP address is the one you have chosen in your project's Docker Compose file).

You can even customize the default image slightly using a Dockerfile and changing one line in the Docker Compose file; see [Add a `Dockerfile` for customization](http://docs.drupalvm.com/en/latest/other/docker/#optional-add-a-dockerfile-for-customization).

> Want a real-world example? See the [Site for Drupal VM Prod Deployment Demonstrations](https://github.com/geerlingguy/drupalvm-live) codebase on GitHub—it's using this technique for the local environment.

## Use Drupal VM to 'bake and share' a custom image

The second way you can use Drupal VM with Docker is to use some built-in functionality to build a completely custom Docker image. For teams with particular requirements (e.g. using Varnish, Solr, and PostgreSQL), you can configure Drupal VM using a `config.yml` file as usual, but instead of requiring each team member to provision a Drupal VM instance on their own, one team member can `composer docker-bake` a Docker container.

Then, save the image with `composer docker-save-image`, share it with team members (e.g. via Google Drive, Dropbox, etc.), then each team member can load in the image with `composer docker-load-image`.

See the documentation here: ['Bake and Share' a custom Drupal VM Docker image](http://docs.drupalvm.com/en/latest/other/docker/#method-2-bake-and-share-a-custom-drupal-vm-docker-image).

## FAQs

Since there are bound to be a lot of questions surrounding experimental Docker support, I thought I'd stick a few of the frequently asked questions in here.

### Why wasn't this done sooner?

The main reason I have held off getting Drupal VM working within Docker containers was because Docker's support for Mac has been weak at best. There were two major issues that I've been tracking, and thankfully, both issues are resolved with the most recent release of Docker:

  1. Using Docker on a custom IP address (so you can have multiple Drupal VM instances on different IP addresses all using port 80, 443, etc.).
  2. Docker for Mac is known for sluggish filesystem access when using default volumes.

The latter issue was a deal-breaker for me, because the performance using a Docker container with a Drupal codebase as a volume was abysmal—it was _18 times slower_ running the same Drupal codebase within a Docker container vs. running it in VirtualBox with an NFS mounted shared folder.

In the issue [File system performance improvements](https://github.com/docker/for-mac/issues/1592), Docker has already added `cached` volume support, where reads are cached for native filesystem read performance, and support for `delegated` volumes will be added soon (which allows _writes_ to be cached as well, so operations like `composer update` on a volume will not be sluggish).

As of May 2017, you need to download Docker's Edge release to use the `cached` or `delegated` volume options on Mac. For a good historical overview of these features, read [File access in mounted volumes extremely slow](https://github.com/docker/for-mac/issues/77).

### Why aren't you using Vagrant with the Docker provider?

We're looking into that: [Consider allowing use of Vagrant with docker provider to run and provision Drupal VM](https://github.com/geerlingguy/drupal-vm/issues/1381).

### You're doing Docker wrong. You shouldn't use a monolith container!

Yeah, well, it works, and it means Docker can function similarly to a VirtualBox VM so we don't have to have two completely different architectures for Docker vs. a VM. At some point in the future, Drupal VM may make its Docker-based setup 'more correct' from a microservices perspective. But if you're pining for a Docker setup that's Docker-centric and splits things up among dozens of containers, there are plenty of options already.

### You're doing Docker wrong. You're using `privileged`!

Yeah, well, it works. See the above answer for reasoning.

### I wish there were other variations of the Drupal VM image on Docker Hub...

So do I; currently Docker Hub doesn't easily support having multiple Dockerfiles with the same build context in an automatically-built Docker Hub image. But Drupal VM might be able to build and manage multiple image versions (e.g. one with LEMP, one with LAMP + Solr, etc.) using a CI tool soon. I just haven't had the time to get something like this running.

### Will this make Windows development awesome?

Sort-of. The nice thing is, now you can use Docker in Windows and drop the baggage of Vagrant + VirtualBox (which has always been slightly painful). But as Docker support is currently experimental, you should expect some bumps in the road. Please feel free to open issues on GitHub if you encounter any problems.

### Should I use a Docker container built with Drupal VM in production?

Probably not. In my opinion, one of the best things about Docker is the fact that you can ship your application container directly to production, and then you can _guarantee_ that your production environment is 100% identical to development (that whole 'it works on _my_ machine' problem...).

But currently Drupal VM (just like about 99% of other local-environment-focused tools) is more geared towards development purposes, and not production (though you can use Drupal VM to build production environments... and I do so for the [Drupal VM Production Demo](http://prod.drupalvm.com) site!).
