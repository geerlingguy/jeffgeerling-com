---
nid: 2427
title: "Fixing sonar-runner error - Can not add twice the same measure"
slug: "fixing-sonar"
date: 2013-09-18T13:41:58+00:00
drupal:
  nid: 2427
  path: /blogs/jeff-geerling/fixing-sonar
  body_format: full_html
  redirects: []
tags:
  - code
  - code quality
  - deployment
  - errors
  - sonarqube
aliases:
  - /blogs/jeff-geerling/fixing-sonar
---

Sometimes, when running sonar-runner to compile the results of a Jenkins build into measurable data for a <a href="http://www.sonarqube.org/">SonarQube</a> dashboard for a project, I get the following errors, and execution stops before the data is sent to the central sonar server:

```
ERROR: Error during Sonar runner execution
ERROR: Unable to execute Sonar
ERROR: Caused by: Can not add twice the same measure on org.sonar.api.resources.File...
```

I was looking into what causes this issue, and couldn't find much via Google. However, just running sonar-runner again, without changing anything or modifying anything, seems to let sonar succeed.

I'll update this post if I ever figure out what might be causing the 'twice the same measure' error, but for now, just run sonar-runner again if you ever bump into this error message :)

<em>I'll be posting more about how to use Sonar + Jenkins + Phing to do some pretty awesome Drupal and PHP code analysis and deployments in future blog posts—stay tuned!</em>
