---
title: "20 Years of Vi"
date: "2005-12-30"
permalink: "/blog/2005/12/30/20YearsOfVi.html"
tags: [vim]
---


`vi`_.
Vee-eye. My text editor of choice for 20 years. Half my life.

Why? Because I
`imprinted <http://en.wikipedia.org/wiki/Filial_imprinting>`_
on vi, like a duckling on its mother.
Vi's keystrokes are bound into my
`muscle memory <http://en.wikipedia.org/wiki/Muscle_memory>`_.
My fingers reflexively use vi keystrokes to move around,
to delete text, to move blocks, to find patterns.
I don't have to think about using ``dw`` to delete a word,
or ``n`` to find the next match of a pattern,
or ``yG`` to yank the rest of a file,
or ``j`` to move down a line,
or ``.`` to repeat the last modification.
My subconcious does it for me.

I don't even have to think much about more complex commands,
like ``ct)`` to replace a parameter list,
or simpler regexp replacements.
I've internalized so many vi idioms in the last two decades.

For nearly all editing tasks, I'm far more productive when I use vi.
Like `Tom Christiansen
<http://www.oreilly.com/news/zenclavier_1299.html>`_,
I can become at one with the machine.

People who've used `vi`_
fall into a bimodal distribution.
They love it or they hate it.
Usually, it's because of vi's
`modal <http://en.wikipedia.org/wiki/Mode_%28computer_interface%29>`_
nature.
I love the `orthogonality
<http://www.ultrasaurus.com/sarahblog/archives/2005_06.html>`_
of the UI.

20 years
========

In the autumn of 1985, I entered my third year
of `Computer Science at Trinity <http://www.cs.tcd.ie/>`_.
We were promoted from three hours a day on the 1200-baud terminals
in the basement to all-day usage of the 9600-baud terminals in the
main terminal room.
We also graduated from the wretched
`SOS <http://www.inwap.com/pdp10/jargon.html#SOS>`_ line editor
to vi running on `Eunice <http://en.wikipedia.org/wiki/Eunice_%28software%29>`_
(a Unix emulator for VAX/VMS).
I don't think I took to vi instantly;
it took a little while for it to grow on me.
Soon enough, though, I was hooked on
`regexps <http://catb.org/~esr/jargon/html/R/regexp.html>`_.

Hitting ESC quickly became a habit:
one that causes me occasional grief,
when I reflexively hit ESC after entering text in an edit field
in some app or other, and destroy what I've just written.

Two years later, I got my first fulltime job,
writing a full-screen text editor for a small Irish typesetting company,
`ICPC <http://www.icpc.ie/>`_. It was a replacement for the in-house
line-based editor used by the data entry keyboaders,
which I wrote in Vax Pascal.
A friend made me aware of
`VITPU <http://www.google.com/search?q=gregg+wonderly+vitpu>`_,
a Vi emulator written in VMS's TPU,
which I gladly latched onto.

Two years after that, I entered the Master's program at
`Brown <http://www.cs.brown.edu/>`_,
where I first got to use Unix and X Windows.
Naturally, I used vi, but it was a lot less powerful than
GNU Emacs, which was very popular.
In time, I learned of VIP, a vi emulator for Emacs.
I began using VIP and quickly forsook standard vi.
I liked having the power and customizability of Emacs,
though I never learned to like the Emacs keybindings.
(François Pinard, a longtime Emacs user, writes eloquently of why he
`moved to Vim <http://pinard.progiciels-bpi.ca/opinions/editors.html>`_.)

I stayed with VIP for years, as it evolved into
`Viper <http://www.cs.sunysb.edu/~kifer/emacs.html>`_.
I show up in the `Viper credits <http://www.delorie.com/gnu/docs/emacs/viper_49.html>`_
for occasional contributions.

In 1992, I moved to Seattle and worked for Microsoft for the first time.
I kept my Emacs+Viper habit.

Vim
===

By 1995, I was working for MicroCrafts and had discovered
`Vim <https://www.vim.org/>`_. Version\-3.x ran on DOS as a 16-bit
command-line app. I used it occasionally on NT. Then I discovered that
Roger Knobbe had ported Vim to NT, but that it was pretty buggy.
I `fixed the bugs <https://groups.google.com/g/comp.editors/c/o_rZRV16I88/m/cVecdHH7-CUJ>`_
and submitted my fixes to 
`Bram Moolenaar <https://www.moolenaar.net/>`_, Vim's author.

One thing led to another, and I became the Win32 guy for Vim\-4.x.
Console-mode Vim became rock solid on NT 4, but I never got it to the same
level on Win95, due to inherent problems in the console APIs on Win9x.
I also put together a proof-of-concept implementation of gvim\-5.0 for Windows.
At that point, I gave up active involvement in the development of Vim:
I had moved back to Microsoft, I was starting to date Emma,
and I was working on the 
`Beginning ATL COM Programming book
<https://web.archive.org/web/20060815204548/http://george.reilly.org/BegAtlCom.html>`_.
Something had to give.

I continued using Viper for much of the time that I was developing Vim,
because Vim was not then rich enough for my needs.
After Vim got a scripting language (VimL) and syntax highlighting in
version\-5, I started using Vim more and more.
I think it's been five years since I last used Emacs,
and I never got beyond GNU Emacs\-19.34.

Recently, I've stopped using Vim as my exclusive programming editor,
and I've been alternating between Vim and Visual Studio plus 
`Resharper <http://www.jetbrains.com/resharper/>`_,
as I've started doing a lot of .NET development.
But more on that some other time. This post is already too long.

.. _vi:
    https://en.wikipedia.org/wiki/Vi

.. _permalink:
    /blog/2005/12/30/20YearsOfVi.html
