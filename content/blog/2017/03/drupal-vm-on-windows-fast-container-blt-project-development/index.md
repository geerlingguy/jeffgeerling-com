---
nid: 2759
title: "Drupal VM on Windows - a fast container for BLT project development"
slug: "drupal-vm-on-windows-fast-container-blt-project-development"
date: 2017-03-29T22:57:05+00:00
drupal:
  nid: 2759
  path: /blog/2017/drupal-vm-on-windows-fast-container-blt-project-development
  body_format: markdown
  redirects: []
tags:
  - acquia
  - blt
  - drupal
  - drupal 8
  - drupal planet
  - drupal vm
  - php
  - phpstorm
  - tutorial
  - vagrant
  - windows
  - windows 7
---

## AKA "Supercharged Windows-based Drupal development"

> **tl;dr**: Use either PhpStorm or a Samba share in the VM mounted on the host instead of using a (slow) Vagrant synced folder, and use Drupal VM 4.4's new `drupal_deploy` features. See the video embedded below for all the details!

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/VBvPw-b9pe8" frameborder='0' allowfullscreen></iframe></div>

I've often mentioned that Windows users who want to build modern Drupal sites and apps are going to have a bit of a difficult time, and even wrote a long post about why this is the case ([Developing with VirtualBox and Vagrant on Windows](//www.jeffgeerling.com/blog/2016/developing-virtualbox-and-vagrant-on-windows)).

But for a long time, I haven't had much incentive to actually get my hands dirty with a Windows environment. Sure, I would make sure Drupal VM minimally ran inside Windows 10... but there were a lot of little inefficiencies in the recommended setup process that would lead to developers getting frustrated with the sluggish speed of the VM!

Since a client I'm currently helping is stuck on Windows 7 for the short-term, and can't do internal development on a Mac or Linux (other OSes are not allowed on workstations), I decided to try to set up a project how _I_ would set it up if I had to work in that situation.

Basically, how do you get Drupal VM to perform as well (or better!) on a Windows 7 machine as it does on a Mac, while still allowing a native IDE (like PHPStorm or Notepad++) to be used?

After a couple days of tinkering, I've found the most stable solution, and that is to build Drupal VM 'outside in'—meaning you build your project inside Drupal VM, then share a folder from Drupal VM to Windows, currently using Samba (but in the future, [SSHFS might be a viable option](https://github.com/dustymabe/vagrant-sshfs/issues/74) for Windows too!).

Here's how I used Drupal VM to run and develop an [Acquia BLT](https://github.com/acquia/blt)-based project locally on Windows 7:

