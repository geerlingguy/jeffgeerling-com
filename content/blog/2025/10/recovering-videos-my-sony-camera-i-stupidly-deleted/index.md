---
nid: 3505
title: "Recovering videos from my Sony camera that I stupidly deleted"
slug: "recovering-videos-my-sony-camera-i-stupidly-deleted"
date: 2025-10-23T17:30:41+00:00
drupal:
  nid: 3505
  path: /blog/2025/recovering-videos-my-sony-camera-i-stupidly-deleted
  body_format: markdown
  redirects: []
tags:
  - backup
  - data recovery
  - disk drill
  - format
  - mp4
  - photorec
  - sony
  - video
---

{{< figure src="./sony-a6700-sd-cards-on-desk.jpeg" alt="Sony A6700 SD cards on desk" width="700" height="394" class="insert-image" >}}

My normal process for transferring video footage from my Sony cameras to my computer is as follows:

  1. Run a `sonydump` script that copies all video files from my SD card to my local computer, then runs `rm *.MP4` in the folder on the SD card, and ejects it.
  2. I copy the files onto my NAS, which has an hourly ZFS snapshot and also backs up that snapshot to my 2nd on-site backup server.
  3. At the end of the day, I run a sync command that synchronizes all my working set of files to an external Thunderbolt drive I always bring home with me.

Unfortunately, as it was the end of the day yesterday when I got back from a video shoot, I had the folder _on the external drive_ open, and not the folder where I copy the files to on my NAS. Thus, after I _thought_ I had copied all the files to the NAS, I deleted the local folder on my computer. Then I ran the sync command, and apparently I have that sync command set to delete files that don't exist in the source.

Oops. Just deleted all the new footage. And because I copied to my local Thunderbolt drive, and not my NAS, that hourly snapshot didn't have the new footage.

No worries, maybe Time Machine backed up the footage in the mean time? Nope. Didn't wait long enough like I normally do before copying the files off the main computer.

_Double oops._

## Video

I have a video version of this blog post on my 2nd channel, embedded below. But if you enjoy reading more than video like I do, scroll down and read on!

<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/dJiUgAqz1q8" frameborder='0' allowfullscreen></iframe></div>
</div>

## First attempt - `photorec`

I've written about [using photorec to restore photos off an erased SD card](/blog/2019/rescue-photos-and-other-files-sd-or-microsd-card-photorec) in the past. I also have gotten a few video files off hard drives where I had errantly deleted them on my Mac before.

And I know it's impossible to recover photos off SD cards on Sony cameras when the card has been formatted, due to the way Sony's cameras perform the formatting operation[^sonyformat]. Don't ask me how I know.

But that's why I have my new import system, that just runs `rm` on all the video files — in theory they should be recoverable!

Unfortunately, it's not that easy.

Photorec recovered over 100 video files off my SD card.

