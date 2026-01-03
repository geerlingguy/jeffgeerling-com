---
nid: 2451
title: "Meet Phergie, an efficient PHP IRC bot"
slug: "meet-phergie-efficient-php"
date: 2014-03-23T17:36:51+00:00
drupal:
  nid: 2451
  path: /blogs/jeff-geerling/meet-phergie-efficient-php
  body_format: full_html
  redirects: []
tags:
  - ansible
  - bot
  - drupal
  - druplicon
  - irc
  - phergie
  - php
aliases:
  - /blogs/jeff-geerling/meet-phergie-efficient-php
---

The Drupal community <a href="https://drupal.org/irc">uses IRC extensively</a> for collaboration and community building. A permanent and ever-helpful fixture of the official #drupal-* IRC channels, and in the Drupal community itself, is the humble Druplicon bot. Druplicon is a Drupal-based IRC bot that was created in 2005, and is still going strong as part of the <a href="https://drupal.org/project/bot">Bot</a> module for Drupal.

Bots like Druplicon do a lot of nice things—they can remind people of things after they were away for a while, they can store facts, track karma, throw people virtual beers, store and retrieve helpful facts, and relay important information. For example, when a build fails in Jenkins, a bot can post a message in IRC. Similarly, if a server goes down, or is under heavy load, the bot could post a message.

What if you want your own bot for a different IRC channel? Drupal's Bot requires an entire Drupal environment to run, and while the bot is not too heavy on resources, an always-connected, efficient and pluggable bot would be better off on its own. And in PHP-land, there's just such a bot. Meet <a href="http://phergie.org/">Phergie</a>, a PHP IRC Bot.

<p style="text-align: center;"><a href="http://phergie.org/">{{< figure src="./phergie-logo.jpg" alt="Phergie logo" width="254" height="63" >}}</a></p>

Phergie 2.0 (the current version) is fully-pluggable, efficient and lightweight, and is a great example of OO code for PHP (of the 5.2/5.3/5.4 era). Phergie 3.0 is under development and will be available soon, bringing even more flexibility and power... but 2.0 works great, and has many available plugins (you can write your own pretty easily, too).

I've been running Phergie on a Raspberry Pi for the past few months, and besides network connectivity issues every now and then, the bot's been reliable and speedy in responding at all times.

I've been on an Ansible kick lately (especially with all the writing I'm doing for Ansible for DevOps lately), so I decided to wrap up Phergie installation and configuration in an Ansible role, and post an example Ansible playbook that sets up an entire Linux VM with Phergie installed. You just need PHP and an active connection to the Internet, then you can start Phergie by logging into the server and running <code>php /path/to/phergie.php</code> (I also have an init script and shell script wrapper that allows me to start and stop the service more efficiently, but haven't generalized it to be included with the Ansible role yet).

Through the role's configuration, you can configure:

<ul>
<li>Which IRC channel(s) to join.</li>
<li>Which plugins to enable (Google can grab search results from Google, Http can fetch page titles and info from pasted URLs, Lart stores and retrieves word definitions, Karma tracks karma, Wunderground retrieves weather information for given locations... and <a href="https://github.com/phergie/phergie/tree/master/Phergie/Plugin">the list of plugins goes on</a>.</li>
<li>The primary and alternate nicks for the bot.</li>
</ul>

If you're interested in installing Phergie and trying it out on your own, check out the <a href="https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/phergie">Ansible Vagrant profile for Phergie</a>, part of my <a href="https://github.com/geerlingguy/ansible-vagrant-examples">Ansible Vagrant Examples</a> project.

And next time you encounter Druplicon, be sure to offer the bot a botsnack or botbeer!
