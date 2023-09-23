---
title: "Wordle Finder"
# date: "2023-mm-dd"
# permalink: "/__drafts/2023/mm/dd/TheSlugGoesHere.html"
permalink: "/__drafts/WordleFinder.html"
tags: [python, wordle]
filter: notypography
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
    find all the words from the list that are eligible as answers.

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
3. match all “correct” positions —      ``3:E``
4. not match any “present” positions —  ``1:C``, ``4:C``, or ``5:E``

These constraints narrow the possible choices from the word list.


Prototyping with Pipes
----------------------

Let's prototype the above constraints with a series of ``grep``\ s
in a `Unix pipeline`__ tailored to this ``OCEAN`` example:

__ https://en.wikipedia.org/wiki/Pipeline_(Unix)

.. code-block:: bash

    # JUDGE=....e CHEST=c.E.. WRECK=..Ec.

    grep '^.....$' /usr/share/dict/words |  # Extract five-letter words
        tr 'a-z' 'A-Z' |                    # Translate each word to uppercase
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
We're not going to attempt to optimize the regexes, however.

Three of the four answers–``ICENI``, ``ILEAC``, and ``OLEIC``—\
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

This approach is promising, but not maintainable.


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
        for guess in guess_scores:
            word, result = guess.split("=")
            for i, (w, r) in enumerate(zip(word, result)):
                assert "A" <= w <= "Z", "WORD should be uppercase"
                if "A" <= r <= "Z":
                    assert g == s
                    valid.add(w)
                    mask[i] = w
                elif "a" <= r <= "z":
                    assert g == s.upper()
                    valid.add(w)
                    wrong_spot[i].add(w)
                elif r == ".":
                    invalid.add(w)
                else:
                    raise ValueError(f"Unexpected {r} for {w}")
        return (invalid, valid, mask, wrong_spot)

Let's try it for the ``OCEAN`` guesses:

.. code-block:: pycon

    >>> invalid, valid, mask, wrong_spot = parse_guesses(
    ...     ["JUDGE=....e", "CHEST=c.E..", "WRECK=..Ec."])

    >>> print(f"{invalid=}\n{valid=}\n{mask=}\n{wrong_spot=}")
    invalid={'H', 'R', 'S', 'W', 'U', 'J', 'K', 'T', 'D', 'G'}
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

Here's the ``is_eligible`` function:

.. wordle1
.. code-block:: python

    def is_eligible(word, invalid, valid, mask, wrong_spot):
        letters = {c for c in word}
        if letters & valid != valid:
            # Missing some 'valid' letters from the word;
            # all Green/Correct and Yellow/Present letters are required
            logging.debug("!Valid: %s", word)
            return False
        elif letters & invalid:
            # Some invalid (Black/Absent) letters are in the word
            logging.debug("Invalid: %s", word)
            return False
        elif any(m is not None and c != m for c, m in zip(word, mask)):
            # Some of the Green/Correct letters are not at their positions
            logging.debug("!Mask: %s", word)
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
``WordleError`` (an exception class),
``TileState`` (a `multi-attribute enumeration`_),
and ``GuessScore`` (a `dataclass`_ that manages a guess–score pair
and the associated ``TileState``\ s).
We'll also use `type annotations`_ because it's 2023.

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

        def __str__(self):
            return f"{self.guess}={self.score}"

        def emojis(self, separator=""):
            return separator.join(t.emoji for t in self.tiles)

For brevity, I presented a minimal version of ``GuessScore.make`` above.
Here's the version with robust validation.
More verbose, but it ensures that no typos in the score slip through:

