---
nid: 2092
title: "Minecraft Patching Guide for Macs"
slug: "minecraft-patching-guide-macs"
date: 2012-04-24T15:09:29+00:00
drupal:
  nid: 2092
  path: /blog/2012/minecraft-patching-guide-macs
  body_format: full_html
  redirects: []
tags:
  - fun
  - games
  - gaming
  - guide
  - mac
  - minecraft
  - patches
  - tutorial
---

I've watched a few episodes of 'The Minecraft Project' on YouTube for inspiration, and I occasionally play Minecraft for an hour or two as a diversion (it's like LEGOs on a computer, but much more fun, because there are zombies!).

<p style="text-align: center;">{{< figure src="./minecraft-farm-jeff.jpg" alt="Jeff's Humble little Minecraft Farm" width="400" height="255" class="blog-image" >}}
My humble little Minecraft farm.</p>

One thing I've always liked is The Minecraft Project's look and feel, mostly due to syndicate's use of the DokuCraft Light texture pack. However, getting that texture pack to work along with other mods and patches (especially the automatic tool switcher mod) took some work on my Mac, and I thought I'd post my process for getting everything to work here, for the benefit of others having the same troubles (especially those getting the 'Use the patcher noob' messages where water, lava, etc. are supposed to appear):

<ol>
	<li>Switch Minecraft to the default texture pack.</li>
	<li>Download and run <a href="http://www.minecraftforum.net/topic/232701-124-125update-328-mcpatcher-hd-fix-235-01/">MCPatcher</a>.

<ol>
	<li>If you have problems, delete the entire 'bin' folder from the minecraft directory (in Users/[yourusername]/Library/minecraft/), reopen Minecraft and run it (this will force-redownload all the Minecraft binary files), and then try MCPatcher again).</li>
</ol></li>
	<li>Download the latest <a href="http://www.minecraftforum.net/topic/513093-32x16x125-dokucraft-the-saga-continues/">Dokucraft Light texture pack</a>, and place it in the proper folder (on a Mac, drop the downloaded .zip file into Users/[yourusername]/Library/minecraft/texturepacks/.</li>
	<li>Download <a href="http://www.minecraftforum.net/topic/75440-v125-risugamis-mods-everything-updated/">ModLoader</a> and follow the directions in the linked forum thread to install it.</li>
	<li>Download <a href="http://www.minecraftforum.net/topic/753030-125124-thebombzens-mods/">AutoSwitch</a> and put the .class file into the minecraft.jar file at Users/[yourusername]/Library/minecraft/bin/minecraft.jar.

<ol>
	<li>If the jar file can't be opened like a directory, change the filename to .zip, double-click on it to unarchive it, then put the file into the directory and change the name back to minecraft.jar again.</li>
</ol></li>
</ol>

NOTE:&nbsp;To open the 'Library' folder in Mac OS X Lion, hold down Option while in the 'Go' menu in the Finder, and you'll see 'Library' appear in the list of folders there
