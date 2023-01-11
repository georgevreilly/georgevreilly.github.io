---
title: "NUnit calling CppUnit"
date: "2007-03-21"
permalink: "/blog/2007/03/21/NUnitCallingCppUnit.html"
tags: [.NET, C++, c-sharp, til]
---



.. image:: /content/binary/NUnit-CppUnit.png
    :alt: NUnit calling CppUnit
    :class: right-float

Over the last few days, I've been adapting an existing native C++ library
so that it can be called from managed code.
I had written a large number of unit tests with `CppUnit`_
and I wanted to be able to call the tests from `NUnit`_.

I suppose that I could have written a new CppUnit `TestRunner`_ so that I
could call it from NUnit.
Instead, I took the cheap-n-dirty route, playing with ``#define``
and include paths.
It took less time to get working than it did to write this blog post.

Here's the original native CppUnit test code

.. code-block:: cpp

    //-------------------------------
    // native\FooTest.h
    //-------------------------------

    #include <cppunit/extensions/HelperMacros.h>

    class FooTest : public CppUnit::TestFixture
    {
        CPPUNIT_TEST_SUITE( FooTest );
        CPPUNIT_TEST( testAlpha );
        CPPUNIT_TEST_SUITE_END();
    public:
        void testAlpha();
    };


    //-------------------------------
    // native\FooTest.cpp
    //-------------------------------

    #include "FooTest.h"

    // Registers the fixture into the test 'registry'
    CPPUNIT_TEST_SUITE_REGISTRATION( FooTest );

    void FooTest::testAlpha()
    {
        CPPUNIT_ASSERT( 4 == 2 + 2);
    }

And here's my managed NUnit-based wrapper.

.. code-block:: csharp

    //-------------------------------
    // managed\FooTest.h
    //-------------------------------

    using namespace NUnit::Framework;

    // Gross hack. Define a completely different NUnit-compatible FooTest
    // test fixture and use #define's to make the CPPUnit-specific
    // stuff build.

    [TestFixture]
    public ref class FooTest
    {
    public:
        [Test] void testAlpha();
    };

    #define CPPUNIT_TEST_SUITE_REGISTRATION(x)
    #define CPPUNIT_ASSERT(x) Assert::IsTrue(x)

I had to make one change to ``native\FooTest.cpp``,
to ``#include <FooTest.h>`` (angle brackets).
This picks up the first ``FooTest.h`` in the include path,
so that the managed version of ``FooTest.cpp``
now picks up ``managed\FooTest.h``,
instead of the original.

.. _NUnit:
    http://www.nunit.org/
.. _CppUnit:
    http://cppunit.sourceforge.net/
.. _TestRunner:
    http://cppunit.sourceforge.net/cppunit-wiki/TestRunner

.. _permalink:
    /blog/2007/03/21/NUnitCallingCppUnit.html
