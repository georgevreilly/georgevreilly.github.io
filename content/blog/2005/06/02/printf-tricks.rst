---
title: "Printf Tricks"
date: "2005-06-02"
permalink: "/blog/2005/06/02/PrintfTricks.html"
tags: [c, c++, til]
---



It may be old-fashioned, but I still find ``printf`` (and ``sprintf``
and ``_vsnprintf``) incredibly useful, both for printing debug output
and for generating formatted strings.

Here are a few lesser-known formats that I use again and again.
See MSDN for the `full reference`_.

.. _full reference: documentation_
.. _documentation:
    http://msdn2.microsoft.com/en-us/library/56e442dc(VS.71).aspx

%04x - 4-digit hex number with leading zeroes
---------------------------------------------

A quick review of some of the basics.

``%x`` prints an ``int`` in hexadecimal.

``%4x`` prints a hex int, right-justified to 4 places.
If it's less than 4 digits, it's preceded by spaces.
If it's more than 4 digits, you get the full number.

``%04x`` prints a hex int, right-justified to 4 places.
If it's less than 4 digits, it's preceded by zeroes.
If it's more than 4 digits, you get the full number,
but no leading zeroes.

Similarly, ``%d`` prints a ``signed int`` in decimal,
and ``%u`` prints an ``unsigned int`` in decimal.

Not so similarly, ``%c`` prints a character and
``%s`` prints a string.
For wide (Unicode) strings, prefix with ``l`` (ell, or ``w``):
``%lc`` and ``%ls``.

Note: For the Unicode variants, such as ``wprintf`` and friends,
``%c`` and ``%s`` print wide strings.
To force a narrow string, no matter which variant,
use the ``%h`` size prefix,
and to force a wide string, use the ``%l`` size prefix;
e.g., ``%hs`` and ``%lc``.


%p - pointer
------------

The *wrong* way to print a pointer is to use ``%x``.
The right way is to use ``%p``.
It's portable to Win64,
as well as to all other operating systems.

Everyone should know this one, but many don't.


%I64d, %I64u, %I64x - 64-bit integers
-------------------------------------

To print 64-bit numbers (``__int64``), use the ``I64`` size prefix.


%Iu, %Id, %Ix - ULONG_PTR
-------------------------

``ULONG_PTR``, ``LONG_PTR``, and ``DWORD_PTR``
are numeric types that are as wide as a pointer.
In other words, they map to
``ULONG``, ``LONG``, and ``DWORD``
respectively on Win32, and
``ULONGLONG``, ``LONGLONG``, and ``ULONGLONG``
on Win64.

The ``I`` size prefix (capital-i, not lowercase-L)
is what you need to print ``*LONG_PTR`` on Win32 and Win64.


%*d - runtime width specifier
-----------------------------

If you want to calculate the width of a field at runtime,
you can use ``%*``.
This says the next argument is the width,
followed by whatever type you want to print.

For example, the following can be used to print a tree:

.. code-block:: cpp

    void Tree::Print(Node* pNode, int level)
    {
        if (NULL != pNode)
        {
            Print(pNode->Left, level+1);
            printf("%*d%s\n", 2 * level, pNode->Key);
            Print(pNode->Right, level+1);
        }
    }



%.*s - print a substring
------------------------

With a variable precision, you can print a substring,
or print a non-NUL-terminated string, if you know its length.
``printf("%.*s\n", sublen, str)`` prints the first
``sublen`` characters of ``str``.

[2005/7/19: fixed a typo in previous sentence (``%.s`` -> ``%.*s``).
A little elaboration on the syntax:
``.``\-in a printf format specification is followed by the *precision*.
For strings, the precision specificies how many characters will be printed.
A precision of ``*`` indicates that the precision is the next argument on the stack.
If the precision is zero, then nothing is printed.
If a string has a precision specification, its length is ignored.]



%.0d - print nothing for zero
-----------------------------

I've occasionally found it useful to suppress output when
a number is zero, and ``%.0d`` is the way to do it.
(If you attempt to print a non-zero number with this zero-precision
specifier, it will be printed.)
Similarly, ``%.0s`` swallows a string.


%#x - print a leading 0x
------------------------

If you want printf to automatically generate ``0x``
before hex numbers, use ``%#x`` instead of ``%x``.


Other tricks
------------

See the `documentation`_ for other useful tricks.


Security
--------

Never use an inputted string as the format argument: ``printf(str)``.
Instead, use ``printf("%s", str)``.
The former is a stack smasher waiting to happen.

``%n`` is dangerous and disabled by default in VS2005.

Don't use ``sprintf``. Use the counted version,
``_snprintf`` or ``_vsnprintf`` instead.
Better still, use the `StrSafe.h functions`_,
``StringCchPrintf`` and ``StringCchVPrintf``,
to guarantee that your strings are NUL-terminated.

[Update: 2008/01/25: See also `Printf %n`_.]

.. _StrSafe.h functions:
    http://msdn2.microsoft.com/en-us/library/ms647466(VS.85).aspx
.. _Printf %n:
    /blog/2007/02/07/PrintfN.html

.. _permalink:
    /blog/2005/06/02/PrintfTricks.html
