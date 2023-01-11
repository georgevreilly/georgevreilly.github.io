---
title: "Recursive Generators in Python 2 and 3"
date: "2016-01-22"
permalink: "/blog/2016/01/22/PythonRecursiveGenerators.html"
tags: [python, metabrite, til]
---



\ 

    Generators decouple iteration from the code
    that uses the results of the iteration.

    — David Beazley, `Generators`_

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

Python generators have a `variety of uses`_.
One such is to lazily evaluate sequences.
Another is for coroutines_.
Yet another is to recursively traverse a tree or a graph,
yielding an iterable sequence.

Consider this simple tree of nodes:

.. code:: python

    node_tree = Node(
        'a', [
            Node('b', [
                Node('e', [
                    Node('g')
                ]),
                Node('f'),
            ]),
            Node('c'),
            Node('d')
        ])

where ``Node`` is defined as:

.. code:: python

    class Node(object):
        def __init__(self, value, children=None):
            self.value = value
            self.children = children

        def __repr__(self):
            return "Node({0})".format(self.value)

This generator recursively traverses the nodes top-down:

.. code:: python

        @classmethod
        def get_tree(cls, node):
            yield node
            for child in node.children or []:
                for n in cls.get_tree(child):
                    yield n

Now we can consume ``get_tree`` as a simple sequence:

.. code:: python

    print([n for n in Node.get_tree(node_tree)])

    [Node(a), Node(b), Node(e), Node(g), Node(f), Node(c), Node(d)]

The first ``yield`` in ``get_tree`` produces the current node.
The ``yield`` in the inner loop is necessary
to percolate the results of lower levels upwards to the outermost caller.

Adding some prints may clarify what's going on:

.. code:: python

        @classmethod
        def get_tree(cls, node, depth=1):
            print("\n{0}yield 1: node={1} depth={2}".format('\t'*depth, node, depth))
            yield node
            for child in node.children or []:
                for n in cls.get_tree(child, depth+1):
                    print("{0}yield 2: node={1} depth={2}".format('\t'*depth, n, depth))
                    yield n

``yield 1`` produces the actual node value and occurs first,
while ``yield 2`` denotes the value bubbling up to the original caller.::
     
        yield 1: node=Node(a) depth=1

            yield 1: node=Node(b) depth=2
        yield 2: node=Node(b) depth=1

                yield 1: node=Node(e) depth=3
            yield 2: node=Node(e) depth=2
        yield 2: node=Node(e) depth=1

                    yield 1: node=Node(g) depth=4
                yield 2: node=Node(g) depth=3
            yield 2: node=Node(g) depth=2
        yield 2: node=Node(g) depth=1

                yield 1: node=Node(f) depth=3
            yield 2: node=Node(f) depth=2
        yield 2: node=Node(f) depth=1

            yield 1: node=Node(c) depth=2
        yield 2: node=Node(c) depth=1

            yield 1: node=Node(d) depth=2
        yield 2: node=Node(d) depth=1

    [Node(a), Node(b), Node(e), Node(g), Node(f), Node(c), Node(d)]

You might be tempted to omit the inner loop consuming the sub-generator,
and just ``yield`` the recursive call:

.. code:: python

        @classmethod
        def get_tree(cls, node, depth=1):
            print("\n{0}yield 1: node={1} depth={2}".format('\t'*depth, node, depth))
            yield node
            for child in node.children or []:
                yield cls.get_tree(child, depth+1)

This produces::
     
        yield 1: node=Node(a) depth=1

    [Node(a), <generator object get_tree at 0x106f12eb0>, <generator object get_tree at 0x106f12f00>,
     <generator object get_tree at 0x106f12f50>]

The call to ``get_tree`` in the ``child`` loop creates a generator object.
It's not until you iterate through that nested generator object
that child results are yielded.

What happens if you omit the second ``yield``, leaving a naked recursive call?

.. code:: python

        @classmethod
        def get_tree(cls, node, depth=1):
            print("\n{0}yield 1: node={1} depth={2}".format('\t'*depth, node, depth))
            yield node
            for child in node.children or []:
                cls.get_tree(child, depth+1)

This produces even fewer results::
     
        yield 1: node=Node(a) depth=1

    [Node(a)]

So the inner loop to consume the sub-generator and re-yield is necessary—at least in Python 2.
This is somewhat ugly and `PEP 0380`_ introduced ``yield from`` in Python 3.3,
which delegates to sub-generators:

.. code:: python

        @classmethod
        def get_tree3(cls, node, depth=1):
            print("\n{0}yield 1: node={1} depth={2}".format('\t'*depth, node, depth))
            yield node
            for child in node.children or []:
                yield from cls.get_tree3(child, depth+1)

Now the output is::
     
        yield 1: node=Node(a) depth=1

            yield 1: node=Node(b) depth=2

                yield 1: node=Node(e) depth=3

                    yield 1: node=Node(g) depth=4

                yield 1: node=Node(f) depth=3

            yield 1: node=Node(c) depth=2

            yield 1: node=Node(d) depth=2

    [Node(a), Node(b), Node(e), Node(g), Node(f), Node(c), Node(d)]

This is only one of several uses for ``yield from``,
which functions as a `transparent two-way channel`_
between the caller and the sub-generator.

.. _Generators:
.. _variety of uses:
    https://www.dabeaz.com/generators/
.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/
.. _coroutines:
    https://www.dabeaz.com/coroutines/
.. _PEP 0380:
    https://www.python.org/dev/peps/pep-0380/
.. _transparent two-way channel:
    https://stackoverflow.com/a/26109157/6364

.. _permalink:
    /blog/2016/01/22/PythonRecursiveGenerators.html
