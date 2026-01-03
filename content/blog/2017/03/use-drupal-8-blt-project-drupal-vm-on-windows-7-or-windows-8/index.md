---
nid: 2758
title: "Use a Drupal 8 BLT project with Drupal VM on Windows 7 or Windows 8"
slug: "use-drupal-8-blt-project-drupal-vm-on-windows-7-or-windows-8"
date: 2017-03-22T23:09:31+00:00
drupal:
  nid: 2758
  path: /blog/2017/use-drupal-8-blt-project-drupal-vm-on-windows-7-or-windows-8
  body_format: markdown
  redirects:
    - /win-7-dvm-blt
aliases:
  - /win-7-dvm-blt
tags:
  - acquia
  - blt
  - cmder
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - tutorial
  - vagrant
  - windows
  - windows 7
  - windows 8
---

Windows 10 is the only release Acquia's BLT [officially supports](http://blt.readthedocs.io/en/8.x/readme/windows-install/). But there are still many people who use Windows 7 and 8, and most of these people don't have control over what version of Windows they use.

{{< figure src="./windows-7-blt-drupal-vm.jpg" alt="Windows 7 - Drupal VM and BLT Setup Guide" width="650" height="366" class="insert-image" >}}

Drupal VM has supported Windows 7, 8, and 10 since I started building it a few years ago (at that time I was still running Windows 7), and using a little finesse, you can actually get an entire modern BLT-based Drupal 8 project running on Windows 7 or 8, as long as you do all the right things, as will be demonstrated in this blog post.

Note that this setup is not recommended—you should try as hard as you can to either upgrade to Windows 10, or switch to Linux or macOS for your development workstation, as setup and debugging are _much_ easier on a more modern OS. However, if you're a sucker for pain, have at it! The process below is akin to the [Apollo 13 Command Module startup sequence](http://spectrum.ieee.org/aerospace/space-flight/apollo-13-we-have-a-solution-part-3):

> It required the crew—in particular the command module pilot, Swigert—to perform the entire power-up procedure in the blind. If he made a mistake, by the time the instrumentation was turned on and the error was detected, it could be too late to fix. But, as a good flight controller should, Aaron was confident his sequence was the right thing to do.

Following the instructions below, you'll be akin to Swigert: there are a number of things you have to get working correctly (in the right sequence) before BLT and Drupal VM can work together in Windows 7 or Windows 8. And once you have your environment set up, you should do everything besides editing source files and running Git commands inside the VM (and, if you want, you can actually do _everything_ inside the VM. For more on why this is the case, please read my earlier post: [Developing with VirtualBox and Vagrant on Windows](//www.jeffgeerling.com/blog/2016/developing-virtualbox-and-vagrant-on-windows).

Here's a video overview of the entire process (see the detailed instructions below the video):

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/LB0NzX3KdS4" frameborder='0' allowfullscreen></iframe></div>

## Upgrade PowerShell

