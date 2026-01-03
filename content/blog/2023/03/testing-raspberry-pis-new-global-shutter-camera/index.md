---
nid: 3278
title: "Testing Raspberry Pi's new Global Shutter Camera"
slug: "testing-raspberry-pis-new-global-shutter-camera"
date: 2023-03-09T08:00:11+00:00
drupal:
  nid: 3278
  path: /blog/2023/testing-raspberry-pis-new-global-shutter-camera
  body_format: markdown
  redirects: []
tags:
  - camera
  - distortion
  - global shutter
  - hq camera
  - photography
  - raspberry pi
  - video
  - youtube
---

Today Raspberry Pi launched their new [Global Shutter Camera](https://www.youtube.com/watch?v=3HhdO11lD04).

{{< figure src="./global-shutter-camera-sensor.jpeg" alt="Global Shutter Camera showing image sensor" width="700" height="467" class="insert-image" >}}

Outwardly it is almost identical to the 12 Megapixel High Quality Camera, and like that camera it accepts C and CS mount lenses, or most anything else with the appropriate adapter.

But flipping it over reveals a black plastic cover over the back of the board that is _not_ present on the HQ or M12 HQ Camera:

{{< figure src="./global-shutter-camera-back.jpeg" alt="Global Shutter Camera Backside Raspberry Pi Logo in plastic cover" width="700" height="467" class="insert-image" >}}

I asked if this cover will make it's way to the HQ camera or not, and so far the word is "probably not, but never say never!" The cover helps prevent light leakage through the PCB to the sensor, and also protects the components on the rear of the board.

## Global vs Rolling Shutter

But the headline feature is the image sensor on this camera, specifically the Sony IMX296. Support was added to Raspberry Pi's Linux fork [back in May last year](https://github.com/raspberrypi/linux/pull/5039), so it works out of the box with Raspberry Pi OS now (though you might need to update to make sure it works!).

The IMX296 is only 1.6 Megapixels (1440x1080), but each one of those pixels is read _instantaneously_. So artifacts you get from rolling shutter, like the weird bending of spinning or moving objects, are gone.

Compare this image I took panning an HQ camera rapidly back and forth:

{{< figure src="./hqcam-example-distortion.jpg" alt="High Quality Camera Distortion due to camera pan" width="700" height="394" class="insert-image" >}}

In this image, I'm holding the black object vertically, but as I pan, it gets distorted and looks like it's being held at a slight angle, depending on the speed of the panning.

{{< figure src="./gscam-example-no-distortion.png" alt="Global Shutter Camera camera panning showing no distortion" width="700" height="394" class="insert-image" >}}

This is the exact same frame from the Global Shutter Camera, showing that while motion blur is still present (the shutter speed was too slow to prevent _that_) the distortion due to rolling shutter is gone.

The setup I used in for this comparison was both cameras, triggered over WiFi by an Ansible playbook, recording side by side on my tripod:

{{< figure src="./global-shutter-camera-with-hq-camera-on-tripod.jpeg" alt="HQ Camera and Global Shutter Camera on Tripod in Jeff Geerling's Studio" width="700" height="394" class="insert-image" >}}

You can see a bit more about it, as well as _video_ comparisons which really show the 'jello' or 'jiggly' effect you get from rolling shutter, in my latest YouTube video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/3HhdO11lD04" frameborder='0' allowfullscreen></iframe></div>
</div>

## Mounting is Different

One caveat for those wishing to incorporate the Global Shutter Camera in their projects is the changed mounting options due to the black plastic cover on the back.

For the Adafruit camera mounting plate, I had to swap out the nylon standoffs it came with for taller ones, since the mounting holes are a bit recessed into the back plate:

{{< figure src="./global-shutter-camera-on-desk.jpeg" alt="Mounting holes and back recessed mounting option for Global Shutter Camera" width="700" height="467" class="insert-image" >}}

The Global Shutter Camera should be available now, for the same price as the HQ camera ($50). You can find all the specs and more details about the sensor on the [Raspberry Pi Global Shutter Camera product page](https://www.youtube.com/watch?v=3HhdO11lD04).
