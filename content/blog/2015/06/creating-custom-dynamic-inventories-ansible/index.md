---
nid: 2596
title: "Creating custom dynamic inventories for Ansible"
slug: "creating-custom-dynamic-inventories-ansible"
date: 2015-06-11T20:36:35+00:00
drupal:
  nid: 2596
  path: /blog/creating-custom-dynamic-inventories-ansible
  body_format: full_html
  redirects: []
tags:
  - ansible
  - ansible for devops
  - dynamic inventory
  - inventory
aliases:
  - /blog/creating-custom-dynamic-inventories-ansible
---

<blockquote>
The following is an excerpt from Chapter 7 of <a href="http://ansiblefordevops.com/">Ansible for DevOps</a>, a book on Ansible by Jeff Geerling.
</blockquote>

<p>Most infrastructure can be managed with a custom inventory file or an off-the-shelf cloud inventory script, but there are many situations where more control is needed. Ansible will accept any kind of executable file as an inventory file, so you can build your own dynamic inventory however you like, as long as you can pass it to Ansible as JSON.</p>

<p>You could create an executable binary, a script, or anything else that can be run and will output JSON to stdout, and Ansible will call it with the argument <code>--list</code> when you run, as an example, <code>ansible all -i my-inventory-script -m ping</code>.</p>

<p>Let's start working our own custom dynamic inventory script by outlining the basic JSON format Ansible expects:</p>

```
{
    "group": {
        "hosts": [
            "192.168.28.71",
            "192.168.28.72"
        ],
        "vars": {
            "ansible_ssh_user": "johndoe",
            "ansible_ssh_private_key_file": "~/.ssh/mykey",
            "example_variable": "value"
        }
    },
    "_meta": {
        "hostvars": {
            "192.168.28.71": {
                "host_specific_var": "bar"
            },
            "192.168.28.72": {
                "host_specific_var": "foo"
            }
        }
    }
}
```

