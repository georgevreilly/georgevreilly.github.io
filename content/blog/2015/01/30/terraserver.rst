---
title: "The TerraServer"
date: "2015-01-30"
permalink: "/blog/2015/01/30/TerraServer.html"
tags: [microsoft, history]
---



.. image:: /content/binary/unloading_ESA10000_from_pallet.png
    :alt: Unloading ESA 10000 Storage Subsystem Cabinet
    :target: http://manx.classiccmp.org/collections/mds-199909/cd3/storage/smcppuga.pdf
    :class: right-float
    :width: 400

I bought a 2TB external hard disk today.
It's about the size of a deck of cards, but thinner,
and it cost me $95.
Disk Utility says it has 2,000,397,884,928 bytes.

In 1998, I got to see more than three terabytes of disks in one system.
At the time, a server with a 25GB disk was considered high capacity.
The 3TB system occupied considerably more volume than a pack of cards.
I don't know what it cost
but clearly it was tens if not hundreds of thousands of dollars.

At that time, I was a developer on the IIS_ team at Microsoft.
I was the lead performance engineer for Microsoft's web server product.
The TerraServer_ was a project born in Microsoft Research
intended to demonstrate that SQL Server could scale up to terabyte-sized workloads.
It stored aerial, satellite, and topographic images of the Earth
in a SQL database available via the Internet,
and it was the world’s largest online atlas.

They launched the TerraServer on the Internet.
And the Internet liked the TerraServer.
And the TerraServer fell over.
So I got called in.

It was June and I was wearing shorts and Birkenstock sandals with no socks.
The TerraServer was housed in one of Microsoft's data centers
and there was cold air blowing up through the floor,
and quite soon I was wishing that I had worn socks that day.

The TerraServer was the biggest microcomputer-based system I had ever seen.
Quoting the `TerraServer Tech Report`_:

    The web site has eight Windows NT servers — 6 web servers and 2 database servers.
    The USGS aerial imagery is maintained on a Compaq AlphaServer™ 8400
    containing 8 440 Mhz Alpha processors and 10 GB of RAM.
    The processor is attached to 7 StorageWorks™
    Enterprise Storage Array 10000 (ESA-10000) cabinets.
    The disk arrays are based on UltraSCSI technology.

    Each ESA-10000 contains 48 9 GB disk drives and
    2 HSZ70 dual-redundant RAID-5 controllers.
    4 sets of 11 disks each are configured into
    a single RAID-5 stripe-set
    and managed as a single logical disk by the HSZ70 controller.
    2 drives per cabinet are available as hot spares.
    Should a disk fail, the HSZ70 controllers automatically
    swap a spare drive into a RAID set.

    Windows NT Server sees each large (85 GB each) disk
    created by the RAID controllers of each of the seven disk cabinets.
    It stripes these into 4 large (595 GB) volumes
    which are then each formatted and managed
    by the Windows NT file system (NTFS).
    Each 595 GB volume contains about thirty 20GB files.
    SQL Server stores its databases in these large files.
    We chose this 20GB file size since it fits conveniently
    on one DLT magnetic tape cartridge.

    Connected to the AlphaServer 8400 is a StorageTek 9710 automated tape robot. 
    The tape robot contains 10 Quantum DLT7000 tape drives.
    Legato Networker backup software can backup
    the entire 1.5 TB TerraServer SQL database to the StorageTek tape robot
    in 7 hours and 15 minutes — or 17 GB/hour.

    ...

    Database back-end: 1 8-way 440Mhz Compaq AlphaServer 8400,
    10GB ram, 3.2 TB raid5 324 9GB Ultra SCSI disks

So, 7 cabinets_ (pictured above)
measuring 2' wide by 3' deep and 5' tall, housing 324 9GB disks.
And another cabinet for the servers.
And one for the tape robot.
The whole thing must have been about 20 feet wide.

By comparison, the 15" mid-2012 MacBook Pro laptop that I'm writing this on
has 16GB RAM, 2.3 GHz Intel Core i7 (4 hyperthreaded cores),
750GB internal disk (HDD), and the aforementioned 2TB external disk.
I've been backing up to that external disk
and I've been hitting 90MB/s transfer rates.
`Moore's Law`_ marches on.

At this point, I can't recall what I actually did to help them out,
but between me and other people,
they got it working satisfactorily within a few days.


.. _IIS:
    http://en.wikipedia.org/wiki/Internet_Information_Services
.. _TerraServer:
    http://en.wikipedia.org/wiki/Terraserver.com
.. _TerraServer Tech Report:
    http://research.microsoft.com/pubs/68574/msr_tr_99_29_terraserver.pdf
.. _ESA 10000 manual:
.. _cabinets:
    http://manx.classiccmp.org/collections/mds-199909/cd3/storage/smcppuga.pdf
.. _Moore's Law:
    http://en.wikipedia.org/wiki/Moore%27s_law

.. _permalink:
    /blog/2015/01/30/TerraServer.html
