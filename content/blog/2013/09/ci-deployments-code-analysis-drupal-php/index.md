---
nid: 2478
title: "CI: Deployments and Static Code Analysis with Drupal/PHP"
slug: "ci-deployments-code-analysis-drupal-php"
date: 2013-09-25T17:54:25+00:00
drupal:
  nid: 2478
  path: /blogs/jeff-geerling/ci-deployments-code-analysis-drupal-php
  body_format: full_html
  redirects: []
tags:
  - ci
  - code quality
  - continuous integration
  - deployment
  - devops
  - drupal
  - drupal planet
  - jenkins
  - phing
  - php
  - sonarqube
aliases:
  - /blogs/jeff-geerling/ci-deployments-code-analysis-drupal-php
---

<p style="text-align: center;">{{< figure src="./sonarqube-code-quality-title.png" alt="CI: Deplyments and Code Quality" width="500" height="214" >}}</p>

<blockquote>
<a href="http://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn't_read">tl;dr</a>: Get the <a href="https://github.com/geerlingguy/drupalci-sonar-jenkins">Vagrant profile for Drupal/PHP Continuous Integration Server</a> from GitHub, and create a new VM (see the README on the GitHub project page). You now have a full-fledged Jenkins/Phing/SonarQube server for PHP/Drupal CI.
</blockquote>

In this post, I'm going to explain how <a href="http://jenkins-ci.org/">Jenkins</a>, <a href="http://www.phing.info/">Phing</a> and <a href="http://www.sonarqube.org/">SonarQube</a> can help you with your Drupal (or hany PHP-based project) deployments and code quality, and walk you through installing and configuring them to work with your codebase. Bear with me... it's a long post!

<h2 id="code-deployment">Code Deployment</h2>

If you manage more than one environment (say, a development server, a testing/staging server, and a live production server), you've probably had to deal with the frustration of deploying changes to your code to these servers.

In the old days, people used FTP and manually copied files from environment to environment. Then FTP clients became smarter, and allowed somewhat-intelligent file synchronization. Then, when version control software became the norm, people would use CVS, SVN, or more recently Git, to push or check out code to different servers.

All the aforementioned deployment methods involved a lot of manual labor, usually involving an FTP client or an SSH session. Modern server management tools like Ansible can help when there are more complicated environments, but wouldn't everything be much simpler if there were an easy way to deploy code to specific environments, especially if these deployments could be automated to either run on a schedule or whenever someone commits something to a particular branch?

<p style="text-align: center;">{{< figure src="./jenkins-logo.png" alt="Jenkins Logo" width="342" height="110" >}}</p>

Enter <a href="http://jenkins-ci.org/">Jenkins</a>. Jenkins is your deployment assistant on steroids. Jenkins works with a wide variety of tools, programming languages and systems, and allows the automation (or radical simplification) of tasks surrounding code changes and deployments.

In my particular case, I use a dedicated Jenkins server to monitor a specific repository, and when there are commits to a development branch, Jenkins checks out that branch from Git, runs some PHP code analysis tools on the codebase using <a href="http://www.phing.info/">Phing</a>, archives the code and other assets in a .tar.gz file, then deploys the code to a development server and runs some drush commands to complete the deployment.

<h2 id="static-code-analysis-code-review">Static Code Analysis / Code Review</h2>

If you're a solo developer, and you're the only one planning on ever touching the code you write, you can use whatever coding standards you want—spacing, variable naming, file structure, class layout, etc. don't really matter.

But if you ever plan on sharing your code with others (as a contributed theme or module), or if you need to work on a shared codebase, or if there's ever a possibility you will pass on your code to a new developer, it's a good idea to follow coding standards and write good code that doesn't contain <a href="http://www.osnews.com/story/19266">too many WTFs/min</a>.

<p style="text-align: center;">{{< figure src="./sonarqube-logo.png" alt="SonarQube Logo" width="125" height="123" >}}</p>

