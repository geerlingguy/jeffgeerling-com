---
nid: 3166
title: "SSH and HTTP to a Raspberry Pi behind CG-NAT"
slug: "ssh-and-http-raspberry-pi-behind-cg-nat"
date: 2022-01-12T21:22:27+00:00
drupal:
  nid: 3166
  path: /blog/2022/ssh-and-http-raspberry-pi-behind-cg-nat
  body_format: markdown
  redirects:
    - /blog/2022/ssh-raspberry-pi-behind-cg-nat-reverse-tunnel
aliases:
  - /blog/2022/ssh-raspberry-pi-behind-cg-nat-reverse-tunnel
tags:
  - raspberry pi
  - remote access
  - remote connection
  - server
  - ssh
  - tunnel
---

For a project I'm working on, I'll have a Raspberry Pi sitting behind a 4G LTE modem:

{{< figure src="./raspberry-pi-4--quectel-4g-lte-modem-pulse-antenna.jpeg" alt="Raspberry Pi 4 with 4G LTE modem and antenna on desk" width="455" height="348" class="insert-image" >}}

This modem is on AT&T's network, but regardless of the provider, unless you're willing to pay hundreds or thousands of dollars a month for a SIM with a public IP address, the Internet connection will be running behind [CG-NAT](https://en.wikipedia.org/wiki/Carrier-grade_NAT).

What this means is there's no publicly routable address for the Pi—you can't access it from the public Internet, since it's only visible inside the cell network's private network.

There are a few different ways people have traditionally dealt with accessing devices running through CG-NAT connections:

  1. Using a VPN
  2. Using a one-off tool like ngrok
  3. Using reverse tunnels, often via SSH

And after weighing the pros and cons, I decided to go with option 3, since—for my needs—I want to have two ports open back to the Raspberry Pi:

  - Port 22, for SSH access
  - Port 80, so I can serve HTTP traffic

> **Security Warning**: Punching a hole through to any network—especially to expose something like a Raspberry Pi to the public Internet, increases your network's attack surface. You're responsible for your own security, and if you don't have a good grasp on fundamental Linux and SSH security, you might not want to do this.

## Prepare a VPS as a Tunnel Server

Paid services like VPNs and ngrok run their own servers, but can cost upwards of $10-20/month if you want to run a lot of traffic through them. Sometimes they are easier for specific needs, but as I mentioned, I just wanted two open ports.

So I chose to use one of my existing DigitalOcean VPSes for the task. I pay $5/month for it, use it to host some websites, and it also gets assigned a static public IP address, so I can point a domain at it, like `www.jeffgeerling.com`.

On that VPS, I needed to configure SSH so it could work as a tunnel server:

SSH's `AllowTCPForwarding` option must be set to `yes` for this to work—and that's the default. But you can confirm this with `sshd -T`.

You will need to configure the `GatewayPorts` option, so edit the SSH config file:

```
$ sudo nano /etc/ssh/sshd_config
```

And add the following line at the bottom:

```
GatewayPorts yes
```

Save your changes, and restart SSH:

```
$ sudo systemctl restart ssh
```

Confirm both settings are `yes` with:

```
$ sshd -T | grep -E 'gatewayports|allowtcpforwarding'
gatewayports yes
allowtcpforwarding yes
```

> **Security Warning**: For better security, you can set `GatewayPorts clientspecified`, and then [specify certain IP addresses allowed to connect](https://www.ssh.com/academy/ssh/tunneling/example#remote-forwarding). Or, you could restrict access to `localhost` by setting `GatewayPorts no`—that way only users who are logged into the tunnel server could access the Raspberry Pi via SSH.

## Prepare the Raspberry Pi

The Raspberry Pi will need to be able to connect to the VPS via SSH, so you should [create an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for this purpose. On the Raspberry Pi, run:

```
$ ssh-keygen -t ed25519 -C "my-raspberry-pi-name"
```

Then press enter for all the prompts. This should create a public SSH key located at `/home/pi/.ssh/id_ed25519.pub`. Get the contents of that file by copying the output of:

```
$ cat /home/pi/.ssh/id_ed25519.pub
```

Now, log into your tunnel VPS, edit the `~/.ssh/authorized_keys` file, paste the public key you just copied into a new line, and save that file.

At this point, you should be able to SSH into the VPS from your Raspberry Pi. Test it with:

```
$ ssh my-username@my-vps-hostname-or-ip
```

You'll be prompted to accept the host key, so type `yes` when prompted, and you should be logged in. Go ahead and log back out (type `exit`).

## Set up the tunnel

Now, it's time to test if tunneling works. First, on the Raspberry Pi, run this command to configure a tunnel over the IPv4 interface between port 22 on the Pi to port 2222 on the VPS:

```
$ ssh -nNTv -R 0.0.0.0:2222:localhost:22 my-username@my-vps-hostname-or-ip
```

This will output a bunch of debug information, and eventually show:

```
...
debug1: Entering interactive session.
debug1: pledge: network
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: remote forward success for: listen 0.0.0.0:2222, connect localhost:22
```

Leave that terminal session running, and in another, log into the VPS and test logging into the Pi from _it_:

```
$ ssh -p 2222 pi@localhost
```

If you have password login disabled like I do, you might get a prompt like:

```
pi@localhost: Permission denied (publickey).
```

But that's okay—the important thing is you should see more `debug` messages in the Pi's terminal—if you do, that means the port forwarding is working.

Now, for the big test: check if you can SSH directly into the Raspberry Pi from your own workstation (not logged into the VPS) _through the VPS tunnel_:

```
$ ssh -p 2222 pi@my-vps-hostname-or-ip
```

And bingo! You should be in. But if not...

## Troubleshooting

There are a few things that could be going wrong:

  - Check SSH's current configuration with `sshd -T | grep -E 'gatewayports|allowtcpforwarding'` — make sure the two settings configured correctly. If the sshd config file is correct, make sure you restart SSH to make the changes take effect (`sudo systemctl restart ssh`).
  - If you have a firewall configured on the server (`iptables`, `nftables`, `ufw`, or `firewalld`), make sure the ports are open through which you're connecting!
  - Triple check open connections with `netstat -tulpn` — in one case, I hadn't set `GatewayPorts` correctly, so when I ran that command, I saw a listing for `127.0.0.1:2222`, meaning the forwarded port was only accessible if logged directly into the VPS. It should be showing as `0.0.0.0:2222` if you set up everything according to this guide.

## Better persistence

This is great if you just want to connect through to the Pi once, but if you want a persistent connection resilient to network dropouts, you will need to run something like `autossh`.

It's easiest to install it via `apt`:

```
$ sudo apt install autossh
```

`autossh` doesn't come with any automatic service integration, so you need to create a systemd unit file and defaults manually.

### autossh defaults

Create a file to store autossh defaults, with `sudo nano /etc/default/autossh`, and put the following inside:

```
AUTOSSH_POLL=60
AUTOSSH_FIRST_POLL=30
AUTOSSH_GATETIME=0
AUTOSSH_PORT=22000
SSH_OPTIONS="-N -R 2222:localhost:22 my-username@my-vps-hostname-or-ip"
```

> Note: You can add multiple ports in the `SSH_OPTIONS` line—just add in an additional `-R`, like `-R 8080:localhost:80` after the first port 22 statement, and you'll be sharing the local HTTP port over the remote server's port `8080`.

### autossh systemd unit file

Create a file to tell systemd about autossh, with `sudo nano /lib/systemd/system/autossh.service`, and put the following inside:

```
[Unit]
Description=autossh
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=pi
EnvironmentFile=/etc/default/autossh
ExecStart=/usr/bin/autossh $SSH_OPTIONS
Restart=always
RestartSec=60

[Install]
WantedBy=multi-user.target
```

Save that file, then symlink it into place so systemd can discover it:

```
$ sudo ln -s /lib/systemd/system/autossh.service /etc/systemd/system/autossh.service
```

### Starting autossh

All that's left is discovering the new systemd unit, and starting the service:

```
$ sudo systemctl daemon-reload
$ sudo systemctl start autossh
```

If everything's working (you can log in from your own workstation through the VPS tunnel server), you can set autossh to run at system boot:

```
$ sudo systemctl enable autossh
```

If you have any problems, run `journalctl -u autossh` to view the logs.

## Conclusion

There are myriad ways of making a Pi accessible through CG-NAT, including VPN solutions like Wireguard (e.g. with Pi-VPN), Tailscale, Zerotier, etc.—however, if you already have a VPS running somewhere, and know SSH pretty well, SSH tunnels are a nice, simple, secure solution, at least for small scale deployments.

You may also not need `autossh` at all—later versions of OpenSSH include some of the features of `autossh` built-in, and you could just use `ssh` + systemd to keep a connection alive. For more on that, see these two posts:

  - [Setting up a Pi for remote Internet connection monitoring](/blog/2021/setting-pi-remote-internet-connection-monitoring)
  - [Create a reverse SSH tunnel for remote access to a restricted Linux machine](https://dev.to/bulletmark/create-a-reverse-ssh-tunnel-for-remote-access-to-a-restricted-machine-1ma0)
