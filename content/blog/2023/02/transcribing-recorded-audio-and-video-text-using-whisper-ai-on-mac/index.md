---
nid: 3273
title: "Transcribing recorded audio and video to text using Whisper AI on a Mac"
slug: "transcribing-recorded-audio-and-video-text-using-whisper-ai-on-mac"
date: 2023-02-16T05:34:15+00:00
drupal:
  nid: 3273
  path: /blog/2023/transcribing-recorded-audio-and-video-text-using-whisper-ai-on-mac
  body_format: markdown
  redirects:
    - /blog/2023/how-transcribe-audio-files-text-using-whisper-ai-on-mac
aliases:
  - /blog/2023/how-transcribe-audio-files-text-using-whisper-ai-on-mac
tags:
  - ai
  - mac
  - software
  - transcription
  - translation
  - tutorial
  - whisper
---

<blockquote><p><strong>2024 Update</strong>: I have a short video outlining my end-to-end process for subtitling all my videos on YouTube using Whisper/MacWhisper:</p>
<div class="yt-embed">
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/S1M9NOtusM8" frameborder='0' allowfullscreen></iframe></div>
</div>
</blockquote>

Late last year, OpenAI announced [Whisper](https://openai.com/blog/whisper/), a new speech-to-text language model that is extremely accurate in translating many spoken languages into text. The [whisper](https://github.com/openai/whisper) repository contains instructions for installation and use.

**tl;dr**:

```
# Install whisper and its dependencies.
pip3 install git+https://github.com/openai/whisper.git 

# (When needed) Update whisper.
pip3 install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

# Make sure ffmpeg is installed.
brew install ffmpeg

# Translate speech into text.
whisper my_audio_file.mp3 --language English
```

One thing I do quite regularly for my YouTube channel is extract the audio track, convert it to text using an online tool (I used to use [Welder](https://www.getwelder.com) until they were bought out by Veed), and then hand-edit the file to fix references to product names, people, etc.

Then I upload either an edited .txt or .srt file alongside my video on YouTube, and people are able to use Closed Captions. YouTube shows whether a video has manually-curated captions with this handy little 'CC' icon:

{{< figure src="./closed-caption-youtube-video.jpg" alt="Closed Captions for YouTube videos" width="700" height="282" class="insert-image" >}}

But as Veed's free tier only allows up to 10 minutes of audio to be transcribed at a time, it was time to look elsewhere. And on my earlier blog post about [using macOS's built-in Dictation feature for transcription](/blog/2022/how-transcribe-audio-text-using-dictation-on-mac), `rasmi` commented that a new tool was available, [Whisper](https://github.com/openai/whisper).

So I took it for a spin!

I installed it and ran it on one of my video's audio tracks using the commands at the top of this post, and I was pleasantly surprised:

  - Experimenting with the different models, `base.en` was very fast for English, but I found that `small` or `medium` were much better at identifying product names, obscure technical terms, etc. Honestly it blew me away that it picked up words like 'PlinkUSA', 'Sliger', and 'Raspberry Pi'—something other transcription tools would trip on.
  - You can even translate text files (using `--translate`), which is a neat trick. It will automatically identify the source language, or you can specify it with `--language`).
  - It's not quite perfect yet—I still need to touch up probably one word every 10 sentences. But it's a thousand times easier than trying to transcribe things manually! And it even does punctuation and outputs an .srt natively.

I've been scanning through discussions and there are already some great ones about features like [diarization](https://github.com/openai/whisper/discussions/264) (being able to identify multiple speakers in a conversation) and [performance benchmarking](https://github.com/openai/whisper/discussions/918).

On my Mac Studio's CPU, the conversion process is only a little slower than real-time. I haven't yet tested it on my PC with a beefier GPU, but I plan on testing that soon.

Being fairly new, specific UIs for Whisper aren't mature yet... but I did find things like [whisper-ui](https://github.com/hayabhay/whisper-ui), and there's even a Hugging Face webapp [Whisper Webui](https://huggingface.co/spaces/aadnk/whisper-webui) you can use for up to 10 minutes of audio transcription to get a feel for it.

And on macOS, if the command line isn't your thing, Jordi Bruin created an app [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper), which is free for the standard version and includes a UI for editing the transcription live:

{{< figure src="./macwhisper.gif" alt="MacWhisper" width="532" height="358" class="insert-image" >}}

Hopefully more UIs are developed, especially something I could toss on one of my PCs here, so I could quickly throw an audio file at it from any device.

I'm generally a bit conservative when it comes at throwing AI at a problem, but speech to text (and vice-versa) is probably one of the most cut-and-dry uses that makes sense and doesn't carry a number of footguns.
