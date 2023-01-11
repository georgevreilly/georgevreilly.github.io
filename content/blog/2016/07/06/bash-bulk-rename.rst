---
title: "Bash: Bulk Renaming"
date: "2016-07-06"
permalink: "/blog/2016/07/06/BashBulkRenaming.html"
tags: [bash, til]
---



I had to rename several hundred thousand files today.
Thanks to a botched invocation of ImageMagick,
they all looked like ``unique_prefix.png.jpg``,
whereas we simply wanted ``unique_prefix.jpg``.

I found a `suitable answer at the Unix StackExchange`__.
As one of the many variants of `parameter substitution`__,
Bash supports ``${var/Pattern/Replacement}``:
“first match of ``Pattern`` within ``var`` replaced with ``Replacement``.”

.. code:: bash

    for f in *.png.jpg;
    do
        mv $f "${f/.png}"
    done

The target expression could also have been written as ``"${f/.png.jpg/.jpg}"``

__  http://unix.stackexchange.com/a/102653/4060
__  http://tldp.org/LDP/abs/html/parameter-substitution.html

.. _permalink:
    /blog/2016/07/06/BashBulkRenaming.html
