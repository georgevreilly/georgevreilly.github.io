---
title: "Distributed Version Control Systems on Windows"
date: "2008-11-10"
permalink: "/blog/2008/11/10/DistributedVersionControlSystemsOnWindows.html"
tags: [git, windows]
---



.. image:: https://www.infoq.com/resource/articles/dvcs-guide/en/resources/CVCSvsDVCS.png
    :target: http://www.infoq.com/articles/dvcs-guide
    :alt: Distributed/Decentralized Version Control Systems

At work, I've been experimenting with the big three
Distributed Version Control Systems,
Git_, Mercurial_, and Bazaar_,
on Windows over the last ten days.

Pavel and Eric have been singing the praises of Git and
`git-svn`_ on their Mac and Linux boxes respectively
for the last few months.
Git allows them to check in small changes locally without perturbing the build.
The ease of branching and merging allows them to work in more than one branch
at a time at a lower cost than Subversion did.
Most of our dev team continue to work in Subversion on Windows boxes.
git-svn allows Pavel and Eric to easily interoperate with the Subversion server.
Pavel is also a big fan of `git-stash`_:
he stacks away in-progress work and switches easily to other patches.

Although I've worked primarily in Python on Linux since the summer,
I've been working on our forthcoming mobile client recently.
It's ASP.NET-based, hence I'm working on Windows again.
I'm in the throes of a major refactoring, extracting the mobile client
out of the main webclient and hoisting other code into shared projects,
while other developers continue to work on the main webclient
and the mobile client.

This seemed like a perfect opportunity to bite the `DVCS bullet`_,
since I knew that branching and merging would be less painful
with git-svn than with Subversion.

Getting git-svn working on Windows turned out to be a major headache.
The Cygwin version of git-svn simply `doesn't work`_ for me.
And msysGit doesn't `currently support`_ git-svn.
(Eric has had some success with an older version of msysGit and git-svn,
but I found it to be wretchedly slow.)
Moreover, Git's integration with Windows is poor.
There's nothing like TortoiseSVN_ to ease developers into using Git.

Having written off Git on Windows for now,
it was time to try Bazaar_ (``bzr``),
which has its own Subversion plugin, `bzr-svn`_.
The version of bzr-svn that was available for Windows the week before last 
was ancient, and `promptly crashed`_.
Jelmer, the developer, mailed me yesterday to say that there should be an 
up-to-date copy of bzr-svn in the brand new 1.9 release of Bazaar.
I'll try it at work tomorrow.
Windows doesn't seem like an afterthought for Bazaar;
indeed, TortoiseBzr_ offers Explorer integration.

On to Mercurial_ (``hg``).
Alas, this has the weakest integration with Subversion.
There are `instructions`_ for doing it by hand (which is what I'm doing).
The hgsubversion_ extension looks promising, but is still immature.

Even so, Mercurial is what I've ended up using for the last week.
Partly because it didn't bite me.
Partly because I like it best of the three.
The `Mercurial book`_ takes much of the credit for that.
Windows is a first-class client
and TortoiseHg_ offers half-way decent Explorer integration.

I'm not impressed with Git as software engineering;
it strikes me as an incoherent mess of C and Perl.
The attitude of superiority from some Git proponents is off-putting.
I watched `Linus Torvalds' Google techtalk`_ about Git on Friday;
he came across as a major jerk,
repeatedly calling anyone who uses Subversion an idiot.
I'd still recommend watching the video:
it gives good insight into the social aspects of
distributed/decentralized VCSes,
how very different they are from traditional centralized VCSes,
and how they afford a different way of working.

Watching my compatriot `Bryan O'Sullivan's Google techtalk`_ on Mercurial
this afternoon was a far more pleasant experience.
He talks more about workflow and implementation.

Both Bazaar and Mercurial are written in Python and
seem to be fairly well architected.
Frankly, if I do have to get my hands dirty in the code
(e.g., hgsubversion), I'd much rather hack in Python.
I did C/C++ for fifteen years and I'm sick of unmanaged code.

Anyway, Mercurial is where I'm going for now,
though I won't categorically rule out Bazaar or Git.

.. _Git: http://git.or.cz/
.. _Mercurial: http://www.selenic.com/mercurial/wiki/
.. _Bazaar: http://bazaar-vcs.org/
.. _git-svn: http://www.kernel.org/pub/software/scm/git/docs/git-svn.html
.. _Subversion: http://subversion.tigris.org/
.. _git-stash: http://www.kernel.org/pub/software/scm/git/docs/git-stash.html
.. _DVCS bullet: http://www.infoq.com/articles/dvcs-guide
.. _doesn't work: http://cygwin.com/ml/cygwin/2008-10/msg00602.html
.. _currently support: http://code.google.com/p/msysgit/issues/detail?id=160
.. _TortoiseSVN: http://tortoisesvn.net/
.. _bzr-svn: https://launchpad.net/bzr-svn
.. _TortoiseBzr: http://bazaar-vcs.org/TortoiseBzr
.. _promptly crashed: https://bugs.launchpad.net/bzr-svn/+bug/291361
.. _instructions:
    http://www.momentaryfascinations.com/programming/how.to.use.mercurial.for.local.source.code.management.with.a.public.subversion.server.html
.. _hgsubversion: http://blog.red-bean.com/sussman/?p=116
.. _Mercurial book: http://hgbook.red-bean.com/
.. _TortoiseHg: http://tortoisehg.wiki.sourceforge.net/
.. _Linus Torvalds' Google techtalk: http://www.youtube.com/watch?v=4XpnKHJAok8
.. _Bryan O'Sullivan's Google techtalk: http://video.google.com/videoplay?docid=-7724296011317502612

.. _permalink:
    /blog/2008/11/10/DistributedVersionControlSystemsOnWindows.html
