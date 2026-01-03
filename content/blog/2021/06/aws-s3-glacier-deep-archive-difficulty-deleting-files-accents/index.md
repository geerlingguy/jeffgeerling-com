---
nid: 3112
title: "AWS S3 Glacier Deep Archive - Difficulty deleting files with accents"
slug: "aws-s3-glacier-deep-archive-difficulty-deleting-files-accents"
date: 2021-06-15T16:04:03+00:00
drupal:
  nid: 3112
  path: /blog/2021/aws-s3-glacier-deep-archive-difficulty-deleting-files-accents
  body_format: markdown
  redirects: []
tags:
  - aws
  - backup
  - billing
  - bugs
  - console
  - glacier
  - s3
---

A few days ago, my personal AWS account's billing alert fired, and delivered me an email saying I'd already exceeded my personal comfort threshold—in the second week of the month!

{{< figure src="./aws-billing-alert.png" alt="AWS billing alert email" width="675" height="144" class="insert-image" >}}

Knowing that I had just rearranged my entire backup plan because I wanted to change the structure of my archives both locally and in my S3 Glacier Deep Archive mirror on AWS, I suspected something didn't get moved or deleted within my backup S3 bucket.

And I was right.

But I wanted to write this up for two reasons:

  1. As a reminder to **always set up billing alerts in AWS**, no matter how small your AWS account! Without that notification, I would've only found out about this problem at the end of the month—and paid about 10x my normal monthly rate until I fixed the problem!
  2. As a warning that even if AWS console says there were no problems deleting an object, you should always double-check to make sure it actually got deleted.

And to the second point, it gets more complicated with S3 Glacier Deep Archive, because I'm used to some operations taking 12 hours or longer, so I got lazy and didn't double-check on the delete operations.

## The problem

So here's how I ended up having two or three copies of many terabytes of backup data:

  1. I tried moving a folder with terabytes of video data in them from one path to another within an S3 Glacier Deep Archive bucket.
  2. Because that operation requires restoring data temporarily so it can be moved, I decided to just download/re-upload the data into the new path manually.
  3. After that manual move was complete, I selected the top-level folder and chose 'Delete' in the AWS Console.

This Delete operation showed me that there were 0 problems deleting anything, and showed many thousand deleted objects. "Great!" I thought.

But I noticed the top level folder was still there, and many things within. So I left it and thought I'd go back and check the next day to see if it was still there. I forgot to do that though, and a few days later I got a billing alert that my threshold was reached.

## Figuring out what was happening

I went into AWS Console and tried deleting the folder again a few days later. It kept showing me:

> Successfully deleted: 0 objects<br>
> Failed to delete: 0 objects

I thought something must be wrong, because I could see objects in the directory. A lot of objects.

So I started going deeper in the folder hierarchy and deleting all the subfolders on every level. And this got me further. Eventually, I found there was just one file in one nested hierarchy that was seemingly impossible to delete:

{{< figure src="./aws-s3-object-not-deleting.png" alt="AWS Object not deleting in Amazon S3 Glacier Deep Archive" width="426" height="398" class="insert-image" >}}

And when I tried deleting it in the Console, I got the message:

{{< figure src="./aws-s3-delete-object-0.jpg" alt="AWS S3 Glacier Deep Archive 0 objects deleted" width="789" height="535" class="insert-image" >}}

So something was weird.

I filed a ticket with AWS Billing support, since my personal account doesn't get any technical support—I figured I was being _billed_ for this stupid bug, so I was justified asking _billing_ to help me take care of it.

## Finding a fix

After [posting about this on Twitter](https://twitter.com/geerlingguy/status/1404566349863702529), someone mentioned trying the delete via the AWS CLI, or via the SDK.

I tried deleting the folder containing the file, and got:

```
$ aws --profile personal s3 rm s3://jg-archive/Volumes/Brachiosaur/Final_Cut_Pro_Archived_Projects/
delete: s3://jg-archive/Volumes/Brachiosaur/Final_Cut_Pro_Archived_Projects/
```

But the folder was still there, along with the file deep inside.

So I tried deleting the file directly, via the S3 URI I copied out of the Console:

```
$ aws --profile personal s3 rm "s3://jg-archive/Volumes/Brachiosaur/Final_Cut_Pro_Archived_Projects/2019-07 Raspberry Pi Road Construction Time-Lapse.fcpbundle/Road Construction Time-Lapse/Original Media/02 Thé À la Menthe.m4a"
delete: s3://jg-archive/Volumes/Brachiosaur/Final_Cut_Pro_Archived_Projects/2019-07 Raspberry Pi Road Construction Time-Lapse.fcpbundle/Road Construction Time-Lapse/Original Media/02 Thé À la Menthe.m4a
```

And _voilà_! The file was gone—and all the nested folders containing it!

So I guess the lesson I've learned as that there's some weird bug surrounding files with accents in their names—and it might be triggered by copying files from macOS into S3 Glacier Deep Archive. Or it might be triggered by something in the Glacier backend. Or in the Console UI's code... who knows.

In the end, I paid maybe $15 extra for the few days of storage duplication, and I'm not sure if it's worth trying to get that credit repaid through my support ticket due to AWS's own bug, even though it _should_ be refunded in my opinion.

Heaven knows I've spent enough in my lifetime through a dozen or so AWS accounts to warrant a few technical support tickets.
