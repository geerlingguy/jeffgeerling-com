---
date: '2026-11-25T15:43:00-06:00'
tags: ['ansible', 'ubuntu', 'server', 'rust', 'sudo', 'sudo-rs']
title: 'Ansible Fails waiting for privilege escalation on Ubuntu 26'
slug: 'ansible-fails-become-ubuntu2604'
# description: 'description_here'
---
I've slowly been moving my servers from Ubuntu 22 and 24 to 26 this year, and noticed my Ansible automation starts failing if I have password protection for `sudo` use:

```
$ ansible-playbook main.yml -K
BECOME password: 

PLAY [Security] *******************************************************

TASK [Gathering Facts] ***********************************************************************
fatal: [my-server.local]: FAILED! => 
    msg: 'Timeout (12s) waiting for privilege escalation prompt: '
```

Apparently Ubuntu's been rewriting system utilities in Rust, and the `sudo-rs` version that ships on Ubuntu 26.04 has some incompatiblities with the `sudo` I've used on servers for 20+ years.

It prints an extra string before the password prompt, which `sudo` doesn't do, and that can confuse automation tools like Ansible that wait for a specific prompt.

There's a thread in the Ansible project covering the issue: [validate sudo become plugin against sudo-rs
](https://github.com/ansible/ansible/issues/85837). The fix landed in Ansible Core 2.22.0, and is being backported into updates in 2.16, 2.18, 2.19, 2.20, and maybe also 2.21 (it's quite disruptive!). It looks like it also broke [pyinfra](https://github.com/pyinfra-dev/pyinfra/pull/1734), and their fix is in the latest release of 3.11.

I updated Ansible (`pip install -U ansible`) and now `-K` (`--ask-become-pass`) works again.

Another alternative is to use the traditional version of `sudo` that still ships with Ubuntu 26. For that, the easiest way is to set the `become_exe` inside your hosts file:

```
dell-precision.local ansible_become_exe=sudo.ws
```

Or you could even revert `sudo` systemwide on your Ubuntu host:

```
update-alternatives --config sudo
```

I'm not sure why Ubuntu sees the need to [rewrite common Linux utils in Rust](https://www.abdallaelmorsi.net/ubuntu-rust-coreutils-migration-what-actually-breaks-in-scripts-and-how-to-fix-it/). I don't mind Rust, but these are foundational tools every Linux system relies on. This isn't a window manager, where experimentation is more acceptable[^oldman].

If other distros plan on moving to `sudo-rs` that's one thing, but if it's just Ubuntu, maybe I should hop back to Debian for everything, and not just my cloud servers.

[^oldman]: Yes, I know this makes me sound like "old man yells at [rust]," but major changes to structural components of Linux _should_ take longer, IMO. At least on the Red Hat side, we have Fedora, which is more bleeding edge, then at least a few years' gap before it hits 'production' systems. With Ubuntu, there is no cutting edge upstream where things like this can be fixed or worked around before hitting prod! (And no, I don't consider non-LTS Ubuntu releases the same thing.)