## Contents

  - [Install required software](#install)
  - [Create an SSH public/private key pair](#keys)
  - [Set your SSH key to run inside Pageant](#pageant)
  - [Build Drupal VM](#drupalvm)
  - [Set up BLT inside the VM](#blt)
  - [Use PhpStorm to work on the codebase](#phpstorm)
  - [Configure a reverse-mounted shared folder](#reverse-share)
  - [Conclusion](#conclusion)

<a name="install"></a>

## Install required software

To make this work, you will need to install the following software:

  1. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
  1. [Vagrant](https://www.vagrantup.com/downloads.html)
  1. [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) (used for Pageant)
  1. [Powershell 4.0+](https://social.technet.microsoft.com/wiki/contents/articles/21016.how-to-install-windows-powershell-4-0.aspx) (if on Windows 7)
  1. [Cmder](http://cmder.net) ('full' download)

<a name="keys"></a>

## Create an SSH public/private key pair

{{< figure src="./cmder-generate-ssh-rsa-key.jpg" alt="Generate an SSH key pair in Cmder" width="650" height="406" class="insert-image" >}}

Before doing any work with a project with code hosted on GitHub, Acquia Cloud, Redmine, or elsewhere, you need to create an SSH key pair so you can authenticate yourself to the main Git repository.

  1. Open Cmder (right click and 'Run as Administrator')
  1. Create an SSH key in the default location: `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
      - Press 'enter' three times to accept the defaults.
  1. Print the contents of the _public_ key: `cat C:\Users\[youraccount]\.ssh\id_rsa.pub`
  1. Copy the entire contents (from `ssh-rsa` to the end of your email address).
  1. Add the copied key into GitHub under Profile icon > Settings > SSH and GPG keys.
      - Also add the key into any other relevant service (e.g. Acquia Cloud under Profile > Credentials).

<a name="pageant"></a>

## Set your SSH key to run inside Pageant

{{< figure src="./puttygen-import-key-convert.jpg" alt="Puttygen - Import and convert SSH key to ppk" width="650" height="406" class="insert-image" >}}

Due to [a bug in the current version of Vagrant](https://github.com/mitchellh/vagrant/issues/8415), you need to use Pageant to allow Vagrant to use your SSH key inside the VM when running commands like `vagrant up` and `vagrant provision`.

Also, Pageant requires a specially-formatted version of your key, so you'll need to use `puttygen.exe` to convert the key before loading it into Pageant.

  1. Install [PuTTY](http://www.putty.org/).
  2. Open `puttygen.exe` (inside `C:\Program Files\PuTTY`).
  3. Select "Conversions > Import key".
  4. In the 'Actions' section, click "Save private key".
  5. In the save dialog, save the file as `id_rsa.ppk` with type "PuTTY Private Key Files (*.ppk)".
  6. Close `puttygen.exe`.
  7. Open `pageant.exe` (this opens a taskbar item).
  8. Right click on the Pageant item in the taskbar, and choose 'Add key', then navigate to where you saved `id_rsa.ppk`.
  9. You should also ensure Pageant runs on system startup to ensure keys are always available when you need them. See [this guide](https://winscp.net/eng/docs/ui_pageant) for further instructions on how to have `pageant.exe` start on boot.

<a name="drupalvm"></a>

## Build Drupal VM

{{< figure src="./drupal-vm-windows-eejgeerling.jpg" alt="Drupal VM Dashboard page on Windows 7" width="650" height="406" class="insert-image" >}}

At this point, we're ready to build a local development environment with [Drupal VM](https://www.drupalvm.com).

> Note: In the rest of this guide, substitute `projectname` for your project's own machine name.

  1. Open Cmder (right click and 'Run as Administrator')
  1. Run `start-ssh-agent` (so your SSH key is loaded and can be used in the VM).
    - When using Pageant this is not strictly required, but once [this bug](https://github.com/mitchellh/vagrant/issues/8415) is resolved, you won't need Pageant at all, and you can just use `start-ssh-agent`.
  1. Clone a copy of Drupal VM to your computer: `git clone https://github.com/geerlingguy/drupal-vm.git`
  1. Change directories into Drupal VM: `cd drupal-vm`
  1. Create a shell script to create your project's directory and set it's permissions correctly:
    1. `touch examples/scripts/setup.sh`
    2. Open your editor of choice (e.g. Notepad++) and edit `setup.sh` (be sure to use Unix line endings!):

            #!/bin/bash
            mkdir -p /var/www/projectname
            chown vagrant:vagrant /var/www/projectname

  1. Create a `config.yml` file: `touch config.yml`
  1. Open your editor of choice (e.g. Notepad++) and edit `config.yml` (be sure to use Unix line endings!)—also make sure the `drupal_deploy_repo` varaible is set to the correct GitHub repository you want to use as your `origin` remote:

        ---
        vagrant_synced_folders: []
        vagrant_synced_folder_default_type: ""
        
        vagrant_hostname: local.projectname.com
        vagrant_machine_name: projectname
        vagrant_ip: 192.168.88.25
        
        drupal_deploy: true
        drupal_deploy_repo: "git@github.com:github-username/projectname.git"
        drupal_deploy_version: master
        drupal_deploy_update: true
        drupal_deploy_dir: "/var/www/projectname"
        drupal_deploy_accept_hostkey: yes
        drupal_core_path: "{{ drupal_deploy_dir }}/docroot"
        ssh_home: "{{ drupal_deploy_dir }}"
        
        drupal_build_composer: false
        drupal_composer_path: false
        drupal_build_composer_project: false
        drupal_install_site: false
        
        firewall_allowed_tcp_ports:
          - "22"
          - "25"
          - "80"
          - "81"
          - "443"
          - "4444"
          - "8025"
          - "8080"
          - "8443"
          - "8983"
          - "9200"
          # For reverse-mount Samba share.
          - "137"
          - "138"
          - "139"
          - "445"
        
        # Run the setup script.
        pre_provision_scripts:
          - "../examples/scripts/setup.sh"
        
        # BLT-specific overrides.
        vagrant_box: geerlingguy/ubuntu1404
        
        drupal_db_user: drupal
        drupal_db_password: drupal
        drupal_db_name: drupal
        
        configure_drush_aliases: false
        
        # Use PHP 5.6.
        php_version: "5.6"
        php_packages_extra:
          - "php{{ php_version }}-bz2"
          - "php{{ php_version }}-imagick"
          - imagemagick
        
        nodejs_version: "4.x"
        nodejs_npm_global_packages:
          - name: bower
          - name: gulp-cli
        drupalvm_user: vagrant
        nodejs_install_npm_user: "{{ drupalvm_user }}"
        npm_config_prefix: "/home/{{ drupalvm_user }}/.npm-global"
        installed_extras:
          - adminer
          - drupalconsole
          - drush
          - mailhog
          - nodejs
          - selenium
          - xdebug
        
        # XDebug configuration.
        # Change this value to 1 in order to enable xdebug by default.
        php_xdebug_default_enable: 0
        php_xdebug_coverage_enable: 0
        # Change this value to 1 in order to enable xdebug on the cli.
        php_xdebug_cli_enable: 0
        php_xdebug_remote_enable: 1
        php_xdebug_remote_connect_back: 1
        # Use PHPSTORM for PHPStorm, sublime.xdebug for Sublime Text.
        php_xdebug_idekey: PHPSTORM
        php_xdebug_max_nesting_level: 256
        php_xdebug_remote_port: "9000"

  1. Back in Cmder, run `vagrant up`
  1. Wait for Drupal VM to complete its initial provisioning. If you get an error, try running `vagrant provision` again.

<a name="blt"></a>

## Set up BLT inside the VM

{{< figure src="./blt-local-refresh-drupal-vm-cmder-windows-7.jpg" alt="BLT local refresh command in Cmder in Windows 7" width="650" height="406" class="insert-image" >}}

  1. Run `vagrant ssh` to log into the VM.
  1. Make sure you're in the project root directory (e.g. `cd /var/www/projectname`).
  1. Run `composer install` to make sure all project dependencies are installed.
  1. Create `blt/project.local.yml` with the following contents:

        drush:
          aliases:
            local: self

  1. Run [the command on this line](https://github.com/acquia/blt/blob/8.6.15/scripts/drupal-vm/post-provision.sh#L9) to set up the `blt` alias inside the VM.
    - Note: After [this BLT bug](https://github.com/acquia/blt/issues/1264) is fixed and your project is running a version of BLT with the fix included, you can just run: `./vendor/acquia/blt/scripts/drupal-vm/post-provision.sh`
  1. Type `exit` to exit Vagrant, then `vagrant ssh` to log back in.
  1. Make sure you're back in the project root directory.
  1. Correct NPM permissions: `sudo chown -R $USER:$USER ~/.npm-global`
  1. Run `blt local:refresh` to pull down the database and run setup tasks.
    - Note that the first time you connect, you'll need to type `yes` when it asks if you want to accept the staging site's host key.

At this point, you can use the site locally at `http://local.projectname.com/`, and manage the codebase inside the VM.

<a name="phpstorm"></a>

## Use PhpStorm to work on the codebase

For speed and compatibility reasons, this method of using Drupal VM to run a BLT project is done 'outside in', where everything is done inside the VM. But if you want to edit the codebase in a native Windows-based editor or IDE, you need access to the project files.

[PhpStorm](https://www.jetbrains.com/phpstorm/) is a fully-featured PHP development IDE from Jetbrains, and is used by many in the Drupal community due to its speed and deep integration with PHP projects and Drupal in particular. You can download a free trial, or acquire a license for PhpStorm to use it.

One benefit of using PhpStorm is that it can work directly with the project codebase inside Drupal VM, so you don’t need to configure a shared folder.

  1. Open PhpStorm.
  1. Click “Create New Project from Existing Files” (if you are in a project already, choose File > “New Project from Existing Files…”).
  1. Choose the option “Web server is on remote host, files are accessible via FTP/SFTP/FTPS.” and then click “Next”.
  1. For “Project name”, enter `Projectname`
  1. Leave everything else as default, and click “Next”.
  1. In the ‘Add Remote Server’ step, add the following information:
    1. Name: `Drupal VM`
    1. Type: `SFTP`
    1. SFTP host: `local.projectname.com`
    1. Port: `22`
    1. Root path: `/var/www/projectname`
    1. User name: `vagrant`
    1. Auth type: `Password`
    1. Password: `vagrant`
    1. Click ‘Test SFTP connection’ and accept the host key if prompted.
    1. Ensure the “Web server root URL” is correct (should be “http://local.projectname.com”).
  1. Click “Next”
  1. Click on the “Project Root” item in the “Choose Remote Path” dialog, and click “Next”.
    1. Leave the ‘Web path’ empty, and click “Finish”.
  1. PhpStorm will start ‘Collecting files’ (this could take a couple minutes).
  1. Change the Deployment configuration in the menu option Tools > Deployment > “Configuration…”
  1. Click on ‘Excluded Paths’ and add deployment paths containing things like Composer and Node.js dependencies:
    1. “/vendor”
    1. “/docroot/themes/custom/project_theme/node_modules”
  1. Enable automatic uploads in menu option Tools > Deployment > “Automatic Upload”

From this point on, you should be able to manage the codebase within PhpStorm. You can also open an SSH session inside the VM directly from PhpStorm—just go to the menu option Tools > “Start SSH Session…”

PhpStorm might also ask if this is a Drupal project—if so you can click on the option to enable it, and make sure the Drupal version is set to the proper version for your site.

> **Note**: If you perform git operations on the codebase running inside the VM, or other operations like configuration exports which generate new files or update existing files, you need to manually sync files back to PhpStorm (e.g. click on project folder and click menu option Tools > Deployment > "Download from Drupal VM". At this time, only automatic _upload_ of files you edit within PhpStorm is supported. See the issue [Auto Refresh of Remote Files](https://youtrack.jetbrains.com/issue/WI-1284) for more info and progress towards an automated solution.

> **Note 2**: If you encounter issues with CSS and JS aggregation, or things like Stage File Proxy showing logged errors like `Stage File Proxy encountered an unknown error by retrieving file [filename]`, you might need to manually create the public files folder inside the project docroot (e.g. inside Drupal VM, run `mkdir files` wherever the public files directory should be.

<a name="reverse-share"></a>

## Configure a reverse-mounted shared folder

{{< figure src="./network-location-windows-7-drupal-vm-samba.jpg" alt="Add a Network Location to Windows 7 from Drupal VM&#39;s Samba share" width="650" height="406" class="insert-image" >}}

If you don't have a PhpStorm license, or prefer another editor or IDE that doesn't allow working on remote codebases (via SFTP), then you can manually create a Samba share instead. In this case, we're going to use Samba, which requires the TCP ports listed in the customized `config.yml` file above to be open (`137`, `138`, `139`, and `445`).

  1. (Inside the VM) Install Samba: `sudo apt-get install samba`
  1. Add the following contents to the bottom of `/etc/samba/smb.conf`:

        [projectname-share]
           comment = projectname
           path = /var/www/projectname
           guest ok = yes
           force user = vagrant
           browseable = yes
           read only = no
           writeable = yes
           create mask = 0777
           directory mask = 0777
           force create mode = 777
           force directory mode = 777
           force security mode = 777
           force directory security mode = 777

  1. Restart the Samba daemon: `sudo service smbd restart` (`sudo systemctl restart smbd.service` on systems with systemd).
  1. Set Samba to start on boot: `sudo update-rc.d samba defaults` (`sudo systemctl enable smbd.service` on systems with systemd).
  1. (Back on Windows) Mount the shared folder from Windows Explorer: `\\local.projectname.com\projectname-share`
  1. You can now browse files from within Windows just as you would any other folder.
  1. If you'd like, you can 'Map a new network drive' for more convenient access:
    1. Right-click while browsing 'Computer' and select "Add a network location"
    1. Go through the wizard, and add the shared folder location you used above (`\\local.projectname.com\projectname-share`).
    1. Save the new network location with a descriptive name (e.g. "BEAGOV").
    1. Now, you can just go to Computer and open the network location directly.

Notes:

  - You can only access the network location when the VM is running. If it is offline, files are inaccessible.
  - You should always use Unix line endings in your editor to prevent strange errors.
  - You can set `guest ok = no` if you want to make sure the shared directory is protected by a login. However, unless you change the Drupal VM defaults, the share should only be accessible internally on your computer (and not on the wider LAN).
  - You can also open a folder as a workspace, for example in Notepad++, by manually entering the network path (`\\local.projectname.com\projectname-share`).
  - Global operations (e.g. project-wide search and replace) are going to be _very_ slow if done on the Windows side. It's better to do that either in the VM itself (using tools like `grep` or `vim`), or on another computer that can work on the files locally!

<a name="conclusion"></a>

## Conclusion

Using this 'outside in' approach makes it so you can get near-native performance when building Drupal sites locally on Windows 7, 8, or 10. It requires a little extra effort to get it working correctly, and there are still a couple small tradeoffs, but it's a lot faster and easier to set up than if you were to use normal shared folders!

Hopefully the SSHFS issues I mentioned earlier are fixed soon, so that the reverse shared folder will be easier to configure (and not require any manual steps inside the VM!).

Also, note that you could use the [`vagrant-exec`](https://github.com/p0deje/vagrant-exec) plugin to run commands inside the VM without first logging in via `vagrant ssh`.
