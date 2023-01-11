---
title: "Hardware Lazarus"
date: "2008-11-18"
permalink: "/blog/2008/11/18/HardwareLazarus.html"
tags: [tech]
---



.. image:: https://www.erowid.org/devel/misc/galleries/maxtor_onetouch_3/images/img_2133.jpg
    :alt: Maxtor OneTouch III disassembly
    :class: right-float
    :target: http://www.erowid.org/devel/misc/archives/000083.shtml

My formerly trusty Casio Exilim EX-Z1000 camera went berserk one night in September.
The zoom lens wedged open and nothing I did would persuade it to retract
into the case or take more photos.
The zoom had grown a little tempermental in the preceding month,
but I didn't expect catastrophic failure.

The other hardware failure was far more upsetting.

From Christmas until August, I ripped most of our CD collection
with `Exact Audio Copy`_ to `FLAC`_ (Free Lossless Audio Codec).
Since FLAC is lossless and open source,
I figured I'd never need to rip the CDs again.
I also wrote a Python script to convert the FLACs to MP3s with LAME_,
since MP3s are far smaller and all players handle MP3s.
I stored the FLACs on a Maxtor OneTouch III drive,
twin 750GB SATA drives configured as NTFS on mirrored `RAID 1`_.

A few minutes changing CDs here and there;
a few more minutes entering album metadata into `Readerware AW`_.
Over the months, it really added up:
775 albums, 250 GB of FLACs, 45GB of MP3s.
The MP3s were replicated on several machines,
but the FLACs and the Readerware AW database were stored
only on the OneTouch's mirrored drives.
This drive became my primary backup solution.
When I had copied the latest data to it,
I'd power it down and store it in the fire safe.

You can guess what's coming next.
The OneTouch stopped working one day.
Refused to do a damn thing on any machine that I connected it to.
I was *very* unhappy.

I was going to return it to Maxtor,
until I read the fine print.
They'd replace it, but they'd send me back different drives
and would make no attempt to get the data off the old drives.

Well, that was completely unacceptable!
I found the `Maxtor OneTouch III disassembly`_ guide online,
but didn't get around to doing anything about it until tonight.
I bought two 3.5" external enclosures at Fry's yesterday.
A couple of hours ago, I voided the warranty by prising the case off,
extracting the drives, and putting them into the enclosures.

They worked! Both of them appear to be fine
and the data is accessible.
Until tonight, I wasn't completely sure that I would be able to
get the data off the disks even if they were okay.
I had visions of having to extract sectors and rebuild the files by hand.

Presumably it's the RAID controller or something else
in the Maxtor case that died.
I'm going to throw that piece of crap away.
One of the drives is undergoing a full chkdsk;
the other will get the same treatment tomorrow.

Not only that, but I also plugged the camera in for the first time
since it had died.
The battery had completely drained and I had to reset the clock.
And now it's decided to work too.
I'm not sure that I trust it,
but should it die again, it's no great loss.

.. _Maxtor OneTouch III disassembly:
    http://www.erowid.org/devel/misc/archives/000083.shtml
.. _Exact Audio Copy:
    http://www.exactaudiocopy.de/
.. _FLAC:
    http://en.wikipedia.org/wiki/Free_Lossless_Audio_Codec
.. _RAID 1:
    http://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1
.. _LAME:
    http://lame.sourceforge.net/
.. _Readerware AW:
    http://www.readerware.com/music/index.html

.. _permalink:
    /blog/2008/11/18/HardwareLazarus.html