The easiest way to do this is to use static code analysis tools like <a href="http://phpmd.org/">PHP Mess Detector</a>, <a href="http://pear.php.net/package/PHP_CodeSniffer/">PHP CodeSniffer</a> (with Drupal's Coder module), and the <a href="https://github.com/sebastianbergmann/phpcpd">PHP Copy/Paste Detector</a>.

It's great to be able to use any of these tools individually, but let's face it—unless they're set up to run and give you reports in some automated fashion, there's little chance you're going to take time out of your busy development schedule to run these helpful code review tools, especially if the boring plain text reports they generate are long.

Jenkins and Phing together will do the heavy lifting of grabbing code from your repository and running it through all these analysis tools (as well as PHPUnit for automated unit testing, or SimpleTest). But we're going to take this to the next level; instead of just leaving you with a long text file to decipher, we're going to use another awesome tool, <a href="http://www.sonarqube.org/">SonarQube</a>, to generate (automatically) graphs, charts, and custom dashboards showing statistics like lines of code and commented lines of code over time, method/function complexity, coding standards violations, etc.

SonarQube helps highlight areas of your codebase where you can get the most ROI for your cleanup efforts; it's easy to spot that one module or template where a bunch of quickly-written messy code might be lurking, waiting to destroy a week of development time because it's lacking documentation, poorly-written, or an incredibly complicated mess!

<h2 id="putting-it-all-together">Putting It All Together</h2>

<p style="text-align: center;">{{< figure src="./vagrant-logo.png" alt="Vagrant Logo" width="164" height="200" >}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{< figure src="./virtualbox-logo.png" alt="VirtualBox Logo" width="200" height="200" >}}</p>

Now, into the nitty gritty. We're going to build ourselves a virtual machine that has everything configured to do all the things I mentioned above, and will be flexible enough to allow us to add more code quality analysis (like Drupal SimpleTest integration) and deployment options over time.

We'll build this VM using Vagrant with VirtualBox, which means the VM can be built and rebuilt on any Mac, Windows, or Linux PC. The configuration can also be split up to create separate servers for all the different components—a Jenkins server with Phing and SonarQube Runner to do the deployments and code analysis, and a SonarQube server for the pretty graphs and overview of our code quality.

The complete VM is available on GitHub (<a href="https://github.com/geerlingguy/drupalci-sonar-jenkins">Vagrant profile for Drupal/PHP Continuous Integration Server</a>), but I'll go through the configuration step by step. This guide assumes you're running CentOS or some other RHEL-flavored Linux, but it should be easily adaptable to other environments that use <code>apt</code> or another package manager instead of <code>yum</code>. Additionally, I am working on rebuilding this Vagrant profile using Ansible instead of shell scripts, but for now, shell scripts will have to do :-)
<h3 id="installing-jenkins">Installing Jenkins</h3>

<em>Note: I will be using the hostname 'jenkins-sandbox' for this server, and Jenkins will run on port 8080.</em>

To install Jenkins, you need to be running Java (in my situation, 1.6.0 is the latest version offered by the standard CentOS repos):

```
yum install --quiet -y java-1.6.0-openjdk
```

After Java is installed and configured (check the version with <code>java -version</code>), install Jenkins from the Jenkins RPM:

```
wget --quiet -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
rpm --quiet --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key
yum install --quiet -y jenkins
```

Configure Jenkins to start automatically after system boot:

```
service jenkins start
chkconfig jenkins on
```

Force Jenkins to update it's plugin directory (you can do this by visiting Jenkins' update center in your browser, but we'll do it via CLI since it's faster and can be part of the automated server build):

```
curl -s -L http://updates.jenkins-ci.org/update-center.json | sed '1d;$d' | curl -s -X POST -H 'Accept: application/json' -d @- http://jenkins-sandbox:8080/updateCenter/byId/default/postBack
```

Install Jenkins' CLI tool so you can run later commands via the command line instead of having to click through the interface:

```
wget --quiet http://jenkins-sandbox:8080/jnlpJars/jenkins-cli.jar
```

Install the Jenkins phing and sonar plugins:

```
java -jar jenkins-cli.jar -s http://jenkins-sandbox:8080/ install-plugin phing
java -jar jenkins-cli.jar -s http://jenkins-sandbox:8080/ install-plugin sonar
```

You can import and export jobs in Jenkins using XML files if you have the Jenkins CLI installed, using the following syntax:

```
java -jar jenkins-cli.jar -s http://jenkins-sandbox:8080/ get-job MyJenkinsJob > /path/to/exported/MyJenkinsJob.xml
java -jar jenkins-cli.jar -s http://jenkins-sandbox:8080/ create-job MyJenkinsJob < /path/to/exported/MyJenkinsJob.xml
```

Restart Jenkins so everything works correctly:

```
service jenkins restart
```

