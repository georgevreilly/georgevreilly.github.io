---
title: "A Use for Octal: Calculating Modulo 36 from Modulo 9"
date: "2019-09-15"
permalink: "/blog/2019/09/15/use-for-octal.html"
tags: [octal, math, go]
---



..

    (I posted an `earlier version`_ of this in December 2004 on my old technical blog.
    A discussion at work last week about 36-bit computers at the `Living Computers Museum`_
    prompted me to write an updated post with improved explanations and much better typography.)

I've been programming in C since 1985 and C++ since 1991,
but I've never found a use for octal_ representation until [2004],
aside from the permissions argument for `chmod`_.
Octal has always seemed as vestigial as a human appendix,
a leftover from the early days of computers,
when `word sizes`_ were often a multiple of three:
6-, 12-, 24-, or 36-bits wide.
All modern computers use word sizes that are powers of two—\
16-, 32-, or 64-bits wide—\
with 8-bit bytes,
so octal is less useful than hex,
which evenly subdivides bytes and words.
I've done a lot of bit twiddling
and hexadecimal has always been indispensable,
while octal has remained a curiosity.

The other day [in 2004], a mathematician friend described to me a problem
that he had solved at a previous company.
They were designing hardware that emulated some old `36-bit computers`_.
For backward compatibility,
the various shift instructions
had to accept an arbitrarily large shift count, :math:`k`,
and shift left or right by :math:`(k \textrm{ mod } 36)`.
Now, divisions are not cheap to implement in hardware,
so they needed to come up with an alternate approach
to calculate the modulus.

My friend tried to do something with the factors of 36: :math:`4 × 9`.
Four and nine are `relatively prime`_:
they have no common factors other than one.
By the `Chinese Remainder Theorem`_ therefore,
the combination of :math:`k \textrm{ mod } 4`
and :math:`k \textrm{ mod } 9` is enough to uniquely
determine :math:`k \textrm{ mod } 36`.
By inspection, this is true for the following table of “residues”.
All the integers in the range :math:`[0,36)` appear exactly once.

.. table::
   :align: right

   ======== ==== ==== ==== ==== ==== ==== ==== ==== ==== 
   4 \\ 9    0    1    2    3    4    5    6    7    8  
   ======== ==== ==== ==== ==== ==== ==== ==== ==== ==== 
   0         0   28   20   12    4   32   24   16    8  
   -------- ---- ---- ---- ---- ---- ---- ---- ---- ---- 
   1         9    1   29   21   13    5   33   25   17  
   -------- ---- ---- ---- ---- ---- ---- ---- ---- ---- 
   2        18   10    2   30   22   14    6   34   26  
   -------- ---- ---- ---- ---- ---- ---- ---- ---- ---- 
   3        27   19   11    3   31   23   15    7   35  
   ======== ==== ==== ==== ==== ==== ==== ==== ==== ==== 

Calculating :math:`k \textrm{ mod } 4` is easy in hardware:
it's the two least-significant bits.

How to calculate :math:`k \textrm{ mod } 9` in hardware is not so obvious.


Shifting and Masking
--------------------

Several programming languages now provide a ``0b`` prefix for binary literals
to go along with the ``0x`` prefix for hex literals
and the ``0o`` prefix for octal literals.
(Older languages, such as C, use a ``0`` prefix for octal and have no ``0b`` prefix.)
See the discussion in `Go number literals`_ for more detail on ``0b``,
including a list of languages that now support this notation.

:math:`2^n`, written in binary, looks like ``1`` followed by :math:`n` |_| ``0``\ s.
For example, :math:`2^3 = 1000_2`.
In C-like languages, :math:`2^n` can be written as ``1 << n``.

Similarly, :math:`2^n - 1`, ``(1 << n) - 1``,
written in binary, looks like :math:`n` |_| ``1``\ s.
For example, :math:`2^5 - 1 = 31_{10} = 11111_2`.

We can **multiply** an unsigned integer, ``u``, by :math:`2^n`
by **shifting** ``u`` **left** by :math:`n` bits, ``u << n``,
introducing :math:`n` |_| zeroes as the low-order bits.
For example, using 8-bit numbers without loss of generality,
written as modern Go/Rust number literals:

.. code:: rust

    0b_0001_0101 << 3 == 0b_1010_1000

