---
title: "ViEmu: a vi and Vim emulator for Visual Studio"
date: "2006-04-09"
permalink: "/blog/2006/04/09/ViEmuAViAndVimEmulatorForVisualStudio.html"
tags: [vim, windows]
---



Vim vs. Visual Studio
---------------------

I've been an `obsessive vi user </blog/2005/12/30/20YearsOfVi.html>`_
for more than 20 years. Vi keystrokes are indelibly burned into my
`muscle memory <http://www.oreilly.com/news/zenclavier_1299.html>`_.
When I have to use Notepad or Word or Visual Studio, I feel crippled.
I have to work harder to do simple things; I have to type too many chords
with Alt and Ctrl; I have to take my hands off the home keys to use the
cursor keys and the mouse.

In the mid-90s, I adopted `Vim <http://www.vim.org>`_ (Vi IMproved)
to the point where I became a significant contributor, writing a big chunk of the
`Win32 code </blog/2005/12/30/20YearsOfVi.html>`_.

While I was at Microsoft, I hardly ever used Visual Studio.
I edited my C/C++ code with Vim,
I compiled and linked it with the
`NT Build Environment <http://www.osronline.com/article.cfm?id=54>`_
and I debugged it with
`WinDbg/ntsd/kd <http://www.microsoft.com/whdc/devtools/debugging/default.mspx>`_.
I was hardly alone in this. In the Windows division, your code has to
build with the NT build environment, and the Windows debuggers are much
better supported than the Visual Studio debugger for developing the OS.

Now that I'm programming in C#, using the Visual Studio IDE makes a lot
more sense. VS's IntelliSense for C# is much richer than
`Vim7's Omni completion
<http://cvs.sourceforge.net/viewcvs.py/vim/vim7/runtime/doc/version7.txt?view=markup>`_,
especially when coupled with `ReSharper <http://www.jetbrains.com/resharper/>`_,
and VS is the debugger of choice for managed code.
I've been spending a fair amount of time in the VS IDE, especially when
pair programming, but I've also been switching back to Vim a lot.
When I'm struggling with unfamiliar code, VS's IntelliSense is a great comfort;
when I'm moving a lot of text around, Vim suits me far better.


ViEmu
-----

Earlier this week, by way of its `graphical Vim cheat sheet
<http://viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html>`_,
I found an interesting compromise.
`ViEmu <http://viemu.com/>`_ is a vi/Vim emulator for VS\-2003 and
VS\-2005.

ViEmu implements most of the vi keystrokes and many of the Vim extended
keystrokes, right inside the Visual Studio IDE.
It uses the native VS IntelliSense in place of Vim's completion
functions. ViEmu even implements some of the more common Ex command line,
including most of the ``:%s`` regular expression substitutions.
The author, who seems to be known only as JNG, is responsive.
Within 24\-hours of my reporting some missing keystrokes, he had
implemented them in a new minor release.

It does not, however, support VimL, the Vim extension language,
so if you have an extensive suite of Vim plugins, as I do, they're not
going to work in ViEmu.

All in all, I'm favorably impressed with ViEmu.
It provides much of the muscle memory experience of Vim
inside of Visual Studio. Technically, it can't have been easy to
impose such a radically different input model on VS or
to emulate Vim and Ex fairly faithfully.

Vim has always been free (actually `charityware
<http://vimdoc.sourceforge.net/htmldoc/uganda.html>`_),
but JNG `charges <http://viemu.com/purchase.html>`_ for ViEmu.
Right now, I'm in the 30-day trial period, but I fully expect
that I'll pay for a license before the trial is up.


VisVim
------

Vim comes with a Visual Studio add-in called VisVim, which is based on
another add-in called VisEmacs. It allows VS5 and VS6 to use Vim
as the default editor, albeit externally to the IDE: Vim continues to run
in its own window.

A few weeks ago, Bram asked me if I could get VisVim to compile with
VS\-2003. I tried, but I was unable. Necessary headers are no longer
included with VS\-2003 or VS\-2005. No doubt this is because the Add-In
architecture changed radically with the introduction of Visual
Studio\-.NET.

Work is underway, albeit very slowly, to create
`VisEmacs.NET <http://blogs.snowmoonsoftware.com/>`_.
At some point, it may be worth creating a merger of VisVim and
VisEmacs.NET.

End Notes
---------

`viWord <http://www.dready.org/blog/section/viword/>`_ allows you to use vi
keybindings in Microsoft Word. It's not nearly as full featured as ViEmu
and I found that I didn't like it enough to keep it around.

This post was, of course, composed in Vim. I wrote it in lightly marked-up
plain text and converted it to HTML with VST,
`Vim reStructured Text <http://skawina.eu.org/mikolaj/vst.html>`_.
Blogging with VST will be the topic of a future post.

To fully take advantage of Vim7's Omni completion, you need a
patched version of `Exuberant Ctags <http://ctags.sourceforge.net/>`_.
I've made a `Win32 binary available <http://georgevreilly.com/vim/ctags.html>`_.

.. _permalink:
    /blog/2006/04/09/ViEmuAViAndVimEmulatorForVisualStudio.html
