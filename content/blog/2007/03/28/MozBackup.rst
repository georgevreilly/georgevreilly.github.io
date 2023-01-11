---
title: "MozBackup"
date: "2007-03-28"
permalink: "/blog/2007/03/28/MozBackup.html"
tags: [tech]
---



.. image:: https://mozbackup.jasnapaka.com/images/eng/02.png
    :alt: MozBackup
    :target: http://mozbackup.jasnapaka.com/

Scott Hanselman wrote today about `family backup plans`_
and alerted me to `MozBackup`_.
MozBackup can backup all of your crucial Firefox and
Thunderbird files to a single, consolidated PCV file,
saving you the hassle of figuring out where all the
crucial files live on your hard disk.

You still have to back that PCV file up to a CD or an external drive,
but now you have one file to back up instead of several dozen,
scattered across several different, deeply hidden directory trees
with non-obvious names.

Speaking of `backup plans`_, I need a better one for myself.
I regularly do a manual backup of my crucial data
to a rotating set of thumbdrives
and move them by hand between my different computers.
I'm not doing a good job of backing up my photos,
only sporadically backing them up by hand to external USB drives.

I really need:

* a centralized server at home, so that all the other computers can do a 
  network backup to it;
* *automated backup* on a regular basis;
* to take some of those backups offline — or better still, offsite;
* a private Subversion_ server on the Internet, so I can keep most of my 
  crucial files under version control, obviating the need to move them
  by hand from computer to computer.

.. _MozBackup:
    http://mozbackup.jasnapaka.com/
.. _family backup plans: backup plans_
.. _backup plans:
    http://www.hanselman.com/blog/OnLosingDataAndAFamilyBackupStrategy.aspx
.. _Subversion:
    http://subversion.tigris.org/

.. _permalink:
    /blog/2007/03/28/MozBackup.html
