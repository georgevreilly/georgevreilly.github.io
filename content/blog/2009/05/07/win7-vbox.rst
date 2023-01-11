---
title: "Windows 7 x64 running in Mac VirtualBox 2.2.2"
date: "2009-05-07"
permalink: "/blog/2009/05/07/Windows7X64RunningInMacVirtualBox222.html"
tags: [windows, mac]
---



.. image:: /content/binary/win7-x64-vbox.jpg
    :alt: Windows 7 x64 running in Mac VirtualBox 2.2.2
    :target: /content/binary/win7-x64-vbox.jpg
    :width: 300
    :class: right-float

I ported `Vim to Win64`_ but I don't have a convenient Win64 system
to test it on.

I decided to install the Win64 build of the Windows 7 RC on `VirtualBox`_,
which has supported 64-bit guest operating systems since version 2.0.

It worked without problems on my MacBook Pro.
I used VirtualBox's Virtual Media Manager to mount the Windows 7 ISO
and installed from that.
See also the `handy guide`_.
(Why does Windows 7 offer a choice of upgrading from a previous
version of Windows on a virgin disk?)
After completing the installation of the operating system,
I installed the Guest Additions for mouse pointer integration
and other goodies.

As always with VirtualBox VMs on my MacBook,
I had to fix the Network settings to work over WiFi.
When the VM is turned off, go to Settings,
choose the Network tab.
Change “Attached to” from “NAT” to “Bridged Adapter”
and “Name” from “en0: Ethernet” to “en1: AirPort”.
Tip: to get a right-click without a mouse,
place two fingers on the trackpad and click the trackpad button,
or Shift+F10.

I tried installing the Win64 build of Win 7 on
my Win32 Vista desktop box at work.
The host system bluescreened within seconds of starting the installer!
I filed `ticket 3963`_.

I had inadvertently installed the Win32 build first on my work system.
That worked fine.
It also seemed to have snappy disk I/O.
When I unzipped the Win64 Vim binaries
(not having realized yet that I had the Win32 Win 7),
it was slower than unzipping in the host operating system,
but not unreasonably so.
On my MacBook, the details pane from the Win 7 zip extractor
said that it was running at a mere 260KB per second,
which is pitiful.
It certainly wasn't that slow when installing the OS
onto the virtual disk.


.. _VirtualBox:
    http://www.virtualbox.org/
.. _handy guide:
    http://www.intowindows.com/how-to-install-windows-7-on-virtualbox/
.. _ticket 3963:
    http://www.virtualbox.org/ticket/3963
.. _Vim to Win64:
    http://code.google.com/p/vim-win3264

.. _permalink:
    /blog/2009/05/07/Windows7X64RunningInMacVirtualBox222.html