Similarly, we can **divide** ``u`` by :math:`2^n`
by **shifting** ``u`` **right** by :math:`n` |_| bits, ``u >>> n``,
which drops the :math:`n` |_| low-order bits
and introduces :math:`n` |_| zeroes as the high-order bits.

.. code:: rust

    0b_0101_0110 >>> 3 == 0b_0000_1010

A sign-extending or arithmetic right shift introduces :math:`n` |_| copies
of the sign bit as the high-order bits.
In some languages, such as Java and JavaScript,
``>>`` |_| means an arithmetic right shift and
``>>>`` |_| means a zero-extending right shift.
In other languages, including C, C++, and Go,
there is only a ``>>`` operator and
sign-extension generally depends upon the type of the left operand,
``signed`` or ``unsigned``.
However, sign extension is not guaranteed in C/C++.

.. code:: rust

    0b_0101_0110 >> 2 == 0b_0001_0101
    0b_1001_0110 >> 2 == 0b_1110_0101

Finally, we can find the **remainder** of dividing ``u`` by :math:`2^n`
by **masking** ``u`` with :math:`2^n - 1`,
that is, **bitwise-and** with ``(1 << n) - 1``,
to extract the :math:`n` |_| **low-order bits**:

.. code:: rust

    0b_0101_0110 & 0b_0000_0111 = 0b_0000_0110

In other words, ``u % 8 == u & 7`` and ``u / 8 == u >> 3``.

Read `bitwise operations`_ for more background.


Casting Out Nines
-----------------

There's an old trick for checking the results of arithmetic operations,
known as `casting out nines`_ or `dropping nines`_.

Add up the decimal digits of each number.
Apply the arithmetic operation to these digit sums.
They should be `congruent`_, modulo 9.

For example, :math:`12,345 × 8,765 = 108,203,925`.

To check the multiplication,
compute the `digit sum`_ of each number,
by adding up each decimal digit:

| :math:`1+2+3+4+5 = 15 ≡ 6\ (\textrm{mod } 9)`
| Note: :math:`12,345 \textrm{ mod } 9 = 6`

and

| :math:`8+7+6+5 = 26 ≡ 8\ (\textrm{mod } 9)`
| Note: :math:`8,765 \textrm{ mod } 9 = 8`

Take the first two digit sums, modulo 9, and multiply them:

| :math:`6 × 8 = 48 ≡ 3\ (\textrm{mod } 9)`
| Note: :math:`15 × 26 = 390 ≡ 3\ (\textrm{mod } 9)`

Check against the sum of the digits of the product:

| :math:`1+0+8+2+0+3+9+2+5 = 30 ≡ 3\ (\textrm{mod } 9)`
| Note: :math:`108,203,925 \textrm{ mod } 9 = 3`

This works because :math:`10^n ≡ 1\ (\textrm{mod } 9)`.

Consider 758:

.. math::

    758 = 7×100 + 5×10 + 8

    758 = 7×(9+1)×(9+1) + 5×(9+1) + 8

    758 = 7×(9^2 + 2×9 + 1) + 5×(9 + 1) + 8

Dropping the nines from each term leaves the digit sum,
which is *congruent* to the original number modulo nine:

.. math::

    7×1 + 5×1 + 8 = 7 + 5 + 8 = 20 ≡ 2\ (\textrm{mod } 9)

Checking: :math:`758 \textrm{ mod } 9 = 2`.

`Congruences`_ have a number of useful properties.


Casting Out Elevens
-------------------

Let's use 11, instead of 9.
Since :math:`10 = 11 - 1`, then :math:`10^n ≡ -1^n\ (\textrm{mod } 11)`.

Consider 5234:

.. math::

    5234 = 5×10^3 + 2×10^2 + 3×10^1 + 4×10^0

    5234 = 5×(11-1)×(11-1)×(11-1) + 2×(11-1)×(11-1) + 3×(11-1) + 4

    5234 = 5×(11^3 - 3×11^2×1 + 3×11×1^2 - 1^3) + 2×(11^2 - 2×11×1 + 1^2) + 3×(11 - 1) + 4

Dropping the elevens from each term leaves the alternating digit sum:

.. math::

    5×-1 + 2×1 + 3×-1 + 4 = -5 + 2 -3 + 4 = -2 ≡ 9\ (\textrm{mod } 11)