<p>Ansible expects a dictionary of groups (each group having a list of <code>hosts</code>, and group variables in the group's <code>vars</code> dictionary), and a <code>_meta</code> dictionary that stores host variables for all hosts individually (inside a <code>hostvars</code> dictionary).</p>

<blockquote>
<p>When you return a <code>_meta</code> dictionary in your inventory script, Ansible stores that data in its cache and doesn't call your inventory script <em>N</em> times for all the hosts in the inventory. You can leave out the <code>_meta</code> variables if you'd rather structure your inventory file to return host variables one host at a time (Ansible will call your script with the arguments <code>--host [hostname]</code> for each host), but it's often faster and easier to simply return all variables in the first call. In this book, all the examples will use the <code>_meta</code> dictionary.</p>
</blockquote>

<p>The dynamic inventory script can do anything to get the data (call an external API, pull information from a database or file, etc.), and Ansible will use it as an inventory source as long as it returns a JSON structure like the one above when the script is called with the <code>--list</code>.</p>

<h2>
<a id="user-content-building-a-custom-dynamic-inventory-in-python" class="anchor" href="#building-a-custom-dynamic-inventory-in-python" aria-hidden="true"><span class="octicon octicon-link"></span></a>Building a Custom Dynamic Inventory in Python</h2>

<p>To create a test dynamic inventory script for demonstration purposes, let's set up a quick set of two VMs using Vagrant. Create the following <code>Vagrantfile</code> in a new directory:</p>

```
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.insert_key = false
  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "256"]
  end

  # Application server 1.
  config.vm.define "inventory1" do |inventory|
    inventory.vm.hostname = "inventory1.dev"
    inventory.vm.box = "geerlingguy/ubuntu1404"
    inventory.vm.network :private_network, ip: "192.168.28.71"
  end

  # Application server 2.
  config.vm.define "inventory2" do |inventory|
    inventory.vm.hostname = "inventory2.dev"
    inventory.vm.box = "geerlingguy/ubuntu1404"
    inventory.vm.network :private_network, ip: "192.168.28.72"
  end
end
```

<p>Run <code>vagrant up</code> to boot two VMs running Ubuntu 14.04, with the IP addresses <code>192.168.28.71</code>, and <code>192.168.28.72</code>. A simple inventory file could be used to control the VMs with Ansible:</p>

```
[group]
192.168.28.71 host_specific_var=foo
192.168.28.72 host_specific_var=bar

[group:vars]
ansible_ssh_user=vagrant
ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key
example_variable=value
```

<p>However, let's assume the VMs were provisioned by another system, and you need to get the information through a dynamic inventory script. Here's a simple implementation of a dynamic inventory script in Python:</p>

```
#!/usr/bin/env python

'''
Example custom dynamic inventory script for Ansible, in Python.
'''

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory);

    # Example inventory for testing.
    def example_inventory(self):
        return {
            'group': {
                'hosts': ['192.168.28.71', '192.168.28.72'],
                'vars': {
                    'ansible_ssh_user': 'vagrant',
                    'ansible_ssh_private_key_file':
                        '~/.vagrant.d/insecure_private_key',
                    'example_variable': 'value'
                }
            },
            '_meta': {
                'hostvars': {
                    '192.168.28.71': {
                        'host_specific_var': 'foo'
                    },
                    '192.168.28.72': {
                        'host_specific_var': 'bar'
                    }
                }
            }
        }

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()
```

<p>Save the above as <code>inventory.py</code> in the same folder as the <code>Vagrantfile</code> you created earlier (and make sure you booted the two VMs with <code>vagrant up</code>), and make the file executable <code>chmod +x inventory.py</code>.</p>

<p>Run the inventory script manually to verify it returns the proper JSON response when run with <code>--list</code>:</p>


```
$ ./inventory.py --list
{"group": {"hosts": ["192.168.28.71", "192.168.28.72"], "vars":
{"ansible_ssh_user": "vagrant", "ansible_ssh_private_key_file":
"~/.vagrant.d/insecure_private_key", "example_variable": "value
"}}, "_meta": {"hostvars": {"192.168.28.72": {"host_specific_va
r": "bar"}, "192.168.28.71": {"host_specific_var": "foo"}}}}
```

<p>Test Ansible's ability to use the inventory script to contact the two VMs:</p>


```
$ ansible all -i inventory.py -m ping
192.168.28.71 | success &gt;&gt; {
    "changed": false,
    "ping": "pong"
}

192.168.28.72 | success &gt;&gt; {
    "changed": false,
    "ping": "pong"
}
```

<p>Since Ansible can connect, verify the configured host variables (<code>foo</code> and <code>bar</code>) are set correctly on each of their respective hosts:</p>


```
$ ansible all -i inventory.py -m debug -a "var=host_specific_var"
192.168.28.71 | success &gt;&gt; {
    "var": {
        "host_specific_var": "foo"
    }
}

192.168.28.72 | success &gt;&gt; {
    "var": {
        "host_specific_var": "bar"
    }
}
```

<p>The only changes you'd need to make to the above <code>inventory.py</code> script for real-world usage is to change the <code>example_inventory()</code> method to something that incorporates the business logic you need for your own inventory—whether calling an external API with all the server data, or pulling in the information from a database or other data store.</p>

<h2>
<a id="user-content-building-a-custom-dynamic-inventory-in-php" class="anchor" href="#building-a-custom-dynamic-inventory-in-php" aria-hidden="true"><span class="octicon octicon-link"></span></a>Building a Custom Dynamic Inventory in PHP</h2>

<p>You can build an inventory script in whatever language you'd like; the same Python script above can be ported to functional PHP as follows:</p>


```
#!/usr/bin/php
<?php

/**
 * @file
 * Example custom dynamic inventory script for Ansible, in PHP.
 */

/**
 * Example inventory for testing.
 *
 * @return array
 *   An example inventory with two hosts.
 */
function example_inventory() {
  return [
    'group' => [
      'hosts' => ['192.168.28.71', '192.168.28.72'],
      'vars' => [
        'ansible_ssh_user' => 'vagrant',
        'ansible_ssh_private_key_file' => '~/.vagrant.d/insecure_private_key',
        'example_variable' => 'value',
      ],
    ],
    '_meta' => [
      'hostvars' => [
        '192.168.28.71' => [
          'host_specific_var' => 'foo',
        ],
        '192.168.28.72' => [
          'host_specific_var' => 'bar',
        ],
      ],
    ],
  ];
}

/**
 * Empty inventory for testing.
 *
 * @return array
 *   An empty inventory.
 */
function empty_inventory() {
  return ['_meta' => ['hostvars' => new stdClass()]];
}

/**
 * Get inventory.
 *
 * @param array $argv
 *   Array of command line arguments (as returned by $_SERVER['argv']).
 *
 * @return array
 *   Inventory of groups or vars, depending on arguments.
 */
function get_inventory($argv = []) {
  $inventory = new stdClass();

  // Called with `--list`.
  if (!empty($argv[1]) && $argv[1] == '--list') {
    $inventory = example_inventory();
  }
  // Called with `--host [hostname]`.
  elseif ((!empty($argv[1]) && $argv[1] == '--host') && !empty($argv[2])) {
    // Not implemented, since we return _meta info `--list`.
    $inventory = empty_inventory();
  }
  // If no groups or vars are present, return an empty inventory.
  else {
    $inventory = empty_inventory();
  }

  print json_encode($inventory);
}

// Get the inventory.
get_inventory($_SERVER['argv']);

?>
```

<p>If you were to save the code above into the file <code>inventory.php</code>, mark it executable (<code>chmod +x inventory.php</code>), and run the same Ansible command as earlier (referencing <code>inventory.php</code> instead of <code>inventory.py</code>), the command should succeed just as with the Python example.</p>

<blockquote>
<p>All the files mentioned in these dynamic inventory examples are available in the <a href="https://github.com/geerlingguy/ansible-for-devops">Ansible for DevOps GitHub repository</a>, in the <code>dynamic-inventory</code> folder.</p>
</blockquote>

<h2>
<a id="user-content-managing-a-paas-with-a-custom-dynamic-inventory" class="anchor" href="#managing-a-paas-with-a-custom-dynamic-inventory" aria-hidden="true"><span class="octicon octicon-link"></span></a>Managing a PaaS with a Custom Dynamic Inventory</h2>

<p><a href="https://hostedapachesolr.com/">Hosted Apache Solr</a>'s infrastructure is built using a custom dynamic inventory to allow for centrally-controlled server provisioning and configuration. Here's how the server provisioning process works on Hosted Apache Solr:</p>

<ol>
<li>A Drupal website holds a 'Server' content type that stores metadata about each server (e.g. chosen hostname, data center location, choice of OS image, and memory settings).</li>
<li>When a new server is added, a remote Jenkins job is triggered, which:

<ol>
<li>Builds a new cloud server on DigitalOcean using an Ansible playbook.</li>
<li>Runs a provisioning playbook on the server to initialize the configuration.</li>
<li>Adds a new DNS entry for the server.</li>
<li>Posts additional server metadata (like the IP address) back to the Drupal website via a private API.</li>
</ol>
</li>
<li>When a server is updated, or there is new configuration to be deployed to the server(s), a different Jenkins job is triggered, which:

<ol>
<li>Runs the same provisioning playbook on all the DigitalOcean servers. This playbook uses an inventory script which calls back to an inventory API endpoint that returns all the server information as JSON (the inventory script on the Jenkins server passes the JSON through to stdout).</li>
<li>Reports back success or failure of the ansible playbook to the REST API.</li>
</ol>
</li>
</ol>

<p>The above process transformed the management of the entire Hosted Apache Solr platform. Instead of taking twenty to thirty minutes to build a new server (when using an Ansible playbook with a few manual steps), the process can be completed in just a few minutes, with no manual intervention.</p>

<blockquote>
<p>The security of your server inventory and infrastructure management should be a top priority; Hosted Apache Solr uses HTTPS everywhere, and has a hardened private API for inventory access and server metadata. If you have any automated processes that run over a network, you should make doubly sure you audit these processes and all the involved systems thoroughly!</p>
</blockquote>

<p><em>Read Ansible for DevOps, available on LeanPub:</em></p>

<iframe width="160" height="400" src="https://leanpub.com/ansible-for-devops/embed" frameborder="0" allowtransparency="true"></iframe>
