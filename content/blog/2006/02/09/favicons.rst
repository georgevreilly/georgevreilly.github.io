---
title: "FavIcon Creation"
date: "2006-02-09"
permalink: "/blog/2006/02/09/FavIconCreation.html"
tags: [tech, til]
---



I installed `dasBlog <http://dasblog.info>`_
at Emma's `The Wheel <http://thewheel.biz>`_ site,
so that she and the other knitters
in `Team Ireland <http://thewheel.biz/TeamIreland>`_
can blog during the `2006 Knitting Olympics
<http://www.yarnharlot.ca/blog/olympics2006.html>`_.
What an ordeal that was!
But that's a post for another time.
(It's not working yet, due to permissions issues that require
the intervention of support at our
`hosting site <http://www.ihostsites.net>`_.)

I decided today to create a favicon for The Wheel,
based on the logo that I drew last year with `Inkscape <http://www.inkscape.org>`_.

.. image:: /content/binary/TheWheel.jpg

A favicon is a 16x16 icon which shows up in the tab in a tabbed browser,
such as FireFox or IE with MSN Search.
For example, the little `gvr` icon that shows up if you're reading this on my
`personal blog </blog/>`_.
I think I created this with a trial copy of `Microangelo Creation
<http://www.microangelo.us/advanced_icon_editor/XP_icon_editor.asp>`_,
but I've repaved my laptop since then, so I'm not sure.

.. image:: /content/binary/georgevreilly.ico

Initially, I drew the favicon by hand with the icon editor in Visual Studio,
since it was the only tool that I had handy at work.
It looked like crap.

.. image:: /content/binary/TheWheel1.ico

This evening, I remembered about the automated
`FavIcon from Pics <http://www.chami.com/html-kit/services/favicon/>`_
service over at `HTML-Kit <http://www.chami.com/html-kit/>`_.
I stripped the wording off the logo and submitted that. Much better!
And much easier than using Visual Studio's horrible icon editor.

.. image:: /content/binary/TheWheel2.ico

If you look at it with
`Magnifixer <http://www.blacksunsoftware.com/lensview.html>`_,
you can see that this image has effectively been heavily anti-aliased.
Or rather, FavIcon from Pics did a good job of shrinking the original image.

I had to flush Firefox's cache before it would pick up the new favicon,
whereas IE picked it up after Ctrl+F5. Score one to IE.

.. _permalink:
    /blog/2006/02/09/FavIconCreation.html
