---
nid: 3308
title: "How to solve \"error: externally-managed-environment\" when installing via pip3"
slug: "how-solve-error-externally-managed-environment-when-installing-pip3"
date: 2023-08-30T19:18:30+00:00
drupal:
  nid: 3308
  path: /blog/2023/how-solve-error-externally-managed-environment-when-installing-pip3
  body_format: markdown
  redirects: []
tags:
  - debian
  - linux
  - pip
  - python
  - server
  - sysadmin
---

On Debian 12 Bookworm, Ubuntu 24.04 Noble Numbat, and macOS 14+ installs, when I try running `pip3 install [something]` (whether that's Ansible or some other Python tool), I get the following error message:

```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.11/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

The error message says you can pass in the flag `--break-system-packages` but that sounds terrifying. I just want pip to stop nagging me, but let me manage my system dependencies like I have for many years.

I think some Python developers _really_ want people like me to [use virtual environments](https://docs.python-guide.org/dev/virtualenvs/), but that's way too much effort when I don't really care to do that, thankyouverymuch. If you want to use `venv` more power to you. I just like getting stuff done on my little servers.

The easiest solution is to delete the `EXTERNALLY-MANAGED` file in your system Python installation:

```
sudo rm -rf /usr/lib/python3.11/EXTERNALLY-MANAGED
```

If using Ansible, you can add this task to your playbook prior to running any `pip` tasks:

```yaml
- name: Ignore PEP 668 because it's silly.
  ansible.builtin.file:
    path: /usr/lib/python3.11/EXTERNALLY-MANAGED
    state: absent
```

Ansible also has a new `break_system_packages` option for the pip module, so if you just need to do it once:

```yaml
- name: Install package via pip.
  ansible.builtin.pip:
    name: "package_name_here"
    state: present
    break_system_packages: true
  become: true
```

Note that the `python3.11` version number should match whatever you have installed—it was 3.11 at the time of this blog post's writing.

  - For Ubuntu 24.02, the version is `python3.12`
  - For macOS, use `find /opt/homebrew -name EXTERNALLY-MANAGED` to find the location (or `find /usr/local -name EXTERNALLY-MANAGED` on Intel Macs)

See [this answer on Stack Overflow](https://stackoverflow.com/a/75722775/100134) for more. Another interesting option is to install and use [pipx](https://pypa.github.io/pipx/), which does the grunt work of managing the `venv`s for you.
