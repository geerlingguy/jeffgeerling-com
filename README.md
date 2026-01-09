# JeffGeerling.com - Website

[![CI](https://github.com/geerlingguy/jeffgeerling-com/actions/workflows/ci.yml/badge.svg)](https://github.com/geerlingguy/jeffgeerling-com/actions/workflows/ci.yml)

This repository contains the [Hugo](https://gohugo.io) source to build [JeffGeerling.com](https://www.jeffgeerling.com).

## Create a new blog post

Since this is the thing I will do most of the time...

```
hugo new content blog/2026/01/my-blog-post/index.md
```

TODO: Create an alias in my `~/.aliases` file that allows me to type `blog my-blog-post` and it will fill in the rest of the above line automatically...

## Local Development

After Hugo is installed (`brew install hugo`), run:

```
# Add `-D` to also render draft posts, add `--gc` if things are stale.
hugo server --disableFastRender
```

Visit [http://localhost:1313/](http://localhost:1313/) in your browser, to preview changes live.

If you're just editing individual content pages (e.g. writing a new blog post or editing an existing piece of content), you can drop the `--disableFastRender` option for a speedier experience.

## Production Deployment

This process currently takes at least 1 minute (usually 3-6 minutes), so I'd like to speed it up. See [#172 - Figure out fast deployment workflow for new posts](https://github.com/geerlingguy/jeffgeerling-com/issues/172).

```
# Build the site.
hugo --gc --minify

# Deploy via rclone.
rclone sync -P --exclude ".DS_Store" --fast-list public/ www.jeffgeerling.com:/var/www/www.jeffgeerling.com/
```

## License

Hugo-related configuration and assets are released under the Apache 2.0 license.

All content and images are Copyright Jeff Geerling. All rights reserved.
