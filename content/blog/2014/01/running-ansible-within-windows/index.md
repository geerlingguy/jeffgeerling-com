---
nid: 2613
title: "Running Ansible within Windows"
slug: "running-ansible-within-windows"
date: 2014-01-13T17:52:10+00:00
drupal:
  nid: 2613
  path: /blog/running-ansible-within-windows
  body_format: full_html
  redirects: []
tags:
  - ansible
  - ansible for devops
  - cmder
  - cygwin
  - powershell
  - windows
aliases:
  - /blog/running-ansible-within-windows
---

<blockquote><strong>2016 Update</strong>: If you are using Windows 10 or later, check out my newer instructions for <a href="/blog/2016/using-ansible-through-windows-10s-subsystem-linux">Using Ansible through Windows 10's Subsystem for Linux</a>.</blockquote>

<p><a href="http://docs.ansible.com/intro.html">Ansible</a> is a simple and powerful infrastructure and configuration management tool that Server Check.in uses to manage it's infrastructure. Installing and using Ansible on Mac OS X or Linux workstations is incredibly easy, and takes all of 30 seconds to set up.</p>

<p style="text-align: center;">{{< figure src="./ansible-version-windows-cygwin.png" alt="Running Ansible via Cygwin on Windows 7" width="593" height="326" >}}</p>
<p>Running Ansible commands from within Windows is unsupported at the time of this writing. <a href="https://groups.google.com/forum/#!topic/ansible-project/ayJ3nd0YTIc">According to the CTO of AnsibleWorks</a>, only windows servers as endpoints (not as hosts for controlling other servers via Ansible) are on the roadmap for future support... That said, if the idea of running a Linux VM on your Windows workstation (with something like the free <a href="https://www.virtualbox.org/">VirtualBox</a> app) just to run Ansible is unsettling, you can still use Ansible within Windows, if you run it within <a href="http://www.cygwin.com/">Cygwin</a>.</p>

<blockquote>
<p>As an aside, this blog post was written while researching for a book on Ansible: <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>. You can purchase Ansible for DevOps on <a href="https://leanpub.com/ansible-for-devops">LeanPub</a>, <a href="http://www.amazon.com/Ansible-DevOps-Server-configuration-management-ebook/dp/B016G55NOU/">Amazon</a>, or <a href="https://itunes.apple.com/us/book/ansible-for-devops/id1050383787?ls=1&mt=11">iTunes</a></em>.</p>
</blockquote>

<p>Here are steps to getting Ansible (and it's related commands, like <code>ansible-playbook</code>) running on Windows:</p>

<ol>
<li>
<p>Download and install <a href="http://cygwin.com/install.html">Cygwin</a>, with at least the following packages selected (you can select the packages during the install process):</p>
<ul>
<li>curl</li>
<li>python (2.7.x)</li>
<li>python-jinja</li>
<li>python-crypto</li>
<li>python-openssl</li>
<li>python-setuptools</li>
<li>git (1.7.x)</li>
<li>vim</li>
<li>openssh</li>
<li>openssl</li>
<li>openssl-devel</li>
</ul>
</li>
<li>
<p>If you are working behind a proxy (as is the case in many corporate networks), edit the .bash_profile used by Cygwin either using vim (open Cygwin and enter <code>vim .bash_profile</code>), or with whatever editor you'd like, and add in lines like the following:</p>


```
export http_proxy=http://username:password@proxy-address-here:80/
export https_proxy=https://username:password@proxy-address-here:80/
```

</li>
<li>
<p>Download and install separately <a href="https://pypi.python.org/pypi/PyYAML/3.10">PyYAML</a> and <a href="https://pypi.python.org/pypi/Jinja2/2.6">Jinja2</a> separately, as they're not available via Cygwin's installer:</p>

<ol>
<li>Open Cygwin</li>
<li>Download PyYAML:


```
curl -O https://pypi.python.org/packages/source/P/PyYAML/PyYAML-3.10.tar.gz
```

</li>
<li>Download Jinja2:


```
curl -O https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.6.tar.gz
```

</li>
<li>Untar both downloads:


```
tar -xvf PyYAML-3.10.tar.gz && tar -xvf Jinja2-2.6.tar.gz
```

</li>
<li>Change directory into each of the expanded folders and run <code>python setup.py install</code> to install each package.</li>
<li>Generate an SSH key for use later: <code>ssh-keygen</code>, then hit enter to skip adding a password until you get back to the command prompt.</li>
<li>Clone ansible from its repository on GitHub:


```
git clone https://github.com/ansible/ansible /opt/ansible
```

</li>
<li>If you'd like to work from a particular Ansible version (like 2.0.1, current as of this writing), change directory into <code>/opt/ansible</code> and checkout the correct tag: <code>git checkout v2.0.1</code> (some users have also reported success with the tag `v2_final`).</li>
<li>
<p>Add the following lines into your Cygwin .bash_profile (like you did the proxy settings—if you're behind one—in step 2):</p>

```
# Ansible settings
ANSIBLE=/opt/ansible
export PATH=$PATH:$ANSIBLE/bin
export PYTHONPATH=$ANSIBLE/lib
export ANSIBLE_LIBRARY=$ANSIBLE/library
```

</li>
<li><p>At this point, you should be able to run ansible commands via Cygwin (once you restart, or enter <code>source ~/.bash_profile</code> to pick up the settings you just added). Try <code>ansible --version</code> to display Ansible's version.</p></li>
</ol>
</li>
</ol><p>If you would like to use Ansible as a provisioner for <a href="http://www.vagrantup.com/">Vagrant</a>, you can try, but after a day's worth of frustration (to the point of trying to add custom .bat files, changing Windows' and Linux' %PATH%/$PATH multiple times, and doing a hundred other things besides), I would recommend using Linux or a Mac to use Vagrant + Ansible together, or you could also use something like my <a href="https://github.com/geerlingguy/JJG-Ansible-Windows">JJG-Ansible-Windows</a> shell provisioning script to run Ansible from within the VM itself.</p>

<p><em>Note</em>: It may also be possible to run Ansible more easily using a bootstrap like <a href="https://github.com/jonathanhle/ansible-babun-bootstrap">Ansible Babun Bootstrap</a>, but the experience of using Ansible on Windows will still be sub-par (but at least easier!).</em>

<p>I have written much more on how to use Ansible, whether you use Windows, Linux, or Mac OS X, in much greater detail, in <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>!</p>
