---
title: "JSON data from Docker Images"
date: "2017-01-30"
permalink: "/blog/2017/01/30/JsonDataFromDockerImages.html"
tags: [docker, til]
---



I was trying to get some structured information from ``docker images``,
hoping to replace some ugly Sed and AWK trickery.
I could have used the `docker-py`__ library.
Instead I chose to use the poorly documented ``--format`` option to ``docker images``
(and some other Docker CLI commands).
Adrian Mouat gives some useful starting points at `Docker Inspect Template Magic`__
and notes that formatting is built around `Go templates`__.

I quickly figured out that this format would meet my immediate need.

.. code-block:: bash

        sudo docker images --format '{{.Repository}}:{{.Tag}}' \
            | grep $IMAGE_NAME \
            | grep -v latest \
            | head -1

That's fine, but I still had no idea what other possible names
could be used in the format template.
While getting there, I learned that `Curl can be used with a Unix socket`__
to talk to the Docker daemon.

.. code-block:: bash

    sudo curl --unix-socket /var/run/docker.sock \
        http://localhost/images/json | python -m json.tool

This produces a prettyprinted list of all the Docker images.
However, the names are not the same as those that can be used in the format template.

The actual field names that can be used in the format template can be found in
`cli/command/formatter/image.go`__. They include:

- ``.ID`` — 12-char SHA aka Image ID
- ``.Repository`` — aka image name
- ``.Tag``
- ``.Digest`` — unsure
- ``.CreatedSince`` — e.g., “4 weeks”
- ``.CreatedAt`` — date
- ``.Size``
- ``.Containers``
- ``.VirtualSize``
- ``.SharedSize``
- ``.UniqueSize``


__ https://docker-py.readthedocs.io/en/stable/
__ http://container-solutions.com/docker-inspect-template-magic/
__ https://golang.org/pkg/text/template/
__ https://nathanleclaire.com/blog/2015/11/12/using-curl-and-the-unix-socket-to-talk-to-the-docker-api/
__ https://github.com/docker/docker/blob/master/cli/command/formatter/image.go

.. _permalink:
    /blog/2017/01/30/JsonDataFromDockerImages.html
