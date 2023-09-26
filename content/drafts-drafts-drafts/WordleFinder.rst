---
title: "Wordle Finder"
# date: "2023-09-dd"
# permalink: "/2023/09/dd/TheSlugGoesHere.html"
permalink: "/drafts-drafts-drafts/WordleFinder.html"
tags: [python, wordle]
filter: notypography
draft: true
---

Unless YOUVE LIVED UNDER ROCKS, you've heard of Wordle_,
the online word game that has become wildly popular since late 2021.
You've probably seen people posting their Wordle games
as grids of little green, yellow, and black (or white) emojis on social media.

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
    programmatically find all the words from the list
    that are eligible as answers.

Let's look at this four-round game for Wordle 797:


.. raw:: html

    <table class="wordle">
      <tr><td class="absent" >J</td> <td class="absent" >U</td> <td class="absent" >D</td> <td class="absent" >G</td> <td class="present">E</td> <td class="gs">JUDGE=....e</td></tr>
      <tr><td class="present">C</td> <td class="absent" >H</td> <td class="correct">E</td> <td class="absent" >S</td> <td class="absent" >T</td> <td class="gs">CHEST=c.E..</td></tr>
      <tr><td class="absent" >W</td> <td class="absent" >R</td> <td class="correct">E</td> <td class="present">C</td> <td class="absent" >K</td> <td class="gs">WRECK=..Ec.</td></tr>
      <tr><td class="correct">O</td> <td class="correct">C</td> <td class="correct">E</td> <td class="correct">A</td> <td class="correct">N</td> <td class="gs">OCEAN=OCEAN</td></tr>
    </table>

The letters of each guess are colored Green, Yellow, or Black (dark-gray).

* A Green tile 🟩 means that the letter is **correct**:
  ``E`` is the third letter of the answer.
* A Yellow tile 🟨 means that the letter is **present** *elsewhere* in the answer.
  There is a ``C`` in the answer;
  it's not in columns 1 or 4, but it is correct in column 2.
  Likewise, an ``E`` is present in the answer;
  it's not in column 5, but it's correct in column 3.
* A Black tile ⬛ is **absent** from the answer:
  ``J``, ``U``, ``D``, ``G``,
  ``H``, ``S``, ``T``,
  ``W``, ``R``, and ``K``
  do not appear anywhere in ``OCEAN``.

(This definition of “absent” turns out to be inadequate,
as you will discover later.)

The ``GUESS=SCORE`` notation is intended to be clear to read
and also easier to write than Greens and Yellows.
For example:

.. raw:: html

    <div style="text-align: center; font-family: 'Source Code Pro', monospace; font-size: 48px;">
        <div><i>GUESS=SCORE</i></div>
        <div>CHEST=c.E..</div>
    </div>

    <table class='wordle'>
      <tr><td class="present">C</td> <td class="absent" >H</td> <td class="correct">E</td> <td class="absent" >S</td> <td class="absent" >T</td></tr>
    </table>

* the *uppercase* ``E`` at position 3 in the score denotes that
  ``E`` is in the **correct** position (i.e., green 🟩);
* the *lowercase* ``c`` at position 1 in the score denotes that
  ``C`` is **present** somewhere in the answer,
  but it is in the wrong position (yellow 🟨);
* the ``.``\ s in the score at positions 2, 4, and 5 denote that
  the corresponding letters in the guess
  (``H``, ``S``, and ``T``, respectively)
  are **absent** from the answer (black ⬛).


Deducing Constraints
--------------------

What can we deduce from the first three rows of guesses,
``JUDGE=....e CHEST=c.E.. WRECK=..Ec.``?

There is a set of *valid* letters,
``C`` and ``E``,
that are either *present* (yellow 🟨) or *correct* (green 🟩).
Both ``E`` and ``C`` start out as present,
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
3. match all “correct” positions —      ``3:E``
4. not match any “present” positions —  ``1:C``, ``4:C``, or ``5:E``

These constraints narrow the possible choices from the word list.

The obvious way to solve this with a computer
is to codify the constraints provided by previous guess–score pairs
and run through the entire list of words
to find eligible words.
But no human solves Wordle by methodically examining thousands of words.
Instead, you rack your brain for
“what ends in ``SE`` and has an ``M``?” or
“I've tried ``A``, ``E``, and ``I``; will ``O`` or ``U`` work?” or
“What are the most likely letters left on the keyboard at the bottom?”

This article will show you how to solve Wordle programmatically.
It won't help you much in playing Wordle by hand,
though you may understand more about the game when you're finished reading.


Prototyping with Pipes
----------------------

