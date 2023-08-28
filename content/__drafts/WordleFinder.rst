---
title: "Wordle Finder"
# date: "2023-mm-dd"
# permalink: "/__drafts/2023/mm/dd/TheSlugGoesHere.html"
permalink: "/__drafts/WordleFinder.html"
tags: [python]
draft: true
---

Unless YOUVE LIVED UNDER ROCKS, you've heard of Wordle_,
the online word game that has become wildly popular since late 2021.
You've almost certainly seen people posting their Wordle games
as little green, yellow, and black (or white) emojis.

**show emojis**

.. _Wordle:
    https://en.wikipedia.org/wiki/Wordle

Take this five-round game:

.. ./render_game.py RISKY=r...Y CRAZY=.ra.Y WEARY=..arY MARRY=.AR.Y PARTY=PARTY

.. raw:: html

    <table class='wordle'>
      <tr><td class="present">R</td> <td class="absent" >I</td> <td class="absent" >S</td> <td class="absent" >K</td> <td class="correct">Y</td></tr>
      <tr><td class="absent" >C</td> <td class="present">R</td> <td class="present">A</td> <td class="absent" >Z</td> <td class="correct">Y</td></tr>
      <tr><td class="absent" >W</td> <td class="absent" >E</td> <td class="present">A</td> <td class="present">R</td> <td class="correct">Y</td></tr>
      <tr><td class="absent" >M</td> <td class="correct">A</td> <td class="correct">R</td> <td class="absent" >R</td> <td class="correct">Y</td></tr>
      <tr><td class="correct">P</td> <td class="correct">A</td> <td class="correct">R</td> <td class="correct">T</td> <td class="correct">Y</td></tr>
    </table>

The letters of each guess are colored Green, Yellow, or Black (dark-gray).

* A Green letter 🟩 means that the letter is *correct*:
  the final letter of the answer is ``Y``.
* A Yellow letter 🟨 means that the letter is *present* elsewhere in the answer.
  There is an ``R`` in the answer;
  it's not at positions 1, 2, or 4, but it is at position 3.
  Likewise, an ``A`` is present in the answer,
  not at position 3, but at position 2.
* A Black letter ⬛ is *absent* from the answer:
  there is no ``I``, ``S``, ``K``, ``C``, ``Z``, ``W``, ``E``, or ``M``
  anywhere in ``PARTY``.

The problem that I want to address in this post is:

    Given a set of ``GUESS=SCORE`` pairs and a word list,
    find all the words from the list that are candidate answers.

Other words that could satisfy
``RISKY=r...Y CRAZY=.ra.Y WEARY=..arY MARRY=.AR.Y``
include but are not limited to
``HARDY HARPY TARDY TARTY``.

The ``GUESS=SCORE`` notation is intended to be clear to read
and easier to write than Greens and Yellows.

For example, ``CRAZY=.ra.Y``:

.. raw:: html

    <table class='wordle'>
      <tr><td class="absent" >C</td> <td class="present">R</td> <td class="present">A</td> <td class="absent" >Z</td> <td class="correct">Y</td></tr>
    </table>

* the ``Y`` is in the correct position (i.e., green 🟩),
* the ``r`` and ``a`` are present somewhere in the answer,
  but they are in the wrong positions (yellow 🟨),
* and ``C`` and ``Z`` are absent from the answer (black ⬛).


Deductions
----------

What can we deduce from the first four rows of guesses,
``RISKY=r...Y CRAZY=.ra.Y WEARY=..arY MARRY=.AR.Y``?

There is a set of *valid* letters,
``Y``, ``A``, and ``R``,
that are either *present* (yellow 🟨) or *correct* (green 🟩):
The ``Y`` is correct from the first time it appears.
The ``A`` and ``R`` are initially present,
but later find their correct position.

There is a set of *invalid* letters that are
known to be *absent* from the answer (black ⬛):
``I``, ``S``, ``K``, ``C``, ``Z``, ``W``, ``E``, and ``M``.

The remaining letters of the alphabet are currently *unknown*.
When they are played, they will turn into *valid* or *invalid* letters.
Unless we already have five correct letters,
we will draw candidate letters from the unknown pool.

Furthermore, we know something about *letter positions*.
The *correct* letters are in the correct positions,
while the *present* letters are in the wrong positions.

A candidate word *must*:

1. include all valid letters —          ``Y``, ``A``, and ``R``
2. exclude all invalid letters —        ``I``, ``S``, ``K``, ``C``, ``Z``, ``W``, ``E``, and ``M``
3. match all correct positions —        ``A=2``, ``R=3``, and ``Y=5``
4. not match any ‘present’ positions —  ``R=1``, ``R=2``, ``R=4``, or ``A=3``

These constraints narrow the possible choices from the word list.

.. raw:: html

    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@700&display=swap');
    table.wordle {
        font-family: 'Libre Franklin', 'Clear Sans', 'Helvetica Neue', Arial, sans-serif;
        font-size: 32px;
        font-weight: bold;
        border-spacing: 6px;
        margin-left: auto;
        margin-right: auto;
    }
    table tr td {
        color: white;
        background-color: white;
        height: 62px;
        width: 62px;
        text-align: center;
    }
    table tr td.correct {
        background-color: #6aaa64;
    }
    table tr td.present {
        background-color: #c9b458;
    }
    table tr td.absent {
        background-color: #838184;
    }
    </style>
