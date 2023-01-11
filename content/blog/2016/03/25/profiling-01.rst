---
title: "Profiling"
date: "2016-03-25"
permalink: "/blog/2016/03/25/Profiling.html"
tags: [performance, python, til]
---



Despite being a *bona fide* performance expert—\
I spent a couple of years as the Performance Lead
for Microsoft's IIS web server product about 15 years ago—\
I still forget to measure rather than assume.

I wrote some code today that imported nearly 300,000 nodes into a graph
from a 500MB XML file.
The code was not particularly fast and I assumed that it was the XML parser.
I had been using the built-in streaming parser, `cElementTree iterparse`_.
I assumed that using the `lmxl iterparse`_ would make the code faster.
It didn't.

Then I had the bright idea of temporarily disabling the per-node processing,
which left only the XML parsing.
Instead of handling 200 nodes per second, I was now parsing more than 10,000 nodes per second.
Clearly it was the processing, not the parsing, despite my assumptions.

Time to profile.

I used `cProfile`_ to gather some actual data on where time was being spent.
The first thing that leaped out at me was
that I was spending nearly all the time in ``str.lower``.
I cached the result of ``lower`` for each node;
instead of making 20 million calls, I was now making only 32,000.

The hot spot then moved to a function where I was doing a linear search
through an unordered list.
I introduced a dictionary and the cumulative time spent in that function
dropped from 1,500 seconds to 0.56 seconds.

So much for my intuition.

.. _cElementTree iterparse:
    https://docs.python.org/2/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse
.. _lmxl iterparse:
    http://lxml.de/api/lxml.etree.iterparse-class.html
.. _cProfile:
    https://pymotw.com/2/profile/

.. _permalink:
    /blog/2016/03/25/Profiling.html
