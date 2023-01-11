---
title: "Opening Vim at the right place"
date: "2016-08-19"
permalink: "/blog/2016/08/19/OpeningVimAtTheRightPlace.html"
tags: [vim]
---



If you know exactly which line you want to go
or which pattern you want to search for,
Vim provides a couple of command-line options that can help:
``+NUM`` goes to line number ``NUM``,
while ``+/PAT`` searches for the first occurrence of ``PAT``.
It's also possible to execute an Ex command with ``+CMD``,
such as ``"+set fenc=latin1"``.
You can supply up to ten ``+`` options.

.. code:: bash

    vim +23 ~/.bashrc
    vim '+/ASIN\|ISBN' template.rst
    vim "+set fenc=latin1" some.csv

.. _permalink:
    /blog/2016/08/19/OpeningVimAtTheRightPlace.html
