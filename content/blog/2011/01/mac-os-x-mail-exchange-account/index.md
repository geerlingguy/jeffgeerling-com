---
nid: 2301
title: "Mac OS X Mail - Exchange Account Stuck unless Mail Quit and Restarted?"
slug: "mac-os-x-mail-exchange-account"
date: 2011-01-26T20:20:25+00:00
drupal:
  nid: 2301
  path: /blogs/jeff-geerling/mac-os-x-mail-exchange-account
  body_format: full_html
  redirects: []
tags:
  - exchange
  - inbox
  - mac
  - mail
aliases:
  - /blogs/jeff-geerling/mac-os-x-mail-exchange-account
---

I was having this particular problem off and on when using Mac OS X Mail on my work Mac, which was set up to use our corporate exchange server, and an 'Exchange 2007' Mail account: Every so often, Mail would quit getting new messages in the inbox, and when I checked the 'Activity' window, I would get the following error:

<p style="text-align: center;">(Screenshot to be posted here)
("Opening Mailbox — Requesting Latest Information")</p>
<p style="text-align: left;">Sometimes, simply hitting the 'stop sign' would allow me to get new messages, but the problem would always crop up again. Other times, I'd pull out my Mac laptop, which was set up to use IMAP instead of Exchange (long story, details don't matter), and after syncing it up with the server, and restarting Mail on my main Mac, the problem would go away.</p>
<p style="text-align: left;">Only today, after finding <a href="http://discussions.apple.com/thread.jspa?threadID=2140011">this forum thread</a> on Apple's Discussion Forums, did I find the source of the problem:</p>
<p style="text-align: left;">Sometimes, a corrupted email (usually spam) would find its way into my inbox, and when Mail tried downloading the message, it would get hung up on it and stop getting new mail. Once I synced my IMAP account on the other computer, and the corrupted message was put into my junk mailbox or deleted, the main Mac/Exchange account worked correctly.</p>
<p style="text-align: left;">Another way to fix this is to login to the Outlook Web Access account through your corporate Exchange server, and see if there's a message in your inbox that isn't showing up on your Exchange-enabled Mail account inbox. Delete or move that message, and restart Mail, and see if it's working again.</p>
<p style="text-align: left;">Problem solved!</p>
