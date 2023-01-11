---
title: "URLs from Unicode Strings"
date: "2016-01-31"
permalink: "/blog/2016/01/31/URLsFromUnicodeStrings.html"
tags: [unicode, urls, metabrite, til]
---



\ 

    [Previously published at the now defunct `MetaBrite Dev Blog`_.]

Some time ago,
we made an ill-considered decision to use recipe names for image URLs,
which simplified image management with our then-rudimentary tools.
For example, the recipe named
``"Twisted Pasta With Browned Butter, Sage, and Walnuts"``
becomes a URL ending in
``"Twisted%20Pasta%20With%20Browned%20Butter%2C%20Sage%2C%20and%20Walnuts.jpg"``.

Life becomes more interesting when you escape the confines of 7-bit ASCII and use Unicode.
How should ``u"Sautéed crème fraîche Provençale"`` be handled?
The only reasonable thing to do is to first convert the Unicode string to UTF-8
and then hex-encode those octets:
``"Saut%C3%A9ed%20cr%C3%A8me%20fra%C3%AEche%20Proven%C3%A7ale"``.

That seems reasonable, but it was giving us inconsistent results
when the images were uploaded to an S3 bucket.
When I investigated, I discovered that it was a problem of `Unicode equivalence`_.
There are two ways to represent,
say, the *e-acute* character in Unicode:
as a composed character,
``é`` = 'LATIN SMALL LETTER E WITH ACUTE' ``(U+00E9)``,
or as a decomposed pair,
``e´`` = 'LATIN SMALL LETTER E' ``(U+0065)`` and 'COMBINING ACUTE ACCENT' ``(U+0301)``.
Thus the name of our fictitious recipe can be represented as
``u"Saut\u00E9ed cr\u00E8me fra\u00EEche Proven\u00E7ale"`` (composed, NFC) *or*
``u"Saute\u0301ed cre\u0300me frai\u0302che Provenc\u0327ale"`` (decomposed, NFD).

======  ========    ======      =============   =========
Letter  Composed    UTF-8       Decomposed      UTF-8
======  ========    ======      =============   =========
``é``   U+00E9      C3 A9       U+0065 U+0301   65 CC 81
``è``   U+00E8      C3 A8       U+0065 U+0300   65 CC 80
``î``   U+00EE      C3 AE       U+0069 U+0302   69 CC 82
``ç``   U+00E7      C3 A7       U+0063 U+0327   63 CC A7
======  ========    ======      =============   =========

When we uploaded our image files to S3 from a Mac,
accented letters were decomposed letter–accent pairs,
while images uploaded from Linux had composed characters in their S3 key names.
This discrepancy was due to the Mac HFS+ filesystem,
which stores filenames in decomposed form.
(Linus Torvalds has a profane `rant about HFS+`_.)
Our client apps always used the composed form of the recipe name
and generated image URLs accordingly.
This led to 404s for recipe images that had been uploaded from a Mac.
If S3 had handled the Unicode equivalence, we'd never have noticed.

We're switching to using numeric identifiers for the recipe images—\
they're much harder to get wrong.

.. _MetaBrite Dev Blog:
    https://web.archive.org/web/20171001220321/http://devblog.metabrite.com/
.. _Unicode equivalence:
    https://en.wikipedia.org/wiki/Unicode_equivalence
.. _rant about HFS+:
    https://archive.ph/VaX6k

.. _permalink:
    /blog/2016/01/31/URLsFromUnicodeStrings.html
