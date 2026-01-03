---
nid: 2737
title: "Set up BLT and Drupal VM entirely within Windows 10"
slug: "set-blt-and-drupal-vm-entirely-within-windows-10"
date: 2017-01-31T02:15:51+00:00
drupal:
  nid: 2737
  path: /blog/2017/set-blt-and-drupal-vm-entirely-within-windows-10
  body_format: markdown
  redirects: []
tags:
  - blt
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - git
  - github
  - ubuntu
  - vagrant
  - windows
  - windows 10
---

<p style="text-align: center;">{{< figure src="./blt-setup-complete-windows-10.png" alt="BLT - Setup complete on Windows 10" width="650" height="366" class="insert-image" >}}</p>

Quite often, I get inquiries from developers about how to get Drupal VM working on Windows 10—and this is often after encountering error after error due to many different factors. Just for starters, I'll give a few tips for success when using Drupal VM (or most any Linux-centric dev tooling or programming languages) on Windows 10:

  - If at all possible, run as much as possible in the Windows Subsystem for Linux with Ubuntu Bash. Some things don't work here yet (like calling Windows binaries from WSL), but hopefully a lot will be improved by the next Windows 10 update (slated for Q2 2017). It's basically an Ubuntu 14.04 CLI running inside Windows.
  - When using Vagrant, run `vagrant plugin install vagrant-vbguest` and `vagrant plugin install vagrant-hostsupdater`. These two plugins make a lot of little issues go away.
  - If you need to use SSH keys for anything, remember that the _private_ key (`id_rsa`) is secret. Don't share it out! The _public_ key (e.g. `id_rsa.pub`) can be shared freely and should be added to your GitHub, Acquia, etc. accounts. And you can take one public/private key pair and put it anywhere (e.g. copy it from your Mac to PC, inside a VM, wherever). Just be careful to protect the private key from prying eyes.
  - If you're getting errors with any step along the way, copy out parts of the error message that seem relevant and search Google and/or the [Drupal VM issue queue](https://github.com/geerlingguy/drupal-vm/issues). Chances are 20 other people have run into the exact problem before. There's a reason I ask everyone to submit issues to the GitHub tracker and not to my email!

Now, down to the nitty-gritty. One group of developers had a requirement that everyone only use Windows 10 to do everything. On most projects I'm involved with, at least one or two developers will have a Linux or macOS environment, and that person would be the one to set up BLT.

But if you need to set up BLT and Drupal VM entirely within Windows, there are a few things you need to do unique to the Windows environment, due to the fact that Windows handles CLIs, line endings, and symlinks differently than other OSes.

I created a video/screencast of the entire process (just to prove to _myself_ it was reliably able to be rebuilt), which I've embedded below, and I'll also post the detailed step-by-step instructions (with extra notes and cautionary asides) below.

## Video / Screencast

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/D60Ifoo0t08" frameborder='0' allowfullscreen></iframe></div>

