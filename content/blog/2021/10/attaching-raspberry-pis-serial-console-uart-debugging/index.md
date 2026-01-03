---
nid: 3130
title: "Attaching to a Raspberry Pi's Serial Console (UART) for debugging"
slug: "attaching-raspberry-pis-serial-console-uart-debugging"
date: 2021-10-01T15:54:42+00:00
drupal:
  nid: 3130
  path: /blog/2021/attaching-raspberry-pis-serial-console-uart-debugging
  body_format: markdown
  redirects:
    - /blog/2021/attaching-raspberry-pis-serial-console-debugging
aliases:
  - /blog/2021/attaching-raspberry-pis-serial-console-debugging
tags:
  - adafruit
  - console
  - debugging
  - raspberry pi
  - serial
  - uart
---

Sometimes a Pi just won't boot. Or it'll boot, but it'll do weird things. Or you don't have an HDMI display, and you can't log into your Pi via SSH. Or maybe you're like me, and [someone 'accidentally' cut your Raspberry Pi in half](https://www.youtube.com/watch?v=Gai_w3uCtIM), and you want to see what it's doing since it won't boot anymore.

{{< figure src="./raspberry-pi-debug-uart.jpeg" alt="Raspberry Pi with UART Serial Console Debug cable connected" width="600" height="353" class="insert-image" >}}

The Raspberry Pi can output information over a 'serial console', technically known as a UART (Universal Asynchronous Receiver/Transmitter). Many devices—including things like storage controller cards, which in a sense run their own internal operating system on an SoC—have a 'UART header', which is typically three or four pins that can connect over the RS-232 standard (though many do not operate at 12v like a traditional serial port! Use a USB-to-TTL adapter like the one I mention below).

[Simply Embedded has a great overview of UART](http://www.simplyembedded.org/tutorials/msp430-uart/) if you want to learn more.

If you want to access the Pi's serial console, here's what you need to do:

  1. Buy a USB to serial adapter. I bought the [Adafruit 954 USB-to-TTL Serial Cable](https://amzn.to/3utU4Dp).
  2. Pop the Pi's microSD card into another computer, edit the `config.txt` file inside the `boot` volume, and add the following line at the bottom: `enable_uart=1`.
  3. Save that change, eject the microSD card, and stick the card back into the Pi.
  4. Plug the USB to serial adapter into the pins as pictured below on the Pi (Black to GND, White to GPIO 14/pin 8 (UART TX), and Green to GPIO 15/pin 10 (UART RX)):

     {{< figure src="./raspberry-pi-serial-cable-connection.png" alt="Raspberry Pi Serial Connection with Adafruit USB to TTL Adapter" width="611" height="397" class="insert-image" >}}

  5. Open a terminal window on your Mac, and run `ls /dev | grep usb`
  6. Note the `tty.usbserial-` and `cu.usbserial-` numbers in there. That's the device you'll connect to on your Mac.

There are a number of ways to interact with the serial console on a Mac (and most are the same as on Linux, with sometimes minor usage differences), but the two I've used in the past are `minicom` and `screen`.

## Use CoolTerm

Sometimes if I'm doing a lot of debugging, I like to use a good serial terminal GUI, and my favorite is [CoolTerm](http://freeware.the-meiers.org). It has a quasi-intuitive GUI interface for any kind of serial terminal viewing.

In its options, select the `/dev/tty.usbserial-0001` device, and then click 'Connect'.

## Use `minicom`

  1. Install minicom (`brew install minicom`) so you can emulate a terminal connected over serial.
  2. Run `minicom -b 115200 -D /dev/tty.usbserial-0001`
  3. Boot the Pi.
  4. Within a few seconds, you should see data in your session.

Note: In `minicom`, the `Meta` key is mapped to 'Esc' by default, at least on macOS. So press 'Esc-Z' to get help. Additionally, if you're attaching to a device using `minicom` _running on the Pi_, you have to press Enter, then Ctrl-A, then Q, and Enter again to exit minicom. Fun!

## Use `screen`

  1. Run `screen /dev/tty.usbserial-0001 115200`
  2. Boot the Pi.
  3. Within a few seconds, you should see data in your session.

Note: To exit the `screen` session, press Ctrl-A, then Ctrl-K, and confirm you want to exit.

{{< figure src="./screen-debug-uart.gif" alt="Debugging session in screen on macOS via Serial Console" width="600" height="316" class="insert-image" >}}

See also: [Adafruit's guide to using a serial console on the Pi](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/test-and-configure).

I've done this process a few times in the past, but I've grown tired of looking back at old notes to remember specifically which pins to use on the GPIO, since I don't do it that often and the pins are unlabeled on most Pis. Hope this helped!

> Update: I also forgot to mention—it's possible to get output from the Pi's own _bootloader_ (at an even earlier stage) using the `BOOT_UART` option supplied to a custom EEPROM build; see [cleverca22's post in the Pi Forums](https://forums.raspberrypi.com/viewtopic.php?f=63&t=320462#p1919044) for details.
