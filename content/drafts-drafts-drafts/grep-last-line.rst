---
title: "Grep Last Line"
# date: "2023-mm-dd"
permalink: "/__drafts/2023/mm/dd/GrepLastLine.html"
tags: [programming, bash]
draft: true
---

.. vim:set ft=rst spell:

.. title:: Grep Last Line

I needed to find all the files whose *last* line matched ``PATTERN``,
then feed them into Vim:

.. code-block:: bash

    find . -name "*.txt" -o -name "*.rst" | while read f; do
        printf "$f:$(tail -1 $f)\n";
    done | grep PATTERN | sed 's/:.*$//' | xargs -o vim

* Find ``*.txt`` and ``*.rst``
* Loop over those filenames
* Compute *filename* + ``:`` + the last line of that filename: ``$(tail -1 $f)``
* Grep the pattern
* Strip off the pattern to yield those filenames which have the pattern.
* Note: This is *decorate-sort-undecorate*, aka the `Schwartzian transform`__.
  (Well, *grep*, not *sort*.)
* Feed the filenames into Vim.
  The ``-o`` argument to ``xargs`` prevents Vim from messing up the terminal when it exits.

Also, find missing symlink targets:

.. code-block:: bash

    ls -l ./public3 | grep ^l | awk '{print $11}' | \
        while read f; do ls -l ./public3/$f; done | grep "No such"

__ https://en.wikipedia.org/wiki/Schwartzian_transform
