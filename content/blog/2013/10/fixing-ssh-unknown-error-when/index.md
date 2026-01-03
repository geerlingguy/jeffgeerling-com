---
nid: 2433
title: "Fixing SSH unknown error when provisioning a Vagrant VM with Ansible"
slug: "fixing-ssh-unknown-error-when"
date: 2013-10-10T14:41:04+00:00
drupal:
  nid: 2433
  path: /blogs/jeff-geerling/fixing-ssh-unknown-error-when
  body_format: markdown
  redirects: []
aliases:
  - /blogs/jeff-geerling/fixing-ssh-unknown-error-when
tags:
  - ansible
  - provisioning
  - ssh
  - vagrant
---

While getting a local VM managed by Vagrant to work with Ansible for provisioning, I kept getting errors like the following:

```
fatal: [solr] => SSH encountered an unknown error during the connection. We recommend you re-run the command using -vvvv, which will enable SSH debugging output to help diagnose the issue

[vm-name-here] : ok=0    changed=0    unreachable=1    failed=0

FATAL: no hosts matched or all hosts have already failed -- aborting

Ansible failed to complete successfully. Any error output should be
visible above. Please fix these errors and try again.
```

It seems that Ansible is unable to connect to the VirtualBox host via SSH because the entry for 127.0.0.1 in my `~/.ssh/known-hosts` file is set for my local computer, and not for any VMs. To work around this limitation, I created a new file, `~/.ssh/config`, with the contents:

```
Host 127.0.0.1
        StrictHostKeyChecking no
        UserKnownHostsFile=/dev/null
```

Now, when Ansible tries connecting during provisioning, it doesn't check the host key for localhost, and provisioning succeeds.
