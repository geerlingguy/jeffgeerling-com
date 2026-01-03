---
nid: 2608
title: "Testing Ansible Roles with Travis CI on GitHub"
slug: "testing-ansible-roles-travis-ci-github"
date: 2014-05-23T20:56:40+00:00
drupal:
  nid: 2608
  path: /blog/testing-ansible-roles-travis-ci-github
  body_format: full_html
  redirects: []
tags:
  - ansible
  - ansible galaxy
  - automation
  - ci
  - continuous integration
  - github
  - roles
  - testing
  - travis ci
aliases:
  - /blog/testing-ansible-roles-travis-ci-github
   - /blog/testing-ansible-roles-travis-ci-github
---

<blockquote>This post was originally written in 2014, using a technique that only easily allows testing on Ubuntu 12.04; since then, I've been adapting many of my roles (e.g. <a href="https://github.com/geerlingguy/ansible-role-apache">geerlingguy.apache</a>) to use a Docker container-based testing approach, and I've written a new blog post that details the new technique: <a href="/blog/2016/how-i-test-ansible-configuration-on-7-different-oses-docker">How I test Ansible configuration on 7 different OSes with Docker</a>.</blockquote>

<p>Since I'm now maintaining <a href="https://galaxy.ansible.com/list#/users/219">37 roles</a> on Ansible Galaxy, there's no way I can spend as much time reviewing every aspect of every role when doing maintenance, or checking out pull requests to improve the roles. Automated testing using a continuous integration tool like <a href="https://travis-ci.org/">Travis CI</a> (which is free for public projects and integrated very well with GitHub) allows me to run tests against my Ansible roles with every commit and be more assured nothing broke since the last commit.</p>

<p style="text-align: center;">{{< figure src="./ansible-role-passing-tests-travis-ci-github.png" alt="Ansible role with passing tests on GitHub with Travis CI" width="411" height="143" class="inserted-image" >}}</p>

<p>Plus, I love the small endorphin kick induced by seeing the green "build passing" icon on my project's home page.</p>

<p>There are four main things I make sure I test when building and maintaining an Ansible role:</p>

<ol>
<li>The role's syntax (are all the .yml files formatted correctly?).</li>
<li>Whether the role will run through all the included tasks without failing.</li>
<li>The role's idempotence (if run again, the role should not make any changes!).</li>
<li>The role's success (does the role do what it should be doing?).</li>
</ol><p>Ultimately, the most important aspect is #4, because what's the point of a role if it doesn't do what you want it to do (e.g. start a web server, configure a database, deploy an app, etc.)?</p>

<h2>
<a name="user-content-setting-up-your-role-for-testing" class="anchor" href="#setting-up-your-role-for-testing"><span class="octicon octicon-link"></span></a>Setting up your role for testing</h2>

<p>Since you're going to need a simple Ansible playbook and inventory file to test your role, you can create both inside a new 'tests' directory in your Ansible role:</p>


```
# Directory structure:
my_role/
  tests/
    test.yml <-- your test playbook
    inventory <-- an inventory file to use with the playbook
```

<p>Inside the <code>inventory</code> file, add:</p>


```
localhost
```

