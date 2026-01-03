---
nid: 2705
title: "Using Ansible through Windows 10's Subsystem for Linux"
slug: "using-ansible-through-windows-10s-subsystem-linux"
date: 2016-10-05T20:51:15+00:00
drupal:
  nid: 2705
  path: /blog/2017/using-ansible-through-windows-10s-subsystem-linux
  body_format: markdown
  redirects:
    - /blog/2016/using-ansible-through-windows-10s
    - /blog/2016/using-ansible-through-windows-10s-subsystem-linux
aliases:
  - /blog/2016/using-ansible-through-windows-10s
  - /blog/2016/using-ansible-through-windows-10s-subsystem-linux
tags:
  - ansible
  - bash
  - command line
  - how-to
  - linux
  - tutorial
  - ubuntu
  - windows
  - windows 10
---

Ever since I heard about the new 'Beta' Windows Subsystem for Linux, which basically installs an Ubuntu LTS release inside of Windows 10 (currently 14.04), I've been meaning to give it a spin, and see if it can be a worthy replacement for Cygwin, Git shell, Cmder, etc. And what I was _most_ interested in was whether I could finally point people to a more stable and friendly way of using Ansible on a Windows workstation.

In the past, there was the option of [running Ansible inside Cygwin](/blog/running-ansible-within-windows) (and this is still the best way to try getting Ansible working in an older Windows environment), but this always felt kludgy to me, and I hated having to recommend either that or forcing Windows users to do a full Linux VM installation just to run Ansible commands. I finally updated my PC laptop to the latest Windows 10 Anniversary Update, and installed the Windows Subsystem for Linux, and lo and behold, Ansible works!

<p style="text-align: center;">{{< figure src="./ansible-on-windows-ubuntu-bash.png" alt="Ansible running on Windows in the Ubuntu Bash shell" width="650" height="349" class="insert-image" >}}</p>

In this blog post, I'll show you how to install and use Ansible on Windows 10.

## Installing Bash on Windows 10

> For reference, here are the official instructions from Microsoft: [Bash on Ubuntu on Windows - Installation Guide](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide).

Before installing the Linux Subsystem, you have to have:

  - Windows 10 (Anniversary update or later version)
  - 64-bit installation (can't run on 32-bit systems)

Once you verify your system is 64-bit and up to date, you have to do a few manual steps to enable the 'Windows Subsystem for Linux':

  1. Open 'Settings' (the cog in the start menu)
  2. Click 'Update & Security', then click the 'For developers' option on the left.
  3. Toggle the 'Developer mode' option, and accept any warnings Windows pops up.

Wait a minute for Windows to install a few things in the background (it will eventually let you know a restart may be required for changes to take effect—ignore that for now). Next, to install the actual Linux Subsystem, you have to jump over to 'Control Panel' (_why is this separate from 'Settings'?_), and do the following:

  1. Click on 'Programs'
  2. Click on 'Turn Windows features on or off'
  3. Scroll down and check 'Windows Subsystem for Linux (Beta)', and then click OK.

The subsystem will be installed, then Windows will require a reboot. Reboot, then open up the start menu and enter 'bash' (to open up 'Bash' installation in a new command prompt). Fill out all the questions (it will have you create a separate user account for the Linux subsystem), and once that's all done (it takes a few minutes to install), you will _finally_ have Ubuntu running on your Windows laptop, _somewhat_ integrated with Windows.

## Installing Ansible

To install Ansible, since we're basically in an Ubuntu environment, it's as simple as installing pip, then installing Ansible:

  1. Open a bash prompt (from start menu, type 'bash' and hit enter).
  2. Install Pip: `sudo apt-get -y install python-pip python-dev libffi-dev libssl-dev`
  3. Install Ansible: `pip install ansible --user` (`--user` installs packages local to the user account instead of globally to avoid permissions issues with Pip and the Linux Subsystem)
  4. Since the `ansible*` commands are installed under `~/.local/bin`, we need to add that to the $PATH, so run the command: `echo 'PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc`
  5. Either exit out of the bash prompt and start it again from the Windows menu, or run `source .bashrc` to update your `$PATH` to include Ansible.

> Note the use of `--user` for the `pip install` command; due to some peculiarities of the way the Linux subsystem works, Pip can't easily install packages globally, so we install packages just for the user account we set up for bash.

## Using Ansible

At this point, `which ansible` should show the path to Ansible, `ansible --version` should show you Ansible's version, and you should be able to use `ansible` and the rest of the command-line tools (e.g. `ansible-playbook`, `ansible-galaxy`, etc.) as you would on any common environment.

> If you get the error message `ImportError: No module named markupsafe`, try installing markupsafe manually with `pip install markupsafe --user`. See [this GitHub issue](https://github.com/ansible/ansible/issues/13570) for more detail.

If you want to run a playbook that's stored in your Windows user account's Documents folder (e.g. `C:\Users\jgeerling\Documents`), you can do so by navigating to `/mnt/c/Users/jgeerling/Documents` (where `jgeerling` is your username). Windows drives are mounted in the Subsystem inside the `/mnt` directory. Let's create a test playbook and see if it works!

  1. Open a bash prompt, and `cd` into your Windows user's Documents directory: `cd /mnt/c/Users/jgeerling/Documents`.
  2. Create a new test playbook: `touch test.yml`
  3. User nano or some other editor to add the following contents:
          
          ---
          - hosts: localhost
            tasks:
              - debug: msg="Ansible is working!"
  4. Run the playbook with the command `ansible-playbook test.yml --connection=local`

Ansible should run the command and print out the debug message. Ansible might warn about no inventory file being present, but since you're using `--connection=local`, the `localhost` host should automatically work.

<p style="text-align: center;">{{< figure src="./ansible-playbook-working-widows-ubuntu-bash.png" alt="Ansible test playbook running on Windows in the Ubuntu Bash shell" width="650" height="349" class="insert-image" >}}</p>

## Going further

Now that you have Ansible installed, you can start automating everything (even including the rest of the bash environment)! If you need to, you can [generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) for use connecting to servers, use `ssh` to directly connect to servers, etc. It's basically a full Ubuntu LTS install running inside Windows!
