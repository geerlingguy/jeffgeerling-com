---
nid: 2991
title: "How I livestream with OBS, a Sony a6000, and a Cam Link"
slug: "how-i-livestream-obs-sony-a6000-and-cam-link"
date: 2020-04-09T20:44:27+00:00
drupal:
  nid: 2991
  path: /blog/2020/how-i-livestream-obs-sony-a6000-and-cam-link
  body_format: markdown
  redirects: []
tags:
  - audio
  - how-to
  - livestream
  - microphone
  - streaming
  - tutorial
  - video
  - youtube
---

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/G9dSMAXHNDw" frameborder='0' allowfullscreen></iframe></div>

A few weeks before this year's pandemic started affecting the US, I started live-streaming on my YouTube channel.

In the past, I've helped run live streams for various events, from liturgies in a cathedral to youth events in a stadium. (I even wrote a blog post on the topic [a few weeks ago](/blog/2020/how-livestream-masses-or-other-liturgies-on-youtube).)

For larger events, there was usually a team of camera operators. We also had remote control 'PTZ' cameras, and dedicated streaming hardware like a Tricaster.

For my own livestreams, I had a very limited budget, and only one person (me) to operate the camera, _produce_ the live stream, and be the _content_ on the live stream!

Since many smaller churches are gearing up to live stream Easter or other major liturgies this week, I thought I'd make a quick video showing how I do my livestream, and giving some tips for people in a similarly budget-and-personnel-limited situation!

This video should also be useful for other individuals interested in making higher quality live streams on their own.

## Simplest option: a smartphone on a tripod

There are a number of different options you have for live streaming; the simplest is to set up a smartphone on a tripod, point it at something, and start streaming using YouTube, Facebook Live, Periscope, or whatever streaming service you want.

But the quality is usually so-so, you are limited to one camera and viewing angle, and the sound is often terrible since the microphone on the phone is not close to the person speaking, nor is it tied into a sound system.

So the next step is to set up a laptop with an external camera.

## Laptop and external camera

If you don't already have a quality webcam—I usually recommend a [Logitech StreamCam](https://www.amazon.com/Logitech-Streamcam-Streaming-YouTube-Graphite/dp/B07TZT4Q89/ref=as_li_ss_tl?dchild=1&keywords=logitech+webcam&qid=1584494169&sr=8-4&linkCode=ll1&tag=mmjjg-20&linkId=2681445ad969e3fa24b8ec8e66c08b26&language=en_US) or [Breo](https://www.amazon.com/gp/product/B01N5UOYC4/ref=as_li_ss_tl?pf_rd_r=4RK2VKPHQWDBDC8G0060&pf_rd_p=ab873d20-a0ca-439b-ac45-cd78f07a84d8&linkCode=ll1&tag=mmjjg-20&linkId=d067b35d2d5aa8d32bdb41929bc781b3&language=en_US)—you might be out of luck because they're sold out pretty much everywhere right now.

But you might have or be able to borrow someone's digital camera (mirrorless or some models of DSLR), and use that to do the live stream.

To do this, you need to be able to plug the camera's HDMI video output into your computer. The best device to assist with that is the [Elgato Cam Link 4K](https://www.amazon.com/Elgato-Cam-Link-Broadcast-Camcorder/dp/B07K3FN5MR/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=7c23ba056b36c281f49c4a60f5dad8e2&language=en_US). Most cameras don't have a full-size HDMI output, so you'll also need to buy a mini or micro-HDMI-to-HDMI adapter cable.

