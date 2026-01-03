---
nid: 2780
title: "Fixing the blurry focus on some Raspberry Pi Camera v2 models"
slug: "fixing-blurry-focus-on-some-raspberry-pi-camera-v2-models"
date: 2017-06-17T02:55:38+00:00
drupal:
  nid: 2780
  path: /blog/2017/fixing-blurry-focus-on-some-raspberry-pi-camera-v2-models
  body_format: markdown
  redirects: []
tags:
  - camera
  - focus
  - hacks
  - hardware
  - photography
  - raspberry pi
  - time lapse
---

The [original Raspberry Pi Camera model v1.3](https://www.amazon.com/Raspberry-5MP-Camera-Board-Module/dp/B00E1GGE40/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1497295092&sr=1-9&keywords=raspberry+pi+camera&linkCode=ll1&tag=mmjjg-20&linkId=9521a2e546e8e83c4213653576055ae7) came from the factory set to ∞ (infinity) focus, so when you used it out of the box for something like a landscape timelapse rig, or for security or monitoring purposes (where the Pi is at least 5 meters away from the subjects it's recording), everything would look crisp and sharp.

For many fixed-focus cameras and lower-end camera sensors, it makes sense to set them to infinity focus; closer objects are still recognizable, but slightly blurry. Most of these cameras don't need to focus on a person a meter away for a portrait, and they're also rarely used for FaceTime-like video chat.

For the [Raspberry Pi Camera v2](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1497295092&sr=1-3&keywords=raspberry+pi+camera&linkCode=ll1&tag=mmjjg-20&linkId=bdb0d05ae19ffebb4d279b38eb4bcc72), the Raspberry Pi Foundation originally decided to have the focus set for 1-2 meters away, so if you bought a v2 camera and used it for distant subjects (like I do for most of my [pi-timelapse](https://github.com/geerlingguy/pi-timelapse) videos), then everything looked a bit blurry or hazy out-of-the-box.

For example, when I swapped out my v1.3 camera for a v2 model this week to record some residential road construction, I ended up getting a pretty poor image:

{{< figure src="./raspberry-pi-camera-v2-blurry-factory-focus.jpg" alt="Raspberry Pi Camera v2 with blurry focus set at the factory" width="650" height="366" class="insert-image" >}}

Notice especially the inset cone at slight magnification; it is not only blurry, but also washed out since a blurry image can really mess with the camera's autoexposure, resulting in a muddy picture that is at best a hazy reproduction of the scene.

The Raspberry Pi Foundation decided to set v2.1 and greater cameras back to inifinity focus, so this wouldn't be an issue with the latest camera. But a lot of resellers (including Amazon) are still shipping from their stock of v2 cameras with the focus set at a short distance.

> **Warning**: Adjusting the lens in the way described below will likely void any warranty you may have had, and you won't be able to return the camera module after doing this. So either be careful and suffer the consequences if something breaks... or don't do it and try to buy a newer camera module with infinity focus from the factory!

Luckily, there's a fairly easy fix: If you have a pair of jeweler's pliers or mini needle-nose pliers, you can use them to directly manipulate the lens focus; just grasp the front element of the lens and rotate; if the lens is difficult to rotate (it has a slight amount of glue locking it in place from the factory), you may need to use another tweezers/pliers to carefully hold the base of the camera module, then give a little back-and-forth twist until the lens starts rotating.

<p style="text-align: center;">{{< figure src="./mini-needle-nose-pliers.jpg" alt="Mini needle-nose pliers for precision electronics work" width="650" height="383" class="insert-image" >}}<br>
<em>I bought <a href="https://www.amazon.com/gp/product/B00FZPHEW2/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=889598a42733f5c0f728f70b1e8dbb4b">this long-nose, or needle-nose pliers</a> from Amazon; but any small needle-nose pliers or a sturdy pair of tweezers should do fine.</em></p>

<p style="text-align: center;">{{< figure src="./raspberry-pi-zero-in-case-with-camera-arrows-on-indents.jpg" alt="Raspberry Pi Zero W in case with camera on top cover" width="650" height="409" class="insert-image" >}}<br>
<em>To adjust focus, pinch the indentations with the pliers (gently), then give a small amount of torque (just enough to break the thin glue that sets factory focus). Turn back and forth in small increments while taking pictures to confirm the correct focus.</em></p>

In my case, I needed to rotate the lens about 50° counter-clockwise (I rotated about 5°, took a picture, rotated another 5°, etc. until the image was about as sharp as I could make it), and the sharpness was _greatly_ improved:

{{< figure src="./raspberry-pi-camera-v2-sharper-manual-focus.jpg" alt="Raspberry Pi Camera v2 with sharper focus set manually" width="650" height="366" class="insert-image" >}}

And here's that other blurry picture again, for comparison:

{{< figure src="./raspberry-pi-camera-v2-blurry-factory-focus.jpg" alt="Raspberry Pi Camera v2 with blurry focus set at the factory" width="650" height="366" class="insert-image" >}}

> [HollandJim](https://www.reddit.com/user/HollandJim) on Reddit mentioned there's also a little $0.95 purpose-built [Lens Adjustment Tool](https://www.adafruit.com/product/3518) available from Adafruit. It is worth picking up this specialty tool if you plan on using your Pi camera in a variety of settings where focus would need to be changed.

If you don't have small pliers, then a credit card, a drill, and a file will do in a pinch. You would need to drill a hole in the credit card that's about 5/16" (~8mm), then file away slots in this hole (with a very small file) to line up to the indentations on the top of the camera lens. See [this Q&A thread](https://www.raspberrypi.org/forums/viewtopic.php?f=43&t=145815) on the Raspberry Pi forums for more on that technique, and some of the explanation of why the v2 camera was made the way it was.
