---
title: "64-bit Windows 7"
date: "2009-07-11"
permalink: "/blog/2009/07/11/64bitWindows7.html"
tags: [windows, regex, til]
---



.. image:: /content/binary/win64-clr-jit-leak.png
    :alt: Humongous JIT memory leak
    :target: /content/binary/win64-clr-jit-leak.png
    :width: 400
    :class: right-float

I mentioned `three weeks ago`_ that I had just repaved my work dev box
and installed the 64-bit version of the Windows 7 RC.
Nine or ten years after I first ported parts of IIS to Win64,
I am finally running my main desktop on 64-bit Windows.
With one exception, it's been painless.
Programs have just worked, devices have just worked.
There are relatively few native x64 applications,
but for the most part it doesn't matter.
The cases where it does matter—\
e.g., shell extensions such as `TortoiseSVN`_\ —\
are available as 64-bit binaries.

I briefly flirted with using the 64-bit build of Python,
but realized that I would have to recompile several eggs as 64-bit binaries.
That was too painful and the 32-bit binary did everything I needed.

Building in Visual Studio 2005 is noticeably faster.
I'm not sure how much of it was due to accumulated cruft after 18 months on Vista,
but builds there were very slow.

The one exception was a major problem for the first week and a half.
Whenever I ran our ASP.NET web application,
it would go berserk, eat up all 4GB of my physical RAM,
push the working set of IIS's w3wp.exe to *12GB*,
and max out one of my 4 cores!
The only way to maintain any sanity was to run ``iisreset``
every 20 minutes to gently kill the process.

`WinDbg`_ and `Process Explorer`_ showed that the rogue thread was stuck in a loop in
``mscorjit!LifetimesListInteriorBlocksHelperIterative<GCInfoLiveRecordManipulator>``.
I passed a minidump on to my former colleagues in IIS, who sent it to the CLR team.
They said:

     The only thing I can tell is that it is Regex,
     and some regex expression compiled down to a method with 456KB of IL.
     That is *huge*, and yes 12GB of RAM consumed for something like that is expected.

With that clue, I was able to track down the problem,
a particularly foul regex, built from a 10KB string, with 32 alternating expressions,
each of which contains dozens of alternated subexpressions.
The string is built from many smaller strings,
so it's not obvious in the source just how ugly it is.
I commented out the ``new Regex()`` and my problems went away.

Regardless of how ugly the regex is, this is a major regression in the CLR.
This code has been working without blatant problems for two years
on the 32-bit flavors of XP, Server 2003, Vista, and Server 2008.
I've been meaning to try this code on 32-bit Windows 7,
but have been too busy.

(The original, long-gone author was apparently aware that the regex
is expensive to create because he runs a background thread to ``new`` the regex,
which should have told him something.
We'll fix the code that uses the regex to do something saner, soon.)

All that aside, I've been happy with the 64-bit version of Windows 7.

.. _three weeks ago:
    /blog/2009/06/20/WhenVideoCardsGoBad.html
.. _TortoiseSVN:
    http://tortoisesvn.net/
.. _WinDbg:
    http://www.microsoft.com/whdc/devtools/debugging/default.mspx
.. _Process Explorer:
    http://technet.microsoft.com/en-us/sysinternals/bb896653.aspx

.. _permalink:
    /blog/2009/07/11/64bitWindows7.html
