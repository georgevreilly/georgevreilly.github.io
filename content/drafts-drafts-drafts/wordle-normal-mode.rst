---
title: "Wordle on Normal Mode"
# date: "2025-01-26"
permalink: "/drafts-drafts-drafts/2025/01/dd/WordleOnNormalMode.html"
tags: [python, wordle]
draft: true
---
In `Exploring Wordle`_, I wrote a long blog post about solving Wordle programmatically,
which implicitly solved Wordle in *hard mode*.
Today, I want to explore different strategies that are possible with Wordle's two modes,
Normal and Hard.

.. image:: /content/binary/WordleHardMode.png
    :alt: Wordle Hard Mode setting
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

Example of Normal Mode being helpful
====================================

::

    * 1285: `OLIVE=....E FRAME=.rA.E STARE=S.ARE PUNCH=....h` yields `SHARE`

``S.ARE`` could be ``SCARE``, ``SHARE``, ``SNARE``, or ``SPARE``.
In Hard Mode, you would have no choice but to try those four choices in some order,
and hope that you got the right one before running out of guesses.
In Normal Mode, you can guess a word that contains the four differing letters,
``C``, ``H``, ``N``, and ``P``, such as ``PUNCH``,
and pin down the answer.
You can't possibly win with ``PUNCH``, but your next guess is guaranteed to win.

.. _Exploring Wordle:
    /blog/2023/09/26/ExploringWordle.html
.. _Wordle:
    https://en.wikipedia.org/wiki/Wordle
.. _Slate:
    https://slate.com/culture/2022/02/wordle-game-nyt-original-vs-hard-mode.html

.. raw:: html

   <link rel="stylesheet" href="/wordle.css">
