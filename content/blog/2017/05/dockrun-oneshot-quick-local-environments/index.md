---
nid: 2778
title: "dockrun oneshot \u2014 quick local environments for testing infrastructure"
slug: "dockrun-oneshot-quick-local-environments"
date: 2017-05-30T19:05:50+00:00
drupal:
  nid: 2778
  path: /blog/2017/dockrun-oneshot-quick-local-environments
  body_format: markdown
  redirects: []
tags:
  - ansible
  - automation
  - docker
  - infrastructure
  - local development
  - testing
---

Since I work among a ton of different Linux distros and environments in my day-to-day work, I have a lot of tooling set up that's mostly-OS-agnostic. I found myself in need of a quick barebones CentOS 7 VM to play around in or troubleshoot an issue. Or I needed to run Ubuntu 16.04 and Ubuntu 14.04 side by side and run the same command in each, checking for differences. Or I needed to bring up Fedora. Or Debian.

I used to use my Vagrant boxes for VirtualBox to boot a full VM, then `vagrant ssh` in. But that took at least 15-20 seconds—assuming I already had the box downloaded on my computer!

When Docker came around a few years back, it was much faster to bring up an environment, but I couldn't do all the things I could do inside a VM to debug things like initv scripts or systemd configuration and logging. But as time went on, and I kept using and abusing Docker containers, I worked around those issues and [produced a set of Docker images](https://hub.docker.com/r/geerlingguy/)—one for each OS I use often—which included the default process manager and Ansible (since I run [automation integration tests](//www.jeffgeerling.com/blog/2016/how-i-test-ansible-configuration-on-7-different-oses-docker) in these containers).

Taking that a step further, I thought it would be nice to have a quick command I could use to say "boot me a clean OS environment really quick", and thus my little bash function `dockrun` was born:

```
# Super useful Docker container oneshots.
# Usage: dockrun, or dockrun [centos7|fedora24|debian8|ubuntu1404|etc.]
dockrun() {
  docker run -it geerlingguy/docker-"${1:-ubuntu1604}"-ansible /bin/bash
}
```

The official list of OSes I currently maintain with a minimal install + process manager + Ansible include:

  - [`ubuntu1204`](https://hub.docker.com/r/geerlingguy/docker-ubuntu1204-ansible/)
  - [`ubuntu1404`](https://hub.docker.com/r/geerlingguy/docker-ubuntu1404-ansible/)
  - [`ubuntu1604`](https://hub.docker.com/r/geerlingguy/docker-ubuntu1604-ansible/)
  - [`ubuntu1804`](https://hub.docker.com/r/geerlingguy/docker-ubuntu1804-ansible/)
  - [`centos6`](https://hub.docker.com/r/geerlingguy/docker-centos6-ansible/)
  - [`centos7`](https://hub.docker.com/r/geerlingguy/docker-centos7-ansible/)
  - [`fedora24`](https://hub.docker.com/r/geerlingguy/docker-fedora24-ansible/)
  - [`fedora29`](https://hub.docker.com/r/geerlingguy/docker-fedora29-ansible/)
  - [`debian8`](https://hub.docker.com/r/geerlingguy/docker-debian8-ansible/)
  - [`debian9`](https://hub.docker.com/r/geerlingguy/docker-debian9-ansible/)
  - [`debian10`](https://hub.docker.com/r/geerlingguy/docker-debian10-ansible/)

So if you want a quick CentOS 7 environment, if you stick the function above into your profile (see [my dotfiles](https://github.com/geerlingguy/dotfiles) for an example) and source it, then run `dockrun centos7` and within a second or two you'll be dropped into the command line as root on a CentOS 7 minimal install!

{{< figure src="./dockrun.gif" alt="Dockrun - quick Docker environments" width="636" height="435" class="insert-image" >}}

I'm sure other people do something similar; I just wanted to post this here in case you are like me and need a variety of OSes instantly spawnable, with the same baseline (and maybe even Ansible, since it's awesome for automation. (And hey, [I wrote a book on that!](https://www.ansiblefordevops.com))
