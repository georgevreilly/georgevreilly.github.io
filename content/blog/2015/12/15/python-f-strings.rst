---
title: "Python f-strings"
date: "2015-12-15"
permalink: "/blog/2015/12/15/PythonFStrings.html"
tags: [python, til]
---



At this month's `PuPPy (Puget Sound Programming Python) Meetup`_,
I heard a brief mention of `Python f-strings`_
as a new feature coming in Python 3.6.

In essence, they offer a simpler, more versatile method
of string formatting and interpolation
over existing methods.
F-strings can include not only symbol names
but Python *expressions* within strings.
With `str.format`_, you can write
``'Hello, {name}'.format(name=some_name)``.
You can control various aspects of how ``name`` is formatted,
such as being centered within a field—\
see `PyFormat`_ and `Python String Format Cookbook`_
for examples—\
but no more complex expression is allowed between the braces.

Herewith some examples of f-string expressions
drawn from `PEP 0498`_:

.. code:: pycon

    >>> date = datetime.date(1991, 10, 12)
    >>> f'{date} was on a {date:%A}'
    '1991-10-12 was on a Saturday'

    >>> f'Column={col_idx+1}'
    >>> f'number of items: {len(items)}'

    >>> f'{extra},waiters:{len(self._waiters)}'
    >>> message.append(f" [line {lineno:2d}]")

It looks moderately useful,
but—as with any new language feature—\
it can only be used in brand-new code.
Python 3.6 is scheduled to be released in a year's time,
in December 2016.
Here's `What's New in Python 3.6`_.

.. _PuPPy (Puget Sound Programming Python) Meetup:
    http://www.meetup.com/PSPPython/
.. _Python f-strings:
.. _PEP 0498:
    https://www.python.org/dev/peps/pep-0498/
.. _str.format:
    https://docs.python.org/3/library/string.html#formatstrings
.. _PyFormat:
    https://pyformat.info/
.. _Python String Format Cookbook:
    https://mkaz.blog/code/python-string-format-cookbook/
.. _What's New in Python 3.6:
    https://docs.python.org/3.6/whatsnew/3.6.html

.. _permalink:
    /blog/2015/12/15/PythonFStrings.html
