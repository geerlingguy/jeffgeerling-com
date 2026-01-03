---
nid: 3069
title: "The Raspberry Pi Pico is a new $4 microcontroller"
slug: "raspberry-pi-pico-new-4-microcontroller"
date: 2021-01-21T07:00:32+00:00
drupal:
  nid: 3069
  path: /blog/2021/raspberry-pi-pico-new-4-microcontroller
  body_format: markdown
  redirects: []
tags:
  - arduino
  - electronics
  - microcontroller
  - pico
  - raspberry pi
---

{{< figure src="./raspberry-pi-pico-development-setup.jpeg" alt="Raspberry Pi Pico on breadboard" width="600" height="392" class="insert-image" >}}

**tl;dr**: The [Raspberry Pi Pico](https://rptl.io/pico) is a new $4 microcontroller board with a custom new dual-core 133 MHz ARM Cortex-M0+ microprocessor, 2MB of built-in flash memory, 26 GPIO pins, an assortment of SPI, I2C, UART, ADC, PWM, and PIO channels.

It also has a few other party tricks, like [edge castellations](https://learn.sparkfun.com/tutorials/how-to-solder-castellated-mounting-holes/all) that make it easier to solder the Pico to other boards.

The Pico is powered by a new RP2040 chip—a brand new Raspberry-Pi-built ARM processor. And the best thing about this processor is the insanely-detailed Datasheet available on the Pico website that steps through every bit of the chip's architecture.

## Video Review and 'Baby Safe Temperature' Project

I posted an entire video reviewing the Pico and demonstrating a MicroPython project. The video is embedded below:

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/dUCgYXF01Do" frameborder='0' allowfullscreen></iframe></div>

## Compared to other microcontrollers

When I saw the Pico, I thought immediately of the [Teensy LC](https://www.pjrc.com/teensy/teensyLC.html) that's almost identical in size, and also has an ARM M0 processor, but 3x, with a single core, and a lot less flash storage.

The going rate for a Teensy LC is $8, twice the Pico.

There's also the [ESP32](http://esp32.net), but a full package like the Pico offers costs $10-20.

Obviously wireless capabilities on the ESP32 aren't present on the Pico, so you have to discount that in the price, but it is a lot less money for any project that doesn't require WiFi or Bluetooth.

Finally, there's also the [Pro Micro](https://www.sparkfun.com/products/12640), but it offers a different set of tradeoffs and a way slower clock speed than the Pico, and it also costs $10 or more most places online!

Anyways, here are the specs of the Raspberry Pi Pico:

  - It has an RP2040 microcontroller with 2 megabytes of flash storage
    - The processor runs up to 133 MHz, and is based around a dual-core Cortex M0+ design
    - The processor also has 264 KB of SRAM
    - The processor has 2 UART, 2 I2C, 2 SPI, and up to 16 PWM channels
    - The processor includes a timer with 4 alarms and a real time counter, as well as dual Programmable IO peripherals
  - It uses a Micro USB port for power and data, and for programming the flash
  - 40 pins are both through-hole and castellated for mounting flexibility
    - There are 26 3.3V GPIO pins
    - 23 of the GPIO pins are digital-only, and 3 are ADC capable
  - It has a 3-pin ARM Serial Wire Debug port
  - And finally, it can be powered via micro USB or a dedicated power supply or battery

### Programming the Pico and writing to the Flash memory

The easiest way to get started with the Pico is to hold down the BOOTSEL button on it while you plug it into a computer. It will be mounted as a Mass Storage Device!

{{< figure src="./thonny-screenshot.jpg" alt="Thonny Python IDE with Raspberry Pi Pico" width="700" height="394" class="insert-image" >}}

To program the Pico with MicroPython, you can use the [Thonny Python IDE](https://thonny.org) that's already built into Raspberry Pi OS, or you can install it on any Mac, Windows, or Linux PC.

Before you can run MicroPython code, though, you need to follow the instructions on the Pico Getting Started Guide to download a UF2 file that will install MicroPython on the Pico and reboot it. After that, the Pico will automatically run whatever's stored in `main.py` on the Pico's filesystem when it boots up.

There's an entire book, [Get started with MicroPython on Raspberry Pi Pico](TODO: Add link) available through the Pico website, and I highly recommend it!

### Power Consumption

Now that we know a bit about the Pico itself, and how to program it, I need to explain when I'd use a microcontroller instead of a full computer like a Raspberry Pi with it's GPIO pins. For me, the main reason is usually power consumption.

I've done [a LOT of power testing for my Raspberry Pi projects](http://www.pidramble.com/wiki/benchmarks/power-consumption). Typically I measure power consumption in Amps and Watts, though there are a few Pi models, like the Model A+ and Zero, that sip only a few hundred milliamps when running at 5V, which translates into 1 to 2 W.

Well, when we talk about microcontrollers like the RP2040 on the Pico, power efficiency on a different planet. In sleep or dormant mode, the Pico consumes less than 2 _milliamps_, or 6 _milliwatts_! That's .006 W!

And even when it's running full tilt, doing graphics rendering, it uses less than 100 milliamps, or .33 watts.

If you program it efficiently, you can run the Pico off a small rechargeable battery for days or even _weeks_!

## Conclusion

{{< figure src="./pico-top.jpeg" alt="Raspberry Pi Pico Top" width="600" height="401" class="insert-image" >}}

One of the things I _don't_ like about the Pico's design is the lack of pin labels on the top of the device.

{{< figure src="./pico-bottom.jpeg" alt="Raspberry Pi Pico Bottom" width="600" height="401" class="insert-image" >}}

They're all labeled nicely on the bottom, but only pins 1, 2, and 39 are labeled on the top.

There's no way to see which pin is which when I have it plugged into a breadboard. It would be nice if the Pi Foundation could silkscreen labels on top somehow, maybe like the Teensy does it, with little angled labels:

{{< figure src="./teensy41_4.jpg" alt="Teensy 4.1" width="379" height="112" class="insert-image" >}}

Other than that, there's not much downside to the Pico. I mean, having two cores may be nice for some projects, but most of my own work wouldn't benefit from dealing with the complexity of multiple threads in software. But that's not really a _bad thing_.

All-in-all, I think the Pi Foundation has a winner with their new $4 microcontroller board, and I can't _wait_ to see what other people come out with based on the RP2040.

You can get a Pico from any of Raspberry Pi's authorized resellers, and I really hope the Pi Foundation can keep up with demand. It would be really sad if they're hard to find months after launch, like [what's happened with the Compute Module 4](https://www.youtube.com/watch?v=ZZ2ub2RZ0o8)!

One other thing I want to see is a full getting started kit, like you can find for the Arduino. I'm sure some companies will be putting these together.

Anyways, for more details, and a hands-on project, check out my video: [The Raspberry Pi Pico Review - $4 ARM Microcontroller](https://www.youtube.com/watch?v=dUCgYXF01Do)
