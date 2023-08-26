---
title: "Wordle Finder"
# date: "2023-mm-dd"
# permalink: "/__drafts/2023/mm/dd/TheSlugGoesHere.html"
permalink: "/__drafts/WordleFinder.html"
tags: [python]
draft: true
---

Unless YOUVE LIVED UNDER ROCKS, you've heard of Wordle_,
the wildly popular web-based word game.


::

    (Use a colored diagram. This example is Wordle 775)

    RISKY=r...Y
    CRAZY=.ra.Y
    WEARY=..arY
    MARRY=.AR.Y
    PARTY=PARTY

The letters of each guess will be colored Green, Yellow, or Black (dark-gray).

* A Green letter 🟩 means that the letter is correct:
  the final letter is ``Y``.
* A Yellow letter 🟨 means that the letter is present elsewhere in the word:
  there is an ``R`` in the word; it's not at positions 1, 2, or 4 but at position 3.
* A Black letter ⬛ is not in the answer at all:
  there is no ``I``, ``S``, ``K``, ``C``, ``Z``, ``W``, ``E``, or ``M``
  anywhere in ``PARTY``.

The problem that I want to address in this post is:

    Given a set of ``GUESS=SCORE`` pairs and a word list,
    find all the words from the list that are candidate answers.

Other words that could satisfy
``RISKY=r...Y CRAZY=.ra.Y WEARY=..arY MARRY=.AR.Y`` include
``HARDY HARPY TARDY TARTY``.

The ``GUESS=SCORE`` notation is intended to be clear
and easier to write than Greens and Yellows.
Example: For ``CRAZY=.ra.Y``:

* the ``Y`` is in the correct position (i.e., green 🟩),
* the ``r`` and ``a`` are in the wrong positions (yellow 🟨),
* and there is no ``C`` or ``Z`` in the answer (black ⬛ / white ⬜).

.. _Wordle:
    https://en.wikipedia.org/wiki/Wordle
