---
title: "Subversive activity"
date: "2006-04-24"
permalink: "/blog/2006/04/24/SubversiveActivity.html"
tags: [subversion]
---



`Vim <http://svn.sourceforge.net/viewcvs.cgi/vim/>`_
and `DasBlog <http://svn.sourceforge.net/viewcvs.cgi/dasblogce/>`_,
two open source projects that I'm associated with,
have both switched over to using the
`Subversion <http://subversion.tigris.org/>`_
source code control system in the last week.
In both cases, the prolonged problems with
`anonymous CVS access at SourceForge
<http://sourceforge.net/docman/display_doc.php?docid=2352&group_id=1>`_
proved the final straw.
And I provided the impetus, by bringing up the need for a change on the
`vim-dev <http://marc.theaimsgroup.com/?l=vim-dev&m=114527322425296&w=2>`_
and `dasblogce-developers
<http://sourceforge.net/mailarchive/forum.php?thread_id=10191521&forum_id=43543>`_
mailing lists.
I take no credit for doing the work, however,
as that was done by others.

(Vim's primary repository continues to be CVS, with Subversion acting as
a mirror for anonymous access. Bram didn't want to change over until
after Vim\-7 ships.)

Earlier this year, we switched over to Subversion at work, after years of
using Visual SourceSafe. It was a *huge* improvement. Having to use VSS was
a big shock to my system, after years of using Source Depot at Microsoft.
Transactional checkins are really nice and I've grown to like
`TortoiseSVN <http://tortoisesvn.tigris.org/>`_ as a front-end to
Subversion.

.. _permalink:
    /blog/2006/04/24/SubversiveActivity.html
