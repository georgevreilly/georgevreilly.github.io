---
title: "Regex Conjunctions"
date: "2023-09-05"
permalink: "/blog/2023/09/05/RegexConjunctions.html"
tags: [regex, til]
---


Most regular expression engines make it easy to
match alternations_ (or disjunctions) with the ``|`` operator:
to match *either* ``foo`` *or* ``bar``,
use ``foo|bar``.

Few regex engines have any provisions for conjunctions_,
and the syntax is often horrible.
Awk makes it easy to match ``/pat1/ && /pat2/ && /pat3/``.

.. code-block:: bash

    $ cat <<EOF | awk '/bar/ && /foo/'
    > foo bar
    > bar
    > barfy food
    > barfly
    > EOF
    foo bar
    barfy food

In the case of a Unix pipeline,
the conjunction could also be expressed as a series of pipes:
``... | grep pat1 | grep pat2 | grep pat3 | ...``.

The `longest regex`_ that I ever encountered
was an enormous alternation—\
a true horror that shouldn't have been a regex at all.

.. _alternations:
    https://www.regular-expressions.info/alternation.html
.. _conjunctions:
    https://unix.stackexchange.com/a/55391/4060
.. _longest regex:
    /blog/2020/04/23/regex-32-problems.html
