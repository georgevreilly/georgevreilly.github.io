---
title: "Accidentally Quadratic: Python List Membership"
date: "2021-10-04"
permalink: "/blog/2021/10/04/AccidentallyQuadraticPythonListMembership.html"
tags: [python, performance, til]
---



We had a performance regression in a test suite recently
when the median test time jumped by two minutes.

.. image:: /content/binary/bigochart.gif
    :alt: Big O Cheat Sheet
    :target: https://www.bigocheatsheet.com/

We tracked it down to this (simplified) code fragment:

.. code:: python

    task_inclusions = [ some_collection_of_tasks() ]
    invalid_tasks = [t.task_id() for t in airflow_tasks
                     if t.task_id() not in task_inclusions]

This looks fairly innocuous—and it was—\
until the size of the result returned from ``some_collection_of_tasks()``
jumped from a few hundred to a few thousand.

The `in comparison operator`_ conveniently works
with all of Python's standard sequences and collections,
but its efficiency varies.
For a ``list`` and other sequences,
``in`` must search linearly through all the elements
until it finds a matching element
*or* the list is exhausted.
In other words, ``x in some_list`` takes :math:`O(n)` time.
For a ``set`` or a ``dict``, however,
``x in container`` takes, on average, only :math:`O(1)` time.
See `Time Complexity`_ for more.

The ``invalid_tasks`` list comprehension
was explicitly looping through one list, ``airflow_tasks``,
and implicitly doing a linear search through ``task_inclusions``
for each value of ``t``.
The nested loop was hidden
and its effect only became apparent
when ``task_inclusions`` grew large.

The list comprehension was actually taking :math:`O(n^2)` time.
When :math:`n` was comparatively small (a few hundred),
this wasn't a problem.
When :math:`n` grew to several thousand,
it became a big problem.

This is a classic example of an `accidentally quadratic`_ algorithm.
Indeed, Nelson describes a very similar problem with `Mercurial changegroups`_.

This performance regression was compounded because this fragment of code
was being called thousands of times—\
I believe once for each task—
making the overall cost cubic, :math:`O(n^3)`.

The fix here is similar:
Use a ``set`` instead of a ``list``
and get :math:`O(1)` membership testing.
The ``invalid_tasks`` list comprehension now takes
the expected :math:`O(n)` time.

.. code:: python

    task_inclusions = set( some_collection_of_tasks() )
    invalid_tasks = [t.task_id() for t in airflow_tasks
                     if t.task_id() not in task_inclusions]

More at `Understanding Big-O Notation`_ and the `Big-O Cheat Sheet`_.


.. _in comparison operator:
   https://docs.python.org/3/reference/expressions.html#membership-test-operations
.. _Time Complexity:
   https://wiki.python.org/moin/TimeComplexity
.. _accidentally quadratic:
   https://accidentallyquadratic.tumblr.com/
.. _Mercurial changegroups:
   https://accidentallyquadratic.tumblr.com/post/161243900944/mercurial-changegroup-application
.. _Understanding Big-O Notation:
   https://www.coengoedegebure.com/understanding-big-o-notation/
.. _Big-O Cheat Sheet:
   https://www.bigocheatsheet.com/

.. _permalink:
    /blog/2021/10/04/AccidentallyQuadraticPythonListMembership.html
