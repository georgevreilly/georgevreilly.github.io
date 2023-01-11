---
title: "Ubuntu Netbook Remix 9.04"
date: "2009-04-25"
permalink: "/blog/2009/04/25/UbuntuNetbookRemix904.html"
tags: [linux]
---



.. image:: https://www.jpierre.com/files/2009/04/screenshot.png
    :alt: Ubuntu Netbook Remix
    :target: http://www.jpierre.com/2009/04/installing-ubuntu-netbook-remix-904-jaunty-jackelope-on-eee-pc-the-howto-guide/
    :width: 512

I spent much of today playing around with
the brand-new Jaunty/9.04 release of the `Ubuntu Netbook Remix`_
on my `Eee 1000H netbook`_.
Previously I had run the Hardy/8.04 version of `Ubuntu Eee`_ on this system.
I had never bothered to update to Intrepid/8.10,
but now that UNR is fully supported by Canonical,
I thought it was time to try it out.

I `downloaded`_ the UNR image last night onto my Mac,
and transferred the image to a 1GB USB stick this morning.
(The `Mac instructions`_ required a little tweaking.)

I spent some time running the Live Image first, before clean installing.
Everything worked seamlessly except the `microphone`_.
WiFi worked, the webcam worked, sound playback worked,
the touchpad was configured in a sane way.
All of these were problems for me when I first installed Ubuntu Eee.
That they worked now was not too surprising,
since the Asus Eee 1000 is a `Tier 1 supported`_ system,
but it's nice to get the confirmation.

One of the first things to strike me about the Live Image
was how nice the fonts looked.
I'm `sensitive to typography`_ and
the default font hinting settings on previous versions of Ubuntu
have always looked like crap: spindly and awkward.
I found it hard to take seriously an operating system that looked so unprofessional.
The Jaunty font hinting yields thicker letters,
which look a lot more like the Mac's shape-preserving font rendering,
though not as good.
The main exception, oddly enough, is the font
used in the netbook-launcher, which looks jagged.

I went ahead and installed Jaunty.
The installer offered me an option to install Jaunty
side-by-side with the existing operating systems,
Ubuntu Eee 8.04 and Windows XP.
I wanted to overwrite the existing Ubuntu partition
and I had to jump through several hoops to make that happen.
The partition editor is pretty and an improvement over GParted.
The timezone picker is also very slick,
with a clickable world map.

Partitioning aside, the installation was quick and painless.
`JPierre`_ has a useful guide to some issues that he ran into.

I've spent most of the afternoon and evening
installing various applications that I care about.
Sleep and hibernate just work now.
Sleep worked before but there were always some obnoxious errors when going to sleep.

As a hardcore Vim user, I use keyboard shortcuts a lot.
Alt+Tab (or Apple+Tab) is my primary method for switching between applications
on Windows, Linux, and Mac.
I had never found a keyboard shortcut for switching back to the netbook-launcher:
I'd always have to click the Ubuntu logo in the top-left corner of the desktop.
Buried in the Keyboard Shortcuts Preferences,
I finally found Ctrl+Alt+Tab, which shows a popup,
and Ctrl+Alt+Escape, which switches immediately.

Other random notes:

* I had to rediscover `ntfs-config to automount`_ my NTFS drives.
* Useful apps like Skype can be installed from the `Medibuntu`_ repository.
* It's necessary to run `dropbox start -i`_ before Dropbox will download the
  real daemon and actually start running.

I have a Linux machine at work that runs Kubuntu.
I kicked off the upgrade from Intrepid to Jaunty yesterday before I left.
I'll find out on Monday how well that worked.


.. _Ubuntu Netbook Remix:
    http://www.canonical.com/projects/ubuntu/unr
.. _Eee 1000H netbook:
    /blog/2008/11/26/Eee.html
.. _Ubuntu Eee:
    http://www.ubuntu-eee.com/
.. _downloaded:
    http://www.ubuntu.com/getubuntu/download-netbook
.. _Mac instructions:
    https://help.ubuntu.com/community/Installation/FromImgFiles/#Mac%20OS%20X
.. _microphone:
    https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/354620
.. _Tier 1 supported:
    https://wiki.ubuntu.com/HardwareSupport/Machines/Netbooks
.. _sensitive to typography:
    /blog/2009/02/18/DramaturgyLaTeX.html
.. _JPierre:
    http://www.jpierre.com/2009/04/installing-ubuntu-netbook-remix-904-jaunty-jackelope-on-eee-pc-the-howto-guide/
.. _ntfs-config to automount:
    http://ubuntuforums.org/showthread.php?t=785263
.. _Medibuntu:
    https://help.ubuntu.com/community/Medibuntu
.. _dropbox start -i:
    http://forums.getdropbox.com/topic.php?id=8695

.. _permalink:
    /blog/2009/04/25/UbuntuNetbookRemix904.html
