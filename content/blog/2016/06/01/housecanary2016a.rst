---
title: "HouseCanary PyCon2016 Progamming Challenge"
date: "2016-06-01"
permalink: "/blog/2016/06/01/HouseCanaryPyCon2016ProgammingChallenge.html"
tags: [python]
---



Yesterday, while at PyCon,
I whipped up a quick, brute-force answer
to the `HouseCanary PyCon2016 Progamming Challenge`_
in a few minutes.
That was sufficient to pass the first two test cases
and win me a very pretty HouseCanary t-shirt.

The answer ran in *O(n⁴)* time, so it failed miserably on the larger problem sets
in the third and fourth cases.
I mulled it over and came up with an *O(n²)* solution that runs in reasonable time
on the larger problem sets.
On the second test case, ``input1.txt``, runtime drops from 5.2s to 0.2s.

I submitted my new answer.
I'll learn on Monday if I won the speed challenge.

.. _HouseCanary PyCon2016 Progamming Challenge:
    https://github.com/housecanary/PyCon2016

.. _permalink:
    /blog/2016/06/01/HouseCanaryPyCon2016ProgammingChallenge.html
