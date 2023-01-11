---
title: "Installing Rainlendar on Kubuntu"
date: "2006-12-26"
permalink: "/blog/2006/12/26/InstallingRainlendarOnKubuntu.html"
tags: [linux]
---



.. image:: /content/binary/rainlendar.png
    :alt: Rainlendar
    :target: http://www.rainlendar.net/

I've dualbooted my laptop between Linux and Windows since June, spending 
nearly all of my time in Linux. I started out with `Ubuntu`_ 6.06 (Dapper Drake),
but soon switched to `Kubuntu`_ (the KDE variant),
later upgrading to Kubuntu 6.10 (Edgy Eft).

To make this useful, certain key applications have to be available in both 
Windows and Linux. `Firefox`_ for browsing; `Thunderbird`_ for email;
`Rainlendar`_ for calendar; `KeePass`_ and `KeePassX`_ for password management;
among others.

My laptop has four partitions:

* Primary 1, NTFS - Windows, aka ``/windows`` or ``/dev/hda1``. 8GB
* Primary 2, Ext3 - Linux system partition, aka ``/`` or ``/dev/hda2``. 12GB
* Extended 1. Linux swap partition. 2GB.
* Extended 2, Ext3. Shared partition, aka ``/shared``. 15GB.

I'm using `NTFS-3G`_ under Kubuntu to read *and write* the NTFS partition.
Linux has long had support for reading NTFS partitions, but only recently 
has good support for writing NTFS partitions been added. It's a user-mode 
only filesystem, so it's not possible to run Linux from an NTFS partition.

I've installed `Ext2 IFS`_ (Installable File System) on Windows,
which allows me to read and write Ext3 (and Ext2) partitions.
I keep cross-platform data, such as my Thunderbird mail folders,
on the Ext3 partition, ``/shared``.
My ``home`` directory is also on the ``/shared`` partition,
so there's very little data that I mind losing on the ``/`` partition.
I haven't had any problems with Ext2 IFS, except that I've had no luck with 
external USB hard drives formatted as Ext3.
I'm not about to convert my Windows partition to Ext3, however.

Rainlendar is a fairly recent addition to the above list of cross-platform
apps. I was using Mozilla `Sunbird`_, but I never liked it very much.
It's very much the poor cousin of Firefox and Thunderbird.
Sunbird is slow, clunky, and ugly, with very few developers,
who have taken years just to get it to version 0.3.
It supports iCal as an export format, but publishing calendars to the web is a bear.

I discovered `Rainlendar`_ a couple of months ago. It's far slicker, with a 
large set of skins, and more functionality. iCal is the native format.
Rainlendar is based on `wxWidgets`_, so it's cross-platform.
Installation on Linux consists of extracting 
everything from a compressed tar file. There's no ``deb`` or ``rpm`` 
packages to install it into your system menu, alas.
I've been running it by using
``Alt+F2`` (Run Command) to launch 
``/shared/georger/rainlendar2/rainlendar`` (yuck!)

Earlier today, I ran across the very useful `ArsGeek`_ site, which has an 
enormous set of useful tips for Ubuntu users. One post on `installing 
Songbird`_ inspired me to figure out how to add Rainlendar to the KDE Menu.

First, open up a terminal, then::

    cd /opt
    sudo mkdir rainlendar2
    sudo chown georger:georger rainlendar2
    tar jxvf /shared/Downloads/Rainlendar-Lite-2.0.1.tar.bz2

Substituting your username twice in the ``chown`` line.

You should now be able to run Rainlendar from the command line::

    ./rainlendar2/rainlendar2 &

At this point, you may want to install a different skin, as the default 
look is overwhelming in my opinion. I use the `Vista skin`_. The older 
skins (``.zip`` files) need to be unzipped into ``rainlendar2/skins``;
newer skins (``.r2skin`` files) merely need to be copied into that 
directory.

Now to get the Rainlendar icon into ``/usr/share/pixmaps``.
(Finding the damn icon was the trickiest part of this whole exercise.)::

    cd rainlendar2/resources
    unzip -j resources.zrc res/logo-large.png
    sudo mv logo-large.png /usr/share/pixmaps/rainlendar.png

Finally, let's add Rainlendar to the Office menu. ArsGeek gives the 
instructions for using Alacarte under Gnome. For KDE, click the K\-Menu 
button, right-click on Office, and choose Edit Menu, which brings up the
KDE Menu Editor. Click New Item, then set:

* Name: Rainlendar
* Description: Calendar
* Comment: Manage calendar and todos
* Command: '/opt/rainlendar2/rainlendar2'

Click the blank icon button, then Other icons. Choose the rainlendar icon 
and click OK. Save the new menu entry.

You should now be able to launch Rainlendar from the Office menu. Enjoy!


.. _Ubuntu: http://www.ubuntu.com/
.. _Kubuntu: http://www.kubuntu.org/
.. _Firefox: http://www.mozilla.com/en-US/firefox/
.. _Thunderbird: http://www.mozilla.com/en-US/thunderbird/
.. _Sunbird: http://www.mozilla.org/projects/calendar/
.. _Songbird: http://www.songbirdnest.com/
.. _Rainlendar: http://www.rainlendar.net/
.. _Ext2 IFS: http://www.fs-driver.org/
.. _NTFS-3G: http://www.ntfs-3g.org/
.. _KeePass: http://keepass.sourceforge.net/
.. _KeePassX: http://keepassx.sourceforge.net/
.. _wxWidgets: http://www.wxwidgets.org/
.. _ArsGeek: http://www.arsgeek.com/
.. _installing Songbird: http://www.arsgeek.com/?p=615
.. _Vista skin: http://www.customize.org/details/45956

.. _permalink:
    /blog/2006/12/26/InstallingRainlendarOnKubuntu.html