## Step-by-step instructions

  1. Install the [Windows Subsystem for Linux with Ubuntu Bash](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide).
  2. Install [Vagrant](https://www.vagrantup.com/downloads.html).
    1. You should also install the following: `vagrant plugin install vagrant-vbguest` and `vagrant plugin install vagrant-hostsupdater`. This helps make things go more smoothly.
  3. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
  4. Open Ubuntu Bash.
  5. Install PHP and Composer (no need for Node.js at this time) following [these BLT Windows install directions](http://blt.readthedocs.io/en/8.x/readme/windows-install/#install-php-nodejs-git-and-composer).
  6. Set up your Git username and password following [these BLT directions](http://blt.readthedocs.io/en/8.x/readme/windows-install/#other-required-setup).
  7. Run the commands inside the [BLT - creating a new project](http://blt.readthedocs.io/en/8.x/readme/creating-new-project/#creating-a-new-project-with-blt) guide.
    1. Note that the `composer create-project` command could take a while (5-10 minutes usually, but could be slower).
    2. If it looks like it's not really doing _anything_, try pressing a key (like down arrow); the Ubuntu Bash environment can get temporarily locked up if you accidentally scroll down.
  8. When you get to the `blt vm` step, run that command, but expect it to fail with a red error message (as of _Windows 10 Anniversary Update_ the WSL can't easily call out to Windows executables from the Ubuntu Bash environment... therefore it fails to see that VirtualBox is installed in Windows since it's only able to see executables in the Ubuntu virtual environment.).
  9. Install [Cmder](http://cmder.net) (preferred), [Cygwin](https://www.cygwin.com), or [Git for Windows](https://git-for-windows.github.io).
  19. Open Cmder.
    1. You need to run Cmder as an administrator (otherwise BLT's Composer-based symlinks go nuts). In Cmder, right-click on the toolbar, click 'New Console...', then check the 'Run as administrator' checkbox and click Start.
    2. You can use other Bash emulators for this (e.g. Cygwin, Git Bash, etc.) as long as they support SSH and are run as Administrator.
    3. When Microsoft releases the Windows 10 update post-Anniversary-update, the WSL _might_ be able to do everything. But right now it's close to impossible to reliably call Windows native exe's from Ubuntu Bash, so don't even try it.
  11. `cd` into the directory created by the `composer create-project` command (e.g. `projectname`).
    1. Note that Ubuntu Bash's home directory is located in your Windows user's home directory, in a path like `C:\Users\[windows-username]\AppData\Local\lxss\home\[ubuntu-username]`.
  12. Run `vagrant up` to build Drupal VM.
    1. Note that it will take anywhere from 5-25 minutes to bring up Drupal VM, depending on your PC's speed and Internet connection.
  13. Once `vagrant up` completes, run `vagrant ssh` to log into the VM.
  14. _From this point on, all or most of your local environment management will take place inside the VM!_
  15. Make sure you add your SSH private key to the Vagrant user account inside Drupal VM (so you can perform actions on the codebase wherever you host it (e.g. BitBucket, GitHub, GitLab, etc.) and through Acquia Cloud).
    1. You can create a new key pair with `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"` if you don't have one already.
    2. Make sure your SSH public key (`id_rsa.pub` contents) is also in your Acquia Cloud account (under 'Credentials'), and GitHub (under 'SSH Keys') or whatever source repository your team uses.
  16. Inside the VM, `cd` into the project directory (`cd /var/www/[projectname]`).
  17. Delete Composer's vendor/bin directory so Composer can set it up correctly inside the VM: `sudo rm -rf vendor/bin`.
  18. Run `composer install`.
    1. If this fails the first time, you may be running a version of BLT that requires [this patch](https://github.com/acquia/blt/pull/1018). If so, run the command `sudo apt-get install -y php5.6-bz2` (using the `php_version` you have configured in `box/config.yml` in place of `5.6`).
    2. If this has weird failures about paths to blt or phing, you might not be running Cmder as an administrator. Restart the entire process from #12 above.
  19. Run `blt local:setup` to install the project locally inside Drupal VM.
    1. If this fails with a warning about `insecure_private_key` or something along those lines, you need to edit your `blt/project.local.yml` file and update the `drush.aliases.local` key to `self` (instead of `projectname.local`). BLT presumes you'll run `blt` commands _outside_ the VM, but when you run them _inside_, you need to override this behavior.
  20. On your host machine, open up a browser and navigate to `http://local.projectname.com/` (where the URL is the one you have configured in `blt/project.yml` under `project.local.hostname`).

CONGRATULATIONS! If all goes well, you should have a BLT-generated project running inside Drupal VM on your Windows 10 PC! You win the Internet for the day.

## Next Steps

If you want to push this new BLT-generated project to a Git repository, make sure you have a public/private key pair set up inside Drupal VM, then in the project root, add the remote Git repository as a new `remote` (e.g. `git remote add origin user@github.com:path/to/repo.git`), then push your code to the new remote (e.g. `git push -u origin master`).

Now, other developers can pull down the codebase, follow a similar setup routine to run `composer install`, then bring up the VM and start working inside the VM environment as well!
