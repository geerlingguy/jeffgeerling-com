---
nid: 3106
title: "Retrieving individual files from S3 Glacier Deep Archive using AWS CLI"
slug: "retrieving-individual-files-s3-glacier-deep-archive-using-aws-cli"
date: 2021-06-08T14:48:57+00:00
drupal:
  nid: 3106
  path: /blog/2021/retrieving-individual-files-s3-glacier-deep-archive-using-aws-cli
  body_format: markdown
  redirects: []
tags:
  - amazon
  - aws
  - backup
  - glacier
  - nas
  - restore
  - s3
---

I still haven't blogged about my overall backup strategy (though I've mentioned it in the past a few times on my YouTube channel)—but overall, how it works is I have two local copies of any important data, and most of the non-video data is _also_ stored in my Dropbox folder, so I get two local copies and one cloud backup for 'free'.

Then I also back up everything (including video content) from my NAS to an Amazon S3 Glacier Deep Archive-backed bucket at least once a week (sometimes more frequently, when I am working on a big project and manually kick off a mid-week backup).

Well, this week I was working on editing a video project with about 60 GB of video files. I had finished most of the edit, and after I thought I had finished the process of 'consolidating' the media files into my video library, I deleted the "scratch" folder that held all the original files. Well, apparently three of the video files were _not_ yet consolidated, and Final Cut Pro showed the dreaded "media missing" warning. I had actually deleted the files from both my local copies, so I was slightly nervous, but it turns out I had run the backup to Glacier manually the night before, so all my video was intact.

But the 'Deep Archive' means data is stored offline in tape storage, and retrieval takes a _minimum_ of about 12 hours. I wanted to document how I restored the three individual video files I needed in this post, just so I don't have to spend the extra 5 minutes reading through Amazon's docs:

## Initiating a restore

Using Amazon's S3 Management Console, I browsed to the file path in my bucket (e.g. `my-bucket`), then checked the box next to the three files and initiated a "restore". I selected the 'Standard' retrieval option, since that was the fastest available (regular Glacier—not Deep Archive—also offers an 'Expedited' rate for more money), and initiated the restore.

Instead of refresh the console UI every bit of time, I ran the following in the terminal to watch and see when the retrieval completed:

```
# Monitor the progress (check every 10 minutes).
$ watch -n 600 "aws --profile personal s3api head-object --bucket my-bucket --key \"Path/To/My/File.mov""
```

This should output something like the following:

```
{
    "AcceptRanges": "bytes",
    "Restore": "ongoing-request=\"true\"",
    ...
    "StorageClass": "DEEP_ARCHIVE"
}
```

And it just keeps repeating the `aws` command every 10 minutes until you see it change to the following:

```
{
    "AcceptRanges": "bytes",
    "Restore": "ongoing-request=\"false\", expiry-date=\"Fri, 11 Jun 2021 00:00:00 GMT\"",
    ...
    "StorageClass": "DEEP_ARCHIVE"
}
```

Now it's time to download the file, since it's available in S3:

```
# Download the file to local machine.
$ aws --profile personal s3api get-object --bucket my-bucket  --key "Path/To/My/File.mov" "File.mov"
```

And there you go! Only a few pennies to restore 10-20 GB of files, in my case. I'll happily pay the $5/month or so it takes to have the extra piece of mind I get from Glacier backing up a few terabytes of files outside my house.

I also decided to turn on my NAS's 'network recycle bin' feature so it retains a copy of any deleted file for a week, too, to protect myself from my own stupidity in the future.
