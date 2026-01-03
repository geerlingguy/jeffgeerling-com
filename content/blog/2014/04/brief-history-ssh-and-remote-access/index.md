---
nid: 2616
title: "A brief history of SSH and remote access"
slug: "brief-history-ssh-and-remote-access"
date: 2014-04-15T13:24:41+00:00
drupal:
  nid: 2616
  path: /blog/brief-history-ssh-and-remote-access
  body_format: full_html
  redirects: []
tags:
  - ansible for devops
  - linux
  - remote access
  - security
  - shell
  - ssh
aliases:
  - /blog/brief-history-ssh-and-remote-access
---

<blockquote><p>This post is an excerpt from Chapter 11: <em>Server Security and Ansible</em>, in <a href="http://www.ansiblefordevops.com/">Ansible for DevOps</a>.</blockquote>

<p>In the beginning, computers were the size of large conference rooms. A punch card reader would merrily accept pieces of paper that instructed the computer to do something, and then a printer would etch the results into another piece of paper. Thousands of mechanical parts worked harmoniously (when they <em>did</em> work) to compute relatively simple commands.</p>

<p>As time progressed, computers became somewhat smaller, and interactive terminals became more user-friendly, but they were still wired directly into the computer being used. Mainframes came to the fore in the 1960s, originally used via typewriter and teletype interfaces, then via keyboards and small text displays. As networked computing became more mainstream in the 1970s and 1980s, remote terminal access was used to interact with the large central computers.</p>

<p>The first remote terminal interfaces assumed a high level of trust between the central computer and all those on the network, because the small, centralized networks used were physically isolated from one another.</p>

<h2>
<a name="user-content-telnet" class="anchor" href="#telnet"><span class="octicon octicon-link"></span></a>Telnet</h2>

<p>In the late 1960s, the Telnet protocol was defined and started being used over TCP networks (normally on port 23) for remote control over larger private networks, and eventually the public Internet.</p>

<p>Telnet's underlying technology (a text-based protocol to transfer data between different systems) was the basis for many foundational communications protocols in use today, including HTTP, FTP, and POP3. However, plain text streams are not secure, and even with the addition of TLS and SASL, Telnet was never very secure by default. With the advent of SSH (which we'll get to in a bit), the protocol has declined in popularity for most remote administration purposes.</p>

<p>Telnet still has uses like configuring devices over local serial connections, or checking if a particular service is operating correctly on a remote server (like an HTTP server on port 80, mysql on port 3306, or munin on port 4949), but it is not installed by default on modern Linux distributions.</p>

<blockquote>
Plain text communications over a network are only as secure as the network's weakest link. In the early days of computer networking, networks were usually isolated to a specific company or educational institution, so transmitting things like passwords or secrets in plain text using the TCP protocol wasn't such a bad idea. Every part of the network (cabling, switches, and routers) was contained inside a secured physical perimeter. When connections started moving to the public Internet, this changed.

TCP packets can be intercepted over the Internet, at any point between the client and server, and these packets can easily be read if not encrypted. Therefore, plain text protocols are highly insecure, and should never be used to transmit sensitive information or system control data. Even on highly secure networks with properly-configured firewalls, it's a bad idea to use insecure communication methods like plain text rlogin and telnet connections for authentication and remote control.

Try running <code>traceroute google.com</code> in your terminal. Look at each of the hops between you and Google's CDN. Do you know who controls each of the devices between your computer and Google? Do you trust these operators with all of your personal or corporate secrets? Probably not. Each of these connection points—and each network device and cable connecting them—is a weak point exposing you to a man-in-the-middle attack. Strong encryption is needed between your computer and the destination if you want to ensure data security.
</blockquote>

<h2>
<a name="user-content-rlogin-rsh-and-rcp" class="anchor" href="#rlogin-rsh-and-rcp"><span class="octicon octicon-link"></span></a>rlogin, rsh and rcp</h2>

<p><code>rlogin</code> was introduced in BSD 4.2 in 1983, and has been distributed with many UNIX-like systems alongside Telnet until recently. rlogin was used widely during the 80s and much of the 90s.</p>

<p>Just like Telnet, a user could log into the remote system with a password, but rlogin additionally allowed automatic (passwordless) logins for users on trusted remote computers. rlogin also worked better than telnet for remote administration, as it worked correctly with certain characters and commands where telnet required extra translation.</p>

