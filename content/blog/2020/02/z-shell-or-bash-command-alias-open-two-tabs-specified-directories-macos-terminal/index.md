---
nid: 2966
title: "Z shell or Bash command alias to open two tabs to specified directories in macOS Terminal"
slug: "z-shell-or-bash-command-alias-open-two-tabs-specified-directories-macos-terminal"
date: 2020-02-17T04:36:36+00:00
drupal:
  nid: 2966
  path: /blog/2020/z-shell-or-bash-command-alias-open-two-tabs-specified-directories-macos-terminal
  body_format: markdown
  redirects: []
tags:
  - aliases
  - bash
  - dotfiles
  - mac
  - macos
  - terminal
  - zsh
  - zshrc
---

There are a few projects I have where I need to work from two separate directories simultaneously, and while there are a number of ways I could set up workspaces in various esoteric IDEs or terminal session managers, I am stodgy in my ways and enjoy using the built-in Terminal in macOS for most things. If you use iTerm on the Mac, the commands are similar, but the AppleScript events that I use may need to be adjusted.

But I'm getting ahead of myself. For these projects, I want to have a bash/zsh alias that does the following:

  1. When I type `xyz` (alias) and hit 'return'
  2. Open the current tab to path `~/projects/xyz`
  3. Open a new tab next to this tab
  4. Change directories in then new tab to path `~/something-else/xyz`

Simple enough, you say, but I found that a number of AppleScript incantations (e.g. `do script` and the like) could not be made to work with bash aliases easily. In the end, I put the following in my `.zshrc` file (see all of [geerlingguy's dotfiles](https://github.com/geerlingguy/dotfiles) here—some private aliases excluded):

```
# Alias to get two tabs ready for programming session for project xyz.
alias xyz='cd ~/projects/xyz && osascript \
  -e '"'"'tell application "Terminal" to activate'"'"' \
  -e '"'"'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down'"'"' \
  -e '"'"'tell application "System Events" to keystroke "cd ~/something-else/xyz" & return & "clear" & return'"'"''
```

Assuming you're always in a Terminal window when using the alias, it should work fine. Note that using `System Events` pops a permissions warning in macOS 10.14 and later, and you may need to grant Accessibility privileges to the Terminal application in the Privacy settings in System Preferences—making changes like this can have security implications, so do so at your own risk!
