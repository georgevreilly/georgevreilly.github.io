---
title: "Git: pruning unused branches"
date: "2017-01-05"
permalink: "/blog/2017/01/05/GitPruningUnusedBranches.html"
tags: [git, til]
---



Ever had a Git repository where there's an overwhelming number of branches,
most of which are surely abandoned?
You run ``git branch --remote`` and you see dozens of unfamiliar branches.
Where to begin?

*   Use `git for-each-ref --sort`__ to sort the branches
    so that you can identify the oldest branches.
*   Use `git branch --remote --merged master`__
    to detect which branches have already been merged into ``master``.
    It's likely that these are branches that weren't deleted
    after a pull request was merged;
    it's usually safe to delete these.
*   ``--no-merged`` shows unmerged branches;
    these require further investigation.

Here's an example for flyingcloud__:

.. code-block:: console

    $ git for-each-ref --sort=-committerdate \
        --format='%(committerdate:short) %(refname)' refs/heads refs/remotes
    2016-12-29 refs/remotes/origin/master
    2016-12-29 refs/remotes/origin/HEAD
    2016-12-29 refs/heads/master
    2016-12-11 refs/remotes/origin/0.1.x
    2016-06-09 refs/remotes/origin/fix/salt-pip-version-problem-in-demo
    2016-05-25 refs/remotes/origin/updates
    2016-05-09 refs/remotes/origin/feature/documentation-improvements-3
    2016-04-19 refs/remotes/origin/feature/developer-setup-example
    2016-04-17 refs/remotes/origin/feature/travis-build
    2016-03-16 refs/remotes/origin/feature/documentation-improvements-2
    2016-03-06 refs/remotes/origin/feature/documentation-improvements-1
    2016-03-06 refs/remotes/origin/feature/documentation-and-examples
    2016-02-26 refs/remotes/origin/rtfd
    2016-02-21 refs/remotes/origin/feature/metakube
    2016-01-17 refs/remotes/origin/walk_tree

    $ git branch --remote --merged master
      origin/HEAD -> origin/master
      origin/feature/documentation-improvements-1
      origin/feature/documentation-improvements-2
      origin/feature/travis-build
      origin/fix/salt-pip-version-problem-in-demo
      origin/master
      origin/rtfd
      origin/updates

__ http://stackoverflow.com/a/11144311/6364
__ http://stackoverflow.com/a/227026/6364
__ https://github.com/cookbrite/flyingcloud

.. _permalink:
    /blog/2017/01/05/GitPruningUnusedBranches.html
