---
nid: 2609
title: "Building VM images with Ansible and Packer"
slug: "server-vm-images-ansible-and-packer"
date: 2014-03-31T13:13:50+00:00
drupal:
  nid: 2609
  path: /blog/server-vm-images-ansible-and-packer
  body_format: full_html
  redirects:
    - /blog/ansible-building-images-ansible-and-packer
aliases:
  - /blog/ansible-building-images-ansible-and-packer
  - /blog/server-vm-images-ansible-and-packer
tags:
  - ansible
  - automation
  - packer
  - virtualbox
  - virtualization
  - vmware
---

<blockquote>TL;DR: Go grab the example <a href="https://github.com/geerlingguy/packer-centos-65">packer-centos-65</a> project from GitHub, run <code>$ packer build centos65.json</code>, and you'll end up with a CentOS 6.5 Vagrant box file for VirtualBox. Modify to suit your needs.
</blockquote>

<div style="text-align: center;">
<a href="http://www.ansible.com/">{{< figure src="./ansible-logo.png" alt="Ansible Logo" >}}</a>

+

<a href="http://www.packer.io/">{{< figure src="./packer-logo.png" alt="Packer Logo" >}}</a>
</div>

<a href="http://www.ansible.com/">Ansible</a> is a powerful and simple infrastructure management and server provisioning tool. For provisioning, Ansible is quick to get going over SSH and can be used with dynamic inventories to manage many servers across multiple cloud providers (AWS, Digital Ocean) or other cloud solutions (like VMWare). Usually, provisioning a simple server like a LAMP server, with a secure configuration and all the application settings, will take at least 10-20 minutes—and that's <em>after</em> you've deployed a new instance, droplet, node, etc., which takes anywhere from 30 seconds to 5 minutes!

You can drastically cut down on per-server provisioning time by using custom-made 'boxes' or 'images' that can be deployed instead of default OS installed. Think of these as preconfigured OS instances that might just need a little extra configuration per-instance, or would need a few files updated after the instance is built.

It just so happens there's a tool built to help you do just this—create boxes (for Vagrant), AMIs (for AWS) or images (for Digital Ocean or other services)—called <a href="http://www.packer.io/">Packer</a>. Packer can even build images for multiple providers using multiple provisioners (like shell scripts, Ansible playbooks, Salt states, Chef cookbooks, Puppet manifests or other popular provisioners), all with one set of configuration and instructions.

In this blog post, I'll show you how to build a Vagrant Box file for CentOS 6.5 using Packer with Ansible and a couple simple shell scripts.

<h2>Prerequisites</h2>

To get started, you will need to install the following:

<ul>
<li><a href="http://www.vagrantup.com/downloads.html">Vagrant</a></li>
<li><a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox</a></li>
<li><a href="http://www.packer.io/downloads.html">Packer</a></li>
<li><a href="http://docs.ansible.com/intro_installation.html">Ansible</a></li>
</ul>

<h2>Setting up a Packer JSON template</h2>

Packer uses a simple .json file as a template for its build process. Inside the file, you need to define <code>provisioners</code>, <code>builders</code>, and <code>post-processors</code> (at a minimum) which will help build, configure, and compress and save your VM image.

Let's take a look at the entire file that we are going to use, and I'll explain the different parts:

```
{
  "provisioners": [
    {
      "type": "shell",
      "execute_command": "echo 'vagrant' | {{.Vars}} sudo -S -E bash '{{.Path}}'",
      "script": "scripts/ansible.sh"
    },
    {
      "type": "ansible-local",
      "playbook_file": "ansible/main.yml",
      "role_paths": [
        "/etc/ansible/roles/geerlingguy.packer-rhel"
      ]
    },
    {
      "type": "shell",
      "execute_command": "echo 'vagrant' | {{.Vars}} sudo -S -E bash '{{.Path}}'",
      "script": "scripts/cleanup.sh"
    }
  ],
  "builders": [
    {
      "type": "virtualbox-iso",
      "boot_command": [
        "<tab> text ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ks.cfg<enter><wait>"
      ],
      "boot_wait": "10s",
      "disk_size": 20480,
      "guest_os_type": "RedHat_64",
      "headless": true,
      "http_directory": "http",
      "iso_urls": [
        "iso/CentOS-6.5-x86_64-minimal.iso",
        "http://centos.mirrors.hoobly.com/6.5/isos/x86_64/CentOS-6.5-x86_64-minimal.iso"
      ],
      "iso_checksum_type": "md5",
      "iso_checksum": "0d9dc37b5dd4befa1c440d2174e88a87",
      "ssh_username": "vagrant",
      "ssh_password": "vagrant",
      "ssh_port": 22,
      "ssh_wait_timeout": "10000s",
      "shutdown_command": "echo 'vagrant'|sudo -S /sbin/halt -h -p",
      "guest_additions_path": "VBoxGuestAdditions_{{.Version}}.iso",
      "virtualbox_version_file": ".vbox_version",
      "vm_name": "packer-centos-6.5-x86_64",
      "vboxmanage": [
        [
          "modifyvm",
          "{{.Name}}",
          "--memory",
          "512"
        ],
        [
          "modifyvm",
          "{{.Name}}",
          "--cpus",
          "2"
        ]
      ]
    }
  ],
  "post-processors": [
    {
      "output": "builds/VirtualBox-centos65.box",
      "type": "vagrant"
    }
  ]
}
```

