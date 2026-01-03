---
nid: 2710
title: "Fix macOS Screen Sharing frequent pauses or freezes"
slug: "fix-macos-screen-sharing-frequent-pauses-or-freezes"
date: 2016-10-30T04:20:49+00:00
drupal:
  nid: 2710
  path: /blog/2016/fix-macos-screen-sharing-frequent-pauses-or-freezes
  body_format: markdown
  redirects: []
tags:
  - back to my mac
  - mac
  - macos
  - screen sharing
  - sierra
---

Ever since upgrading my Macs to macOS Sierra, there have been one or two times when using Screen Sharing (as part of Back to My Mac) when the session would freeze up, or intermittently pause. It seemed that every 5 or 10 seconds, there would be 10 seconds where the shared screen would stay frozen.

I could enter keystrokes, but things like pasting or clicking was hit-or-miss. This made it extremely annoying to work on one of my headless Macs (without a monitor plugged in), because I could only do work in brief spurts!

I opened up the Console app (in Applications > Utilities) to see what was happening, and quickly found that the following three errors were logged any time the screen would freeze:

    error 22:03:06.197195 -0500 sharingd  Request failed <SDActivityPayloadRequestRecord: 0x7fdac1fcc9d0, advertisementPayload:<70627579 70652321>, command:pbtypes, message/requestIdentifier:9C76A140-0B19-4CAD-8860-614ACAF1367F, deviceIdentifier:361CA780-A004-4108-8241-B741CDF4B033, requestCreated:2016-10-29 03:02:55 +0000, hasCompletionHandler:YES, _timeoutTimer:<__NSCFTimer: 0x7fdac1fa3600>, error:Error Domain=com.apple.ids.idssenderrordomain Code=12 "(null)">
    error 22:03:06.197790 -0500 useractivityd [PBOARD CONTROLLER] Type payload fetch error: <private>
    error 22:03:06.198617 -0500 pboard  [Local Pasteboard] Type Fetch Error: <private>

Seeing the `pboard` and `Local Pasteboard` keywords in the errors hinted at a problem with the Screen Sharing session's shared clipboard (which I remember I had enabled recently). As it turns out, if I simply disabled the shared clipboard (inside Screen Sharing, click Edit > Use Shared Clipboard), then everything worked great again, without any freezes! Here's the menu option:

<p style="text-align: center;">{{< figure src="./use-shared-clipboard.png" alt="Use Shared Clipboard menu option in Screen Sharing" width="227" height="256" class="insert-image" >}}</p>