.. code-block:: python

    class GuessScore:
        @classmethod
        def make(cls, guess_score: str) -> "GuessScore":
            if guess_score.count("=") != 1:
                raise WordleError(f"Expected one '=' in {guess_score!r}")
            guess, score = guess_score.split("=")
            if len(guess) != WORDLE_LEN:
                raise WordleError(f"Guess {guess!r} is not {WORDLE_LEN} characters")
            if len(score) != WORDLE_LEN:
                raise WordleError(f"Score {score!r} is not {WORDLE_LEN} characters")
            tiles = []
            for i in range(WORDLE_LEN):
                if not "A" <= guess[i] <= "Z":
                    raise WordleError("Guess {guess!r} should be uppercase")
                state = cls.tile_state(score[i])
                if state is TileState.CORRECT:
                    if guess[i] != score[i]:
                        raise WordleError(f"Mismatch at {i+1}: {guess}!={score}")
                elif state is TileState.PRESENT:
                    if guess[i] != score[i].upper():
                        raise WordleError(f"Mismatch at {i+1}: {guess}!={score}")
                tiles.append(state)
            return cls(guess, score, tiles)

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
to classify the current tile and build up state.
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
            elif letters & self.invalid:
                # Invalid (black) letters are in the word
                logging.debug("Invalid: %s", word)
                return False
            elif any(m is not None and c != m for c, m in zip(word, self.mask)):
                # Couldn't find all the green/correct letters
                logging.debug("!Mask: %s", word)
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


Tests
=====

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

First Bug
---------

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


String Representation
---------------------

Let's write a few helper functions to improve the string representation.

