---
title: "Flattening List Comprehensions in Python"
date: "2009-03-20"
permalink: "/blog/2009/03/20/FlatteningListComprehensionsInPython.html"
tags: [python, til]
---



.. image:: https://3.bp.blogspot.com/_GrwhB3fzGXM/R3pbFbVFxQI/AAAAAAAAADU/Tg7y0mtUHi8/s320/listcomprehension.png
    :alt: List Comprehension
    :class: right-float

Python has `list comprehensions`_,
syntactic sugar for building lists from an expression.

.. code:: pycon

    >>> [2 * i for i in (2, 3, 5, 7, 11)]
    [4, 6, 10, 14, 22]

This doesn't work so well when the comprehension expression
is itself a list: you end up with a list of lists.

.. code:: pycon

    >>> def gen():
    ...     for l in [['a', 'b'], ['c'], ['d', 'e', 'f']]:
    ...         yield l
    ... 
    >>> [l for l in gen()]
    [['a', 'b'], ['c'], ['d', 'e', 'f']]

This is ugly. Here's one way to build a flattened list,
but it's less elegant than the comprehension.

.. code:: pycon

    >>> x = []
    >>> for l in gen():
    ...     x.extend(l)
    ... 
    >>> x
    ['a', 'b', 'c', 'd', 'e', 'f']

It took me a while to find a readable list comprehension,
with a little `help from Google`_.
Use `sum()`_ on the outer list and prime it with an empty list, ``[]``.
Python will concatenate the inner lists, producing a flattened list.

.. code:: pycon

    >>> sum([l for l in gen()], [])
    ['a', 'b', 'c', 'd', 'e', 'f']

Alternatively, you can use `itertools.chain()`_.

.. code:: pycon

    >>> import itertools
    >>> list(itertools.chain(*gen()))
    ['a', 'b', 'c', 'd', 'e', 'f']

That might be slightly more efficient,
though I find the ``sum()`` to be a little more readable.

.. code:: pycon

    >>> import itertools
    >>> list(itertools.chain(*gen()))
    ['a', 'b', 'c', 'd', 'e', 'f']

That might be slightly more efficient,
though I find the ``sum()`` to be a little more readable.

**Edit**: I forgot about nested comprehensions

.. code:: pycon

    >>> [inner
    ...     for outer in gen()
    ...         for inner in outer]
    ['a', 'b', 'c', 'd', 'e', 'f']

Somewhat cryptic on one line however:

.. code:: pycon

    >>> [j for i in gen() for j in i]
    ['a', 'b', 'c', 'd', 'e', 'f']

**Update**: The nested comprehension became one of my most `popular StackOverflow answers`_.

.. _list comprehensions:
    http://docs.python.org/tutorial/datastructures.html#list-comprehensions
.. _help from Google:
    http://www.google.com/search?q=python+list+comprehension+flatten
.. _sum():
    http://docs.python.org/library/functions.html#sum
.. _itertools.chain():
    http://docs.python.org/library/itertools.html#itertools.chain

.. _popular StackOverflow answers:
    http://stackoverflow.com/a/716761/6364

.. _permalink:
    /blog/2009/03/20/FlatteningListComprehensionsInPython.html
