---
title: "Command-line Tools for the Clipboard"
date: "2009-02-12"
permalink: "/blog/2009/02/12/CommandlineToolsForTheClipboard.html"
tags: [tech, windows, linux, mac]
---



.. image:: https://hdbizblog.com/blog/wp-content/uploads/2008/01/clipboard.gif
    :alt: Clipboard
    :width: 200
    :class: right-float

I mentioned in my post on `reStructuredText`_ that I use a little command-line tool,
pbcopy_, to pipe the output into the clipboard.
I finally found a similar tool for Linux, xsel_.

* Mac: pbcopy_ (UTF-8 aware, unlike the built-in version of pbcopy)
  copies its input to the pasteboard (Mac name for the clipboard);
  pbpaste writes the pasteboard to stdout.
* Linux: xsel_ gets and sets the X selection.
* Windows: winclip_ reads and writes the clipboard in a variety of formats.
  Use ``-m`` for UTF-8 text.
  The winclip binary is available as part of the outwit_ package.

.. _reStructuredText:
    /blog/2008/11/24/reStructuredText.html
.. _pbcopy:
    http://sigpipe.macromates.com/2005/10/11/clipboard-access-from-shell-utf-8/
.. _xsel:
    http://www.vergenet.net/~conrad/software/xsel/
.. _winclip:
    http://www.dmst.aueb.gr/dds/sw/outwit/winclip.html
.. _outwit:
    http://www.dmst.aueb.gr/dds/sw/outwit/

.. _permalink:
    /blog/2009/02/12/CommandlineToolsForTheClipboard.html
