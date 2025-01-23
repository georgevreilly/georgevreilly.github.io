---
title: "George's reStructuredText cheat sheet"
# date: "2025-mm-dd"
permalink: "/drafts-drafts-drafts/GeorgesReStructuredTextCheatSheet.html"
tags: [reStructuredText]
draft: true
---


.. image:: /content/binary/How-to-eat-a-Slug.jpg
    :alt: How to eat a Slug
    :target: http://www.backuptrauma.com/video/default2.aspx
    :class: right-float

1. Code:
   ``terminate="yes"``
2. *italics*
3. **bold**
4. Nbsp: G.V. Reilly
5. Deferred link: `Master and Commander`_
6. Amazon: `A Storm of Swords
   <https://www.amazon.com/exec/obidos/ASIN/055357342X/georgvreill-20>`_
7. `Anonymous link`__ to Vim scripting

.. _Master and Commander: http://www.masterandcommanderthefarsideoftheworld.com/
__ http://www.ibm.com/developerworks/linux/library/l-vim-script-1/index.html


Letters::

      !"#$%&'()*+,-./0123456789:;<=>?
     @ABCDEFGHIJKLMNOPQRSTUVWXYZ[/]^_
     'abcdefghijklmnopqrstuvwxyz{|}~

=============================   ====================    =======================
``Regular ASCII``               *Italics*               **Bold**
=============================   ====================    =======================
:literal:`\ !"#$%&'()*+,-./`    *\ !"#$%&'()*+,-./*     **\ !"#$%&'()*+,-./**
:literal:`0123456789:;<=>?`     *0123456789:;<=>?*      **0123456789:;<=>?**
:literal:`@ABCDEFGHIJKLMNO`     *@ABCDEFGHIJKLMNO*      **@ABCDEFGHIJKLMNO**
:literal:`PQRSTUVWXYZ[\\]^_`    *PQRSTUVWXYZ[\\]^_*     **PQRSTUVWXYZ[\\]^_**
:literal:`\`abcdefghijklmno`    *\`abcdefghijklmno*     **\`abcdefghijklmno**
:literal:`pqrstuvwxyz{|}~`      *pqrstuvwxyz{|}~*       **pqrstuvwxyz{|}~**
=============================   ====================    =======================

*****************
Five-column table
*****************

======  ==  ========================    ===========  ===============
Hex     Ch  Name                        HTML         Vim Digraph
======  ==  ========================    ===========  ===============
  x60   \`  grave accent                &#96;        :literal:`\``
  xB4   \´  acute accent                &#180;       ``''``
  xA0   \   non-breaking space          &nbsp;       ``NS``
  xBC   ¼   one quarter                 &frac14;     ``14``
  xBD   ½   one half                    &frac12;     ``12``
  xBE   ¾   three quarters              &frac34;     ``34``
  xB9   ¹   superscript one             &sup1;       ``1S``
  xB2   ²   superscript two             &sup2;       ``2S``
u2080   ₁   subscript one               &#x2081;     ``1s``
u2081   ₂   subscript two               &#x2082;     ``2s``
  x2D   -   minus                       -            ``-``
u2013   –   en dash                     &ndash;      ``-N``
u2014   —   em dash                     &mdash;      ``-M``
  x27   '   apostrophe                  &#39;        ``'``
u2018   ‘   left single quote           &lsquo;      ``'6``
u2019   ’   right single quote          &rsquo;      ``'9``
u201A   ‚   single low-9 quote          &sbquo;      ``.9``
  x22   "   double quote                &#34;        ``"``
u201C   “   left double quote           &ldquo;      ``"6``
u201D   ”   right double quote          &rdquo;      ``"9``
u201E   „   double low-9 quote          &bdquo;      ``:9``
  xAB   «   double guillemet left       &laquo;      ``<<``
  xBB   »   double guillemet right      &raquo;      ``>>``
u2039   ‹   single guillemet left       &lsaquo;     ``<1``
u203A   ›   single guillemet right      &rsaquo;     ``>1``
u2026   …   horizontal ellipsis         &hellip;     ``,.``
u21A9   ↩   left arrow with hook        &#x21a9;     <none>
u278A   ➊   neg circled digit 1         &#x278a;     <none>
u2793   ➓   neg circled digit 10        &#x2793;     <none>
  xB0   °   degree                      &deg;        ``DG``
u2318   ⌘   clover                      &#8984;      <none>
u2325   ⌥   option                      &#8997;      <none>
u21e7   ⇧   shift                       &#8679;      <none>
u2303   ⌃   control                     &#8963;      <none>
======  ==  ========================    ===========  ===============


Dingbats
========

