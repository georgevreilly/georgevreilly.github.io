---
title: "Progressive Sums"
# date: "2023-mm-dd"
permalink: "/drafts-drafts-drafts/2023/mm/dd/ProgressiveSums.html"
tags: [python]
draft: true
---

The heart of this solution is reducing the time
to compute the maximal window from the naive O(n**2) time to O(1)
by noting that in the inner loop,
W-1 of the additions are the same as on the previous iteration of the outer loop.

.. code:: python

    def window_sums(v, W):
        sums = []
        for i in range(0, len(v)-W):
            total = 0
            for j in range(i, i+W):
                total += v[j]
            sums.append(total)

Instead, we can simply subtract the previous leftmost item off the running total
and add the new rightmost item.


.. code:: python

    def window_sums(v, W):
        sums = []
        total = sum(v[0:W-1])  # O(n)
        prev = 0
        for i in range(0, len(v)-W):
            total += v[i + W - 1] - prev
            prev = v[i]
            sums.append(total)
