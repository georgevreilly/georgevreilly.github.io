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

.. _Wordle:
    https://en.wikipedia.org/wiki/Wordle

|   *Wordle 775 5/6*
|
|   🟨 ⬛ ⬛ ⬛ 🟩
|   ⬛ 🟨 🟨 ⬛ 🟩
|   ⬛ ⬛ 🟨 🟨 🟩
|   ⬛ 🟩 🟩 ⬛ 🟩
|   🟩 🟩 🟩 🟩 🟩


The problem that I want to address in this post is:

    Given some ``GUESS=SCORE`` pairs for Wordle and a word list,
    find all the words from the list that are candidate answers.

Let's look at this five-round game for Wordle 775:

.. RISKY=r...Y CRAZY=.ra.Y WEARY=..arY MARRY=.AR.Y PARTY=PARTY

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
  ``Y`` is the final letter of the answer.
* A Yellow letter 🟨 means that the letter is *present* elsewhere in the answer.
  There is an ``R`` in the answer;
  it's not at positions 1, 2, or 4, but it is correct at position 3.
  Likewise, an ``A`` is present in the answer;
  it's not at position 3, but it's correct at position 2.
  (The ``A`` should not have been played twice at position 3.)
* A Black letter ⬛ is *absent* from the answer:
  there is no ``I``, ``S``, ``K``, ``C``, ``Z``, ``W``, ``E``, or ``M``
  anywhere in ``PARTY``.

Other words that could satisfy
``RISKY=r...Y CRAZY=.ra.Y WEARY=..arY MARRY=.AR.Y``
include but are not limited to
``HARDY``, ``HARPY``, ``TARDY``, and ``TARTY``.

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
3. match all correct positions —        ``2:A``, ``3:R``, and ``5:Y``
4. not match any ‘present’ positions —  ``1:R``, ``2:R``, ``3:A``, or ``4:R``

These constraints narrow the possible choices from the word list.


Prototyping with Pipes
----------------------

Let's prototype the above with a series of ``grep``\ s
in a Unix pipeline tailored to this example:

.. code-block:: bash

    grep '^.....$' /usr/share/dict/words    `# Five-letter words`       \
        | tr '[a-z]' '[A-Z]'                `# Translate to uppercase`  \
        | grep '.AR.Y'                      `# Match CORRECT positions` \
        | grep 'A' | grep 'R' | grep 'Y'    `# Match VALID set`         \
        | grep -v '[ISKCZWEM]'              `# Exclude INVALID set`     \
        | grep '[^R][^R][^A][^R][A-Z]'      `# Exclude PRESENT chars`   \
        | rs                                `# BSD reshape lines to columns`

gives (on macOS 13.4)::

    BARDY  DARBY  HARDY  LARDY  PARTY  VARDY  YARLY
    BARNY  GARDY  HARPY  PARLY  TARDY  YARAY

I used ``rs`` to make the output more compact, but it can be omitted.
I got some annoying ``command not found`` warnings from Zsh
about the back-ticked comments.
On Ubuntu, I had to install the
`rs`_ and `wamerican`_ (for ``/usr/share/dict/words``) packages first.

.. _rs:
    https://packages.ubuntu.com/focal/rs
.. _wamerican:
    https://packages.ubuntu.com/focal/wamerican

This is promising, but not maintainable.

.. Sticking the stylesheet at the end out of the way
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
