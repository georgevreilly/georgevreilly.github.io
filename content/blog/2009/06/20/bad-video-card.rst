---
title: "When Video Cards Go Bad"
date: "2009-06-20"
permalink: "/blog/2009/06/20/WhenVideoCardsGoBad.html"
tags: [tech, windows]
---



.. image:: https://www.overclock.net/attachments/nvidia/86626d1225425462-blown-capacitor-caps.jpg
    :alt: Blown Capacitors
    :target: http://www.hardforum.com/showthread.php?t=1411360
    :width: 200
    :class: right-float

I complained a week ago about my `display driver going berserk`_.
I blamed Windows Update, since it happened within hours of a pile of updates being installed.
I upgraded to the latest beta NVidia drivers on Monday
and it helped for a while, but by Wednesday,
it was almost as bad again as it had been last Friday.
It was infuriating and I was both entertaining and alarming my neighbors
with my cursing.

Today was the last day of a very busy sprint_ for me
and at last I had the time to dig into it.
I opened up the case and took a look at both video cards\
—I have two dual-head cards connected to three monitors—\
and one of them had partially blown capacitors like those in the picture.
I removed the bad card and did some graphics-intensive things for an hour,
and the other card behaved flawlessly.

Oddly, until someone mentioned that it might be a hardware problem yesterday,
it didn't occur to me, even though a video card blew in this machine last year.
I came in one morning to find a black monitor, and when I pulled out that card,
I found that some of the capacitors had popped right open with stuffing protruding.

On general principles, I had been meaning to repave this machine for a while.
I've had it since December 2007
and it was still running the original installation of Vista.
I booted from a DVD, reformatted my C: drive, and installed Windows 7 x64 RC1.

I finally have a 64-bit OS as my primary Windows desktop,
so I'll actually be using the `Win64 build of Vim that I maintain`_.
My first impressions of Windows 7 on this machine are very favorable,
but there's plenty more that I need to install
before the machine has everything that I need.

.. _display driver going berserk:
    /blog/2009/06/12/DisplayDriverNvlddmkmStoppedRespondingAndHasSuccessfullyRecovered.html
.. _sprint:
    /blog/2009/04/25/Sprints.html
.. _Win64 build of Vim that I maintain:
    /blog/2009/05/07/Windows7X64RunningInMacVirtualBox222.html

.. _permalink:
    /blog/2009/06/20/WhenVideoCardsGoBad.html
