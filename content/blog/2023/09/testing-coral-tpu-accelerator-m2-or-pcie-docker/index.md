---
nid: 3309
title: "Testing the Coral TPU Accelerator (M.2 or PCIe) in Docker"
slug: "testing-coral-tpu-accelerator-m2-or-pcie-docker"
date: 2023-09-05T16:12:53+00:00
drupal:
  nid: 3309
  path: /blog/2023/testing-coral-tpu-accelerator-m2-or-pcie-docker
  body_format: markdown
  redirects:
    - /blog/2023/testing-m2-or-pcie-coral-accelerator-tpu-docker
aliases:
  - /blog/2023/testing-m2-or-pcie-coral-accelerator-tpu-docker
tags:
  - accelerator
  - ai
  - coral
  - linux
  - m.2
  - ml
  - pcie
  - python
---

{{< figure src="./DSC02738.jpeg" alt="Google Coral TPU in PCIe carrier" width="700" height="384" class="insert-image" >}}

I recently tried setting up an M.2 Coral TPU on a machine running Debian 12 'Bookworm', which ships with Python 3.11, making the [installation of the pyCoral](https://coral.ai/docs/m2/get-started) library very difficult (maybe impossible for now?).

Some of the devs responded 'just install an older Ubuntu or Debian release' in the GitHub issues, as that would give me a compatible Python version (3.9 or earlier)... but in this case I didn't want to do that.

So the next best option would be to set up the PCIe device following the [official guide](https://coral.ai/docs/m2/get-started) (so you can see it at `/dev/apex_0`), then pass it through to a Docker container—which would be easier to set up following Coral's install guide.

## Install Docker

I installed Docker using the instructions provided for an [apt-based install on Debian](https://docs.docker.com/engine/install/debian/#install-using-the-repository):

```
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Build a Docker image for Coral testing

Create a `Dockerfile` with the following contents:

```
FROM debian:10

WORKDIR /home
ENV HOME /home
RUN cd ~
RUN apt-get update
RUN apt-get install -y git nano python3-pip python-dev pkg-config wget usbutils curl

RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" \
| tee /etc/apt/sources.list.d/coral-edgetpu.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update
RUN apt-get install -y edgetpu-examples
```

It's important to use Debian 10, as that version still has a system Python version old enough to work with the Coral Python libraries.

Build the Docker image, and tag it `coral`:

```
sudo docker build -t "coral" .
```

## Run the Docker image and test the TPU

Make sure the device `/dev/apex_0` is appearing on your system, then use the following `docker run` command to pass that device into the container:

```
sudo docker run -it --device /dev/apex_0:/dev/apex_0 coral /bin/bash
```

(If you're in the `docker` group, you can omit the `sudo`).

This should drop you inside the running container, where you can run an Edge TPU example:

```
container-id# python3 /usr/share/edgetpu/examples/classify_image.py --model /usr/share/edgetpu/examples/models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite --label /usr/share/edgetpu/examples/models/inat_bird_labels.txt --image /usr/share/edgetpu/examples/images/bird.bmp
```

This _should_ work... but in my case I was debugging some other flaky bits in the OS, so it didn't work on my machine.

Special thanks to [this comment](https://github.com/google-coral/edgetpu/issues/125#issuecomment-642806176) on GitHub for the suggestion for how to run Coral examples inside a Docker container.
