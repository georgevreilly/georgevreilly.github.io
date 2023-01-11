---
title: "Sorting Python Dictionaries by Value"
date: "2016-02-16"
permalink: "/blog/2016/02/16/SortingPythonDictionariesByValue.html"
tags: [python, metabrite, til]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

I needed to sort a Python dictionary by *value* today, rather than by *key*.
I found it confusing, so I'll share what I learned.

Assume the following dictionary, where each value is a tuple of (ID, score).
How do we sort by score; i.e., the second item in the value tuple?
(For the purposes of this discussion, ignore the meaning of the dictionary's key.)

.. code:: pycon

    >>> some_dict = dict(a=(123, 0.7), b=(372, 0.2), e=(456, 0.85), d=(148, 0.23), c=(502, 0.1))
    >>> some_dict
    {'a': (123, 0.7), 'c': (502, 0.1), 'b': (372, 0.2), 'e': (456, 0.85), 'd': (148, 0.23)}

Python dictionaries are inherently unsorted,
unless you use `OrderedDict`_,
which remembers the insertion order.

    From Python 3.6 onwards, dictionary order is guaranteed to be insertion order.
    Even with ``OrderedDict`` or Python 3.6+,
    the dictionary will be sorted only if the insertion order was sorted.

If you want to sort a dictionary *by value*,
you must create an ordered sequence.
You have two options:

* produce a sorted list of key-value pairs;
  e.g., ``[('e', (456, 0.85)), ('a', (123, 0.7)), ..., ('c', (502, 0.1))]``
* produce a sorted list of keys, which are then used to access the dictionary;
  e.g., ``['e', 'a', 'd', 'b', 'c']``

The latter should be a little faster.

Let's use Python's built-in sorted_ function.
If you supply a ``key`` parameter to ``sorted()``,
you're providing a function that (somehow) extracts a *sort-key* from the item passed to it.
The ``key`` parameter is not related to dictionary keys.

To produce the sorted list of keys for ``some_dict``,
in descending order of score:

.. code:: python

    sorted(some_dict, key=lambda k: some_dict[k][1], reverse=True)

This can be used to build a sorted list of key-value pairs:

.. code:: pycon

    >>> [(k, some_dict[k]) for k in sorted(some_dict, key=lambda k: some_dict[k][1], reverse=True)]
    [('e', (456, 0.85)), ('a', (123, 0.7)), ('d', (148, 0.23)), ('b', (372, 0.2)), ('c', (502, 0.1))]

Note that ``for k in some_dict``
yields the same sequence as ``for k in some_dict.keys()``.
Here, ``sorted()`` walks through ``some_dict`` once,
obtaining a dictionary key, ``k``, at each step.
This ``k`` is passed to the ``key`` function.
Our lambda fetches the associated value—an ID-score tuple—\
from ``some_dict`` and extracts the score.
This score becomes the sort-key for ``k``.
In *O(n)* time, ``sorted()`` extracts (sort-key, dictionary-key) pairs,
which are then sorted in *O(n log n)* time on the sort-key,
yielding a sorted sequence of dictionary-keys.

``operator.itemgetter`` and ``operator.attrgetter`` can also be used
for the ``key`` parameter to ``sorted()``.

If we express this sort-key behavior using the `Decorate-Sort-Undecorate`_ pattern,
it may be clearer,
albeit slower and more verbose:

.. code:: pycon

    # Decorate: Build a list of (sort-key, dict-key) pairs
    >>> decorated = [(id_score[1], k) for k,id_score in some_dict.items()]
    >>> decorated
    [(0.7, 'a'), (0.1, 'c'), (0.2, 'b'), (0.85, 'e'), (0.23, 'd')]

    # Sort in descending order of sort-keys (scores)
    >>> decorated.sort(reverse=True)

    >>> decorated
    [(0.85, 'e'), (0.7, 'a'), (0.23, 'd'), (0.2, 'b'), (0.1, 'c')]

    # Undecorate: Extract the sorted dictionary keys
    >>> keys = [k for score,k in decorated]
    >>> keys
    ['e', 'a', 'd', 'b', 'c']


Sorting directly by value
-------------------------

If we have a simpler dictionary that we want to sort directly by value,
we can use `dict.get`_ as the ``key`` function:

.. code:: pycon

    >>> other_dict = dict(a=7, b=3, c=14, d=2, e=9)
    >>> other_dict
    {'a': 7, 'c': 14, 'b': 3, 'e': 9, 'd': 2}

    >>> sorted(other_dict, key=other_dict.get)
    ['d', 'b', 'a', 'e', 'c']

    >>> [(k, other_dict[k]) for k in sorted(other_dict, key=other_dict.get)]
    [('d', 2), ('b', 3), ('a', 7), ('e', 9), ('c', 14)]

``other_dict.get`` is a partial function bound to the ``other_dict`` instance.
When it is used as the ``key`` parameter to ``sorted()``
and invoked with a dictionary key from ``other_dict``,
it yields the associated value;
e.g., ``key('c') → other_dict.get('c') → 14``.


Sorting by key
--------------

To sort the dictionary's keys:

.. code:: pycon

    >>> sorted(other_dict.keys())
    ['a', 'b', 'c', 'd', 'e']

    >>> [(k, other_dict[k]) for k in sorted(other_dict.keys())]
    [('a', 7), ('b', 3), ('c', 14), ('d', 2), ('e', 9)]


.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/
.. _OrderedDict:
    https://pymotw.com/2/collections/ordereddict.html
.. _sorted:
.. _Sorting How-To:
    https://wiki.python.org/moin/HowTo/Sorting
.. _Decorate-Sort-Undecorate:
    https://wiki.python.org/moin/HowTo/Sorting#The_Old_Way_Using_Decorate-Sort-Undecorate
.. _dict.get:
    https://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value

.. _permalink:
    /blog/2016/02/16/SortingPythonDictionariesByValue.html
