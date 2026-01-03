---
nid: 2896
title: "Deploying a React single-page web app to Kubernetes"
slug: "deploying-react-single-page-web-app-kubernetes"
date: 2018-12-05T20:50:18+00:00
drupal:
  nid: 2896
  path: /blog/2018/deploying-react-single-page-web-app-kubernetes
  body_format: markdown
  redirects: []
tags:
  - containers
  - docker
  - javascript
  - js
  - kubernetes
  - node
  - node.js
  - react
---

React seems to have taken the front-end development community by storm, and is extremely popular for web UIs.

It's development model is a breath of fresh air compared to many other tools: you just clone your app, and as long as you have Node.js installed in your environment, to start developing you run (either with `npm` or `yarn` or whatever today's most popular package manager is):

```
yarn install
yarn serve
```

And then you have a local development server running your code, which updates in real time when you change code.

But when it comes time to _deploy_ a real-world React app to non-local environments, things can get a little... weird.

For most modern projects I work on, there are usually multiple environments:

  - Local developer environments
  - Stage environment (or 'pre-production', or 'test')
  - Prod environment

For any app that does anything useful, there will be some variables the app uses which need to change in different environments. Let's say I'm pulling data out of a backend, and that backend is also different per environment:

  - Local: `http://localhost/`
  - Stage: `https://stage.example.com/`
  - Prod: `https://prod.example.com/`

A developer can set a value in React's `src/config.js` file and add in a variable like:

```
export default {
  backendUrl: process.env.REACT_APP_BACKEND_URL,
};
```

And when that developer runs `REACT_APP_BACKEND_URL="http://localhost/" yarn start` (or runs it in a Docker container with the environment set up appropriately), then the URL the app sees is dynamically set by the environment variable.

But there's a problem lurking here: When you run `yarn start` or `npm start` to start your app, it outputs this nice little warning in the stdout:

```
yarn run v1.9.4
$ node scripts/start.js
Starting the development server...

Compiled successfully!

You can now view my-react-app in the browser.

  Local:            http://localhost:3000/
  On Your Network:  http://172.22.0.2:3000/

Note that the development build is not optimized.
To create a production build, use yarn build.
```

So we need to run `yarn build` to _build_ the app, and then serve the generated `build/` directory for production. This is because React builds SPAs (Single-Page Apps) that are static HTML/JS and run in the client browser, _not_ on a server.

So to follow best practices for containerized deployments and [Twelve-Factor Apps](https://12factor.net), we can just take this `build/` directory, copy it into a container with a webserver (e.g. some tiny container like `nginx-alpine` from the Docker library), start the container, and be happy with our tiny (< 10 MB compressed) container that starts up in < 1 second!

But wait... when I ran `yarn build`, the environment variables that were in play in that environment (e.g. `backendUrl:"http://localhost/"`) were hard-coded into my optimized static build. So... if I want to take the container I just built and run it in my production environment, the application is going to look for localhost, which is not going to work.

Okay, so let's change the `REACT_APP_BACKEND_URL` to the production URL, `https://prod.example.com/`, and re-build the Docker image. Great! Now we can run that container image in production. Starts up super fast, container is only 10 MB, everyone's happy!

Oh, wait... I just tried to deploy the same container image into Stage, and it's still pointing at the backend `https://prod.example.com/`.

Are you seeing the problem?

With production-optimized React SPA apps, the values for these configurable-in-development variables are hardcoded and cannot be changed. This breaks 12 Factor App rule #3:

> An app’s config is everything that is likely to vary between deploys (staging, production, developer environments, etc). This includes:
> 
>   - Resource handles to the database, Memcached, and other backing services
>   - Credentials to external services such as Amazon S3 or Twitter
>   - Per-deploy values such as the canonical hostname for the deploy
> 
> Apps sometimes store config as constants in the code. This is a violation of twelve-factor, which requires **strict separation of config from code**. Config varies substantially across deploys, code does not.

I was researching the problem quite a bit, and it seems like most react developers are like "you don't just have a production environment and a local environment?", or they don't deploy in a containerized environment like Kubernetes, Mesos, Rancher, ECS, etc., so they just do the build when they do a deploy to a different environment.

But I do, so I had to figure out a way to solve the problem. It looks like the three ways to solve it are:

## Method 1 - YOLO, run it in development mode in production!

I like to name this the `¯\_(ツ)_/¯` technique, because it's not recommended _by the software itself_ (see the output from `yarn start` earlier in this post), but it's currently the easiest way to get a build up and running _relatively_ quickly using environment variables for configuration. And the main things that suffer are container size and performance/scalability.

## Method 2 - Run the build at container startup

This option is kinda-sorta okay:

  - Build the Docker image with `yarn install` already done (so all the app dependencies are present).
  - Have a script that runs when the container starts (e.g. run as the `CMD` or `ENTRYPOINT`), which does the following:
    1. `yarn build`
    2. copy the `build/` directory someplace where it should be served by an HTTP server
    3. Start an HTTP server

This option is mentioned by GitHub user mikesparr in some comments on the thread [How to run React app inside Docker with env vars](https://github.com/facebook/create-react-app/issues/982#issuecomment-444302220), and he has a sample app which is set up this way; see:

  - [https://github.com/mikesparr/tutorial-react-docker/blob/master/Dockerfile](https://github.com/mikesparr/tutorial-react-docker/blob/master/Dockerfile)
  - [https://github.com/mikesparr/tutorial-react-docker/blob/master/run](https://github.com/mikesparr/tutorial-react-docker/blob/master/run)

But this option has some major drawbacks:

  - You have to have your _production_ container image contain all of the following:
    1. A complete Node.js runtime
    2. All of your application's source code and node_modules
    3. An HTTP server
  - Your production container image will be in the 100s of MB instead of being 10-20 MB (for a typical React app).
  - Your container startup time is going to take at least 30-60s since it has to complete the `build` process (vs < 1 second to just start up nginx or some other http server).

## Method 3 - Rearchitect the way your React app loads config

This method is the cleanest in terms of following the Twelve Factor App rules, and in terms of allowing super-fast container startup and having teensy-tiny container images. Basically, you have a script that runs at container startup (as the `CMD` or `ENTRYPOINT`) which takes environment variables and writes them to a config file like `env.js` or `config.json`, then you set your React app to load these values in `index.html` by adding another `<script>` tag to load that file.

This method is better explored in this Stack Exchange answer: [Rendering an environment variable to the browser in a react.js redux production build running in different environments](https://stackoverflow.com/a/49989975/100134)... though for simplicity's sake, and since I'm deploying an app that's developed by someone else and I don't have the time right now to guide that development team to implement this solution, I'm going to stick with Method 2, even with its major drawbacks.

It's funny, there's a similar issue I've found with Magento (another app that I've had a "fun" time containerizing) where you have to run a code compile command on container startup because there's some generated code that's not supposed to be shared between containers for performance reasons. Why you can't just compile the code at runtime, or during image build... I'm not quite sure.

## Conclusion

In the end, I'm going with Method 2 for now, just because it will cause the least amount of friction with the early development cycle I'm in on this project... but it would be nice if there were some officially-supported pattern that's documented for how to deal with variables-from-the-environment in production React apps.

Right now it seems there is no good way to do it, just a bunch of different unofficial ways with different tradeoffs.

And it really doesn't help that any time there's an issue raised about this gap (e.g. [How to run React app inside Docker with env vars](https://github.com/facebook/create-react-app/issues/982)), 80% of the developers who respond don't actually read and/or understand the issue being presented. I think half the comments in that particular thread were discussing solutions to a problem that was never mentioned!