My Sony A6700 is set to 'XAVC S 4K', 30p, 100M 4:2:0 8bit, and every clip seems to get a little XML sidecar file, like:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<NonRealTimeMeta xmlns="urn:schemas-professionalDisc:nonRealTimeMeta:ver.2.20" xmlns:lib="urn:schemas-professionalDisc:lib:ver.2.10" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" lastUpdate="2025-10-21T10:30:35-06:00">
  <TargetMaterial umidRef="060A2B340101010501010D4313000000CE4E5C17690906C4B0653AFFFE5881D9"/>
  <Duration value="390"/>
  <LtcChangeTable tcFps="30" halfStep="false">
    <LtcChange frameCount="0" value="67212901" status="increment"/>
    <LtcChange frameCount="389" value="66342901" status="end"/>
  </LtcChangeTable>
  <CreationDate value="2025-10-21T10:30:22-06:00"/>
  <KlvPacketTable>
    <KlvPacket key="060E2B34010101050301020A02000000" frameCount="0" lengthValue="095F5265635374617274" status="spot"/>
  </KlvPacketTable>
  <VideoFormat>
    <VideoRecPort port="DIRECT"/>
    <VideoFrame videoCodec="AVC_3840_2160_HP@L51" captureFps="29.97p" formatFps="29.97p"/>
    <VideoLayout pixel="3840" numOfVerticalLine="2160" aspectRatio="16:9"/>
  </VideoFormat>
  <AudioFormat numOfChannel="2">
    <AudioRecPort port="DIRECT" audioCodec="LPCM16" trackDst="CH1"/>
    <AudioRecPort port="DIRECT" audioCodec="LPCM16" trackDst="CH2"/>
  </AudioFormat>
  <Device manufacturer="Sony" modelName="ILCE-6700" serialNo="[redacted]"/>
  <RecordingMode type="normal" cacheRec="false"/>
  <AcquisitionRecord>
    <Group name="CameraUnitMetadataSet">
      <Item name="CaptureGammaEquation" value="rec709"/>
      <Item name="CaptureColorPrimaries" value="rec709"/>
      <Item name="CodingEquations" value="rec709"/>
    </Group>
    <ChangeTable name="ImagerControlInformation">
      <Event frameCount="0" status="start"/>
    </ChangeTable>
    <ChangeTable name="LensControlInformation">
      <Event frameCount="0" status="start"/>
    </ChangeTable>
    <ChangeTable name="DistortionCorrection">
      <Event frameCount="0" status="start"/>
    </ChangeTable>
    <ChangeTable name="Gyroscope">
      <Event frameCount="0" status="start"/>
    </ChangeTable>
    <ChangeTable name="Accelerometor">
      <Event frameCount="0" status="start"/>
    </ChangeTable>
  </AcquisitionRecord>
</NonRealTimeMeta>
```

After that, in the sidecar, there's a bunch of other data, maybe like an MP4 header file or something? Not sure what the other data in the file is for.

But the other odd thing is `photorec` winds up recovering two types of video files; larger `.mp4` files, and smaller `_moov.mov` files, like:

```
f90809344_moov.mov
f77701376.mp4
f77701120_moov.mov
f71932160.mp4
f72326400.mp4
...
```

I see many mentions of [split files from photorec](https://forum.cgsecurity.org/phpBB3/viewtopic.php?t=4855), but like the one I just linked, they often also include a file ending in `_ftyp.mov`, which is the 'first atom of the video file'. Recovery of the full video file would be thus:

```
cat f28480574_ftyp.mov f36193751.mp4 > fixed.mp4
```

I've tried that with the `_moov.mov` and `.mp4` files, even writing a script to try combining every combination (this takes up a lot of space, lol), and none of those files would play. Most would just open up to a black screen with a video length as set (presumably) in the `_moov.mov` file, but there is no audio or video.

Some forum posts suggested enabling the `photorec` option `[X] mov/mdat Recover mdat atom as a separate file` under `File Opt` in the partition settings screen. Unfortunately doing that and re-scanning the entire drive didn't result in any more files (especially not the `_ftyp.mov` files that seemed so precious). Maybe a quirk with how Sony writes XAVC video files?

## Saving myself from desparation

To make sure I had a full byte-for-byte backup of my SD card, I opened up Disk Utility and elected to 'Create a Disk Image from [SD card]' in the File menu. This saves off a `.dmg` or Disk Image file that I can open up and mess with later.

I could've also used `dd` to create a standard `.img` disk image on either Linux or Mac:

```
diskutil list  # Get the ID of the SD card (in my case, /dev/disk4)
diskutil unmountDisk /dev/disk4
sudo dd if=/dev/rdisk4 of=sd-card-backup.img bs=1m
```

You can press Ctrl-T to see `dd` progress if you want. It takes a while since at least on my Mac/card, the maximum read speed is around 250 MB/sec, on a 128 GB card.

I should've probably done this right away, instead of waiting until a few passes with data recovery tools!

**The moral of this part of the story**: if you suspect any data deletion recovery will be needed, don't write anything to a drive at all, as it may write over the free space you need to scan to find the missing file! If you don't know what you're doing, it's probably best to eject the drive, _don't_ put it back in your camera or plug it in anywhere else, and send it off to a data recovery service like [Drive Savers](https://drivesaversdatarecovery.com).

If you _do_ want to work on restoring it, take a complete bit-for-bit backup, and work on _that_ copy. Not only will that preserve the contents of your SD card, recovering data off the cloned copy will run much faster, assuming your SSD or other storage is faster than the SD card.

## Second attempt - fixing the incomplete video files with `untrunc`

With round one of failures under my belt, I decided the next step would be to try recovering video data from the presumably-kinda-borked video files themselves (lacking any easy way to get the 'video header' info that is needed to turn the 3+ GB video files into playable media).

One tool I found mentioned on Reddit and a few other forums was [untrunc](https://github.com/anthwlock/untrunc), which explicitly stated it has support for recovering some Sony XAVC video files.

To do that, you provide it with a known _working_ MP4 file from your camera, and one of the corrupted files, and it will try to fill in the gaps with metadata from the working file (I guess a bit like [Mr. DNA's dino DNA](https://jurassicpark.fandom.com/wiki/Mr._DNA)).

I gave it a shot, building and running it inside a Docker container, and it generated a file with nothing in it.

Trying again with the `-s` option, which 'steps through unknown sequences', I got much further:

```
 10:22:55 ~/Downloads/untrunc 
