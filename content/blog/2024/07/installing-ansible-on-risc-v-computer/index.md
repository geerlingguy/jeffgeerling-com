---
nid: 3388
title: "Installing Ansible on a RISC-V computer"
slug: "installing-ansible-on-risc-v-computer"
date: 2024-07-02T18:16:37+00:00
drupal:
  nid: 3388
  path: /blog/2024/installing-ansible-on-risc-v-computer
  body_format: markdown
  redirects: []
tags:
  - ansible
  - compile
  - linux
  - pip
  - python
  - risc-v
  - rust
  - sbc
---

Ansible runs on Python, and Python runs on... well pretty much _everything_. Including newer RISC-V machines.

But Ansible has a lot of dependencies, and some of these dependencies have caused frustration from time to time on x86 and Arm (so having issues with a dependency is just a way of life when you enter [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell))... but in this case, for the past few months, I've never had luck installing Ansible from PyPI (Python's Package Index) on any RISC-V system, using `pip install ansible`.

I prefer installing this way (rather than compiling from source or from system packages) because it generally gets the latest version of Ansible, with an easy upgrade/downgrade path. It's also easy to add `ansible` to a Python `requirements.txt` file and install it alongside other package dependencies.

> **UPDATE 2025-02**: It seems that at least under Ubuntu's latest releases, Ansible installs with a simple `pip install ansible` again, no need for the extra steps below. Yay!

Regardless, the `cryptography` library, which requires a Rust compiler to build if the package is not already built for a particular system, has made it difficult to install Ansible from `pip`:

```
      copying src/cryptography/hazmat/bindings/_rust/openssl/x448.pyi -> build/lib.linux-riscv64-cpython-310/cryptography/hazmat/bindings/_rust/openssl
      running build_ext
      running build_rust
      error: can't find Rust compiler
      
      If you are using an outdated pip version, it is possible a prebuilt wheel is available for this package but pip is not able to install from it. Installing from the wheel would avoid the need for a Rust compiler.
      
      To update pip, run:
      
          pip install --upgrade pip
      
      and then retry package installation.
      
      If you did intend to build this package from source, try installing a Rust compiler from your system package manager and ensure it is on the PATH during installation. Alternatively, rustup (available at https://rustup.rs) is the recommended way to download and update the Rust compiler toolchain.
      
      This package requires Rust >=1.63.0.
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for cryptography
  Building wheel for MarkupSafe (setup.py) ... done
  Created wheel for MarkupSafe: filename=MarkupSafe-2.1.5-cp310-cp310-linux_riscv64.whl size=23821 sha256=da37d67f972b1023bca608d3c5a2038e1f99061240ccd1a57a2d9a30baeddf3d
  Stored in directory: /home/user/.cache/pip/wheels/2a/04/fa/f54a9011eaf18a437110e8171478b3e963dc249ed60ce77f17
Successfully built PyYAML MarkupSafe
Failed to build cryptography
ERROR: Could not build wheels for cryptography, which is required to install pyproject.toml-based projects
```

See [this GitHub issue](https://github.com/geerlingguy/top500-benchmark/issues/35) for a bit more.

After posting about this on Twitter/X, [user @mediocreDevops followed up with a solution](https://x.com/mediocredevops/status/1808147686043865377?s=43), which he [details in this GitHub Gist](https://gist.github.com/afro-coder/2b1f96ca31880fb66795b6dc15763e78).

I followed along and tried to do this on a Milk-V Mars SBC I'm testing currently ([see test results here](https://github.com/geerlingguy/sbc-reviews/issues/46)), and here's how I tried installing it:

  1. [Install `rustup`](https://www.rust-lang.org/tools/install): `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` (choose the 'default' option)
  2. Make sure your shell has the rust env vars added: `. "$HOME/.cargo/env"` (or log out and back in)
  3. Make sure other dependencies are installed: `sudo apt install -y pkg-config python3-pip`
  4. Install Ansible: `pip3 install ansible`

Unfortunately, it was locking up, so I rebooted and tried again, but it errored out with `IndexError: list index out of range` since it seemed to be trying to get Rust's version and failing. `rustc --version` was returning nothing, so I reinstalled rust:

```
user@milkv:~$ rustup uninstall stable
...
user@milkv:~$ rustup install stable
```

After doing that, I tried installing `ansible` yet again:

```
user@milkv:~$ rustc --version
rustc 1.79.0 (129f3b996 2024-06-10)
user@milkv:~$ pip3 install ansible
...
Successfully installed MarkupSafe-2.1.5 PyYAML-6.0.1 ansible-10.1.0 ansible-core-2.17.1 cffi-1.16.0 cryptography-42.0.8 jinja2-3.1.4 packaging-24.1 pycparser-2.22 resolvelib-1.0.1
user@milkv:~$ export PATH=$PATH:/home/user/.local/bin
user@milkv:~$ ansible --version
ERROR: Ansible could not initialize the preferred locale: unsupported locale setting
```

Running it with a locale environment variable Ansible is happy with (see [this issue for more details](https://github.com/NixOS/nixpkgs/issues/223151)):

```
user@milkv:~$ LC_ALL="C.UTF-8" ansible --version
ansible [core 2.17.1]
  config file = None
  configured module search path = ['/home/user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/user/.local/lib/python3.10/site-packages/ansible
  ansible collection location = /home/user/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/user/.local/bin/ansible
  python version = 3.10.9 (main, Dec  7 2022, 13:47:07) [GCC 12.2.0] (/usr/bin/python3)
  jinja version = 3.1.4
  libyaml = False
```

So we got it going... eventually. Hopefully as RISC-V becomes a bit more widespread, things like more universal wheels will exist in that ecosystem like they do Arm today. And if not, hopefully installation of things like the Rust language become a little simpler / more stable!
