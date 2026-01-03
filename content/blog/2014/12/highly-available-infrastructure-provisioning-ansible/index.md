---
nid: 2605
title: "Highly-Available Infrastructure Provisioning and Configuration with Ansible"
slug: "highly-available-infrastructure-provisioning-ansible"
date: 2014-12-15T15:50:59+00:00
drupal:
  nid: 2605
  path: /blog/highly-available-infrastructure-provisioning-ansible
  body_format: full_html
  redirects:
    - /blog/highly-available-infrastructure-provisioning-and
aliases:
  - /blog/highly-available-infrastructure-provisioning-and
   - /blog/highly-available-infrastructure-provisioning-ansible
tags:
  - ansible
  - ansible for devops
  - automation
  - high availability
  - infrastructure
---

<blockquote>
<p>The following is an excerpt from Chapter 8 of <a href="http://ansiblefordevops.com/">Ansible for DevOps</a>, a book on Ansible by Jeff Geerling. The example highlights Ansible's simplicity and flexibility by provisioning and configuring of a highly available web application infrastructure on a local Vagrant-managed cloud, DigitalOcean droplets, and Amazon Web Services EC2 instances, with one set of Ansible playbooks.</p>

<p><strong>tl;dr</strong> Check out the <a href="https://github.com/geerlingguy/ansible-for-devops/tree/master/lamp-infrastructure">code on GitHub</a>, and <a href="http://www.ansiblefordevops.com/">buy the book</a> to learn more about Ansible!</p>
</blockquote>

<h2>
<a id="user-content-highly-available-infrastructure-with-ansible" class="anchor" href="#highly-available-infrastructure-with-ansible" aria-hidden="true"><span class="octicon octicon-link"></span></a>Highly-Available Infrastructure with Ansible</h2>

<p>Real-world web applications require redundancy and horizontal scalability with multi-server infrastructure. In the following example, we'll use Ansible to configure a complex infrastructure (illustrated below) on servers provisioned either locally via Vagrant and VirtualBox, or on a set of automatically-provisioned instances running on either DigitalOcean or Amazon Web Services:</p>

<p style="text-align: center;">{{< figure src="./8-highly-available-infrastructure_2.png" alt="Highly-Available Infrastructure." >}}</a></p>

<p><strong>Varnish</strong> acts as a load balancer and reverse proxy, fronting web requests and routing them to the application servers. We could just as easily use something like <strong>Nginx</strong> or <strong>HAProxy</strong>, or even a proprietary cloud-based solution like an Amazon's <strong>Elastic Load Balancer</strong> or Linode's <strong>NodeBalancer</strong>, but for simplicity's sake, and for flexibility in deployment, we'll use Varnish.</p>

<p><strong>Apache</strong> and mod_php run a PHP-based application that displays the entire stack's current status and outputs the current server's IP address for load balancing verification.</p>

<p>A <strong>Memcached</strong> server provides a caching layer that can be used to store and retrieve frequently-accessed objects in lieu of slower database storage.</p>

<p>Two <strong>MySQL</strong> servers, configured as a master and slave, offer redundant and performant database access; all data will be replicated from the master to the slave, and the slave can also be used as a secondary server for read-only queries to take some load off the master.</p>

<h3>
<a id="user-content-directory-structure" class="anchor" href="#directory-structure" aria-hidden="true"><span class="octicon octicon-link"></span></a>Directory Structure</h3>

<p>In order to keep our configuration organized, we'll use the following structure for our playbooks and configuration:</p>


```
lamp-infrastructure/
  inventories/
  playbooks/
    db/
    memcached/
    varnish/
    www/
  provisioners/
  configure.yml
  provision.yml
  requirements.txt
  Vagrantfile
```

<p>Organizing things this way allows us to focus on each server configuration individually, then build playbooks for provisioning and configuring instances on different hosting providers later. This organization also keeps server playbooks completely independent, so we can modularize and reuse individual server configurations.</p>

<h3>
<a id="user-content-individual-server-playbooks" class="anchor" href="#individual-server-playbooks" aria-hidden="true"><span class="octicon octicon-link"></span></a>Individual Server Playbooks</h3>

<p>Let's start building our individual server playbooks (in the <code>playbooks</code> directory). To make our playbooks more efficient, we'll use some contributed Ansible roles on Ansible Galaxy rather than install and configure everything step-by-step. We're going to target CentOS 6.x servers in these playbooks, but only minimal changes would be required to use the playbooks with Ubuntu, Debian, or later versions of CentOS.</p>

<p><strong>Varnish</strong></p>

<p>Create a <code>main.yml</code> file within the the <code>playbooks/varnish</code> directory, with the following contents:</p>


```
---
- hosts: lamp-varnish
  sudo: yes

  vars_files:
    - vars.yml

  roles:
    - geerlingguy.firewall
    - geerlingguy.repo-epel
    - geerlingguy.varnish

  tasks:
    - name: Copy Varnish default.vcl.
      template:
        src: "templates/default.vcl.j2"
        dest: "/etc/varnish/default.vcl"
      notify: restart varnish
```

<p>We're going to run this playbook on all hosts in the <code>lamp-varnish</code> inventory group (we'll create this later), and we'll run a few simple roles to configure the server:</p>

<ul>
<li><code>geerlingguy.firewall</code> configures a simple iptables-based firewall using a couple variables defined in <code>vars.yml</code>.</li>
<li>
<code>geerlingguy.repo-epel</code> adds the EPEL repository (a prerequisite for varnish).</li>
<li>
<code>geerlingguy.varnish</code> installs and configures Varnish.</li>
</ul>

<p>Finally, a task copies over a custom <code>default.vcl</code> that configures Varnish, telling it where to find our web servers and how to load balance requests between the servers.</p>

<p>Let's create the two files referenced in the above playbook. First, <code>vars.yml</code>, in the same directory as <code>main.yml</code>:</p>


```
---
firewall_allowed_tcp_ports:
  - "22"
  - "80"

varnish_use_default_vcl: false
```

