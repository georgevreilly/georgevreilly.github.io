---
title: "Find remote Git branch with change to a file"
date: "2016-04-03"
permalink: "/blog/2016/04/03/FindRemoteGitBranchWithChangeToAFile.html"
tags: [git, til]
---



I needed to track down a remote branch created a couple of months ago
on another machine.
I knew which file had been changed,
but none of the far-too-many remote branches' names rang a bell.

Turns out that using `git branch --contains`_ in the right way
finds all the relevant branches.

.. code:: bash

    git log --all --format=%H FILENAME \
        | while read f; do git branch --remotes --contains $f; done \
        | sort -u

The first line, ``git log --all --format=%H FILENAME``,
lists all the *hashes* for commits that contained changes to ``FILENAME``.
The second finds all the branches that contain those hashes
(I added ``--remotes``).
The third uniquifies the results.

The `original answer`_ goes on to suggest using
``gitk --all --date-order -- FILENAME``
to manually inspect all branches.
However, gitk complains ``unknown color name "lime"`` on my new Mac.
I must have hit this before, on an earlier installation of Git,
because the `StackOverflow answer`_ contains an edit from me.

.. _git branch --contains:
.. _original answer:
    http://stackoverflow.com/questions/6258440/find-a-git-branch-containing-changes-to-a-given-file
.. _StackOverflow answer:
    http://stackoverflow.com/questions/34637896/gitk-will-not-start-on-mac-unknown-color-name-lime

.. _permalink:
    /blog/2016/04/03/FindRemoteGitBranchWithChangeToAFile.html
