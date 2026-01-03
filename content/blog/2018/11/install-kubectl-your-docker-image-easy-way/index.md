---
nid: 2888
title: "Install kubectl in your Docker image, the easy way"
slug: "install-kubectl-your-docker-image-easy-way"
date: 2018-11-12T20:18:44+00:00
drupal:
  nid: 2888
  path: /blog/2018/install-kubectl-your-docker-image-easy-way
  body_format: markdown
  redirects: []
tags:
  - composer
  - containers
  - docker
  - image
  - kubectl
  - kubernetes
---

Most of the time, when I install software on my Docker images, I add a rather hairy `RUN` command which does something like:

  1. Install some dependencies for key management.
  2. Add a GPG key for a new software repository.
  3. Install software from that new software repository.
  4. Clean up apt/yum/dnf caches to save a little space.

This is all well and good; and this is the [most recommended way to install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) in most situations, but it's not without it's drawbacks:

  - You have to have a multi-part RUN command.
  - You have to add a GPG key and an extra software repository to support the install (taking up some precious space in your image layer).
  - It's just annoying when you just need a single binary or executable to be present!

So for a while now, I've been using the following shortcut to getting certain utilities on my Docker images. As long as you trust the upstream from which you install them, you can actually copy executables directly from other images on Docker Hub (or any other image repository) as part of your `Dockerfile` build. For example, I just want `kubectl` in my Docker image's `$PATH`:

```
# Install kubectl from Docker Hub.
COPY --from=lachlanevenson/k8s-kubectl:v1.10.3 /usr/local/bin/kubectl /usr/local/bin/kubectl
```

Now in the rest of the `Dockerfile`, or in the running container, I can use `kubectl` with no problem! As long as you trust the image source (in this case, [Lachlan Evenson](https://github.com/lachie83), who works for Microsoft), it's a way simpler (and lighter-weight) way to grab a single binary.

> _Why am I pulling v1.10.3 instead of the latest?_
> Because that's the only currently-supported version of Kubernetes on EKS, which is what I'm using for the particular project from which this example was pulled.

This also works for things like Composer, which is used to manage PHP dependencies. I usually pull the latest version of the binary straight from the official Docker Library image:

```
# Install Composer from Docker Hub, to faciliate install Magento dependencies.
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Install Prestissimo to speed up Composer installs.
RUN composer global require hirak/prestissimo
```

This example shows how you can immediately start using the executable in the rest of the `Dockerfile` if you want.
