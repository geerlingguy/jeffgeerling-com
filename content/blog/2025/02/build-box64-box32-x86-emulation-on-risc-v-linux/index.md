---
nid: 3442
title: "Build Box64 with Box32 for X86 emulation on RISC-V Linux"
slug: "build-box64-box32-x86-emulation-on-risc-v-linux"
date: 2025-02-11T17:05:50+00:00
drupal:
  nid: 3442
  path: /blog/2025/build-box64-box32-x86-emulation-on-risc-v-linux
  body_format: markdown
  redirects: []
tags:
  - box32
  - box64
  - box86
  - emulation
  - p550
  - risc-v
  - sifive
---

{{< figure src="./risc-v-gpu-2.jpeg" alt="RISC-V GPU system testing" width="700" height="394" class="insert-image" >}}

Recently I've been [testing a SiFive HiFive Premier P550](https://github.com/geerlingguy/sbc-reviews/issues/65), and as part of that testing, I _of course_ plugged in some AMD GPUs I had laying around.

I'll get to that testing at a later date, but one thing I enjoy in my testing is finding what 3D accelerated games and other applications can be run on alternative architectures. With the great work from Wine and Proton over the years, a great many games run out of the box on Linux—and they can be made to run on Arm and RISC-V architectures with almost as much ease as Linux on X86/AMD64!

The process for manually compiling Box64 on RISC-V Linux was a little different than what I'm used to. And on RISC-V, you have to use Box32 (included with Box64 but not enabled by default) instead of Box86. Because of that, I thought I'd document the process here, since I guarantee I'll refer back to it a few dozen times over the next couple years :)

## Compiling Box64 with Box32 on RISC-V Linux

{{< figure src="./box64-box32-compile.jpg" alt="Box64 - Box32 option for compilation" width="700" height="369" class="insert-image" >}}

This process was done on a SiFive HiFive Premier P550 system running Ubuntu 24.04.1 LTS.

```
# Clone box64 and prepare to compile it
git clone https://github.com/ptitSeb/box64
cd box64
mkdir build; cd build

# Run ccmake to enable options:
#   - BOX32
#   - BOX32_BINFMT
#   - CMAKE_BUILD_TYPE (set to 'RelWithDebInfo')
#   - RV64
#   - RV64_DYNAREC
sudo apt install -y cmake-curses-gui
ccmake ..  # After selections, press 'c' to configure and 'g' to generate

# Compile box64
cmake ..
make -j4  # Takes a while

# Install box64 and restart binfmt
sudo make install
sudo systemctl restart systemd-binfmt
```

_Currently_ Steam is not supported on RISC-V. If you run the included `install_steam.sh` script, and run the command `steam`, you'll get:

```
/home/ubuntu/.local/share/Steam/ubuntu12_32/steam: cannot execute binary file: Exec format error
```

See the [original post](https://github.com/geerlingguy/sbc-reviews/issues/65#issuecomment-2649116590) where I tested the process on my GitHub issue for the HiFive Premier P550 system.

## Running x86/AMD64 applications

Box64 includes some test applications in its `tests` directory. You can run one to see if everything's working:

```
ubuntu@ubuntu:~/Downloads/box64/tests$ box64 ./test01
[BOX64] Warning: DynaRec is available on this host architecture, an interpreter-only build is probably not intended.
[BOX64] Running on unknown riscv64 cpu with 4 cores, pagesize: 4096
[BOX64] Will use hardware counter measured at 1.0 MHz emulating 2.0 GHz
[BOX64] Box64 v0.3.3 a50d34e4 built on Feb 10 2025 22:37:30
[BOX64] Detected 48bits at least of address space
[BOX64] Counted 25 Env var
[BOX64] BOX64 LIB PATH: 
[BOX64] BOX64 BIN PATH: ./:bin/:/home/ubuntu/.local/bin/:/usr/local/sbin/:/usr/local/bin/:/usr/sbin/:/usr/bin/:/sbin/:/bin/:/usr/games/:/usr/local/games/:/snap/bin/
[BOX64] Looking for ./test01
[BOX64] Rename process to "test01"
[BOX64] Using native(wrapped) libc.so.6
[BOX64] Using native(wrapped) ld-linux-x86-64.so.2
[BOX64] Using native(wrapped) libpthread.so.0
[BOX64] Using native(wrapped) libdl.so.2
[BOX64] Using native(wrapped) libutil.so.1
[BOX64] Using native(wrapped) libresolv.so.2
[BOX64] Using native(wrapped) librt.so.1
[BOX64] Using native(wrapped) libbsd.so.0
Hello x86_64 World!
```

### Installing Wine

If you want to run _Windows_ applications, you will also need Wine. To install that, grab the download link for the latest `wine-VERSION_HERE-amd64-wow64.tar.xz` file from [Wine-Builds releases](https://github.com/Kron4ek/Wine-Builds/releases), and install it:

```
# 10.0 is the latest stable version as of this writing
cd ~/Downloads
wget https://github.com/Kron4ek/Wine-Builds/releases/download/10.0/wine-10.0-amd64-wow64.tar.xz
tar -xvf wine-10.0-amd64-wow64.tar.xz
mv wine-10.0-amd64-wow64 wine

# Make shortcuts so it's easier to use wine
sudo ln -s ~/Downloads/wine/bin/wine /usr/local/bin/wine
sudo ln -s ~/Downloads/wine/bin/wineserver /usr/local/bin/wineserver
sudo ln -s ~/Downloads/wine/bine/wineboot /usr/local/bin/wineboot
sudo ln -s ~/Downloads/wine/bin/wine64 /usr/local/bin/wine64
```

Then you should be able to run EXEs with:

```
wine my-windows-application.exe
```

### Playing Games

Games often require additional library support—and chances are you have decent Vulkan support if you're using a dGPU with drivers under Linux, like an AMD GPU.

So a tool like [`dxvk`](https://github.com/doitsujin/dxvk) is useful, to translate DirectX system calls to Vulkan. And to install that, and a couple other handy Wine tools, I used `winetricks` at the suggestion of Box64 devs:

```
cd Downloads
wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
chmod +x winetricks
sudo mv winetricks /usr/bin/winetricks
```

Then use it to install three necessary libraries:

```
sudo apt install cabextract
winetricks corefonts dxvk vkd3d 
```

Using all of that, I was able to install and run The Witcher 3 on my P550... albeit _very_ slowly. It was more like a slideshow with user input _suggestions_ rather than a video game:

{{< figure src="./witcher-gameplay.jpg" alt="Witcher 3 gameplay on RISC-V" width="700" height="394" class="insert-image" >}}

ptitSeb's [earlier demo of The Witcher 3 on RISC-V](https://www.youtube.com/watch?v=5UMUEM0gd34) was run on the Sophgo 64-core RISC-V CPU inside a Milk-V Pioneer, a _much_ faster overall CPU (not on a per-core basis, though) than the 4 P550 cores...

I documented the entire [Box64 / Wine / Witcher 3 process on GitHub](https://github.com/ptitSeb/box64/issues/2346).