| negative circled sans serif:  ➊ ➋ ➌ ➍ ➎ ➏ ➐ ➑ ➒ ➓   dingbat negative circled sans-serif digit
|          circled sans serif:  ➀ ➁ ➂ ➃ ➄ ➅ ➆ ➇ ➈ ➉   dingbat circled sans-serif digit
| negative circled digits:    ⓿ ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿   dingbat negative circled digit
|          circled digit:     ⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ 
|          circled number     ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ 
| superscripts:               ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹
| subscripts:                 ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉

.. |---| unicode:: U+02014 .. em dash
   :trim:

Replacements |---| such as the em-dash |---| are used like this.
Here’s a ‘literal’ em-dash—or emdash—character.
And here’s the “endash”, 2–3000.


Replacement Text: I recommend you try |Python|_.

.. |Python| replace:: Python, *the* best language around
.. _Python: http://www.python.org/

Image substitution: The |biohazard| symbol must be used on containers
used to dispose of medical waste.

.. |biohazard| image:: https://docutils.sourceforge.net/docs/user/rst/images/biohazard.png

If you've set up |~/.pgpass|_, you can specify ``--no-password`` instead.

.. |~/.pgpass| replace:: ``~/.pgpass``
.. _~/.pgpass:
    https://blog.sleeplessbeastie.eu/2014/03/23/how-to-non-interactively-provide-password-for-the-postgresql-interactive-terminal/

.. _Format text in a link in reStructuredText:
    http://stackoverflow.com/a/4836544/6364

Use the `literal role`__ instead of double backquotes
to get inline literal backquotes:
e.g., triple backticks, :literal:`\`\`\``.

Don't forget `anonymous hyperlinks`__.

__ http://docutils.sourceforge.net/docs/ref/rst/roles.html#literal
.. __: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks


.. raw:: html

    <a href="/content/binary/AndaleConsoleFont.jpg" title="Click on screenshot to enlarge">
         <img src="/content/binary/AndaleConsoleFont.jpg"
              style="margin: 0pt 0pt 0pt 15px;" align="right" width="300" />
    </a>

The registry file includes entries for:

* `Andale Mono <http://corefonts.sourceforge.net/>`_
* `Consolas <http://www.poynter.org/column.asp?id=47&aid=78683>`_
* and more.

#. auto-enumerated
#. lists are handy too

    ‣ as are
    ‣ nested
      bullet
    ‣ lists

#. as you can see.

Container Directive
===================

.. container:: my-custom

    Bob Howard is a computational demonologist working for the secretive British agency
    known as the “Laundry”.

    Some very nasty people are trying to hasten the end of the world,
    there's a mole in the Laundry,
    and Bob's superior, the mysteriously ageless Angleton, is missing.
   
Definition Lists
==================

what
  Definition lists associate a term with a definition.

*how*
  The term is a one-line phrase, and the definition is one or more
  paragraphs or body elements, indented relative to the term.
  Blank lines are not allowed between term and definition.

Preformatted block: Inserting a ``<script>`` node requires::

    var scr = document.createElement('script');
    scr.type = 'text/javascript';

The ``code-block`` directive for Vim:

.. code-block:: vim

    syn match rstEnumeratedList /^\s*[0-9#]\{1,3}\.\s\@=/
    syn match rstBulletedList /^\s*[+*-]\s\@=/
    syn match rstNbsp /[\xA0]/
    syn match rstEmDash /[\u2014]/
    syn match rstUnicode /[\u2013\u2018\u2019\u201C\u201D]/ " – ‘ ’ “ ”

    exec 'hi def rstBold    term=bold cterm=bold gui=bold guifg=' . s:SynFgColor('PreProc')
    exec 'hi def rstItalic  term=italic cterm=italic gui=italic guifg=' . s:SynFgColor('Statement')
    exec 'hi def rstNbsp    gui=underline guibg=' . s:SynBgColor('ErrorMsg')
    exec 'hi def rstEmDash  gui=bold guifg=' . s:SynFgColor('Title') . ' guibg='. s:SynBgColor('Folded')
    exec 'hi def rstUnicode guifg=' . s:SynFgColor('Number')

And this is ``raw:: html``:

.. raw:: html

    <div align="center">
    <object width="425" height="350">
        <param name="movie" value="http://www.youtube.com/v/kB48J_0re2g"></param>
        <param name="wmode" value="transparent"></param>
        <embed src="http://www.youtube.com/v/kB48J_0re2g" 
            type="application/x-shockwave-flash" wmode="transparent" 
            width="425" height="350"></embed>
    </object><br/>
    Andrew Sullivan and Christopher Hitchens on CNN
    </div>

Attributed quote:

    "This isn't an election anymore, it's an intervention."

    — Andrew Sullivan on CNN.

watched the `CNBC Video`_ that started the meme.
Funny stuff. Go watch the `original video`_.

.. _CNBC Video:
.. _original video: http://www.youtube.com/watch?v=2Y_Jp6PxsSQ

Inline link, `Highland Shepherd site <http://www.msgr.ca/msgr-2/christmas_countdown.htm>`_.
