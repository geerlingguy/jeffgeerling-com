---
nid: 3250
title: "Docker and systemd, getting rid of dreaded 'Failed to connect to bus' error"
slug: "docker-and-systemd-getting-rid-dreaded-failed-connect-bus-error"
date: 2022-10-26T15:54:25+00:00
drupal:
  nid: 3250
  path: /blog/2022/docker-and-systemd-getting-rid-dreaded-failed-connect-bus-error
  body_format: markdown
  redirects: []
tags:
  - ansible
  - continuous integration
  - docker
  - molecule
  - systemd
---

The following error has been the bane of my existence for the past few months:

```
TASK [geerlingguy.containerd : Ensure containerd is started and enabled at boot.] ***
fatal: [instance]: FAILED! => {
  "changed": false,
  "cmd": "/bin/systemctl",
  "msg": "Failed to connect to bus: No such file or directory",
  "rc": 1,
  "stderr": "Failed to connect to bus: No such file or directory",
  "stderr_lines": [
    "Failed to connect to bus: No such file or directory"
  ],
  "stdout": "",
  "stdout_lines": []
}
```

Since I use [Molecule](https://molecule.readthedocs.io/en/latest/) with my Ansible roles and playbooks to test them in identical CI environments both locally and in GitHub Actions, I can maintain an identical environment inside which tests are run. And many of my roles and playbooks need to test whether systemd services are configured and run correctly.

But Docker recently switched from cgroups v1 to cgroups v2, and that started this 'Failed to connect to bus' business—systemd relied on some configuration that was easy enough to add in the past: just run your containers with these options:

```
--privileged -v /sys/fs/cgroup:/sys/fs/cgroup:rw
```

But after the cgroups v2 upgrade, you either had to add the option `"deprecatedCgroupv1": true` to Docker's `settings.json` file, or add the command line option `--cgroupns=host`.

The trouble is, Molecule didn't have a way to pass the `cgroupns` option, so if I wanted to run things locally, I was stuck having to use the 'deprecated' cgroup v1 option. Until yesterday!

All I had to do to ensure systemd would work inside my containers is add the `cgroupns_mode: host` option in my `molecule.yml` file, for example:

```
platforms:
  - name: instance
    image: "geerlingguy/docker-debian11-ansible:latest"
    command: ""
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
      - /var/lib/containerd
    cgroupns_mode: host  ## <-- This is the line I added
    privileged: true
    pre_build_image: true
```

For more information, check out these issues:

  - [docker/for-mac - Unable to run systemd services on Docker Desktop 4.3.0](https://github.com/docker/for-mac/issues/6073)
  - [ansible-community/molecule - Host Debian 11 running molecule on Debian 11 fails](https://github.com/ansible-community/molecule/issues/3632)
