---
title: "Subtracting Compound Objects"
date: "2016-05-17"
permalink: "/blog/2016/05/17/SubtractingCompoundObjects.html"
tags: [programming, til]
---



Quick!
How many days between ``2014-11-29`` and ``2016-05-17``?
What's the angle between the hour hand and the minute hand on an analog clock
when the time reads 11:37?

The hard way to compute the difference between the two dates
is to start counting back months and days until you reach the earlier date,
or equivalently to count forward from the beginning.
(Don't forget that Feb 2016 has 29 days but Feb 2015 has 28.)
Similarly with the angle between the hands.

The easier way is to compute the number of units between the first point
and some reference (or base) point,
to do the same for the second point,
and to subtract the two numbers.

Say the base date is ``2000-01-01``.
The first date, ``2014-11-29`` is 14 years since the base date,
and 2000, 2004, 2008, and 2012 are leap years,
so 365×14 + 4 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 29 = 5,447 days.
The second date, ``2016-05-17``, is
365×16 + 4 + 31 + 29 + 31 + 30 + 17 = 5,982 days since 2000-01-01.
(Four not five leap years, since 2016 is incomplete and Feb 29 is counted.)
The difference is 535 days.

All modern date libraries have some notion of an epoch;
typically ``1970-01-01T00:00:00Z`` is zero seconds.
Compute the number of seconds since the epoch for both dates, then subtract,
and divide the remainder by 24×60×60.
Note: this does not take daylight savings into account,
when certain days are 23 or 25 hours long.
However, a decent date library will handle all of this.

I learned this trick from Charles Bryant circa 1984 on Vax Pascal.
I don't believe there was a date library;
we just stored the year/month/day in a custom Pascal record.

.. _permalink:
    /blog/2016/05/17/SubtractingCompoundObjects.html
