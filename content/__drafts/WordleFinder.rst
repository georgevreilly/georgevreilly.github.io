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

    <div style="text-align: center; font-family: 'Source Code Pro', monospace; font-size: 48px;">
        <div><i>GUESS=SCORE</i></div>
        <div>CHEST=c.E..</div>
    </div>

    <table class='wordle'>
      <tr><td class="present">C</td> <td class="absent" >H</td> <td class="correct">E</td> <td class="absent" >S</td> <td class="absent" >T</td></tr>
    </table>

* the uppercase ``E`` at position 3 in the score denotes that
  ``E`` is in the correct position (i.e., green 🟩);
* the lowercase ``c`` at position 1 in the score denotes that
  ``C`` is  present somewhere in the answer,
  but it is in the wrong position (yellow 🟨);
* the ``.``\ s in the score at positions 2, 4, and 5 denote that
  the corresponding letters in the guess (``H``, ``S``, and ``T``)
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
2. exclude all invalid letters —        ``JUDGHSTWRK``
3. match all correct positions —        ``3:E``
4. not match any ‘present’ positions —  ``1:C``, ``4:C``, or ``5:E``

These constraints narrow the possible choices from the word list.


Prototyping with Pipes
----------------------

Let's prototype the above constraints with a series of ``grep``\ s
in a Unix pipeline tailored to this ``OCEAN`` example:

.. code-block:: bash

    # TODO why is alignment messed up?

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

We can accomplish this with only the simplest features of regular expressions,
the `dot metacharacter`_ (``.``),
`character classes`_ (``[JUD...]``) and negated character classes (``[^E]``),
and the ``^`` and ``$`` `anchors`_.
Awk gives us `regex conjunctions`_.

.. _dot metacharacter:
    https://www.regular-expressions.info/dot.html
.. _character classes:
    https://www.regular-expressions.info/charclass.html
.. _anchors:
    https://www.regular-expressions.info/anchors.html
.. _regex conjunctions:
    /blog/2023/09/05/RegexConjunctions.html

Let's try our pipeline for Wordle 787 (``INDEX``):

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


Initial Python Solution
-----------------------

Let's attempt to solve this in Python.
The first piece is to parse a list of ``GUESS=SCORE`` pairs.

.. code-block:: python

    def parse_guesses(guess_scores):
        invalid = set()  # Black/Absent
        valid = set()  # Green or Yellow
        mask = [None] * 5  # Exact match for position (Green/Correct)
        wrong_spot = [set() for _ in range(5)]  # Wrong spot (Yellow/Present)
        for guess in guess_scores:
            word, result = guess.split("=")
            for i, (w, r) in enumerate(zip(word, result)):
                assert "A" <= w <= "Z", "WORD should be uppercase"
                if "A" <= r <= "Z":
                    valid.add(w)
                    mask[i] = w
                elif "a" <= r <= "z":
                    valid.add(w)
                    wrong_spot[i].add(w)
                elif r == ".":
                    invalid.add(w)
                else:
                    raise ValueError(f"Unexpected {r} for {w}")
        return (invalid, valid, mask, wrong_spot)

Here's how we use the parsed data:

.. code-block:: python

    def is_eligible(word, invalid, valid, mask, wrong_spot):
        letters = {c for c in word}
        if letters & valid != valid:
            # Missing some 'valid' letters
            trace(f"!Valid: {word}")
            return False
        elif letters & invalid:
            trace(f"Invalid: {word}")
            return False
        elif any(m is not None and c != m for c, m in zip(word, mask)):
            # Some of the Green/Correct letters are missing
            trace(f"!Mask: {word}")
            return False
        elif any(c in ws for c, ws in zip(word, wrong_spot)):
            # We have Yellow letters
            trace(f"WrongSpot: {word}")
            return False
        else:
            trace(f"Got: {word}")
            return True

Classes
-------

Returning four parallel collections from a function is a `code smell`_.
Let's refactor this into a class.

First, we'll need some helper classes:
``TileState``, a `multi-attribute enumeration`_, and ``GuessScore``.

.. _code smell:
    https://pragmaticways.com/31-code-smells-you-must-know/
.. _multi-attribute enumeration:
    /blog/2023/09/02/PythonEnumsWithAttributes.html

.. code-block:: python

    class TileState(namedtuple("TileState", "value emoji color css_color"), Enum):
        CORRECT = 1, "\U0001F7E9", "Green",  "#6aaa64"
        PRESENT = 2, "\U0001F7E8", "Yellow", "#c9b458"
        ABSENT  = 3, "\U00002B1B", "Black",  "#838184"



Old
===

And how we call ``is_eligible``:

.. code-block:: python

    def main():
        namespace = parse_args()
        with open(namespace.word_file) as f:
            WORDS = [w.upper().strip() for w in f
                     if len(w.strip()) == WORDLE_LEN]
        invalid, valid, mask, wrong_spot = parse_guesses(namespace.guess_scores)
        choices = [w for w in WORDS if is_eligible(w, invalid, valid, mask, wrong_spot)]
        print("\n".join(choices))

For the sake of completeness, here's the rest:

.. code-block:: python

    _VERBOSITY = 0

    def debug(s):
        if _VERBOSITY: print(s)

    def trace(s):
        if _VERBOSITY >= 2: print(s)

    def parse_args():
        parser = argparse.ArgumentParser(description="Wordle Finder")
        parser.set_defaults(
            word_file="/usr/share/dict/words",
            verbose=0,
        )
        parser.add_argument(
            "--verbose", "-v", action="count", help="Show all the steps")
        parser.add_argument(
            "--word-file", "-w", help="Word file. Default: %(default)s")
        parser.add_argument(
            "guess_scores",
            nargs="+",
            metavar="GUESS=score",
            help="Examples: 'ARISE=.r.se' 'ROUTE=R.u.e' 'RULES=Ru.eS'",
        )
        namespace = parser.parse_args()
        global _VERBOSITY
        _VERBOSITY = namespace.verbose
        return namespace

Let's try it!::

    $ ./wordle.py HARES=.ar.. GUILT=..... CROAK=.Roa. BRAVO=bRa.o
    ARBOR

    $ ./wordle1.py CHAIR=Cha.. CLASH=C.a.h CATCH=CA.ch
    CACHE
    CAHOW

    $ ./wordle1.py LEAKS=..... MIGHT=.i..t BLITZ=..it. OPTIC=o.tIC TONIC=TO.IC
    TORIC
    TOXIC

This looks right
but there are a couple of subtle bugs here.
We'll come back to those.

Class
-----

Bugs
----

``FIFTY: HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY``
can be fixed by inserting ``if w not in valid``
between ``elif r == "."`` and ``invalid.add(w)``.
But this returns too many results.

We need the per-position ``invalid`` for these:

* ``QUICK: MORAL=..... TWINE=..I.. CHICK=..ICK`` doesn't find ``QUICK``
* ``STYLE: `GROAN=..... WHILE=...LE BELLE=...LE TUPLE=t..LE STELE=ST.LE``
  finds both ``STYLE`` and ``STELE`` (which is known to be wrong)

.. _Knuth pipeline:
    https://www.spinellis.gr/blog/20200225/


.. -------------------------------------------------------------_
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