<p>The first variable tells the <code>geerlingguy.firewall</code> role to open TCP ports 22 and 80 for incoming traffic. The second variable tells the <code>geerlingguy.varnish</code> we will supply a custom <code>default.vcl</code> for Varnish configuration.</p>

<p>Create a <code>templates</code> directory inside the <code>playbooks/varnish</code> directory, and inside, create a <code>default.vcl.j2</code> file. This file will use Jinja2 syntax to build Varnish's custom <code>default.vcl</code> file:</p>


```
vcl 4.0;

import directors;

{% for host in groups['lamp-www'] %}
backend www{{ loop.index }} {
  .host = "{{ host }}";
  .port = "80";
}
{% endfor %}

sub vcl_init {
  new vdir = directors.random();
{% for host in groups['lamp-www'] %}
  vdir.add_backend(www{{ loop.index }}, 1);
{% endfor %}
}

sub vcl_recv {
  set req.backend_hint = vdir.backend();

  # For testing ONLY; makes sure load balancing is working correctly.
  return (pass);
}
```

<p>We won't study Varnish's VCL syntax in depth but we'll run through <code>default.vcl</code> and highlight what is being configured:</p>

<ol>
<li>(1-3) Indicate that we're using the 4.0 version of the VCL syntax and import the <code>directors</code> varnish module (which is used to configure load balancing).</li>
<li>(5-10) Define each web server as a new backend; give a host and a port through which varnish can contact each host.</li>
<li>(12-17) <code>vcl_init</code> is called when Varnish boots and initializes any required varnish modules. In this case, we're configuring a load balancer <code>vdir</code>, and adding each of the <code>www[#]</code> backends we defined earlier as backends to which the load balancer will distribute requests. We use a <code>random</code> director so we can easily demonstrate Varnish's ability to distribute requests to both app backends, but other load balancing strategies are also available.</li>
<li>(19-24) <code>vcl_recv</code> is called for each request, and routes the request through Varnish. In this case, we route the request to the <code>vdir</code> backend defined in <code>vcl_init</code>, and indicate that Varnish should <em>not</em> cache the result.</li>
</ol>

<p>According to #4, we're actually <em>bypassing Varnish's caching layer</em>, which is not helpful in a typical production environment. If you only need a load balancer without any reverse proxy or caching capabilities, there are better options. However, we need to verify our infrastructure is working as it should. If we used Varnish's caching, Varnish would only ever hit one of our two web servers during normal testing.</p>

<p>In terms of our caching/load balancing layer, this should suffice. For a true production environment, you should remove the final <code>return (pass)</code> and customize <code>default.vcl</code> according to your application's needs.</p>

<p><strong>Apache / PHP</strong></p>

<p>Create a <code>main.yml</code> file within the the <code>playbooks/www</code> directory, with the following contents:</p>


```
---
- hosts: lamp-www
  sudo: yes

  vars_files:
    - vars.yml

  roles:
    - geerlingguy.firewall
    - geerlingguy.repo-epel
    - geerlingguy.apache
    - geerlingguy.php
    - geerlingguy.php-mysql
    - geerlingguy.php-memcached

  tasks:
    - name: Remove the Apache test page.
      file:
        path: /var/www/html/index.html
        state: absent
    - name: Copy our fancy server-specific home page.
      template:
        src: templates/index.php.j2
        dest: /var/www/html/index.php
```

