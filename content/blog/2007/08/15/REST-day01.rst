---
title: "Building a REST Web Service, day 1"
date: "2007-08-15"
permalink: "/blog/2007/08/15/BuildingARESTWebServiceDay1.html"
tags: [cozi, rest, c-sharp]
---



.. image:: https://upload.wikimedia.org/wikipedia/en/thumb/8/89/Resttriangle.svg/273px-Resttriangle.svg.png
    :alt: The REST Triangle
    :target: http://rest.blueoxen.net/
    :class: right-float

My first project at `Cozi`_ is to build a simple `REST`_-style Web Service.
Nobody here has done that before.

The first thing that I'm trying to get going is a simple `URL rewriter`_,
using an ASP.NET HttpModule.

I'm running Vista as my development desktop for the first time.
So far, not bad, but there are lots of new quirks to get used to.
I've been a good boy so far and I've left the User Access Control stuff enabled,
so that I'm not running with administrative privileges by default.

It's my first exposure to IIS 7.
I must say that the IIS UI is much improved
(a low bar to surmount).

My first problem was that `Skype was squatting on port 80`_,
preventing browser requests going to localhost.
This happens to me about once a year on a new dev machine,
and I always forget.

To get the HttpModule going, I had to follow
Mark Rasmussen's detailed instructions on
`making URL rewriting on IIS 7 work like IIS 6`_.
The code will be deployed on Windows Server 2003,
so IIS 6 compatibility is more important to me than IIS 7 purity.

I was trying to get some debug output appearing in `DebugView`_,
but my ``Trace.WriteLine``\ s were not showing up.
Some Googling eventually showed me that I had to enable
``Capture Global Win32``, which I never had to do before.
Presumably because ASP.NET is executing in a different desktop session.

.. _Cozi:
    http://www.cozi.com/
.. _REST:
    http://rest.blueoxen.net/
.. _URL rewriter:
    http://msdn2.microsoft.com/en-us/library/ms972974.aspx
.. _Skype was squatting on port 80:
    /blog/2005/11/17/SkypeAndSSL.html
.. _making URL rewriting on IIS 7 work like IIS 6:
    http://www.improve.dk/blog/2006/12/11/making-url-rewriting-on-iis7-work-like-iis6
.. _DebugView:
    http://www.microsoft.com/technet/sysinternals/utilities/debugview.mspx

.. _permalink:
    /blog/2007/08/15/BuildingARESTWebServiceDay1.html
