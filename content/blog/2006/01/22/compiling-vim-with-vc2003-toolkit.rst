---
title: "Compiling Vim with Visual C++ 2003 Toolkit"
date: "2006-01-22"
permalink: "/blog/2006/01/22/CompilingVimWithVisualC2003Toolkit.html"
tags: [vim, c++, til]
---



I've been trying to make `Vim 7 <http://www.vim.org/develop.php>`_
compile with the
`Microsoft Visual C++ 2003 Toolkit
<http://msdn.microsoft.com/visualc/vctoolkit2003/>`_,
as a favor to Bram Moolenaar, the primary author of Vim.
He wants to be able to use the free compiler as the
primary build tool for the Win32 version of Vim.

Oh. My. God.

The VC2003 toolkit may include a full optimizing compiler,
but it's certainly far from a complete system for building
Windows binaries.

First, I discovered that it came only with the C library headers,
but not the Windows headers. That was easily rectified. Download the
`Platform SDK <http://www.microsoft.com/msdownload/platformsdk/sdkupdate/>`_.
Just the Windows Core SDK subset. This also got me nmake.

At this point, I was able to compile Vim, but not to link it.
The linker required cvtres.exe, to link some resources.
Some googling showed me that this is included in the `.NET Runtime
<http://www.microsoft.com/downloads/details.aspx?familyid=262d25e3-f589-4842-8157-034d1e7cf3a3>`_.

The main Vim executable now linked, but the shell extension DLL didn't.
I didn't have msvcrt.lib! It took me more detective work to learn
that I'd have to install the `.NET Framework SDK
<http://www.microsoft.com/downloads/details.aspx?familyid=9b3a2ca6-3647-4070-9f41-a333c6b9181d>`_ to get msvcrt.lib. There are several clever hacks out there
that generate msvcrt.lib from msvcrt.dll, with the help
of ``link -dump -exports`` and a `sed script
<http://www.delta3d.org/article.php?story=20050721180227305&topic=tutorials>`_,
but these do not include the all-important ``_DllMainCRTStartup@12``,
the **real** entrypoint for DLLs linked with msvcrt.

All the necessary steps for getting the downloads are summarized on the
`Code::Blocks wiki
<http://wiki.codeblocks.org/index.php?title=Integrating_Microsoft_Visual_Toolkit_2003_with_Code::Blocks_IDE>`_. Code::Blocks is an open-source IDE that can host the
VC2003 toolkit, GCC, and a number of other compilers.

So why bother with the VC2003 toolkit, since 
`Visual C++ 2005 Express Edition
<http://msdn.microsoft.com/vstudio/express/visualC/default.aspx>`_
is freely downloadable?

The main reason is that it's free only for the first year,
and Bram wants something that will still be available after
November 2006, so that anyone can compile it.

I have also ported Vim 7 to compile with VC2005 Express.
It was fairly straightforward, after I had added the following

.. code:: c

    #if _MSC_VER >= 1400
    # define _CRT_SECURE_NO_DEPRECATE
    # define _CRT_NONSTDC_NO_DEPRECATE
    #endif

to shut up the warnings about `deprecated CRT functions
<http://msdn.microsoft.com/msdnmag/issues/05/05/SafeCandC/default.aspx>`_.
I also had to make it link with libcmt.lib (multithreaded) instead of libc.lib,
as the single-threaded static library is gone.

I still need to make sure that everything continues to work with
the retail compilers, VC6, VC7.1, and VC8, before passing my changes
back to Bram. Sigh.

.. _permalink:
    /blog/2006/01/22/CompilingVimWithVisualC2003Toolkit.html
