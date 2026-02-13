# JeffGeerling.com - Website

[![CI](https://github.com/geerlingguy/jeffgeerling-com/actions/workflows/ci.yml/badge.svg)](https://github.com/geerlingguy/jeffgeerling-com/actions/workflows/ci.yml)

This repository contains the [Hugo](https://gohugo.io) source to build [JeffGeerling.com](https://www.jeffgeerling.com).

## Create a new blog post

To create a new blog post, either run this command from within this directory:

```
hugo new content blog/2026/01/my-blog-post/index.md
```

Or use the alias `blog` to create a new post (from anywhere on the computer) based on a given title:

```
blog "My blog post"
```

## Local Development

After Hugo is installed (`brew install hugo`), run:

```
# Add `-D` to render drafts, `-F` to render future posts, and `--gc` if stale.
hugo server --disableFastRender -D -F --gc
```

And make sure the following is added to your `/etc/hosts` file:

```
127.0.0.1 dev.jeffgeerling.com
```

Visit [http://dev.jeffgeerling.com:1313/](http://dev.jeffgeerling.com:1313/) in your browser, to preview changes live.

If you're just editing individual content pages (e.g. writing a new blog post or editing an existing piece of content), you can drop the `--disableFastRender` option for a speedier experience.

### Local Dev with Comments

Head over to the (currently private) `mm-comments` project and run:

```
docker compose --env-file .env.dev --profile debug up
```

## Production Deployment

This process currently takes at least 1 minute (usually 3-6 minutes), so I'd like to speed it up. See [#172 - Figure out fast deployment workflow for new posts](https://github.com/geerlingguy/jeffgeerling-com/issues/172).

```
# In mm infra project directory:
ansible-playbook deploy.yml

# Or manually: build the site.
hugo --gc --minify --cleanDestinationDir

# Deploy via rclone.
rclone sync -P --exclude ".DS_Store" --fast-list public/ www.jeffgeerling.com:/var/www/www.jeffgeerling.com/
```

## License

Hugo-related configuration and assets are released under the Apache 2.0 license.

All content and images are Copyright Jeff Geerling. All rights reserved.
