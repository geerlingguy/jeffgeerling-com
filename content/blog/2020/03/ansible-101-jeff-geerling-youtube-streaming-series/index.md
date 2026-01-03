---
nid: 2982
title: "Ansible 101 by Jeff Geerling - YouTube streaming series"
slug: "ansible-101-jeff-geerling-youtube-streaming-series"
date: 2020-03-22T17:52:11+00:00
drupal:
  nid: 2982
  path: /blog/2020/ansible-101-jeff-geerling-youtube-streaming-series
  body_format: markdown
  redirects:
    - /blog/2020/ansible-101-jeff-geerling-new-series-on-youtube
aliases:
  - /blog/2020/ansible-101-jeff-geerling-new-series-on-youtube
tags:
  - ansible
  - devops
  - live
  - streaming
  - tutorial
  - video
  - youtube
---

{{< figure src="./ansible-101-header.jpg" alt="Ansible 101 Header Image" width="720" height="211" class="insert-image" >}}

After the incredible response I got from [making my Ansible books free for the rest of March](/blog/2020/you-can-get-my-devops-books-free-rest-month) to help people learn new automation skills, I tried to think of some other things I could do to help developers who may be experiencing hardship during the coronavirus pandemic and market upheaval.

So I asked on Twitter:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Considering adding a weekly livestream “Ansible 101” teaching Ansible automation following the book <a href="https://t.co/jk6G0An9gb">https://t.co/jk6G0An9gb</a> — would you be interested?</p>&mdash; Jeff Geerling (@geerlingguy) <a href="https://twitter.com/geerlingguy/status/1241538147126775809?ref_src=twsrc%5Etfw">March 22, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

And immediately got a lot of positive feedback. So I kicked off a weekly 1-hour live-streaming series, "Ansible 101 with Jeff Geerling," and recorded 15 one-hour episodes, covering all of Ansible's basic usage, using examples from my book [Ansible for DevOps](https://www.ansiblefordevops.com).

