---
nid: 2601
title: "Simple GlusterFS Setup with Ansible"
slug: "simple-glusterfs-setup-ansible"
date: 2015-07-27T15:19:14+00:00
drupal:
  nid: 2601
  path: /blog/simple-glusterfs-setup-ansible
  body_format: full_html
  redirects:
    - /blog/simple-glusterfs-setup-ansible-redux
aliases:
  - /blog/simple-glusterfs-setup-ansible-redux
  - /blog/simple-glusterfs-setup-ansible
tags:
  - ansible
  - ansible for devops
  - glusterfs
  - infrastructure
  - storage
---

<blockquote>
The following is an excerpt from Chapter 8 of <a href="https://www.ansiblefordevops.com/">Ansible for DevOps</a>, a book on Ansible by Jeff Geerling.
</blockquote>

<p>Modern infrastructure often involves some amount of horizontal scaling; instead of having one giant server, with one storage volume, one database, one application instance, etc., most apps use two, four, ten, or dozens of servers.</p>

<p style="text-align: center;">{{< figure src="./glusterfs-architecture-diagram.jpg" alt="GlusterFS Architecture Diagram" width="550" height="338" class="inserted-image" >}}</p>

<p>Many applications can be scaled horizontally with ease, but what happens when you need shared resources, like files, application code, or other transient data, to be shared on all the servers? And how do you have this data scale out with your infrastructure, in a fast but reliable way? There are many different approaches to synchronizing or distributing files across servers:</p>

<ul>
<li>Set up rsync either on cron or via inotify to synchronize smaller sets of files on a regular basis.</li>
<li>Store everything in a code repository (e.g. Git, SVN, etc.) and deploy files to each server using Ansible.</li>
<li>Have one large volume on a file server and mount it via NFS or some other file sharing protocol.</li>
<li>Have one master SAN that's mounted on each of the servers.</li>
<li>Use a distributed file system, like Gluster, Lustre, Fraunhofer, or Ceph.</li>
</ul>

<p>Some options are easier to set up than others, and all have benefits—and drawbacks. Rsync, git, or NFS offer simple initial setup, and low impact on filesystem performance (in many scenarios). But if you need more flexibility and scalability, less network overhead, and greater fault tolerance, you will have to consider something that requires more configuration (e.g. a distributed file system) and/or more hardware (e.g. a SAN).</p>

