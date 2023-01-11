---
title: "Nosetests won't discover tests in executable files"
date: "2015-03-02"
permalink: "/blog/2015/03/02/NosetestsWontDiscoverExecutableFiles.html"
tags: [python]
---



.. image:: /content/binary/nose-is-nicer-testing-for-python.jpg
    :alt: Nose is nicer testing for Python
    :target: http://nose.readthedocs.org/
    :class: right-float

We use `Nose <http://nose.readthedocs.org/>`_ to run unit tests.
I noticed that we had some tests that weren't being run,
and it took me some time to work out why.
Eventually, I found this `checklist <https://www.hyperink.com/blog/?p=22>`_,
which told me to "make sure the files in your tests directory are not executable".

A quick ``chmod -x *.py`` later and ``nosetests project/tests`` suddenly found all the tests.

Now that I know what to look for, I found this in the Nose docs:

    It is important to note that the default behavior of nose
    is to not include tests from files which are executable.

    ``--exe``: Look for tests in python modules that are executable.
    Normal behavior is to exclude executable modules, since they may not be import-safe

.. _permalink:
    /blog/2015/03/02/NosetestsWontDiscoverExecutableFiles.html