For my setup, I use a [Sony a6000](https://www.amazon.com/Sony-Mirrorless-Digitial-3-0-Inch-16-50mm/dp/B00I8BICB2/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=93347c427d39e481873c3b504760910f&language=en_US) mirrorless camera, with a [10 foot micro-HDMI to HDMI cable](https://www.amazon.com/gp/product/B00609B3J2/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=263baef94440f87daec6419e45efea76&language=en_US), plugged into my Cam Link 4K, which is then plugged into my computer.

I also have a nice [Manfrotto fluid video tripod head](https://www.amazon.com/gp/product/B000JLO6RS/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=1ef269a82ea6a35afc214b7c7a85ce4e&language=en_US) that allows me to pan and tilt the camera smoothly, so if I want to move around the camera and zoom in or out during the stream, I can do that easily (but for my live streams, I usually keep it still).

You can use an external camera plugged into the Cam Link directly with most any streaming software, since it shows up as a selectable camera just like any plugged in webcam, but for ultimate control, especially with advanced 'scene' capabilities that allow you to add title cards (for things like prayers), you should use streaming software like [OBS](https://obsproject.com).

## OBS for ultimate streaming control

OBS is a free and open source program that lets you produce live streams and deliver the streaming content into any major platform like YouTube, Facebook Live, or Twitch.

For my livestreams, I have one main 'scene' set up in OBS:

  - It has my main computer screen so I can share what I'm doing on the computer.
  - It has my external camera in a 'picture in picture' area on the bottom right.
  - It uses my external shock-mounted microphone, for really good audio.

We'll get to the audio in a minute, but for now I'll focus on OBS.

In OBS, you can set up one or more 'scenes' and switch between them. You could have one scene be an image or video that plays prior to your stream officially starting (make sure you have the microphone or audio input muted during that time!). Then you could have another scene with your main camera, and switch to that when it's time for the stream to start.

If you have a webcam in addition to the external camera, you could set the webcam to be a 'wide' overview angle, showing the entire area of interest (like the whole sanctuary, if streaming a liturgy), and you can have the external camera set up on a tripod with a zoom lens, and that camera could zoom in and focus on areas of interest, like an altar, lectern, or the presider's chair.

In OBS, you can switch to the wide-angle webcam scene, then while it's not visible on the live stream, point the external camera at the next area of interest, and then go back to OBS and switch back to the external camera again.

You're basically doing all the amazing things sports broadcasters do when producing live events in their video trailer, but all on your own laptop!

## Great lighting makes great video

Now, many churches already have pretty good lighting in the sanctuary, but if not, in a pinch you can set up a few worklights on stands to 'flood' the area in light.

For individual live streaming, I have a few overhead LED light panels that are built into my office lighting. To supplement that and give a tiny bit of a 'catch' light in my eyes, as well as slightly more even illumination on my face, I have a small [on-camera video light panel](https://www.amazon.com/gp/product/B07YJFCSRR/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=6a675cbc7ab9338b3f8da4215dc1de50&language=en_US), which is battery powered, charges over USB, and sits in my camera's hot shoe.

There are other lighting rigs which can be much more elaborate, but the main thing is to make sure there's enough light so your camera doesn't have to raise its ISO or lower its shutter speed to get good image quality. If that happens you get a lot of distracting noise and artifacts in the live stream picture.

## Making sure you have power

There are three major caveats to this setup, though, and they all have to do with power:

First, mirrorless and DSLR cameras like my a6000 use a lot of power when streaming video, and one battery only lasts about 20 or 30 minutes. So I have an [external power supply for my a6000](https://www.amazon.com/gp/product/B01D67LTIK/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=ad6eccb12c335825533926b3a9b1962a&language=en_US) that plugs into where the battery is. Not all cameras have an external power supply available, or can be powered through a USB-C cable, so you might have to make sure you have extra batteries and a plan for swapping them out in the middle of the stream.

Second, you should make sure you have your laptop plugged into external power the entire stream, as it will also need to use a lot of power to put together and compress the live stream.

Third, you should use as new and fast a laptop as possible; a cheap ten your old laptop is not going to have the processing power required to run a live stream with OBS very well.

## Getting great sound

The last thing that's important to mention is sound.

In my streams, I am able to use a big, bulky [studio microphone](https://www.amazon.com/Electro-Voice-EVRE320-RE320/dp/B07K2YWRVZ/ref=as_li_ss_tl?dchild=1&keywords=re320&qid=1586464780&sr=8-3&linkCode=ll1&tag=mmjjg-20&linkId=64aaed4cecaa319aac611b487fd1a7c5&language=en_US) plugged into an [audio interface](https://www.amazon.com/gp/product/B00QHURUBE/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=849dd11891d39b604b98fcec1187e242&language=en_US) on my computer. And this makes really good sound.

For live streams, the best option is to find a way to tie the in-house audio system directly into your computer. Usually if you have a sound system, it has a headphone output, usually with a separate headphone audio level control.

If that's the case, you could get a [long quarter-inch guitar cable](https://www.amazon.com/dp/B07GZPM5BB/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=d1b51e505702340c3d81c88290d443f3&language=en_US), plug it into the headphone output, then plug the other end into an [audio adapter](https://www.amazon.com/AD2-Microphone-Amplifier-Interface-Smartphone/dp/B081GK8SVM/ref=as_li_ss_tl?dchild=1&keywords=iphone+guitar+adapter&qid=1586464947&s=musical-instruments&sr=1-16&linkCode=ll1&tag=mmjjg-20&linkId=0cc21e51c13609483b8bc618563f073f&language=en_US) that goes into your computer's audio input. Then, in OBS, set the audio settings to use that audio input instead of your camera or computer's microphone.

Otherwise, you might be able to plug the sound system output directly into your camera's microphone input, assuming your camera has one, and use the camera's audio in OBS.

Finally, if there's only one person who will be talking, you could consider using a wireless lavaliere microphone. I have an [older Audio Technica model](https://www.amazon.com/Audio-Technica-Wireless-Lavalier-Omnidirectional-Microphone/dp/B00006I523/ref=as_li_ss_tl?dchild=1&keywords=audio+technica+wireless+microphone&qid=1586465005&sr=8-11&linkCode=ll1&tag=mmjjg-20&linkId=2eea8eb13a147158ec39ad0f15098ddb&language=en_US), which is good for short distances, but if you need to be moving around a lot in a large space, using a more expensive UHF microphone system would be better. But a UHF wireless microphone system is usually four to five times more expensive!
