---
title: "Delete all Docker Images by Tags"
# date: "2023-mm-dd"
permalink: "/drafts-drafts-drafts/2023/mm/dd/DeleteAllDockerImagesByTags.html"
tags: [docker, programming, bash]
draft: true
---



.. code-block:: bash

    sudo docker images \
        | grep ^quill \
        | awk '{printf("quill:%s\n", $2) }' \
        | xargs sudo docker rmi
