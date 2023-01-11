---
title: Backwards Ranges in Python
date: 2022-12-19 15:20
tags: [python,til]
permalink: /blog/2022/12/19/BackwardsRangesInPython.html
filter: markdown+fenced_code+codehilite
summary: The asymmetry of specifying backward ranges in Python
---

In Python, if you want to specify a sequence of numbers
from `a` up to (but excluding) `b`,
you can write `range(a, b)`.
This generates the sequence `a, a+1, a+2, ..., b-1`.
You start at `a` and keep going until the next number would be `b`.

In Python 3, `range` is *lazy*
and the values in the sequence do not materialize
until you consume the range.

```pycon
>>> range(3,12)
range(3, 12)
>>> list(range(3,12))
[3, 4, 5, 6, 7, 8, 9, 10, 11]
```

Trey Hunner makes the point that
[range is a lazy iterable](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/)
rather than an iterator.

You can also *step* by an increment other than one:
`range(a, b, s)`.
This generates `a, a+s, a+2*s, ..., b-s`
(assuming that `(b - a) % s == 0`;
i.e., `a` and `b` are separated by an exact multiple of `s`.)

```pycon
>>> list(range(3, 12, 3))
[3, 6, 9]
```

What if you want to count down?
`range(b, a, -s)` won't do what you want.

```pycon
>>> list(range(12,3, -3))
[12, 9, 6]
```

Why? Because you're starting at `b`,
a value that doesn't appear in the forward range,
and you're ending before you reach `a`,
a value that is certainly in the forward range.
You have to subtract `s` from both `b` and `a`:

When you use `range(b-s, a-s, -s)`,
you get `b-s, b-2*s, ..., a+s, a`.

```pycon
>>> list(range(12-3,3-3, -3))
[9, 6, 3]
>>> list(range(12-3,3-3, -3)), list(reversed(range(3, 12, 3)))
([9, 6, 3], [9, 6, 3])
```