It's more convenient to proceed rightwards from the least significant digit,
:math:`4 - 3 + 2 - 5`.

Checking: :math:`5234 \textrm{ mod } 11 = 9`.

To cast out elevens,
we calculate the `alternating sum`_ *from right to left*.

Casting out elevens catches some `transposition errors`_, unlike casting out nines.
For more, see `divisibility rule for 11`_
and `proof for alternating sum`_.


Modulo 9
--------

At last, we turn to base 8, octal.
Nine bears the same relationship
to eight in octal,
as eleven does to ten in decimal:
:math:`9_{10} = 11_8`,
base plus one,
and :math:`8^n ≡ -1^n\ (\textrm{mod } 9)`.

We can calculate :math:`k \textrm{ mod } 9` in base 8 by alternately
adding and subtracting the octal digits, from right to left.
For example,
:math:`1234_8 \textrm{ mod } 9 = 4 - 3 + 2 - 1 = 2`.
This gives the right answer.

Here's a simple, albeit incomplete, algorithm in Go.
We're masking and shifting three bits at a time,
which is tantamount to working with the octal representation of ``k``.

.. code-block:: go

    func Mod9(k uint) uint {
        var m int = 0
        sign := +1

        for t := k; 0 != t; t >>= 3 {
            r := int(t & 7)
            m += sign * r
            sign = -sign
        }

        return uint(m)
    }

What about :math:`617_8`?

.. math::

    7 - 1 + 6 = 12 ≡ 3\ (\textrm{mod } 9)

    617_8 \textrm{ mod } 9 = 3

And :math:`6172_8`?

.. math::

    2 - 7 + 1 - 6 = -10 ≡ 8\ (\textrm{mod } 9)

    6172_8 \textrm{ mod } 9 = 8

Almost there!

    Casting out “octal-elevens” (:math:`11_8 = 9_{10}`) in octal,
    by an alternating sum of the base-eight digits,
    computes a small number
    *congruent* to the original number number modulo nine.

The algorithm above is calculating numbers
that are congruent to the correct answer modulo nine,
but which may be outside the desired range.
If the intermediate sum dips below zero or rises above eight,
we have to add nine or subtract nine respectively
to keep the running total in the range :math:`[0,9)`.

Here's a complete algorithm for Modulo 9 in Go,
computing the alternating sum of the octal digits:

.. code-block:: go

    func Mod9(k uint) uint {
        var m int = 0
        var negative bool = false

        for t := k; 0 != t; t >>= 3 {
            r := int(t & 7)
            if negative {
                m -= r
                if m < 0 {
                    m += 9
                }
            } else {
                m += r
                if m >= 9 {
                    m -= 9
                }
            }
            // assert(0 <= m && m < 9)
            negative = !negative
        }

        return uint(m)
    }

Clearly, this algorithm can be implemented in much simpler circuitry
than that required to compute a remainder through full-blown division.


Modulo 36
---------

We now have enough to calculate :math:`k \textrm{ mod } 36`
from ``Mod9`` and the Chinese Remainder Theorem:

.. code-block:: go

    func Mod36(k uint) uint {
        Residues := [4][9]uint{
            { 0, 28, 20, 12,  4, 32, 24, 16,  8},
            { 9,  1, 29, 21, 13,  5, 33, 25, 17},
            {18, 10,  2, 30, 22, 14,  6, 34, 26},
            {27, 19, 11,  3, 31, 23, 15,  7, 35},
        }
        return Residues[k & 3][Mod9(k)]
    }

My friend says that he later learned that similar tricks were
used in classic 36-bit hardware.

I looked everywhere I could think of to see if I could
find this algorithm to calculate modulo 9 described.
I found something that hinted at it in 
Knuth's `Seminumerical Algorithms`_, §4.4.C,
discussing `converting octal integers to decimal`_ by hand,
where he mentions using casting out nines in octal and in decimal
to check the result.
There was no mention of it in Warren's marvelous
`Hacker's Delight`_ or in `HAKMEM`_.

