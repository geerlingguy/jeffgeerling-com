---
nid: 3349
title: "My TODO list is a .txt file on the desktop"
slug: "my-todo-list-txt-file-on-desktop"
date: 2024-02-20T03:42:13+00:00
drupal:
  nid: 3349
  path: /blog/2024/my-todo-list-txt-file-on-desktop
  body_format: markdown
  redirects: []
tags:
  - plain text
  - productivity
---

About six months ago, I finally reached a breaking point: my email-based TODO system stopped working.

It was beyond its breaking point for a few years, actually... ever since I my average daily email volume increase from maybe 5-10 'important' emails to deal with to 50+.

My email-based TODO system used to go like this:

  1. Email myself things I deemed important enough to do the next day
  2. Next morning, when I checked my email, knock off the top item in that list, and try to work down the list a bit
  3. Anything else, forward that email again for the next day

Once an item got maybe 5-10 `Fwd:`s in the Subject line, I would decide whether to nix the TODO item entirely, or move it off into a Trello board—in either case, likely to be forgotten forever.

I didn't say the system was _good_.

But it did work, before my inbox became full of _actually important stuff_ relating to running my business.

{{< figure src="./tuesday-md-todo-day-of-week-file.png" alt="Tuesday.md TODO file for the day of the week" width="400" height="auto" class="insert-image" >}}

With the tsunami of emails, a new system was devised, and it centers around a file on my desktop, called: `[day of week here].md`

And the file, this morning, looks like:

```
Today:

  - [ ] SHORT: Water cooling Pi 5, close-up thermal images of Pi 5, overclock testing
  - [ ] Mount PoE Pi 5 in network rack
  - [ ] Pi 5 Silicon video script

Soon:

  - [ ] Benchmark Arm NAS
  - [ ] Set up Samba share on zfs pool on NAS
  - [ ] Set up AirPort base station
  - [ ] Retro Mac video script
  - [ ] Test Hailo AI module, check into Frigate integration
```

My rules for this file are:

  1. No more than three items in 'Today' (I usually complete one, maybe two if I'm crazy lucky)
  2. If an item is bumped down to 'Soon' and doesn't make it to 'Today' within a week or two, knock it off into my Trello board.

This system works surprisingly well, and since I have my `Desktop` folder synced between my Macs and iPhone using iCloud Drive (one of the only good uses for _that_!), the file is always up to date on all my devices.

Using Markdown's checklist syntax and not deleting items or rearranging them until the end of the day means I have a nice visual indication of how much I've completed on a given weekday.

For larger tasks, I still have a Trello card or a separate project folder somewhere that I stash all the important information, but if a task cannot be distilled into a short sentence, it's not worth working on, thus it doesn't go in my `[day of week here].md` file.

And yes, I use a 20% grey desktop background.
