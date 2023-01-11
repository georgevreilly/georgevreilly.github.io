---
title: "git commit --verbose"
date: "2016-08-03"
permalink: "/blog/2016/08/03/GitCommitVerbose.html"
tags: [git, til]
---



I learned today about the ``-v`` (``--verbose``) flag to ``git commit`` (git-commit__),
which causes a unified diff of what would be committed
to be appended to the end of the commit message.
This diff is not part of the commit.
Set the ``commit.verbose`` configuration variable (new in Git 2.9)
to adjust the default behavior.

I also learned about using ``git show`` (git-show__)
to display the diff for the most recent commit.
I had been using ``git log -1 --patch`` (git-log__).
More on `git log -p vs. git show vs. git diff`__.

__ https://git-scm.com/docs/git-commit
__ https://git-scm.com/docs/git-show
__ https://git-scm.com/docs/git-log
__ http://stackoverflow.com/questions/25608809/git-log-p-vs-git-show-vs-git-diff

.. _permalink:
    /blog/2016/08/03/GitCommitVerbose.html
