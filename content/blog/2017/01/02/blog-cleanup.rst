---
title: "Blog Cleanup"
date: "2017-01-02"
permalink: "/blog/2017/01/02/BlogCleanup.html"
tags: [blogging, tech, reStructuredText]
---



I started this blog 14 years ago, in February 2003,
on EraBlog, a long-defunct platform.
Many of my early posts expressed outrage at the imminent Iraq War.
Within a couple of years,
I had moved to running dasBlog_ on my own website, hosted at `ihost.net`_.

I wrote a lot of posts over the next decade.
With rare exception, most posts were composed offline as reStructuredText
and saved in a repository.
There was no formal schema and most posts did not know their permalink.

In late 2014, I moved to the `Acrylamid`_ static blog generator
and I hosted `www.georgevreilly.com`_ at GitHub Pages.
I migrated most of the dasBlog content into a more Acrylamid-friendly form.
A few hundred posts did not get migrated;
mostly the ones that hadn't stored the permalinks.
I added a pile of new posts, but I left the old posts alone.
Until this weekend, when I cleaned up several hundred more posts
and published them here_.
I'm sure I missed a few but almost everything is up now.
I believe all internal hyperlinks have been repaired.
One big exception: all the permalinks used to end in ``.aspx``,
thanks to dasBlog being written in ASP.NET.
Now all permalinks end in ``.html``.
A number of the offsite links have rotted.
I will probably never fix those.

The easiest repairs were along the lines of::

    git grep -l 'SomePattern' | xargs -o vim
    :bufdo %s/SomePattern/OtherPattern/ | update

Many of the repairs were not so easy,
starting with figuring out the correct permalink for orphaned source files.

.. _dasBlog:
    https://github.com/shanselman/dasblog
.. _Acrylamid:
    https://posativ.org/acrylamid/
.. _ihost.net:
    http://ihost.net/
.. _www.georgevreilly.com:
    http://www.georgevreilly.com/
.. _here:
    /articles/

.. _permalink:
    /blog/2017/01/02/BlogCleanup.html
