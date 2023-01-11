---
title: "Gitting Along"
date: "2009-10-15"
permalink: "/blog/2009/10/15/GittingAlong.html"
tags: [git, til]
---



.. image:: /content/binary/gitlogo.png
    :alt: Git logo
    :target: http://git-scm.com/
    :class: right-float

In the last few weeks, I've switched over to `Git`_ for most of my version-control needs,
at home and at work, after putting it on the long finger for months.

We continue to use `Subversion`_ at work,
but I've recently followed Pavel and Eric's lead in using `git-svn`_.
I work locally on my own private branches and
``git svn dcommit`` and ``git svn rebase`` occasionally.
I'm primarily on Windows at work, but I have a Linux box and a Mac Mini too,
while at home, I have a MacBook, a Linux netbook, and a Vista desktop.
I'm using `msysGit`_, occasionally supplemented by `TortoiseGit`_ and `QGit`_.
Pavel's on a Mac and Eric's mostly on Ubuntu, so git adoption was easy for them.

When I first tried git-svn under msysGit about a year ago,
it didn't work worth a damn.
Git-svn works fine now, but it's slow compared to the \*nix implementation.
The developers say that's due to the ``fork()`` emulation
of the MSys/Cygwin layer.
The rest of msysGit is much faster.

For my home needs, I've had private Subversion repositories at
`DevjaVu.com`_ and `OpenSvn.csie.org`_.
DevjaVu has gone out of business and OpenSvn has been unavailable too often for my liking.
It was time to find some new hosting.

I've experimented with private Git repositories at 
`GitHub`_ and `ProjectLocker`_.
GitHub is *very* nice, but charges for private repositories.
ProjectLocker provides free private repositories,
but is comparatively clunky.

ProjectLocker lets you set up a fresh repository on their server.
They tell you how to clone from that, which is great for a new repository.
But they don't tell you how to hook it up to an existing local repository.
Since I had some difficulty in figuring it out, here's the recipe::

    git remote add origin git-foobar@freeN.projectlocker.com:foobar.git
    git pull origin master
    ... merge, local edits and commits ...
    git push origin master

I found `Git, Xcode and ProjectLocker`_ and `Cygwin, SSH and ProjectLocker`_
useful in figuring this out.

.. _Git:
    http://git-scm.com/
.. _Subversion:
    http://subversion.tigris.org/
.. _git-svn:
    http://andy.delcambre.com/2008/03/04/git-svn-workflow.html
.. _msysGit:
    http://code.google.com/p/msysgit/
.. _TortoiseGit:
    http://code.google.com/p/tortoisegit/
.. _QGit:
    http://sourceforge.net/projects/qgit/files/
.. _DevjaVu.com:
    http://devjavu.com
.. _OpenSvn.csie.org:
    http://opensvn.csie.org
.. _GitHub:
    http://www.github.com/
.. _ProjectLocker:
    http://www.projectlocker.com/
.. _Cygwin, SSH and ProjectLocker:
    http://www.cforcoding.com/2009/09/windows-git-tutorial-cygwin-ssh-and.html
.. _Git, Xcode and ProjectLocker:
    http://rudifa.wordpress.com/2009/05/19/git-xcode-and-projectlocker/

.. _permalink:
    /blog/2009/10/15/GittingAlong.html
