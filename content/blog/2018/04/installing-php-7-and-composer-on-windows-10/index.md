---
nid: 2837
title: "Installing PHP 7 and Composer on Windows 10, Natively"
slug: "installing-php-7-and-composer-on-windows-10"
date: 2018-04-09T03:23:35+00:00
drupal:
  nid: 2837
  path: /blog/2018/installing-php-7-and-composer-on-windows-10
  body_format: markdown
  redirects:
    - /blog/2018/installing-php-7-and-composer-on-windows-10-natively
aliases:
  - /blog/2018/installing-php-7-and-composer-on-windows-10-natively
tags:
  - composer
  - drupal
  - drupal planet
  - php
  - tutorial
  - windows
  - windows 10
---

> **Note**: If you want to install and use PHP 7 and Composer within the Windows Subsystem for Linux (WSL) using Ubuntu, [I wrote a guide for that, too](//www.jeffgeerling.com/blog/2018/installing-php-7-and-composer-on-windows-10-using-ubuntu-wsl)!

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/SR33B74gWL4" frameborder='0' allowfullscreen></iframe></div>

I am working a lot on Composer-based Drupal projects lately (especially gearing up for DrupalCon Nashville and my joint [workshop on Drupal and Composer](https://events.drupal.org/nashville2018/sessions/how-build-drupal-site-composer-and-keep-all-your-hair) with Matthew Grasmick), and have been trying to come up with the simplest solutions that work across macOS, Linux, and Windows. For macOS and Linux, getting PHP and Composer installed is fairly quick and easy. However, on Windows there seem to crop up little issues here and there.

Since I finally spent a little time getting the official version of PHP for native Windows installed, I figured I'd document the process here. Note that many parts of this process were learned from the concise article [Install PHP7 and Composer on Windows 10](http://kizu514.com/blog/install-php7-and-composer-on-windows-10/) from the website KIZU 514.

## Install PHP 7 on Windows 10

{{< figure src="./php-powershell-windows-10.png" alt="PHP 7 running in Windows 10 in PowerShell" width="650" height="155" class="insert-image" >}}

  1. Install the [Visual C++ Redistributable for Visual Studio 2015](http://www.microsoft.com/en-us/download/details.aspx?id=48145)—this is linked in the sidebar of the [PHP for Windows Download page](https://windows.php.net/download/), but it's kind of hidden. If you don't do this, you'll run into a rather cryptic error message, `VCRUNTIME140.DLL was not found`, and `php` commands won't work.
  1. [Download PHP for Windows](https://windows.php.net/download/). I prefer to use 7.1.x (current release - 1), so I downloaded the latest _Non-thread-safe_ 64-bit version of 7.1.x. I downloaded the .zip file version of the `VC14 x64 Non Thread Safe` edition, under the PHP 7.1 heading.
  1. Expand the zip file into the path `C:\PHP7`.
  1. Configure PHP to run correctly on your system:
    1. In the `C:\PHP7` folder, rename the file `php.ini-development` to `php.ini`.
    1. Edit the `php.ini` file in a text editor (e.g. Notepad++, Atom, or Sublime Text).
    1. Change the following settings in the file and save the file:
      1. Change `memory_limit` from `128M` to `1G` (because Composer can use lots of memory!)
      1. Uncomment the line that reads `; extension_dir = "ext"` (remove the `; ` so the line is just `extension_dir = "ext"`).
      1. In the section where there are a bunch of `extension=` lines, uncomment the following lines:
         1. `extension=php_gd2.dll`
         1. `extension=php_curl.dll`
         1. `extension=php_mbstring.dll`
         1. `extension=php_openssl.dll`
         1. `extension=php_pdo_mysql.dll`
         1. `extension=php_pdo_sqlite.dll`
         1. `extension=php_sockets.dll`
  1. Add `C:\PHP7` to your Windows system path:
    1. Open the System Control Panel.
    1. Click 'Advanced System Settings'.
    1. Click the 'Environment Variables...' button.
    1. Click on the `Path` row under 'System variables', and click 'Edit...'
    1. Click 'New' and add the row `C:\PHP7`.
    1. Click OK, then OK, then OK, and close out of the System Control Panel.
  1. Open PowerShell or another terminal emulator (I generally prefer [cmder](http://cmder.net)), and type in `php -v` to verify PHP is working.

At this point, you should see output like:

```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\jgeerling> php -v
PHP 7.0.29 (cli) (built: Mar 27 2018 15:23:04) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2017 Zend Technologies
```

This means PHP is working, yay!

## Install Composer on Windows 10

{{< figure src="./composer-powershell-windows-10.png" alt="Composer running in Windows 10 in PowerShell" width="650" height="479" class="insert-image" >}}

Next, we're going to install Composer by downloading it and moving it into place so we can run it with just the `composer` command:

  1. Download the [Windows Installer for Composer](https://getcomposer.org/download/) and run it.
  1. Note that the Windows Installer for Composer might ask to make changes to your `php.ini` file. That's okay; allow it and continue through the setup wizard.
  1. Close out of any open PowerShell or other terminal windows, and then open a new one.
  1. Run the `composer` command, and verify you get a listing of the Composer help and available commands.

That's it! Now you have PHP 7 and Composer running natively on your Windows 10 PC. Next up, dominate the world with some new PHP projects!
