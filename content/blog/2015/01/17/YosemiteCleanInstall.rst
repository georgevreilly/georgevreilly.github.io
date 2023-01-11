---
title: "Clean Installing Yosemite"
date: "2015-01-17"
permalink: "/blog/2015/01/17/YosemiteCleanInstall.html"
tags: [mac]
---



.. image:: https://cdn.macrumors.com/article-new/2014/05/os_x_yosemite_roundup.jpg
    :alt: OS X Yosemite
    :target: https://en.wikipedia.org/wiki/OS_X_Yosemite
    :class: right-float

Every few years, I find it necessary to wipe my computers
and do a clean install of the operating system.
As a developer and a power user, I install a lot of software.
The cumulative effect of installations and upgrades
is to leave a lot of cruft on the machines.
Entropy increases and the machines grow slower and perhaps less reliable.
So I like to wipe the hard disk, install a new operating system,
and reinstall only those apps that I know I need.

My mid-2012 MacBook Pro came with OS X 10.7.
Shortly thereafer, 10.8 was released and I promptly upgraded; likewise with 10.9.
Yosemite_ (10.10) was released in October 2014,
but I held off switching until now,
as I knew I wanted to do a clean install,
which meant setting aside a sizeable block of time.

I backed up everything during the week,
over and above my normal backups of external drives,
`CrashPlan`_, `Dropbox`_, and `GitHub`_.
I made a list of all the apps that I care about and of various settings.
And I prepared a `bootable thumb drive`_ with the OS X Yosemite Installer app.

Last night, I inserted the thumb drive into the USB slot.
I restarted the machine while holding down the Option key,
which brought me to a boot menu.
I used Disk Utility to erase the partition and then I installed Yosemite.

And then I spent many hours installing apps I care about
and restoring data.

I've been a fan of the Homebrew_ package manager for several years.
It does a great job of installing and updating developer-related tools
for use at the command line.
Last year, I learned about a sister project, `Homebrew Cask`_,
which takes of installing graphical applications.
Instead of downloading DMGs, I used Cask to install a number of apps.

I discovered `Caskroom Fonts`_ last night,
which took care of installing most of the fonts I care about.
One exception: I wanted to install Consolas and some of the other C* fonts
from the `ClearType Font Collection`_, without installing Microsoft Office.
It's possible to do that via Microsoft's `Open XML File Format Converter for Mac`_.

My 2½-year-old machine feels faster and more responsive after the clean install.
I upgraded my late-2013 work MacBook Pro to Yosemite a couple of months ago,
without seeing a difference in performance,
so I attribute the improvement to getting rid of a lot of crap.


.. _Yosemite:
    http://en.wikipedia.org/wiki/OS_X_Yosemite
.. _CrashPlan:
    https://www.crashplan.com
.. _Dropbox:
    https://www.dropbox.com/
.. _GitHub:
    https://github.com/
.. _bootable thumb drive:
    http://www.macworld.com/article/2367748/how-to-make-a-bootable-os-x-10-10-yosemite-install-drive.html
.. _Homebrew:
    http://brew.sh/
.. _Homebrew Cask:
    http://caskroom.io/
.. _Caskroom Fonts:
    https://github.com/caskroom/homebrew-fonts
.. _ClearType Font Collection:
    http://www.poynter.org/how-tos/visuals/32588/the-next-big-thing-in-online-type/
.. _Open XML File Format Converter for Mac:
    http://zjhzxhz.com/2014/01/install-microsofts-consolas-font-on-mac-os-x/

.. _permalink:
    /blog/2015/01/17/YosemiteCleanInstall.html
