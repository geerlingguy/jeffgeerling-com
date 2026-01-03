---
nid: 2890
title: "Decoding Kubernetes Ingress auth Secrets"
slug: "decoding-kubernetes-ingress-auth-secrets"
date: 2018-11-21T00:47:19+00:00
drupal:
  nid: 2890
  path: /blog/2019/decoding-kubernetes-ingress-auth-secrets
  body_format: markdown
  redirects:
    - /blog/2018/decoding-kubernetes-ingress-auth-secrets
aliases:
  - /blog/2018/decoding-kubernetes-ingress-auth-secrets
tags:
  - authentication
  - base64
  - encoding
  - encryption
  - http
  - ingress
  - kubernetes
  - secrets
  - traefik
---

> Update: In the comments, the following one-liner is suggested by Matt T if you have `jq` installed (a handy utility if there ever was one!):
>
> <code>kubectl get secret my-secret -o json | jq '.data | map_values(@base64d)'</code>

I figured it would be handy to have a quick reference for this, since I'll probably forget certain secrets many, many times in the future (I'm like that, I guess):

I have a Kubernetes `Secret` used for Traefik ingress basic HTTP authentication (using annotation `ingress.kubernetes.io/auth-secret`), and as an admin with `kubectl` access, I want to see (or potentially modify) its structure.

Let's say the Secret is in namespace `testing`, and is named `test-credentials`. To get the value of the basic auth credentials I do:

    kubectl get secret test-credentials -n testing -o yaml

This spits out the Kubernetes object definition, including a field like:

    data:
      auth: [redacted base64-encoded string]

So then I copy out that string and decode it:

    echo '[redacted base64-encoded string]' | base64 --decode

And now I have a set of one or more basic HTTP auth credentials; in my case they were encrypted with MD5 encryption, since they were prefixed by `$apr1$` (see [Apache password encryptions](http://httpd.apache.org/docs/current/misc/password_encryptions.html) docs). If I want to update the secret with a new password, I can add it by generating the string with `htpasswd`, then adding it to the data, then base64 encoding it, then modifying the Secret with the new value!

(For production clusters, though, I store all my Kubernetes objects as YAML manifest files in code, so I would make the appropriate changes there then apply the changes using (at least, in my case) Ansible. So this would be a lot less complicated.)
