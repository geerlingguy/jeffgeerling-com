---
nid: 2635
title: "Fastest way to reset a host key when rebuilding servers on the same IP or hostname frequently"
slug: "fastest-way-reset-host-key-when-rebuilding-servers-on-same-ip-or-hostname-frequently"
date: 2016-03-17T15:30:12+00:00
drupal:
  nid: 2635
  path: /blog/2016/fastest-way-reset-host-key-when-rebuilding-servers-on-same-ip-or-hostname-frequently
  body_format: markdown
  redirects: []
tags:
  - bash
  - host keys
  - known_hosts
  - security
  - sed
  - ssh
---

I build and rebuild servers quite often, and when I want to jump into the server to check a config setting (when I'm not using Ansible, that is...), I need to log in via SSH. It's best practice to let SSH verify the host key every time you connect to make sure you're not getting MITMed or anything else is going on.

However, any time you rebuild a server from a new image/OS install, the host key should be new, and this will result in the following message the next time you try to log in:

```
 10:21 AM:~ $ ssh pi@10.0.1.18
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:9Xayf4TxnEwUCDrkJm2h9+upZV+hbx4p4Bi7gSB3tZw.
Please contact your system administrator.
Add correct host key in /Users/jeff.geerling/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /Users/jeff.geerling/.ssh/known_hosts:188
ECDSA host key for 10.0.1.18 has changed and you have requested strict checking.
Host key verification failed.
```

One fix for this, which is especially useful for local development environments or things like Raspberry Pis that you re-image frequently, is to add a configuration like the following for all hosts which you don't care about the SSH host key verification to your .ssh/config file:

```
Host 10.0.1.60 10.0.1.61 10.0.1.62 10.0.1.63 10.0.1.64
        StrictHostKeyChecking no
        UserKnownHostsFile=/dev/null
        LogLevel=error
```

(The above configuration is what I use to prevent the warning when working on my [Raspberry Pi Dramble](http://www.pidramble.com/) infrastructure.)

However, if you have live servers in the wild that you _do_ want to verify on every connection that change often, you can use one of two commands to quickly remove the offending line from your `known_hosts` file:

```
# Best for removing one line, by line number (e.g. 188), from the known_hosts file:
 10:21 AM:~ $ sed -i '' '188d' ~/.ssh/known_hosts

# Best for removing host, by hostname/ip, from the known_hosts file:
 10:21 AM:~ $ ssh-keygen -R hostname
```

(Where `188` is the line to be deleted, or `hostname` is the hostname or IP address). For non-OS X bash, remove the blank `''`.

You can even add a function to your profile (e.g. `~/.bash_profile`) so you can just enter something like `knownrm 188` to delete that line number from your known_hosts file by line number:

```
# Delete a given line number in the known_hosts file.
knownrm() {
  re='^[0-9]+$'
  if ! [[ $1 =~ $re ]] ; then
    echo "error: line number missing" >&2;
  else
    sed -i '' "$1d" ~/.ssh/known_hosts
  fi
}
```

I find it's easier/faster to type `knownrm [line-number]` than `ssh-keygen -R hostname`.
