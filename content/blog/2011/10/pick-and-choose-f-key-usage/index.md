---
nid: 2337
title: "Pick and Choose F-key usage (Brightness, Sound, Dashboard, etc.) on a Mac"
slug: "pick-and-choose-f-key-usage"
date: 2011-10-25T19:42:40+00:00
drupal:
  nid: 2337
  path: /blogs/jeff-geerling/pick-and-choose-f-key-usage
  body_format: full_html
  redirects: []
tags:
  - functionflip
  - keyboard
  - keyboard shortcuts
  - mac
  - preferences
aliases:
  - /blogs/jeff-geerling/pick-and-choose-f-key-usage
---

For the longest time, I've flip-flopped on whether to check the 'Use all F1, F2, etc. keys as standard function keys' option in the Keyboard System Preference pane.

I love using the volume up and down keys on the keyboard, and probably use them fifty times a day. I sometimes like using the 'Dashboard' key too. I rarely use the media control keys. I'm undecided on the F1/F2 keys, though... I would like to use them as brightness control on my MacBook Air keyboard, but when my Air is plugged into my external monitor and keyboard, I want to use those as F1 and F2 (especially for code folding in TextMate).

Lucky for me, I found this great bit of freeware: <strong><a href="http://kevingessner.com/software/functionflip/">FunctionFlip</a></strong>.

It's a System Preference pane that lets you choose which F keys are used as standard function keys, and which ones are used for the marked purposes (brightness, volume, etc.). AND, you can even set things different depending on what keyboard you're using. Nice!
<p style="text-align: center;">{{< figure src="./functionflip.jpg" alt="" width="470" height="278" >}}</p>
For my purposes, I have things configured thusly:

<ul>
	<li>Leave the 'Use all F1, F2, etc. keys as standard function keys' in the Keyboard pane <strong>unchecked</strong></li>
	<li><strong>Check</strong> the boxes in FunctionFlip next to the functions you <strong>wouldn't</strong> like to use. In my case, I just checked the F1 box for now, since I use that for code folding. All the other keys work normally.</li>
</ul>

I could probably remap keys manually to do this stuff using <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/force-sleep-display-2010-2011">a tip I mentioned in an earlier post</a>, but FunctionFlip is so much more simple.
