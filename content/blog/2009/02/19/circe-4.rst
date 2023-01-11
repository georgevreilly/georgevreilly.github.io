---
title: "Dramaturgy: Vim"
date: "2009-02-19"
permalink: "/blog/2009/02/19/DramaturgyVim.html"
tags: [tech, vim, jamesjoyce, LaTeX, dramaturgy]
---



.. image:: /content/binary/bloom-anointed-pdf.png 
    :alt: Bloomsday reading
    :target: http://www.wildgeeseseattle.org/

So how do I go from the `Project Gutenberg etext`_ to `LaTeX`_?

Here's the Gutenberg text for the pictured fragment::

    (BLOOM'S WEATHER. A SUNBURST APPEARS IN THE NORTHWEST.)

    THE BISHOP OF DOWN AND CONNOR: I here present your undoubted emperor-
    president and king-chairman, the most serene and potent and very puissant
    ruler of this realm. God save Leopold the First!

    ALL: God save Leopold the First!

    BLOOM: (IN DALMATIC AND PURPLE MANTLE, TO THE BISHOP OF DOWN AND CONNOR,
    WITH DIGNITY) Thanks, somewhat eminent sir.

    WILLIAM, ARCHBISHOP OF ARMAGH: (IN PURPLE STOCK AND SHOVEL HAT) Will you
    to your power cause law and mercy to be executed in all your judgments in
    Ireland and territories thereunto belonging?

    BLOOM: (PLACING HIS RIGHT HAND ON HIS TESTICLES, SWEARS) So may the
    Creator deal with me. All this I promise to do.

    MICHAEL, ARCHBISHOP OF ARMAGH: (POURS A CRUSE OF HAIROIL OVER BLOOM'S
    HEAD) GAUDIUM MAGNUM ANNUNTIO VOBIS. HABEMUS CARNEFICEM. Leopold,
    Patrick, Andrew, David, George, be thou anointed!

The Gutenberg transcriber has converted all italics to uppercase.
All accents on letters have been lost (there were none in this fragment).

Here's the corresponding LaTeX that I derived from the above:

.. code-block:: latex

    \stage{(Bloom's weather.
    A sunburst appears in the northwest.)}

    \DownConnor:
    \gab{1470}
    I here present your undoubted emperor-president and king-chairman,
    the most serene and potent and very puissant ruler of this realm.
    God save Leopold the First!

    \All:
    God save Leopold the First!

    \Bloom:
    \stage{(in dalmatic and purple mantle,
    to the bishop of Down and Connor, with dignity)}
    Thanks, somewhat eminent sir.

    \WillArmagh:
    \stage{(in purple stock and shovel hat)}
    \gab{1480}
    Will you to your power cause law and mercy to be executed
    in all your judgments in Ireland and territories thereunto belonging?

    \Bloom:
    \stage{(placing his right hand on his testicles, swears)}
    So may the Creator deal with me.
    All this I promise to do.

    \MikeArmagh:
    \stage{(pours a cruse of hairoil over Bloom's head)}
    \latin{Gaudium magnum annuntio vobis.
    Habemus carneficem.}
    Leopold, Patrick, Andrew, David, George, be thou anointed!

I could simply have used ``\em`` to get italics,
but I'm a big believer in semantic markup,
so I wrote a set of custom macros,
like ``\stage`` and ``\latin``.
The name macros, like ``\Bloom`` and ``\All``,
are defined in terms of the ``\role`` macro.
The ``\gab`` macro lists the line number
in the Gabler edition of *Ulysses*.
It's useful for looking up reference works
and it would have been hard to do in reStructuredText. :

.. code-block:: latex

    \newcommand{\stage}[1]{\emph{#1}}
    \newcommand{\role}[1]{{\textsc{#1}}}
    \newcommand{\Bloom}{\role{Bloom}}
    \newcommand{\gab}[1]{\marginpar{#1}}

I used Vim to massage the text.

* For my own sanity, I have broken each clause onto a separate line.
  Much of this can be done by substituting a newline
  after every period and right parenthesis.
  The other breaks require manual splitting and joining of lines.
* Transforming ``BLOOM:`` into ``\Bloom:`` is a trivial text substitution,
  ``:%s/^BLOOM: /\\Bloom:\r/``
* All the uppercase text has been converted to mixed case.
  Much of it needs to be bracketed by ``\stage{}`` in this chapter.
  The rest needs to be treated as ``\latin{}``, ``\hebrew{}``, ``\french{}``,
  and so on.

I used the following Vim macro to bracket the `visual selection`_
with ``\stage{}``. :

.. code-block:: vim

    " ;s => SELECTION -> \stage{selection}
    vnoremap <buffer> <silent> ;s u`>a}<Esc>`<i\stage{<Esc>

Breaking it down, since that looks like line noise.

==============  ================================
vnoremap        Visual-mode keymap; no further expansion of the right-hand side
<buffer>        Buffer-local. Won't apply in other buffers.
<silent>        Mapping won't be echoed on the Vim command line
;s              Mapping is bound to sequence ``;s``
u               Make highlighted text lowercase; cancels selection
\`>             Go to end of former visual selection
a}<Esc>         Append ``}``
\`<             Go to beginning of former visual selection
i\\stage{<Esc>  Insert ``\stage{``
==============  ================================

It's necessary to append to the end of the selection first.
Were I to first insert at the beginning,
the append would happen seven characters (``len('\stage{')``) too early.
(I picked this trick up from Christian Robinson's `HTML macros`_.)
Then I have to go back and convert a few characters to uppercase
with the ``~`` operator.

This workflow isn't for everyone and it would be difficult
if I had to hand it off to someone else.
Most non-geeks would prefer to use a WYSIWYG tool like Word.
I loathe Word and I want the control.

All of this is somewhat tedious,
since even with useful Vim macros taking care of many of the changes,
I still have to make manual tweaks on almost every line.
But this is also a virtue,
as it makes me intimately familiar with the text.

The hardest task—at least for me—is making the dramaturgical decisions.
Usually, it can be hard to decide exactly to whom
a particular line should be ascribed—making
sense of Bloom's interior monologue, for example,
or splitting a long stretch of narrative between several narrators.
This year's chapter is written in the form of a play,
so that particular problem is gone.
Last year was the first time we abridged a chapter.
This year, we have to reduce 60,000 words to 15–20,000 words.
Whether that's by breaking the chapter into two or more readings,
or by deep, deep cuts, I have yet to decide.
And that's where the line-by-line familiarity is helpful.

.. _Project Gutenberg etext:
    http://www.gutenberg.org/etext/4300
.. _LaTeX:
    /blog/2009/02/18/DramaturgyLaTeX.html
.. _visual selection:
    http://jmcpherson.org/editing.html
.. _HTML macros:
    http://www.infynity.spodzone.com/vim/HTML/

.. _permalink:
    /blog/2009/02/19/DramaturgyVim.html
