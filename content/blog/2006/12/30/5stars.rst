---
title: "Rating with Stars"
date: "2006-12-30"
permalink: "/blog/2006/12/30/RatingWithStars.html"
tags: [programming, regex]
---



.. image:: /content/binary/5star0.gif
    :alt: 0 stars out of 5
.. image:: /content/binary/5star3.5.gif
    :alt: 3.5 stars out of 5
.. image:: /content/binary/5star5.gif
    :alt: 5 stars out of 5

I want to be able to write some reviews and graphically rate them with stars.
I put together some transparent stars in Gimp and added a macro to dasBlog.

I'm going to rate this effort:

$stars(4.5)

To get this effect, I simply wrote ``$``\ ``stars(4.5)``.

(And I had to carefully construct the previous sentence so
that dasBlog wouldn't invoke the ``stars`` macro.)

I'm hardnosed. I rarely give 5/5 to anything. I don't really expect to need 
the half stars, but I may want that fine control at some point.

To use this in your own blog, download the `zipfile`_ of star images.

Copy ``5star*.gif`` to your blog's ``images`` directory.
The ``*.xcf`` files are Gimp source files.

Add the following line to the ``<ContentFilters>`` section of your blog's
site.config::

    <ContentFilter
      find="\$stars\((?&lt;expr&gt;[\d.]+)\)"
      replace="&lt;div&gt;&lt;img src=&quot;images/5star${expr}.gif&quot; /&gt; ${expr} stars out of 5&lt;/div&gt;"
      isregex="true" />

Enjoy!

.. _zipfile: /content/binary/5stars.zip

.. _permalink:
    /blog/2006/12/30/RatingWithStars.html