<p>However, like Telnet, rlogin still used plain text communications over TCP port 513 by default. On top of that, rlogin also didn't have many safeguards against clients spoofing their true identities. Some of rlogin's intrinsic flaws were highlighted in a 1998 report by Carnegie Mellon, <a href="http://resources.sei.cmu.edu/asset_files/TechnicalReport/1998_005_001_16670.pdf">rlogin: The Untold Story</a>.</p>

<p><code>rsh</code> ("remote shell") is a command line program used alongside rlogin to execute individual shell commands remotely, and <code>rcp</code> ("remote copy") is used for remote file copies. <code>rsh</code> and <code>rcp</code> inherited the same security problems as rlogin, since they use the same connection method (over different ports).</p>

<h2>
<a name="user-content-ssh" class="anchor" href="#ssh"><span class="octicon octicon-link"></span></a>SSH</h2>

<p>Secure Shell was created in 1995 by Finland native Tatu Ylönen, in response to a <a href="http://en.wikipedia.org/wiki/Secure_Shell#Version_1.x">password-sniffing attack</a> at his university. Seeing the flaws in plain text communication for secure information, Tatu created Secure Shell/SSH with a strong emphasis on encryption and security.</p>

<p>His version of SSH was developed for a few years as freeware with liberal licensing, but as his <a href="http://www.ssh.com/">SSH Communications Security Corporation</a> began limiting the license and commercializing SSH, alternative forks began to gain in popularity. The most popular fork, OSSH, by Swedish programmer Bjoern Groenvall, was chosen as a starting point by some developers from the OpenBSD project.</p>

<p>OpenBSD was (and still is!) a highly secure, free version of BSD UNIX, and the project's developers needed a secure remote communication protocol, so a few project members worked to <a href="http://www.openbsd.org/openssh/history.html">clean up and improve OSSH</a> so it could be included in OpenBSD's 2.6 release in December 1999. From there, it was quickly ported and adopted for all major versions of Linux, and is now ubiquitous in the world of POSIX-compliant operating systems.</p>

<p>How does SSH work, and what makes it better than telnet or rlogin? It starts with the basic connection. SSH connection encryption works similarly to SSL for secure HTTP connections, but it's authentication layer adds more security:</p>

