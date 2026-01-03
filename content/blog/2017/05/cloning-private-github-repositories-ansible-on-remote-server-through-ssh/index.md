---
nid: 2771
title: "Cloning private GitHub repositories with Ansible on a remote server through SSH"
slug: "cloning-private-github-repositories-ansible-on-remote-server-through-ssh"
date: 2017-05-01T14:44:38+00:00
drupal:
  nid: 2771
  path: /blog/2018/cloning-private-github-repositories-ansible-on-remote-server-through-ssh
  body_format: markdown
  redirects:
    - /blog/2017/cloning-private-github-repositories-ansible-on-remote-server-through-ssh
aliases:
  - /blog/2017/cloning-private-github-repositories-ansible-on-remote-server-through-ssh
tags:
  - ansible
  - git
  - github
  - security
  - ssh
  - ssh-agent
---

One of Ansible's strengths is the fact that its 'agentless' architecture uses SSH for control of remote servers. And one classic problem in remote Git administration is authentication; if you're cloning a private Git repository that requires authentication, how can you do this while also protecting your own private SSH key (by not copying it to the remote server)?

As an example, here's a task that clones a private repository to a particular folder:

```
- name: Clone a private repository into /opt.
  git:
    repo: git@github.com:geerlingguy/private-repo.git
    version: master
    dest: /opt/private-repo
    accept_hostkey: yes
  # ssh-agent doesn't allow key to pass through remote sudo commands.
  become: no
```

If you run this task, you'll probably end up with something like:

```
TASK [geerlingguy.role : Clone a private repository into /opt.] *******************************************
fatal: [server]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /opt/private-repo", "failed": true, "msg": "Cloning into '/opt/private-repo'...\nWarning: Permanently added the RSA host key for IP address 'server' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/opt/private-repo'...\nWarning: Permanently added the RSA host key for IP address 'server' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stderr_lines": ["Cloning into '/opt/private-repo'...", "Warning: Permanently added the RSA host key for IP address 'server' to the list of known hosts.", "Permission denied (publickey).", "fatal: Could not read from remote repository.", "", "Please make sure you have the correct access rights", "and the repository exists."], "stdout": "", "stdout_lines": []}
```

(Or, more succinctly: `Permission denied (publickey).`, meaning GitHub refused the clone request.)

The problem is you have an SSH key locally that allows access to the Git repository, but the remote server doesn't see that key (even if you have `ssh-agent` running and your key loaded via `ssh-add`).

The simplest solutions are either:

  1. Add a task that copies your local SSH private key to the remote server. (I tend to avoid doing this—if the remote server is ever hacked, your own private key would be exposed!)
  2. Add a task that generates a private key on the remote server, then another task (or manual step) of adding the generated public key to GitHub, so that server can authenticate for Git commands.

But if you want to avoid having any private keys on the remote server (sometimes this can be a necessary security requirement), you can pass your own private key through to the remote server via Ansible's SSH connection.

## Using SSH Agent

First, add the following SSH configuration to your `~/.ssh/config` file:

```
Host [server-address-here] [ip-address-here]
    ForwardAgent yes
```

This enables forwarding keys loaded into `ssh-agent` to remote SSH connections.

Check which keys are loaded currently using `ssh-add -l`, and add any additional required keys using `ssh-add ~/.ssh/key-here`.

The next time you run the Git task in your playbook, you should see something like:

```
TASK [geerlingguy.role : Clone a private repository into /opt.] *******************************************
changed: [server]
```

Any time you run the Ansible playbook (or ad hoc tasks), the Ansible's SSH connection will hold all the loaded SSH Agent keys, so you can perform private Git repository operations without tasks failing.

## Copying a key to the server

The other method, which I tend to avoid as I don't like having keys on remote servers too often, is to copy a private key to the server then use it for the `git` operation. As an example, I recently set up an Apache-based Ubuntu webserver with an application codebase cloned into the `/var/www/html` docroot, and used the following tasks to copy a GitHub deploy key into place and use it:

```
- name: Ensure /var/www/html directory has correct permissions.
  file:
    path: /var/www/html
    state: directory
    owner: www-data
    group: www-data

- name: Ensure .ssh directory exists.
  file:
    path: /var/www/.ssh
    state: directory
    mode: 0700
    owner: www-data
    group: www-data

- name: Ensure GitHub deploy key is present on the server.
  copy:
    content: "{{ deploy_private_key }}"
    dest: /var/www/.ssh/deploy_key
    mode: 0600
    owner: www-data
    group: www-data

# See: https://stackoverflow.com/a/37096534/100134
- name: Ensure setfacl support is present.
  package: name=acl

- name: Clone the code repository to the docroot.
  git:
    repo: "{{ git_repo }}"
    dest: /var/www/html
    accept_hostkey: yes
    key_file: /var/www/.ssh/deploy_key
  become_user: www-data
```