$ docker run -v ~/Downloads/:/mnt untrunc -s /mnt/C0366.MP4 /mnt/recup_dir.2/f25575424.mp4
Composition time offset atom found. Out of order samples possible.
Info: version 'v367-13cafed-dirty' using ffmpeg '4.4.2-0ubuntu0.22.04.1' Lavc58.134.100
Info: reading /mnt/C0366.MP4
Info: parsing healthy moov atom ... 
[mov,mp4,m4a,3gp,3g2,mj2 @ 0xaaaadf1ac410] st: 0 edit list: 1 Missing key frame while searching for timestamp: 1001
[mov,mp4,m4a,3gp,3g2,mj2 @ 0xaaaadf1ac410] st: 0 edit list 1 Cannot find an index entry before timestamp: 1001.
Info: special track found (meta, 'Timed Metadata Media Handler')

Info: unknown track 'twos' found -> fallback to dynamic stats
Info: using dynamic stats, use '-is' to see them
Info: reading mdat from truncated file ...
Warning: NOT skipping esds atom: 3665212690 (at 0x19e4635 / 0x19e46f5)
Warning: NOT skipping xml  atom: 916274239 (at 0x3ffff3e / 0x3fffffe)
Warning: NOT skipping prof atom: 1835103021 (at 0x3ffff87 / 0x4000047)
Warning: NOT skipping prof atom: 1835103021 (at 0x3ffffc9 / 0x4000089)
Warning: NOT skipping name atom: 1869967392 (at 0x40003e7 / 0x40004a7)
Warning: NOT skipping data atom: 1298494561 (at 0x40003fb / 0x40004bb)
Warning: NOT skipping name atom: 1952804128 (at 0x400040e / 0x40004ce)
Warning: NOT skipping name atom: 1952804128 (at 0x400044a / 0x400050a)
Warning: NOT skipping name atom: 1952804128 (at 0x4000481 / 0x4000541)
Warning: Invalid slice type, probably this is not an avc1 sample
...
Failed reading golomb: too large!
Warning: Invalid slice type, probably this is not an avc1 sample
Failed reading golomb: too large!
Warning: Invalid slice type, probably this is not an avc1 sample
Info: Found 19313681 packets ( avc1: 10349 avc1-keyframes: 36 twos: 19291272 rtmd: 12060 )
Tip: Audio and video seem to have different durations (1.16388).
     If audio and video are not in sync, give `-sv` a try. See `--help`