Please consider [subscribing to my YouTube channel](https://www.youtube.com/c/JeffGeerling) if you like this content and want to be notified when I start a new series!

Each stream is embedded below (or you can view all the videos in this  [Ansible 101 YouTube Playlist](https://www.youtube.com/playlist?list=PL2_OBreMn7FqZkvMYt6ATmgC0KAGGJNAN)), and below the video is a list of contents or 'chapter markers' linked to that particular topic on YouTube itself. If you watch the videos on YouTube, you can navigate the video by section more easily.

- [Episode 1 - Introduction to Ansible](#e01) (March 25)
- [Episode 2 - Ad-hoc tasks and Inventory](#e02) (April 1)
- [Episode 3 - Introduction to Playbooks](#e03) (April 8)
- [Episode 4 - Your first real-world playbook](#e04) (April 15)
- [Episode 5 - Playbook handlers, environment vars, and variables](#e05) (April 22)
- [Episode 6 - Ansible Vault and Roles](#e06) (April 29)
- [Episode 7 - Ansible Galaxy, ansible-lint, and Molecule testing](#e07) (May 6)
- [Episode 8 - Testing Ansible playbooks with Molecule and GitHub Actions for CI](#e08) (May 13)
- [Episode 9 - First 5 minutes server security with Ansible](#e09) (May 20)
- [Episode 10 - Ansible Tower and AWX](#e10) (May 27)
- [Episode 11 - Dynamic Inventory and Smart Inventory](#e11) (June 3)
- [Episode 12 - Real-world Ansible Playbooks](#e12) (June 10)
- [Episode 13 - Ansible Collections and a Test Plugin](#e13) (June 17)
- [Episode 14 - Ansible and Windows](#e14) (June 24)
- [Episode 15 - FINAL episode with live Q&A](#e15) (July 1)

## <a name="e01"></a>Episode 1 - March 25 - Introduction to Ansible

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/goclfp6a2IQ" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=0s">00:00:00</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=107s">00:01:47</a> - Preface and Info about Ansible for DevOps<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=471s">00:07:51</a> - Ansible Background<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=1063s">00:17:43</a> - Installing Ansible<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=1255s">00:20:55</a> - Connecting to a Server with Ansible<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=1610s">00:26:50</a> - Using an ansible.cfg file<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=1737s">00:28:57</a> - Running ad-hoc commands<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=2016s">00:33:36</a> - Vagrant Intro<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=2724s">00:45:24</a> - First Ansible Playbook<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=3107s">00:51:47</a> - Idempotence<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=3416s">00:56:56</a> - Importance of naming tasks<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=3678s">01:01:18</a> - Chat questions answered<br>
<a href="https://www.youtube.com/watch?v=goclfp6a2IQ&amp;t=3776s">01:02:56</a> - Outtro

## <a name="e02"></a>Episode 2 - April 1 - Ad-hoc tasks and Inventory

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/7kVfqmGtDL8" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=0s">00:00:00</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=112s">00:01:52</a> - Free books for April<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=331s">00:05:31</a> - Intro to ad-hoc commands<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=600s">00:10:00</a> - Multi-VM Vagrant configuration<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=1204s">00:20:04</a> - Multi-host inventory<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=1733s">00:28:53</a> - ad-hoc orchestration<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=1876s">00:31:16</a> - Forks and parallelization<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=2234s">00:37:14</a> - Setup module<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=2792s">00:46:32</a> - Becoming root with sudo<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=3001s">00:50:01</a> - ansible-doc CLI docs<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=3313s">00:55:13</a> - Targeting inventory groups<br>
<a href="https://www.youtube.com/watch?v=7kVfqmGtDL8&amp;t=3625s">01:00:25</a> - Outtro

## <a name="e03"></a>Episode 3 - April 8 - Introduction to Playbooks

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/WNmKjtWtqIc" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=0s">00:00:00</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=265s">00:04:25</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=500s">00:08:20</a> - Multi-host ad-hoc orchestration<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=1142s">00:19:02</a> - Using different modules ad-hoc<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=1478s">00:24:38</a> - Intro to Playbooks<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=1698s">00:28:18</a> - Comparing to shell scripts<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=1955s">00:32:35</a> - Moving commands into YAML playbooks<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=2368s">00:39:28</a> - Making playbooks more Ansible-ish<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=3182s">00:53:02</a> - Running the Apache playbook<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=3384s">00:56:24</a> - Limiting playbook runs to specific servers<br>
<a href="https://www.youtube.com/watch?v=WNmKjtWtqIc&amp;t=3614s">01:00:14</a> - Outtro

## <a name="e04"></a>Episode 4 - April 15 - Your first real-world playbook

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/SLW4LX7lbvE" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=0s">00:00</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=243s">04:03</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=418s">06:58</a> - It was DNS<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=460s">07:40</a> - Ansible content site<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=552s">09:12</a> - Our first real-world playbook<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=1350s">22:30</a> - Adding handlers<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=1458s">24:18</a> - Installing Java and Solr<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=2432s">40:32</a> - Checking playbook syntax<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=2490s">41:30</a> - Running the playbook<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=2720s">45:20</a> - Testing idempotence<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=2760s">46:00</a> - Viewing the Solr Dashboard<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=2913s">48:33</a> - Cowsay quote<br>
<a href="https://www.youtube.com/watch?v=SLW4LX7lbvE&amp;t=2950s">49:10</a> - Outtro

## <a name="e05"></a>Episode 5 - April 22 - Playbook handlers, environment vars, and variables

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/HU-dkXBCPdU" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=0s">00:00</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=265s">04:25</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=478s">07:58</a> - Raspberry Pi K8s cluster<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=600s">10:00</a> - Simple Apache playbook<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=693s">11:33</a> - Playbook handlers<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=1425s">23:45</a> - Environment variables<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=2143s">35:43</a> - Dynamic variable files for multi-OS<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=2920s">48:40</a> - Ansible facts and setup module<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=3048s">50:48</a> - Registered variables<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=3296s">54:56</a> - facter and ohai<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=3385s">56:25</a> - Preview of Ansible Vault<br>
<a href="https://www.youtube.com/watch?v=HU-dkXBCPdU&amp;t=3480s">58:00</a> - Outtro

## <a name="e06"></a>Episode 6 - April 29 - Ansible Vault and Roles

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/JFweg2dUvqM" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=0s">00:00:00</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=390s">00:06:30</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=651s">00:10:51</a> - Intro to Ansible Vault<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=840s">00:14:00</a> - Encrypting a vars file with Vault<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=1075s">00:17:55</a> - Decrypt, encrypt, edit, rekey, etc.<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=1293s">00:21:33</a> - Task features - conditionals and tags<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=1554s">00:25:54</a> - Blocks<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=1625s">00:27:05</a> - Chapter 5 Cowsay<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=1646s">00:27:26</a> - Playbook organization<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=1805s">00:30:05</a> - Includes and imports<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=2113s">00:35:13</a> - Caution about dynamic tasks<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=2238s">00:37:18</a> - Playbook includes<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=2380s">00:39:40</a> - Node.js playbook example<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=2766s">00:46:06</a> - Roles<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=3087s">00:51:27</a> - Options for including Roles<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=3150s">00:52:30</a> - Real-world flexible role usage<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=3633s">01:00:33</a> - The Golden Hammer<br>
<a href="https://www.youtube.com/watch?v=JFweg2dUvqM&amp;t=3672s">01:01:12</a> - Outtro

## <a name="e07"></a>Episode 7 - May 6 - Ansible Galaxy, ansible-lint, and Molecule testing

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/FaXVZ60o8L8" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=0s">00:00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=20s">00:00:20</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=313s">00:05:13</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=635s">00:10:35</a> - Ansible Galaxy requirements files<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=958s">00:15:58</a> - Mac development playbook<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=1037s">00:17:17</a> - A new chapter for testing<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=1155s">00:19:15</a> - The Ansible testing spectrum<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=1430s">00:23:50</a> - Testing inline in playbooks<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=1719s">00:28:39</a> - Linting with yamllint<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=2080s">00:34:40</a> - Check syntax with --syntax-check<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=2250s">00:37:30</a> - Linting with ansible-lint<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=2562s">00:42:42</a> - Introduction to Molecule<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=2843s">00:47:23</a> - Testing a role with Molecule<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=3352s">00:55:52</a> - Role dev with molecule converge<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=3555s">00:59:15</a> - Using molecule login<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=3654s">01:00:54</a> - Other molecule commands<br>
<a href="https://www.youtube.com/watch?v=FaXVZ60o8L8&amp;t=3732s">01:02:12</a> - Outtro

## <a name="e08"></a>Episode 8 - May 13 - Testing Ansible playbooks with Molecule and GitHub Actions for CI

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/CYghlf-6Opc" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=0s">00:00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=9s">00:00:09</a> - Intro and 10K subscribers!<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=354s">00:05:54</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=673s">00:11:13</a> - Ansible for DevOps 1.23<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=780s">00:13:00</a> - 60fps streaming is here<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=830s">00:13:50</a> - Molecule playbook testing<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=1174s">00:19:34</a> - Testing systemd services in Docker<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=1823s">00:30:23</a> - Testing on multiple OS distros<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=2040s">00:34:00</a> - Molecule verifiers<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=2333s">00:38:53</a> - Molecule and testinfra<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=2420s">00:40:20</a> - Linting with Molecule<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=2619s">00:43:39</a> - Playbooks in a GitHub repo<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=2737s">00:45:37</a> - GitHub Actions<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=2912s">00:48:32</a> - Molecule job in GitHub Actions<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=3273s">00:54:33</a> - Improving Molecule output in CI<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=3515s">00:58:35</a> - Demonstration of failing CI<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=3643s">01:00:43</a> - Summary of Ansible testing spectrum<br>
<a href="https://www.youtube.com/watch?v=CYghlf-6Opc&amp;t=3716s">01:01:56</a> - Outtro

## <a name="e09"></a>Episode 9 - May 20 - First 5 minutes server security with Ansible

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/gV_16dU7XjM" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=0s">00:00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=35s">00:00:35</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=266s">00:04:26</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=462s">00:07:42</a> - Linux security setup with Ansible<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=590s">00:09:50</a> - 9 Basic security measures<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=774s">00:12:54</a> - Use secure encrypted communications<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=970s">00:16:10</a> - History of SSH (rlogin, telnet)<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=1178s">00:19:38</a> - Securing SSH<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=1430s">00:23:50</a> - Ansible SSH security playbook<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=2249s">00:37:29</a> - Managing users and sudoers<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=2620s">00:43:40</a> - Remove unused apps<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=2769s">00:46:09</a> - Principle of least privilege<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=2850s">00:47:30</a> - POSIX file permissions<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=3060s">00:51:00</a> - Automatic updates with Ansible<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=3299s">00:54:59</a> - Configuring a firewall with Ansible<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=3580s">00:59:40</a> - Oops - locked myself out<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=3637s">01:00:37</a> - Security role on Galaxy<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=3712s">01:01:52</a> - Other security concerns<br>
<a href="https://www.youtube.com/watch?v=gV_16dU7XjM&amp;t=3796s">01:03:16</a> - Outtro

## <a name="e10"></a>Episode 10 - May 27 - Ansible Tower and AWX

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/iKmY4jEiy_A" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=0s">00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=35s">00:35</a> - Spaaaaaace!<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=209s">03:29</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=291s">04:51</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=673s">11:13</a> - Intro to Tower and AWX<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=900s">15:00</a> - How to install Tower or AWX<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=1288s">21:28</a> - Running the Demo Job Template<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=1339s">22:19</a> - Adding a playbook to Tower<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=1670s">27:50</a> - Using Galaxy roles and collections<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=1798s">29:58</a> - Add a credential to Tower<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=2001s">33:21</a> - Add an inventory to Tower<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=2175s">36:15</a> - Add a git project to Tower<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=2303s">38:23</a> - Add a job template to Tower<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=2461s">41:01</a> - Using Galaxy requirements in Tower<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=2660s">44:20</a> - Failure to launch<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=3052s">50:52</a> - Tower Dashboard and other parts<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=3291s">54:51</a> - Jenkins section in book<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=3388s">56:28</a> - Outtro<br>
<a href="https://www.youtube.com/watch?v=iKmY4jEiy_A&amp;t=3534s">58:54</a> - Someone fell upstairs

## <a name="e11"></a>Episode 11 - June 3 - Dynamic Inventory and Smart Inventory

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/_rDzMYp-fBs" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=0s">00:00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=22s">00:00:22</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=540s">00:09:00</a> - What broke last episode?<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=684s">00:11:24</a> - Questions from last episode<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=1200s">00:20:00</a> - Inventory group_vars and host_vars<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=1472s">00:24:32</a> - Building dynamic inventory in PHP<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=1607s">00:26:47</a> - Use ansible-inventory CLI<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=2024s">00:33:44</a> - Python dynamic inventory example<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=2310s">00:38:30</a> - Using inventory plugins<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=2464s">00:41:04</a> - AWS inventory plugin demo<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=2912s">00:48:32</a> - Dynamic inventory in Ansible Tower<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=3320s">00:55:20</a> - More advanced inventory examples<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=3538s">00:58:58</a> - Answering live chat questions<br>
<a href="https://www.youtube.com/watch?v=_rDzMYp-fBs&amp;t=3726s">01:02:06</a> - Outtro

## <a name="e12"></a>Episode 12 - June 10 - Real-world Ansible Playbooks

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/_QZr4xKhir4" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=0s">00:00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=29s">00:00:29</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=423s">00:07:03</a> - Questions from previous episode<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=895s">00:14:55</a> - My real-world LAMP playbooks<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=1569s">00:26:09</a> - Complexity vs Simplicity<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=1704s">00:28:24</a> - Deploying Apps behind Load Balancer<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=2415s">00:40:15</a> - Capistrano and Ansistrano deployments<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=2585s">00:43:05</a> - Multi-server zero-downtime deployments<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=3198s">00:53:18</a> - Serial and max fail percentage<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=3286s">00:54:46</a> - A word on dependencies<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=3386s">00:56:26</a> - Introducing Collections<br>
<a href="https://www.youtube.com/watch?v=_QZr4xKhir4&amp;t=3420s">00:57:00</a> - Outtro

## <a name="e13"></a>Episode 13 - June 17 - Ansible Collections and a Test Plugin

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/nyXDR4RG4A8" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=0s">00:00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=28s">00:00:28</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=172s">00:02:52</a> - Questions from previous episode<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=503s">00:08:23</a> - Intro Collections and new chapter<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=582s">00:09:42</a> - History of Ansible Collections<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=1201s">00:20:01</a> - Creating a Test Plugin with Python<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=2233s">00:37:13</a> - Creating a collection<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=2506s">00:41:46</a> - Moving our plugin into the collection<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=2580s">00:43:00</a> - Using the FQCN<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=2797s">00:46:37</a> - Collections on Ansible Galaxy<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=2888s">00:48:08</a> - Installing collections from Galaxy<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=3175s">00:52:55</a> - Other Collection features<br>
<a href="https://www.youtube.com/watch?v=nyXDR4RG4A8&amp;t=3650s">01:00:50</a> - Outtro

## <a name="e14"></a>Episode 14 - June 24 - Ansible and Windows

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/N7tgLVCXup4" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=0s">00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=20s">00:20</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=218s">03:38</a> - Jeff's Windows Background<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=392s">06:32</a> - Windows Update<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=450s">07:30</a> - Install WSL2 and Ansible<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=1033s">17:13</a> - Vagrant and Ansible with WSL2<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=1965s">32:45</a> - Manage Windows with Ansible<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=2034s">33:54</a> - Set up OpenSSH on Windows<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=2438s">40:38</a> - Talking to myself<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=2461s">41:01</a> - Ansible Windows Modules<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=2747s">45:47</a> - Ansible Windows Collection<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=2994s">49:54</a> - Ansible 101 series discussion<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=3143s">52:23</a> - Call for questions for final episode<br>
<a href="https://www.youtube.com/watch?v=N7tgLVCXup4&amp;t=3384s">56:24</a> - Outtro

## <a name="e15"></a>Episode 15 - July 1 - FINAL episode with live Q&A

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/sb5XYD3BLMA" frameborder='0' allowfullscreen></iframe></div>

### Contents

<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=0s">00:00:00</a> - Start<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=8s">00:00:08</a> - Intro<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=286s">00:04:46</a> - Ansible 101 retrospective<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1020s">00:17:00</a> - Ansible best practices<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1180s">00:19:40</a> - Bootstrapping computers with Ansible<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1368s">00:22:48</a> - Ansible for Kubernetes<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1496s">00:24:56</a> - Where to store variables<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1604s">00:26:44</a> - Running Ansible in CI/CD and Docker<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1754s">00:29:14</a> - Monorepo vs many repos for automation<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=1888s">00:31:28</a> - Organizing tasks for apps vs implementations<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2031s">00:33:51</a> - SSH forwarding or proxying in VMware<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2138s">00:35:38</a> - Managing isolated servers in DMZ<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2188s">00:36:28</a> - Writing tasks based on facts<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2410s">00:40:10</a> - Installing AWX in Kubernetes<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2570s">00:42:50</a> - When shouldn't Ansible be used<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2705s">00:45:05</a> - WinRM through multiple Linux bastions<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2751s">00:45:51</a> - Multi-host Molecule testing<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2904s">00:48:24</a> - Managing SSH users and keys<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=2983s">00:49:43</a> - Running roles on specific hosts<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3156s">00:52:36</a> - Organizing playbooks - blocks, tags, environments<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3323s">00:55:23</a> - Visualizing Ansible playbooks<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3511s">00:58:31</a> - Connecting through multiple SSH bastions<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3572s">00:59:32</a> - Templating filenames with Jinja<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3644s">01:00:44</a> - Better output for debugging<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3755s">01:02:35</a> - Jeff's pivot from PHP to Python, Ansible, K8s<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3905s">01:05:05</a> - Contributing to Ansible<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=3991s">01:06:31</a> - AWX or Tower on a Raspberry Pi 4<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4160s">01:09:20</a> - Ansible with GitLab CI<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4303s">01:11:43</a> - Using 'block' in playbooks<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4357s">01:12:37</a> - Building Ansible modules<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4473s">01:14:33</a> - Book giveaway<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4568s">01:16:08</a> - What's next?<br>
<a href="https://www.youtube.com/watch?v=sb5XYD3BLMA&amp;t=4712s">01:18:32</a> - Outtro
