---
title: "Virtualization"
date: "2007-10-24"
permalink: "/blog/2007/10/24/Virtualization.html"
tags: [programming]
---



.. image:: /content/binary/virtualization.jpg
    :alt: Virtualization
    :class: right-float

Picture this.

An external USB hard drive plugged in to a machine running Win64.
The OS has *virtualized* the underlying transport so that it's
essentially indistinguishable from an internal IDE, SCSi, or SATA drive.
Call the machine, Boss, and the USB drive, L:.

Boss is running Virtual PC, which is hosting a 32-bit *virtual* machine
on top of Boss's 64-bit OS.
Let's call the 32-bit VM, Sidekick.

Sidekick is not only a VM, but a *virtual* network host.
Boss is bridging connections to Sidekick, and
Sidekick and Boss both appear on the LAN as separate network hosts.

The USB drive has several ISO images, which Sidekick wants to use.
Sidekick connects to \\Master\L$ over the virtual network,
and uses a tool like `VcdTool`_ to mount the remote ISO on a
*virtual* CD drive.

Amazingly enough, it all just worked for me last night.

I'm trying to set up an environment where I can build
Vim with various 32-bit and 64-bit Microsoft compilers and,
more importantly, run the `Win64 binary`_.
I have a set of VM images with distinct flavors of MSVC,
which was necessary to update `INSTALLpc.txt`_
and to keep Make_mvc.mak building.

In previous iterations, I got Remote Desktop access to
a colleague's Win64 machine, but that was at Atlas,
so it's no longer an option.
I bought a new AMD64 desktop system a few months ago
and over the weekend set it up to `dual boot`_.

.. _VcdTool:
    http://jeranderson.wordpress.com/2006/10/17/installing-windows-vista-with-a-virtual-cddvd-drive/
.. _Win64 binary:
    /blog/2007/02/20/VimOnWin64Updated.html
.. _INSTALLpc.txt:
    http://vim.svn.sourceforge.net/viewvc/vim/vim7/src/INSTALLpc.txt?view=markup
.. _dual boot:
    http://apcmag.com/5485/dualbooting_vista_and_xp

.. _permalink:
    /blog/2007/10/24/Virtualization.html
