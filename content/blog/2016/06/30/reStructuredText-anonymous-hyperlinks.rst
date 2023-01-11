---
title: "reStructuredText Anonymous Hyperlinks"
date: "2016-06-30"
permalink: "/blog/2016/06/30/ReStructuredTextAnonymousHyperlinks.html"
tags: [reStructuredText, til]
---



While researching `yesterday's post`__ about nested markup in ReStructuredText,
I finally learned how to use `anonymous hyperlinks`__.

.. __: /blog/2016/06/29/reStructuredTextNestedMarkup.html
__ http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks

Hitherto, I used one of these three forms for hyperlinks:

.. code:: rst

    1. The central conceit of the fictional `Flashman Papers`_ is that Flashy
    2. besieging Breda_ in 1625.
    3. my club, `Freely Speaking Toastmasters <http://freelyspeaking.org/>`_.

    .. _Flashman Papers:
        https://en.wikipedia.org/wiki/The_Flashman_Papers
    .. _Breda: http://en.wikipedia.org/wiki/Siege_of_Breda

The first, :literal:`\`Flashman Papers\`_`, is a *named hyperlink reference*,
which refers to an *external hyperlink target*, :literal:`.. _Flashman Papers: URI`.
Note that the reference name starts with a backquote, :literal:`\``,
and ends with backquote-underscore, :literal:`\`_`. 

The second, :literal:`Breda_`, is a *simple reference name*\ —the backquotes are optional,
but the trailing ``_`` is crucial.

:literal:`\`Freely Speaking Toastmasters <http://freelyspeaking.org/>\`_`,
is an *embedded URI*.
The syntax is :literal:`\``, reference-name, :literal:`<`, URI, :literal:`>\``.

With anonymous hyperlinks,
the reference name does not need to be repeated in the hyperlink target.
Instead, the reference name ends with a double-underscore, ``__``,
and the target looks like either :literal:`.. __: URI` or :literal:`__ URI`.
The targets must appear in the order they are referenced.
It's best if they're close to the references in the text, for maintainability.

.. code:: rst

    researching `yesterday's post`__ about ...,
    I learned how to use `anonymous hyperlinks`__.

    .. __: /blog/2016/06/29/reStructuredTextNestedMarkup.html
    __ http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks

To handle escaping backquotes inside code literals for this post,
I used the `literal role`__ instead of double backquotes::

    The first, :literal:`\`Flashman Papers\`_`, is a *named hyperlink reference*
    Normally, I use double-backquotes to bracket code: ``a += b & c[i]``.

__ http://docutils.sourceforge.net/docs/ref/rst/roles.html#literal

.. _permalink:
    /blog/2016/06/30/ReStructuredTextAnonymousHyperlinks.html
