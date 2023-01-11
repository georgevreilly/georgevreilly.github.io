---
title: "Lucida Hybrid"
date: "2009-02-27"
permalink: "/blog/2009/02/27/LucidaHybrid.html"
tags: [font, html]
---



.. image:: https://www.brownbatterystudios.com/sixthings/images/lucida-hybrid/lucida-hybrid-03.png
    :alt: Lucida Hybrid
    :target: http://www.brownbatterystudios.com/sixthings/2007/03/14/lucida-hybrid-the-grande-alternative/
    :class: right-float

One thing that's been bugging me since I started using `Opera`_
is that **bold** and *italic* text was showing as normal text in my `personal blog`_.
Yet other browsers were correctly displaying bold and italic on my blog.

I'm still not entirely sure why Mac Opera had a problem with it,
but I fixed it by using the `Lucida Hybrid`_ stylesheet tweak.

.. code-block:: css

    body, #content {
        font-family: "Lucida Sans Unicode", "Lucida Grande",
            Verdana, Arial, Helvetica, sans-serif;
    }

    strong, em, b, i {
        font-family: "Lucida Sans", "Lucida Sans Unicode", "Lucida Grande",
            Verdana, Arial, Helvetica, sans-serif;
    }


I adjusted a few other things while I was at it.
The most obvious is that the font size is larger.

Most RSS readers won't pick up the stylesheet,
so take a look at the actual blog_.

.. _Opera:
    /blog/2009/01/22/UsingOpera.html
.. _personal blog:
.. _blog:
    /blog/
.. _Lucida Hybrid:
    http://web.archive.org/web/20090316133744/http://www.brownbatterystudios.com/sixthings/2007/03/14/lucida-hybrid-the-grande-alternative

.. _permalink:
    /blog/2009/02/27/LucidaHybrid.html