Windows 7 ships with a very old version of PowerShell (2.0) which is incompatible with Vagrant, and causes `vagrant up` to hang. To work around this problem, you will need to upgrade to PowerShell 4.0:

  1. Visit the [How to Install Windows PowerShell 4.0](https://social.technet.microsoft.com/wiki/contents/articles/21016.how-to-install-windows-powershell-4-0.aspx) guide.
  2. Download the `.msu` file appropriate for your system (most likely `Windows6.1-KB2819745-x64-MultiPkg.msu`).
  3. Open the downloaded installer.
  4. Run through the install wizard.
  5. Restart your computer when the installation completes.
  6. Open Powershell and enter the command `$PSVersionTable.PSVersion` to verify you're running major version `4` or later.

## Install XAMPP (for PHP)

XAMPP will be used for it's PHP installation, but it won't be used for actually running the site; it's just an easy way to get PHP installed and accessible on your Windows computer.

  1. [Download XAMPP](https://www.apachefriends.org/download.html) (PHP 5.6.x version).
  2. Run the XAMPP installer.
  3. XAMPP might warn that UAC is enabled; ignore this warning, you don't need to bypass UAC to just run PHP.
  4. On the 'Select Components' screen, only choose "Apache", "PHP", and "Fake Sendmail" (you don't need to install any of the other components).
  5. Install in the `C:\xampp` directory.
  6. Uncheck the Bitnami checkbox.
  7. When prompted, allow access to the Apache HTTP server included with XAMPP.
  8. Uncheck the 'Start the control panel when finished' checkbox and Finish the installation.
  9. Verify that PHP is installed correctly:
    1. Open Powershell.
    2. Run the command: `C:\xampp\php\php.exe -v`

> Note: If you have PHP installed and working through some other mechanism, that's okay too. The key is we need a PHP executable that can later be run through the CLI.

## Set up Cmder

  1. Download [Cmder](http://cmder.net) - the 'full' installation.
  2. Expand the zip file archive.
  3. Open the `cmder` directory and right-click on the `Cmder` executable, then choose 'Run as administrator'.
    - If you are prompted to allow access to Cmder utilities, grant that access.
  4. Create an alias to PHP: `alias php=C:\xampp\php\php.exe $*`
  5. Verify that the PHP alias is working correctly: `php -v` (should return the installed PHP version).

> Cmder is preferred over [Cygwin](https://www.cygwin.com) because it's terminal emulator works slightly better than `mintty`, which is included with Cygwin. Cygwin can also be made to work, as long as you install the following packages during Cygwin setup: `openssh`, `curl`, `unzip`, `git`.

### Configure Git (inside Cmder)

There are three commands you should run (at a minimum) to configure Git so it can work correctly with the repository:

  1. `git config --global user.name "John Doe"` (use your own name)
  2. `git config --global user.email your_email@example.com` (use an email address associated with your GitHub account)
  3. `git config --global core.autocrlf true` (to ensure correct line endings)

### Install Composer (inside Cmder)

  1. Make sure you're in your home directory: `cd C:\Users\[yourusername]`.
  2. Run the following commands to [download and install Composer](https://getcomposer.org/download/):
    1. Download Composer: `php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"`
    2. Build the Composer executable: `php composer-setup.php`
    3. Delete the setup file: `rm -f composer-setup.php`
  3. Test that Composer is working by running `php composer.phar --version`.

## Create a Private/Public SSH Key Pair to authenticate to GitHub and Acquia Cloud

### Generate an SSH key

All the following commands will be run inside of Cmder.

  1. Inside of Cmder, make sure you're in your home directory: `C:\Users\[yourusername]`
  2. Run the command: `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
    - When prompted for where to save the key, press enter/return (to choose the default path).
    - When prompted to enter a passphrase, press enter/return (to leave it empty).
    - When prompted to enter the same passphrase, press enter/return (to leave it empty).
  3. To get the value of the new public key, run the command: `cat .ssh/id_rsa.pub`
    - Highlight the text that is output (starts with `ssh-rsa` and ends with your email address)
    - Copy the text of the public key

> Note: The public key (`id_rsa.pub`) can be freely shared and added to services where you need to connect. NEVER share the private key (`id_rsa`), as that is a secret that identifies you personally to the services to which you're connecting.

#### Add the SSH key to your GitHub account

  1. Log into [GitHub](https://github.com/)
  2. Go to your account settings (click on your profile image in the top right, then choose 'Settings').
  3. Click on "SSH and GPG keys" in the 'Personal settings' area.
  4. Click "New SSH key" to add your new SSH key.
  5. Add a title (like "Work Windows 7")
  6. Paste your key in the "Key" field.
  7. Click "Add SSH Key" to save the key.

#### Add the SSH key to your Acquia Cloud account

  1. Log into [Acquia Cloud](https://cloud.acquia.com/)
  2. Go to your Profile (click on your profile image in the top right, then choose 'Edit Profile').
  3. Click on "Credentials"
  4. Under "SSH Keys", click "Add SSH Key"
  5. Add a nickname (like "Work_Windows_7")
  6. Paste your key in the "Public key" field.
  7. Click "Add Key" to save the key.

## Set up the BLT-based Drupal project

### Fork the BLT project into your own GitHub account

  1. Log into GitHub.
  2. Visit your project's GitHub repository page.
  3. Click the "Fork" button at the top right to create a clone of the project in your own account.
  4. After GitHub has created the Fork, you'll be taken to your Fork's project page.

### Clone the BLT project to your computer

  1. Click the "Clone or download" button on your Fork's project page.
  2. Copy the URL in the 'Clone with SSH' popup that appears.
  3. Go back to Cmder, and `cd` into whatever directory you want to store the project on your computer.
  4. Enter the command: `git clone [URL that you copied in step 2 above]`
    - If you receive a prompt asking if you want to connect to github.com, type `yes` and press enter/return.
    - Wait for Git to clone the project to your local computer.

> Note: At this time, you may also want to add the 'canonical' GitHub repository as an `upstream` remote repo so you can easily synchronize your codebase with the repository you forked earlier. That way it's easy for you to make sure you're always working on the latest code. This also makes it easier to do things like open Pull Requests on GitHub from the command line using [Hub](https://hub.github.com).

### Install BLT project dependencies

  1. Change directory into the project directory (`cd projectname`).
  2. Ensure you're on the `master` branch by checking the repository's status: `git status`
  3. Move the `composer.phar` file into the project directory: `mv ..\composer.phar .\composer.phar`
  4. Run `php composer.phar install --prefer-source` to ensure everything needed for the project is installed.
    - Wait for Composer to finish installing all dependencies. This could take 10-20 minutes the first time it's run.
    - If the installation times out, run `php composer.phar install --prefer-source` again to pick up where it left off.
    - The installation may warn that patches can't be applied; ignore this warning (we'll reinstall dependencies later).
  5. Move the `composer.phar` file back out of the project directory: `mv composer.phar ..\composer.phar` (in case you ever need it on your host computer again).

> Note: You need to use the `--prefer-source` option when installing to prevent the `ZipArchive::extractTo(): Full extraction path exceed MAXPATHLEN (260)` error. See [this Stack Overflow answer](http://stackoverflow.com/a/29747994) for details.

## Set up the Virtual Machine (Drupal VM)

  1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
  2. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
  3. Restart your computer after installation.
  4. Open Cmder, and `cd` into the project folder (where you cloned the project).
  5. Install recommended Vagrant plugins: `vagrant plugin install vagrant-hostsupdater vagrant-vbguest vagrant-cachier`
    - Note that if you get an error about a space in your username, you will need to add a folder and VAGRANT_HOME environment variable (see [this post](http://stackoverflow.com/a/26217200) for more info).
  6. Create a config file for your VM instance: `touch box/local.config.yml`
  7. Inside the config file, add the following contents (you can use `vi` or some other Unix-line-ending-compatible editor to modify the file):

        vagrant_synced_folder_default_type: ""
        vagrant_synced_folders:
          - local_path: .
            destination: /var/www/projectname
            type: ""
        post_provision_scripts: []

  5. Run `vagrant up`.
    - This will download a Linux box image, install all the prerequisites, then configure it for the Drupal site.
    - This could take 10-20 minutes (or longer), depending on your PC's speed and Internet connection.
    - If the command stalls out and seems to not do anything for more than a few minutes, you may need to restart your computer, then run `vagrant destroy -f` to destroy the VM, then run `vagrant up` again to start fresh.

> Note: If you encounter any errors during provisioning, kick off another provisioning run by running `vagrant provision` again. You may also want to reload the VM to make sure all the configuration is correct after a failed provision—to do that, run `vagrant reload`.

## Log in and start working inside the VM

  1. First make sure that `ssh-agent` is running and has your SSH key (created earlier) loaded: `start-ssh-agent`
  2. Run `vagrant ssh` to log into the VM (your SSH key will be used inside the VM via `ssh-agent`).
  3. Change directories into the project directory: `cd /var/www/projectname`
  4. **Using Windows Explorer** (to avoid access errors), remove the contents of the following directories which Composer will recreate:
    - `vendor`
    - `docroot/core`
    - `docroot/libraries`
    - `docroot/modules/contrib`
    - `docroot/themes/contrib`
    - `docroot/profiles/contrib`
  5. **Back in Cmder**, run `composer install` so all the packages will be reinstalled and linked correctly.
  6. Manually run the BLT post-provision shell script to configure BLT inside the VM: `./vendor/acquia/blt/scripts/drupal-vm/post-provision.sh`
  7. Log out (`exit`), then log back in (`vagrant ssh`) and `cd` back into the project directory.
  8. Use BLT to pull down the latest version of the database and finish building your local environment: `blt local:refresh`

After a few minutes, the site should be running locally, accessible at http://local.projectname.com/

> Note: `ssh-agent` functionality is outside the scope of this post. Basically, it allows you to use your SSH keys on your host machine in other places (including inside Drupal VM) without worrying about manually copying anything. If you want `ssh-agent` to automatically start whenever you open an instance of Cmder, please see Cmder's documentation: [SSH Agent in Cmder](https://github.com/cmderdev/cmder#ssh-agent).
