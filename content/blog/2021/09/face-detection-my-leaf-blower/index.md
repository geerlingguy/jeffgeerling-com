---
nid: 3128
title: "Face detection for my leaf blower"
slug: "face-detection-my-leaf-blower"
date: 2021-09-29T14:01:11+00:00
drupal:
  nid: 3128
  path: /blog/2021/face-detection-my-leaf-blower
  body_format: markdown
  redirects: []
tags:
  - cm4
  - compute module
  - facial recognition
  - hq camera
  - imutils
  - opencv
  - python
  - raspberry pi
  - video
  - youtube
---

In the class of 'out there' projects, I recently added a little AI to my leaf blower:

{{< figure src="./leaf-blower-with-raspberry-pi-on-top.jpeg" alt="Leaf blower with Raspberry Pi on top for AI ML Machine Vision blasting" width="600" height="498" class="insert-image" >}}

The short of it: I have a face detection algorithm running which, when a certain individual enters the field of the Pi's vision, triggers a servo that powers on the blower, releasing a powerful air blast.

{{< figure src="./rsj-air-blaster.gif" alt="Red Shirt Jeff gets blasted by air cannon" width="640" height="336" class="insert-image" >}}

I've been wanting to play around with face detection on the Pi for some time, but the Pi Zero I use in most of my camera projects is seriously underpowered for this kind of work.

## CM4Ext Nano

So when Harlab (Hardware Laboratory) told me they'd like to send me a [CM4Ext Nano](https://github.com/harlab/CM4Ext_Nano) board for testing, I thought it'd be the perfect opportunity to play with machine vision on the Pi.

Instead of the anemic 1 GHz BCM2835 processor in the Zero, I could pop in a CM4 with a _much_ faster multicore BCM2711.

The CM4Ext Nano also offers a lot of IO in such a tiny package—including two HDMI display ports!

{{< figure src="./cm4ext-nano.jpeg" alt="Harlab CM4Ext Nano" width="600" height="418" class="insert-image" >}}

It comes with a kit of screws and a spacer board for the HQ camera, so you can mount everything into a very petite package:

{{< figure src="./cm4ext-nano-raspberry-pi-compute-module-4-hq-camera.jpeg" alt="CM4Ext Nano with Raspberry Pi Compute Module 4 and HQ Camera" width="600" height="400" class="insert-image" >}}

With the Pi hardware put together, I just needed some software to train the Pi to recognize someone, then monitor the camera feed, and trigger a servo once that person was detected.

## Software

The first step was to get the camera to actually work via the CSI connector; on the Compute Module 4 (unlike most other Pi models), you have to manually download a device tree file to enable the camera.

Instructions for doing that are outlined on the Raspberry Pi Documentation site: [Compute Module 4 Camera Module guide](https://www.raspberrypi.org/documentation/computers/compute-module.html#quickstart-guide).

### Machine Vision with OpenCV

This was my first time messing around with machine vision and image-based training, and I leaned heavily on the code and example from [this Tom's Hardware post from Caroline Dunn](https://www.tomshardware.com/how-to/raspberry-pi-face-mask-detector).

Contrary to that post's instructions, you don't need to compile everything from scratch—the required libraries can be installed on a freshly-imaged Raspberry Pi with three commands:

```
# Install OpenCV dependencies.
$ sudo apt-get install -y libatlas-base-dev

# Install OpenCV and face recognition libraries.
$ sudo pip3 install opencv-python face-recognition imutils

# I had to do this due to a numpy import error with OpenCV.
$ sudo pip3 install --force-reinstall numpy
```

After that, it's a matter of training and using a model for face detection. I posted my code in [my fork of Caroline Dunn's facial_recognition project](https://github.com/geerlingguy/facial_recognition).

> Note: Some people may want to compile OpenCV from scratch to unlock as much performance as possible on the Pi—and I admit I haven't had time yet to properly benchmark the different installation methods. YMMV.

To train the model:

1. Grab a bunch of images that clearly shows a person's face in a folder named for that person in the `dataset` directory.
2. Run `python3 train_model.py`, and wait for the `.pickle` file to be generated with the information required.

Once training is done, run the image recognition via:

```
python3 facial_recognition.py
```

A window with the camera feed will open up. You may notice it only runs around 2-3 fps on the Compute Module 4—I believe it can be optimized further to either run threaded (it looks like it's only using one core with the current code), or offload some of the work to Pi's GPU.

A Coral TPU could also help with software like this, and some people have been able to get USB 2 and USB 3 Coral TPU models working, but I am still holding out hope that the drivers can be made to work with the Coral TPU on the PCI Express bus directly—this would allow for simpler, faster Pi AI/ML CM4 builds without an extra USB 3.0 bus.

Anyways, here's a sample of what the performance looks like on my CM4:

{{< figure src="./raspberry-pi-facial-recognition-jeff-box-face.gif" alt="Jeff entering door while Raspberry Pi identifies his face" width="640" height="480" class="insert-image" >}}

The AI-powered leaf blower is not a very practical intruder deterrent, but it was fun to build, and was the primary subject in a video I made to highlight the CM4Ext Nano—and to get revenge on Red Shirt Jeff for [cutting my Raspberry Pi 4 model B in half](TODO)! Here's that video:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Gai_w3uCtIM" frameborder='0' allowfullscreen></iframe></div>
</div>
