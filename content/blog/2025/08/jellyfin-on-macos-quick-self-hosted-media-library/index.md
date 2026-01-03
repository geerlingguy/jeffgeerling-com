---
nid: 3485
title: "Jellyfin on macOS for a quick self-hosted media library"
slug: "jellyfin-on-macos-quick-self-hosted-media-library"
date: 2025-08-20T01:06:23+00:00
drupal:
  nid: 3485
  path: /blog/2025/jellyfin-on-macos-quick-self-hosted-media-library
  body_format: markdown
  redirects: []
tags:
  - homebrew
  - jellyfin
  - mac
  - macos
  - media
  - movies
  - self-hosted
---

I forgot to bring my portable Pi media server running Jellyfin on a family trip, but had a small selection of my [ripped movie and TV show library](/blog/2022/how-i-rip-dvds-and-blu-rays-my-mac-2022-edition) on my portable SSD.

One dreaded part of choosing a movie or show to watch after a rainy afternoon and all other avenues of entertainment are exhausted is having the kids (especially the youngest, who can't read yet) choose a movie without the 'movie shelf' showing the movie posters/cover artwork.

So... without the Pi, and only armed with my MacBook Air, I thought I'd spin up a Jellyfin Docker container. Except, [macOS is explicitly called out as unsupported for the Docker container for Jellyfin](https://jellyfin.org/docs/general/installation/container/#installation-instructions).

Switching tracks, I found Jellyfin is also packed up as a .app for macOS, and you can install it by [downloading the .dmg and copying the .app to your Mac](https://jellyfin.org/downloads/macos/), or you can do it like I did, with Homebrew:

```
brew install --cask jellyfin
```

Once it's installed, open Jellyfin in the Applications folder to launch it. You won't see a traditional Dock icon or app window when it launches, it just runs in the background, with a tiny Jellyfin status menu in the menu bar:

{{< figure src="./jellyfin-status-menu.png" alt="Jellyfin Status Menu in macOS" width="210" height="auto" class="insert-image" >}}

Fire up your browser, and visit `http://localhost:8096` to open up the Jellyfin UI (or just choose 'Launch' in the status menu, to be taken there directly).

Follow the wizard to choose a language and create your admin user, then when it asks about Media Libraries, add a media library (e.g. 'Movies') and browse to the path where all your media files are stored.

After you finish the setup wizard, wait a minute or so for the full media library scan to complete, then refresh the Jellyfin library page in your browser, and you should see all the available movies / shows...

{{< figure src="./jellyfin-macos-localhost-8096.jpg" alt="Jellyfin server running on macOS in browser with movie library" width="700" height="470" class="insert-image" >}}

To quit the Jellyfin server, click on the Jellyfin status menu, and choose 'Quit'. To uninstall, quit Jellyfin from the status menu, then drag Jellyfin.app to the Trash.