Let's prototype the above constraints with a series of `grep's`__
in a `Unix pipeline`__ tailored to this ``OCEAN`` example:

__ https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/
__ https://en.wikipedia.org/wiki/Pipeline_(Unix)

.. code-block:: bash

    # JUDGE=....e CHEST=c.E.. WRECK=..Ec.

    grep '^.....$' /usr/share/dict/words |  # Extract five-letter words
        tr 'a-z' 'A-Z' |                    # Translate each word to uppercase
        grep '^..E..$' |                    # Match CORRECT positions
        awk '/C/ && /E/' |                  # Match ALL of VALID set, CORRECT|PRESENT
        grep -v '[JUDGHSTWRK]' |            # Exclude INVALID set
        grep '^[^C]..[^C][^E]$'             # Exclude PRESENT positions

gives::

    ICENI
    ILEAC
    OCEAN
    OLEIC

(This was in Bash, on macOS 13.6.
Zsh doesn't like the comments in the middle of the multi-line pipeline,
so you may have to omit them.
Other operating systems will have different versions of ``/usr/share/dict/words``
that may not have all of these obscure words.)

We can accomplish this with only the simplest features of regular expressions:
the `dot metacharacter`_ (``.``),
`character classes`_ (``[JUD...]``)
and negated character classes (``[^E]``),
and the ``^`` and ``$`` `anchors`_.
Awk gives us `regex conjunctions`_, allowing us to match *all* of the chars.

.. _dot metacharacter:
    https://www.regular-expressions.info/dot.html
.. _character classes:
    https://www.regular-expressions.info/charclass.html
.. _anchors:
    https://www.regular-expressions.info/anchors.html
.. _regex conjunctions:
    /blog/2023/09/05/RegexConjunctions.html

The above regular expressions are
a simple mechanical transformation of the guess–score pairs.
They could be simplified.
For example, after ``grep '^..E..$'``,
the ``E`` in ``awk '/C/ && /E/'`` is redundant.
We're not going to optimize the regexes, however.

Three of the four answers—``ICENI``, ``ILEAC``, and ``OLEIC``—\
are far too obscure to be Wordle answers.
Actual Wordle answers also exclude simple plurals (``YARDS``)
and simple past tense (``LIKED``),
but allow more complex plurals (``BOXES``)
and irregular past tense (``DWELT``, ``BROKE``).
We make no attempt to judge if an eligible word is *likely* as a Wordle answer;
merely that it fits.

Let's make a pipeline for Wordle 787 (``INDEX``):

.. code-block:: bash

    # VOUCH=..... GRIPE=..i.e DENIM=deni. WIDEN=.iDEn

    grep '^.....$' /usr/share/dict/words |
        tr 'a-z' 'A-Z' |
        grep '^..DE.$' |                    # CORRECT pos
        awk '/D/ && /E/ && /I/ && /N/' |    # VALID set
        grep -v '[VOUCHGRPMW]' |            # INVALID set
        grep '^[^D][^EI][^IN][^I][^EN]$'    # PRESENT pos

yields::

    INDEX

This approach is promising,
but constructing those regexes by hand is not maintainable.


Initial Python Solution
-----------------------

Let's attempt to solve this in Python.
The first piece is to parse a list of ``GUESS=SCORE`` pairs.

.. wordle1
.. code-block:: python

    def parse_guesses(guess_scores):
        invalid = set()                         # Black/Absent
        valid = set()                           # Green/Correct or Yellow/Present
        mask = [None] * 5                       # Exact match for pos (Green/Correct)
        wrong_spot = [set() for _ in range(5)]  # Wrong spot (Yellow/Present)
        for gs in guess_scores:
            guess, score = gs.split("=")
            for i, (g, s) in enumerate(zip(guess, score)):
                assert "A" <= g <= "Z", "GUESS should be uppercase"
                if "A" <= s <= "Z":
                    assert g == s
                    valid.add(g)
                    mask[i] = g
                elif "a" <= s <= "z":
                    assert g == s.upper()
                    valid.add(g)
                    wrong_spot[i].add(g)
                elif s == ".":
                    invalid.add(g)
                else:
                    raise ValueError(f"Unexpected {s} for {g}")
        return (invalid, valid, mask, wrong_spot)

Let's try it for the ``OCEAN`` guesses:

.. code-block:: pycon

    >>> invalid, valid, mask, wrong_spot = parse_guesses(
    ...     ["JUDGE=....e", "CHEST=c.E..", "WRECK=..Ec."])

    >>> print(f"{invalid=}\n{valid=}\n{mask=}\n{wrong_spot=}")
    invalid={'H', 'K', 'D', 'G', 'T', 'R', 'U', 'W', 'J', 'S'}
    valid={'E', 'C'}
    mask=[None, None, 'E', None, None]
    wrong_spot=[{'C'}, set(), set(), {'C'}, {'E'}]

    >>> for w in vocab:
    ...     if is_eligible(w, invalid, valid, mask, wrong_spot):
    ...         print(w)
    ...
    ICENI
    ILEAC
    OCEAN
    OLEIC

Here's the ``is_eligible`` function.
We `short-circuit the evaluation`__ and
return as soon as any condition is ``False``.

__ https://www.geeksforgeeks.org/short-circuiting-techniques-python/#

.. wordle1
.. code-block:: python

    def is_eligible(word, invalid, valid, mask, wrong_spot):
        letters = {c for c in word}
        if letters & valid != valid:
            # Missing some 'valid' letters from the word;
            # all Green/Correct and Yellow/Present letters are required
            logging.debug("!Valid: %s", word)
            return False
        elif any(m is not None and c != m for c, m in zip(word, mask)):
            # Some of the Green/Correct letters are not at their positions
            logging.debug("!Mask: %s", word)
            return False
        elif letters & invalid:
            # Some invalid (Black/Absent) letters are in the word
            logging.debug("Invalid: %s", word)
            return False
        elif any(c in ws for c, ws in zip(word, wrong_spot)):
            # We have valid letters in the wrong position (Yellow/Present)
            logging.debug("WrongSpot: %s", word)
            return False
        else:
            logging.debug("Got: %s", word)
            return True


Converting to Classes
---------------------

Returning four parallel collections from a function is a `code smell`_.
Let's refactor these functions into a ``WordleGuesses`` class.

First, we'll need some helper classes:

* ``WordleError``: an exception class;
* ``TileState``: a `multi-attribute enumeration`_;
* ``GuessScore``: a `dataclass`_ that manages a guess–score pair
  and the associated ``TileState``\ s.
* We'll also use `type annotations`_ because it's 2023.

.. _code smell:
    https://pragmaticways.com/31-code-smells-you-must-know/
.. _multi-attribute enumeration:
    /blog/2023/09/02/PythonEnumsWithAttributes.html
.. _dataclass:
    https://realpython.com/python-data-classes/
.. _type annotations:
    https://bernat.tech/posts/the-state-of-type-hints-in-python/

.. wordle2
.. code-block:: python

    WORDLE_LEN = 5

    class WordleError(Exception):
       """Base exception class"""

    class TileState(namedtuple("TileState", "value emoji color css_color"), Enum):
        CORRECT = 1, "\U0001F7E9", "Green",  "#6aaa64"
        PRESENT = 2, "\U0001F7E8", "Yellow", "#c9b458"
        ABSENT  = 3, "\U00002B1B", "Black",  "#838184"

    @dataclass
    class GuessScore:
        guess: str
        score: str
        tiles: list[TileState]

        @classmethod
        def make(cls, guess_score: str) -> "GuessScore":
            guess, score = guess_score.split("=")
            tiles = [cls.tile_state(s) for s in score]
            return cls(guess, score, tiles)

        @classmethod
        def tile_state(cls, score_tile: str) -> TileState:
            if "A" <= score_tile <= "Z":
                return TileState.CORRECT
            elif "a" <= score_tile <= "z":
                return TileState.PRESENT
            elif score_tile == ".":
                return TileState.ABSENT
            else:
                raise WordleError(f"Invalid score: {score_tile}")

        def __repr__(self):
            return f"{self.guess}={self.score}"

        def emojis(self, separator=""):
            return separator.join(t.emoji for t in self.tiles)

For brevity, I presented a minimal version of ``GuessScore.make`` above.
The version in my `wordle repository`_ has robust validation.

.. _wordle repository:
   https://github.com/georgevreilly/wordle

Let's add the main class, ``WordleGuesses``:

.. wordle2
.. code-block:: python

    @dataclass
    class WordleGuesses:
        mask: list[str | None]      # Exact match for position (Green/Correct)
        valid: set[str]             # Green/Correct or Yellow/Present
        invalid: set[str]           # Black/Absent
        wrong_spot: list[set[str]]  # Wrong spot (Yellow/Present)
        guess_scores: list[GuessScore]

        @classmethod
        def parse(cls, guess_scores: list[GuessScore]) -> "WordleGuesses":
            mask: list[str | None] = [None] * WORDLE_LEN
            valid: set[str] = set()
            invalid: set[str] = set()
            wrong_spot: list[set[str]] = [set() for _ in range(WORDLE_LEN)]

            for gs in guess_scores:
                for i, (t, g) in enumerate(zip(gs.tiles, gs.guess)):
                    if t is TileState.CORRECT:
                        mask[i] = g
                        valid.add(g)
                    elif t is TileState.PRESENT:
                        wrong_spot[i].add(g)
                        valid.add(g)
                    elif t is TileState.ABSENT:
                        invalid.add(g)

            return cls(mask, valid, invalid, wrong_spot, guess_scores)

``WordleGuesses.parse`` is a bit shorter and clearer than ``parse_guesses``.
It uses ``TileState`` at each position
to classify the current tile and
accumulate state in the four member collections.
Since ``GuessScore.make`` has validated the input,
``parse`` doesn't need to do any further validation.

The ``is_eligible`` method is essentially the same as its predecessor:

.. wordle2
.. code-block:: python

    class WordleGuesses:
        def is_eligible(self, word: str) -> bool:
            letters = {c for c in word}
            if letters & self.valid != self.valid:
                # Did not have the full set of green+yellow letters known to be valid
                logging.debug("!Valid: %s", word)
                return False
            elif any(m is not None and c != m for c, m in zip(word, self.mask)):
                # Couldn't find all the green/correct letters
                logging.debug("!Mask: %s", word)
                return False
            elif letters & self.invalid:
                # Invalid (black) letters are in the word
                logging.debug("Invalid: %s", word)
                return False
            elif any(c in ws for c, ws in zip(word, self.wrong_spot)):
                # Found some yellow letters: valid letters in wrong position
                logging.debug("WrongSpot: %s", word)
                return False
            else:
                # Potentially valid
                logging.info("Got: %s", word)
                return True

        def find_eligible(self, vocabulary: list[str]) -> list[str]:
            return [w for w in vocabulary if self.is_eligible(w)]

There's a `famous story`__ where Donald Knuth
was asked by Jon Bentley to demonstrate `literate programming`__
by finding the *K* most common words from a text file.
Knuth turned in an eight-page gem of WEB, which was reviewed by Doug McIlroy,
who demonstrated that the task could also be accomplished in a six-line pipeline.

Wordle can also be solved with a six-line pipeline,
but the regexes are quite difficult to type correctly
and they have to be carefully hand tailored
for each set of guess–score pairs.
There is no one general six-line pipeline.

I know that I'd much rather work with these Python classes.
As we'll see below, they are a solid foundation
that can be built upon in many ways.

__ https://www.spinellis.gr/blog/20200225/
__ http://www.literateprogramming.com/


Does it Work?
-------------

Let's try it!:

.. code-block:: bash

    # answer: ARBOR
    $ ./wordle.py HARES=.ar.. GUILT=..... CROAK=.Roa. BRAVO=bRa.o
    ARBOR

    # answer: CACHE
    $ ./wordle.py CHAIR=Cha.. CLASH=C.a.h CATCH=CA.ch
    CACHE
    CAHOW

    # answer: TOXIC
    $ ./wordle.py LEAKS=..... MIGHT=.i..t BLITZ=..it. OPTIC=o.tIC TONIC=TO.IC
    TORIC
    TOXIC

This looks right
but there are some subtle bugs in the code.


Fifty is the new Witty
----------------------

Here we expect to find ``FIFTY``, but no words match:

.. code-block:: bash

    # answer: FIFTY
    $ ./wordle.py HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY
    --None--

Let's take a look at the state of the ``WordleGuesses`` instance:

.. code-block:: pycon

    >>> guess_scores = [GuessScore.make(gs) for gs in
            "HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY".split()]

    >>> wg = WordleGuesses.parse(guess_scores)
    >>> wg
    WordleGuesses(mask=[None, 'I', None, 'T', 'Y'], valid={'T', 'I', 'Y'}, invalid={
    'A', 'E', 'D', 'M', 'U', 'H', 'I', 'B', 'L', 'T', 'P', 'O', 'R', 'W', 'N', 'S'},
    wrong_spot=[{'T'}, set(), {'I'}, set(), {'T'}], guess_scores=[GuessScore(guess='HARES',
    score='.....', tiles=[<TileState.ABSENT: TileState(value=3, emoji='⬛', color='Black',
    css_color='#838184')>, <TileState.ABSENT: TileState(value=3, emoji='⬛', color='Black',
    css_color='#838184')>,
        ... much snipped ...

That's ugly.


Better String Representation
----------------------------

Let's write a few helper functions to improve the ``__repr__``:

.. wordle3
.. code-block:: python

    def letter_set(s: set[str]) -> str:
        return "".join(sorted(s))

    def letter_sets(ls: list[set[str]]) -> str:
        return "[" + ",".join(letter_set(e) or "-" for e in ls) + "]"

    def dash_mask(mask: list[str | None]):
        return "".join(m or "-" for m in mask)

    class WordleGuesses:
        def __repr__(self) -> str:
            mask = dash_mask(self.mask)
            valid = letter_set(self.valid)
            invalid = letter_set(self.invalid)
            wrong_spot = letter_sets(self.wrong_spot)
            unused = letter_set(
                set(string.ascii_uppercase) - self.valid - self.invalid)
            _guess_scores = [", ".join(f"{gs}|{gs.emojis()}"
                for gs in self.guess_scores)]
            return (
                f"WordleGuesses({mask=}, {valid=}, {invalid=},\n"
                f"    {wrong_spot=}, {unused=})"
            )

Let's run it again, printing out the instance:

.. code-block:: bash

    # answer: FIFTY
    $ ./wordle.py -v HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY
    WordleGuesses(mask='-I-TY', valid='ITY', invalid='ABDEHILMNOPRSTUW',
        wrong_spot='[T,-,I,-,T]', unused='CFGJKQVXZ')
        guess_scores= ['HARES=.....|⬛⬛⬛⬛⬛, BUILT=..i.t|⬛⬛🟨⬛🟨,
            TIMID=tI...|🟨🟩⬛⬛⬛, PINTO=.I.T.|⬛🟩⬛🟩⬛, WITTY=.I.TY|⬛🟩⬛🟩🟩']
    --None--

That's a huge improvement in legibility
over the default string representation!

There's a ``T`` in both ``valid`` and ``invalid``—\
two sets that should be mutually exclusive.
The first “absent” ``T`` at position 3 in ``WITTY``
has poisoned the second  ``T`` at position 4, which is “correct”.
The ``T`` at position 1 in ``TIMID`` and
the ``T`` at position 5 in ``BUILT`` are “present”
because they are the only ``T`` in those guesses.

When there are two ``T``\ s in a guess, but only one ``T`` in the answer,
one of the ``T``\ s will either be “correct” or “present”.
The second, superfluous ``T`` will be “absent”.


First Attempt at Fixing the Bug
-------------------------------

Let's modify ``WordleGuesses.parse`` slightly to address that.
When we get an ``ABSENT`` tile,
we should add that letter to ``invalid``
only if it's not already in ``valid``.

.. wordle4
.. code-block:: python

    class WordleGuesses:
        @classmethod
        def parse(cls, guess_scores: list[GuessScore]) -> "WordleGuesses":
            mask: list[str | None] = [None] * WORDLE_LEN
            valid: set[str] = set()
            invalid: set[str] = set()
            wrong_spot: list[set[str]] = [set() for _ in range(WORDLE_LEN)]

            for gs in guess_scores:
                for i, (t, g) in enumerate(zip(gs.tiles, gs.guess)):
                    if t is TileState.CORRECT:
                        mask[i] = g
                        valid.add(g)
                    elif t is TileState.PRESENT:
                        wrong_spot[i].add(g)
                        valid.add(g)
                    elif t is TileState.ABSENT:
                        if g not in valid:  # <<< new
                            invalid.add(g)

            return cls(mask, valid, invalid, wrong_spot, guess_scores)

Does it work? Yes!
Now we have ``FIFTY``.

.. code-block:: bash

    # answer: FIFTY
    $ ./wordle.py -v HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY
    WordleGuesses(mask='-I-TY', valid='ITY', invalid='ABDEHLMNOPRSUW',
        wrong_spot='[T,-,I,-,T]', unused='CFGJKQVXZ')
    FIFTY
    JITTY
    KITTY
    ZITTY

But we also have ``JITTY``, ``KITTY``, and ``ZITTY``,
which should not been considered eligible
since ``WITTY`` was eliminated for the ``T`` at position 3.
We'll come back to this soon.


The Problem of Repeated Letters
-------------------------------

There's a problem that we haven't grappled with properly yet:
*repeated letters* in a guess or in an answer.
We've made an implicit assumption that there are five distinct letters
in each guess and in the answer.

Here's an example that fails with the original ``parse``:

.. code-block:: bash

    # answer: EMPTY
    $ ./wordle.py -v LODGE=....e WIPER=..Pe. TEPEE=teP.. EXPAT=E.P.t
    WordleGuesses(mask='E-P--', valid='EPT', invalid='ADEGILORWX',
        wrong_spot='[T,E,-,E,ET]', unused='BCFHJKMNQSUVYZ')
    --None--

but works with the current ``parse``:

.. code-block:: bash

    # answer: EMPTY
    $ ./wordle.py -v LODGE=....e WIPER=..Pe. TEPEE=teP.. EXPAT=E.P.t
    WordleGuesses(mask='E-P--', valid='EPT', invalid='ADGILORWX',
        wrong_spot='[T,E,-,E,ET]', unused='BCFHJKMNQSUVYZ')
    EMPTS
    EMPTY

Note that there is no longer an ``E`` in ``invalid``.
In ``TEPEE=teP..``, the ``E`` in position 2 is considered “present”,
while the two ``E``\ s in positions 4 and 5 are marked “absent”.
This tells us that there is only one ``E`` in the answer.
Since ``P`` is correct in position 3 of ``TEPEE``,
the ``E`` must be in position 1.
This is confirmed by the subsequent ``EXPAT=E.P.t``,
where the initial ``E`` is marked “correct”.

Our previous understanding of “absent” was too simple.
An “absent” tile can mean one of two things:

1. This letter is not in the answer at all—the usual case.
2. If another copy of this letter
   is “correct” or “present” elsewhere in the same guess (i.e., *valid*),
   the letter is superfluous at this position.
   The guess has more instances of this letter than the answer does.

Consider the results here:

.. code-block:: bash

    # answer: STYLE
    $ ./wordle.py -v GROAN=..... WHILE=...LE BELLE=...LE TUPLE=t..LE STELE=ST.LE
    WordleGuesses(mask='ST-LE', valid='ELST', invalid='ABGHINOPRUW',
        wrong_spot='[T,-,-,-,-]', unused='CDFJKMQVXYZ')
    STELE
    STYLE

``STELE`` was an incorrect guess,
so it should not have been offered as an eligible word.
``E`` is valid in position 5, but wrong in position 3.

Another example:

.. code-block:: bash

    # answer: WRITE
    $ ./wordle.py -v SABER=...er REFIT=re.it TRITE=.RITE
    WordleGuesses(mask='-RITE', valid='EIRT', invalid='ABFS',
        wrong_spot='[R,E,-,EI,RT]', unused='CDGHJKLMNOPQUVWXYZ')
    TRITE
    URITE
    WRITE

``TRITE`` was an incorrect guess,
so it should not have been offered.
``4:T`` is valid, ``1:T`` is wrong.


Fixing Repeated Absent Letters
------------------------------

We can fix this by making two passes through the tiles
for each guess–score pair.

1. Handle “correct” and “present” tiles as before.
2. Add “absent” tiles to either ``invalid`` or ``wrong_spot``.

We need the second pass to handle a case like ``WITTY=.I.TY``,
where the “absent” ``3:T`` precedes the “correct” ``4:T``:
the ``valid`` set must be fully updated before we process “absent” tiles.

.. wordle5
.. code-block:: python

    class WordleGuesses:
        @classmethod
        def parse(cls, guess_scores: list[GuessScore]) -> "WordleGuesses":
            mask: list[str | None] = [None for _ in range(WORDLE_LEN)]
            valid: set[str] = set()
            invalid: set[str] = set()
            wrong_spot: list[set[str]] = [set() for _ in range(WORDLE_LEN)]

            for gs in guess_scores:
                # First pass for correct and present
                for i, (t, g) in enumerate(zip(gs.tiles, gs.guess)):
                    if t is TileState.CORRECT:
                        mask[i] = g
                        valid.add(g)
                    elif t is TileState.PRESENT:
                        wrong_spot[i].add(g)
                        valid.add(g)

                # Second pass for absent letters
                for i, (t, g) in enumerate(zip(gs.tiles, gs.guess)):
                    if t is TileState.ABSENT:
                        if g in valid:
                            # There are more instances of `g` in `gs.guess`
                            # than in the answer
                            wrong_spot[i].add(g)
                        else:
                            invalid.add(g)

            return cls(mask, valid, invalid, wrong_spot, guess_scores)

We can see that ``valid`` and ``invalid`` are disjoint.
The ``is_eligible`` method needs no changes.

Let's try the ``WRITE`` example again:

.. code-block:: bash

    # answer: WRITE
    $ ./wordle.py -v SABER=...er REFIT=re.it TRITE=.RITE
    WordleGuesses(mask='-RITE', valid='EIRT', invalid='ABFS',
        wrong_spot='[RT,E,-,EI,RT]', unused='CDGHJKLMNOPQUVWXYZ')
    URITE
    WRITE

There is now a ``T`` in the first ``wrong_spot`` entry.

And ``STYLE``?

.. code-block:: bash

    # answer: STYLE
    $ ./wordle.py -v GROAN=..... WHILE=...LE BELLE=...LE TUPLE=t..LE STELE=ST.LE
    WordleGuesses(mask='ST-LE', valid='ELST', invalid='ABGHINOPRUW',
        wrong_spot='[T,E,EL,-,-]', unused='CDFJKMQVXYZ')
    STYLE

Both the second and third ``wrong_spot``\ s now have an ``E``.
The “absent” ``3:L`` from ``BELLE`` is also in the third ``wrong_spot``.

What about some other examples?

In our previous attempt at fixing the bug,
neither ``QUICK`` nor ``SPICK`` were found
because the first ``C`` in ``CHICK`` was “absent”
and thus marked invalid.
Now, the ``valid`` and ``invalid`` sets are disjoint,
there's a ``C`` in the first element of ``wrong_spot``,
and both words are found:

.. code-block:: bash

    # answer: QUICK
    $ ./wordle.py -v MORAL=..... TWINE=..I.. CHICK=..ICK
    WordleGuesses(mask='--ICK', valid='CIK', invalid='AEHLMNORTW',
        wrong_spot='[C,-,-,-,-]', unused='BDFGJPQSUVXYZ')
    QUICK
    SPICK

As expected, we find only one answer for ``FIFTY`` now:

.. code-block:: bash

    # answer: FIFTY
    $ ./wordle.py -v HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY
    WordleGuesses(mask='-I-TY', valid='ITY', invalid='ABDEHLMNOPRSUW',
        wrong_spot='[T,-,IT,I,T]', unused='CFGJKQVXZ')
    FIFTY

The new ``T`` in the third element of ``wrong_spot``
blocks the rhymes for ``WITTY``.


Further Optimization of the Mask
--------------------------------

There's still room for improvement.
If you guess ``ANGLE=ANGle``,
it's immediately obvious (to a human player) that
you should swap the ``L`` and ``E``
to guess ``ANGEL`` on your next turn.
Or swap the ``P`` and ``T`` in ``SPRAT=SpRAt`` to guess ``STRAP``.

Similarly, ``TENET=TEN.t`` tells you that
the fourth letter of the answer must be ``T``,
while ``CHORE=C.OrE`` must have ``2:R``.

A more complex example:

.. code-block:: bash

    # answer: BURLY
    $ ./wordle.py -v LOWER=l...r FRAIL=.r..l BLURT=Blur.
    WordleGuesses(mask='B----', valid='BLRU', invalid='AEFIOTW',
        wrong_spot='[L,LR,U,R,LR]', unused='CDGHJKMNPQSVXYZ')

The ``R`` is in the wrong spot
in positions 5 (``l...r``), 2 (``.r..l``), and 4 (``Blur.``).
The ``B`` is correct in position 1, so ``R`` must be in position 3.

The ``L`` is in the wrong spot in positions 1, 5, and 2.
``B`` is in position 1, ``R`` is now in 3, so that leaves only position 4.

There remain two possibilities for ``U``\
—positions 2 and 5—\
so we need more information
than is contained in ``mask`` and ``wrong_spot``
to determine where to place it.

The original mask, ``B----``, was due to having only one “correct” letter.
Using the cumulative information in the guesses and scores,
we can infer a mask of ``B-RL-``.

In all of these cases,
we can find exactly one remaining position
where a “present” letter can be placed.
In the ``BURLY`` example, it takes two passes:
we couldn't uniquely determine a place for ``L``
until we had already placed ``R``.

Up to now, we've been treating each tile in almost complete isolation.
Let's optimize the mask programmatically.

First, we loop through all the guess–score pairs,
building a ``valid`` multiset of the “correct” and “present” letters.
Then we subtract a multiset of the “correct” letters,
yielding a multiset of the “present” letters.
To account for repeated letters,
such as the two ``T``\ s in ``TENET=TEN.t``,
we use Python's ``collections.Counter`` as a multiset_.

We loop over ``present``, trying for each letter
to find a single empty position where it can be placed in the mask.
If there is such a position,
we update ``mask2`` and break out of the inner loop.
If there isn't (as in the two possibilities for ``U`` in ``BURLY``),
then we use the little-known `break-else`_ construct
to exit from the outer loop.

Finally, we merge ``mask2`` into ``self.mask``.
This ``optimize`` method is called
from the end of ``WordleGuesses.parse``.

.. _multiset:
    https://dbader.org/blog/sets-and-multiset-in-python
.. _break-else:
    https://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html

.. wordle
.. code-block:: python

    class WordleGuesses:
        def optimize(self) -> list[str | None]:
            """Use PRESENT tiles to improve `mask`."""
            mask1: list[str | None] = self.mask
            mask2: list[str | None] = [None] * WORDLE_LEN
            # Compute `valid`, a multiset of the correct and present letters in all guesses
            valid: Counter[str] = Counter()
            for gs in self.guess_scores:
                valid |= Counter(
                    g for g, t in zip(gs.guess, gs.tiles) if t is not TileState.ABSENT
                )
            correct = Counter(c for c in mask1 if c is not None)
            # Compute `present`, a multiset of the valid letters
            # whose correct position is not yet known; i.e., PRESENT in any row.
            present = valid - correct
            logging.debug(f"{valid=} {correct=} {present=}")

            def available(c, i):
                "Can `c` be placed in slot `i` of `mask2`?"
                return mask1[i] is None and mask2[i] is None and c not in self.wrong_spot[i]

            while present:
                for c in present:
                    positions = [i for i in range(WORDLE_LEN) if available(c, i)]
                    # Is there only one position where `c` can be placed?
                    if len(positions) == 1:
                        i = positions[0]
                        mask2[i] = c
                        present -= Counter(c)
                        logging.debug(f"{i+1} -> {c}")
                        break
                else:
                    # We reach this for-else only if there was no `break` in the for-loop;
                    # i.e., no one-element `positions` was found in `present`.
                    # We must abandon the outer loop, even though `present` is not empty.
                    break

            logging.debug(f"{present=} {mask2=}")

            self.mask = [m1 or m2 for m1, m2 in zip(mask1, mask2)]
            logging.info(
                f"\toptimize: {dash_mask(mask1)} | {dash_mask(mask2)}"
                f" => {dash_mask(self.mask)}"
            )
            return mask2

Here are some examples of it in action.
Going from ``---ET`` to ``-ESET``:

.. code-block:: bash

    # answer: BESET
    $ ./wordle.py -vv CIVET=...ET EGRET=e..ET SLEET=s.eET
    WordleGuesses(mask=---ET, valid=EST, invalid=CGILRV,
        wrong_spot=[ES,-,E,-,-], unused=ABDFHJKMNOPQUWXYZ)
    valid=Counter({'E': 2, 'T': 1, 'S': 1}) correct=Counter({'E': 1, 'T': 1})
        present=Counter({'E': 1, 'S': 1})
    2 -> E
    3 -> S
    present=Counter() mask2=[None, 'E', 'S', None, None]
        optimize: ---ET | -ES-- => -ESET

And from ``C----`` to ``CLER-``:

.. code-block:: bash

    # answer: CLERK
    $ ./wordle.py -vv SINCE=...ce CEDAR=Ce..r CRUEL=Cr.el
    WordleGuesses(mask=C----, valid=CELR, invalid=ADINSU,
        wrong_spot=[-,ER,-,CE,ELR], unused=BFGHJKMOPQTVWXYZ)
    valid=Counter({'C': 1, 'E': 1, 'R': 1, 'L': 1}) correct=Counter({'C': 1})
        present=Counter({'E': 1, 'R': 1, 'L': 1})
    3 -> E
    4 -> R
    2 -> L
    present=Counter() mask2=[None, 'L', 'E', 'R', None]
        optimize: C---- | -LER- => CLER-


Demanding an Explanation
------------------------

Would you like to know *why* a guess is ineligible?
We can do that too.


.. code-block:: bash

    # answer: ROUSE
    $ ./wordle.py THIEF=...e. BLADE=....E GROVE=.ro.E \
        --words ROMEO PROSE STORE MURAL ROUSE --explain

    WordleGuesses(mask=----E, valid=EOR, invalid=ABDFGHILTV,
        wrong_spot=[-,R,O,E,-], unused=CJKMNPQSUWXYZ)
        guess_scores: ['THIEF=...e.|⬛⬛⬛🟨⬛, BLADE=....E|⬛⬛⬛⬛🟩,
                        GROVE=.ro.E|⬛🟨🟨⬛🟩']
    ROMEO   Mask: needs ----E; WrongSpot: has ---E-
    PROSE   WrongSpot: has -RO--
    STORE   Invalid: has -T---; WrongSpot: has --O--
    MURAL   Valid: missing EO; Mask: needs ----E; Invalid: has ---AL
    ROUSE   Eligible

.. code-block:: bash

    # answer: BIRCH
    $ ./wordle.py CLAIM=c..i. TRICE=.riC. \
        --words INCUR TAXIS PRICY ERICA BIRCH --explain

    WordleGuesses(mask=---C-, valid=CIR, invalid=AELMT,
        wrong_spot=[C,R,I,I,-], unused=BDFGHJKNOPQSUVWXYZ)
        guess_scores: ['CLAIM=c..i.|🟨⬛⬛🟨⬛, TRICE=.riC.|⬛🟨🟨🟩⬛']
    INCUR   Mask: needs ---C-
    TAXIS   Valid: missing CR; Mask: needs ---C-; Invalid: has TA---; WrongSpot: has ---I-
    PRICY   WrongSpot: has -RI--
    ERICA   Invalid: has E---A; WrongSpot: has -RI--
    BIRCH   Eligible

Here's how those explanations were computed,
using a variation on ``is_eligible``:

.. wordle
.. code-block:: python

    class WordleGuesses:
        def is_ineligible(self, word: str) -> dict[str, str]:
            reasons = {}
            letters = {c for c in word}
            if missing := self.valid - (letters & self.valid):
                # Did not have the full set of green+yellow letters known to be valid
                reasons["Valid"] = f"missing {letter_set(missing)}"

            mask = [(m if c != m else None) for c, m in zip(word, self.mask)]
            if any(mask):
                # Couldn't find all the green/correct letters
                reasons["Mask"] = f"needs {dash_mask(mask)}"

            invalid = [(c if c in self.invalid else None) for c in word]
            if any(invalid):
                # Invalid (black) letters present at specific positions
                reasons["Invalid"] = f"has {dash_mask(invalid)}"

            wrong = [(c if c in ws else None) for c, ws in zip(word, self.wrong_spot)]
            if any(wrong):
                # Found some yellow letters: valid letters in wrong position
                reasons["WrongSpot"] = f"has {dash_mask(wrong)}"

            return reasons

        def find_explanations(self, vocabulary: list[str]) -> list[tuple[str, str | None]]:
            explanations = []
            for word in vocabulary:
                reasons = self.is_ineligible(word)
                why = None
                if reasons:
                    why = "; ".join(
                        f"{k}: {v}" for k, v in self.is_ineligible(word).items())
                explanations.append((word, why))
            return explanations

This approach is slower than ``is_eligible``,
though it's not noticeable
when running ``wordle.py`` for one set of guess–scores.
I have a test tool (``score.py``)
that runs through the 200+ games that I've recorded.
Using ``find_explanations``, it took about 10 seconds to run.
Switching to ``find_eligible``, it dropped to 2 seconds (5x improvement).
By prefiltering the word list with a regex made from the mask,
the time drops to about 500 milliseconds (further 4x improvement).

.. code-block:: python

    pattern = re.compile("".join(m or "." for m in parsed_guesses.mask))
    word_list = [w for w in vocabulary if pattern.fullmatch(w)]
    eligible = parsed_guesses.find_eligible(word_list)


Finally
-------

I thought I knew a lot about solving Wordle programmatically
when I started this long post a month ago.
Along the way,
I realized that I could use a few ugly greps
to accomplish the same thing;
wrote a tool to render games as HTML and emojis;
spun off a couple of blog posts on
`multi-attribute enumeration`_ and `regex conjunctions`_;
found and fixed several bugs with repeated letters,
greatly refining my understanding of the nuances;
added a means to explain ineligibility;
and realized that I could optimize the mask programmatically.

The full code can be found in my `wordle repository`_.


.. -------------------------------------------------------------_
.. Sticking the Wordle stylesheet at the end out of the way

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
    table.wordle tr td {
        color: white;
        background-color: white;
        height: 62px;
        width: 62px;
        text-align: center;
    }
    table.wordle tr td.correct {
        background-color: #6aaa64;
    }
    table.wordle tr td.present {
        background-color: #c9b458;
    }
    table.wordle tr td.absent {
        background-color: #838184;
    }
    table.wordle tr td.gs {
        font-family: 'Source Code Pro', monospace;
        color: black;
        font-weight: 400;
        padding-left: 1em;
    }
    </style>
