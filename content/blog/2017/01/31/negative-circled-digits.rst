---
title: "Negative Circled Digits"
date: "2017-01-31"
permalink: "/blog/2017/01/31/NegativeCircledDigits.html"
tags: [writing, tech, font, blogging, til]
---



I found something very useful in the dingbats__ range of Unicode characters:
the negative circled san-serif digits, ➊ ➋ ➌ ➍ ➎ ➏ ➐ ➑ ➒ ➓ .

I've started using them to label points of interest in code.
They play well with the ``code-block`` directive in reStructuredText.

.. code-block:: bash

        sudo docker images --format '{{.Repository}}:{{.Tag}}' \    ➊ 
            | grep $IMAGE_NAME \                                    ➋ 
            | grep -v latest \                                      ➌ 
            | head -1                                               ➍ 

1. A Golang Template format string for image-name and tag
2. Match some Docker image name
3. Exclude the ``latest`` tag
4. Take only the first

Because these characters are extra-wide even in a monospaced font,
Vim doesn't render them properly unless they're followed by a space.

__ http://graphemica.com/blocks/dingbats
.. _dingbat negative circled sans-serif digit one:
    http://graphemica.com/%E2%9E%8A

.. _permalink:
    /blog/2017/01/31/NegativeCircledDigits.html
