---
title: "Transparent PNGs Can Deadlock IE6"
date: "2008-03-10"
permalink: "/blog/2008/03/10/TransparentPNGsCanDeadlockIE6.html"
tags: [tech, programming]
---



.. image:: /content/binary/deadlock_thumb.jpg
    :alt: Deadlock in Real Life
    :target: http://nedbatchelder.com/blog/200801/deadlock_in_real_life.html
    :class: right-float

Over at `Cozi`_, we've started a new `technical blog`_.
I just put my `first post`_ up,
describing a nasty problem we had late last year.

.. _Cozi:
    http://www.cozi.com/
.. _technical blog:
    http://blogs.cozi.com/tech/
.. _first post: More here_
.. _More here:
    http://blogs.cozi.com/tech/2008/03/transparent-pngs-can-deadlock-ie6.html

Here's the summary:

    Internet Explorer 6 does not support transparency in PNG images.
    The best-known solution is to use the DirectX AlphaImageLoader_ CSS filter.
    It's less well known that using AlphaImageLoader sometimes leads to a deadlock in IE6.
    There are two workarounds.
    Either wait until after the image has been downloaded
    to apply the filter to the image's ``style``,
    or use the little-known transparent PNG8_ format instead of the filter.

`More here`_.

.. _AlphaImageLoader:
    http://www.satzansatz.de/cssd/tmp/alphatransparency.html
.. _PNG8:
    http://www.sitepoint.com/blogs/2007/09/18/png8-the-clear-winner/

.. _permalink:
    /blog/2008/03/10/TransparentPNGsCanDeadlockIE6.html
