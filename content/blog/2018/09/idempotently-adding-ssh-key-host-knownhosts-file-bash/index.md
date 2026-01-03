---
nid: 2874
title: "Idempotently adding an SSH key for a host to known_hosts file with bash"
slug: "idempotently-adding-ssh-key-host-knownhosts-file-bash"
date: 2018-09-19T19:42:27+00:00
drupal:
  nid: 2874
  path: /blog/2018/idempotently-adding-ssh-key-host-knownhosts-file-bash
  body_format: markdown
  redirects: []
tags:
  - bash
  - ci
  - github
  - host keys
  - known_hosts
  - shell
  - ssh
---

I noticed on one of the CI servers I'm running that the `.ssh/known_hosts` file had ballooned up to over 1,000,000 lines!

Looking into the root cause (I `tail`ed the file until I could track down a few jobs that ran every minute), I found that there was the following line in a setup script:

```
ssh-keyscan -t rsa github.com >> /var/lib/jenkins/.ssh/known_hosts
```

"This can't be good!" I told myself, and I decided to add a condition to make it idempotent (that is, able to be run once or one million times but only affecting change the first time it's run—basically, a way to change something only if the change is required):

```
if ! grep -q "^github.com" /var/lib/jenkins/.ssh/known_hosts; then
  ssh-keyscan -t rsa github.com >> /var/lib/jenkins/.ssh/known_hosts
fi
```

Now the host key for github.com is only scanned once the first time that script runs, and it is only stored in known_hosts one time for the host github.com... instead of millions of times!

> **Note**: The above test won't work if you have `HashKnownHosts` enabled—which is the default on Debian 9, at least. You should use the test `ssh-keygen -H -F github.com` instead.
