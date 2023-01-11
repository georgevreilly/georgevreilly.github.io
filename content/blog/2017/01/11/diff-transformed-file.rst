---
title: "Diff a Transformed File"
date: "2017-01-11"
permalink: "/blog/2017/01/11/DiffTransformedFile.html"
tags: [programming, bash, til]
---



I wanted to diff two files.
One of them needed some ``sed``\ s on each line and sorting.
I wanted to do that on the fly,
without leaving a massaged intermediate file lying around.

.. code-block:: bash

    colordiff --unified <(cat orphaned_permalinks.txt
                            | sed 's@http://www.georgevreilly.com/@@'
                            | sed 's/.aspx$/.html/'
                            | sort)
            links.txt | less -R

* Use `process substitution`__\ —``<(cat | sed | sort)``\
  —to generate one argument to `colordiff`__.
  The other argument is simply ``links.txt``.
* The first ``sed`` is using ``@`` as the delimiter rather than the more usual ``/``,
  since the pattern contains multiple slashes that would otherwise need to be escaped.
* Pipe the `colored output`__ into ``less -R`` (aka ``--RAW-CONTROL-CHARS``).

__ https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html
__ https://www.colordiff.org/
__ https://unix.stackexchange.com/questions/19317/can-less-retain-colored-output

.. _permalink:
    /blog/2017/01/11/DiffTransformedFile.html
