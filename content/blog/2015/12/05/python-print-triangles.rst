---
title: "Python Print Formatting"
date: "2015-12-05"
permalink: "/blog/2015/12/05/python-print-formatting.html"
tags: [python, til]
---



On StackOverflow, someone wanted to
`print triangles in Python
<http://stackoverflow.com/questions/34109838/for-while-loops-to-make-triangles>`_
in an M-shape.
Various clumsy solutions were offered.

Here's mine which uses the left- and right-justification features of
`str.format <https://docs.python.org/2/library/string.html#formatstrings>`_.

* ``"{0}+++{0}".format('Hello!')`` produces two copies of the zeroth argument to ``format``
  (here ``'Hello!'``), separated by three plusses: ``Hello!+++Hello!``.
* ``"{:<4}".format('x')`` left-justifies ``'x'`` in a 4-character field; i.e., ``'x   '``.
* ``"{:>4}".format('x')`` right-justifies ``'x'`` in a 4-character field; i.e., ``'   x'``.
* ``"{:>{}}".format('x', width)`` right-justifies ``'x'`` in a ``width``-character field.
* ``'ab' * 4`` yields 4 copies of ``'ab'``; i.e., ``'abababab'``.

Putting them together::

.. code:: pycon

    >>> WIDTH = 4
    >>>
    >>> for a in range(1, WIDTH+1):
    ...     print("{0:<{1}}{0:>{1}}".format('*' * a, WIDTH))
    ...
    *      *
    **    **
    ***  ***
    ********

Handy references: `PyFormat <https://pyformat.info/>`_ and
`Python String Format Cookbook <https://mkaz.tech/python-string-format.html>`_.

.. _permalink:
    /blog/2015/12/05/python-print-formatting.html
