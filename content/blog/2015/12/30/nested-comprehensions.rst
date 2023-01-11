---
title: "Python: a use for nested list comprehensions"
date: "2015-12-30"
permalink: "/blog/2015/12/30/UseForPythonNestedListComprehensions.html"
tags: [python, til]
---



I wanted to turn a list like 
``['*.zip', '*.pyc', '*.log']`` into
``['--exclude', '*.zip', '--exclude', '*.pyc', '--exclude', '*.log']``.

A simple list comprehension doesn't work as desired:

.. code:: pycon

    In [1]: excludes = ['*.zip', '*.pyc', '*.log']

    In [2]: [('--exclude', e) for e in excludes]
    Out[2]: [('--exclude', '*.zip'), ('--exclude', '*.pyc'), ('--exclude', '*.log')]

The trick is to use a `nested comprehension`_:

.. code:: pycon

    In [5]: [arg for pattern in excludes
                 for arg in ['--exclude', pattern]]
    Out[5]: ['--exclude', '*.zip', '--exclude', '*.pyc', '--exclude', '*.log']


.. _nested comprehension:
    ../../../../2009/03/20/FlatteningListComprehensionsInPython.html

.. _permalink:
    /blog/2015/12/30/UseForPythonNestedListComprehensions.html
