---
title: "Daylight Savings Time and JavaScript"
date: "2008-03-13"
permalink: "/blog/2008/03/13/DaylightSavingsTimeAndJavaScript.html"
tags: [calendar, javascript]
---



.. image:: /content/binary/js-date-dst2.png
    :alt: Daylight Savings Time and JavaScript
    :target: http://blogs.cozi.com/tech/2008/03/daylight-savings-time-and-javascript.html
    :class: right-float

The JavaScript engines in Firefox 2 (Windows) and IE6
can't handle the new Daylight Savings Time rules in the U.S.
The ``Date()`` function returns a value that is off by an hour
if the system time is between the second Sunday of March
and the first Sunday of April.

`More at the Cozi Tech Blog`_.

**Update 2008/03/14**: *Mea culpa*.
This is *not* a widespread problem.
It is caused by the presence of ``set TZ=PST8PDT``
in my ``C:\AutoExec.bat``.
Per KB932590_, the existence of the ``TZ`` environment variable
will cause the CRT to use the old DST rules.
(I can't remember why I set ``TZ`` several years ago.
It's part of the accumulated mess of files that
I bring everywhere with me.)

.. _More at the Cozi Tech Blog:
    http://blogs.cozi.com/tech/2008/03/daylight-savings-time-and-javascript.html
.. _KB932590:
    http://support.microsoft.com/kb/932590

.. _permalink:
    /blog/2008/03/13/DaylightSavingsTimeAndJavaScript.html
