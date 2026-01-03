---
nid: 2514
title: "\"Error: The libsass binding was not found\" when running gulp"
slug: "error-libsass-binding-was-not"
date: 2015-12-09T20:06:49+00:00
drupal:
  nid: 2514
  path: /blogs/jeff-geerling/error-libsass-binding-was-not
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal planet
  - frontend
  - gulp
  - homebrew
  - node.js
  - npm
  - nvm
  - theme
aliases:
  - /blogs/jeff-geerling/error-libsass-binding-was-not
---

I was recently futzing around with a Drupal site that has a fairly complex theme setup, and which relies on npm/gulp to setup and build the theme assets. One time after not touching the project for a couple weeks, when I came back and ran the <code>gulp</code> command again, I got the following error:

```
/path/to/node_modules/node-sass/lib/extensions.js:158
    throw new Error([
          ^
Error: The `libsass` binding was not found in /path/to/node_modules/node-sass/vendor/darwin-x64-14/binding.node
This usually happens because your node version has changed.
Run `npm rebuild node-sass` to build the binding for your current node version.
    at Object.sass.getBinaryPath (/path/to/node_modules/node-sass/lib/extensions.js:158:11)
    at Object.<anonymous> (/path/to/node_modules/node-sass/lib/index.js:16:36)
    at Module._compile (module.js:460:26)
    at Object.Module._extensions..js (module.js:478:10)
    at Module.load (module.js:355:32)
    at Function.Module._load (module.js:310:12)
    at Module.require (module.js:365:17)
    at require (module.js:384:17)
    at Object.<anonymous> (/path/to/node_modules/gulp-sass/index.js:176:21)
    at Module._compile (module.js:460:26)
```

And I think that the line <code>This usually happens because your node version has changed.</code> was exactly right. I manage <code>npm</code> and my Node.js install using Homebrew, and I remember having updated recently; it went from 4.x to 5.x. I also remembered that the project itself was supposed to be managed with 0.12!

So first things first, I installed nvm and used it to switch back to Node.js 0.12:

```
brew install nvm
source $(brew --prefix nvm)/nvm.sh
nvm install 0.12
```

Then, I re-ran <code>npm install</code> inside the theme directory to make sure I had all the proper versions/dependencies. But I was still getting the error. So I found <a href="http://stackoverflow.com/a/30067395/100134">this answer</a> on Stack Overflow, which suggested rebuilding <code>node-sass</code> with:

```
npm rebuild node-sass
```

After that ran a couple minutes, <code>gulp</code> worked again, and I could move along with development on this particular Drupal site. Always mind your versions for Node.js!
