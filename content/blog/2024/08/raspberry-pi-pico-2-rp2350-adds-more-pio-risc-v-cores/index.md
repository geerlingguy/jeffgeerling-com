---
nid: 3398
title: "Raspberry Pi Pico 2 - RP2350 adds more PIO, RISC-V cores"
slug: "raspberry-pi-pico-2-rp2350-adds-more-pio-risc-v-cores"
date: 2024-08-08T15:04:29+00:00
drupal:
  nid: 3398
  path: /blog/2024/raspberry-pi-pico-2-rp2350-adds-more-pio-risc-v-cores
  body_format: markdown
  redirects: []
tags:
  - microcontroller
  - pico
  - pio
  - raspberry pi
  - rp2040
  - rp2350
  - video
  - youtube
---

{{< figure src="./raspberry-pi-pico-2.jpeg" alt="Pico 2 Logo" width="700" height="auto" class="insert-image" >}}

The [$5 Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/) was announced today, with a new chip, the [RP2350](https://www.raspberrypi.com/products/rp2350/). This silicon improves on almost every aspect of the RP2040:

  - 3 PIOs instead of 2
  - 150 MHz instead of 133 MHz base clock
  - Faster Arm Cortex M33 cores _and_ RISC-V Hazard3 cores

I've had access to pre-release hardware and good news: even though the new chip is faster and has more features, it actually uses _less_ power than RP2040, meaning if you run one of these things off a battery, it'll last longer.

I'll talk more about power later, but first, here's the specs.

{{< figure src="./pico-pico-2-side-by-side.jpeg" alt="Pico 2 and Pico side by side comparison" width="700" height="auto" class="insert-image" >}}

The layout is nearly identical. It has the same castellated edges, so you can solder the board down onto your project. The top has the same `BOOTSEL` button, micro USB port, and LED. And the chip is the same size and pinout. The bottom is identical except there's one extra test pad in the middle of the board. So the Pico 2 is a drop-in replacement, and the RP2350 chip on top is _almost_ a drop-in replacement for the RP2040 (it has 4 more pins, and a slightly adjusted pinout).

But now we'll get to the differences:

  - This chip has a faster base clock, 150 MHz, and I haven't tested overclocking it yet, but it should be easy to do that. 
  - PIO, or Programmable I/O, lets you build your own communication interfaces using GPIO pins, and the RP2350 adds an extra PIO interface—so now there are 3 PIOs with 12 state machines.
  - The Pico had 2 Arm Cortex M0+ cores, and the Pico 2 upgrades to 2 Cortex-M33. _And_ it adds on two Hazard3 RISC-V cores. (More on how that works, later.)
  - The Pico 2 doubles the original Pico's SRAM from 264 to 520 kiB.
  - The Pico consumed around 100 mW at idle, the Pico 2 only about 80.
  - The RP2040 came in one package size, with 4 ADCs and 30 total GPIO pins. The RP2350 comes in two package sizes, and the bigger one has _48_ GPIO pins.
  - The RP2350 includes 8 kiB of OTP (One-Time Programmable) storage
  - The RP2350 ships in variants including built-in flash (saving on your BoM if you're building a custom project integrating the RP2350).
  - The Pico 2 is $1 more expensive than the original Pico ($5 vs $4), and I'm guessing other variants will adjust their pricing similarly.

There's a lot more in the datasheet I can't cover here, but the fact is, Raspberry Pi's improved every aspect of their first chip, which is _still_ very popular, and they solved some of the most annoying problems people had with it.

{{< figure src="./rp2350-microcontroller-pico-2.jpeg" alt="Raspberry Pi RP2350A0A2" width="700" height="auto" class="insert-image" >}}

Maintaining the same Pico form factor and base RP2040 footprint means you can quickly upgrade your projects to the newer hardware, assuming you adjust your software.

## Pico Projects

And that's a wise decision, as it allows the huge ecosystem of RP2040-based projects to carry on in the Pi ecosystem with minimal disruption.

{{< figure src="./picoboy-v2.jpg" alt="PicoBoy V2" width="700" height="auto" class="insert-image" >}}

There are _thousands_ of projects out there that already made good use of RP2040. Like the [PicoBoy V2](https://github.com/HalloSpaceBoy5/PicoBoy)—as chance would have it, I was contacted by HalloSpaceBoy5 last week, asking if I'd like to take a look at it.

It's a custom handheld console built on the RP2040, with Python ports of classic games like Breakout, Pac Man, Space Invaders, and Flappy Bird. Okay, well that last one isn't quite a classic...

But this is just one of the many projects that caught my eye over the past year:

There's a mod chip for the Nintendo Switch called the [PicoFly](https://www.youtube.com/watch?v=hkCV2Kcy7z4), Pimoroni makes their own gamepad called the [PicoSystem](https://shop.pimoroni.com/products/picosystem?variant=32369546985555), and of course, the Pico runs DOOM... [on a LEGO brick!](https://www.youtube.com/watch?v=oVG5g6zOnjo).

But games are one thing, someone built a [Logic Analyzer](https://github.com/gusmanb/logicanalyzer), a [portable serial terminal](https://github.com/ncrawforth/VT2040), and even a full SDR receiver called [PiccoloSDR](https://www.youtube.com/watch?v=okIkjC02J_M)!

There's even a rackmount monitor for homelabs and businesses called [Axe Effect](https://www.craftcomputing.com/product/axe-effect-temperature-sensor-beta-/1?cp=true&sa=true&sbp=false&q=false), made by YouTuber [Craft Computing](https://www.youtube.com/channel/UCp3yVOm6A55nx65STpm3tXQ)—I've yet to test the beta unit Jeff sent me (sorry about that!).

Retro enthusiasts are all over the RP2040, I've seen it used to [build custom N64 flash carts](https://twitter.com/kbeckmann/status/1539738410063208454), [emulate a full classic Macintosh](https://www.youtube.com/watch?v=G3bW4f5Gn4o), and almost everyone with one of these old Macs has a [BlueSCSI v2](https://jcm-1.com/product/bluescsi-v2-50-pin-desktop/) to emulate hard drives and CD-ROMs.

Then there's the [ISA Blaster](https://www.youtube.com/watch?v=8HuxukpbsAE), and the [ZX Spectrum emulator](https://github.com/antirez/zx2040)...

And that's before we get into places where you might never notice there's an RP2040 unless you look closely. Like the [MNT reform I tested early this year](/blog/2024/mnt-reform-hackable-laptop-not-everyone), the trackball is run on a 2040. And the [Radxa X4](https://docs.radxa.com/en/x/x4) marries an RP2040 to an Intel N100 for the first SBC with Intel + Arm microcontroller for GPIO. I've been [testing the X4](https://github.com/geerlingguy/sbc-reviews/issues/48) and will post more on it later.

Raspberry Pi knocked the RP2040 and the original Pico out of the park. I don't think anyone could've predicted how popular it would become. It introduced the world of microcontrollers to a lot of people who never got into them before, myself included.

But it wasn't without its flaws: one of the main ones was power consumption.

## Power

{{< figure src="./pico-2-4mA-current.jpg" alt="Pico 2 Power measurements" width="700" height="auto" class="insert-image" >}}

RP2040 doesn't really do a deep sleep down to the µA range—the best I could find is [around 1 mA](https://forum.core-electronics.com.au/t/pi-pico-sleep-dormant-states/12584/5). My own tests with MicroPython shows the Pi going down to 2 mA.

The RP2040's way better than a full Pi running Linux, of course, but in microcontroller-land, milliamps aren't impressive. Like [this ESP32 can get down to _5 µA_](https://youtu.be/HmXfyLyN38c?t=529) in deep sleep. That means battery life could be measured in _months_ instead of days or weeks. Is the Pico 2 better than the Pico?

Here are my informal test results:

| State | Pico | Pico 2 |
| --- | --- | --- |
| Idle, base clock | 20 mA (100 mW) | 16 mA (80 mW) |
| MicroPython `lightsleep` state | 2 mA (10 mW) | 4 mA (20 mW)* |
| MicroPython `deepsleep` state | N/A | DNF |

The sleep states... well, let's just say I'm still a noob at C (so I couldn't get the `hello_sleep.c` code ported to Pico 2 in time for this post), and the MicroPython build I had seemed to flake out when messing with sleep states.

So I'll post a follow-up when I can get more power testing in. For MicroPython, I've opened up [one issue for `machine.lightsleep()`](https://github.com/micropython/micropython/issues/15622), and [another for `machine.deepsleep()`](https://github.com/micropython/micropython/issues/15623). For now, I'll refer you to the RP2350 datasheet, which states:

> Extended low-power sleep states with optional SRAM retention: **as low as 10 μA DVDD**

_Realistically_, my guess is we'll see somewhere between 10-100 μA, but looking at the SDK, it seems like it won't take as much effort to get the RP2350 into a dormant state (and to wake it back up, e.g. for periodic sensors—_without_ an external trigger).

## Pi goes RISC-V

Screenshot of Hazard3 RISC-V core layout from [bitlog.it's RISC-V CPU Core ASIC roundup](https://bitlog.it/20220118_asic_roundup_of_open_source_riscv_cpu_cores.html#hazard3-rv32i--m-c-a-zicsr-zba-zbb-zbc-zbs):

{{< figure src="./hazard3-core-layout-bitlog.it_.jpg" alt="RISC-V Hazard3 core rendering" width="700" height="auto" class="insert-image" >}}

The other headline feature is the inclusion of [two Hazard3 RISC-V cores](https://bitlog.it/20220118_asic_roundup_of_open_source_riscv_cpu_cores.html#hazard3-rv32i--m-c-a-zicsr-zba-zbb-zbc-zbs). What does that mean? Well the Arm cores are proprietary.

Raspberry Pi pays Arm some money, Arm sends them the designs, and Raspberry Pi can use the Arm cores in their chip.

The RISC-V cores aren't really 'owned'. They're open source, meaning Raspberry Pi can just [clone this git repository](https://github.com/Wren6991/Hazard3), use the designs, and that's it. No licensing, no proprietary specs. That doesn't mean the Hazard3 cores are _faster_ or more _efficient_, just that they're open.

Including both sets of cores allows you to choose between Arm and RISC-V, and you can even build [a 'universal binary'](https://github.com/raspberrypi/pico-examples?tab=readme-ov-file#universal) that works on either set of cores at runtime.

There are a couple caveats:

  1. You can't run all four cores at the same time, it's either-or.
  2. There's a lot less code out there that works low-level with RISC-V, so for most people, especially casual programmers just running MicroPython, you'll probably stick to the Arm cores.

But the way Raspberry Pi's doing this, I have to wonder: is it a signal that people should start transitioning their code to RISC-V? We'll see. EspressIf's had [RISC-V versions of their ESP32s](https://www.espressif.com/en/products/socs/esp32-c3) one out for a while. It's nice to see Raspberry Pi joining the party.

## Conclusion

That's the Pico 2 and everything that's changed. A Pico 2 W will be arriving later this year. But bottom line, the RP2350 and its bigger B variant are going to be appearing in a ton of new devices.

Watch the video that goes along with this blog post:

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/oXF_lVwA8A4" frameborder='0' allowfullscreen></iframe></div>
</div>
