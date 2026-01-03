---
nid: 2595
title: "Automating Your Automation with Ansible Tower"
slug: "automating-your-automation-ansible-tower"
date: 2015-05-27T02:55:54+00:00
drupal:
  nid: 2595
  path: /blog/automating-your-automation-ansible-tower
  body_format: full_html
  redirects: []
tags:
  - ansible
  - ansible for devops
  - automation
  - cd
  - ci
  - continuous integration
  - tower
aliases:
  - /blog/automating-your-automation-ansible-tower
---

<blockquote>
The following is an excerpt from Chapter 11 of <a href="http://ansiblefordevops.com/">Ansible for DevOps</a>, a book on Ansible by Jeff Geerling. The example highlights the effectiveness of <a href="http://www.ansible.com/tower">Ansible Tower</a> for automating infrastructure operations, especially in a team environment.
</blockquote>

<p>Throughout this book, all the examples use Ansible's CLI to run playbooks and report back the results. For smaller teams, especially when everyone on the team is well-versed in how to use Ansible, YAML syntax, and follows security best practices with playbooks and variables files, using the CLI can be a sustainable approach.</p>

<p>But for many organizations, there are needs that stretch basic CLI use too far:</p>

<ul>
<li>The business needs detailed reporting of infrastructure deployments and failures, especially for audit purposes.</li>
<li>Team-based infrastructure management requires varying levels of involvement in playbook management, inventory management, and key and password access.</li>
<li>A thorough visual overview of the current and historical playbook runs and server health helps identify potential issues before they affect the bottom line.</li>
<li>Playbook scheduling can help ensure infrastructure remains in a known state.</li>
</ul>

