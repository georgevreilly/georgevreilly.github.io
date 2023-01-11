---
title: "Nose Test Discovery"
date: "2016-01-24"
permalink: "/blog/2016/01/24/NoseTestDiscovery.html"
tags: [python, til]
---



.. image:: /content/binary/nose-is-nicer-testing-for-python.jpg
    :alt: Nose is nicer testing for Python
    :target: http://nose.readthedocs.org/
    :class: right-float

I figured out why I saw the following error every time I ran Nose_:

.. code:: python

    ======================================================================
    ERROR: Failure: TypeError (type() takes 1 or 3 arguments)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File ".../lib/python2.7/site-packages/nose-1.3.7-py2.7.egg/nose/loader.py", line 523, in makeTest
        return self._makeTest(obj, parent)
      File ".../lib/python2.7/site-packages/nose-1.3.7-py2.7.egg/nose/loader.py", line 582, in _makeTest
        return MethodTestCase(obj)
      File ".../lib/python2.7/site-packages/nose-1.3.7-py2.7.egg/nose/case.py", line 345, in __init__
        self.inst = self.cls()
    TypeError: type() takes 1 or 3 arguments

It turns out that one module was importing a class called ``TestApi``
which had a ``classmethod`` called ``run_integration_tests``.
The module itself had no tests; it just declared a class called ``TestObfuscatedMixin``,
which used some other ``classmethod``\ s on ``TestApi``.
Nose's `test discovery`_ considered ``run_integration_tests`` to be a test because
both the class and the function matched the ``testMatch`` regular expression,
i.e., a name that has ``test`` or ``Test`` at a word boundary
or following a ``-`` or ``_``.

I renamed it to ``run_integration_t3sts`` [sic].
It's hard to find a good synonym for "tests".

Tip: to run a particular test from the command line::

    nosetests path/to/test_module.py:SomeTestClass.test_whatever

That is, *pathname* COLON *classname* DOT *testname*

.. _Nose:
    /blog/2015/03/02/NosetestsWontDiscoverExecutableFiles.html
.. _test discovery:
    http://nose.readthedocs.org/en/latest/writing_tests.html

.. _permalink:
    /blog/2016/01/24/NoseTestDiscovery.html
