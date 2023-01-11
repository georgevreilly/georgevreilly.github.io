---
title: "OrderedDict Initialization"
date: "2017-02-21"
permalink: "/blog/2017/02/21/OrderedDictInitialization.html"
tags: [python, hashtables, til]
---



An OrderedDict__ is a Python ``dict`` which remembers insertion order.
When iterating over an ``OrderedDict``, items are returned in that order.
Ordinary ``dicts`` return their items in an unspecified order.

__ https://docs.python.org/2/library/collections.html#collections.OrderedDict

Ironically, most of the ways of constructing an initialized ``OrderedDict``
end up breaking the ordering in Python 2.x and in Python 3.5 and below.
Specifically, using keyword arguments or passing a ``dict`` (mapping)
will not retain the insertion order of the source code.

.. code-block:: pycon

    Python 2.7.13 (default, Dec 18 2016, 07:03:39)
    >>> from collections import OrderedDict

    >>> odict = OrderedDict()
    >>> odict['one'] = 1
    >>> odict['two'] = 2
    >>> odict['three'] = 3
    >>> odict['four'] = 4
    >>> odict['five'] = 5
    >>> odict.items()
    [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)]

    >>> OrderedDict(one=1, two=2, three=3, four=4, five=5).items()
    [('four', 4), ('one', 1), ('five', 5), ('three', 3), ('two', 2)]

    >>> OrderedDict(dict(one=1, two=2, three=3, four=4, five=5)).items()
    [('four', 4), ('five', 5), ('three', 3), ('two', 2), ('one', 1)]

    >>> OrderedDict({"one": 1, "two": 2, "three": 3, "four": 4,↩  
                     "five": 5}).items()
    [('four', 4), ('three', 3), ('five', 5), ('two', 2), ('one', 1)]

Only passing an *iterable* of key-value pairs will retain the order.

.. code-block:: pycon

    >>> OrderedDict([("one", 1), ("two", 2), ("three", 3),↩  
                     ("four", 4), ("five", 5)]).items()
    [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)]

Note that ``OrderedDict`` is noticeably slower than ``dict`` in Python 2.7,
so only use ``OrderedDict`` when insertion order matters.

In Python 3.6, the `order of kwargs is preserved`__,
thanks to the `new compact implementation of dict`__.
``OrderedDict`` is also implemented in C
and its performance is on par with that of ``dict``.

Python 3.6 ``dict``\ s are now ordered too,
but if you care about portable code
(earlier CPython or other Python implementations such as Jython),
use ``OrderedDict`` rather than relying on this implementation detail.

.. code-block:: python

    Python 3.6.0 (default, Dec 24 2016, 08:01:42)
    >>> from collections import OrderedDict

    >>> OrderedDict(one=1, two=2, three=3, four=4, five=5).items()
    odict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), …

    >>> OrderedDict(dict(one=1, two=2, three=3, four=4, five=5)).items()
    odict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), …

    >>> OrderedDict({"one": 1, "two": 2, "three": 3, "four": 4,↩  
                     "five": 5}).items()
    odict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), …

    >>> OrderedDict([("one", 1), ("two", 2), ("three", 3),↩  
                     ("four", 4), ("five", 5)]).items()
    odict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), …

__ https://www.python.org/dev/peps/pep-0468/
__ https://mail.python.org/pipermail/python-dev/2016-September/146327.html

.. _permalink:
    /blog/2017/02/21/OrderedDictInitialization.html
