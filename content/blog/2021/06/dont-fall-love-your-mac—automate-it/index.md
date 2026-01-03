---
nid: 3105
title: "Don't fall in love with your Mac\u2014automate it!"
slug: "dont-fall-love-your-mac\u2014automate-it"
date: 2021-06-04T14:00:26+00:00
drupal:
  nid: 3105
  path: /blog/2021/dont-fall-love-your-mac—automate-it
  body_format: markdown
  redirects: []
tags:
  - ansible
  - automation
  - mac
  - mac mini
  - macbook air
  - macbook pro
  - macos
  - video
  - youtube
---

Ah, the feeling of unpacking a brand new computer:

{{< figure src="./macbook-pro-16-setup-2019.jpeg" alt="16 inch 2019 MacBook Pro with Intel core i9 9th gen processor - macOS Setup screen" width="500" height="368" class="insert-image" >}}

In my case, I'm actually _selling_ the 16" MacBook Pro pictured above and replacing it with a 13" MacBook Air and 10 Gigabit Mac mini.

Once you turn on the new Mac, what's next? Do you:

  1. Wait 6+ hours for a Time Machine restore (you _do_ have a backup, right?) or use Migration Assistant to move all your old files and cruft from your old Mac?
  2. Manually install apps and click through tons of preference panes to set it up to your liking?
  3. Use a completely automated process like [mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook) to build everything fresh using `mas`, `homebrew`, and a tool like Ansible, so it's in a pristine state, with all your data and apps configured within an hour or two?

I choose the latter. And as a bonus, I can run the automation on both my new Macs frequently, to keep their configuration and app layout in sync!

I just posted a video about the entire process to my YouTube channel:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/1VhPVu5EK5o" frameborder='0' allowfullscreen></iframe></div>
</div>

As I said in the video, you should really treat your workstation like cattle, not a pet—my goal is to be able to be 100% productive with a new computer in less than a day. Sometimes you don't even get the choice, if your computer dies or gets stolen!

If you want to see how to use the open source playbook, [check out the mac-dev-playbook README](https://github.com/geerlingguy/mac-dev-playbook).

It took about one hour before all my apps and configuration were present, and only a few more minutes for the initial Dropbox data sync to complete. After that, Photos slowly downloaded my entire library in the background, and all the rest of my work is open source and available on GitHub and a private mirror, so I just ran a shell script to clone all my repositories to my `~/Development` folder.

Less than a full day to fully transition to a new Mac mini and format my old MacBook Pro—all done while recording the video above!

There are other tools focused on managing 'fleets' of Macs (like [Jamf](https://www.jamf.com) and other MDM tools), but Ansible's a pretty robust tool for managing one or more Macs, and it and the Mac Dev Playbook are nice and free!
