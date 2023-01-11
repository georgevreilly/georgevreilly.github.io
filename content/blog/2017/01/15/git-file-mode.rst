---
title: "Git File Modes"
date: "2017-01-15"
permalink: "/blog/2017/01/15/GitFileModes.html"
tags: [git, til]
---



Ever wonder what the six-digit file modes are in a Git commit?
The mysterious ``100644`` and ``100755`` modes?

.. code-block:: diff

    diff --git a/foo/bar.py b/foo/bar.py
    old mode 100644
    new mode 100755
    index b829edea4..ee6bda024
    --- a/foo/bar.py
    +++ b/foo/bar.py
    @@ -1,3 +1,4 @@
    ...

I had made ``foo/bar.py`` executable by using ``chmod +x``
and adding a ``#!/usr/bin/env python`` shebang.
The last three digits are obviously the same octal__ digits that you can use with ``chmod``.
But what's that ``100`` prefix?

The explanation can be found in a `StackOverflow answer`__::

    100644₈  regular file (non-executable)  S_IFREG | S_IRUSR | S_IWUSR
                                                    | S_IRGRP | S_IWGRP
                                                    | S_IROTH | S_IWOTH
    100755₈  regular file (executable)      S_IFREG | S_IRUSR | S_IWUSR | S_IXUSR
                                                    | S_IRGRP | S_IWGRP | S_IXGRP
                                                    | S_IROTH | S_IWOTH | S_IXOTH
    120000₈  symbolic link                  S_IFLNK
    160000₈  gitlink                        No stat(2) equivalent
    040000₈  directory                      S_IFDIR

A gitlink__ is used to refer to a commit in another repository;
it's how submodules are implemented.

__ http://weblogs.asp.net/george_v_reilly/archive/2004/12/13/284388.aspx
__ http://stackoverflow.com/a/8347325/6364
__ https://www.kernel.org/pub/software/scm/git/docs/git-fast-import.html#_tt_filemodify_tt

.. _permalink:
    /blog/2017/01/15/GitFileModes.html
