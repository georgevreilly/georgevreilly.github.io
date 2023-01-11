---
title: "Ack - Better than Grep"
date: "2009-03-25"
permalink: "/blog/2009/03/25/AckBetterThanGrep.html"
tags: [tech, regex, til]
---



.. image:: /content/binary/ack-thpppt.png
    :alt: Ack!
    :target: http://www.betterthangrep.com/
    :class: right-float

On a StackOverflow question about `favorite Vim plugins`_, I learned about Ack_,
a replacement for grep that's smarter about searching source trees.

Ack is written in Perl.
The built-in ``:vimgrep`` is rather slow.
It seems to have some Vim-specific overhead,
such as creating swap files and executing ``BufRead`` autocmds.
Ack is noticeably faster,
though somewhat slower than GNU grep.

Which would you rather type to search a tree,
ignoring the ``.svn`` and ``.git`` subtrees?

.. sourcecode:: bash

    $ ack -i -l foobar
    $ grep --exclude='*.svn*' --exclude='*.git*' -i -l -r foobar .

The ack takes 6 seconds to search 4500 files, while the grep completes in 2.
This does not count the time that I spent trying to figure out
the correct syntax and argument quoting for ``--exclude``.
The help says both ``--regexp=PATTERN`` and ``--exclude=PATTERN``,
but the latter is a *glob* (file wildcard pattern).

On Windows, I wrapped ack with `pl2bat`_.

.. _favorite Vim plugins:
    http://stackoverflow.com/questions/21725/favorite-gvim-plugins-scripts
.. _Ack:
    http://www.betterthangrep.com/
.. _pl2bat:
    http://www.perl.com/doc/manual/html/win32/bin/pl2bat.pl.html

.. _permalink:
    /blog/2009/03/25/AckBetterThanGrep.html
