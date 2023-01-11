---
title: "Dramaturgy: LaTeX"
date: "2009-02-18"
permalink: "/blog/2009/02/18/DramaturgyLaTeX.html"
tags: [jamesjoyce, LaTeX, tech, reStructuredText, dramaturgy]
---



.. image:: /content/binary/talboys-xetex.png
    :alt: Bloomsday reading
    :target: http://www.wildgeeseseattle.org/
 

I have a long-standing fascination with typography.
In the late '80s and early '90s, I became quite `adept with TeX and LaTeX`_,
the well-known `scientific typesetting system`_.
When I was at ICPC_, I think I read the TeXbook_ cover to cover—twice.
I became the TeX administrator for the CS department while I was at Brown.

And then I moved to Seattle to work for Microsoft
and entered the world of Windows,
and I left TeX behind for more than 15 years.

I wrote the other day that I prepared the Bloomsday_ scripts in XML_
for several years, using XSLT to generate HTML.
I used to send the HTML to the readers,
but everyone's browser paginated differently when printing,
which led to confusion at rehearsals.
So I started giving them PDFs:
problem solved except for the person who needed a large-print version.

Last year, I prepared the script with `reStructuredText`_.
Normally, I use reST to generate HTML,
but reST can also generate LaTeX.
I decided to use `rst2latex`_ to take advantage of LaTeX's superior typesetting.

I wasn't happy with the results.
The script looked like a crappy technical paper from the '90s,
thanks to the tired `Computer Modern`_ layout.
CM works well for math, less well for text, in my opinion.

The MacTeX_ extras included XeTeX_,
a modern variant of TeX that supports Unicode and OpenType fonts.
I experimented with using Hoefler_ to set the script.
You can see the results above: it looks gorgeous.

More to come.

.. _adept with TeX and LaTeX:
    http://www.google.com/search?q=gvr@cs.brown.edu+LaTeX
.. _scientific typesetting system:
    http://en.wikipedia.org/wiki/LaTeX
.. _ICPC:
    /blog/2009/02/02/LeavingIrelandPart1.html
.. _TeXbook:
    http://www-cs-faculty.stanford.edu/~knuth/abcde.html
.. _Bloomsday:
    http://www.wildgeeseseattle.org/
.. _XML:
    /blog/2009/02/16/DramaturgyXML.html
.. _reStructuredText:
    /blog/2008/11/24/reStructuredText.html
.. _rst2latex:
    http://docutils.sourceforge.net/docs/user/tools.html#latex-generating-tools
.. _Computer Modern:
    http://en.wikipedia.org/wiki/Computer_Modern
.. _MacTeX:
    http://www.tug.org/mactex/
.. _XeTeX:
    http://en.wikipedia.org/wiki/XeTeX
.. _Hoefler:
    http://en.wikipedia.org/wiki/Hoefler_Text

.. _permalink:
    /blog/2009/02/18/DramaturgyLaTeX.html
