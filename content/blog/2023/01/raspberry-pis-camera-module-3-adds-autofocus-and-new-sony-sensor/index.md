---
nid: 3262
title: "Raspberry Pi's Camera Module 3 adds autofocus and new Sony sensor"
slug: "raspberry-pis-camera-module-3-adds-autofocus-and-new-sony-sensor"
date: 2023-01-09T08:00:08+00:00
drupal:
  nid: 3262
  path: /blog/2023/raspberry-pis-camera-module-3-adds-autofocus-and-new-sony-sensor
  body_format: markdown
  redirects:
    - /blog/2023/raspberry-pis-camera-module-3-adds-autofocus-and-imx708-sensor
aliases:
  - /blog/2023/raspberry-pis-camera-module-3-adds-autofocus-and-imx708-sensor
tags:
  - autofocus
  - camera
  - camera module
  - photography
  - raspberry pi
  - reviews
  - video
  - youtube
---

Raspberry Pi just announced their new [Camera Module 3](https://www.raspberrypi.com/products/camera-module-3/), which comes in four variations (standard and wide angle, normal and NoIR for infrared use), and costs $25 for the standard versions, and $35 for wide angle.

{{< figure src="./camera-module-3-varieties.jpeg" alt="Raspberry Pi Camera Module 3 varieties - standard, wide, and NoIR" width="700" height="467" class="insert-image" >}}

That's a step up from the older [Camera Module 2](http://raspberrypi.com/products/camera-module-v2/), which cost $25 and only came in a 'standard' focal length.

I posted a video reviewing the Camera Module 3 on YouTube, and you can watch it here:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class="embed-container"><iframe src="https://www.youtube.com/embed/1EIFfln3Kxs" frameborder="0" allowfullscreen=""></iframe></div>
</div>

I won't go through all the detail found in the video, but I did want to give a quick summary of my review. The new module uses the Sony IMX708 image sensor, with all Sony's wonderful modern features like backside illumination, stacked CMOS, etc.

But the major new addition is autofocus—specifically, very snappy PDAF (Phase-Detect Auto Focus).

{{< figure src="./camera-module-3-lens-macro.jpeg" alt="Camera Module 3 autofocus and lens mechanism" width="700" height="467" class="insert-image" >}}

Raspberry Pi OS has already been updated so `libcamera` and `Picamera2` fully support the new Camera Module, and indeed, if you want to see how effective the autofocus is, you can plug in the camera, and on an up-to-date Pi, run:

```
libcamera-hello -t 0 --autofocus-mode continuous
```

And point the camera around at various objects. I found it much faster to focus than the [ArduCam Hawk-eye](/blog/2022/64-megapixel-hawk-eye-brings-high-res-imaging-pi), though the image quality isn't nearly as crisp.

The focus felt similar in responsiveness to my iPhone, which is all the more impressive considering the horrible experience of trying to manually refocus the older Camera Module 2 with a purpose-built wrench.

I didn't have a problem focusing in most scenarios, though it struggled when only part of the frame was filled with a subject. I tried taking some photos of houses with lots of sky above, and the Pi kept losing focus:

{{< figure src="./picam-lose-focus-sunny-sky.jpg" alt="Pi Camera Module 3 loses focus in sunny sky with lower contrast" width="700" height="394" class="insert-image" >}}

Outside of being impressed by autofocus performance (it's not going to beat a mirrorless, but it's on par with your average smartphone), the image quality was good.

The sensor is great—and with even passable lighting, you'll get a good exposure and color balance leaving the Pi set to auto settings in _most_ scenarios.

The one place where this new Camera Module falls apart a bit is in the details. The lens included in both the standard and wide-angle versions just can't resolve 12 megapixels of detail.

The difference is most apparent when comparing the same shot between the Camera Module 3 and my iPhone 13 Pro—the sharpness is just not there on the Pi camera:

{{< figure src="./picam-vs-iphone-13-pro-camera.jpg" alt="Camera Module 3 versus iPhone 13 Pro - lens sharpness" width="700" height="394" class="insert-image" >}}

And that's not on the corners—that distant tower was positioned in the center of the frame!

You can't expect the moon out of a $35 camera with an integrated lens, and it _is_ still a marked improvement in all aspects versus the earlier Camera Modules. But I hate it when a higher resolution sensor's potential isn't fully realized because the glass in front is just not good enough.

Ah well... it's the same thing as someone buying a Canon R5 and throwing a cheap kit lens on it. It's not the worst thing, and there's still plenty of resolution to be useful!

The most important difference between the Camera Module 3 and those before is in physical dimensions. The PCB footprint and mounting holes are identical, but the camera on top is a bit larger and has a movable front lens element, meaning many existing Camera Module cases will not work with this new version.

But any design which doesn't enclose the lens should be fine.

I'd like to thank Raspberry Pi for sending a set of Camera Modules (pictured at the top of this post) for testing and review—I didn't get too much time to test the video recording functionality or the NoIR camera yet, but I hope to do so when my schedule clears up.