Info: Duration of avc1: 5min 45s 311ms  (345311 ms)
Info: Duration of twos: 6min 41s 901ms  (401901 ms)
Info: Duration of rtmd: 6min 42s 402ms  (402402 ms)
Warning: Unknown sequences: 1495
Warning: Bytes NOT matched: 725MiB (20.69%)
Info: saving /mnt/recup_dir.2/f25575424.mp4_fixed-s1-dyn.MP4
          
5483 warnings were hidden!
```

The resulting `f25575424.mp4_fixed-s1-dyn.MP4` file actually played! It had the right length, it was smooth for a few short moments of time, and the audio was _somewhat_ intact... but the main thing: I was on to something!

{{< figure src="./still-frame-untrunc-distorted-video.jpg" alt="untrunc restored video still frame" width="700" height="394" class="insert-image" >}}

Nevermind the video was extremely choppy, the audio had weird blips, and the few moments with like 0.5 seconds of smooth motion still had some weird artifacts (e.g. the screen on the dBa meter above)... I had the faintest whiff at success! The next step was to turn that small success into a full video that played back smoothly.

## Learning more about MP4 from Federico Ponchio

The original author of the `untrunc` utility has a whole article about how to [Fix a truncated mp4: do it yourself.](https://vcg.isti.cnr.it/~ponchio/untrunc.php).

In it, he mentions the `moov` data's purpose:

> My Sangsung camera died while shooting the video of my marriage cerimony leaving a 600MB mp4 file which no player could read. The problem is that the codec information and frame indexes where missing at the end of the mp4. The whole moov section actually (as vlc points out and any hex heditor can confirm):
>
> ```
> [00000417] mp4 demux error: MP4 plugin discarded (no moov box)
> ```

So... from this clue, I surmised that maybe the `_moov.mov` file data should be at the _end_ of the video? So maybe my earlier attempt to blindly match up all MP4 files with a `_moov.mov` file was done in the reverse?

Reading further on the [Multimedia Wiki's QuickTime container page](https://wiki.multimedia.cx/index.php?title=QuickTime_container):

> All Quicktime files need to have a moov atom and a mdat atom at the top level. There are other top level atoms as well (e.g. the 'ftyp' atom), which generally are not interesting and can safely be skipped if encountered. The moov atom contains instructions for playing the data in the file. The mdat atom contains the data that will be played.

I tried switching up my script, so it would take an MP4 file and then `cat` every `_moov.mov` file onto the end of it. And that didn't work either. When doing it the first way, it at least created playable files of the length defined in the `_moov.mov` file, but the video frame was black, and audio was choppy (mostly static).

So there was definitely valid data in the MP4 files, and definitely something useful in the `_moov.mov` files. How was I going to reconcile the two!?

## Back to `untrunc`

I figured, I would just try _brute forcing_ things. I'll let `untrunc` have at it with all 40 or so of the MP4 files I had recovered, seeing if I could get a successful restoration of _any_ of them.

I wrote a shell script, `untrunc.sh`, that would attempt to recover each file, deleting the Docker container between each run[^docker]:

```bash
#!/bin/bash

# Find all .mp4 files and loop through each one
for mp4_file in *.mp4; do
    if [ -f "$mp4_file" ]; then
        echo "Running untrunc on $mp4_file"
        docker run --rm -v ~/Downloads/:/mnt untrunc -s /mnt/a-good-file-short.MP4 /mnt/recup_dir.2/$mp4_file
    fi
done

