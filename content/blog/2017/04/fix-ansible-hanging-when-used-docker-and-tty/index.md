---
nid: 2761
title: "Fix for Ansible hanging when used with Docker and TTY"
slug: "fix-ansible-hanging-when-used-docker-and-tty"
date: 2017-04-02T01:50:34+00:00
drupal:
  nid: 2761
  path: /blog/2017/fix-ansible-hanging-when-used-docker-and-tty
  body_format: markdown
  redirects: []
tags:
  - ansible
  - containers
  - devops
  - docker
  - terminal
  - testing
  - travis ci
---

For almost all my Ansible roles on Ansible Galaxy, I have a comprehensive suite of tests that run against all supported OSes on Travis CI, and the only way that's possible is using Docker containers (one container for each OS/test combination).

For the past year or so, I've been struggling with some of the test suites having strange issues when I use `docker exec --tty` (which passes through Ansible's pretty coloration) along with Ansible playbooks running inside Docker containers in Travis CI. It seems that certain services, when restarted on OSes running sysvinit (like Ubuntu 14.04 and CentOS 6), cause `ansible-playbook` to hang indefinitely, resulting in a build failure:

```
...
changed: [localhost]

RUNNING HANDLER [geerlingguy.apache : restart apache] **************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=16   changed=8    unreachable=0    failed=0   

No output has been received in the last 10m0s, this potentially indicates a stalled build or something wrong with the build itself.
Check the details on how to adjust your build configuration on: https://docs.travis-ci.com/user/common-build-problems/#Build-times-out-because-no-output-was-received
The build has been terminated
```

When glancing around at issues, it seems that if you use Ansible's own Docker connection, it might not have this issue, but if you execute Docker commands and run Ansible _inside_ a Docker container, that's when the issue arises.

Tonight, while fixing this problem for the umpteenth time, I finally found a stable workaround that allows me to see pretty colors for ok/changed/failed tasks, and doesn't cause the playbook to hang after completion:

```
# Set ANSIBLE_FORCE_COLOR instead of using `--tty`
docker exec [container] env ANSIBLE_FORCE_COLOR=1 ansible-playbook /path/to/playbook.yml
```

Doing this allows me to have fancy colors while not breaking my builds!

{{< figure src="./colors-terminal-ansible-playbook-in-docker.png" alt="Colors in terminal output using ansible-playbook in a Docker container" width="650" height="381" class="insert-image" >}}
