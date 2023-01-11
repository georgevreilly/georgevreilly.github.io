---
title: "Exuberant Ctags and JavaScript"
date: "2009-03-23"
permalink: "/blog/2009/03/23/ExuberantCtagsAndJavaScript.html"
tags: [vim, javascript, regex, til]
---



.. image:: https://ctags.sourceforge.net/ctags.png
    :alt: Exuberant Ctags
    :target: http://ctags.sourceforge.net/
    :class: right-float

`Exuberant Ctags`_ is an essential complement to Vim:
it generates an index of symbol names (tags) for a set of source files.
In Vim, just place the cursor on a function name
and type ``C-]`` to go to its definition.

Ctags works well for most of the languages that I deal with,
but falls down badly on modern JavaScript.
Its built-in parser simply doesn't handle declarations like these:

.. sourcecode:: javascript

    Sizzle.selectors.filters.animated = function(elem) { // ...
    ajaxSetup: function( settings ) {

I came across Unbad_'s workaround earlier tonight.
His code didn't work for me, so I hacked on it until it did::

    --langdef=js
    --langmap=js:.js
    --regex-js=/([A-Za-z0-9._$]+)[ \t]*[:=][ \t]*\{/\1/,object/
    --regex-js=/([A-Za-z0-9._$()]+)[ \t]*[:=][ \t]*function[ \t]*\(/\1/,function/
    --regex-js=/function[ \t]+([A-Za-z0-9._$]+)[ \t]*\(([^)])\)/\1/,function/
    --regex-js=/([A-Za-z0-9._$]+)[ \t]*[:=][ \t]*\[/\1/,array/
    --regex-js=/([^= ]+)[ \t]*=[ \t]*[^"]'[^']*/\1/,string/
    --regex-js=/([^= ]+)[ \t]*=[ \t]*[^']"[^"]*/\1/,string/

Simply add the above to ``~/.ctags`` or ``$HOME/ctags.cnf``.

.. _Exuberant Ctags:
    http://ctags.sourceforge.net/
.. _Unbad:
    http://www.unbad.net/blog/ctags-and-relevant-support-for-javascript

.. _permalink:
    /blog/2009/03/23/ExuberantCtagsAndJavaScript.html
