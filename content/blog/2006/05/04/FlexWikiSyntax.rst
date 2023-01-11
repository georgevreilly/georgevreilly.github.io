---
title: "Vim Syntax Highlighting for FlexWiki"
date: "2006-05-04"
permalink: "/blog/2006/05/04/VimSyntaxHighlightingForFlexWiki.html"
tags: [vim, til]
---



We use `FlexWiki <http://www.flexwiki.com/>`_ at work. It's an
ASP.NET-based `wiki <http://wiki.org/wiki.cgi?WhatIsWiki>`_,
a low-overhead, organic way of sharing knowledge.

.. image:: /vim/flexwiki/plugin.jpg
    :alt: Vim Syntax Highlighting for FlexWiki

The only built-in means of editing a page in FlexWiki is to
type into an HTML textbox, which is a horrendous user experience.
There's no WYSIWYG feedback showing you whether you've got the wiki markup
right.

Back in December, Emma and I went to the Oregon coast for a week.
We had no Internet access and long dark evenings, so I spent quite a bit of
time on my laptop, working on a couple of projects. One was a new theme
(skin) for DasBlog, which I didn't finish to my satisfaction. I really
ought to get back to that.

The other was Vim syntax highlighting for FlexWiki, partially because it's
useful in its own right, partially because I wanted an excuse to learn the
arcane syntax highlighting mechanism in Vim.

As you can see in the picture, syntax highlighting makes the wiki markup a
lot clearer than it would be in black-and-white.

I got it working satisfactorily in December, but I didn't get around to
releasing it on the `Vim scripts repository <http://www.vim.org/scripts/>`_
until last week. The week before, Bram had issued a final call for
submissions of scripts for Vim\-7.0, which galvanized me into releasing it
as the `FlexWiki Plugin for Vim <http://www.georgevreilly.com/vim/flexwiki/>`_.

Bram has included it in the most recent beta, Vim\-7.0g, after I made a few
changes. Those changes have not yet been propagated into the
`standalone version <http://www.georgevreilly.com/vim/flexwiki/>`_,
but I'll try to do that later this week.

.. _permalink:
    /blog/2006/05/04/VimSyntaxHighlightingForFlexWiki.html