<ol>
<li>When you enter <code>ssh user@example.host</code> to connect to the <code>example.host</code> server as <code>user</code>, your client and the host exchange keys.</li>
<li>If you're connecting to a host the first time, or if the host's key has changed since last time you connected (this happens often when connecting via DNS rather than directly by IP), SSH will prompt you for your approval of the host key.</li>
<li>If you have a private key in your <code>~/.ssh</code> folder that matches one of the keys in <code>~/.ssh/authorized_keys</code> on the remote system, the connection will continue to step 4. Otherwise, if password authentication is allowed, SSH will prompt you for your password. There are other authentication methods as well, such as Kerberos, but they are less common and not covered in this book.</li>
<li>The transferred key is used to create a session key that's used for the remainder of the connection, encrypting all communication with a cipher such as AES, 3DES, Blowfish or RC4 ('arcfour').</li>
<li>The connection remains encrypted and persists until you exit out of the remote connection (in the case of an interactive session), or until the operation being performed (an <code>scp</code> or <code>sftp</code> file transfer, for example) is complete.</li>
</ol><p>SSH uses encrypted keys to identify the client and host (which adds a layer of security over <code>telnet</code> and <code>rlogin</code>'s defaults), and then sets up a per-session encrypted channel for further communication. This same connection method is used for interactive <code>ssh</code> sessions, as well as for services like:</p>

<ul>
<li>
<code>scp</code> (secure copy), SSH's counterpart to rlogin's <code>rcp</code>.</li>
<li>
<code>sftp</code> (secure FTP), SSH's client/server file transfer protocol.</li>
<li>SSH port forwarding (so you can run services securely over remote servers).</li>
<li>SSH X11 forwarding (so you can use X windows securely).</li>
</ul><p>(A full list of features is available on OpenBSD's site: <a href="http://www.openbsd.org/openssh/features.html">OpenSSH Features</a>).</p>

<p>The full suite of SSH packages also includes helpful utilities like <code>ssh-keygen</code>, which generates public/private key pairs suitable for use when connecting via SSH. You can also install the utility <code>ssh-copy-id</code>, which speeds up the process of manually adding your identity file to a remote server.</p>

<p>SSH is fairly secure by default—certainly more so than telnet or rlogin's default configuration—but for even greater security, there are a few extra settings you should use (all of these settings are configured in <code>/etc/ssh/sshd_config</code>, and require a restart of the <code>sshd</code> service to take effect):</p>

<ol>
<li>
<strong>Disable password-based SSH authentication.</strong> Even though passwords are not sent in the clear, disabling password-based authentication makes it impossible for brute-force password attacks to even be <em>attempted</em>, even if you have the additional (and recommended) layer of something like Fail2Ban running. Set <code>PasswordAuthentication no</code> in the configuration.</li>
<li>
<strong>Disable root account remote login.</strong> You shouldn't log in as the root user regardless (use <code>sudo</code> instead), but to reinforce this good habit, disable remote root user account login by setting <code>PermitRootLogin no</code> in the configuration. If you need to perform actions as root, either use <code>sudo</code> (preferred), or if it's absolutely necessary to work interactively as root, login with a normal account, then <code>su</code> to the root account.</li>
<li>
<strong>Explicitly allow/deny SSH for users.</strong> You can enable or disable SSH access for particular users on your system with <code>AllowUsers</code> and <code>DenyUsers</code>. To allow only 'John' to log in, the rule would be <code>AllowUsers John</code>. To allow any user <em>except</em> John to log in, the rule would be <code>DenyUsers John</code>.</li>
<li>
<strong>Use a non-standard port.</strong> You can change the default SSH port from 22 to something more obscure, like 2849, and prevent thousands of 'script kiddie' attacks that simply look for servers responding on port 22. While security through obscurity is no substitute for actually securing SSH overall, it can provide a slight extra layer of protection. To change the port, set <code>Port [new-port-number]</code> in the configuration.</li>
</ol><p>We'll cover how Ansible can help configure some of these particular options in SSH in the next section.</p>

<h2>
<a name="user-content-the-evolution-of-ssh-and-the-future-of-remote-access" class="anchor" href="#the-evolution-of-ssh-and-the-future-of-remote-access"><span class="octicon octicon-link"></span></a>The evolution of SSH and the future of remote access</h2>

<p>It has been over a decade since OpenSSH became the <em>de facto</em> standard of remote access protocols, and in that time, Internet connectivity has changed dramatically. For reliable, low-latency LAN and Internet connections, SSH is still the king due to its simplicity, speed, and security. But in high-latency environments (think 3G or 4G mobile network connections, or satellite uplinks), using SSH can be a slow and painful experience.</p>

<p>In some circumstances, just <em>establishing a connection</em> can take some time. Additionally, once connected, the delay inherent in SSH's TCP interface (where every packet must reach its destination and be acknowledged before further input will be accepted) means entering commands or viewing progress over a high-latency connection is an exercise in frustration.</p>

<p><a href="https://www.usenix.org/system/files/conference/atc12/atc12-final32.pdf">Mosh</a>, "the mobile shell", a new alternative to SSH, uses SSH to establish an initial connection, then synchronizes the following local session with a remote session on the server via UDP.</p>

<p>Using UDP instead of TCP requires Mosh to do a little extra behind-the-scenes work to synchronize the local and remote sessions (instead of simply sending all local keystrokes over the wire serially via TCP, then waiting for stdout and stderr to be returned, like SSH).</p>

<p>Mosh also promises better UTF-8 support than SSH, and is well supported by all the major POSIX-like operating systems (and can even run inside Google Chrome!).</p>

<p>It will be interesting to see where the future leads with regard to remote terminal access, but one thing is for sure: Ansible will continue to support the most secure, fast, and reliable connection methods to help you build and manage your infrastructure!</p>

<p><em>Purchase Ansible for DevOps on <a href="https://leanpub.com/ansible-for-devops">LeanPub</a>, <a href="http://www.amazon.com/Ansible-DevOps-Server-configuration-management-ebook/dp/B016G55NOU/">Amazon</a>, or <a href="https://itunes.apple.com/us/book/ansible-for-devops/id1050383787?ls=1&mt=11">iTunes</a></em>.</p>
