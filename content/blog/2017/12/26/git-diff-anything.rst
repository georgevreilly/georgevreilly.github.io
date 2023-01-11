---
title: "Git Diff Tips"
date: "2017-12-26"
permalink: "/blog/2017/12/26/GitDiffTips.html"
tags: [git, til]
---



The `Git Diff`_ utility is much more functional than the standard command-line ``diff``.

To see changes relative to the staging area (aka the index),
use ``git diff``.

To see *staged* changes, use ``git diff --staged`` (or ``--cached``).

To see changes side by side on a line (where it makes sense),
use the ``--color-word`` option.

To compare two arbitrary files in the file system,
use ``git diff --no-index``.

To try some other `diff algorithms`_,
use the ``--patience``, ``--histogram``, or ``--minimal`` options. 
The default diff algorithm is ``--myers``.

Lots more at the docs_.


.. _Git Diff:
.. _docs:
    https://git-scm.com/docs/git-diff
.. _diff algorithms:
    https://stackoverflow.com/questions/4045017/what-is-git-diff-patience-for

.. _permalink:
    /blog/2017/12/26/GitDiffTips.html
