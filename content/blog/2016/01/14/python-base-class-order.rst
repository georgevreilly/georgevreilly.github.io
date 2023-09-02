---
title: "Python Base Class Order"
date: "2016-01-14"
permalink: "/blog/2016/01/14/PythonBaseClassOrder.html"
tags: [python, til]
---



When I declare a derived class that inherits
from both a base class and some mixins,
I am always tempted to write:

.. code:: python

    class Derived(Base, Mixin1, Mixin2):
        "Some class"

My reasoning is that ``Derived`` is a ``Base``
with some ``Mixin1`` and ``Mixin2`` goodness sprinkled on.
Generally, that's fine.
The exception is when I want one of the mixins to override
a method or attribute that's defined in ``Base``.
Because the `Method Resolution Order`_ is left-to-right,
then ``Base``’s implementation will always be found first.

To get the desired behavior of the mixin overriding the base,
``Base`` should always appear *last* in the inheritance list.

.. code:: python

    from __future__ import print_function

    class Useful(object):
        def __init__(self, msg):
            print("{0}: {1}".format(self.__class__.__name__, msg))

        def stuff(self):
            print("useful")

    class Mixin(object):
        def stuff(self):
            print("mixin")

    class UsefulThenMixin(Useful, Mixin):
        pass

    class MixinThenUseful(Mixin, Useful):
        pass

    UsefulThenMixin('base first').stuff()
    print('')
    MixinThenUseful('base last').stuff()


Running yields:

.. code:: bash

    UsefulThenMixin: base first
    useful

    MixinThenUseful: base last
    mixin


.. _Method Resolution Order:
    http://python-history.blogspot.com/2010/06/method-resolution-order.html

.. _permalink:
    /blog/2016/01/14/PythonBaseClassOrder.html
