---
title: "Python Enums with Attributes"
date: "2023-09-02"
permalink: "/blog/2023/09/02/PythonEnumsWithAttributes.html"
tags: [python, til]
---

Python enumerations_ are useful for grouping related constants in a namespace.
You can add additional behaviors to an enum class,
but there isn't an easy and obvious way
to add attributes to enum members.

.. code-block:: python

    class TileState(Enum):
        CORRECT = 1
        PRESENT = 2
        ABSENT  = 3

        def color(self):
            if self is self.CORRECT:
                return "Green"
            elif self is self.PRESENT:
                return "Yellow"
            elif self is self.ABSENT:
                return "Black"

        def emoji(self):
            return {
                self.CORRECT: "\U0001F7E9",
                self.PRESENT: "\U0001F7E8",
                self.ABSENT:  "\U00002B1B",
            }[self]

Accessing the members and the methods:

.. code-block:: pycon

    >>> for ts in TileState:
    ...     print(f"{ts.name:<7}: {ts.value} {ts.color():<6} {ts.emoji()}")
    ...
    CORRECT: 1 Green  🟩
    PRESENT: 2 Yellow 🟨
    ABSENT : 3 Black  ⬛

You can add methods like ``color()`` and ``emoji()`` above\
—you can even decorate them with ``@property`` so that you don't need parentheses—\
but you have to remember to update *each* method
when you add or remove members from the enumeration.

Namedtuples to the rescue
-------------------------

It `turns out`_ that you can build a `mixin`_ enumeration
from namedtuple_ and ``Enum`` that gives terse construction syntax:

.. code-block:: python

    class TileState(namedtuple("TileState", "value emoji color css_color"), Enum):
        CORRECT = 1, "\U0001F7E9", "Green",  "#6aaa64"
        PRESENT = 2, "\U0001F7E8", "Yellow", "#c9b458"
        ABSENT  = 3, "\U00002B1B", "Black",  "#838184"

Each member now has multiple read-only attributes,
like ``emoji`` and ``css_color``:

.. code-block:: pycon

    >>> for ts in TileState:
    ...     print(f"{ts.name:<7}: {ts.value} {ts.emoji} U+{ord(ts.emoji):05x} "
    ...           f"{ts.color:<6} {ts.css_color}")
    ...
    CORRECT: 1 🟩 U+1f7e9 Green  #6aaa64
    PRESENT: 2 🟨 U+1f7e8 Yellow #c9b458
    ABSENT : 3 ⬛ U+02b1b Black  #838184

.. _enumerations:
    https://realpython.com/python-enum/
.. _turns out:
    https://stackoverflow.com/a/62601113/6364
.. _mixin:
    /blog/2016/01/14/PythonBaseClassOrder.html
.. _namedtuple:
    https://realpython.com/python-namedtuple/
