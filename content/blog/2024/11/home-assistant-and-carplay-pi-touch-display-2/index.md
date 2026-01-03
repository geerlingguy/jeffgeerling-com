---
nid: 3416
title: "Home Assistant and CarPlay with the Pi Touch Display 2"
slug: "home-assistant-and-carplay-pi-touch-display-2"
date: 2024-11-08T15:01:32+00:00
drupal:
  nid: 3416
  path: /blog/2024/home-assistant-and-carplay-pi-touch-display-2
  body_format: markdown
  redirects:
    - /blog/2024/pi-touch-display-home-assistant-compact-smart-home-controller
    - /blog/2024/build-home-assistant-dashboard-new-pi-touch-display
aliases:
  - /blog/2024/pi-touch-display-home-assistant-compact-smart-home-controller
  - /blog/2024/build-home-assistant-dashboard-new-pi-touch-display
tags:
  - alexa
  - home assistant
  - raspberry pi
  - screen
  - smart home
  - touch
  - video
  - youtube
---

After a decade, Raspberry Pi [finally upgraded their official Touch Display](https://www.raspberrypi.com/news/raspberry-pi-touch-display-2-on-sale-now-at-60/) from 480p to 720p, while keeping the price and overall aesthetic the same.

{{< figure src="./pi-touch-display-2-home-assistant-dashboard.jpeg" alt="Raspberry Pi Touch Display 2 - Home Assistant Dashboard" width="700" height="auto" class="insert-image" >}}

I've had early access to the Touch Display 2, and have been testing it in a variety of scenarios. Generally, Linux touchscreen support isn't wonderful. And Pi OS, being a fairly customized UI focused on simple use cases, is not quite to a usable state if you go touchscreen-only, considering I had trouble getting the onscreen keyboard to work in Chromium half the time, and it would overlay things I was typing even in fully-supported apps like Terminal.

But that software can and will be improved. I've had two projects on the backburner for some time, and once I received the Touch Display 2, I thought it was finally time to give them a go. I wanted to see how well these ideas would work out on the Pi 5:

  - An always-on Home Assistant smart home control panel
  - CarPlay to replace the old AM/FM radio and CD player in my 2007 Toyota Camry

I have almost everything for the first project done, and documented in my [Raspberry Pi Kiosk project](https://github.com/geerlingguy/pi-kiosk) on GitHub. I'm still working on the CarPlay setup, but the software side is already pretty solid—I'll get to where I'm at later in this post.

If you'd like to see a video with all these things demoed in a less static way, I have a short video on my YouTube channel, you can watch it below:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/gpyYCTgJO88" frameborder='0' allowfullscreen></iframe></div>
</div>

First things first, I needed a way to secure the Touch Display so the Raspberry Pi wasn't just bare, sitting upside-down on my desktop! I found a [ton of 'Pi Touch Display' enclosures on Printables](https://www.printables.com/search/models?q=pi+touch+screen), but almost _anything_ designed for the original Touch Display won't work for the updated version, because the mounting holes and some of the metal enclosure are in a different location (even if the overall outer glass dimensions are the same).

So I quickly designed and printed some 'legs' to screw in on either side of the Touch Display 2—using the screws included with the display—and hold it in a landscape orientation:

{{< figure src="./pi-touch-display-rear-stand-3d-printed.jpeg" alt="Raspberry Pi Touch Display 2 - custom 3D printed legs" width="700" height="auto" class="insert-image" >}}

You can find my [Pi Touch Display 2 3D printable stand](https://www.printables.com/model/1062445-raspberry-pi-touch-display-2-stand) on Printables.

## Pi OS Touch Display 2 Configuration

There are a few things you can do in Pi OS install to get it working nicely with the Touch Display 2:

  - Use the Screen Configuration app to rotate the display or change it's brightness.
  - In the CLI, you can rotate the display output with `wlr-randr --output DSI-1 --transform 90`, or save the setting inside `~/.config/kanshi/config`.
  - Also in the CLI, you can change brightness, setting a level between `1-31` with the command `echo [VALUE] | sudo tee /sys/class/backlight/6-0045/brightness` (note: the number in that command will vary based on your setup)
  - Switch between light and dark mode by right-clicking on the desktop and entering into the Display Preferences. I'm not sure how to right-click just using the touchscreen though...

...which brings me to how I manage the Pi remotely, since not everything can be done using the touch UI, and plugging in a keyboard and mouse can be annoying.

I either connect via [Raspberry Pi Connect](https://connect.raspberrypi.com/), or via SSH if I'm on my local network. Then I can run Terminal commands or do things like right-click or scroll around more easily.

## Setting up a Home Assistant Kiosk with a Pi

Once I had my screen rotated the right way, I created a new open source project, [Raspberry Pi Kiosk](https://github.com/geerlingguy/pi-kiosk), which has a shell script and a systemd service file.

You copy the included shell script [`kiosk.sh`](https://github.com/geerlingguy/pi-kiosk/blob/master/kiosk.sh) into a folder inside your home folder, then copy the [`kiosk.service`](https://github.com/geerlingguy/pi-kiosk/blob/master/kiosk.service) file into `/lib/systemd/system/kiosk.service`, and run `sudo systemctl enable kiosk.service`.

After a reboot, Chromium should automatically launch into `--kiosk` mode, opening the URL configured inside `kiosk.sh`.

Since Home Assistant is already fairly touchscreen-friendly, and my own dashboards are designed to fit everything on the screen without scrolling, touch targets are easy enough to use without worrying about Linux/Pi OS's touch tomfoolery.

## Setting up CarPlay with a Pi

My stretch goal was to see if I could get the Touch Display 2 set up as a CarPlay display in my 2007 Toyota Camry.

I bought all the hardware I needed:

  - Raspberry Pi 5 + Touch Display 2 + microSD card
  - [Carlinkit CPC200-CCPA CarPlay adapter](https://amzn.to/3Csksp0)
  - [DC 12V step-down converter to 5V 5A USB-C](https://amzn.to/48Cc5U9)

And then I got to work on the software. After initially hitting a roadblock where [`react-carplay` wouldn't recognize my Carlinkit](https://github.com/rhysmorgan134/react-carplay/issues/76), I eventually got CarPlay fully working, including audio in and out!

{{< figure src="./raspberry-pi-touch-display-2-carlinkit-carplay.jpg" alt="CarPlay with Carlinkit and react-carplay on the Pi 5 and Touch Display 2" width="700" height="auto" class="insert-image" >}}

I was excited to move my setup into the car, but ran into two roadblocks:

  - **Time**: I had already spent an afternoon debugging the `react-carplay` issue, so that ate into the other time I had allocated to getting a quick and dirty mounting solution for the car.
  - **Temperature**: The [Touch Display 2 Product Brief](https://datasheets.raspberrypi.com/display/touch-display-2-product-brief.pdf) states "This device should be operated in a dry environment at 0–50°C". My car can get up to 51 or 52°C in the summer. And -20°C in the winter! I might have to scrap the idea of using _this_ display for my CarPlay head unit replacement. But maybe not, I'm willing to sacrifice $60 to see if it'll work well enough in the extremes :)

I've also yet to settle on what kind of microphone I'd use with my setup. I plan on using a cheap USB audio adapter with a mic input and speaker output, but I'm certain there's a good USB microphone for car use out there... right?

## Conclusion

The Touch Display 2 is a reasonable upgrade over the original Touch Display. It will not win any awards for screen quality, smudge resistance, robustness, etc... but it's _good enough_ for tinkering and simple projects requiring a touchscreen.

For the time being, mine is set up at my desk and I've been using it to control things via Home Assistant. It's also nice to switch to my surveillance tab and check on camera feeds at my studio. I still hope to test it in the car, too; maybe a torture test to see how well it holds up over a winter!
