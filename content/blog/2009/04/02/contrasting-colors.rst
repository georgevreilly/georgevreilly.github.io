---
title: "Contrasting Colors for Text and Background"
date: "2009-04-02"
permalink: "/blog/2009/04/02/ContrastingColorsForTextAndBackground.html"
tags: [tech, color, til]
---



.. image:: /content/binary/ColorSchemeDesigner-Wheel.png
    :alt: ColorSchemeDesigner.com
    :target: http://colorschemedesigner.com/
    :class: right-float

About three weeks ago, I answered a question on StackOverflow
about generating the `most readable color`_ of text
on a colored background.

I suggested flipping the top bit of each component,
``(r ^ 0x80, g ^ 0x80, b ^ 0x80)``.
This has the same effect as adding 128 if the component is less than 128,
and subtracting 128 otherwise.

Another way to think about it is to imagine the 256x256x256 color cube.
Inside that cube, erect another cube half as wide.
One corner is at your original color
and the diagonally opposite corner is the one computed above.

The questioner liked my answer the best,
but I decided to experiment further.
I wrote some JavaScript to compute that color.
As you can see in the table of 549 colors below,
it works well most of the time, but it's not perfect.

Someone else suggested an earlier SO question on `good-looking font colors`_.
Looking at that thread, I decided to try inverting the `HSL`_ value to
``(h + 180, s, l + (l < 0.5 ? 0.5 : -0.5))``.
That works well too.
Generally, it yields different colors than my first approach.
It looks like one of the two always contrasts well.

I found that the most effective approach was to compute
the gray-level intensity of the original color,
``(0.30*r + 0.59*g + 0.11*b)``.
If it was dark, use white; otherwise, black.

Really, though, unless you have a requirement to work with arbitrary colors,
you should pick your color scheme carefully.
I found a really nice site this afternoon, `ColorSchemeDesigner.com`_

.. _most readable color:
    http://stackoverflow.com/questions/646068/find-most-readable-colour-of-text-that-is-drawn-on-a-coloured-surface/646328#646328
.. _good-looking font colors:
    http://stackoverflow.com/questions/301869/how-to-find-good-looking-font-color-if-background-color-is-known
.. _HSL:
    http://en.wikipedia.org/wiki/HSL_and_HSV#Conversion_from_RGB_to_HSL_or_HSV
.. _ColorSchemeDesigner.com:
    http://colorschemedesigner.com/
.. _source:
    /tests/inverse-colors/inverse-colors.html

.. raw:: html

    <iframe id="inverse-colors"
        src="/tests/inverse-colors/inverse-colors.html"
        width="600" height="250" marginwidth="0" marginheight="0"
        hspace="0" vspace="0" frameborder="1" scrolling="auto">
    </iframe>

Here's the `source`_ of my colortable.

.. _permalink:
    /blog/2009/04/02/ContrastingColorsForTextAndBackground.html
