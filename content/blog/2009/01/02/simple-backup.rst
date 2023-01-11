---
title: "Over-Engineering Backup"
date: "2009-01-02"
permalink: "/blog/2009/01/02/OverEngineeringBackup.html"
tags: [tech]
---



.. image:: https://www.thegadgetblog.com/wp-content/uploads/2008/02/wdfmypassport_essential320gb.jpg
    :alt: WD Passport
    :width: 200
    :class: right-float

When my parents visited me in September,
I bought them a second laptop and an external drive for backup.
One laptop stays in Dublin,
the other in Cape Town where they spend much of their year.
Both laptops are in Dublin with me at present,
so that I can clean them up and get them in sync.
(I had to remove some very obscure registry settings to
get one DVD drive working again. <sigh/>)

Their backup needs are simple.
Both of them have web-based email at Yahoo!.
The only personal data on either computer is photos.
Inevitably the photos are out of sync between the two machines.

The WD Passport drive came with WDSync,
which syncs specified data, encrypted with AES, between the computer and the drive.
Different computers can have different profiles on the drive.
If data is removed from the computer, WDSync will remove it from the drive.

I felt that this was overkill for my parents
and I didn't like that the photos were not readily visible on the drive.

So I just wrote a simple batch file that treecopies the photos folder
from the laptop to the external drive, and vice versa.
They just need to run the batch file periodically,
to back up new photos, and bring the drive with them
when they travel to and from Cape Town,
so that the other laptop can be updated.

.. _permalink:
    /blog/2009/01/02/OverEngineeringBackup.html
