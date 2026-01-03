---
nid: 2375
title: "Force-Sleep the Display on a 2010-2011 MacBook Air"
slug: "force-sleep-display-2010-2011"
date: 2011-10-07T06:04:19+00:00
drupal:
  nid: 2375
  path: /blogs/jeff-geerling/force-sleep-display-2010-2011
  body_format: full_html
  redirects: []
tags:
  - apps
  - display
  - keyboard shortcuts
  - mac
  - macbook air
  - sleep
---

[<strong>Update</strong>: It looks like Mountain Lion finally restored this functionality—you can press Shift + Control + Power key, and the screen will immediately go to sleep.]

The 2010/2011 MacBook Air models are all amazing, and I believe Apple will eventually convert all their Mac laptops to the same basic design (just different sizes), forgoing the optical drives.

The only downside to this new design is the lack of an eject key—of course, most people probably only knew the key could eject discs, so it's no big loss for them. I, however, use that key in a standard Shift + Control + Eject combination to instantly turn off my Mac's display to conserve power and prevent any pixel ghosting. I've used the combo for a few years, and it took me some time to find out a way to reliably do something similar on my new 11" MacBook Air.

There are a few ways you can get this functionality back:

<ol>
	<li><strong>Assign a Hot Corner</strong>: Open the Mission Control System Preference, click on 'Hot Corners...' and assign 'Put Display to Sleep' to one of the corners.</li>
	<li><strong>Use the Sleep Display Dockable App</strong>: <a href="http://getdockables.com/">Dockables</a>&nbsp;are little apps you can throw in your Dock, or open on your own (either using a keyboard shortcut assigned with something like Quicksilver), that perform single tasks... like 'Put Display to Sleep'.</li>
	<li><strong>Reassign the Eject Key</strong>: Use <a href="http://pqrs.org/macosx/keyremap4macbook/">KeyRemap4MacBook</a>&nbsp;and assign something like the F12 key to the Eject key (check 'F12 to Eject' under the 'Change F1..F19 Key' heading.</li>
</ol>

And there you have it! I'm currently using method #3, with the new key command Shift + Fn + Control + F12, and I'm happy with it. I just wish Apple had exposed a keyboard-shortcuttable command, or at least a shell-scriptable command that I could run in the terminal. Having to install more software on my Mac to get back this shortcut is an annoyance.
