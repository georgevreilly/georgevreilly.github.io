---
title: "Decrementing Loops"
date: "2016-01-05"
permalink: "/blog/2016/01/05/DecrementingLoops.html"
tags: [c++, performance]
---



The canonical ``for``-loop in C and C++ is written thus,
counting up ``i = 0``, ``i = 1``, ..., ``i = N-1``:

.. code:: c++

    for (int i=0; i < N; i++) {
        // loop body
    }

(In C, you have to declare ``int i`` before the ``for``-loop.)

Let's unpack that ``for``-loop into an equivalent ``while``-loop:

.. code:: c++

    int i = 0;
    while (i < N) {
        // loop body
        i = i + 1
    }

In other words, we initialize ``i`` to zero.
Then, before every execution of either loop,
we check ``i < N``.
If ``i`` is still within bounds,
we execute the loop body.
Then we postincrement ``i``.
Then back to the top of the loop, checking ``i < N`` again.
And so on, executing the loop ``N`` times,
with ``i = 0``, ``i = 1``, ..., ``i = N-1``.

There's a more efficient way to write that loop—if you don't mind counting *down*
from ``N-1`` to ``0``:

.. code:: c++

    for (int i=N; --i >= 0; ) {
        // loop body
    }

Transforming it into the equivalent ``while``-loop may make it clearer:

.. code:: c++

    int i = N;
    while (--i >= 0) {
        // loop body
    }

We initialize ``i=N``.
Then, before every execution of either loop,
we (a) predecrement ``i``, that is, set ``i = i-1`` and use the new value of ``i``;
then (b) check ``i >= 0``.
If the new value of ``i`` is still non-negative, the loop body is executed.
This loop is also executed ``N`` times,
with ``i = N-1``, ``i = N-2``, ..., ``i = 1``, ``i = 0``.

In the count-up loop, the compiler has to emit an explicit comparison against ``N``,
which must be executed on every iteration of the loop.
If ``N`` is not stored in a register (ia32 doesn't have many),
it will have to be fetched on each iteration.
The count-up loop overhead then
is a possible fetch of ``N``,
a comparison against ``N``,
and a postincrement.

For the count-down loop however,
the compiler won't emit an explicit comparison against zero,
as the predecrement is enough to condition the CPU's `negative flag`_.
If the result of the predecrement is a negative number,
the *sign bit* will be set.

Using a count-down loop, you can shave one instruction off every iteration.
Furthermore, ``N`` is only read once and won't occupy a register.
The predecrement is unavoidable.
For a tight loop, these savings may be important.

However, I would use this idiom sparingly.

* It's only appropriate for loops where it doesn't matter whether you count up or down.
* Make sure that the index is a signed ``int``, not an ``unsigned int``,
  or the count-down loop won't terminate.
  (I've done this a few times.)
* The idiom is not well-known and places a higher cognitive burden on most readers.
  I favor clarity over micro-efficiency,
  so I would only use it for a tight inner loop.
  Everyone recognizes the count-up loop.
* Modern compilers are smart and capable of deep analysis.
  It's possible that some compilers may automatically transform count-up loops
  into count-down loops when their analysis indicates that it's safe to do so.


.. _negative flag:
    https://en.wikipedia.org/wiki/Negative_flag

.. _permalink:
    /blog/2016/01/05/DecrementingLoops.html
