---
nid: 2474
title: "Vagrant - NFS shared folders for Mac/Linux hosts, Samba shares for Windows"
slug: "vagrant-nfs-shared-folders"
date: 2014-02-12T04:16:49+00:00
drupal:
  nid: 2474
  path: /blogs/jeff-geerling/vagrant-nfs-shared-folders
  body_format: full_html
  redirects: []
tags:
  - drupal planet
  - performance
  - samba
  - sync
  - vagrant
  - virtualbox
  - virtualization
aliases:
  - /blogs/jeff-geerling/vagrant-nfs-shared-folders
---

[Edit: I'm not using rsync shared folders (a new feature in 1.5+) instead of SMB/NFS - please see this post for more info: <a href="https://servercheck.in/blog/rsync-vagrant-15-file-performance-windows-dev">rsync in Vagrant 1.5 improves file performance and Windows usage</a>].

[Edit 2: Some people have reported success using the <code>vagrant-winnfsd</code> plugin to use NFS in Windows.]

I've been using Vagrant to provision local development and testing VMs for a couple years, and on my Mac, NFS shared folders (which are supported natively by VirtualBox) work great; they're many, many times faster than native shared folders. To set up an NFS share in your Vagrantfile, just make sure the <code>nfs-utils</code> package is installed on the managed VM, and add the following:

```
    config.vm.synced_folder "~/Sites/shared", "/shared",
      :nfs => !is_windows,
      id: "shared"
```

<em>Note</em>: See <a href="https://github.com/geerlingguy/JJG-Ansible-Windows">JJG-Ansible-Windows</a> to see how you can get the <code>is_windows</code> variable.

Regular shared folders (just like above, but without the :nfs option) work well if you just need to access a file or two from time to time within the VM, but are abysmal for any file operation performance—doubly so if you're trying to run any typical PHP application (like Drupal or Wordpress) from within the shared folder; the VM needs to access hundreds of files per page request, and slow individual file access makes the overall operation abysmally slow! (For more on VM filesystem performance, see Mitchell Hashimoto's excellent post <a href="http://mitchellh.com/comparing-filesystem-performance-in-virtual-machines">Comparing Filesystem Performance in Virtual Machines</a>).

On Windows, NFS is not really an option; you might be able to find hackish ways to get NFS working (like <a href="http://www.jankowfsky.com/blog/2013/11/28/nfs-for-vagrant-under-windows/">this</a> or <a href="https://github.com/mitchellh/vagrant/issues/2806">this</a>), but it's not worth the effort at this point in time. Additionally, I investigated using a Windows shared folder on your PC, and connecting to it by mounting it with samba on the VM, but doing that resulted in <em>worse</em> performance than VirtualBox's native shared folder support!

<p style="text-align: center;">{{< figure src="./drupal-page-load-vagrant-virtualbox-nfs-samba.png" alt="VirtualBox shared folder performance with Vagrant - samba NFS native and virtualbox shares" width="511" height="283" >}}
Your results may vary. This was unscientific, only two runs after a cache clear using each method.</p>

The best solution for performance (on Windows) is to have your code live within the VM's disk image—if you do this, VirtualBox's filesystem caching will give a nice speed boost, and performance should be close to native. Unfortunately, if your code lives within the VM, you have to log into the VM to access the code, or you have to use some sort of SFTP utility to manage files. Definitely not ideal.

For the benefit of my co-workers who are forced to use Windows at work, I decided to set up a Samba share <em>within</em> the VM to which the Windows host could connect via a mapped drive (making file access/management work like a native Windows filesystem, albeit with <em>slightly</em> slower-than-native access from the Windows side. For our development workflow, this made our Drupal sites load in milliseconds instead of many seconds, which sped up our development greatly.

Here's how to set up your VM (these instructions assume CentOS, but setup would be similar for other Linux flavors) to create a samba share that can be mounted from Windows (or Mac/Linux... but like I said earlier, I like keeping my Mac set up with NFS, since that allows the best of both worlds):

<ol>
<li>Install samba: <code>sudo yum -y install samba samba-common cifs-utils</code></li>
<li>Start samba and make it run on boot: <code>sudo service smb start</code>, then <code>sudo chkconfig smb on</code></li>
<li>Add something like the following to the bottom of <code>/etc/samba/smb.conf</code>, then restart samba (<code>sudo service smb restart</code>).

```
[shared]
path = /shared
public = yes
browseable = yes
writable = yes
guest ok = yes
guest only = yes
guest account = root
</code></li>
</ol>

<strong>Security note/warning</strong>: These samba share settings are <em>highly</em> insecure. The only reason I use these settings is so the windows users don't need to use a username/password, or worry about file permissions (much) when operating on files within the share via Windows. If you aren't using private VM networking, or are doing anything on a non-local server, you should use more secure settings.

If you have a restrictive firewall on the VM (some people don't worry about such things for development VMs...), you'll also need to open ports 137, 138, 139, and 445 (make note of the UDP/TCP differences below):

<code>
sudo iptables -A INPUT -m state --state NEW -p udp --dport 137 -j ACCEPT
sudo iptables -A INPUT -m state --state NEW -p udp --dport 138 -j ACCEPT
sudo iptables -A INPUT -m state --state NEW -p tcp --dport 139 -j ACCEPT
sudo iptables -A INPUT -m state --state NEW -p tcp --dport 445 -j ACCEPT
sudo iptables -A INPUT -m state --state NEW -p udp --dport 445 -j ACCEPT
```

Once samba is restarted and the firewall is open, you can map a network drive from Windows Explorer, using the path <code>\\[ip-address-of-vm]\shared</code>. You won't need to enter a username or password, it should just open up the drive and allow you to use whatever code editor/file management you normally use in Windows.

If you want to map the drive on a Mac (though, as I said earlier, NFS is probably a better option for Mac users), go to the Finder and press Command-K (Go > Connect to Server...), and connect to Server Address <code>smb://[ip-address-of-vm]/shared</code>.

As I said earlier, accessing the samba share in Mac OS X / Windows incurs a little performance penalty (doing git operations/full search on a large directory will be slower), but it's well worth the price to allow Windows users to load pages in a reasonable amount of time!
