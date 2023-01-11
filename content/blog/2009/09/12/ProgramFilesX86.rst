---
title: "Launching 32-bit applications from batchfiles on Win64"
date: "2009-09-12"
permalink: "/blog/2009/09/12/Launching32bitApplicationsFromBatchfilesOnWin64.html"
tags: [windows, cmd, til]
---



.. image:: /content/binary/win64-biticon.gif
    :alt: Win64
    :class: right-float

I've been running the `64-bit version of Windows 7 RC`_ since June.
It's been quite painless on the whole.

One wrinkle that I ran into was with some batchfiles which
launch applications in ``%ProgramFiles%`` (normally ``C:\Program Files``).
Due to the magic `WOW64 redirector`_, 32-bit applications
are actually installed into ``%ProgramFiles(x86)%``\
—normally ``C:\Program Files (x86)``\ —\
instead of ``%ProgramFiles%``.
This is transparent to the 32-bit applications,
which think they're running in ``%ProgramFiles%`` (``C:\Program Files``).

However, the cmd.exe shell is 64-bit
(unless you make a special effort to run the 32-bit cmd.exe in SysWOW64),
so batchfiles see the 64-bit ``%ProgramFiles%`` which contains 64-bit applications.

Hence, a batchfile that launches an installed 32-bit application on Win64
must use ``%ProgramFiles(x86)%``, not ``%ProgramFiles%``.

It sounds trivial to have a batchfile detect
which flavor of ``%ProgramFiles%`` it should use,
but the parentheses in the environment variable name make it `tricky`_ to parse.
On earlier versions of Win64, the environment variable was called ``%ProgramFilesx86%``.
Presumably they added the strange parentheses into the variable name
because the directory name always included them.

Here's a tiny batchfile that will launch the 32-bit `DiffMerge`_
correctly on both Win64 and Win32 platforms.

.. sourcecode:: bat

    @setlocal
    @set _pf=%ProgramFiles%
    @if not "[%ProgramFiles(x86)%]"=="[]" set _pf=%ProgramFiles(x86)%
    @start "" /b "%_pf%\SourceGear\DiffMerge\DiffMerge.exe" %*

I long ago found that the safest way to test environment variables
whose values may include spaces, is to surround them with
both double quotes and square brackets.

.. _64-bit version of Windows 7 RC:
    /blog/2009/06/20/WhenVideoCardsGoBad.html
.. _WOW64 redirector:
    http://blogs.msdn.com/craigmcmurtry/archive/2004/12/14/301155.aspx
.. _tricky:
    http://marsbox.com/blog/howtos/batch-file-programfiles-x86-parenthesis-anomaly/
.. _DiffMerge:
    http://www.sourcegear.com/diffmerge/

.. _permalink:
    /blog/2009/09/12/Launching32bitApplicationsFromBatchfilesOnWin64.html
