---
title: "De-partitioning a Mac disk"
date: "2009-04-12"
permalink: "/blog/2009/04/12/DepartitioningAMacDisk.html"
tags: [mac]
---



.. image:: /content/binary/diskutil2.png
    :alt: Disk Utility after de-partitioning
    :class: right-float

I wrote yesterday about `NTFS-3G`_ because I was backing my MacBook
to an external NTFS drive.
I was backing up because I wanted to de-partition my Mac.

When I `upgraded my MacBook`_ to a bigger drive, more RAM, and OS X 10.5,
I partitioned the drive.
I created two 25GB partitions with the intention of
putting Windows and Linux on them with BootCamp.
It turns out that BootCamp doesn't like that.
It wants the system drive to have only one partition,
which it would shrink.
I never bothered to go any further.

The disk has been filling up recently and I wanted the extra space back,
to extend my primary HFS+ partition by 50GB.
I found a guide to `nondestructively resizing volumes`_
with the command-line ``diskutil`` tool.

With some trepidation, I set out to reclaim the end of my drive.
Happily, it turned out to be both quick and painless.

Here's the old disk layout::

    georger@georger-macbook:~$ diskutil list
    /dev/disk0
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      GUID_partition_scheme                        *298.1 Gi   disk0
       1:                        EFI                         200.0 Mi   disk0s1
       2:                  Apple_HFS GeorgeR Mac             250.0 Gi   disk0s2
       3:       Microsoft Basic Data WINDOWS                 25.0 Gi    disk0s3
       4:       Microsoft Basic Data LINUX                   22.8 Gi    disk0s4

First, I merged the two FAT32 partitions into one HFS+ partition::

    georger@georger-macbook:~$ sudo diskutil mergePartitions \
        "Journaled HFS+" End disk0s3 disk0s4
    The chosen disk does not support resizing, do you wish to format instead? (y/N) y
    Merging partitions into a new partition
         Start partition: disk0s3 WINDOWS
         Finish partition: disk0s4 LINUX
    Started erase after partitioning on disk disk0s3
    Erasing
    Mounting disk
    [ + 0%..10%..20%..30%..40%..50%..60%..70%..80%..90%..100% ] 
    Finished erase after partitioning on disk disk0s3 End
    /dev/disk0
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      GUID_partition_scheme                        *298.1 Gi   disk0
       1:                        EFI                         200.0 Mi   disk0s1
       2:                  Apple_HFS GeorgeR Mac             250.0 Gi   disk0s2
       3:                  Apple_HFS End                     47.6 Gi    disk0s3

Then, I merged the two HFS+ partitions::

    georger@georger-macbook:~$ sudo diskutil mergePartitions \
        "Journaled HFS+" End disk0s2 disk0s3
    Merging partitions into a new partition
         Start partition: disk0s2 GeorgeR Mac
         Finish partition: disk0s3 End
    Attempting resize
    Changing filesystem size on disk 'disk0s2'...
    Attempting to change filesystem size from 268435456000 to 319728959488 bytes
    /dev/disk0
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      GUID_partition_scheme                        *298.1 Gi   disk0
       1:                        EFI                         200.0 Mi   disk0s1
       2:                  Apple_HFS GeorgeR Mac             297.8 Gi   disk0s2

And everything is good::

    georger@georger-macbook:~$ df
    Filesystem    512-blocks      Used     Avail Capacity  Mounted on
    /dev/disk0s2   624470624 508168048 115790576    81%    /

Disclaimer: back your disk up and
read the ``diskutil`` man page very carefully before using:
one misstep could ruin the contents of your disk.

.. _NTFS-3G:
    /blog/2009/04/11/NTFS3GTheUniversalFilesystem.html
.. _upgraded my MacBook:
    /blog/2008/07/16/MacBookMakeover.html
.. _nondestructively resizing volumes:
    http://www.macgeekery.com/tips/cli/nondestructively_resizing_volumes

.. _permalink:
    /blog/2009/04/12/DepartitioningAMacDisk.html
