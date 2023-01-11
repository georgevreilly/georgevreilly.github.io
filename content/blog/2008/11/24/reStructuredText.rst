---
title: "reStructuredText"
date: "2008-11-24"
permalink: "/blog/2008/11/24/reStructuredText.html"
tags: [reStructuredText, til]
---



.. image:: /content/binary/reStructuredText.png
    :alt: reStructuredText
    :target: http://docutils.sourceforge.net/
    :class: right-float

I hate composing anything longer than a couple of paragraphs
in an online HTML editor.
Specifically, I hate writing posts for this blog online.
I'd much rather write in Vim and upload HTML.
But I don't want to compose in raw HTML either.

I use `reStructuredText`_ (reST), an unobtrusive plaintext markup language
popular in the Python world. 
reST can generate HTML, LaTeX, `native PDF`_, ODF, and other formats.
The picture at right shows a draft of this document in MacVim_;
reST is, as you can see, quite readable
(though I work with a larger font).
I use restview_ to preview the HTML locally
and Pygments_ for syntax highlighting of code.
Vim has its own `syntax highlighting`_ for reST
and I've developed a set of keyboard macros for my own use.

.. _reStructuredText:
    http://docutils.sourceforge.net/docs/user/rst/quickstart.html
.. _native PDF:
    http://code.google.com/p/rst2pdf/
.. _MacVim:
    http://code.google.com/p/macvim/
.. _Pygments:
    http://pygments.org/
.. _syntax highlighting:
    http://www.vim.org/scripts/script.php?script_id=973
.. _restview:
    http://mg.pov.lt/restview/

The weak link in this scheme is posting to the blog.
Right now, I have a little wrapper that generates HTML,
extracts the body, and copies it to the `pasteboard`_ (clipboard).
I then manually paste that into a raw HTML textarea
in the blog's editor.
Someday, I have to adapt mtsend_ or Firedrop2_ to
make this less painful.
Or I could hack `dasBlog`_ to support reST in `IronPython`_,
or switch over to a blog that supports reST natively.
Someday.

For a long time, I used VST_ (Vim reStructuredText)
to generate HTML from reST.
As I began using Python more and more,
I realized that I was far better off with the real thing,
which is well designed and quite fast.
The VimL scripting language is not that good
and VST pushes it to its limits.

As of the recent Python 2.6 release,
all the official `Python documentation`_ is in reST format.
Sphinx_ is a documentation build system that wraps
a collection of reST documents into a larger navigable entity.

There are many other `lightweight markup languages`_,
such as `Textile`_, `Markdown`_, and `AsciiDoc`_.
No doubt they have their strengths,
but I now have a significant investment in reST
and it's well supported by the Python community.

.. _pasteboard:
    http://sigpipe.macromates.com/2005/10/11/clipboard-access-from-shell-utf-8/
.. _mtsend:
    http://scott.yang.id.au/2002/12/mtsendpy/
.. _Firedrop2:
    http://www.voidspace.org.uk/python/firedrop2/
.. _dasBlog:
    http://www.dasblog.info/
.. _IronPython:
    http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython
.. _VST:
    http://skawina.eu.org/mikolaj/vst.html
.. _Python documentation:
    http://docs.python.org/dev/
.. _Sphinx: http://sphinx.pocoo.org/
.. _lightweight markup languages:
    http://en.wikipedia.org/wiki/Lightweight_markup_language
.. _Textile:
    http://www.textism.com/tools/textile/
.. _Markdown:
    http://daringfireball.net/projects/markdown/
.. _AsciiDoc:
    http://www.methods.co.nz/asciidoc/

.. _permalink:
    /blog/2008/11/24/reStructuredText.html