I tried to come up with an analytic way to calculate the
elements of the :math:`9x4` table.
The best that I found is
:math:`(72 - 8 × (k \textrm{ mod } 9) + 9 × (k \textrm{ mod } 4)) \textrm{ mod } 36`!
The inner expression yields a number in the range :math:`[0,99]`,
which can be reduced to :math:`[0,36)`
by subtracting 36 at most twice.
From `Concrete Mathematics`_,
mod 36 can be derived from mod 4 and mod 9
by looking at the [0][1] and [1][0] elements of the table:
:math:`(9 × (k \textrm{ mod } 4) + 28 × (k \textrm{ mod } 9)) \textrm{ mod } 36`.
It works, but it's even worse.
A table lookup is clearly more efficient.

Most, if not all, of the computer architectures
designed in the last forty years
use a word size that is a power of two.
Useful relationships like shifting and masking are one big reason
why non-power-of-two word sizes have gone out of fashion.

Another big reason is the success of C and Unix,
which have a bias towards 8-bit bytes.
`C doesn't require 8-bit bytes`_,
but there's a lot of software which tacitly assumes that
``char`` has exactly 8 bits.

On systems with 9-bit bytes,
like the 36-bit computers,
octal is useful,
since a 9-bit byte can hold all values up to :math:`777_8`
and the word size is a multiple of three.

And there you have it: an unexpected use for octal notation.
It's not exactly an important use,
but then 36-bit computers aren't exactly important any more either.

.. |_| unicode:: 0xA0 
   :trim:

.. _earlier version:
    https://weblogs.asp.net/george_v_reilly/284388
.. _Living Computers Museum:
    https://livingcomputers.org/
.. _octal:
    https://en.wikipedia.org/wiki/Octal
.. _chmod:
    http://en.wikipedia.org/wiki/Chmod
.. _word sizes:
    https://en.wikipedia.org/wiki/Word_(computer_architecture)
.. _Go number literals:
    https://github.com/golang/proposal/blob/master/design/19308-number-literals.md
.. _WinDbg:
    https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools
.. _36-bit computers:
    https://retrocomputing.stackexchange.com/questions/11801/what-was-the-rationale-behind-36-bit-computer-architectures
.. _relatively prime:
    https://artofproblemsolving.com/wiki/index.php/Relatively_prime
.. _Chinese Remainder Theorem:
    https://medium.com/@astartekraus/the-chinese-remainder-theorem-ea110f48248c
.. _bitwise operations:
    https://en.wikipedia.org/wiki/Bitwise_operation
.. _casting out nines:
    http://mathworld.wolfram.com/CastingOutNines.html
.. _dropping nines:
    http://web.archive.org/web/20060101140519/http://web.mit.edu/mwpstr/www/dropnine.htm
.. _digit sum:
    https://en.wikipedia.org/wiki/Digit_sum
.. _congruent:
    https://en.wikipedia.org/wiki/Congruence_relation
.. _Congruences:
    https://www.math.nyu.edu/faculty/hausner/congruence.pdf
.. _transposition errors:
    http://mathyear2013.blogspot.com/2013/01/casting-out-elevens.html
.. _alternating sum:
    https://en.wikipedia.org/wiki/Alternating_sum
.. _divisibility rule for 11:
    https://artofproblemsolving.com/wiki/index.php/Divisibility_rules/Rule_for_11_proof
.. _proof for alternating sum:
    https://en.wikipedia.org/wiki/Divisibility_rule#Proof_using_basic_algebra
.. _Seminumerical Algorithms:
    http://www-cs-faculty.stanford.edu/~knuth/taocp.html
.. _converting octal integers to decimal:
    https://books.google.com/books?id=Zu-HAwAAQBAJ&pg=PT532&lpg=PT532&dq=octal+cast+out+nines+modulo+36&source=bl&ots=9nglVlTuaU&sig=ACfU3U0_RR51okwrvfY3WwC0xBudfLGhuw&hl=en&sa=X&ved=2ahUKEwih44eUxc_kAhVVo54KHcgKDeEQ6AEwDXoECAgQAg#v=onepage&q=octal%20cast%20out%20nines%20modulo%2036&f=false
.. _Hacker's Delight:
    http://www.informit.com/articles/article.asp?p=28678
.. _HAKMEM:
    http://home.pipeline.com/~hbaker1/hakmem/hakmem.html
.. _Concrete Mathematics:
    http://www-cs-faculty.stanford.edu/~knuth/gkp.html
.. _C doesn't require 8-bit bytes:
    http://www.parashift.com/c++-faq-lite/intrinsic-types.html

.. _permalink:
    /blog/2019/09/15/use-for-octal.html
