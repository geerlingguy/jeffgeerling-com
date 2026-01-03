---
nid: 2782
title: "Use an ARG in Dockerfile FROM for dynamic image specification"
slug: "use-arg-dockerfile-dynamic-image-specification"
date: 2017-06-14T17:44:35+00:00
drupal:
  nid: 2782
  path: /blog/2017/use-arg-dockerfile-dynamic-image-specification
  body_format: markdown
  redirects: []
tags:
  - arg
  - command line
  - docker
  - dockerfile
  - registry
  - tutorial
---

`Dockerfile`s have been able to use `ARG`s to allow passing in parameters during a `docker build` using the CLI argument `--build-arg` for some time. But until recently (Docker's [17.05](https://github.com/moby/moby/releases/tag/v17.05.0-ce) release, to be precise), you weren't able to use an `ARG` to specify all or part of your `Dockerfile`'s mandatory `FROM` command.

But since the pull request [Allow ARG in FROM](https://github.com/moby/moby/pull/31352) was merged, you can now specify an image / repository to use at runtime. This is great for flexibility, and as a concrete example, I used this feature to allow me to pull from a private Docker registry when building a Dockerfile in production, or to build from a local Docker image that was created as part of a CI/testing process inside Travis CI.

To use an `ARG` in your `Dockerfile`'s `FROM`:

```
ARG MYAPP_IMAGE=myorg/myapp:latest
FROM $MYAPP_IMAGE
...
```

Then if you want to use a different image/tag, you can provide it at runtime:

```
docker build -t container_tag --build-arg MYAPP_IMAGE=localimage:latest .
```

If you don't specify `--build-arg`, then Docker will use the default value in the `ARG`.

Typically, it's preferred that you set the `FROM` value in the Dockerfile itself—but there are many situations (e.g. CI testing) where you can justify making it a runtime argument.