<p>As with Varnish's configuration, we'll configure a firewall and add the EPEL repository (required for PHP's memcached integration), and we'll also add the following roles:</p>

<ul>
<li>
<code>geerlingguy.apache</code> installs and configures the latest available version of the Apache web server.</li>
<li>
<code>geerlingguy.php</code> installs and configures PHP to run through Apache.</li>
<li>
<code>geerlingguy.php-mysql</code> adds MySQL support to PHP.</li>
<li>
<code>geerlingguy.php-memcached</code> adds Memcached support to PHP.</li>
</ul>

<p>Two final tasks remove the default <code>index.html</code> home page included with Apache, and replace it with our PHP app.</p>

<p>As in the Varnish example, create the two files referenced in the above playbook. First, <code>vars.yml</code>, alongside <code>main.yml</code>:</p>


```
---
firewall_allowed_tcp_ports:
  - "22"
  - "80"
```

<p>Create a <code>templates</code> directory inside the <code>playbooks/www</code> directory, and inside, create an <code>index.php.j2</code> file. This file will use Jinja2 syntax to build a (relatively) simple PHP script to display the health and status of all the servers in our infrastructure:</p>

```
<code>
<?php
/**
 * @file
 * Infrastructure test page.
 *
 * DO NOT use this in production. It is simply a PoC.
 */

$mysql_servers = array(
{% for host in groups['lamp-db'] %}
  '{{ host }}',
{% endfor %}
);
$mysql_results = array();
foreach ($mysql_servers as $host) {
  if ($result = mysql_test_connection($host)) {
    $mysql_results[$host] = '<span style="color: green;">PASS</span>';
    $mysql_results[$host] .= ' (' . $result['status'] . ')';
  }
  else {
    $mysql_results[$host] = '<span style="color: red;">FAIL</span>';
  }
}

// Connect to Memcached.
$memcached_result = '<span style="color: red;">FAIL</span>';
if (class_exists('Memcached')) {
  $memcached = new Memcached;
  $memcached->addServer('{{ groups['lamp-memcached'][0] }}', 11211);

  // Test adding a value to memcached.
  if ($memcached->add('test', 'success', 1)) {
    $result = $memcached->get('test');
    if ($result == 'success') {
      $memcached_result = '<span style="color: green;">PASS</span>';
      $memcached->delete('test');
    }
  }
}

/**
 * Connect to a MySQL server and test the connection.
 *
 * @param string $host
 *   IP Address or hostname of the server.
 *
 * @return array
 *   Array with keys 'success' (bool) and 'status' ('slave' or 'master').
 *   Empty if connection failure.
 */
function mysql_test_connection($host) {
  $username = 'mycompany_user';
  $password = 'secret';
  try {
    $db = new PDO(
      'mysql:host=' . $host . ';dbname=mycompany_database',
      $username,
      $password,
      array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));

    // Query to see if the server is configured as a master or slave.
    $statement = $db->prepare("SELECT variable_value
      FROM information_schema.global_variables
      WHERE variable_name = 'LOG_BIN';");
    $statement->execute();
    $result = $statement->fetch();

    return array(
      'success' => TRUE,
      'status' => ($result[0] == 'ON') ? 'master' : 'slave',
    );
  }
  catch (PDOException $e) {
    return array();
  }
}
?>
```

```
<!DOCTYPE html>
<html>
<head>
  <title>Host {{ inventory_hostname }}</title>
  <style>* { font-family: Helvetica, Arial, sans-serif }</style>
</head>
<body>
  <h1>Host {{ inventory_hostname }}</h1>
<?php foreach ($mysql_results as $host => $result): ?>
    <p>MySQL Connection (<code>
<?php print $host; ?>
</code>): <code>
<?php print $result; ?>
</code></p>
<?php endforeach; ?>
  <p>Memcached Connection: <code>
<?php print $memcached_result; ?>
</code></p>
</body>
</html>
```

<blockquote>
<p>Don't try transcribing this example manually; you can get the code from this book's repository on GitHub. Visit the <a href="https://github.com/geerlingguy/ansible-for-devops">ansible-for-devops</a> repository and download the source for <a href="https://github.com/geerlingguy/ansible-for-devops/blob/master/lamp-infrastructure/playbooks/www/templates/index.php.j2">index.php.j2</a></p>
</blockquote>

<p>As this is the heart of the example application we're deploying to the infrastructure, it's necessarily a bit more complex than most examples in the book, but a quick run through follows:</p>

<ul>
<li>(9-23) Iterate through all the <code>lamp-db</code> MySQL hosts defined in the playbook inventory, and test the ability to connect to them, and whether they are configured as master or slave, using the <code>mysql_test_connection()</code> function defined later (40-73).</li>
<li>(25-39) Check the first defined <code>lamp-memcached</code> Memcached host defined in the playbook inventory, confirming the ability to connect and create, retrieve, and delete a value from the cache.</li>
<li>(41-76) Define the <code>mysql_test_connection()</code> function which tests the the ability to connect to a MySQL server and also returns its replication status.</li>
<li>(78-91) Print the results of all the MySQL and Memcached tests, along with <code>{{ inventory_hostname }}</code> as the page title, so we can easily see which web server is serving the viewed page.</li>
</ul>

<p>At this point, the heart of our infrastructure — the application that will test and display the status of all our servers — is ready to go.</p>

<p><strong>Memcached</strong></p>

<p>Compared to the earlier playbooks, the Memcached playbook is quite simple. Create <code>playbooks/memcached/main.yml</code> with the following contents:</p>


```
---
- hosts: lamp-memcached
  sudo: yes

  vars_files:
    - vars.yml

  roles:
    - geerlingguy.firewall
    - geerlingguy.memcached
```

<p>As with the other servers, we need to ensure only the required TCP ports are open using the simple <code>geerlingguy.firewall</code> role. Next we install Memcached using the <code>geerlingguy.memcached</code> role.</p>

<p>In our <code>vars.yml</code> file (again, alongside <code>main.yml</code>), add the following:</p>


```
---
firewall_allowed_tcp_ports:
  - "22"
firewall_additional_rules:
  - "iptables -A INPUT -p tcp --dport 11211 -s {{ groups['lamp-www'][0] }} -j ACCEPT"
  - "iptables -A INPUT -p tcp --dport 11211 -s {{ groups['lamp-www'][1] }} -j ACCEPT"
```

<p>We need port 22 open for remote access, and for Memcached, we're adding manual iptables rules to allow access on port 11211 for the web servers <em>only</em>. We add one rule per <code>lamp-www</code> server by drilling down into each item in the the generated <code>groups</code> variable that Ansible uses to track all inventory groups currently available.</p>

<blockquote>
<p>The <strong>principle of least privilege</strong> "requires that in a particular abstraction layer of a computing environment, every module ... must be able to access only the information and resources that are necessary for its legitimate purpose" (Source: <a href="http://en.wikipedia.org/wiki/Principle_of_least_privilege">Wikipedia</a>). Always restrict services and ports to only those servers or users that need access!</p>
</blockquote>

<p><strong>MySQL</strong></p>

<p>The MySQL configuration is more complex than the other servers because we need to configure MySQL users per-host and configure replication. Because we want to maintain an independent and flexible playbook, we also need to dynamically create some variables so MySQL will get the right server addresses in any potential environment.</p>

<p>Let's first create the main playbook, <code>playbooks/db/main.yml</code>:</p>


```
---
- hosts: lamp-db
  sudo: yes

  vars_files:
    - vars.yml

  pre_tasks:
    - name: Create dynamic MySQL variables.
      set_fact:
        mysql_users:
          - {
            name: mycompany_user,
            host: "{{ groups['lamp-www'][0] }}",
            password: secret,
            priv: "*.*:SELECT"
          }
          - {
            name: mycompany_user,
            host: "{{ groups['lamp-www'][1] }}",
            password: secret,
            priv: "*.*:SELECT"
          }
        mysql_replication_master: "{{ groups['a4d.lamp.db.1'][0] }}"

  roles:
    - geerlingguy.firewall
    - geerlingguy.mysql
```

<p>Most of the playbook is straightforward, but in this instance, we're using <code>set_fact</code> as a <code>pre_task</code> (to be run before the <code>geerlingguy.firewall</code> and <code>geerlingguy.mysql</code> roles) to dynamically create variables for MySQL configuration.</p>

<p><code>set_fact</code> allows us to define variables at runtime, so we can are guaranteed to have all server IP addresses available, even if the servers were freshly provisioned at the beginning of the playbook's run. We'll create two variables:</p>

<ul>
<li>
<code>mysql_users</code> is a list of users the <code>geerlingguy.mysql</code> role will create when it runs. This variable will be used on all database servers so both of the two <code>lamp-www</code> servers get <code>SELECT</code> privileges on all databases.</li>
<li>
<code>mysql_replication_master</code> is used to indicate to the <code>geerlingguy.mysql</code> role which database server is the master; it will perform certain steps differently depending on whether the server being configured is a master or slave, and ensure that all the slaves are configured to replicate data from the master.</li>
</ul>

<p>We'll need a few other normal variables to configure MySQL, so we'll add them alongside the firewall variable in <code>playbooks/db/vars.yml</code>:</p>


```
---
firewall_allowed_tcp_ports:
  - "22"
  - "3306"

mysql_replication_user: {name: 'replication', password: 'secret'}
mysql_databases:
  - { name: mycompany_database, collation: utf8_general_ci, encoding: utf8 }
```

<p>We're opening port 3306 to anyone, but according to the <strong>principle of least privilege</strong> discussed earlier, you would be justified in restricting this port to only the servers and users that need access to MySQL (similar to the memcached server configuration). In this case, the attack vector is mitigated because MySQL's own authentication layer is used through the <code>mysql_user</code> variable generated in <code>main.yml</code>.</p>

<p>We are defining two MySQL variables, <code>mysql_replication_user</code> to be used as for master and slave replication, and <code>mysql_databases</code> to define a list of databases that will be created (if they don't already exist) on the database servers.</p>

<p>With the configuration of the database servers complete, the server-specific playbooks are ready to go.</p>

<h3>
<a id="user-content-main-playbook-for-configuring-all-servers" class="anchor" href="#main-playbook-for-configuring-all-servers" aria-hidden="true"><span class="octicon octicon-link"></span></a>Main Playbook for Configuring All Servers</h3>

<p>A simple playbook including each of the group-specific playbooks is all we need for the overall configuration to take place. Create <code>configure.yml</code> in the project's root directory, with the following contents:</p>


```
---
- include: playbooks/varnish/main.yml
- include: playbooks/www/main.yml
- include: playbooks/db/main.yml
- include: playbooks/memcached/main.yml
```

<p>At this point, if you had some already-booted servers and statically defined inventory groups like <code>lamp-www</code>, <code>lamp-db</code>, etc., you could run <code>ansible-playbook configure.yml</code> and you'd have a full HA infrastructure at the ready!</p>

<p>But we're going to continue to make our playbooks more flexible and useful.</p>

<h3>
<a id="user-content-getting-the-required-roles" class="anchor" href="#getting-the-required-roles" aria-hidden="true"><span class="octicon octicon-link"></span></a>Getting the required roles</h3>

<p>Ansible allows you to define all the required Ansible Galaxy roles for a given project in a <code>requirements.txt</code> file. Instead of having to remember to run <code>ansible-galaxy install -y [role1] [role2] [role3]</code> for each of the roles we're using, we can create <code>requirements.txt</code> in the root of our project, with the following contents:</p>


```
geerlingguy.firewall
geerlingguy.repo-epel
geerlingguy.varnish
geerlingguy.apache
geerlingguy.php
geerlingguy.php-mysql
geerlingguy.php-memcached
geerlingguy.mysql
geerlingguy.memcached
```

<p>To make sure all the required dependencies are available, just run <code>ansible-galaxy install -r requirements.txt</code> from within the project's root.</p>

<blockquote>
<p>Ansible 1.8 and greater provide more flexibility in requirements files. If you use a YAML file (e.g. <code>requirements.yml</code>) to define a structured list of all the roles you need, you can source them from Ansible Galaxy, a git repository, a web-accessible URL (as a <code>.tar.gz</code>), or even a mercurial repository! See the documentation for <a href="http://docs.ansible.com/galaxy.html#advanced-control-over-role-requirements-files">Advanced Control over Role Requirements Files</a>.</p>
</blockquote>

<h3>
<a id="user-content-vagrantfile-for-local-infrastructure-via-virtualbox" class="anchor" href="#vagrantfile-for-local-infrastructure-via-virtualbox" aria-hidden="true"><span class="octicon octicon-link"></span></a>Vagrantfile for Local Infrastructure via VirtualBox</h3>

<p>As with many other examples in this book, we can use Vagrant and VirtualBox to build and configure the infrastructure locally. This lets us test things as much as we want with zero cost, and usually results in faster testing cycles, since everything is orchestrated over a local private network on a (hopefully) beefy workstation.</p>

<p>Our basic Vagrantfile layout will be something like the following:</p>

<ol>
<li>Define a base box (in this case, CentOS 6.x) and VM hardware defaults.</li>
<li>Define all the VMs to be built, with VM-specific IP addresses and hostname configurations.</li>
<li>Define the Ansible provisioner along with the last VM, so Ansible can run once at the end of Vagrant's build cycle.</li>
</ol>

<p>Here's the Vagrantfile in all its glory:</p>


```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Base VM OS configuration.
  config.vm.box = "geerlingguy/centos6"

  # General VirtualBox VM configuration.
  config.vm.provider :virtualbox do |v|
    v.customize ["modifyvm", :id, "--memory", 512]
    v.customize ["modifyvm", :id, "--cpus", 1]
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--ioapic", "on"]
  end

  # Varnish.
  config.vm.define "varnish" do |varnish|
    varnish.vm.hostname = "varnish.dev"
    varnish.vm.network :private_network, ip: "192.168.2.2"
  end

  # Apache.
  config.vm.define "www1" do |www1|
    www1.vm.hostname = "www1.dev"
    www1.vm.network :private_network, ip: "192.168.2.3"

    www1.vm.provision "shell",
      inline: "sudo yum update -y"

    www1.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--memory", 256]
    end
  end

  # Apache.
  config.vm.define "www2" do |www2|
    www2.vm.hostname = "www2.dev"
    www2.vm.network :private_network, ip: "192.168.2.4"

    www2.vm.provision "shell",
      inline: "sudo yum update -y"

    www2.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--memory", 256]
    end
  end

  # MySQL.
  config.vm.define "db1" do |db1|
    db1.vm.hostname = "db1.dev"
    db1.vm.network :private_network, ip: "192.168.2.5"
  end

  # MySQL.
  config.vm.define "db2" do |db2|
    db2.vm.hostname = "db2.dev"
    db2.vm.network :private_network, ip: "192.168.2.6"
  end

  # Memcached.
  config.vm.define "memcached" do |memcached|
    memcached.vm.hostname = "memcached.dev"
    memcached.vm.network :private_network, ip: "192.168.2.7"

    # Run Ansible provisioner once for all VMs at the end.
    memcached.vm.provision "ansible" do |ansible|
      ansible.playbook = "configure.yml"
      ansible.inventory_path = "inventories/vagrant/inventory"
      ansible.limit = "all"
      ansible.extra_vars = {
        ansible_ssh_user: 'vagrant',
        ansible_ssh_private_key_file: "~/.vagrant.d/insecure_private_key"
      }
    end
  end
end
```

<p>Most of the Vagrantfile is straightforward, and similar to other examples used in this book. The last block of code, which defines the <code>ansible</code> provisioner configuration, contains three extra values that are important for our purposes:</p>


```
      ansible.inventory_path = "inventories/vagrant/inventory"
      ansible.limit = "all"
      ansible.extra_vars = {
        ansible_ssh_user: 'vagrant',
        ansible_ssh_private_key_file: "~/.vagrant.d/insecure_private_key"
      }
```

<ol>
<li>
<code>ansible.inventory_path</code> defines an inventory file to be used with the <code>ansible.playbook</code>. You could certainly create a dynamic inventory script for use with Vagrant, but because we know the IP addresses ahead of time, and are expecting a few specially-crafted inventory group names, it's simpler to build the inventory file for Vagrant provisioning by hand (we'll do this next).</li>
<li>
<code>ansible.limit</code> is set to <code>all</code> so Vagrant knows it should run the Ansible playbook connected to all VMs, and not just the current VM. You could technically use <code>ansible.limit</code> with a provisioner configuration for each of the individual VMs, and just run the VM-specific playbook through Vagrant, but our live production infrastructure will be using one playbook to configure all the servers, so we'll do the same locally.</li>
<li>
<code>ansible.extra_vars</code> contains the vagrant SSH user configuration for Ansible. It's more standard to include these settings in a static inventory file or use Vagrant's automatically-generated inventory file, but it's easiest to set them once for all servers here.</li>
</ol>

<p>Before running <code>vagrant up</code> to see the fruits of our labor, we need to create an inventory file for Vagrant at <code>inventories/vagrant/inventory</code>:</p>


```
[lamp-varnish]
192.168.2.2

[lamp-www]
192.168.2.3
192.168.2.4

[a4d.lamp.db.1]
192.168.2.5

[lamp-db]
192.168.2.5
192.168.2.6

[lamp-memcached]
192.168.2.7
```

<p>Now <code>cd</code> into the project's root directory, run <code>vagrant up</code>, and after ten or fifteen minutes, load <code>http://192.168.2.2/</code> in your browser. Voila!</p>

<p style="text-align: center;">{{< figure src="./8-ha-infrastructure-success_0.png" alt="Highly Available Infrastructure - Success!" >}}</a></p>

<p>You should see something like the above screenshot; the PHP app simply displays the current app server's IP address, the individual MySQL servers' status, and the Memcached server status. Refresh the page a few times to verify Varnish is distributing requests randomly between the two app servers.</p>

<p>We have local infrastructure development covered, and Ansible makes it easy to use the exact same configuration to build our infrastructure in the cloud.</p>

<h3>
<a id="user-content-provisioner-configuration-digitalocean" class="anchor" href="#provisioner-configuration-digitalocean" aria-hidden="true"><span class="octicon octicon-link"></span></a>Provisioner Configuration: DigitalOcean</h3>

<p>In Chapter 7, we learned provisioning and configuring DigitalOcean droplets in an Ansible playbook is fairly simple. But we need to take provisioning a step further by provisioning multiple droplets (one for each server in our infrastructure) and dynamically grouping them so we can configure them after they are booted and online.</p>

<p>For the sake of flexibility, let's create a playbook for our DigitalOcean droplets in <code>provisioners/digitalocean.yml</code>. This will allow us to add other provisioner configurations later, alongside the <code>digitalocean.yml</code> playbook. As with our example in Chapter 7, we will use a local connection to provision cloud instances. Begin the playbook with:</p>


```
---
- hosts: localhost
  connection: local
  gather_facts: false
```

<p>Next we need to define some metadata to describe each of our droplets. For simplicity's sake, we'll inline the <code>droplets</code> variable in this playbook:</p>


```
  vars:
    droplets:
      - { name: a4d.lamp.varnish, group: "lamp-varnish" }
      - { name: a4d.lamp.www.1, group: "lamp-www" }
      - { name: a4d.lamp.www.2, group: "lamp-www" }
      - { name: a4d.lamp.db.1, group: "lamp-db" }
      - { name: a4d.lamp.db.2, group: "lamp-db" }
      - { name: a4d.lamp.memcached, group: "lamp-memcached" }
```

<p>Each droplet is an object with two keys:</p>

<ul>
<li>
<code>name</code>: The name of the Droplet for DigitalOcean's listings and Ansible's host inventory.</li>
<li>
<code>group</code>: The Ansible inventory group for the droplet.</li>
</ul>

<p>Next we need to add a task to create the droplets, using the <code>droplets</code> list as a guide, and as part of the same task, register each droplet's information in a separate dictionary, <code>created_droplets</code>:</p>


```
  tasks:
    - name: Provision DigitalOcean droplets.
      digital_ocean:
        state: "{{ item.state | default('present') }}"
        command: droplet
        name: "{{ item.name }}"
        private_networking: yes
        size_id: "{{ item.size | default(66) }}" # 512mb
        image_id: "{{ item.image | default(6372108) }}" # CentOS 6 x64.
        region_id: "{{ item.region | default(4) }}" # NYC2
        ssh_key_ids: "{{ item.ssh_key | default('138954') }}" # geerlingguy
        unique_name: yes
      register: created_droplets
      with_items: droplets
```

<p>Many of the options (e.g. <code>size_id</code>) are defined as <code>{{ item.property | default('default_value') }}</code>, which allows us to use optional variables per droplet. For any of the defined droplets, we could add <code>size_id: 72</code> (or whatever valid value you'd like), and it would override the default value set in the task.</p>

<blockquote>
<p>You could specify an SSH public key per droplet, or (as in this instance) use the same key for all hosts by providing a default. In this case, I added an SSH key to my DigitalOcean account, then used the DigitalOcean API to retrieve the key's numeric ID (as described in the previous chapter).</p>

<p>It's best to use key-based authentication and add at least one SSH key to your DigitalOcean account so Ansible can connect using keys instead of insecure passwords, especially since these instances will be created with only a root account.</p>
</blockquote>

<p>We loop through all the defined <code>droplets</code> using <code>with_items: droplets</code>, and after each droplet is created add the droplet's metadata (name, IP address, etc.) to the <code>created_droplets</code> variable. Next, we'll loop through that variable to build our inventory on-the-fly so our configuration applies to the correct servers:</p>


```
    - name: Add DigitalOcean hosts to their respective inventory groups.
      add_host:
        name: "{{ item.1.droplet.ip_address }}"
        groups: "do,{{ droplets[item.0].group }},{{ item.1.droplet.name }}"
        # You can dynamically add inventory variables per-host.
        ansible_ssh_user: root
        mysql_replication_role: >
          "{{ 'master' if (item.1.droplet.name == 'a4d.lamp.db.1')
          else 'slave' }}"
        mysql_server_id: "{{ item.0 }}"
      when: item.1.droplet is defined
      with_indexed_items: created_droplets.results
```

<p>You'll notice a few interesting things happening in this task:</p>

<ul>
<li>This is the first time we've used <code>with_indexed_items</code>. The reason for using this less-common loop feature is to add a sequential and unique <code>mysql_server_id</code>. Though only the MySQL servers need a server ID set, it's simplest to dynamically create the variable for every server, so it's available when needed. <code>with_indexed_items</code> simply sets <code>item.0</code> to the key of the item, and <code>item.1</code> to the value of the item.</li>
<li>
<code>with_indexed_items</code> also helps us reliably set each droplet's group. Because the v1 DigitalOcean API doesn't support features like tags for Droplets, we need to set up the groups on our own. Using the <code>droplets</code> variable we manually created earlier allows us to set the proper group for a particular droplet.</li>
<li>Finally we add inventory variables per-host in <code>add_host</code> by adding the variable name as a key, and the variable value as the key's value. Simple, but powerful!</li>
</ul>

<blockquote>
<p>There are a few different ways you can approach dynamic provisioning and inventory management for your infrastructure, and, especially if you are only targeting one cloud hosting provider, there are ways to avoid using more exotic features of Ansible (e.g. <code>with_indexed_items</code>) and complex if/else conditions. This example is slightly more complex due to the fact that the playbook is being created to be interchangeable with other similar provisioning playbooks.</p>
</blockquote>

<p>The final step in our provisioning is to make sure all the droplets are booted and can be reached via SSH, so at the end of the <code>digitalocean.yml</code> playbook, add another play to be run on hosts in the <code>do</code> group we just defined:</p>


```
- hosts: do
  remote_user: root

  tasks:
    - name: Wait for port 22 to become available.
      local_action: "wait_for port=22 host={{ inventory_hostname }}"
```

<p>Once we know port 22 is reachable, we know the droplet is up and ready for configuration.</p>

<p>We're <em>almost</em> ready to provision and configure our entire infrastructure on DigitalOcean, but we need to create one last playbook to tie everything together. Create <code>provision.yml</code> in the project root with the following contents:</p>


```
---
- include: provisioners/digitalocean.yml
- include: configure.yml
```

<p>That's it! Now, assuming you set the environment variables <code>DO_CLIENT_ID</code> and <code>DO_API_KEY</code>, you can run <code>$ ansible-playbook provision.yml</code> to provision and configure the infrastructure on DigitalOcean.</p>

<p>The entire process should take about 15 minutes, and once it's complete, you should see something like:</p>


```
PLAY RECAP *****************************************************************
107.170.27.137             : ok=19   changed=13   unreachable=0    failed=0
107.170.3.23               : ok=13   changed=8    unreachable=0    failed=0
107.170.51.216             : ok=40   changed=18   unreachable=0    failed=0
107.170.54.218             : ok=27   changed=16   unreachable=0    failed=0
162.243.20.29              : ok=24   changed=15   unreachable=0    failed=0
192.241.181.197            : ok=40   changed=18   unreachable=0    failed=0
localhost                  : ok=2    changed=1    unreachable=0    failed=0
```

<p>Visit the IP address of the varnish server and you should be greeted with a status page similar to the one generated by the Vagrant-based infrastructure:</p>

<p style="text-align: center;">{{< figure src="./8-ha-infrastructure-digitalocean_0.png" alt="Highly Available Infrastructure on DigitalOcean." >}}</a></p>

<p>Because everything in this playbook is idempotent, running <code>$ ansible-playbook provision.yml</code> again should report no changes, and helps you verify that everything is running correctly.</p>

<p>Ansible will also rebuild and reconfigure any droplets that may be missing from your infrastructure. If you're daring, and want to test this feature, just log into your DigitalOcean account, delete one of the droplets just created by this playbook (maybe one of the two app servers), then run the playbook again.</p>

<p>Now that we've tested our infrastructure on DigitalOcean, we can destroy the droplets just as easily (change the <code>state</code> parameter in <code>provisioners/digitalocean.yml</code> to default to <code>'absent'</code> and run <code>$ ansible-playbook provision.yml</code> again).</p>

<p>Next up, we'll build the infrastructure a third time—on Amazon's infrastructure.</p>

<h3>
<a id="user-content-provisioner-configuration-amazon-web-services-ec2" class="anchor" href="#provisioner-configuration-amazon-web-services-ec2" aria-hidden="true"><span class="octicon octicon-link"></span></a>Provisioner Configuration: Amazon Web Services (EC2)</h3>

<p>For Amazon Web Services, provisioning works slightly different. Amazon has a broader ecosystem of services surrounding EC2 instances, and for our particular example, we will need to configure security groups prior to provisioning instances.</p>

<p>To begin, create <code>aws.yml</code> inside the <code>provisioners</code> directory and begin the playbook the same ways as with DigitalOcean:</p>


```
---
- hosts: localhost
  connection: local
  gather_facts: false
```

<p>EC2 instances use security groups as an AWS-level firewall (which operates outside the individual instance's OS).
We will need to define a list of <code>security_groups</code> alongside our EC2 <code>instances</code>. First, the <code>instances</code>:</p>


```
  vars:
    instances:
      - {
        name: a4d.lamp.varnish,
        group: "lamp-varnish",
        security_group: ["default", "a4d_lamp_http"]
      }
      - {
        name: a4d.lamp.www.1,
        group: "lamp-www",
        security_group: ["default", "a4d_lamp_http"]
      }
      - {
        name: a4d.lamp.www.2,
        group: "lamp-www",
        security_group: ["default", "a4d_lamp_http"]
      }
      - {
        name: a4d.lamp.db.1,
        group: "lamp-db",
        security_group: ["default", "a4d_lamp_db"]
      }
      - {
        name: a4d.lamp.db.2,
        group: "lamp-db",
        security_group: ["default", "a4d_lamp_db"]
      }
      - {
        name: a4d.lamp.memcached,
        group: "lamp-memcached",
        security_group: ["default", "a4d_lamp_memcached"]
      }
```

<p>Inside the <code>instances</code> variable, each instance is an object with three keys:</p>

<ul>
<li>
<code>name</code>: The name of the instance, which we'll use to tag the instance and ensure only one instance is created per name.</li>
<li>
<code>group</code>: The Ansible inventory group in which the instance should belong.</li>
<li>
<code>security_group</code>: A list of security groups into which the instance will be placed. The <code>default</code> security group comes is added to your AWS account upon creation, and has one rule to allow outgoing traffic on any port to any IP address.</li>
</ul>

<blockquote>
<p>If you use AWS exclusively, it would be best to autoscaling groups and change the design of this infrastructure a bit. For this example, we just need to ensure that the six instances we explicitly define are created, so we're using particular <code>name</code>s and an <code>exact_count</code> to enforce the 1:1 relationship.</p>
</blockquote>

<p>With our instances defined, we'll next define a <code>security_groups</code> variable containing all the required security group configuration for each server:</p>


```
    security_groups:
      - name: a4d_lamp_http
        rules:
          - { proto: tcp, from_port: 80, to_port: 80, cidr_ip: 0.0.0.0/0 }
          - { proto: tcp, from_port: 22, to_port: 22, cidr_ip: 0.0.0.0/0 }
        rules_egress: []
      - name: a4d_lamp_db
        rules:
          - { proto: tcp, from_port: 3306, to_port: 3306, cidr_ip: 0.0.0.0/0 }
          - { proto: tcp, from_port: 22, to_port: 22, cidr_ip: 0.0.0.0/0 }
        rules_egress: []
      - name: a4d_lamp_memcached
        rules:
          - { proto: tcp, from_port: 11211, to_port: 11211, cidr_ip: 0.0.0.0/0 }
          - { proto: tcp, from_port: 22, to_port: 22, cidr_ip: 0.0.0.0/0 }
        rules_egress: []
```

<p>Each security group has a <code>name</code> (which was used to identify the security group in the <code>instances</code> list), <code>rules</code> (a list of firewall rules like protocol, ports, and IP ranges to limit <em>incoming</em> traffic), and <code>rules_egress</code> (a list of firewall rules to limit <em>outgoing</em> traffic).</p>

<p>We need three security groups: <code>a4d_lamp_http</code> to open port 80, <code>a4d_lamp_db</code> to open port 3306, and <code>a4d_lamp_memcached</code> to open port 11211.</p>

<p>Now that we have all the data we need to set up security groups and instances, the first task needs to to create or verify the existence of the security groups:</p>


```
  tasks:
    - name: Configure EC2 Security Groups.
      ec2_group:
        name: "{{ item.name }}"
        description: Example EC2 security group for A4D.
        region: "{{ item.region | default('us-west-2') }}" # Oregon
        state: present
        rules: "{{ item.rules }}"
        rules_egress: "{{ item.rules_egress }}"
      with_items: security_groups
```

<p>The <code>ec2_group</code> requires a name, region, and rules for each security group. Security groups will be created if they don't exist, modified to match the supplied values if they do exist, or simply verified if they exist and match the given values.</p>

<p>With the security groups configured, we can provision the defined EC2 instances by looping through <code>instances</code> with the <code>ec2</code> module:</p>


```
    - name: Provision EC2 instances.
      ec2:
        key_name: "{{ item.ssh_key | default('jeff_mba_home') }}"
        instance_tags:
          inventory_group: "{{ item.group | default('') }}"
          inventory_host: "{{ item.name | default('') }}"
        group: "{{ item.security_group | default('') }}"
        instance_type: "{{ item.type | default('t2.micro')}}" # Free Tier
        image: "{{ item.image | default('ami-11125e21') }}" # RHEL6 x64 hvm
        region: "{{ item.region | default('us-west-2') }}" # Oregon
        wait: yes
        wait_timeout: 500
        exact_count: 1
        count_tag:
          inventory_group: "{{ item.group | default('') }}"
          inventory_host: "{{ item.name | default('') }}"
      register: created_instances
      with_items: instances
```

<p>This example is slightly more complex than the DigitalOcean example, and a few parts warrant a deeper look:</p>

<ul>
<li>EC2 allows SSH keys to be defined by name—in my case, I have a key <code>jeff_mba_home</code> in my AWS account. You should set the <code>key_name</code> default to a key that you have in your account.</li>
<li>Instance tags are tags that AWS will attach to your instance, for categorization purposes. By giving a list of keys and values, I can then use that list later in the <code>count_tag</code> parameter.</li>
<li>
<code>t2.micro</code> was used as the default instance type, since it falls within EC2's free tier usage. If you just set up an account and keep all AWS resource usage within free tier limits, you won't be billed anything.</li>
<li>
<code>exact_count</code> and <code>count_tag</code> work together to ensure AWS provisions only one of each of the instances we defined. The <code>count_tag</code> tells the <code>ec2</code> module to match the given group + host and then <code>exact_count</code> tells the module to only provision <code>1</code> instance. If you wanted to <em>remove</em> all your instances, you could set <code>exact_count</code> to 0 and run the playbook again.</li>
</ul>

<p>Each provisioned instance will have its metadata added to the registered <code>created_instances</code> variable, which we'll use to build Ansible inventory groups for the server configuration playbooks.</p>


```
    - name: Add EC2 instances to their respective inventory groups.
      add_host:
        name: "{{ item.1.tagged_instances.0.public_ip }}"
        groups: "aws,{{ item.1.item.group }},{{ item.1.item.name }}"
        # You can dynamically add inventory variables per-host.
        ansible_ssh_user: ec2-user
        mysql_replication_role: >
          {{ 'master' if (item.1.item.name == 'a4d.lamp.db.1')
          else 'slave' }}
        mysql_server_id: "{{ item.0 }}"
      when: item.1.instances is defined
      with_indexed_items: created_instances.results
```

<p>This <code>add_host</code> example is slightly simpler than the one for DigitalOcean, because AWS attaches metadata to EC2 instances which we can re-use when building groups or hostnames (e.g. <code>item.1.item.group</code>). We don't have to use list indexes to fetch group names from the original <code>instances</code> variable.</p>

<p>We still use <code>with_indexed_items</code> so we can use the index to generate a unique ID per server for use in building the MySQL master-slave replication.</p>

<p>The final step in provisioning the EC2 instances is to ensure we can connect to them before continuing, and to set <code>selinux</code> into permissive mode so the configuration we supply will work correctly.</p>


```
# Run some general configuration on all AWS hosts.
- hosts: aws
  gather_facts: false

  tasks:
    - name: Wait for port 22 to become available.
      local_action: "wait_for port=22 host={{ inventory_hostname }}"

    - name: Set selinux into 'permissive' mode.
      selinux: policy=targeted state=permissive
      sudo: yes
```

<p>Since we defined <code>ansible_ssh_user</code> as <code>ec2-user</code> in the dynamically-generated inventory above, we need to ensure the <code>selinux</code> task runs with <code>sudo</code> explicitly.</p>

<p>Now, modify the <code>provision.yml</code> file in the root of the project folder, and change the provisioners include to look like the following:</p>


```
---
- include: provisioners/aws.yml
- include: configure.yml
```

<p>Assuming the environment variables <code>AWS_ACCESS_KEY_ID</code> and <code>AWS_SECRET_ACCESS_KEY</code> are set in your current terminal session, you can run <code>$ ansible-playbook provision.yml</code> to provision and configure the infrastructure on AWS.</p>

<p>The entire process should take about 15 minutes, and once it's complete, you should see something like:</p>


```
PLAY RECAP *****************************************************************
54.148.100.44              : ok=24   changed=16   unreachable=0    failed=0
54.148.120.23              : ok=40   changed=19   unreachable=0    failed=0
54.148.41.134              : ok=40   changed=19   unreachable=0    failed=0
54.148.56.137              : ok=13   changed=9    unreachable=0    failed=0
54.69.160.32               : ok=27   changed=17   unreachable=0    failed=0
54.69.86.187               : ok=19   changed=14   unreachable=0    failed=0
localhost                  : ok=3    changed=1    unreachable=0    failed=0
```

<p>Visit the IP address of the varnish server (the first server configured) and you should be greeted with a status page similar to the one generated by the Vagrant and DigitalOcean-based infrastructure:</p>

<p style="text-align: center;">{{< figure src="./8-ha-infrastructure-aws_0.png" alt="Highly Available Infrastructure on AWS EC2." >}}</a></p>

<p>As with the earlier examples, running <code>ansible-playbook provision.yml</code> again should produce no changes, because everything in this playbook is idempotent. And if one of your instances were terminated, running the playbook again would recreate and reconfigure the instance in a few minutes.</p>

<p>To terminate all the provisioned instances, you can change the <code>exact_count</code> in the <code>ec2</code> task to <code>0</code>, and run <code>$ ansible-playbook provision.yml</code> again.</p>

<h3>
<a id="user-content-summary" class="anchor" href="#summary" aria-hidden="true"><span class="octicon octicon-link"></span></a>Summary</h3>

<p>In the above example, an entire highly-available PHP application infrastructure was defined in a series of short Ansible playbooks, and then provisioning configuration was created to build the infrastructure on either local VMs, DigitalOcean droplets, or AWS EC2 instances.</p>

<p>Once you start working on building infrastructure this way — abstracting individual servers, then abstracting cloud provisioning — you'll start to see some of Ansible's true power in being more than just a configuration management tool. Imagine being able to create your own multi-datacenter, multi-provider infrastructure with Ansible and some basic configuration.</p>

<p>While Amazon, DigitalOcean, Rackspace and other hosting providers have their own tooling and unique infrastructure merits, the agility and flexibility afforded by building infrastructure in a provider-agnostic fashion lets you treat hosting providers as commodities, and gives you freedom to build more reliable, performant, and simple application infrastructure.</p>

<p>Even if you plan on running everything within one hosting provider's network (or in a private cloud, or even on a few bare metal servers), Ansible provides deep stack-specific integration so you can do whatever you need to do and manage the provider's services within your playbooks.</p>

<blockquote>
<p>You can find the entire contents of this example in the <a href="https://github.com/geerlingguy/ansible-for-devops">Ansible for DevOps GitHub repository</a>, in the <code>lamp-infrastructure</code> directory.</p>
</blockquote>

<p><em>Purchase Ansible for DevOps on <a href="https://leanpub.com/ansible-for-devops">LeanPub</a>, <a href="http://www.amazon.com/Ansible-DevOps-Server-configuration-management-ebook/dp/B016G55NOU/">Amazon</a>, or <a href="https://itunes.apple.com/us/book/ansible-for-devops/id1050383787?ls=1&mt=11">iTunes</a></em>.</p>
