---
nid: 3038
title: "Using a Nikon D750 as a webcam or for live streaming"
slug: "using-nikon-d750-webcam-or-live-streaming"
date: 2020-09-07T04:09:08+00:00
drupal:
  nid: 3038
  path: /blog/2020/using-nikon-d750-webcam-or-live-streaming
  body_format: markdown
  redirects: []
tags:
  - d750
  - nikon
  - photography
  - streaming
  - video
  - webcam
  - youtube
---

You can use a Nikon D750 as a webcam or for live streaming, assuming you have a [mini HDMI to HDMI cable](https://www.amazon.com/Cable-Rankie-High-Speed-Mini-HDMI-Black/dp/B01KRKO4MM/ref=as_li_ss_tl?dchild=1&keywords=mini+hdmi+to+hdmi&qid=1599082907&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=ca7d27b4ab02eb32dacfb0f755ae4129&language=en_US) and an [HDMI interface](https://www.amazon.com/Elgato-Cam-Link-Broadcast-Camcorder/dp/B07K3FN5MR/ref=as_li_ss_tl?dchild=1&keywords=elgato+cam+link+4k&qid=1599082873&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=74c27f913840b095b895320694c706c2&language=en_US) for your computer.

While it's forte is stills photography, the D750 isn't bad at video; it can output up to 1080p at 60 frames per second, and has full-time autofocus, but the live view autofocus isn't that great, so I recommend manual focus if you don't have to move around much.

Why would you use a D750? Well, for the same reason you'd use most any other DSLR or mirrorless camera for video instead of a cheaper webcam or built-in camera on your laptop: the video quality is amazing!

## Video for this blog post

This blog post has a video to go along with it from my YouTube channel:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/S4yqtg432TY" frameborder='0' allowfullscreen></iframe></div>

## Quality Differences

{{< figure src="./d750-webcam-compare-facetime.jpg" alt="D750 as webcam comparison to FaceTime camera on MacBook Pro" width="600" height="338" class="insert-image" >}}

For example, pictured above is a frame captured by my MacBook Pro's built-in webcam. It's not great. You can see me well enough, but it's not a very pleasing image and there's a lot of noise that's even more apparent when you see the live video.

{{< figure src="./d750-webcam-compare-c920.jpg" alt="D750 as webcam comparison to Logitech C920" width="600" height="338" class="insert-image" >}}

And above is another frame captured with my Logitech C920. It's better, and having the camera external to the computer also allows me to position the camera somewhere different. But it's still not amazing.

Finally, this is what it looks like on the D750:

{{< figure src="./d750-webcam.jpg" alt="D750 as webcam - 50mm f/1.8" width="600" height="338" class="insert-image" >}}

In fact, if you watch the video earlier in this post, the whole thing was recorded on my D750.

In addition to more more control over out of focus areas and the type of lens and focal length you want to use, Nikon's image processing engine also results in better color and cleaner output.

## D750 settings for clean HDMI with no time limits

First things first, I set my D750 to 1080p resolution at 60 frames per second (fps). You can use a lower resolution or frame rate if you choose, but I like this frame rate for my YouTube videos and streaming, and my computer can handle it pretty well.

To set the size and frame rate, open the menu, then go to:

**Menu** > **Movie Shooting** > **Frame size and frame rate**

Choose your preferred size and frame rate. Note that some computers might not have the processing power to handle 1080p @ 60 fps. You might need to try lower settings until you find what your computer can handle.

After setting the size and frame rate, you need to set up the D750 for 'Clean HDMI output'; that means setting the D750 so its HDMI output doesn't show camera settings or informational displays, just the pure video output from the camera sensor.

If you don't disable the Live view on-screen display, you'll see all the live view info output on your computer, which is not what you want:

{{< figure src="./d750-live-view-info-display.jpg" alt="D750 live view info display - disable for Clean HDMI output" width="600" height="338" class="insert-image" >}}

To get rid of the info display, turn on Live view by pressing the Lv button, and set the live view switch to 'Movie' mode.

Then go to Menu, and choose:

**Menu** > **Setup** > **HDMI** > **Advanced** > **Live view on-screen display**

Turn that option **Off**, then go out of the menu.

Plug the mini HDMI output on the D750 into your video capture device—in my case I've tested it with an [Elgato Cam Link 4K](https://www.amazon.com/Elgato-Cam-Link-Broadcast-Camcorder/dp/B07K3FN5MR/ref=as_li_ss_tl?dchild=1&keywords=elgato+cam+link+4k&qid=1599420864&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=f5121f923bea8e0e50a1eee69169169b&language=en_US) and a [ClonerAlliance Flint LX](https://www.amazon.com/ClonerAlliance-Capture-Latency-Support-Android/dp/B076GXQTJK/ref=as_li_ss_tl?dchild=1&keywords=cloner+alliance+flint+lx&qid=1599420886&sr=8-1&linkCode=ll1&tag=mmjjg-20&linkId=5b8c8c14cc6d82608212395013e8bb38&language=en_US), and both worked great.

The last thing you'll need to do is tell the camera to remain in Live View for more than 10 minutes. By default, Live View will shut off after 10 minutes.

To do that, go to Menu, and select:

**Menu** > **Custom Setting Menu** > **'c' - Timers/AE lock** > **'c4' - Monitor off delay** > **Live view**

Choose **No limit** to turn off the automatic shutoff.

Use QuickTime Player on your Mac (see [how I use QuickTime to record multiple cameras at once](/blog/2020/recording-multiple-camera-angles-full-size-simultaneously-on-mac)), or whatever other video capture software you'd like, and start a new recording or streaming session, and the camera should show up nice and clear... or maybe a little blurry at first.

## Live view autofocus

If you have a very blurry image, that's because Nikon has live view set to single shot AF, where it only focuses when you half-press the shutter button.

And the reason for this default is apparent the first time you try focusing in live view!

When you use the D750 to take pictures with the viewfinder, you can use the very good Multi-CAM autofocus module to get a good focus lock, quickly, even when using advanced 3D autofocus modes.

{{< figure src="./Multi-CAM-3500FX.jpg" alt="Nikon Multi-CAM 3500FX Autofocus Module" width="400" height="292" class="insert-image" >}}

But when you use the D750 with live view, and the mirror flips up, that autofocus module can't be used since it's not part of the image sensor, so the camera uses on-sensor 'contrast-detect' autofocus, which is pretty slow and results in a lot of back-and-forth as the camera tries to lock focus.

Generally, if you can set focus manually, you'll get better battery life and a lot less noise, especially for older lenses with loud focus motors.

But if you need to have autofocus throughout the video, and can live with the limitations, you can turn on 'Full-time servo AF'. To do that, make sure the focus switch on the side of the lens mount is set to 'AF', then hold the focus mode button and use the back control wheel to set the focus mode to AF-F:

{{< figure src="./d750-af-f-autofocus-live-view.jpg" alt="Nikon D750 Live view with AF-F full time autofocus" width="600" height="338" class="insert-image" >}}

At this point, the camera will begin hunting for focus the entire time live view is engaged. For an older lens like my 60mm f/2.8 macro, focusing is an exercise in futility—and it's loud when it's focusing. For newer AF-S or AF-P lenses, the motor is a bit quieter, but it will still be picked up by the on-camera mic, so I recommend using a separate microphone when you're recording with the D750.

You can either plug a microphone into the D750's mic jack, or plug in a separate sound source on your computer. In my case, I use an [EV RE320](https://www.amazon.com/Electro-Voice-RE320-Diaphragm-Dynamic-Microphone/dp/B00KCN83VI/ref=as_li_ss_tl?dchild=1&keywords=ev+re320&qid=1599082971&s=electronics&sr=1-4&linkCode=ll1&tag=mmjjg-20&linkId=4508a9d4aa187a21a3c4b058266e1c88&language=en_US) microphone plugged into a [Behringer USB audio interface](https://www.amazon.com/gp/product/B00QHURUBE/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=294134088c7563aea1db49b6b022237e&language=en_US) for studio-quality sound.

## Battery life and overheating

So we've gotten a good image out of the camera, but how long will that last? On battery, I got about 20 to 30 minutes of run time. But you can buy an external power supply for the D750, like the [generic EP-5B power adapter](https://www.amazon.com/gp/product/B00VLQ3N3I/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=8a70431bac8b49ab7af452d45b1a1432&language=en_US) I use.

Remove the battery and replace it with the battery connector on the power supply, and the camera stays powered indefinitely.

But what about overheating? As long as you're not recording to the internal memory card and you're using a power supply, you can stream or record pretty much forever. I didn't run into any time limitations. It's probably best if you keep the LCD out from the body, though, just to let more air flow against the back side of the camera where the sensor is located.

> Note: The sensor does get noticeably warm after 30+ minutes of continuous live view mode. I haven't experienced any hot or dead pixels, or any other anomalies even after using my D750 for streaming a few times for over an hour. But your mileage may vary—if you need a camera for tons of streaming video, the D750 might not be the best option!

## Conclusion

As long as you don't need 4K and full-time autofocus, the D750 works well for occasional live streaming or recording to your computer. It has a clean HDMI signal, a crisp output resolution and outputs up to 60 fps.

But there's a reason most people who use their photo gear for video choose cameras like the Nikon Z6 or a Sony mirrorless camera (I usually use my Sony a6000)—those cameras have much better on-sensor autofocus and have lenses built with much quieter autofocus motors. Plus, many of these cameras are built with video in mind.

I don't have a D780, but seeing as most people say it's like a D750 (for viewfinder shooting) mixed with a Z6 (for live view shooting), maybe that camera has the best of both worlds!
