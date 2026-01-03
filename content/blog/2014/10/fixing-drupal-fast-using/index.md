---
nid: 2467
title: "Fixing Drupal Fast - Using Ansible to deploy a security update on many sites"
slug: "fixing-drupal-fast-using"
date: 2014-10-16T04:01:54+00:00
drupal:
  nid: 2467
  path: /blogs/jeff-geerling/fixing-drupal-fast-using
  body_format: full_html
  redirects: []
tags:
  - ansible
  - drupal
  - drupal 7
  - drupal planet
  - security
aliases:
  - /blogs/jeff-geerling/fixing-drupal-fast-using
---

<p>Earlier today, the Drupal Security Team announced <a href="https://www.drupal.org/SA-CORE-2014-005">SA-CORE-2014-005 - Drupal core - SQL injection</a>, a 'Highly Critical' bug in Drupal 7 core that could result in SQL injection, leading to a whole host of other problems.</p>

<p>While not a regular occurrence, this kind of vulnerability is disclosed from time to time—if not in Drupal core, in some popular contributed module, or in some package you have running on your Internet-connected servers. What's the best way to update your entire infrastructure (all your sites and servers) against a vulnerability like this, and <em>fast</em>? High profile sites could be quickly targeted by criminals, and need to be able to deploy a fix ASAP... and though lower-profile sites may not be immediately targeted, you can bet there will eventually be a malicious bot scanning for vulnerable sites, so these sites need to still apply the fix in a timely manner.</p>

<p>In this blog post, I'll show how I patched all of Midwestern Mac's Drupal 7 sites in less than 5 minutes.</p>

<h2>
<a name="user-content-hotfixing-drupal-core---many-options" class="anchor" href="#hotfixing-drupal-core---many-options" aria-hidden="true"><span class="octicon octicon-link"></span></a>Hotfixing Drupal core - many options</h2>

<p>Before we begin, let me start off by saying there are many ways you can apply a security patch, and some are simpler than others. As many have pointed out (e.g. <a href="https://drupalize.me/blog/201410/tips-applying-drupal-core-security-updates">Lullabot</a>, you can simply download the <a href="https://www.drupal.org/files/issues/SA-CORE-2014-005-D7.patch">one line patch</a> and apply it to your Drupal codebase using <code>patch -p1</code>.</p>

<p>You could also use Drush to do a Drupal core update (<code>drush up drupal</code>), but you'll still need to do this, manually, on every Drupal installation you manage.</p>

<p>If you have multiple webservers with Drupal (or multiple instances of Drupal 7 on a single server, or spread across multiple servers), then there are simpler ways of either deploying the hotfix, or upgrading Drupal core via drush and/or version control (you are using Git or some other VCS, right?).</p>

<h2>
<a name="user-content-enter-ansible-the-swiss-army-knife-for-infrastructure" class="anchor" href="#enter-ansible-the-swiss-army-knife-for-infrastructure" aria-hidden="true"><span class="octicon octicon-link"></span></a>Enter Ansible, the Swiss Army Knife for infrastructure</h2>

<p><a href="http://www.ansible.com/">Ansible</a> is a powerful infrastructure management tool. It does Configuration Management (CM), just like Puppet or Chef, but it goes much, much further. One great feature of Ansible is the ability to run ad-hoc commands against a bunch of servers at once.</p>

<p>After <a href="http://docs.ansible.com/intro_installation.html">installing Ansible</a>, you need to create a hosts file at <code>/etc/ansible/hosts</code>, and tell Ansible about your servers (this is an 'inventory' of servers). Here's a simplified overview of my file:</p>


```
[mm]
jeffgeerling.com drupal_docroot=/path/to/drupal

[servercheck-drupal]
servercheck.in drupal_docroot=/path/to/drupal

[hostedsolr-drupal]
hostedapachesolr.com drupal_docroot=/path/to/drupal

[drupal7:children]
mm
servercheck-drupal
hostedsolr-drupal
```

<p>There are a couple quick things to note: the inventory file follows an ini-style format, so you define groups of servers with <code>[groupname]</code> (then list the servers one by one after the group name, with optional variables in <code>key=value</code> format after the server name), then define groups of groups with <code>[groupname:children]</code> (then list the groups you want to include in this group). We defined a group for each site (currently each group just has one Drupal web server), then defined a <code>drupal7</code> group to contain all the Drupal 7 servers.</p>

<p>As long as you can connect to the servers using SSH, you're golden. No additional configuration, no software to install on the servers, nada.</p>

<p>Let's go ahead and quickly check if we can connect to all our servers with the <code>ansible</code> command:</p>


```
$ ansible drupal7 -m ping
hostedapachesolr.com | success >> {
    "changed": false,
    "ping": "pong"
}
[...]
```

<p>All the servers have responded with a 'pong', so we know we're connected. Yay!</p>

<p>For a simple fix, we could add a variable to our inventory file for each server defining the Drupal document root(s) on the server, then use that variable to apply the hotfix like so:</p>


```
$ ansible drupal7 -m shell -a "curl https://www.drupal.org/files/issues/SA-CORE-2014-005-D7.patch | patch -p1 chdir={{ drupal_docroot }}"
```

<p>This would quickly apply the hotfix on all your servers, using Ansible's <code>shell</code> module (which, conveniently, runs shell commands verbatim, and tells you the output).</p>

<h3>
<a name="user-content-fixing-core-and-much-more" class="anchor" href="#fixing-core-and-much-more" aria-hidden="true"><span class="octicon octicon-link"></span></a>Fixing core, and much more</h3>

<p>Instead of running one command via <code>ansible</code>, let's make a really simple, short Ansible playbook to fix and verify the vulnerability. I created a file named <code>drupal-fix.yml</code> (that's right, Ansible uses plain old YAML files, just like Drupal 8!), and put in the following contents:</p>


