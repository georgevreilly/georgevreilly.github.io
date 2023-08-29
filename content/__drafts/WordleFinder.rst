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

|   Wordle 797 4/6
|
|   ⬛ ⬛ ⬛ ⬛ 🟨
|   🟨 ⬛ 🟩 ⬛ ⬛
|   ⬛ ⬛ 🟩 🟨 ⬛
|   🟩 🟩 🟩 🟩 🟩


The problem that I want to address in this post is:

    Given some ``GUESS=SCORE`` pairs for Wordle and a word list,
    find all the words from the list that are candidate answers.

Let's look at this four-round game for Wordle 797:

.. JUDGE=....e CHEST=c.E.. WRECK=..Ec. OCEAN=OCEAN

.. raw:: html

    <table class='wordle'>
      <tr><td class="absent" >J</td> <td class="absent" >U</td> <td class="absent" >D</td> <td class="absent" >G</td> <td class="present">E</td></tr>
      <tr><td class="present">C</td> <td class="absent" >H</td> <td class="correct">E</td> <td class="absent" >S</td> <td class="absent" >T</td></tr>
      <tr><td class="absent" >W</td> <td class="absent" >R</td> <td class="correct">E</td> <td class="present">C</td> <td class="absent" >K</td></tr>
      <tr><td class="correct">O</td> <td class="correct">C</td> <td class="correct">E</td> <td class="correct">A</td> <td class="correct">N</td></tr>
    </table>

The letters of each guess are colored Green, Yellow, or Black (dark-gray).

* A Green letter 🟩 means that the letter is *correct*:
  ``N`` is the final letter of the answer.
* A Yellow letter 🟨 means that the letter is *present* elsewhere in the answer.
  There is a ``C`` in the answer;
  it's not at positions 1 or 4, but it is correct at position 2.
  Likewise, an ``E`` is present in the answer;
  it's not at position 5, but it's correct at position 3.
* A Black letter ⬛ is *absent* from the answer:
  there is no ``J``, ``U``, ``D``, ``G``,
  ``H``, ``S``, ``T``,
  ``W``, ``R``, or ``K``
  anywhere in ``OCEAN``.

Other words that could satisfy
``JUDGE=....e CHEST=c.E.. WRECK=..Ec.``
are ``ICENI``, ``ILEAC``, and ``OLEIC``—\
none of which is plausible as a Wordle answer.

The ``GUESS=SCORE`` notation is intended to be clear to read
and easier to write than Greens and Yellows.
For example:

.. raw:: html

    <table class='wordle'>
      <tr><td class="present">C</td> <td class="absent" >H</td> <td class="correct">E</td> <td class="absent" >S</td> <td class="absent" >T</td></tr>
    </table>

    <div style="margin-left: auto; margin-right: auto; text-align: center; font-family: 'Source Code Pro', monospace; font-size: 48px;">
        <span>CHEST=c.E..</span>
    </div>

* the ``E`` is in the correct position (i.e., green 🟩);
* the ``c`` is  present somewhere in the answer,
  but it is in the wrong position (yellow 🟨);
* the ``.``\ s in the score denote that the corresponding letters in the guess
  (``H``, ``S``, and ``T``)
  are absent from the answer (black ⬛).


Deductions
----------

What can we deduce from the first three rows of guesses,
``JUDGE=....e CHEST=c.E.. WRECK=..Ec.``?

There is a set of *valid* letters,
``C`` and ``E``,
that are either *present* (yellow 🟨) or *correct* (green 🟩).
Both ``E`` and ``C`` are initially present,
but ``E`` later finds its correct position,
while ``C`` does not.

There is a set of *invalid* letters that are
known to be *absent* from the answer (black ⬛):
``J``, ``U``, ``D``, ``G``, ``H``, ``S``, ``T``, ``W``, ``R``, and ``K``.

The remaining letters of the alphabet are currently *unknown*.
When they are played, they will turn into *valid* or *invalid* letters.
Unless we already have all five correct letters,
we will draw candidate letters from the unknown pool.

Furthermore, we know something about *letter positions*.
The *correct* letters are in the correct positions,
while the *present* letters are in the wrong positions.

A candidate word *must*:

1. include all valid letters —          ``C`` and ``E``
2. exclude all invalid letters —        ``J``, ``U``, ``D``, ``G``, ``H``, ``S``, ``T``,
   ``W``, ``R``, and ``K``
3. match all correct positions —        ``3:E``
4. not match any ‘present’ positions —  ``1:C``, ``4:C``, or ``5:E``

These constraints narrow the possible choices from the word list.


Prototyping with Pipes
----------------------

Let's prototype the above constraints with a series of ``grep``\ s
in a Unix pipeline tailored to this ``OCEAN`` example:

.. code-block:: bash

    # JUDGE=....e CHEST=c.E.. WRECK=..Ec.

    grep '^.....$' /usr/share/dict/words |  # Five-letter words
        tr 'a-z' 'A-Z' |                    # Translate to uppercase
        grep '^..E..$' |                    # Match CORRECT positions
        awk '/C/ && /E/' |                  # Match ALL of VALID set, CORRECT|PRESENT
        grep -v '[JUDGHSTWRK]' |            # Exclude INVALID set
        grep '^[^C]..[^C][^E]$'             # Exclude PRESENT positions

gives (in Bash, on macOS 13.4)::

    ICENI
    ILEAC
    OCEAN
    OLEIC

Let's try it for Wordle 787 (``INDEX``):

.. code-block:: bash

    # VOUCH=..... GRIPE=..i.e DENIM=deni. WIDEN=.iDEn

    grep '^.....$' /usr/share/dict/words |
        tr 'a-z' 'A-Z' |
        grep '^..DE.$' |                    # CORRECT pos
        awk '/D/ && /E/ && /I/ && /N/' |    # VALID set
        grep -v '[VOUCHGRPMW]' |            # INVALID set
        grep '^[^D][^EI][^I][^I][^EN]$'     # PRESENT pos

yields::

    INDEX

This approach is promising, but not maintainable.





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