Now that Jenkins is installed, you could visit http://jenkins-sandbox:8080/ in your browser and start playing around in the UI... but we're going to keep moving along, getting the rest of our PHP CI system up and running.
<h3 id="installing-php-and-phing">Installing PHP and Phing</h3>

Since we're going to be building PHP projects in Jenkins, and using a variety of PHP code analysis tools to inspect and test our code, we need to install PHP, PEAR, Phing, and some other plugins.

First, let's install PHP, PEAR, and some other basic dependencies:

```
yum install --quiet -y php php-devel php-xml php-pear ImageMagick
pear channel-update pear.php.net
pear config-set auto_discover 1
```

Then, install PHPUnit if you'd like to run unit tests against your code:

```
pear channel-discover pear.phpunit.de
pear channel-discover pear.symfony.com
pear install phpunit/PHPUnit
```

Install the PHP Copy/Paste Detector (this will check for duplicate code that could be merged to reduce the lines of code you need to maintain):

```
pear install pear.phpunit.de/phpcpd
```

Install the PHP Mess Detector (this will check for poor code quality, overly-complicated code, and code that will introduce lots of technical debt).

```
pear channel-discover pear.phpmd.org
pear channel-discover pear.pdepend.org
pear install phpmd/PHP_PMD
```

Install PHP CodeSniffer (this will 'sniff' your code for bad formatting and coding standards violations):

```
pear install PHP_CodeSniffer
```

Install XDebug (useful for debugging PHP code, and used by some other tools):

```
pecl install xdebug
```

Install Phing (which will be used to coordinate the running of all the other tools we just installed against your code):

```
pear channel-discover pear.phing.info
pear install phing/phing
```

Download the Drupal Coder module, copy the Drupal Coding Standards out of the coder_sniffer submodule into the PHP CodeSniffer's standards diretory, then delete the downloaded module:

```
wget --quiet http://ftp.drupal.org/files/projects/coder-7.x-2.x-dev.tar.gz
tar -zxvf coder-7.x-2.x-dev.tar.gz
mv coder/coder_sniffer/Drupal $(pear config-get php_dir)/PHP/CodeSniffer/Standards/Drupal
rm coder-7.x-2.x-dev.tar.gz
rm -rf coder
```

At this point, you should have a working PHP installation that has all (or at least <em>most</em>) of the tools you need to find potential issues with your code, and deploy your code using Jenkins and Phing.
<h3 id="installing-mysql">Installing MySQL</h3>

SonarQube requires a database to function, and it's pretty simple to get MySQL set up and configured to be able to handle anything SonarQube can throw at it. Let's install mysql and mysql server:

```
yum install --quiet -y mysql-server mysql
```

Start MySQL and set it to start up at system boot.

```
service mysqld start
chkconfig mysqld on
```

You could run the MySQL setup assistant at this point, but we'll just run a few scriptable commands to do the same things as the <code>mysql_secure_installation</code> script would do (configure the root password (we'll use 'root' for simplicity's sake), delete the anonymous user, and delete the test database):

```
/usr/bin/mysqladmin -u root password root
/usr/bin/mysqladmin -u root -h jenkins-sandbox password root
echo "DELETE FROM mysql.user WHERE User='';" | mysql -u root -proot
echo "FLUSH PRIVILEGES;" | mysql -u root -proot
echo "DROP DATABASE test;" | mysql -u root -proot
```

Now we just need to create a database and user for SonarQube:

```
echo "CREATE DATABASE sonar CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u root -proot
echo "CREATE USER 'sonar' IDENTIFIED BY 'sonar';" | mysql -u root -proot
echo "GRANT ALL ON sonar.* TO 'sonar'@'%' IDENTIFIED BY 'sonar';" | mysql -u root -proot
echo "GRANT ALL ON sonar.* TO 'sonar'@'localhost' IDENTIFIED BY 'sonar';" | mysql -u root -proot
echo "FLUSH PRIVILEGES;" | mysql -u root -proot
```

MySQL is ready to go!
<h3 id="installing-sonarqube-server">Installing SonarQube Server</h3>

SonarQube is a very nice code analysis and code review visualization and tracking tool, and it needs to be installed on a server with Java (which we already have set up for Jenkins) and a database (which we just set up above). First, we'll install Sonar:

```
wget --quiet http://dist.sonar.codehaus.org/sonar-3.7.1.zip
unzip -q sonar-3.7.1.zip
rm -f sonar-3.7.1.zip
mv sonar-3.7.1 /usr/local/sonar
```