```
---
- hosts: drupal7
  tasks:
    - name: Download drupal core patch.
      get_url:
        url: https://www.drupal.org/files/issues/SA-CORE-2014-005-D7.patch
        dest: /tmp/SA-CORE-2014-005-D7.patch

    - name: Apply the patch from the drupal docroot.
      shell: "patch -p1 < /tmp/SA-CORE-2014-005-D7.patch chdir={{ drupal_docroot }}"

    - name: Restart apache (or nginx, and/or php-fpm, etc.) to rebuild opcode cache.
      service: name=httpd state=restarted

    - name: Clear Drupal caches (because it's always a good idea).
      command: "drush cc all chdir={{ drupal_docroot }}"

    - name: Ensure we're not vulnerable anymore.
      [redacted]
```

<p>Now, there are again many, many different ways I could've done this. (And to the eagle-eyed, you'll note I haven't included my test for the vulnerability... I'd rather not share how to test for the vulnerability until people have had a chance to update all their sites).</p>

<p>I chose to do the hotfix first, and quickly, since I didn't necessarily have time to update all my Drupal project codebases to Drupal 7.32, then push the updated code to all my repositories. I <em>did</em> do this later in the day, however, and used a playbook similar to the above, replacing the first two tasks with:</p>


```
- name: Pull down the latest code changes.
  git:
    repo: "git://[mm-git-host]/{{ inventory_hostname }}.git"
    dest: "{{ drupal_docroot }}"
    version: master
```

<p>Using Ansible's <code>git</code> module, I can tell Ansible to make sure the given directory (<code>dest</code>) has the latest commit to the <code>master</code> branch in the given <code>repo</code>. I could've also used a <code>command</code> and run <code>git pull</code> from the <code>drupal_docroot</code> directory, but I like using Ansible's git module, which provides great reporting and error handling.</p>

<h2>
<a name="user-content-summary" class="anchor" href="#summary" aria-hidden="true"><span class="octicon octicon-link"></span></a>Summary</h2>

<p>This post basically followed my train of thought after hearing about the vulnerability, and while there are a dozen other ways to patch the vulnerability on multiple sites/servers, this was the way I did it. Though I patched just 9 servers in about 5 minutes (from the time I started writing the playbook (<code>drupal-fix.yml</code>) to the time it was deployed everywhere), I could just as easily have deployed the fix to dozens or hundreds of Drupal servers in the same amount of time; Ansible is fast and uses simple, secure SSH connections to manage servers.</p>

<p>If you want to see much, much more about what Ansible can do for your infrastructure, please check out my book, <a href="https://leanpub.com/ansible-for-devops">Ansible for DevOps</a>, and also check out my session from DrupalCon Austin earlier this year: <a href="https://austin2014.drupal.org/session/devops-humans-ansible-drupal-deployment-victory.html">DevOps for Humans: Ansible for Drupal Deployment Victory!</a>.</p>