echo "Processing complete."
```

I let this run for an hour or so, and process it did! I actually got fragments of many of the files I was after—unfortunately, only brief 10-20 frame portions would play smoothly, with the frame frozen most of the time. Audio was nearly perfect on a couple clips, but extremely choppy with lots of static on others.

{{< figure src="./untrunc-file-results-restore-videos.png" alt="untrunc file results after restoring video" width="700" height="353" class="insert-image" >}}

I also tested with four other 'good' source videos (some longer, some shorter), and was also considering testing [`mp4fixer`](https://github.com/bookkojot/mp4fixer) as suggested in [this Stack Exchange answer](https://superuser.com/a/1334772). But the other videos didn't make a difference (some resulted in an even _worse_ result!), and I wasn't enthused by mp4fixer not being touched in 6 years. But mainly I grew tired after putting in about 12 hours of work (and writing through maybe 15 TB of disk space with all my experiments. I decided to stop.

It seemed like a dead-end to try recovering these 4K video files, at least as far as 'potentially easy but free' solutions went.

## Pay the Piper

Looking at some of the software people recommended, as a last-ditch effort, I tried [Disk Drill](https://www.disk-drill.com), first downloading the free 'preview' version for Mac.

{{< figure src="./disk-drill-01-scanning-general-video-files.png" alt="Disk Drill - scanning general video files" width="700" height="427" class="insert-image" >}}

Immediately, the software was a breath of fresh air after diving down Docker, shell, and ffmpeg rabbit holes. It might even use some of the same free software under the hood, but being able to click on a drive, click scan, then see it find a bunch of Sony video files (like `C0326.MP4`) instead of having to deal with randomized filenames... that was encouraging.

I let it run its deep scan, then paid up the $108 for a perpetual 'PRO' license and recovered some files.

Unfortunately... the recovered files—while they had the original filenames intact—were still unplayable, and could only be partially recovered the same way as the `photorec`-recovered files, using `untrunc`.

### Advanced Camera Recovery Module

I was about to give up, but went fishing in Disk Drill's support FAQs, and found an article on an [Advanced Camera Recovery](https://www.cleverfiles.com/help/advanced-camera-recovery-in-disk-drill.html) mode, which seemed promising.

{{< figure src="./disk-drill-02-recover-video.png" alt="Disk Drill - advanced camera video restoration mode" width="700" height="427" class="insert-image" >}}

I re-scanned the SD card in _that_ mode, with 'Sony' set as a the camera type, and let it run.

{{< figure src="./disk-drill-03-recover-in-process.png" alt="Disk Drill - recovering files from SD card" width="700" height="432" class="insert-image" >}}

When it was done... I had all my original video files, which seemed to be perfectly intact! Not sure exactly what magic they're running under the hood, but I'm guessing someone on the team at Clever Files knows MP4s and the way Sony (and GoPro, and Insta360, and Canon, and Nikon, etc.) lays out the file structure on their SD cards.

## Conclusion

In conclusion: _don't delete video files for a big project you're working on until you're 100% absolutely certain you stored and backed them up in the correct location._

Otherwise, you're in for a world of pain! I'm okay with spending over $100 on Disk Drill, because the footage was not going to be easy to get again. Otherwise, and especially if you're willing to learn how the MP4 file structure works, you can probably get things recovered (at least some of the time) using open source tools.

I learned a lot about file recovery today, and I hope you did too!

I also decided to buy a whole set of [6 SONY Tough M-series SD cards](https://amzn.to/4hxteCU), so I will have a total of 8. It's a big one-time expense, but since these cards are the lifeblood of my YouTube work... I figure I should change up my workflow. I will not delete anything off the SD cards until after I complete the process of editing a video. I'd rather not _have_ to rely on Disk Drill in the future, but it's good to know that if I'm careful about how badly I fail at transferring my footage, I may still be able to recover :)

[^sonyformat]: It's not a quick erase like I was used to on my Nikon cameras; it goes in and issues a [direct erasure of the entire SD card filesystem](https://stackoverflow.com/questions/65772094/what-is-the-sd-card-erase-process) in a way `photorec` can't recover it.

[^docker]: I could've also just run the same Docker container throughout, but I was already spinning up a new container for each manual run, so thought I'd keep doing that here.