Next, edit the sonar.properties file so Sonar knows how to connect to the MySQL database we created earlier (the file is located at <code>/usr/local/sonar/conf/sonar.properties</code>). Edit the following configuration options to match:

```
sonar.jdbc.username: sonar
sonar.jdbc.password: sonar
sonar.jdbc.url: jdbc:mysql://localhost:3306/sonar?useUnicode=true&amp;characterEncoding=utf8&amp;rewriteBatchedStatements=true
```

Install the PHP plugin for Sonar, so our PHP projects can be analyzed without an ugly error message (you can also install the plugin through Sonar's interface, but this method is faster and easy to include in a script):

```
wget --quiet http://repository.codehaus.org/org/codehaus/sonar-plugins/php/sonar-php-plugin/1.2/sonar-php-plugin-1.2.jar
mv sonar-php-plugin-1.2.jar /usr/local/sonar/extensions/plugins/
```

To make sonar easier to manage from the command line, we'll add an init script so you can start/restart/stop it with <code>service</code> and use <code>chkconfig</code>. Create a file at <code>etc/init.d/sonar</code> with the following contents:

```
#!/bin/sh
#
# rc file for SonarQube
#
# chkconfig: 345 96 10
# description: SonarQube system (www.sonarsource.org)
#
### BEGIN INIT INFO
# Provides: sonar
# Required-Start: $network
# Required-Stop: $network
# Default-Start: 3 4 5
# Default-Stop: 0 1 2 6
# Short-Description: SonarQube system (www.sonarsource.org)
# Description: SonarQube system (www.sonarsource.org)
### END INIT INFO
/usr/bin/sonar $*
```

Next, we'll symlink the appropriate sonar executable into <code>/usr/bin</code>, set the correct permissions, and enable sonar at system boot:

```
ln -s /usr/local/sonar/bin/linux-x86-64/sonar.sh /usr/bin/sonar
chmod 755 /etc/init.d/sonar
chkconfig --add sonar
```

Finally, we're ready to start up sonar for the first time:

```
service sonar start
```

It will probably take 45 seconds to a minute to start up the first time, as Sonar will generate it's database and configure itself. Once it's started, you can access Sonar at http://jenkins-sandbox:9000/.
<h3 id="installing-sonarqube-runner">Installing SonarQube Runner</h3>

There are two parts to SonarQube: the server itself, and the Runner, which is helpful if you're using a language that doesn't need to be compiled, but needs to have code analysis generated and dumped into an active SonarQube installation (basically anything that doesn't use Maven). Here we'll install and configure SonarQube Runner, so we can push the code analysis done on our Drupal site into our SonarQube server.

First, we need to download sonar-runner and place it in the appropriate directory (note: this guide was written for version 2.3... in the future, you may need to update the version number/URL):

```
wget --quiet http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/2.3/sonar-runner-dist-2.3.zip
unzip -q sonar-runner-dist-2.3.zip
rm -f sonar-runner-dist-2.3.zip
mv sonar-runner-2.3 /usr/local/sonar-runner
```

Now, configure your sonar-runner instance to point to the SonarQube server we set up earlier by editing the sonar-runner.properties file (located at <code>/usr/local/sonar-runner/conf/sonar-runner.properties</code>). The file should contain something the following (at least):

```
# SonarQube Host URL.
sonar.host.url=http://jenkins-sandbox:9000
# MySQL connection.
sonar.jdbc.url=jdbc:mysql://localhost:3306/sonar?useUnicode=true&amp;amp;characterEncoding=utf8
# MySQL credentials.
sonar.jdbc.username=sonar
sonar.jdbc.password=sonar
```

Finally, to allow sonar-runner to work correctly (so you can just <code>cd</code> to a directory containing a sonar properties file for a project and enter <code>sonar-runner</code> to analyze the code), you need to set the environment variable <code>SONAR_RUNNER_HOME</code> and add the sonar-runner bin directory to your <code>PATH</code>. The simplest way to do this is to add the file <code>/etc/profile.d/sonar.sh</code> with the following inside:

```
# Sonar settings for terminal sessions.
export SONAR_RUNNER_HOME=/usr/local/sonar-runner
export PATH=$PATH:/usr/local/sonar-runner/bin
```

You can also have Jenkins install SonarQube Runner via the UI, but that spoils the fun of using the shell commands, and also isn't able to be wrapped up in a Vagrant profile :-).

<h2 id="lets-do-this-thing">Let's Do This Thing!</h2>

Okay, now that we've completed the marathon of installation and configuration (or just finished a cup of coffee if you used the Vagrant profile and <code>vagrant up</code>), it's time to jump into Jenkins, run a deployment, and see our results in Jenkins and SonarQube!

<p style="text-align: center;">{{< figure src="./jenkins-dashboard-complete.jpg" alt="Jenkins Dashboard" width="550" height="402" >}}
The Jenkins Dashboard</p>

Fire up your web browser and visit http://jenkins-sandbox:8080/ to get to the Jenkins dashboard. We'll create a new project to test everything out:
<ol>
<li>Click on 'New Job'.</li>
<li>Put in a Job name (like 'Drupal 7') and choose 'Build a free-style software project', then click OK.</li>
<li>Under Source Code Management, choose 'Git' and enter the following:<ul>
<li>Repository URL: http://git.drupal.org/project/drupal.git</li>
<li>Branch Specifier: 7.x</li>
<li>(In 'Advanced...') Local subdirectory for repo: drupal</li>
</ul>
</li>
<li>Under Build, click 'Add build step' and choose 'Invoke Phing targets', then enter the following:<ul>
<li>Targets: build</li>
<li>Phing Build File: /vagrant/config/jenkins/drupal-7-example/build.xml</li>
<li>Properties: project.builddir=${WORKSPACE}</li>
</ul>
</li>
<li>Under Build, click 'Add build step' and choose 'Invoke Standalone Sonar Analysis', then enter the following:<ul>
<li>Path to project properties: /vagrant/config/jenkins/drupal-7-example/sonar-project.properties</li>
</ul>
</li>
<li>Click Save at the bottom of the page.</li>
</ol>

(Note that the build.xml and sonar-project.properties files are in the location they would be if you use the Vagrant profile linked at the top of this post—if you're building the server manually, update the paths to your Phing and Sonar properties files accordingly).

If everything is configured correctly, you can now click 'Build Now', and prepare to be dazzled! After a few minutes (depending on the speed of your connection), Jenkins will clone the Drupal git repository, run some analysis on the code through Phing, archive the codebase, and send the analysis results off to SonarQube.

Once everything is complete (and, hopefully, you get a happy blue ball indicating build success!), you can click the Sonar link from the Project's main page to view the SonarQube analysis.

<h2 id="conclusion">Conclusion</h2>

You now have a Continuous Integration server set up that will enable more automated deployments and make code review a more visual and simple process. Plus, as you improve your codebase, you'll be able to see pretty SonarQube graphs and charts showing you how much the code has improved!

Phing and Jenkins offer many more features—I've barely scratched the surface! Go forward and explore the many things you can now do, like automatically generate API documentation for your custom code or email developers directly when their commits break tests.

And, for Heaven's sake, instead of following the 100+ manual steps above to configure a Continuous Integration server, use the <a href="https://github.com/geerlingguy/drupalci-sonar-jenkins">Vagrant profile for Drupal/PHP Continuous Integration Server</a>, and let Vagrant + VirtualBox do the heavy lifting of configuring your server!

<em>Security caveat: The steps above and the Vagrant profile are meant for local testing only—if you build a production/web-accessible CI server, make sure to lock down access with better passwords, authentication, and firewall rules.</em>

<h2 id="related-posts-and-links-for-more-info">Related Posts and Links for More Info</h2>
<ul>
<li><a href="http://wearepropeople.com/blog/phing-and-drupal-first-steps-to-continuous-integration">Phing and Drupal. First steps to continuous integration.</a></li>
<li><a href="http://www.linuxjournal.com/content/achieving-continuous-integration-drupal">Achieving Continuous Integration with Drupal</a></li>
<li><a href="http://reload.github.io/phing-drupal-template/">Phing Drupal Template - build.xml</a></li>
<li><a href="http://www.daedtech.com/static-analysis-why-you-should-care">Static Analysis: Why You Should Care</a></li>
<li><a href="http://jenkins-php.org/">Template for Jenkins Jobs for PHP Projects</a></li>
<li><a href="http://www.jeffgeerling.com/blogs/jeff-geerling/devops-server-deployment-and">Devops, Server Deployment and Configuration Management</a></li>
</ul>
