---
title: "Daylight Saving Time"
date: "2016-03-12"
permalink: "/blog/2016/03/12/DaylightSavingTime.html"
tags: [tech, calendar]
---



.. image:: /content/binary/what-is-daylight-saving-time.jpg
    :alt: What is Daylight Saving Time
    :target: http://www.theverge.com/2016/3/12/11186842/daylight-saving-time-car-crashes-work-accidents-fatigue
    :class: right-float

`Daylight Saving Time is hot garbage`_
is a typical article you can expect to read this weekend
condemning DST.

My own dislike of DST was boosted when I worked on calendar software at Cozi.
We learned the hard way that we needed to test our latest software
ahead of both the start and end of DST each year.
That's trickier than you might think.
Setting the computer's clock forward a couple of weeks,
past the change of DST, is one thing;
getting the changed time to last for more than a few minutes is another.
Most computers aggressively sync their clocks to a network time server,
which can be tricky to disable.

I no longer remember the details of the bugs.
I think one was due to an all-day appointment not lasting 24 hours.
Depending on whether the clock has moved forward or back,
a day is 23 or 25 hours long,
and you either instantaneously jump from 2am to 3am,
or you experience that hour twice.
You can't just add 24*60*60 seconds to a timestamp and move to the same time the next day.

`Falsehoods programmers believe about time`_ and
`More falsehoods programmers believe about time`_
have lots more examples of invalid time-based beliefs.

Timezones were another pain as there are several changes a year.
We had to update our copy of the `Olson timezone database`_ a few times.

.. _Daylight Saving Time is hot garbage:
    http://www.theverge.com/2016/3/12/11186842/daylight-saving-time-car-crashes-work-accidents-fatigue
.. _Falsehoods programmers believe about time:
    http://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time
.. _More falsehoods programmers believe about time:
    http://infiniteundo.com/post/25509354022/more-falsehoods-programmers-believe-about-time
.. _Olson timezone database:
    https://en.wikipedia.org/wiki/Tz_database

.. _permalink:
    /blog/2016/03/12/DaylightSavingTime.html
