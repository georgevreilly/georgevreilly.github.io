---
title: "Python String Formatting"
date: "2009-04-23"
permalink: "/blog/2009/04/23/PythonStringFormatting.html"
tags: [python, til]
---



.. image:: /content/binary/py-str-format.png
    :alt: string formatting
    :target: http://docs.python.org/library/string.html#format-string-syntax
    :class: right-float

Python has long had a string interpolation operator, ``%``.

Python 2.6 and 3.0 introduced a new, richer set of `string formatting operations`_.
See `PEP 3101`_ for the rationale.

One trick that I liked with the old way of formatting was
to put the `locals()`_ dictionary or ``self.__dict__``
on the right-hand side

.. sourcecode:: pycon

    >>> def stuff(a, b):
    ...  c = a+b; d = a-b
    ...  return "%(a)s, %(b)s, %(c)s, %(d)s" % locals()
    ...
    >>> stuff(3, 17)
    '3, 17, 20, -14'

It took me a few minutes to figure out how to do the equivalent with ``string.format``:
use the ``**`` syntax to unpack the dict into ``kwargs``.

.. sourcecode:: pycon

    >>> class Person(object):
    ...  def __init__(self, name, age):
    ...   self.name = name
    ...   self.age = age
    ...  def old(self):
    ...   return "name=%(name)s, age=%(age)d" % self.__dict__
    ...  def new(self):
    ...   return "name={name}, age={age}".format(**self.__dict__)
    ...  def dict(self):
    ...   return "name={0[name]}, age={0[age]}".format(self.__dict__)
    ...
    >>> gb = Person('George Burns', 100)
    >>> gb.old()
    'name=George Burns, age=100'
    >>> gb.new()
    'name=George Burns, age=100'
    >>> gb.dict()
    'name=George Burns, age=100'

The ``getitem`` variant (``{0[name]}``) might be slightly more efficient,
since the dict does not need to be flattened,
but I doubt it makes a perceptible difference in practice.


.. _string formatting operations:
    http://docs.python.org/library/string.html#format-string-syntax
.. _PEP 3101:
    http://www.python.org/dev/peps/pep-3101/
.. _locals():
    http://docs.python.org/library/functions.html#locals

.. _permalink:
    /blog/2009/04/23/PythonStringFormatting.html
