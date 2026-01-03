---
nid: 3164
title: "Autofocus on a Pi - ArduCam's new 16MP camera"
slug: "autofocus-on-pi-arducams-new-16mp-camera"
date: 2022-01-12T15:05:28+00:00
drupal:
  nid: 3164
  path: /blog/2022/autofocus-on-pi-arducams-new-16mp-camera
  body_format: markdown
  redirects:
    - /blog/2022/autofocus-on-pi-–-arducams-new-16mp-camera
aliases:
  - /blog/2022/autofocus-on-pi-–-arducams-new-16mp-camera
tags:
  - arducam
  - camera
  - hq camera
  - photography
  - raspberry pi
  - reviews
  - video
  - youtube
---

{{< figure src="./arducam-with-other-pi-cameras-hq-v2.jpeg" alt="ArduCam with other Raspberry Pi Cameras - v2 HQ and Autofocus 16MP" width="660" height="440" class="insert-image" >}}

ArduCam recently completed a successful [crowdfunding campaign](https://www.kickstarter.com/projects/arducam/high-resolution-autofocus-camera-module-for-raspberry-pi) for a 16 megapixel Raspberry Pi camera with built-in autofocus.

The camera is on a board with the same footprint as the Pi Camera V2, but it has a Sony IMX519 image sensor with twice the resolution (16 Mpix vs 8 Mpix) and a larger image sensor (1/2.53" vs 1/4"), a slightly nicer lens, and the headline feature: a built-in autofocus motor.

## Autofocus performance

Getting right into the meat of it: autofocus works, with some caveats.

First, the good. Autofocus is quick to acquire focus in many situations, especially in well-lit environments with one main subject. Using ArduCam's fork of `libcamera-still` or `libcamera-vid`, you only need to pass in `--autofocus` and the camera will snap into focus immediately.

For some examples of how well it works—since it's hard to convey in a static blog post—please check out my YouTube video reviewing the camera:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/j2S8sZoH36Y" frameborder='0' allowfullscreen></iframe></div>
</div>

But here begins the limitations. First, autofocus is generally a one-time thing: you can pass `--autofocus`, and the camera focuses once, immediately after invoking the `libcamera-*` command, and you can also pass `--keypress` to listen for a 'F' + 'Enter' key combo which will refocus while the camera feed is live.

ArduCam also maintains a [Python focusing script](https://github.com/ArduCAM/Arducam-Pivariety-V4L2-Driver/tree/master/focus) that can be used to manually control autofocus with the up and down arrows, or you can use `v4l2-ctl -d /dev/v4l-subdev1 -c focus_absolute=[value]` to work to manually focus the camera one time.

Discounting software issues, the lack of full-time autofocus—like that on webcams and point-and-shoot cameras—means this camera requires tweaking and a little extra work for certain use cases.

Finally, autofocus is a one-trick pony. Originally I thought it was based around a small central focus area, but after more usage, it seems to be based on contrast across the full frame. It was frustrating sometimes, trying to focus on a central subject with a detailed background—more often than not, the camera would focus on the background.

And there's currently no method of face detection or 'focus areas', so if you want to focus on something with less contrast or something that doesn't dominate the frame, you'll have to do it manually.

{{< figure src="./arducam-on-tripod-mug.jpeg" alt="ArduCam 16MP Autofocus Pi Camera on Tripod with Raspberry Pi Mug" width="660" height="440" class="insert-image" >}}

_That said_ I strongly prefer the ArduCam with autofocus over the Pi Camera v2. For any use case where the camera is not in a fixed position and focused to infinity (e.g. for security or environment monitoring), the ArduCam is more convenient, with better image quality to boot.

The ArduCam could also fit some basic macro / close-up use cases too—I tested a minimum focus distance of 6 cm (about 2.25").

## Image quality

I set three cameras in front of a still-life featuring a couple Pi Zeros, a Raspberry Pi mug, my Go gopher, and my Null 2 retro game console. I'll show the full pictures below, linked to the full resolution, unmodified images (just cropped slightly).

Everything was identical in the images, except for shutter speed—it was adjusted to compensate for the differing apertures between the cameras.

### Pi Camera V2

<a href="./cropped-pi-camera-v2-still.jpg">{{< figure src="./pi-camera-v2-still-example.jpg" alt="Pi Camera V2 Still Life Example" width="700" height="350" class="insert-image" >}}</a>

### ArduCam 16MP Autofocus Camera

<a href="./cropped-pi-arducam-still.jpg">{{< figure src="./pi-arducam-still-example.jpg" alt="ArduCam 16MP Autofocus Camera Still Life Example" width="700" height="359" class="insert-image" >}}</a>

### HQ Camera

<a href="./cropped-hq-camera-still.jpg">{{< figure src="./hq-camera-still-example.jpg" alt="HQ Camera Still Life Example" width="700" height="350" class="insert-image" >}}</a>

### Image quality observations

It seems in terms of colors, the HQ Camera reproduced the scene the most accurately—notice especially the green of the PCBs on the Pi Zeroes, and the more deeply saturated red of the mug.

But in terms of clarity, the 16 megapixel sensor on the ArduCam beats both of the official Pi Cameras—including the 12 megapixel HQ camera, at least with the standard 6mm wide angle lens I used in my test. With a nicer lens, you probably wouldn't notice the difference as much, but you'll be adding a bit of cost!

Also, partly due to the resolution, but probably also due to image processing, the ArduCam doesn't suffer from some amount of fringing that can make edges 'muddier' (even in the center of the frame)—notice the transition from the white of the Pi logo on the mug to the red. The dark fringing on the Pi logo shouldn't be there—and it's not, on the ArduCam.

## Video quality

For video quality... it's hard to convey that in a blog post, so again, check out the embedded video above. There's a video demonstration around the 5:00 mark.

What's interesting is—and I only noticed this after editing the video—the ArduCam seems to have focused on the background in that video clip, and I think it's because the guitar, photo, and other elements in the background have more contrasty elements on them than my face and shirt.

It's counter-intuitive, because I think most people (especially coming from dedicated cameras, whether point and shoot or SLR/mirrorless) would expect there to be some sort of center-weighting... but there seems to be none of that, nor any control other than "trigger an autofocus event".

And as mentioned earlier, you can run `libcamera-vid` with the `--keypress` option, then press F + Enter to re-focus, but it's a bit of a burden to try doing that if you're using it as a webcam. It would be interesting if there were a way to have the camera detect when contrast/focus is lost, then refocus at that point.

You could probably set up an image processing pipeline that would do it automatically using something like OpenCV, but it would be really nice to have it 'out of the box', at least if you want to use the ArduCam for video.

## Conclusion

The ArduCam 16 MP Autofocus Camera should be available soon [on ArduCam's website](https://www.arducam.com), and the retail price is $25. That's the same price as the less-featured Pi Camera V2, and half the price of the High Quality Camera.

I have a feeling this camera will be the default choice for most Pi users moving forward—the convenience of autofocus, the standard Pi Camera module footprint, and the extra resolution will make Pi vision and photography projects that much more interesting moving forward.
