---
title: "Diffing a fragment of a file"
date: "2022-01-31"
permalink: "/blog/2022/01/31/DiffFileFragment.html"
tags: [programming, bash, til]
---



A while back, I had extracted some code out of a large file
into a separate file and made some modifications.
I wanted to check that the differences were minimal.
Let's say that the extracted code had been between
lines 123 and 456 of ``large_old_file``.

.. code-block:: bash

    diff -u <(sed -n '123,456p;457q' large_old_file) new_file

What's happening here?

* ``sed -n '123,456p'`` is printing lines 123–456 of ``large_old_file``.
* The ``457q`` tells sed to abandon the file at line 457.
  Otherwise, it will keep reading all the way to the end.
* The ``<(sed ...)`` is an example of `process substitution`_.
  The *output* of the ``sed`` invocation
  becomes the first *input* of the ``diff`` command.

A similar example: `Diff a Transformed File`_.

BTW, these days, I usually use `delta`_ for diffing at the command line,
especially with Git.

.. _process substitution:
    https://tldp.org/LDP/abs/html/process-sub.html
.. _Diff a Transformed File:
    /blog/2017/01/11/DiffTransformedFile.html
.. _git-delta:
.. _delta:
    https://github.com/dandavison/delta

.. _permalink:
    /blog/2022/01/31/DiffFileFragment.html

