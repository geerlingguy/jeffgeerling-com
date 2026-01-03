---
nid: 3201
title: "How to run glmark2-drm to benchmark an external GPU on a Raspberry Pi"
slug: "how-run-glmark2-drm-benchmark-external-gpu-on-raspberry-pi"
date: 2022-04-15T15:33:00+00:00
drupal:
  nid: 3201
  path: /blog/2022/how-run-glmark2-drm-benchmark-external-gpu-on-raspberry-pi
  body_format: markdown
  redirects:
    - /blog/2022/how-run-glmark2-drm-benchmark-opengl-on-raspberry-pi
aliases:
  - /blog/2022/how-run-glmark2-drm-benchmark-opengl-on-raspberry-pi
tags:
  - amd
  - arm64
  - benchmarking
  - glmark2
  - graphics
  - linux
  - radeon
  - raspberry pi
---

Recently I wanted to see whether I could get `glmark2` (an OpenGL 2.0 and ES 2.0 benchmark tool) to run on a Raspberry Pi with an external graphics card (see [this thread](https://github.com/geerlingguy/raspberry-pi-pcie-devices/issues/4)).

But `glmark2` isn't available in any Pi repositories, so you have to build it from source:

```
sudo apt install -y meson libjpeg-dev libdrm-dev libgbm-dev libudev-dev
git clone https://github.com/glmark2/glmark2.git
cd glmark2
meson setup build -Dflavors=drm-gl,drm-glesv2
ninja -C build
sudo ninja -C build install
```

I built this for `drm` only, so it can run fullscreen without any X/Wayland environment. To run the full suite:

```
glmark2-drm
```

Or you can run a specific benchmark like `glmark2-drm -b jellyfish`.

```
pi@radeon10:~ $ glmark2-drm -b buffer
=======================================================
    glmark2 2021.12
=======================================================
    OpenGL Information
    GL_VENDOR:      X.Org
    GL_RENDERER:    AMD CEDAR (DRM 2.50.0 / 5.10.17-v8+, LLVM 11.0.1)
    GL_VERSION:     3.1 Mesa 20.3.5
    Surface Config: buf=32 r=8 g=8 b=8 a=8 depth=24 stencil=0
    Surface Size:   1920x1080 fullscreen
=======================================================
[buffer] <default>: FPS: 29 FrameTime: 34.483 ms
=======================================================
                                  glmark2 Score: 29 
=======================================================
```

On my Raspberry Pi with an AMD Radeon 5450, it's not the best performing setup in the world—half the tests don't run yet—but it's a helpful tool to see if you still need to improve the drivers a bit :)

For comparison, according to [these benchmarks](https://www.mjr19.org.uk/glmark2.html), the 5450 should get around a score of 380. So the Pi's leaving a lot of performance on the table!

Stay tuned to my [YouTube channel](https://www.youtube.com/c/JeffGeerling); I'll be posting an update on external graphics cards on the Raspberry Pi soon!
