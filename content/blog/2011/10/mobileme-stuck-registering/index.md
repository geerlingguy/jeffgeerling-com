---
nid: 2334
title: "MobileMe Stuck on 'Registering Computer...'? Try this"
slug: "mobileme-stuck-registering"
date: 2011-10-07T03:47:06+00:00
drupal:
  nid: 2334
  path: /blogs/jeff-geerling/mobileme-stuck-registering
  body_format: full_html
  redirects: []
tags:
  - apple
  - mac
  - macbook air
  - mobileme
---

I was having tons of trouble getting my brand new 11" MacBook Air to get MobileMe Sync set up, and it kept getting stuck with 'Registering computer...' either when I checked the 'Synchronize with MobileMe' checkbox or when I clicked 'Advanced...' and then 'Register Computer'.

Since I've subscribed to iTools, then .Mac, and now MobileMe (soon iCloud) since 2000, I figured this may have something to do with the fact that, after all these years, my default AppleID would change to @me.com (rather than @mac.com, as it has been for years).

The steps you should try before giving up are as follows:

<ol>
	<li>In the MobileMe account preference pane in System Preferences, log out (there's a button for that), then quit System Prefs, reopen it, and log back in. See if that works.</li>
	<li>Disable the mail, contacts and calendars for MobileMe if you have it enabled. Then do step 1.</li>
	<li>Click on 'Accounts' and see if any of the user accounts on the computer have an Apple ID (mine had @me.com). Edit that ID and make sure it's the same as your MobileMe login ID. Or just remove that ID (I don't know what it's for anyways...). Then restart your Mac and go back to step 1.</li>
	<li>Try <a href="http://support.apple.com/kb/ts1627">Resetting the SyncServices Folder</a>. Then restart your mac and go back to step 1.</li>
</ol>

If none of these things work, and you've searched through countless forum topics since 2007 like I have, then, well, I don't know what else to try...
