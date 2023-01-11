---
title: "Turn off Windows Defender on your builds"
date: "2013-11-11"
permalink: "/blog/2013/11/11/TurnOffWindowsDefenderOnYourBuilds.html"
tags: [windows, python, til]
---



I've spent some time this evening profiling a Python application on Windows,
trying to find out why it was so much slower than on Mac or Linux.
The application is an in-house build tool which reads a number of config files,
then writes some output files.

Using the RunSnakeRun_ Python profile viewer on Windows,
two things immediately leapt out at me:
we were running ``os.stat`` a lot
and ``file.close`` was really expensive.

A quick test convinced me that we were `stat-ing`_ the same files over and over.
It was a combination of explicit checks and implicit code,
like ``os.walk`` calling ``os.path.isdir``.
I wrote a little cache that memoizes the results,
which brought the cost of the ``os.stats`` down from 1.5 seconds to 0.6.

Figuring out why closing files was so expensive was harder.
I was writing 77 files, totaling just over 1MB, and it was taking 3.5 seconds.
It turned out that it wasn't the UTF-8 codec or newline translation.
It was simply that *closing* those files took far longer than it should have.

I decided to try a different profiler, hoping to learn more.
I downloaded the `Windows Performance Toolkit`_.
I recorded a couple of traces of my application running,
then I looked at them in the Windows Performance Analyzer,
whereupon I saw that in each case, the CPU spike of my app
was followed by a CPU spike in MsMpEng.exe.

`What's MsMpEng.exe`_? It's Microsoft's antimalware engine,
at the heart of Windows Defender.
I added my build tree to the list of excluded locations,
and my runtime *halved*.
The 3.5 seconds of file closing dropped to 60 milliseconds,
a 98% reduction.

The moral of this story is:
don't let your virus checker run on your builds.

.. image:: /content/binary/WindowsDefender-FileExclusion.png
    :alt: Windows Defender: Exclude directory for scanning

.. _RunSnakeRun:          
    http://www.vrplumber.com/programming/runsnakerun/
.. _stat-ing:
    http://docs.python.org/2/library/stat.html
.. _Windows Performance Toolkit:
    http://msdn.microsoft.com/en-us/library/windows/hardware/hh448170.aspx
.. _What's MsMpEng.exe:
    http://helpdeskgeek.com/windows-vista-tips/what-is-msmpeng-exe/

.. _permalink:
    /blog/2013/11/11/TurnOffWindowsDefenderOnYourBuilds.html
