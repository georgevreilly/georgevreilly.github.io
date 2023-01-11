---
title: "Er, er"
date: "2007-10-25"
permalink: "/blog/2007/10/25/ErEr.html"
tags: [programming, til]
---



.. image:: /content/binary/ErEr.png
    :alt: Er, er

I've grown fond of the JavaScript ``||`` idiom::

    function FrobImage(img) {
        var width  = img.width  || 400;
        var height = img.height || 300;
        // ...
    }

    FrobImage({height: 100, name: "example.png"});

If ``img.width`` exists and it's `truthy`_,
then ``width = img.width``; otherwise, ``width = 400``.
Here, it will be ``400`` since the ``img`` hash
has no ``width`` property.
More than two alternatives may be used:
``x = a || b || c || ... || q;``

A few weeks ago, while cleaning up the error handling in some batch files,
I came across a `similar idiom`_::

    foo.exe bar 123 "some stuff"  || goto :Error

Only if ``foo.exe`` fails (``exit()`` returns a non-zero value),
is the second clause executed.

`Perl's die`_ is typically used in a very similar idom::

    chdir '/usr/spool/news' || die "Can't cd to spool: $!\n"

though the ``or`` keyword seems to be preferred nowadays to ``||``.

This morning, I came across the `?? operator in C# 2.0`_,
aka the null coalescing operator::

    Customer cust = getCustomer(id) ?? new Customer();

If ``getCustomer(id)`` is not ``null``, then that's the value that ``cust`` gets;
otherwise it's set to ``new Customer()``.

All of these idioms are `syntactic sugar`_ and all of them are in my toolbox.

.. _truthy:
    http://mattsnider.com/wp-content/uploads/2007/04/FalseTest.html
.. _|| in CMD: similar idiom_
.. _similar idiom:
    http://www.ss64.com/ntsyntax/conditional.html
.. _Perl's die:
    http://perldoc.perl.org/functions/die.html
.. _?? operator in C# 2.0:
    http://blog.devstone.com/Aaron/archive/2006/01/02/1404.aspx
.. _syntactic sugar:
    http://en.wikipedia.org/wiki/Syntactic_sugar

.. _permalink:
    /blog/2007/10/25/ErEr.html
