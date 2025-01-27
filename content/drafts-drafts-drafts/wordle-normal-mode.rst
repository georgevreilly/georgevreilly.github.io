---
title: "Wordle on Normal Mode"
# date: "2025-01-26"
permalink: "/drafts-drafts-drafts/2025/01/dd/WordleOnNormalMode.html"
tags: [python, wordle]
draft: true
---
In `Exploring Wordle`_, I wrote a long blog post about solving Wordle programmatically,
which implicitly solved Wordle in *hard mode*.
I want to explore different strategies that are possible with Wordle's two modes,
Normal and Hard.

.. image:: /content/binary/WordleHardMode.png
    :alt: Wordle Hard Mode setting
    :target: https://slate.com/culture/2022/02/wordle-game-nyt-original-vs-hard-mode.html

Hard Mode
    Can be turned on through the Settings menu at the top right of the screen.
    “Any revealed hints must be used in subsequent guesses” it says.
    If you guess a “present” (yellow) letter, say ``V``,
    that letter must be used on all subsequent guesses.
    If you guess a “correct” (green) letter, say ``3:T`` 
    that letter must played in that position on all the remaining guesses.

    When you post your results, the score will be suffixed with a star, ``*``.

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

Many people do 


.. _Exploring Wordle:
    /blog/2023/09/26/ExploringWordle.html
.. _Wordle:
    https://en.wikipedia.org/wiki/Wordle
.. _Slate:
    https://slate.com/culture/2022/02/wordle-game-nyt-original-vs-hard-mode.html

.. raw:: html

   <link rel="stylesheet" href="/wordle.css">
