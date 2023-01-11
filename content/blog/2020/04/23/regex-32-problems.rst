---
title: "Now You Have 32 Problems"
date: "2020-04-23"
permalink: "/blog/2020/04/23/regex-32-problems.html"
tags: [regex, performance, til]
---



\ 

    Some people, when confronted with a problem, think
    “I know, I'll use regular expressions.”
    `Now they have two problems`_.

        — Jaime Zawinksi

A Twitter thread about `very long regexes`_
reminded me of the `longest regex`_ that I ever ran afoul of,
a particularly horrible multilevel mess
that had worked acceptably on the 32-bit .NET CLR,
but brought the 64-bit CLR to its knees.

    Whenever I ran our ASP.NET web application [on Win64],
    it would go berserk, eat up all 4GB of my physical RAM,
    push the working set of IIS's w3wp.exe to *12GB*,
    and max out one of my 4 cores!
    The only way to maintain any sanity was to run ``iisreset``
    every 20 minutes to gently kill the process.

    WinDbg and Process Explorer showed that the rogue thread was stuck in a loop in
    ``mscorjit!LifetimesListInteriorBlocksHelperIterative<GCInfoLiveRecordManipulator>``.
    I passed a minidump on to my former colleagues in IIS, who sent it to the CLR team.
    They said:

         The only thing I can tell is that it is Regex,
         and some regex expression compiled down to a method with 456KB of IL.
         That is *huge*, and yes 12GB of RAM consumed for something like that is expected.

    With that clue, I was able to track down the problem,
    a particularly foul regex, built from a 10KB string,
    with 32 alternating expressions,
    each of which contains dozens of alternated subexpressions.
    The string is built from many smaller strings,
    so it's not obvious in the source just how ugly it is.

I never wrote a followup post explaining how I dealt with this beast.

The regex was used on the `Cozi calendar`_
to parse appointments in everyday language,
such as “Ann/John Dinner out Friday at 8pm”
or “John's birthday every Dec. 7”.
These would get translated into (possibly recurring) iCalendar_ appointments.

Some of the subexpressions mentioned above looked like:

* ``ordinals = "1st|2nd|...|31st"``
* ``short_days = "Sun|Mon|...|Sat"``
* ``full_days = "Sunday|Monday|...|Saturday"``
* ``short_months = "Jan|Feb|...|Dec"``
* ``full_months = "January|February|...|December"``
* ``recurrence = "((every|each)? (first|second|third|fourth|fifth|last)? " 
  + "(" + short_days + "|" + full_days + ")" + ...``

I've elided the intermediate values but they were spelled out in the original.
Some of the simpler subexpressions were repeated several times,
nested inside others.

This all screamed *grammar* and *real parser* to me,
but the test suite also screamed *here be dragons!*

I resisted the temptation
to rewrite the appointment parser from scratch with a proper grammar,
or to experiment with a real natural language parser,
though it remained on my personal todo list for the rest of my time at Cozi.
We were migrating from C# to Python at that point,
and the legacy appointment parser was one of the few remaining pieces
that prevented us from shutting down the .NET servers.

Instead, I changed the appointment parser code
so that it didn't attempt to match the entire 10KB monster in one go.
I looped through each of the 32 top-level disjunctions,
manually performing the alternation.
If any one of those matched, then I had what I needed.
Reducing the regexes to a few hundred characters each
tamed the combinatorial explosion of backtracking state.

Regexes definitely have a place,
but do not try to implement a full grammar as a single regular expression.


.. _Now they have two problems:
    http://regex.info/blog/2006-09-15/247
.. _very long regexes:
    https://twitter.com/nbashaw/status/1253186961482715136
.. _longest regex:
    /blog/2009/07/11/64bitWindows7.html
.. _Cozi calendar:
   https://www.cozi.com/calendar/
.. _iCalendar:
   https://tools.ietf.org/html/rfc5545

.. _permalink:
    /blog/2020/04/23/regex-32-problems.html
