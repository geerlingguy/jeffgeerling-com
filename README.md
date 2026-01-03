# JeffGeerling.com - Website

TODO: Add badges here.

This repository contains the [Hugo](https://gohugo.io) source to build [JeffGeerling.com](https://www.jeffgeerling.com).

## Create a new blog post

Since this is the thing I will do most of the time...

```
hugo new content blog/2026/01/my-blog-post/index.md
```

TODO: Create an alias in my `~/.aliases` file that allows me to type `blog my-blog-post` and it will fill in the rest of the above line automatically...

## Local Development

  1. Ensure Hugo is installed (e.g. `brew install hugo`).
  2. Run `hugo server --disableFastRender`

Visit [http://localhost:1313/](http://localhost:1313/) in your browser, to preview changes live.

If you're just editing individual content pages (e.g. writing a new blog post or editing an existing piece of content), you can drop the `--disableFastRender` option for a speedier experience.

## Theme Development

TODO.

## Production Deployment

TODO:

```
hugo  # builds site
```

## License

Hugo-related configuration and assets are released under the Apache 2.0 license.

All content and images are Copyright Jeff Geerling. All rights reserved.
