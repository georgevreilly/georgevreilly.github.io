---
title: "reStructuredText syntax highlighting"
date: "2009-03-07"
permalink: "/blog/2009/03/07/reStructuredTextSyntaxHighlighting.html"
tags: [reStructuredText, vim, til]
---



.. image:: /content/binary/rst-syntax-dash.png
    :alt: reStructuredText syntax highlighting

Vim has had `syntax highlighting`_ since version 5.0 in 1998.
It quickly became indispensable.
It's hard to go back to looking at monochromatic source code
after you've become accustomed to syntax highlighting.

The syntax highlighting is tied into Vim's support for colorschemes,
which define colors for the fundamental syntax groups
like ``Number``, ``Comment``, and ``String``.
The syntax highlighting for a particular language
defines custom syntax groups for specific language features,
such as ``cppExceptions`` or ``htmlEndTag``,

The custom syntax groups are *linked* to the underlying fundamental syntax groups.
Hence, if you change your colorscheme, your syntax highlighting is updated automatically.

The reStructuredText syntax highlighting in Vim 7.2
has some shortcomings, in my opinion.
For example, ``*italic*`` shows up as *italic* in gVim,
but in the same color as regular text,
while ``**bold**`` shows up in a different color, but not bolded.

When you declare a syntax group,
you can either link it to another gropu and pick up that's one color and fontstyle,
or you can give it a concrete fontstyle and color.
If you do that, then the syntax group
won't change color when you change the colorscheme.

After much poking around, I found a way to set a syntax group's
fontstyle *and* link it to another group's color:
see ``hi def rstItalic`` and ``hi def rstBold`` below.

I also make use of certain Unicode characters in my reStructuredText source,
such as endash and emdash,
which are very hard to tell apart in a fixed-width font—\
even though an emdash (—) is twice as wide as an endash (–) in a proportional font.
Worse, a non-breaking space is invisible and
can't easily be distinguished from a normal space.

I provided custom highlighting for these Unicode characters
and the various ‘curly’ “quotes”.

All of this goes into ``~/.vim/syntax/rst.vim``,
which treats ``$VIMRUNTIME/syntax/rst.vim`` as a subroutine.
I tried putting it into ``~/.vim/after/syntax/rst.vim``,
which gets executed after ``$VIMRUNTIME/syntax/rst.vim`` completes,
but then I can't provide non-overrideable definitions for
``rstEmphasis`` and ``rstStrongEmphasis``.


.. _syntax highlighting:
    http://vimdoc.sourceforge.net/htmldoc/syntax.html
.. _reStructuredText:
    /blog/2008/11/24/reStructuredText.html


.. code:: vim

    function! s:SynFgColor(hlgrp)
        return synIDattr(synIDtrans(hlID(a:hlgrp)), 'fg')
    endfun

    function! s:SynBgColor(hlgrp)
        return synIDattr(synIDtrans(hlID(a:hlgrp)), 'bg')
    endfun

    syn match rstEnumeratedList /^\s*[0-9#]\{1,3}\.\s/
    syn match rstBulletedList /^\s*[+*-]\s/
    syn match rstNbsp /[\xA0]/
    syn match rstEmDash /[\u2014]/
    syn match rstUnicode /[\u2013\u2018\u2019\u201C\u201D]/ " – ‘ ’ “ ”

    exec 'hi def rstBold    term=bold cterm=bold gui=bold guifg=' . s:SynFgColor('PreProc')
    exec 'hi def rstItalic  term=italic cterm=italic gui=italic guifg=' . s:SynFgColor('Statement')
    exec 'hi def rstNbsp    gui=underline guibg=' . s:SynBgColor('ErrorMsg')
    exec 'hi def rstEmDash  gui=bold guifg=' . s:SynFgColor('Title') . ' guibg='. s:SynBgColor('Folded')
    exec 'hi def rstUnicode guifg=' . s:SynFgColor('Number')

    hi link rstEmphasis       rstItalic
    hi link rstStrongEmphasis rstBold
    hi link rstEnumeratedList Operator
    hi link rstBulletedList   Operator

    source $VIMRUNTIME/syntax/rst.vim

    syn cluster rstCruft                contains=rstEmphasis,rstStrongEmphasis,
          \ rstInterpretedText,rstInlineLiteral,rstSubstitutionReference,
          \ rstInlineInternalTargets,rstFootnoteReference,rstHyperlinkReference,
          \ rstNbsp,rstEmDash,rstUnicode

.. _permalink:
    /blog/2009/03/07/reStructuredTextSyntaxHighlighting.html
