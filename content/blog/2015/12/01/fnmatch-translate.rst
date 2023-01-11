---
title: "Explaining the epilog of fnmatch.translate, \\Z(?ms)"
date: "2015-12-01"
permalink: "/blog/2015/12/01/ExplainingEpilogFnmatchTranslate.html"
tags: [python, regex, til]
---



I was debugging a `filtering directory walker
<http://stackoverflow.com/a/5141829/6364>`_
(on which, more to follow)
and I was trying to figure out
the mysterious suffix that
`fnmatch.translate <https://docs.python.org/2/library/fnmatch.html#fnmatch.translate>`_
appends to its result,
``\Z(?ms)``.

``fnmatch.translate`` takes a Unix-style glob,
like ``*.py`` or ``test_*.py[cod]``,
and translates it character-by-character into a regular expression.
It then appends ``\Z(?ms)``.
Hence the latter glob becomes ``r'test\_.*\.py[cod]\Z(?ms)'``,
using Python's raw string notation to avoid the
`backslash plague <https://docs.python.org/2/howto/regex.html#the-backslash-plague>`_.
Also, the ``?`` wildcard character becomes the ``.`` regex special character,
while the ``*`` wildcard becomes the ``.*`` greedy regex.

A `StackOverflow answer partially explains <http://stackoverflow.com/a/11998653/6364>`_,
which set me on the right track.
``(?ms)`` is equivalent to compiling the regex with ``re.MULTILINE | re.DOTALL``.
The ``re.DOTALL`` modifier makes the ``.`` special character
match *any* character,
including newline;
normally, ``.`` excludes newlines.
The ``re.MULTILINE`` modifier makes ``^`` and ``$``
operate on newline boundaries within the search string;
otherwise, they anchor to the beginning and end of the string.
``\A`` always matches the beginning of the string;
``\Z`` always matches the end of the string.

Another way of saying this:

.. code:: pycon

    # No multiline, so ^ and $ anchor beginning and end of string
    >>> re.search(r'^\.git$(?s)', '.git')
    <_sre.SRE_Match object at 0x10e73a850>

    >>> re.search(r'^\.git$(?s)', 'bar\n.git\nfoo')
    # Nope

    # Multiline => ^ matches after \n and $ before \n
    >>> re.search(r'^\.git$(?ms)', 'bar\n.git\nfoo')
    <_sre.SRE_Match object at 0x10e73a988>

    # \A and \Z always anchor beginning and end of string
    >>> re.search(r'\A\.git\Z(?ms)', '.git')
    <_sre.SRE_Match object at 0x10e73a850>

    >>> re.search(r'\A\.git\Z(?ms)', 'foo\n.git')
    # Nope

So, ``\Z(?ms)`` at the end of the pattern means:

* ``\Z``: the pattern must match all the way to the end of the search string;
* ``(?m)``: the search string may contain newlines;
* ``(?s)``: the ``?`` and ``*`` wildcards may match newlines in the search string.

.. _permalink:
    /blog/2015/12/01/ExplainingEpilogFnmatchTranslate.html
