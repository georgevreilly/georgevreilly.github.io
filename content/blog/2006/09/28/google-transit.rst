---
title: "Google Transit"
date: "2006-09-28"
permalink: "/blog/2006/09/28/GoogleTransit.html"
tags: [tech]
---



.. image:: /content/binary/google-transit.jpg
    :alt: Google Transit

I experimented with Google's new service,
`Google Transit <http://www.google.com/transit>`_.

It suggested this route for traveling from
my home to my work::

    Begin by walking
    1   Start at 4XXX 13th Ave S
    2   Go to Airport Way S & S Industrial Way (takes about 7 mins)

    Take the King County Metro 131 (Direction: NORTH)
    3   7:17pm leave from Airport Way S & S Industrial Way
    4   7:24pm arrive at 4th Ave S & S Jackson St
        
    End by walking
    5   Go to 315 5th Ave S (takes about 2 mins)

This fails badly in two respects.

First, four bus routes run along 15th Avenue S,
two blocks east of my house:
the `39 <http://transit.metrokc.gov/tops/bus/schedules/s039_0_.html>`_,
the `32 <http://transit.metrokc.gov/tops/bus/schedules/s032_0_.html>`_,
the `36 <http://transit.metrokc.gov/tops/bus/schedules/s036_0_.html>`_,
and the `60 <http://transit.metrokc.gov/tops/bus/schedules/s060_0_.html>`_.
The 39 drops me one block from work at 4th & Jackson.
The 60 leaves me at 12th & Jackson.
The 36 only runs along 15th after 7pm;
earlier than that, I a 10-minute walk to Beacon Ave.
And the 32 is an express bus that only runs at rush hour.

Second, it suggests that it's a seven-minute walk to
Airport Way S & S Industrial Way.
Actually, it's a two-mile walk, because I-5 and the railroad are in the 
way. You have the unpleasant choices of walking north to Spokane Street
and climbing down an endless set of stairs at the freeway onramp,
or south to the Lucile St bridge. And even if there were a direct route,
it would take at least 10 minutes to walk down there.

That said, it integrates very nicely with Google Maps.

The Google Transit page links to
`Metro Trip Planner <http://tripplanner.metrokc.gov/>`_,
which does a better job. Their disambiguation of addresses sucks, however. 
Try entering ``5th & Jackson``. It suggests a short list, starting with
``5TH AVE S & S JACKSON ST (in SEATTLE)``. However, if you actually type 
that address into the main page, it offers you a long list of suggestions.
In other words, it can't consume its own output.

**Update 2006/12/29**. I just tried the same experiment again.
Google Transit now correctly suggests walking two blocks east
to 15th Ave S and taking the 39.

.. _permalink:
    /blog/2006/09/28/GoogleTransit.html
