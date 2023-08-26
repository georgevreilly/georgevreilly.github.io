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

    (Use a colored diagram. This example is Wordle 776)

    PRANG=.rA..
    BLARE=..AR.
    CHART=CHART

The letters of each guess will be colored Green, Yellow, or Black (dark-gray).

* A Green letter 🟩 means that the letter is correct:
  the third letter is ``A``.
* A Yellow letter 🟨 means that the letter is present elsewhere in the word:
  there is an ``R`` in the word; it's not at positions 2 but at position 4.
* A Black letter ⬛ is not in the answer at all:
  there is no ``P``, ``N``, ``G``, ``B``, ``L`` or ``E``  anywhere in ``CHART``.

The problem that I want to address in this post is:

    Given a set of ``GUESS=SCORE`` pairs and a word list,
    find all the words that are candidate answers.

A *partial* list of words that could satisfy ``PRANG=.rA..  BLARE=..AR.`` includes
``AWARD CHARD CHARM CHARY DIARY DWARF HOARD OVARY QUARK QUART
SCARF SHARK SMARM STARK START SWARM TIARA WHARF``.
It's clear that ``CHART`` was a lucky guess here.

The ``GUESS=SCORE`` notation is intended to be clear
and easier to write than Greens and Yellows.
Example: For ``TRACK=.RAc.``:

* the ``R`` and ``A`` are in the correct positions (i.e., green 🟩),
* the ``c`` is in the wrong position (yellow 🟨),
* and there is no ``T`` or ``K`` (gray ⬛/⬜).

.. _Wordle:
    https://en.wikipedia.org/wiki/Wordle