<p>We just want to tell Ansible to run commands on the local machine (we'll use the <code>--connection=local</code> option when running the test playbook).</p>

<p>Inside <code>test.yml</code>, add:</p>


```
---
- hosts: localhost
  remote_user: root
  roles:
    - github-role-project-name
```

<p>Substitute your own role name for <code>[github-role-project-name]</code> (e.g. <code>ansible-role-django</code>). This is a typical Ansible playbook, and we tell Ansible to run the tasks on localhost, with the <code>root</code> user (otherwise, you could run tasks with <code>travis</code> if you want, and use <code>sudo</code> on certain tasks). You can add <code>vars</code>, <code>vars_files</code>, etc. if you want, but we'll keep things simple, because for many smaller roles, the role is pre-packaged with sane defaults and all the other info it needs to run.</p>

<p>The next step is to add a <a href="http://docs.travis-ci.com/user/build-configuration/"><code>.travis.yml</code></a> file to your role so Travis CI will pick it up and use it for testing. Add that file to the root level of your role, and add the following to kick things off:</p>


```
---
language: python
python: "2.7"

before_install:
  # Make sure everything's up to date.
  - sudo apt-get update -qq

install:
  # Install Ansible.
  - pip install ansible

  # Add ansible.cfg to pick up roles path.
  - "printf '[defaults]\nroles_path = ../' > ansible.cfg"

script:
  # We'll add some commands to test the role here.
```

<p>The only surprising part here is the <code>printf</code> line in the <code>install</code> section; I've added that line to create a quick and dirty <code>ansible.cfg</code> configuration file Ansible will use to set the <code>roles_path</code> one directory up from the current working directory. That way, we can include roles like <code>github-role-project-name</code>, or if we use <code>ansible-galaxy</code> to download dependencies (as another command in the <code>install</code> section), we can just use <code>- galaxy-role-name-here</code> to include that role in our <code>test.yml</code> playbook.</p>

<p>Now that we have the basic structure, it's time to start adding the commands to test our role.</p>

<h2>
<a name="user-content-testing-the-roles-syntax" class="anchor" href="#testing-the-roles-syntax"><span class="octicon octicon-link"></span></a>Testing the role's syntax</h2>

<p>This is the easiest test; <code>ansible-playbook</code> has a built in command that will check a playbook's syntax (including all the included files and roles), and return <code>0</code> if there are no problems, or an error code and some output if there were any syntax issues.</p>


```
ansible-playbook -i tests/inventory tests/test.yml --syntax-check
```

<p>Add this as a command in the <code>script</code> section of <code>.travis.yml</code>:</p>


```
script:
  # Check the role/playbook's syntax.
  - ansible-playbook -i tests/inventory tests/test.yml --syntax-check
```

<p>If there are any syntax errors, Travis will fail the build and output the errors in the log.</p>

<h2>
<a name="user-content-role-success---first-run" class="anchor" href="#role-success---first-run"><span class="octicon octicon-link"></span></a>Role success - first run</h2>

<p>The next aspect to check is whether the role runs correctly or fails on it's first run.</p>


```
# Run the role/playbook with ansible-playbook.
- "ansible-playbook -i tests/inventory tests/test.yml --connection=local --sudo"
```

<p>This is a basic ansible-playbook command, which runs the playbook <code>test.yml</code> against the local host, using <code>--sudo</code>, and with the <code>inventory</code> file we added to the role's <code>tests</code> directory.</p>

<p>Ansible returns a non-zero exit code if the playbook run fails, so Travis will know whether the command succeeded or failed.</p>

<h2>
<a name="user-content-role-idempotence" class="anchor" href="#role-idempotence"><span class="octicon octicon-link"></span></a>Role idempotence</h2>

<p>Another important test is the idempotence test—does the role change anything if it runs a second time? It should not, since all tasks you perform via Ansible should be idempotent (ensuring a static/unchanging configuration on subsequent runs with the same settings).</p>


```
# Run the role/playbook again, checking to make sure it's idempotent.
- >
  ansible-playbook -i tests/inventory tests/test.yml --connection=local --sudo
  | grep -q 'changed=0.*failed=0'
  && (echo 'Idempotence test: pass' && exit 0)
  || (echo 'Idempotence test: fail' && exit 1)
```

<p>This command runs the exact same command as before, but pipes the results through grep, which checks to make sure 'changed' and 'failed' both report <code>0</code>. If there were no changes or failures, the idempotence test passes (and Travis sees the <code>0</code> exit and is happy), but if there were any changes or failures, the test fails (and Travis sees the <code>1</code> exit and reports a build failure).</p>

<h2>
<a name="user-content-role-success---final-result" class="anchor" href="#role-success---final-result"><span class="octicon octicon-link"></span></a>Role success - final result</h2>

<p>The last thing I check is whether the role actually did what it was supposed to do. If it configured a web server, is the server responding on port 80 or 443 without any errors? If it configured a command line application, does that command line application work when invoked, and do the things it's supposed to do?</p>


```
# Request a page via the web server, to make sure it's running and responds.
- "curl http://localhost/"
```

<p>In this example, I'm testing a web server by loading 'localhost'; curl will exit with a 0 status (and dump the output of the web server's response) if the server responds with a <code>200 OK</code> status, or will exit with a non-zero status if the server responds with an error status (like <code>500</code>) or is unavailable.</p>

<p>Taking this a step further, you could even run a deployed application or service's <em>own</em> automated tests after ansible is finished with the deployment, thus testing your infrastructure <em>and</em> application in one go—but we're getting ahead of ourselves here... that's a topic for a future post :)</p>

<h2>
<a name="user-content-some-notes-about-travis-ci" class="anchor" href="#some-notes-about-travis-ci"><span class="octicon octicon-link"></span></a>Some notes about Travis CI</h2>

<p>There are a few things you need to know about Travis CI, especially if you're testing Ansible, which will rely heavily on the VM environment inside which it is running:</p>

<ul>
<li>
<strong>Ubuntu 12.04</strong>: As of this writing, the only OS available via Travis CI is Ubuntu 12.04. Most of my roles work with Ubuntu/Debian/RedHat/CentOS, so it's not an issue for me... but if your roles strictly target a non-Debian-flavored distro, you probably won't get much mileage out of Travis.</li>
<li>
<strong>Preinstalled packages</strong>: Travis CI comes with a bunch of services installed out of the box, like MySQL, Elasticsearch, Ruby, etc. In the <code>.travis.yml</code> <code>before_install</code> section, you may need to do some <code>apt-get remove --purge [package]</code> commands and/or other cleanup commands to make sure the VM is fresh for your Ansible role's run.</li>
<li>
<strong>Networking/Disk/Memory</strong>: Travis CI continously shifts the VM specs you're using, so don't assume you'll have <em>X</em> amount of RAM, disk space, or network capacity. You can add commands like <code>cat /proc/cpuinfo</code>, <code>cat /proc/meminfo</code>, <code>free -m</code>, etc. in the <code>.travis.yml</code> <code>before_install</code> section if you need to figure out the resources available in your VM.</li>
</ul>

See much more information on the <a href="http://docs.travis-ci.com/user/ci-environment/">Travis CI Build Environment</a> page.

<h2>
<a name="user-content-real-world-examples" class="anchor" href="#real-world-examples"><span class="octicon octicon-link"></span></a>Real-world examples</h2>

I have integrated this style of testing into many of the roles I've submitted to <a href="https://galaxy.ansible.com/">Ansible Galaxy</a>; here are a few example roles that use Travis CI integration in the way I've outlined in this blog post:

<ul>
<li>https://github.com/geerlingguy/ansible-role-apache</li>
<li>https://github.com/geerlingguy/ansible-role-gitlab</li>
<li>https://github.com/geerlingguy/ansible-role-mysql</li>
</ul>

<p>These are some of the things I do to make my roles as thoroughly-tested as I can using some free resources; there are some other ways to go even deeper, and I hope to have more to share soon!</p>

<p>Also check out the <a href="http://docs.ansible.com/test_strategies.html">Testing Strategies</a> section of Ansible's documentation. There is some good information about how and what you should be testing your Ansible roles and playbooks.

<p><strong>This post has been adapted from one of the chapters in my book <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>, which is available for sale on LeanPub.</strong></p></body></html>
