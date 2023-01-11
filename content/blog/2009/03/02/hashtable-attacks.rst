---
title: "Hash Table Attacks"
date: "2009-03-02"
permalink: "/blog/2009/03/02/HashTableAttacks.html"
tags: [programming, til]
---



.. image:: /content/binary/hashtable-collide.png
    :alt: Worst-case hash table collisions
    :target: https://www.usenix.org/legacy/event/sec03/tech/full_papers/crosby/crosby.pdf
    :class: right-float

At lunch today, I told Eric about `Hash Attacks`_:
for many hash functions,
it's possible to construct a large set of keys that collide.
This can be used to cause a Denial of Service
as hashtable operations can be induced
to take *O(n)* time instead of *O(1)*.

Crosby and Wallach successfully demonstrated_ this
against a number of applications.

Andrew has a good writeup of `Hash Algorithm Attacks`_.

There are various mitigations suggested.
The one that I used when I first became aware of this problem
is to use a *salt* to the hash function.

In other words, change:

.. code:: C

    unsigned hash(const char* s)
    {
        unsigned h = 0;
        while (*s)
            h = h * 101 + (unsigned) *s++;
        return h;
    }

to:

.. code:: C

    unsigned hash(const char* s, unsigned salt)
    {
        unsigned h = salt;
        while (*s)
            h = h * 101 + (unsigned) *s++;
        return h;
    }

where ``salt`` is chosen *randomly* when the hash table is created
or when the process starts.
This should be enough to vary the order in which keys
are distributed to buckets from run to run.

.. _Hash Attacks:
.. _Denial of Service via Algorithmic Complexity Attacks:
.. _demonstrated:
    https://www.usenix.org/legacy/event/sec03/tech/full_papers/crosby/crosby.pdf
.. _Hash Algorithm Attacks:
    http://web.archive.org/web/20120318203841/http://www.team5150.com/~andrew/blog/2007/03/hash_algorithm_attacks.html

.. _permalink:
    /blog/2009/03/02/HashTableAttacks.html
