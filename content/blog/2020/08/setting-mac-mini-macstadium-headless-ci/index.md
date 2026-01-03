---
nid: 3033
title: "Setting up a Mac mini from MacStadium for headless CI"
slug: "setting-mac-mini-macstadium-headless-ci"
date: 2020-08-17T22:37:05+00:00
drupal:
  nid: 3033
  path: /blog/2020/setting-mac-mini-macstadium-headless-ci
  body_format: markdown
  redirects:
    - /blog/2020/setting-mac-mini-macstadium-ci
aliases:
  - /blog/2020/setting-mac-mini-macstadium-ci
tags:
  - ansible
  - mac
  - macos
  - macstadium
  - screen sharing
  - ssh
  - vnc
---

I recently got an offer from [MacStadium](https://www.macstadium.com) to use one of their dedicated Mac minis to perform CI and testing tasks for my Mac-based open source projects (for example, my [Mac Dev Ansible Playbook](https://github.com/geerlingguy/mac-dev-playbook), which I use to configure my own Macs).

{{< figure src="./apple-glowy-laptop-back.jpeg" alt="Apple logo on glowy laptop background" width="600" height="400" class="insert-image" >}}

So I thought I'd document a little bit in this blog post about how I configured the Mac mini for more secure remote administration, since Macs tend to be a little more 'open' out of the box than comparable Linux machines that I'm used to working with.

## Securing SSH

First of all, I used `ssh-copy-id` to add my SSH key to the default `administrator` account on the Mac mini that was created for me:

```
$ ssh-copy-id administrator@[ip-address-here]
```

Once I could confirm I could log in with SSH successfully, I disabled password-based login, since that's an easy attack vector for scripts looking to hack into my servers:

```
# While logged into the Mac mini...
$ sudo nano /etc/ssh/sshd_config

# Make the following changes to the file:
PermitRootLogin no
PasswordAuthentication no
```

Then restart the SSH daemon:

```
$ sudo launchctl stop com.openssh.sshd
$ sudo launchctl start com.openssh.sshd
```

## Disable the Login Screen Screen Saver

While logged in via SSH, it's also a good idea to disable the built-in screensaver, since there's no monitor plugged in that needs any burn-in protection. It also adds a little load to the Mac mini since rendering a screensaver isn't free!

```
$ sudo defaults write /Library/Preferences/com.apple.screensaver loginWindowIdleTime 0
```

You can check on the status of the `loginWindowIdleTime` property with `sudo defaults read /Library/Preferences/com.apple.screensaver`.

## Disable RDP / Screen Sharing

Unless you really need it, it's a good idea to also disable Screen Sharing (which opens up VNC access over the Internet), because it's a less efficient way of administering a Mac, it requires more running services, and in general unless you _need_ it available, it's better to close off access.

It _seems_ like you'd be able to disable screen sharing with the following command:

```
$ sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart \
-deactivate -configure -access -off
```

And then re-enable with the following command:

```
$ sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart \
-activate -configure -access -on \
-clientopts -setvnclegacy -vnclegacy yes \
-clientopts -setvncpw -vncpw mypasswd \
-restart -agent -privs -all
```

[Original source](https://apple.stackexchange.com/a/30239/17366).

_However_, it seems that the way the Mac is set up for remote management, the 'Screen Sharing' feature is kind of locked out from changes via SSH. Even if I log in via screen share and try to disable it, I see the message "Screen Sharing is currently being controlled by the Remote Management service."

{{< figure src="./mac-mini-macstadium-remote-management-screen-sharing.png" alt="Mac mini remote management and screen sharing preferences" width="546" height="449" class="insert-image" >}}

To be honest, I'd rather not tamper too much here, since I could end up locking myself out of this Mac via anything but SSH entirely—I _might_ be able to turn off Remote Management, then separately enable or disable Screen Sharing, but I fear I'd just make it so I could never use Screen Sharing again! (Any real-world experience here?)

## Other configuration

Well, at this point, you're on your own. But might I interest you in this wonderful little tool I use called [Ansible](https://github.com/ansible/ansible)? I like it so much I even wrote a book on it, [Ansible for DevOps](https://www.ansiblefordevops.com), and I use it to [install software on and configure my own Macs](https://github.com/geerlingguy/mac-dev-playbook).

There are a few other things that I normally configure on my Linux servers that I'd like to automate on this public Mac server, but for now it looks like I need to do it in the GUI, like:

  - Enabling Automatic Updates (System Preferences > Software Update > 'Automatically keep my Mac up to date')
  - Configuring some form of fail2ban equivalent on macOS (is there anything like it?)

Overall, I tend to stick with Linux servers for most anything facing the public Internet, for a number of reasons (not the least of which is extreme ease in remote management via SSH). But there are a few things that require Macs, like macOS software CI (apps for macOS, iOS, ipadOS, watchOS, or tvOS), and certain apps that run best (or only) on Macs.

Also—especially if you're shipping your _own_ Mac mini to them—check out [MacStadium's Colocation Configuration Guide](https://www.macstadium.com/colo/configuration-guide).