.. wordle3
.. code-block:: python

    def letter_set(s: set[str]) -> str:
        return "".join(sorted(s))

    def letter_sets(ls: list[set[str]]) -> str:
        return "[" + ",".join(letter_set(e) or "-" for e in ls) + "]"

    def dash_mask(mask: list[str | None]):
        return "".join(m or "-" for m in mask)

    class WordleGuesses:
        def __str__(self) -> str:
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
    $ ./wordle.py HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY
    WordleGuesses(mask='-I-TY', valid='ITY', invalid='ABDEHILMNOPRSTUW',
        wrong_spot='[T,-,I,-,T]', unused='CFGJKQVXZ')
    guess_scores: ['HARES=.....|⬛⬛⬛⬛⬛, BUILT=..i.t|⬛⬛🟨⬛🟨,
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

.. code-block:: bash

    # answer: FIFTY
    $ ./wordle.py -v HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY
    WordleGuesses(mask='-I-TY', valid='ITY', invalid='ABDEHLMNOPRSUW',
        wrong_spot='[T,-,I,-,T]', unused='CFGJKQVXZ')
    FIFTY
    JITTY
    KITTY
    ZITTY

Now we have ``FIFTY``.
But we also have ``JITTY``, ``KITTY``, and ``ZITTY``,
which should not been considered eligible
since ``WITTY`` was eliminated for the ``T`` at position 3.
We'll come back to this later.

Here's an example that fails with the previous ``parse``:

.. code-block:: bash

    # answer: EMPTY
    ./wordle.py -v LODGE=....e WIPER=..Pe. TEPEE=teP.. EXPAT=E.P.t
    WordleGuesses(mask='E-P--', valid='EPT', invalid='ADEGILORWX',
        wrong_spot='[T,E,-,E,ET]', unused='BCFHJKMNQSUVYZ')
    --None--

but works with the current:

.. code-block:: bash

    # answer: EMPTY
    $ ./wordle.py -v LODGE=....e WIPER=..Pe. TEPEE=teP.. EXPAT=E.P.t
    WordleGuesses(mask='E-P--', valid='EPT', invalid='ADGILORWX',
        wrong_spot='[T,E,-,E,ET]', unused='BCFHJKMNQSUVYZ')
    EMPTS
    EMPTY

Note in ``TEPEE=teP..`` that the ``E`` in position 2 is considered “present”,
while the two ``E``\ s in positions 4 and 5 are marked “absent”,
telling us that there is only one ``E`` in the answer.
From the subsequent ``EXPAT=E.P.t``,
where the initial ``E`` is marked “correct”,
we learn that it must be at position 1.


Repeated Letters
----------------

There's still a problem that we haven't grappled with properly yet:
*repeated letters* in a guess or in an answer.
We've made an implicit assumption that there are five distinct letters
in each guess and in the answer.

Consider the results here:

.. code-block:: bash

    # answer: STYLE
    $ ./wordle.py -v GROAN=..... WHILE=...LE BELLE=...LE TUPLE=t..LE STELE=ST.LE
    WordleGuesses(mask='ST-LE', valid='ELST', invalid='ABGHINOPRUW',
        wrong_spot='[T,-,-,-,-]', unused='CDFJKMQVXYZ')
    STELE
    STYLE

``STELE`` was an incorrect guess,
so it should not have been considered eligible.
``E`` is valid in position 5, but invalid in position 3.

A second example:

.. code-block:: bash

    # answer: WRITE
    ❯ ./wordle.py -v SABER=...er REFIT=re.it TRITE=.RITE
    WordleGuesses(mask='-RITE', valid='EIRT', invalid='ABFS',
        wrong_spot='[R,E,-,EI,RT]', unused='CDGHJKLMNOPQUVWXYZ')
    TRITE
    URITE
    WRITE

``TRITE`` was an incorrect guess,
so it should not have been considered eligible.
``T`` is valid in position 4, but invalid in position 1.

Let's fix this properly.
First, revert the ``if g not in valid``
introduced in our previous attempt
and go back to our original ``WordleGuesses.parse`` implementation.

We're going to change the handling of ``invalid`` in ``is_eligible``.
The approach of checking all the letters together is insufficient.

.. wordle4
.. code-block:: python

    class WordleGuesses:
        def is_eligible(self, word: str) -> bool:
            letters = {c for c in word}
            ...
            elif letters & self.invalid:  << # insufficient
                # Invalid (black) letters are in the word
                logging.debug("Invalid: %s", word)
                return False

We need to treat each tile separately.
If we know the ``CORRECT`` letter for a tile,
then ``mask[i]`` has a letter instead of ``None``
and we'll check if ``word[i]`` also has that letter.

Otherwise, for tiles where ``mask[i]`` is ``None``,
we check to see if ``word[i]`` is in the ``invalid`` set.

.. wordle8
.. code-block:: python

    class WordleGuesses:
        def is_eligible(self, word: str) -> bool:
            ...
            elif any(m is not None and c != m for c, m in zip(word, self.mask)):
                # Couldn't find all the green/correct letters
                logging.debug("!Mask: %s", word)
                return False
            elif any(m is None and c in self.invalid for c, m in zip(word, self.mask)):
                # Invalid (black) letters are in the word
                logging.debug("Invalid: %s", word)
                return False

Let's try the ``WRITE`` and ``STYLE`` examples again:

.. code-block:: bash

    # answer: WRITE
    $ ./wordle.py -v SABER=...er REFIT=re.it TRITE=.RITE
    WordleGuesses(mask='-RITE', valid='EIRT', invalid='ABFST',
        wrong_spot='[R,E,-,EI,RT]', unused='CDGHJKLMNOPQUVWXYZ')
    URITE
    WRITE

.. code-block:: bash

    # answer: STYLE
    $ ./wordle.py -v GROAN=..... WHILE=...LE BELLE=...LE TUPLE=t..LE STELE=ST.LE
    WordleGuesses(mask='ST-LE', valid='ELST', invalid='ABEGHILNOPRUW',
        wrong_spot='[T,-,-,-,-]', unused='CDFJKMQVXYZ')
    Got: STYLE
    STYLE

``E`` is in the mask at position 5, so a trailing ``E`` is required.
The “absent” ``E`` at position 3 in the ``STELE`` guess
added ``E`` to the invalid set.
The third character in the mask is unknown,
so all words with ``E`` in the middle are ineligible.

What about some other examples?

With our previous ``if g not in valid`` attempt at fixing the bug,
neither ``QUICK`` nor ``SPICK`` were found
because of the two ``C``\ s in ``CHICK``.

.. code-block:: bash

    # answer: QUICK
    $ ./wordle.py -v MORAL=..... TWINE=..I.. CHICK=..ICK
    WordleGuesses(mask='--ICK', valid='CIK', invalid='ACEHLMNORTW',
        wrong_spot='[-,-,-,-,-]', unused='BDFGJPQSUVXYZ')
    QUICK
    SPICK

We only find one answer for ``FIFTY`` now.
``KITTY`` et al are no longer offered.

.. code-block:: bash

    # answer: FIFTY
    $ ./wordle.py -v HARES=..... BUILT=..i.t TIMID=tI... PINTO=.I.T. WITTY=.I.TY
    WordleGuesses(mask='-I-TY', valid='ITY', invalid='ABDEHILMNOPRSTUW',
        wrong_spot='[T,-,I,-,T]', unused='CFGJKQVXZ')
    FIFTY

Using this per-tile invalid set approach,
here's the updated Unix pipeline for ``INDEX``:

.. code-block:: bash

    # VOUCH=..... GRIPE=..i.e DENIM=deni. WIDEN=.iDEn

    grep '^.....$' /usr/share/dict/words |
        tr 'a-z' 'A-Z' |
        grep '^..DE.$' |                                        # CORRECT pos
        awk '/D/ && /E/ && /I/ && /N/' |                        # VALID set
        grep '^[^VOUCHGRPMW][^VOUCHGRPMW]..[^VOUCHGRPMW]$' |    # INVALID set
        grep '^[^D][^EI][^IN][^I][^EN]$'                        # PRESENT pos

Previously, the ``INVALID`` check was the simpler ``grep -v '[VOUCHGRPMW]'``.

Because the ``CORRECT`` and ``INVALID`` regexes are mutually exclusive,
they can be combined into a single ``grep``:

.. code-block:: bash

    # VOUCH=..... GRIPE=..i.e DENIM=deni. WIDEN=.iDEn

    grep '^.....$' /usr/share/dict/words |
        tr 'a-z' 'A-Z' |
        awk '/D/ && /E/ && /I/ && /N/' |                        # VALID set
        grep '^[^VOUCHGRPMW][^VOUCHGRPMW]DE[^VOUCHGRPMW]$' |    # CORRECT + INVALID
        grep '^[^D][^EI][^IN][^I][^EN]$'                        # PRESENT pos


Further Optimization of the Mask
--------------------------------

There's still a little room for improvement:

.. code-block:: bash

    # answer: TENTH
    $ ./wordle.py -v PLANK=...n. TENOR=TEN.. TENET=TEN.t
    WordleGuesses(mask='TEN--', valid='ENT', invalid='AEKLOPR',
        wrong_spot='[-,-,-,N,T]', unused='BCDFGHIJMQSUVWXYZ')
    TENCH
    TENDS
    TENDU
    TENTH
    TENTS
    TENTY

A human player getting ``TENET=TEN.t``
would realize that the fourth tile *must* be ``T``.

*Explain ``optimize``*.


Demand an Explanation
---------------------


.. code-block:: bash

    $ ./wordle.py THIEF=...e. BLADE=....E GROVE=.ro.E \
        --words ROMEO PROSE STORE MURAL ROUSE --explain

    WordleGuesses(mask=----E, valid=EOR, invalid=ABDFGHILTV,
        wrong_spot=[-,R,O,E,-], unused=CJKMNPQSUWXYZ)
        guess_scores: ['THIEF=...e.|⬛⬛⬛🟨⬛, BLADE=....E|⬛⬛⬛⬛🟩,
                        GROVE=.ro.E|⬛🟨🟨⬛🟩']
    ROMEO   Mask: needs ----E; WrongSpot: has ---E-
    PROSE   WrongSpot: has -RO--
    STORE   Invalid: has -T---; WrongSpot: has --O--
    MURAL   Valid: missing EO; Invalid: has ---A-; Mask: needs ----E
    ROUSE   eligible

.. code-block:: bash

    $ ./wordle.py CLAIM=c..i. TRICE=.riC. \
        --words INCUR TAXIS ACRID PRICY BIRCH --explain

    WordleGuesses(mask=---C-, valid=CIR, invalid=AELMT,
        wrong_spot=[C,R,I,I,-], unused=BDFGHJKNOPQSUVWXYZ)
        guess_scores: ['CLAIM=c..i.|🟨⬛⬛🟨⬛, TRICE=.riC.|⬛🟨🟨🟩⬛']
    INCUR   Mask: needs ---C-
    TAXIS   Valid: missing CR; Invalid: has TA---; Mask: needs ---C-; WrongSpot: has ---I-
    ACRID   Invalid: has A----; Mask: needs ---C-; WrongSpot: has ---I-
    PRICY   WrongSpot: has -RI--
    birch   eligible


.. _Knuth pipeline:
    https://www.spinellis.gr/blog/20200225/
.. _break-else:
    https://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html

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
    table tr td.gs {
        font-family: 'Source Code Pro', monospace;
        color: black;
        font-weight: 400;
        padding-left: 1em;
    }
    </style>
