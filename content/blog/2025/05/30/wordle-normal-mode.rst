---
title: "Wordle on Normal Mode"
# date: "2025-05-30"
permalink: "/blog/2025/05/30/WordleOnNormalMode.html"
tags: [python, wordle]
---
.. pull-quote::

    At the `June 2025 PuPPy meetup`_ (Puget Sound Programming Python),
    I will be giving a talk about *Exploring Wordle*.

    | June 11: doors open at 5:30pm
    | GitHub Bellevue
    | 10900 NE 4th St, Floor 21
    | Bellevue, WA 98004

In `Exploring Wordle`_, I wrote a long blog post about solving Wordle programmatically,
which implicitly solved Wordle in *Hard Mode*.
Today, I want to discuss a strategy that is only possible in Normal Mode.

.. image:: /content/binary/WordleHardMode.png
    :alt: Hard Mode in Wordle setting
    :target: https://slate.com/culture/2022/02/wordle-game-nyt-original-vs-hard-mode.html

Hard Mode
    Can be turned on through the Settings menu at the top right of the screen.
    “Any revealed hints must be used in subsequent guesses” it says.
    If you guess a “present” (yellow) letter,
    that letter must be used on all subsequent guesses.
    If you guess a “correct” (green) letter, such as ``3:T``,
    that letter must played in that position on all the remaining guesses.

    When you post your results,
    the ``N/6`` score will be suffixed with a star, ``*``.

    | Wordle 1,317 4/6*
    | ⬜⬜⬜🟨⬜
    | 🟩⬜🟨⬜⬜
    | 🟩🟩⬜⬜🟩
    | 🟩🟩🟩🟩🟩

Normal Mode
    If you've never turned on Hard Mode,
    then you're playing Normal Mode.
    You can play any letter at any time.
    You are not required to play all the present and correct letters
    from previous guesses.

    This post will explore why this might be useful.

Many people play hard mode rules, without realizing it.
They instinctively apply all the constraints that they've learned from earlier guesses.

Slate_ has a discussion of the merits of Hard Mode and Normal Mode.

An example of Normal Mode being helpful
=======================================

.. figure:: /content/binary/olive-frame-stare.png
    :alt: Game 1285: OLIVE=....E FRAME=.rA.E STARE=S.ARE
    :width: 400

    `Wordle Game 1285`_

``S.ARE`` could be ``SCARE``, ``SHARE``, ``SNARE``, or ``SPARE``.
In Hard Mode, you would have no choice
but to try those four choices in some order,
and hope that you got the right one before running out of guesses.
Three guesses have already been played and three remain.

Each of the following outcomes are possible:

* getting the correct answer on your fourth guess
* on your fifth guess
* on your sixth guess
* losing the game if the correct word was last in your list.

In Normal Mode however,
you can guess a word that contains the four differing letters,
``C``, ``H``, ``N``, and ``P``,
and pin down the answer.
``PUNCH`` and ``PINCH`` are both suitable words.
You can't possibly win with ``PUNCH``, but your next guess is guaranteed to win.
In this case, I got ``PUNCH=....h``,
so I played ``SHARE`` as my fifth guess.

.. _Exploring Wordle:
    /blog/2023/09/26/ExploringWordle.html
.. _Wordle:
    https://en.wikipedia.org/wiki/Wordle
.. _June 2025 PuPPy meetup:
    https://www.meetup.com/psppython/events/307728743/
.. _Slate:
    https://slate.com/culture/2022/02/wordle-game-nyt-original-vs-hard-mode.html
.. _Wordle Game 1285:
    https://wordlearchive.com/1285
.. _Wordle Game 1310:
    https://wordlearchive.com/1310

.. raw:: html

   <link rel="stylesheet" href="/wordle.css">
