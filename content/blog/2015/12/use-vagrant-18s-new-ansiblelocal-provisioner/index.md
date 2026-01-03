---
nid: 2615
title: "Use Vagrant 1.8's new ansible_local provisioner for Ansible provisioning"
slug: "use-vagrant-18s-new-ansiblelocal-provisioner"
date: 2015-12-23T05:08:49+00:00
drupal:
  nid: 2615
  path: /blog/use-vagrant-18s-new-ansiblelocal-provisioner
  body_format: full_html
  redirects:
    - /blog/using-vagrant-18s-new-ansiblelocal-provisioner
aliases:
  - /blog/using-vagrant-18s-new-ansiblelocal-provisioner
tags:
  - ansible
  - drupal vm
  - provisioning
  - vagrant
---

I build a <em>lot</em> of local development VMs in a typical week, and need to support Ansible provisioning on Mac, Linux, and Windows workstations (with or without Ansible installed)—<a href="https://hashicorp.com/blog/vagrant-1-8.html">Vagrant 1.8.0</a> was an early Christmas gift for me!

In the past, when I wanted to build a Vagrantfile to provision a VM using an Ansible playbook, I added the following, which used the <a href="https://github.com/geerlingguy/JJG-Ansible-Windows">JJG-Ansible-Windows</a> shell script to install Ansible inside the VM, install role dependencies, and run a given Ansible playbook:

```
  # Use Ansible provisioner if it's installed on host, JJG-Ansible-Windows if not.
  if which('ansible-playbook')
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "#{dir}/provisioning/playbook.yml"
      ansible.sudo = true
    end
  else
    config.vm.provision "shell" do |sh|
      sh.path = "#{dir}/provisioning/JJG-Ansible-Windows/windows.sh"
      sh.args = "/provisioning/playbook.yml"
    end
  end
```

There were a few downsides to this approach: it required inclusion of the JJG-Ansible-Windows script/project in the repository, terminal output was passed through without color (so it's harder to read playbook output), terminal output was had a long delay, and the JJG-Ansible-Windows shell script itself isn't as widely tested as a solution baked into Vagrant.

Vagrant 1.8.0 (and beyond) includes the new <code><a href="https://docs.vagrantup.com/v2/provisioning/ansible_local.html">ansible_local</a></code> provisioner. Instead of using a shell script to install Ansible, install Galaxy roles, and run a playbook, you can pass in options like <code>playbook</code> and <code>galaxy_role_file</code>, and Vagrant does all the hard work:

```
  # Use ansible provisioner if it's installed on host, ansible_local if not.
  if which('ansible-playbook')
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "#{dir}/provisioning/playbook.yml"
    end
  else
    config.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "provisioning/playbook.yml"
      ansible.galaxy_role_file = "provisioning/requirements.yml"
    end
  end
```

The above example is taken from <a href="http://www.drupalvm.com/">Drupal VM</a>, a VM built for easy local Drupal development environments.

Run the playbook on a host without Ansible installed, and you'll notice Vagrant does all the extra work to run the playbook inside the guest:

```
$ vagrant provision
==> drupalvm: Running provisioner: ansible_local...
    drupalvm: Installing Ansible...
    drupalvm: Running ansible-galaxy...
    [...]
    drupalvm: Running ansible-playbook...

PLAY [all] ******************************************************************** 

GATHERING FACTS *************************************************************** 
ok: [drupalvm]
[...]
```

One minor downside to this approach is that, because the <code>ansible-galaxy install</code> command isn't idempotent (see <a href="https://github.com/ansible/ansible/issues/11266">this issue</a>), it will re-download all configured roles every time you run <code>vagrant provision</code>, and depending on how many roles your project requires, this could add a bit of time to the project's provisioning!

For more details and options, be sure to read through the <a href="https://docs.vagrantup.com/v2/provisioning/ansible_local.html">main <code>ansible_local</code> documentation page</a>, as well as the <a href="https://docs.vagrantup.com/v2/provisioning/ansible_common.html">common options</a> shared between both Ansible provisioners.
