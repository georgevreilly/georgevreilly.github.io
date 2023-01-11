---
title: "Assert(Result.ToString() == \"Expected\")"
date: "2006-04-29"
permalink: "/blog/2006/04/29/AssertResultToStringExpected.html"
tags: [tech, c++]
---



I'm writing some C++ code at the moment, after months of C#.
I'm trying to be very `Test First
<http://www.xprogramming.com/xpmag/testFirstGuidelines.htm>`_,
writing Red tests, then making them turn Green.

I'm also using `CppUnit <http://cppunit.sourceforge.net/cppunit-wiki>`_
for the first time. It's not as easy as
`NUnit <http://www.nunit.org/>`_. You can't just declare
your test method with an attribute, you have to declare the test method
in a header file, place it inside a macro, and then have the test
implementation in a .cpp\-file. And there's no nunit-gui.
I'm using a post-build step to run the tests, which makes it
fairly pain free.

There was one internal method that I didn't have an explicit test for,
although I had tests for methods that called it. The main obstacle
was that I didn't have a simple way to check the result, as the method
returned a vector of objects. I didn't want to have to construct
another vector of expected results.

Then it came to me: I could wrap the vector in a class and write a
``ToString()`` method for it (as well as a ``ToString()`` for the
contained objects), and compare that to a string constant::

    RateList result = creative.GetRates();
    CPPUNIT_ASSERT(result.ToString() == "100_4x3:100_16x9|200_16x9|400_4x3:400_16x9");

In retrospect, it should have been obvious. I already have ``ToString()``
methods for many of my other objects, and I'm using
``CPPUNIT_ASSERT(actual.ToString() == expected)`` in many of my unit tests.
The extra step of writing ``ToString()`` for the collection blocked my
thinking.

.. _permalink:
    /blog/2006/04/29/AssertResultToStringExpected.html