First, we have three provisioners; a shell script that installs Ansible (in our case, for CentOS 6.x, it simply installs the EPEL repository and installs ansible via <code>yum</code>), then an Ansible playbook that calls the role <a href="https://galaxy.ansible.com/list#/roles/671">geerlingguy.packer-rhel</a> (which configures RHEL/CentOS for Vagrant), and finally a cleanup shell script that clears off unused space to save a few MB in the resulting disk image.

Next, the builders are defined (since we're only interested in building a VirtualBox image, there's only one). One of the first options, <code>boot_command</code>, gives a command to run on system boot; for CentOS, we kick off a <a href="http://www.centos.org/docs/5/html/Installation_Guide-en-US/ch-kickstart2.html">Kickstart installation</a> using a <code>ks.cfg</code> script that we save in an 'http' folder in the same folder as our template file. Next, we give some general options for the system (like the shutdown command, SSH port to use, username and password, a set of <code>iso_urls</code> to use to download the actual OS image to be used for installation, and other required attributes as per <a href="http://www.packer.io/docs/templates/builders.html">Packer's builder documentation</a>.

Finally, we define a <code>vagrant</code> post-processor, which simply creates the .box file at the path defined in the <code>output</code> parameter.

<h2>Building shell scripts to set up and clean up</h2>

Now that we have a template file, we need to fill in some of the files we referenced. I keep all my shell scripts in a 'scripts' folder, and we've defined two:

<strong>ansible.sh</strong>:

```
#!/bin/bash -eux

# Install EPEL repository.
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

# Install Ansible.
yum -y install ansible
```

<strong>cleanup.sh</strong>:

```
#!/bin/bash -eux

# Zero out the rest of the free space using dd, then delete the written file.
dd if=/dev/zero of=/EMPTY bs=1M
rm -f /EMPTY

# Add `sync` so Packer doesn't quit too early, before the large file is deleted.
sync
```

<h2>Using Ansible for the necessary Vagrant box requisites</h2>

There are plenty of examples of people using a bunch of shell scripts to do the necessary setup to get a Vagrant box or VMWare image configured (one of the best examples is the entire Bento project), but I couldn't find many examples using Ansible.

So, I built a role that does all the grunt-work for you, and you can install it (if you have Ansible 1.4.2 or later installed on your system) with the command <code>$ ansible-galaxy install geerlingguy.packer-rhel</code>. Now, just create a file <code>main.yml</code> in an 'ansible' subdirectory, with the following contents:

```
---
- hosts: all
  sudo: yes
  gather_facts: yes
  roles:
    - geerlingguy.packer-rhel
```

Note that you can add more roles, tasks, etc. here, but as stated in the <a href="http://www.packer.io/docs/provisioners/ansible-local.html">ansible-local</a> provisioner documentation, since the playbook is run from within the provisioned instance, over a local connection, you need to tell Packer to copy all the relevant roles and other files up to the server so they'll be available when the Ansible provisioner is run.

This means it's probably a good idea to wrap up the things you need to do in roles, or use some pre-built roles from <a href="https://galaxy.ansible.com/">Ansible Galaxy</a>, and customize to suit your needs. That way you don't have to copy up a hundred files defined in your .json template file!

<h2>Putting it all together and next steps</h2>

Assuming you've done everything correctly, and also added this <a href="">ks.cfg</a> file inside an 'http' subdirectory, you can change directory to the folder containing the Packer .json template, and run the command <code>$ packer build [template-name].json</code>. A few minutes later, you'll have a Vagrant box that you can share with other developers or deploy to VMs for testing.

If you want to save yourself some work, go grab the example <a href="https://github.com/geerlingguy/packer-centos-65">packer-centos-65</a> project from GitHub (which contains all the code I've demonstrated in this post), and customize to suit your needs—or just build it as-is to get a simple CentOS 6.5 x86-64 Vagrant box file.

This post gave a nice, short introduction to how Packer works, and how you can do provision Vagrant box files for VirtualBox, but Packer's true strength is the ability to build all kinds of image files—for Amazon, Digital Ocean, VirtualBox, VMWare, and other providers—quickly and easily. And you're not limited to CentOS, or even Linux, either; you can work with just about any flavor of Linux, or build Windows or Mac OS X images, provided you have the proper licenses and infrastructure! You can even <a href="http://www.packer.io/docs/builders/docker.html">build Docker images</a> without using a Dockerfile!

<h2>Further resources</h2>

<ul>
<li>Many more good Packer examples are available in opscode's <a href="https://github.com/opscode/bento">Bento</a> repository on GitHub.</li>
<li>If you're interested in learning more about Ansible, please check out my book, <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>.</li>
</ul>
