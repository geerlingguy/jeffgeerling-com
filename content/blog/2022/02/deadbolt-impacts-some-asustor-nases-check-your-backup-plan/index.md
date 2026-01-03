---
nid: 3186
title: "Deadbolt impacts some ASUSTOR NASes \u2014 check your backup plan!"
slug: "deadbolt-impacts-some-asustor-nases-check-your-backup-plan"
date: 2022-02-24T16:00:12+00:00
drupal:
  nid: 3186
  path: /blog/2022/deadbolt-impacts-some-asustor-nases-check-your-backup-plan
  body_format: markdown
  redirects:
    - /blog/2022/deadbolt-impacts-some-asustor-nases-—-check-your-backup-plan
aliases:
  - /blog/2022/deadbolt-impacts-some-asustor-nases-—-check-your-backup-plan
tags:
  - asustor
  - backup
  - crypto
  - disaster recovery
  - nas
  - ransomware
  - security
---

{{< figure src="./asustor-arm.jpeg" alt="ASUSTOR ARM NAS with four hard drives and cover removed" width="700" height="453" class="insert-image" >}}

A few months ago, I wrote up a post covering [my backup plan](/blog/2021/my-backup-plan). In it, I talk about the 3-2-1 backup strategy:

  - 3 copies of all your important data
  - 2 different media
  - 1 offsite

In that post, I mentioned I back everything up with two local copies (two separate NAS units), and a third offsite copy on Amazon Glacier Deep Archive.

Since I use Glacier Deep Archive along with `rclone` to manage the backup copies (in a setup where file deletions are not propagated to the cloud storage), if a file is encrypted or deleted in one of my local copies, that deletion/encryption won't affect that 'offline' copy on Glacier.

I wasn't explicitly clear on it then, but I will be now: because of the rise of ransomware attacks—where a malicious actor will encrypt all your files and 'ransom' an encryption key (usually in exchange for a small crypto payment)—**you _must_ have an offline copy** of any data that's important to you.

So maybe it should be made more explicit in the 3-2-1 plan, expanding it with one more point—O for 'offline' copy:

  - 3 Copies of all your important data
  - 2 different media
  - 1 offsite
  - O **offline**

At its simplest, you could just buy a [12 TB USB hard drive](https://amzn.to/3JU1TIK), plug that into your NAS every week or month, and do a one-touch backup—assuming all your data fits onto it.

Then unplug the drive when the backup is complete, and set it on a shelf (or in a safe, for a little more protection!).

The point is: ransomware/cryptolocking can be a bump in the road rather than a catastrophe. All it takes is a reliable and tested [backup plan](https://github.com/geerlingguy/my-backup-plan).

One other thing I'll mention is I never turn on any type of service like 'EZConnect.' Services that expose any home device (not just NASes) publicly over the Internet are ripe targets for hacking, because one vulnerability can lead to thousands of devices hacked.

Instead, I only expose devices to my internal network. If I absolutely need remote access, I will set up a connection through a secure VPN that I manage within my home. (And even that—running your own home VPN—is a risk I think most people shouldn't take.)
