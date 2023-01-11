---
title: "NTFS-3G: the universal filesystem"
date: "2009-04-11"
permalink: "/blog/2009/04/11/NTFS3GTheUniversalFilesystem.html"
tags: [windows, linux, mac]
---



.. image:: https://www.ntfs-3g.org/logo/ntfs-3g-logo.png
    :alt: NTFS-3G
    :target: http://www.ntfs-3g.org/
    :class: right-float

After I started running Linux and then Mac OS X, in addition to Windows, 
I started on a quest to find the universal filesystem.
I had multiboot systems and external drives where I wanted to
to be able to read and write disks under multiple operating systems.

The obvious choice is `FAT32`_,
the ubiquitous, lowest-common denominator filesystem.
FAT32 is supported out-of-the-box by
all major operating systems, digital cameras, and PDAs,
so that's a huge advantage.
FAT32 also has major shortcomings:

* Maximum file size is 4GB. I have ISOs, MPEGs, and other large files exceeding this limit.
* Fragmentation happens too easily.
* Timestamps: accurate only to 2-second resolution. No notion of timezones or UTC.
* Journaling: none. Preferred for robustness.
* ACLs or Permissions. Nothing beyond R/W.

I experimented with `ext3`_ (and its non-journaling sibling, ext2)
on Windows and later on the Mac.
On Windows, `ext2fs`_ works well and I used it happily for several months 
on a machine dualbooting XP and Ubuntu.
It did not work well with Vista initially, though that seems to have been fixed since.

My experiences on the Mac were bad:
`ext2fsx`_ caused some kernel panics,
which was enough for me to abandon it.

There was no free solution for reading and writing Mac HFS+ disks
under Linux and Windows the last time that I checked.

Both Linux and Macs natively support mounting NTFS disks read-only.
The `NTFS-3G`_ project allows Linux to write to NTFS disks,
and `Mac NTFS-3G`_ does likewise for Macs.
I've never had a problem with NTFS-3G and it's worked
flawlessly under Linux and Mac for me.


.. _FAT32:
    http://en.wikipedia.org/wiki/File_Allocation_Table#FAT32
.. _NTFS-3G:
    http://www.ntfs-3g.org/
.. _Mac NTFS-3G:
    http://macntfs-3g.blogspot.com/
.. _ext3:
    http://en.wikipedia.org/wiki/Ext3
.. _ext2fs:
    http://www.fs-driver.org/
.. _ext2fsx:
    http://sourceforge.net/projects/ext2fsx/

.. _permalink:
    /blog/2009/04/11/NTFS3GTheUniversalFilesystem.html