<p>Ansible Tower checks off these items---and many more---and provides a great mechanism for team-based Ansible usage. The product is currently free for teams managing ten or fewer servers (it's basically an 'unlimited trial' mode), and has flexible pricing for teams managing dozens to thousands of servers.</p>

<p>While this book includes a brief overview of Tower, and how you can get started with Tower, it is highly recommended that you read through Ansible, Inc's extensive <a href="http://releases.ansible.com/ansible-tower/docs/tower_user_guide-latest.pdf">Tower User Guide</a>, which includes details this book won't be covering such as LDAP integration and multiple-team playbook management workflows.</p>

<h2>
<a id="user-content-getting-and-installing-ansible-tower" class="anchor" href="#getting-and-installing-ansible-tower" aria-hidden="true"><span class="octicon octicon-link"></span></a>Getting and Installing Ansible Tower</h2>

<p>Ansible has a very thorough <a href="http://releases.ansible.com/ansible-tower/docs/tower_user_guide-latest.pdf">Ansible Tower User Guide</a>, which details the installation and configuration of Ansible Tower. For the purposes of this chapter, since we just want to download and try out Tower locally, we are going to use Ansible's official Vagrant box to quickly build an Ansible Tower VM.</p>

<p>Make sure you have <a href="https://www.vagrantup.com/downloads.html">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox</a> installed, then create a directory (e.g. <code>tower</code>) and do the following within the directory:</p>

<ol>
<li><code>vagrant init tower http://vms.ansible.com/ansible-tower-2.1.4-virtualbox.box</code> (Create a new Vagrantfile using the Tower base box from Ansible).</li>
<li>
<code>vagrant up</code> (Build the Tower VM).</li>
<li>
<code>vagrant ssh</code> (Log into the VM, and Tower will display a message with connection information).</li>
</ol>

<blockquote>
The above installation instructions and Vagrant box come from a blog post on Ansible's official blog, <a href="http://www.ansible.com/blog/ansible-vagrant">Ansible Tower and Vagrant</a>.
</blockquote>

<p>You can now visit the URL provided by the login welcome message (something like <code>https://10.42.0.42/</code>), and after confirming a security exception for the Ansible Tower certificate, login with the credentials from step 3.</p>

<p>At this point, you will need to register a free trial license of Ansible Tower, which can be done following the instructions on the screen. The free trial allows you to use all of Tower's features for up to 10 servers, and is great for experimenting and seeing how Tower fits into your workflow. After you get the license (it's a block of JSON which you paste into the license field), you should get to Tower's default dashboard page:</p>

<p style="text-align: center;">{{< figure src="./ansible-tower-dashboard_0.png" alt="Ansible Tower's Dashboard" >}}</p>

<h2>
<a id="user-content-using-ansible-tower" class="anchor" href="#using-ansible-tower" aria-hidden="true"><span class="octicon octicon-link"></span></a>Using Ansible Tower</h2>

<p>Ansible Tower is centered around the idea of organizing <em>Projects</em> (which run your playbooks via <em>Jobs</em>) and <em>Inventories</em> (which describe the servers on which your playbooks should be run) inside of <em>Organizations</em>. <em>Organizations</em> can then be set up with different levels of access based on <em>Users</em> and <em>Credentials</em> grouped in different <em>Teams</em>. It can be a little overwhelming at first, but once you get the initial structure configured, you'll see how powerful and flexible Tower's Project workflow is.</p>

<p>Let's get started with our first project!</p>

<p>The first step is to make sure you have a test playbook you can run using Ansible Tower. Generally, your playbooks should be stored in a source code repository (e.g. Git or Subversion), with Tower configured to check out the latest version of the playbook from the repository and run it. Since we're only going to run a simple example, we will create a playbook in Tower's default <code>projects</code> directory located in <code>/var/lib/awx/projects</code>:</p>

<ol>
<li>Log into the Tower VM: <code>vagrant ssh</code></li>
<li>Switch to the <code>awx</code> user: <code>sudo su - awx</code>
</li>
<li>Go to Tower's default <code>projects</code> directory: <code>cd /var/lib/awx/projects</code>
</li>
<li>Create a new project directory: <code>mkdir ansible-for-devops &amp;&amp; cd ansible-for-devops</code>
</li>
<li>Create a new playbook file, <code>main.yml</code>, within the new directory, with the following contents:</li>
</ol>

```
---
- hosts: all
  gather_facts: no
  connection: local

  tasks:
    - name: Check the date on the server.
      command: date
```

<p>Switch back to your web browser and get everything set up to run the test playbook inside Ansible Tower's web UI:</p>

<ol>
<li>Create a new <em>Organization</em>, called 'Ansible for DevOps'.</li>
<li>Add a new User to the Organization, named John Doe, with the username <code>johndoe</code> and password <code>johndoe1234</code>.</li>
<li>Create a new <em>Team</em>, called 'DevOps Engineers', in the 'Ansible for DevOps' Organization.</li>
<li>Under the Team's Credentials section, add in SSH credentials by selecting 'Machine' for the Credential type, and setting 'Name' to <code>Vagrant</code>, 'Type' to <code>Machine</code>, 'SSH Username' to <code>vagrant</code>, and 'SSH Password' to <code>vagrant</code>.</li>
<li>Under the Team's Projects section, add a new <em>Project</em>. Set the 'Name' to <code>Tower Test</code>, 'Organization' to <code>Ansible for DevOps</code>, 'SCM Type' to <code>Manual</code>, and 'Playbook Directory' to <code>ansible-for-devops</code> (Tower automatically detects all folders placed inside <code>/var/lib/awx/projects</code>, but you could also use an alternate Project Base Path if you want to store projects elsewhere).</li>
<li>Under the Inventories section, add an <em>Inventory</em>. Set the 'Name' to <code>Tower Local</code>, and 'Organization' set to <code>Ansible for DevOps</code>. Once the inventory is saved:

<ol>
<li>Add a 'Group' with the Name <code>localhost</code>. Click on the group once it's saved.</li>
<li>Add a 'Host' with the Host Name <code>127.0.0.1</code>.</li>
</ol>
</li>
</ol>

<blockquote>
New <em>Credentials</em> have a somewhat dizzying array of options, and offer login and API key support for a variety of services, like SSH, AWS, Rackspace, VMWare vCenter, and SCM systems. If you can login to a system, Tower likely supports the login mechanism!
</blockquote>

<p>Now that we have all the structure for running playbooks configured, we need only create a <em>Job Template</em> so we can run the playbook on the localhost and see whether we've succeeded. Click on 'Job Templates', and create a new Job Template with the following configuration:</p>

<ul>
<li>Name: <code>Tower Test</code>
</li>
<li>Inventory: <code>Tower Local</code>
</li>
<li>Project: <code>Tower Test</code>
</li>
<li>Playbook: <code>main.yml</code>
</li>
<li>Machine Credential: <code>Vagrant</code>
</li>
</ul>

<p>Save the Job Template, then click the small Rocketship button to start a job using the template. You'll be redirected to a Job status page, which provides live updates of the job status, and then a summary of the playbook run when complete:</p>

<p style="text-align: center;">{{< figure src="./ansible-tower-job-complete.png" alt="Ansible Tower Test job completed successfully!" >}}</p>

<p>You can view the playbook run's standard output in real-time (or review it after the fact) with the 'View standard out' button. You can also stop a running job, delete a job's record, or relaunch a job with the same parameters using the respective buttons on the job's page.</p>

<p>The job's dashboard page is very useful for giving an overview of how many hosts were successful, how many tasks resulted in changes, and the timing of the different parts of the playbook run.</p>

<h2>
<a id="user-content-other-tower-features-of-note" class="anchor" href="#other-tower-features-of-note" aria-hidden="true"><span class="octicon octicon-link"></span></a>Other Tower Features of Note</h2>

<p>In our simple walkthrough above, we used Tower to run a simple playbook on the local server; setting up Tower to run playbooks on real-world infastructure or other local VMs is just as easy, and the tools Ansible Tower provides are very handy, especially when working in larger team environments.</p>

<p>This book won't walk through the entirety of Ansible Tower's documentation, but a few other simple features you should try out include:</p>

<ul>
<li>Setting up scheduled Job runs (especially with the 'Check' option instead of 'Run') for CI/CD.</li>
<li>Integrating user accounts and Teams with LDAP users and groups for automatic team-based project management.</li>
<li>Setting different levels of permissions for Users and Teams so certain users can edit certain jobs, others can only run certain jobs, and yet others can only view the results of job runs within an Organization.</li>
<li>Configuring Ansible Vault credentials so you can easily and automatically use Vault-protected variables in your playbooks.</li>
<li>Setting up Provisioning Callbacks so newly-provisioned servers can self-provision via a URL per Job Template.</li>
<li>Surveys, which allow users to add extra information based on a 'Survey' of questions per job run.</li>
<li>Inventory Scripts, which allow you to build inventory dynamically.</li>
<li>Built-in Munin monitoring (to monitor the Tower server), available with the same admin credentials at <code>https://[tower-hostname]/munin</code>.</li>
</ul>

<p>Ansible Tower continues to improve rapidly, and is one of the best ways to run Ansible Playbooks from a central CI/CD-style server with team-based access and extremely detailed live and historical status reporting.</p>

<h2>
<a id="user-content-tower-alternatives" class="anchor" href="#tower-alternatives" aria-hidden="true"><span class="octicon octicon-link"></span></a>Tower Alternatives</h2>

<p>Ansible Tower is purpose-built for use with Ansible playbooks, but there are many other ways to run playbooks on your servers with a solid workflow. If price is a major concern, and you don't need all the bells and whistles Tower provides, you can use other popular tools like <a href="http://jenkins-ci.org/">Jenkins</a>, <a href="http://rundeck.org/">Rundeck</a>, or <a href="http://www.go.cd/">Go CI</a>.</p>

<p>All these tools provide flexiblity and security for running Ansible Playbooks, and each one requires a different amount of setup and configuration before it will work well for common usage scenarios. One of the most popular and long-standing CI tools is Jenkins, so we'll explore how to configure a similar Playbook run in Jenkins next.</p>

<p><em>Read Ansible for DevOps, available on LeanPub:</em></p>

<iframe width="160" height="400" src="https://leanpub.com/ansible-for-devops/embed" frameborder="0" allowtransparency="true"></iframe>
