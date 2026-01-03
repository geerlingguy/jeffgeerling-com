---
nid: 2988
title: "Resolving intermittent Fedora DNF error \"No such file or directory: '/var/lib/dnf/rpmdb_lock.pid'\""
slug: "resolving-fedora-dnf-error-no-such-file-or-directory-varlibdnfrpmdblockpid"
date: 2020-04-03T17:22:39+00:00
drupal:
  nid: 2988
  path: /blog/2020/resolving-fedora-dnf-error-no-such-file-or-directory-varlibdnfrpmdblockpid
  body_format: markdown
  redirects: []
tags:
  - ansible
  - boot
  - docker
  - fedora
  - linux
  - systemctl
  - systemd
---

For many of my Ansible playbooks and roles, I have CI tests which run over various distributions, including CentOS, Ubuntu, Debian, and Fedora. Many of my [Docker Hub images for Ansible testing](https://hub.docker.com/u/geerlingguy/) include systemd so I can test services that are installed inside. For the most part, systemd-related issues are rare, but it seems with Fedora and DNF, I often encounter random test failures which invariably have an error message like:

    No such file or directory: '/var/lib/dnf/rpmdb_lock.pid'

The full Ansible traceback is:

```
TASK [geerlingguy.docker : Install Docker.] ************************************
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: FileNotFoundError: [Errno 2] No such file or directory: '/var/lib/dnf/rpmdb_lock.pid'
fatal: [instance]: FAILED! => {"changed": false, "module_stderr": "Traceback (most recent call last):
  File "<stdin>", line 102, in <module>
  File "<stdin>", line 94, in _ansiballz_main
  File "<stdin>", line 40, in invoke_module
  File "/usr/lib64/python3.7/runpy.py", line 205, in run_module
    return _run_module_code(code, init_globals, run_name, mod_spec)
  File "/usr/lib64/python3.7/runpy.py", line 96, in _run_module_code
    mod_name, mod_spec, pkg_name, script_name)
  File "/usr/lib64/python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/tmp/[...]/ansible_dnf_payload.zip/ansible/modules/packaging/os/dnf.py", line 1304, in <module>
  File "/tmp/[...]/ansible_dnf_payload.zip/ansible/modules/packaging/os/dnf.py", line 1293, in main
  File "/tmp/[...]/ansible_dnf_payload.zip/ansible/modules/packaging/os/dnf.py", line 1272, in run
  File "/tmp/[...]/ansible_dnf_payload.zip/ansible/modules/packaging/os/dnf.py", line 1187, in ensure
  File "/usr/lib/python3.7/site-packages/dnf/base.py", line 869, in do_transaction
    tid = self._run_transaction(cb=cb)
  File "/usr/lib/python3.7/site-packages/dnf/lock.py", line 147, in __exit__
    os.unlink(self.target)
FileNotFoundError: [Errno 2] No such file or directory: '/var/lib/dnf/rpmdb_lock.pid'
", "module_stdout": "", "msg": "MODULE FAILURE
See stdout/stderr for the exact error", "rc": 1}
```

I have been tracking this issue on GitHub for one of my repositories since Fedora 29 in 2018: [Automated tests failing for Fedora 29 with Ansible/Python dnf OSError](https://github.com/geerlingguy/ansible-role-composer/issues/54). After some prodding on that issue by [mafalb](https://github.com/mafalb), I found the problem was systemd was still completing the boot process on Fedora sometimes, and it _usually_ took seconds, but sometimes took minutes. You can run `systemd-analyze` to see how long the boot takes. And the big issue was the `systemd-tmpfiles-setup.service` had not yet run, so DNF didn't have it's pid file yet...

There may be a better way to fix the consistency issue on Fedora, but for now, my fix is to add the following in `pre_tasks` of my playbooks that deal with fresh Fedora instances (in VMs or in containers):

```
  pre_tasks:
    - name: Wait for systemd to complete initialization. # noqa 303
      command: systemctl is-system-running
      register: systemctl_status
      until: "'running' in systemctl_status.stdout"
      retries: 30
      delay: 5
      when: ansible_service_mgr == 'systemd'
      changed_when: false
```

This should work fine on any of the different systemd-powered distros (including any recent version of CentOS, Fedora, Ubuntu, and Debian), and will make your playbook wait until the system is fully booted and ready.

Note: `systemctl is-system-running` could also return `degraded`, if one of the unit files failed startup (for example, on my CentOS 7 images, I sometimes get `Failed to start LSB: Bring up/down networking` for the `network.service`—still working on figuring that one out too :). In that case, you might need to use an or conditional (assuming `degraded` is okay for your environment) like the following:

```
      until: >
        'running' in systemctl_status.stdout or
        'degraded' in systemctl_status.stdout
```

