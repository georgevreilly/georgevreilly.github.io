---
title: "Printf %n"
date: "2007-02-07"
permalink: "/blog/2007/02/07/PrintfN.html"
tags: [security, c, til]
---



.. image:: /content/binary/printf.png
    :alt: Printf %n
    :class: right-float

In my post about `Printf Tricks`_ a couple of years ago,
I mentioned that "``%n`` is dangerous and disabled by default in Visual Studio 2005."

I got email today from someone who was porting a large codebase to VS 2005.
He was getting an assert from ``%n`` and he needed a way to get past it.
He intends to fix the uses of ``%n`` when he has a chance.

I spent several minutes digging around in MSDN and came up with
`set_printf_count_output`_. Wikipedia's `Format string attack`_ page
led me to `Exploiting Format String Vulnerabilities`_, which
describes in detail how ``%n`` (and ``%s``) may be exploited.

In short, if you have ``printf(unvalidated_user_input)``,
instead of ``printf("%s", unvalidated_user_input)``,
then placing ``%n`` into ``unvalidated_user_input`` can
lead to ``printf`` writing arbitrary data into memory.

.. _Printf Tricks:
    /blog/2005/06/02/PrintfTricks.html
.. _set_printf_count_output:
    http://msdn2.microsoft.com/en-us/library/ms175782(VS.80).aspx
.. _Format string attack:
    http://en.wikipedia.org/wiki/Format_string_attack
.. _Exploiting Format String Vulnerabilities:
    http://julianor.tripod.com/bc/formatstring-1.2.pdf

.. _permalink:
    /blog/2007/02/07/PrintfN.html
