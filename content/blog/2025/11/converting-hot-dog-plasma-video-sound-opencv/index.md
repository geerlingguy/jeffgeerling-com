---
nid: 3508
title: "Converting hot dog plasma video to sound with OpenCV"
slug: "converting-hot-dog-plasma-video-sound-opencv"
date: 2025-11-07T16:15:39+00:00
drupal:
  nid: 3508
  path: /blog/2025/converting-hot-dog-plasma-video-sound-opencv
  body_format: markdown
  redirects: []
tags:
  - arduino
  - geerling engineering
  - hot dog
  - opencv
  - plasma
  - python
  - video
  - youtube
---

When you ground a hot dog to an AM radio tower, it generates plasma.

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" autoplay loop muted>
  <source src="./hotdog-am-tower-plasma-compressed.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

While the hot dog's flesh is getting vaporized, a tiny plasma arc moves the air around it back and forth. And because this tower is an AM tower, it uses [_Amplitude_ Modulation](https://en.wikipedia.org/wiki/Amplitude_modulation), where a transmitter changes the amplitude of a carrier wave up and down. Just like a speaker cone moving up and down, the plasma arc from the hot dog turns that modulation into audible sound.

At Open Sauce this year, I met Gavin Free, who I know mostly through his work on [The Slow Mo Guys](https://www.youtube.com/@theslowmoguys) YouTube channel. He was interested in recording various plasma-inducing techniques on the KHOJ-AM radio tower where we had previously filmed [a preliminary hot dog test](https://www.youtube.com/watch?v=GgDxXDV4_hc), and a [follow-up with the Plasma Channel, testing how shorting the tower affects the RF signal propagation](https://www.youtube.com/watch?v=wzDEIBpbLRk).

But a few people left comments speculating whether an audio waveform could be reproduced based on the plasma arcing—using video frames alone. Put another way: could I get slow motion footage to translate the _visual_ plasma arcing into _audible_ sound?

I think so, but since my iPhone only does 240 fps, and I'd need at _least_ 8,000 Hz for discernible sound, I thought I'd never get the chance to test the theory. That is, until Gavin showed up!

He'll post a video with more depth on the plasma and the hot dog, but for the video below, I focused on whether I could extract audio from video frames (without using a microphone).

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/nMF3Plt-mCY" frameborder='0' allowfullscreen></iframe></div>
</div>

## Testing with an LED

To test whether I could potentially recover audio from a light source that gets brighter as the amplitude of the signal increases, I built a little Arduino contraption that blinks an LED brighter in response to an analog audio input, which I plugged my phone's headphone jack into:

{{< figure src="./led-arduino-speaker-phone-test.jpg" alt="Arduino LED blinking to music iPhone test" width="700" height="394" class="insert-image" >}}

The code I used is slightly adapted from Arduino's example sketch for controlling an LED's brightness using a potentiometer. The actual code I used, and the rest of my notes for test setup and video to audio conversion are in a new GitHub project: [Audio from SloMo Video](https://github.com/geerlingguy/audio-from-slow-motion-video).

The project also includes a Python [script that uses OpenCV](https://github.com/geerlingguy/audio-from-slow-motion-video/blob/master/video_to_audio.py) to turn a video into audio waveforms, by converting frame brightness to sound amplitude.

But for my LED test, I cut a black piece of construction paper and placed it behind the LED, turned off the lights in my studio, and set my camera to record in 240 fps HD. And before recording a test clip through the LED, I made the audio clip 40 times slower (this, I hoped, would give me enough frames to work with even at 240 fps, since I needed at least 5-10 KHz for intelligible sound).

{{< figure src="./iphone-recording-led-high-speed-dark-blinking-arduino.jpg" alt="iPhone recording slow motion LED blinking Arduino" width="700" height="394" class="insert-image" >}}

When recording, I locked AF and exposure, and intentionally made focus a bit blurry, to smooth out the LED's overall brightness (otherwise you have a tiny point of light in the middle, and a ring of dimmer brightness surrounding it).

I then processed the slow-motion video:

  1. I pulled the video into Final Cut Pro and adjusted the crop and brightness, to isolate the LED and give as much luminance range as possible.
  2. I ran the video through my Python script, which calculates an average luminance value for each frame using `numpy`, then aggregates the luminance values as audio waveform amplitudes, and outputs a WAV file.
  3. I applied an automatic DC Offset correction using Sound Studio, and normalized the resulting audio clip.
  4. I used `sox` to speed up the audio file (e.g. `speed 0.025`), since I had slowed down the source recording earlier.

And here's what it sounds like:

<figure>
  <figcaption>Source recording:</figcaption>
  <audio controls src="./audio-from-video-led-original.mp3"></audio>
</figure>

<figure>
  <figcaption>After turning LED video back into sound:</figcaption>
  <audio controls src="./audio-from-video-led-processed.mp3"></audio>
</figure>

Not amazing fidelity-wise, but there's intelligible speech, which made me more hopeful with the slow-mo plasma attempt!

## Capturing the slow-motion footage

Disclaimer: _don't try this at home_!

Even though you can never be 100% safe around high-power RF (seriously, don't mess with it, you don't want permanent internal burns that cook you from the inside out!), we mitigated risks by:

  - Working with an antenna engineer familiar with the transmitter power level and phasor setup at this site to determine a 'keep-out' zone, to reduce exposure to RF safety limits established by the FCC (beyond that of the fence, which is where general public exposure limits are reached)
  - Using 10kV-rated insulating gloves and a 7' wooden stick to ground the hot dog to the tower

With safety procedures in place, we tested a number of hot dogs, a corn dog, and new this time, an actual corn cob—which sadly didn't pop corn in a cartoon-like way (apparently [not all corn pops](https://shumwaypopcorn.com/2022/01/can-you-make-popcorn-from-corn-on-the-cob/)).

{{< figure src="./hot-dog-rf-phantom-high-speed-camera-gavin-free-geerling-engineering.jpg" alt="Phantom high speed camera capturing hot dog plasma in slow motion" width="700" height="394" class="insert-image" >}}

One thing I _hadn't_ realized until we were recording was Gavin could only capture about 2 seconds of video at a time, on his [Phantom TMX 7510](https://www.phantomhighspeed.com/products/cameras/tmx) camera. Just two seconds of video, at 40,000 fps, takes up nearly 200 GB of disk space!

That two seconds turns into 1 hour and 48 minutes of runtime, when you play back the giant `.cine` file the camera produces.

So I realized I'd be dealing with two problems:

  1. The LED blinking test clip I did on my iPhone was 5 seconds long. Even under the controlled environment in my studio, I could get a few intelligible words.
  2. Some of the plasma arcing was hidden by the hot dog, since it's a 3D object, unlike the LED, which was flashing light directly into my camera lens.

But we were committed, so we captured a final hot dog clip at 40k fps (to extend the runtime, while providing what I hoped would be an adequate fps to give reproducible sound).

And after I got home, I promptly [deleted all the footage, necessitating a day-long recovery effort](/blog/2025/recovering-videos-my-sony-camera-i-stupidly-deleted).

## Testing with slow-motion footage

This was my first time working with a `.cine` file, and I was happy to see it just opens natively in DaVinci Resolve. Using that program, I exported the entire 1 hour 48 minute video as H.265, just so I'd have an easier time handling it in Final Cut Pro.

I also spent more time than I expected just watching various plasma arcs propagate from the tower to the hot dog. It was fascinating seeing how some arcs would be direct internal arcs on the sacrificial end of the hot dog, and other arcs would jump through hundreds of plasma 'tendrils' all over the skin of the hot dog from a point on the tower up to an inch away!

(This just reinforced my healthy fear of touching anything that is potentially energized with RF—even a 10 watt transmitter, like you'd find in a ham shack, provides significant pain, often with a lasting internal scar!)

To run my brightness script with just the plasma, I applied a luminance key in Final Cut Pro, and exported the video at 480p, since higher resolution isn't really that helpful (and just slows down the OpenCV frame processing).

{{< figure src="./plasma-arcing-video-to-audio.jpg" alt="Plasma arc hot dog video frames to audio processed" width="700" height="394" class="insert-image" >}}

After running it through my script, and post-processing the WAV file, I wound up with this:

<figure>
  <figcaption>Sound derived from AM hot dog RF plasma arcing:</figcaption>
  <audio controls src="./slow-motion-video-to-audio-hotdog-final.mp3"></audio>
</figure>

Because of the real-world problems (only 2s of audio, with much of the plasma occluded by the hot dog), the only obvious bits are in a couple peaks of the transmitted audio. Lined up with the original sound (you can observe it at 8:25 in the video above), it's a tenuous relationship between what I got out of the plasma and the actual sound from the broadcast.

But... I wouldn't call the theory that I can recover audio from hot dog RF plasma arcs _debunked_. Just... more challenging than expected when a hot dog and high-power RF is involved.

There are some other interesting learnings in the video at the start of this post, and if you're interested in this topic and want to dig deeper, check out:

  - The source code used for this testing: [Audio from SlowMo Video](https://github.com/geerlingguy/audio-from-slow-motion-video)
  - Gavin's video on The Slow Mo Guys: [Hot Dog vs Radio Tower at 200,000 FPS](https://www.youtube.com/watch?v=L1c7Nu3iR8c)