<p>GlusterFS is licensed under the AGPL license, has good documentation, and a fairly active support community (especially in the #gluster IRC channel). But to someone new to distributed file systems, it can be daunting to get set it up the first time.</p>

<h2>
<a id="user-content-configuring-gluster---basic-overview" class="anchor" href="#configuring-gluster---basic-overview" aria-hidden="true"><span class="octicon octicon-link"></span></a>Configuring Gluster - Basic Overview</h2>

<p>To get Gluster working on a basic two-server setup (so you can have one folder that's synchronized and replicated across the two servers—allowing one server to go down completely, and the other to still have access to the files), you need to do the following:</p>

<ol>
<li>Install Gluster server and client on each server, and start the server daemon.</li>
<li>(On both servers) Create a 'brick' directory (where Gluster will store files for a given volume).</li>
<li>(On both servers) Create a directory to be used as a mount point (a directory where you'll have Gluster mount the shared volume).</li>
<li>(On both servers) Use <code>gluster peer probe</code> to have Gluster connect to the other server.</li>
<li>(On one server) Use <code>gluster volume create</code> to create a new Gluster volume.</li>
<li>(On one server) Use <code>gluster volume start</code> to start the new Gluster volume.</li>
<li>(On both servers) Mount the gluster volume (adding a record to <code>/etc/fstab</code> to make the mount permanent).</li>
</ol>

<p>Additionally, you need to make sure you have the following ports open on both servers (so Gluster can communicate): TCP ports 111, 24007-24011, 49152-49153, and UDP port 111. (You need to add an additional TCP port in the 49xxx range for each extra server in your Gluster cluster.)</p>

<h2>
<a id="user-content-configuring-gluster-with-ansible" class="anchor" href="#configuring-gluster-with-ansible" aria-hidden="true"><span class="octicon octicon-link"></span></a>Configuring Gluster with Ansible</h2>

<p>For demonstration purposes, we'll set up a simple two-server infrastructure using Vagrant, and create a shared volume between the two, with two replicas (meaning all files will be replicated on each server). As your infrastructure grows, you can set other options for data consistency and transport according to your needs.</p>

<p>To build the two-server infrastructure locally, create a folder <code>gluster</code> containing the following <code>Vagrantfile</code>:</p>

```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Base VM OS configuration.
  config.vm.box = "geerlingguy/ubuntu1404"
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.ssh.insert_key = false

  config.vm.provider :virtualbox do |v|
    v.memory = 256
    v.cpus = 1
  end

  # Define two VMs with static private IP addresses.
  boxes = [
    { :name => "gluster1", :ip => "192.168.29.2" },
    { :name => "gluster2", :ip => "192.168.29.3" }
  ]

  # Provision each of the VMs.
  boxes.each do |opts|
    config.vm.define opts[:name] do |config|
      config.vm.hostname = opts[:name]
      config.vm.network :private_network, ip: opts[:ip]

      # Provision both VMs using Ansible after the last VM is booted.
      if opts[:name] == "gluster2"
        config.vm.provision "ansible" do |ansible|
          ansible.playbook = "playbooks/provision.yml"
          ansible.inventory_path = "inventory"
          ansible.limit = "all"
        end
      end
    end
  end

end
```

<p>This configuration creates two servers, <code>gluster1</code> and <code>gluster2</code>, and will run a playbook at <code>playbooks/provision.yml</code> on the servers defined in an <code>inventory</code> file in the same directory as the Vagrantfile.</p>

<p>Create the <code>inventory</code> file to help Ansible connect to the two servers:</p>

```
[gluster]
192.168.29.2
192.168.29.3

[gluster:vars]
ansible_ssh_user=vagrant
ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key
```

<p>Now, create a playbook named <code>provision.yml</code> inside a <code>playbooks</code> directory:</p>

```
---
- hosts: gluster
  sudo: yes

  vars_files:
    - vars.yml

  roles:
    - geerlingguy.firewall
    - geerlingguy.glusterfs

  tasks:
    - name: Ensure Gluster brick and mount directories exist.
      file: "path={{ item }} state=directory mode=0775"
      with_items:
        - "{{ gluster_brick_dir }}"
        - "{{ gluster_mount_dir }}"

    - name: Configure Gluster volume.
      gluster_volume:
        state: present
        name: "{{ gluster_brick_name }}"
        brick: "{{ gluster_brick_dir }}"
        replicas: 2
        cluster: "{{ groups.gluster | join(',') }}"
        host: "{{ inventory_hostname }}"
        force: yes
      run_once: true

    - name: Ensure Gluster volume is mounted.
      mount:
        name: "{{ gluster_mount_dir }}"
        src: "{{ inventory_hostname }}:/{{ gluster_brick_name }}"
        fstype: glusterfs
        opts: "defaults,_netdev"
        state: mounted
```

<p>This playbook uses two roles to set up a firewall and install the required packages for GlusterFS to work. You can manually install both of the required roles with the command <code>ansible-galaxy install geerlingguy.firewall geerlingguy.glusterfs</code>, or add them to a <code>requirements.txt</code> file and install with <code>ansible-galaxy install -r requirements.txt</code>.</p>

<p>Gluster requires a 'brick' directory to use as a virtual filesystem, and our servers also need a directory where the filesystem can be mounted, so the first <code>file</code> task ensures both directories exist (<code>gluster_brick_dir</code> and <code>gluster_mount_dir</code>). Since we need to use these directory paths more than once, we use variables which will be defined later, in <code>vars.yml</code>.</p>

<p>Ansible's <code>gluster_volume</code> module (added in Ansible 1.9) does all the hard work of probing peer servers, setting up the brick as a Gluster filesystem, and configuring the brick for replication. Some of the most important configuration parameters for the <code>gluster_volume</code> module include:</p>

<ul>
<li>
<code>state</code>: Setting this to <code>present</code> makes sure the brick is present. It will also start the volume when it is first created by default, though this behavior can be overridden by the <code>start_on_create</code> option.</li>
<li>
<code>name</code> and <code>brick</code> give the Gluster brick a name and location on the server, respectively. In this example, the brick will be located on the boot volume, so we also have to add <code>force: yes</code>, or Gluster will complain about not having the brick on a separate volume.</li>
<li>
<code>replicas</code> tells Gluster how many replicas to ensure exist; this number can vary depending on how many servers you have in the brick's <code>cluster</code>, and how tolerance you have for server outages. We won't get much into tuning GlusterFS for performance and resiliency, but most situations warrant a value of <code>2</code> or <code>3</code>.</li>
<li>
<code>cluster</code> defines all the hosts which will contain the distributed filesystem. In this case, all the <code>gluster</code> servers in our Ansible inventory should be included, so we use a Jinja2 <code>join</code> filter to join all the addresses into a list.</li>
<li>
<code>host</code> sets the host for peer probing explicitly. If you don't set this, you can sometimes get errors on brick creation, depending on your network configuration.</li>
</ul>

<p>We only need to run the <code>gluster_volume</code> module once for all the servers, so we add <code>run_once: true</code>.</p>

<p>The last task in the playbook uses Ansible's <code>mount</code> module to ensure the Gluster volume is mounted on each of the servers, in the <code>gluster_mount_dir</code>.</p>

<p>After the playbook is created, we need to define all the variables used in the playbook. Create a <code>vars.yml</code> file inside the <code>playbooks</code> directory, with the following variables:</p>


```
---
# Firewall configuration.
firewall_allowed_tcp_ports:
  - 22
  # For Gluster.
  - 111
  # Port-mapper for Gluster 3.4+.
  # - 2049
  # Gluster Daemon.
  - 24007
  # 24009+ for Gluster <= 3.3; 49152+ for Gluster 3.4+.
  - 24009
  - 24010
  # Gluster inline NFS server.
  - 38465
  - 38466
firewall_allowed_udp_ports:
  - 111

# Gluster configuration.
gluster_mount_dir: /mnt/gluster
gluster_brick_dir: /srv/gluster/brick
gluster_brick_name: gluster
```

<p>This variables file should be pretty self-explanatory; all the ports required for Gluster are opened in the firewall, and the three Gluster-related variables we use in the playbook are defined.</p>

<p>Now that we have everything set up, the folder structure should look like this:</p>


```
gluster/
  playbooks/
    provision.yml
    main.yml
  inventory
  Vagrantfile
```

<p>Change directory into the <code>gluster</code> directory, and run <code>vagrant up</code>. After a few minutes, provisioning should have completed successfully. To ensure Gluster is working properly, you can run the following two commands, which should give information about Gluster's peer connections and the configured <code>gluster</code> volume:</p>


```
$ ansible gluster -i inventory -a "gluster peer status" -s
192.168.29.2 | success | rc=0 >>
Number of Peers: 1

Hostname: 192.168.29.3
Port: 24007
Uuid: 1340bcf1-1ae6-4e55-9716-2642268792a4
State: Peer in Cluster (Connected)

192.168.29.3 | success | rc=0 >>
Number of Peers: 1

Hostname: 192.168.29.2
Port: 24007
Uuid: 63d4a5c8-6b27-4747-8cc1-16af466e4e10
State: Peer in Cluster (Connected)

$ ansible gluster -i inventory -a "gluster volume info" -s
192.168.29.3 | success | rc=0 >>

Volume Name: gluster
Type: Replicate
Volume ID: b75e9e45-d39b-478b-a642-ccd16b7d89d8
Status: Started
Number of Bricks: 1 x 2 = 2
Transport-type: tcp
Bricks:
Brick1: 192.168.29.2:/srv/gluster/brick
Brick2: 192.168.29.3:/srv/gluster/brick

192.168.29.2 | success | rc=0 >>

Volume Name: gluster
Type: Replicate
Volume ID: b75e9e45-d39b-478b-a642-ccd16b7d89d8
Status: Started
Number of Bricks: 1 x 2 = 2
Transport-type: tcp
Bricks:
Brick1: 192.168.29.2:/srv/gluster/brick
Brick2: 192.168.29.3:/srv/gluster/brick
```

<p>You can also do the following to confirm that files are being replicated/distributed correctly:</p>

<ol>
<li>Log into the first server: <code>vagrant ssh gluster1</code></li>
<li>Create a file in the mounted gluster volume: <code>sudo touch /mnt/gluster/test</code>
</li>
<li>Log out of the first server: <code>exit</code>
</li>
<li>Log into the second server: <code>vagrant ssh gluster2</code>
</li>
<li>List the contents of the gluster directory: <code>ls /mnt/gluster</code>
</li>
</ol>

<p>You should see the <code>test</code> file you created in step 2; this means Gluster is working correctly!</p>

<h2>
<a id="user-content-summary" class="anchor" href="#summary" aria-hidden="true"><span class="octicon octicon-link"></span></a>Summary</h2>

<p>Deploying distributed file systems like Gluster can seem challenging, but Ansible simplifies the process, and more importantly, does so idempotently; each time you run the playbook again, it will ensure everything stays configured as you've set it.</p>

<p>This example Gluster configuration can be found in its entirety on GitHub, in the <a href="https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/gluster">Gluster example</a> in the Ansible Vagrant Examples project.</p>

<p><em>Read Ansible for DevOps, available on LeanPub:</em></p>

<iframe width="160" height="400" src="https://leanpub.com/ansible-for-devops/embed" frameborder="0" allowtransparency="true"></iframe>
