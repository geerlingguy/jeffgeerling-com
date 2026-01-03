---
nid: 3459
title: "It's easier than ever to de-censor videos"
slug: "its-easier-ever-de-censor-videos"
date: 2025-04-15T17:00:33+00:00
drupal:
  nid: 3459
  path: /blog/2025/its-easier-ever-de-censor-videos
  body_format: markdown
  redirects: []
tags: []
---

Last month I asked people to [hack part of my YouTube video](https://youtu.be/gaV-O6NPWrI?t=297), specifically to de-pixelate the contents of a folder I had pixelated starting at the 4:57 mark.

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" controls>
  <source src="./depixelate-original-video-ezgif.com-mute-video.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

For years, people have used the censor tool to blur or pixelate out parts of videos where there's sensitive information. And for years, every time I've used it, I get a few comments from people saying that's not a safe way to censor information.

So is that true?

I wanted to find out, so I put a message saying I'd send fifty bucks to anyone who could tell me what it said under the pixelation. And you know what? Less than a day later, _three_ people solved it, using three slightly different techniques—scary!

This blog post is a lightly edited transcript of the following video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/acKYYwcxpGk" frameborder='0' allowfullscreen></iframe></div>
</div>

## How did they do it?

But how did they do it? I asked each of them, and they were more than happy to share. For most of us who like reverse-engineering or tinkering, it's fun to share the craft. And even more fun when it's _sanctioned_ fun. Add on a little monetary reward, and that's just icing on the cake.

GitHub user KoKuToru was kind enough to share [an entire GitHub repo](https://github.com/KoKuToru/de-pixelate_gaV-O6NPWrI) with the process and the code, along with two different ways that user tried to depixlate my footage.

First a [brute-force attempt](https://github.com/KoKuToru/de-pixelate_gaV-O6NPWrI/tree/master/v1) to extract aligned images of just the window, with some code using TensorFlow to extract pixel data and aggregate it into a somewhat-fuzzy (but almost clear enough to read) picture:

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" controls>
  <source src="./depixelate-v1-result.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

The idea here is the pixelation is kind of like shutters over a picture. As you move the image beneath, you can peek into different parts of the picture. As long as you have a solid frame of reference, like the window that stays the same size, you can 'accumulate' pixel data from the picture underneath.

Due to the slight error in selecting the window by hand, the final result was slightly blotchy. For the second attempt, GIMP was used to get a better window selection algorithm with ffmpeg, and with a slight bit more data (more frames extracted), a perfectly legible result:

<div style="text-align: center;">
<video style="max-width: 95%; width: 640px; height: auto;" controls>
  <source src="./depixelate-v2-result.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
</div>

## Any way to prevent it?

Blurring or pixelating video, especially _moving_ video, may lead to similar results as you saw here. Years ago it would've required a supercomputer and a PhD to do this stuff. But today, between AI assistance with the trickier bits of coding, and how fast neural networks run on computers, it's easier and faster than ever to de-pixelate video!

If there's one thing computers are good at, it's finding order in seeming chaos, like how modern tools can [pull a clean voice out of a horrible recording](https://www.youtube.com/watch?v=7msuhEq1Vz4).

The more motion in the video, the more data points the reverse engineering has to play with. And thus, the better the confidence in the results.

If I _hadn't_ moved around my Finder window in the video, I don't think it would've worked. You might get a couple letters right, but it would be very low confidence.

Moving forward, if I _do_ have sensitive data to hide, I'll place a pure-color mask over the area, instead of a blur or pixelation effect.

Intuitively, blur might do better than pixelation... but that might just be my own monkey brain talking. I'd love to hear more in the comments if you've dealt with that kind of image processing in the past.

It's amazing what people can do with a neural network, ingenuity, and time.

I guess the moral of the story is _if you don't want people to read censored data... don't post it online_.

tl;dr - check out [KoKoToru's de-pixelate GitHub repo for all the details on how it was done](https://github.com/KoKuToru/de-pixelate_gaV-O6NPWrI/tree/master/v1).
