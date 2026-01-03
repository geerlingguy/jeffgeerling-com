---
nid: 2411
title: "Supercharge your Key Repeat rates in Mac OS X Lion"
slug: "supercharge-your-key-repeat"
date: 2011-10-08T15:07:35+00:00
drupal:
  nid: 2411
  path: /blogs/jeff-geerling/supercharge-your-key-repeat
  body_format: filtered_html
  redirects: []
tags:
  - keyboard
  - lion
  - mac
  - typing
---

As an ardent keyboard-only user of Mac OS X (mice are so early 90s!), I like having a very fast key repeat rate, allowing me to hold the delete key to remove characters, command-z to undo a bunch of things in my text editor, etc.

Since I have a MacBook Air without an Eject key, I had to use <a href="http://pqrs.org/macosx/keyremap4macbook/">KeyRemap4MacBook</a> to switch the F12 key to behave like the Eject key for the purpose of <a href="http://www.jeffgeerling.com/blogs/jeff-geerling/force-sleep-display-2010-2011">turning off the screen with the keyboard</a>.

This gives me another nice feature, too: the ability to have extremely fine-grained control over key repeat rates. After installing KeyRemap4MacBook, you can click on it&#8217;s &#8216;Key Repeat&#8217; tab in the System Preference pane, and set your own values (in ms) for waits.

I simply set the &#8216;Initial Wait&#8217; to 200ms, and the &#8216;Wait&#8217; to 25ms. These values let me type, delete, and undo things very fast. That&#8217;s sooooooooooooooo spiffy ;-)

Note: You may also need to <a href="http://www.karthikk.net/2011/08/how-to-enable-key-repeat-in-mac-os-x-lion/">enable key repeats</a> (rather than hold-to-popup accents) for Lion before key repeats work normally.

Another alternative, if you don't want to install an extra bit of software, is to edit the values directly using the Terminal (see <a href="http://apple.stackexchange.com/a/83923">this answer</a> for details):

```
defaults write -g InitialKeyRepeat -int 10 # normal minimum is 15 (225 ms)
defaults write -g KeyRepeat -int 1 # normal minimum is 2 (30 ms)
```

