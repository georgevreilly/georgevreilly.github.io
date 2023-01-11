---
title: "Passphrase Generators"
date: "2021-05-10"
permalink: "/blog/2021/05/10/PassphraseGenerators.html"
tags: [tech, security]
---



.. image:: https://imgs.xkcd.com/comics/password_strength.png
    :alt: Password Strength
    :target: https://xkcd.com/936/

I've been using `password managers`_ for at least 15 years
to keep track of all my passwords.
I have separate, distinct, strong passwords for hundreds of sites,
and I've only memorized the handful that I need to actually type regularly.

I started out with the KeePass_ desktop app originally,
but I switched to the online LastPass_ app about a decade ago.
At work, we use 1Password_.

When I register for a site,
LastPass generates a random password for me,
such as::

    tV%5joS$U6^uY5xU
    T2oEUY!g70Iv1b&I
    8kNHg9*A5GMR9%8D

LastPass securely syncs my passwords between machines and devices.
Its browser integration and its Android and iPhone apps
mean that I rarely ever have to actually type any of those ugly messes in.

But when I do have to type in such a password,
it's unpleasant in a browser.
It doesn't help that LastPass in some cases displays passwords
in a sans-serif font that makes it easy to misrecognize_ letters
such as ``Il``, ``0O``, ``5S``, or ``8B``.
It's far more painful in an Android app,
where you have to switch the keyboard in and out of symbol mode.
It's usually even worse in iPhone apps,
which rarely offer you an option to see your password in the clear
as you're laboriously typing it,
so it's easy to make a mistake.
When I tried to use a remote control
to enter my Netflix and Amazon Prime passwords into a new set-top box,
I got so annoyed that I brought down a real keyboard
and plugged it into the USB port.

Passphrases_ have nice properties compared to random passwords:
they're human readable,
they're much easier—if longer—to type,
and you can actually remember them if you have to.
A passphrase of at least five words (chosen by a secure random generator)
is computationally infeasible to crack.

The ur-example of random passphrase generators is Diceware_ from 1995.
There are various problems with the Diceware wordlist,
which are rectified by more modern lists,
such as the `EFF Wordlists`_.

Which would you rather type?
The `line noise`_ above or one of these passphrases?::

    confident starfish aftermost elsewhere jasmine
    shun baggage chaps reward cuddle
    avenue rut pardon skating earlobe
    latter blissful snippet jolt corroding
    upstage-divinely-ninth-unfilled-skeleton
    SkimmingMachinistBlessHesitancyKissableRink

When I want to generate a random passphrase,
I tend to use either the `Python diceware`_ command-line tool
or Glenn Rempe's JavaScript-based `Diceware website`_.
Both use cryptographic random number generators
to generate excellent passphrases.

The `1Password Online Generator`_ (in Memorable Password mode)
also generates passphrases,
as do the desktop and browser versions of 1Password.

My master password for LastPass is a passphrase,
as is my laptop password.
I'm also using Authy_ for 2FA, but that's a post for another time.

.. tip:: If you have to supply answers
    for one of those misbegotten `security questions`_,
    such as your favorite movie or your first car,
    *do not answer truthfully*.
    Truthful answers increase your risk of identity theft.
    The answers are often guessable,
    can frequently be learned easily about you,
    and may be obtained through a password breach on another site.

    Instead, generate a passphrase as the "answer"
    *and store it and the question
    in the Notes field of your password manager*.
    If you have to supply the answer to a security question
    over the phone to a customer service rep,
    you'll be thankful that you chose something
    that you can clearly say aloud.

    Also `Facebook quizzes`_ and memes like
    "Your porn name is your middle name and the first car you had"
    are trying to obtain your answers to common security questions.
    Don't answer them.

.. _password managers:
    https://en.wikipedia.org/wiki/Password_manager
.. _LastPass:
    /blog/2016/01/07/DicewareAndLastpass.html
.. _KeePass:
    /blog/2006/02/06/200KeePassEntries.html
.. _1Password:
    https://1password.com/
.. _misrecognize:
    https://typography.guru/journal/letters-symbols-misrecognition/
.. _Passphrases:
    https://theintercept.com/2015/03/26/passphrases-can-memorize-attackers-cant-guess/
.. _Diceware:
    https://en.wikipedia.org/wiki/Diceware
.. _EFF Wordlists:
    https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
.. _line noise:
    http://www.catb.org/jargon/html/L/line-noise.html
.. _1Password Online Generator:
    https://1password.com/password-generator/
.. _Python diceware:
    https://github.com/ulif/diceware
.. _Diceware website:
    https://www.rempe.us/diceware/#eff
.. _Authy:
    https://authy.com/
.. _security questions:
    https://www.okta.com/blog/2021/03/security-questions/
.. _Facebook quizzes:
    https://www.mentalfloss.com/article/522136/taking-facebook-quizzes-could-put-you-risk-identity-theft

.. _permalink:
    /blog/2021/05/10/PassphraseGenerators.html
