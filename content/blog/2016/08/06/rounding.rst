---
title: "Rounding"
date: "2016-08-06"
permalink: "/blog/2016/08/06/Rounding.html"
tags: [python, math, til]
---



I recently learned from a `StackOverflow question`__
that the rounding behavior in Python 3.x is different from Python 2.x:

    The round() function rounding strategy and return type have changed.
    Exact halfway cases are now rounded to the nearest even result
    instead of away from zero.
    (For example, round(2.5) now returns 2 rather than 3.)

The “away from zero” rounding strategy is the one that most of us learned at school.
The “nearest even” strategy is also known as “banker’s rounding”.

There are actually `five rounding strategies defined in IEEE 754`__:

=================================   ======  ======  ======  ======
Mode / Example Value                +11.5   +12.5   −11.5   −12.5
=================================   ======  ======  ======  ======
to nearest, ties to even            +12.0   +12.0   −12.0   −12.0
to nearest, ties away from zero     +12.0   +13.0   −12.0   −13.0
toward 0 (truncation)               +11.0   +12.0   −11.0   −12.0
toward +∞ (ceiling)                 +12.0   +13.0   −11.0   −12.0
toward −∞ (floor)                   +11.0   +12.0   −12.0   −13.0
=================================   ======  ======  ======  ======

Further reading on IEEE 754, David Goldberg's classic
`What Every Computer Scientist Should Know About Floating-Point Arithmetic`__.

__ http://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior
__ https://en.wikipedia.org/wiki/IEEE_floating_point#Rounding_rules
__ http://perso.ens-lyon.fr/jean-michel.muller/goldberg.pdf

.. _permalink:
    /blog/2016/08/06/Rounding.html
