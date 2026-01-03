---
nid: 2838
title: "Installing PHP 7 and Composer on Windows 10, Using Ubuntu in WSL"
slug: "installing-php-7-and-composer-on-windows-10-using-ubuntu-wsl"
date: 2018-04-11T13:34:21+00:00
drupal:
  nid: 2838
  path: /blog/2018/installing-php-7-and-composer-on-windows-10-using-ubuntu-wsl
  body_format: markdown
  redirects: []
tags:
  - composer
  - drupal
  - drupal planet
  - linux
  - php
  - ubuntu
  - windows
  - windows 10
  - wsl
---

> **Note**: If you want to install and use PHP 7 and Composer within Windows 10 _natively_, [I wrote a guide for that, too](//www.jeffgeerling.com/blog/2018/installing-php-7-and-composer-on-windows-10)!

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/Zxmxri7DmSE" frameborder='0' allowfullscreen></iframe></div>

Since Windows 10 introduced the Windows Subsystem for Linux (WSL), it has become far easier to work on Linux-centric software, like most PHP projects, within Windows.

To get the WSL, and in our case, Ubuntu, running in Windows 10, follow the directions in Microsoft's documentation: [Install the Windows Subsystem for Linux on Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10), and download and launch the Ubuntu installer from the Windows Store.

Once it's installed, open an Ubuntu command line, and let's get started:

## Install PHP 7 inside Ubuntu in WSL

Ubuntu has packages for PHP 7 already available, so it's just a matter of installing them with `apt`:

  1. Update the apt cache with `sudo apt-get update`
  2. Install PHP and commonly-required extensions: `sudo apt-get install -y git php7.0 php7.0-curl php7.0-xml php7.0-mbstring php7.0-gd php7.0-sqlite3 php7.0-mysql`.
  3. Verify PHP 7 is working: `php -v`.

If it's working, you should get output like:

{{< figure src="./php-7-ubuntu-wsl-windows-resized.png" alt="PHP 7 running under Ubuntu under WSL on Windows 10" width="650" height="128" class="insert-image" >}}

## Install Composer inside Ubuntu in WSL

Following the [official instructions for downloading and installing Composer](https://getcomposer.org/download/), copy and paste this command into the CLI:

```
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
php composer-setup.php && \
php -r "unlink('composer-setup.php');"
```

To make Composer easier to use, run the following command to move Composer into your global path:

    sudo mv composer.phar /usr/local/bin/composer

Now you can run `composer`, and you should get the output:

{{< figure src="./composer-ubuntu-wsl-windows.png" alt="Composer running under Ubuntu under WSL on Windows 10" width="650" height="340" class="insert-image" >}}

That's it! Now you have PHP 7 and Composer running inside Ubuntu in WSL on your Windows 10 PC. Next up, dominate the world with some new PHP projects!
