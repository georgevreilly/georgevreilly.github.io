---
title: "Homograph Attacks"
date: "2016-08-26"
permalink: "/blog/2016/08/26/HomographAttacks.html"
tags: [security, unicode, til]
---



During an internal training exercise today,
as a sort of one-man `Chaos Monkey`__,
I deliberately broke a test system by changing a config setting to read::

    itemfinder.url = http://test-іtemfinder.example.com/

The correct value should have been::

    itemfinder.url = http://test-itemfinder.example.com/

What's that, you say? There's no difference, you say?

There *is* a difference, but it's subtle.
The first ``i`` in the URL is
`'CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I' (U+0456)`__,
not `'LATIN SMALL LETTER I' (U+0069)`__.
Depending upon the font, the two ``i``\ s may be visually indistinguishable,
very similar looking, or the Cyrillic ``i`` may not render.

This is an example of an `International Domain Name Homograph Attack`__.
There are Greek letters and Cyrillic letters that look very similar to Latin letters,
but which have distinct meanings, histories, and code points.
International Domain Names permit the construction of non-Latin domain names.

Since domain name labels may only contain Latin letters, digits, and hyphens,
an encoding scheme known as `Punycode`__ transforms Unicode domain names into ASCII domain names.
For example, ``test-іtemfinder.example.com`` (Cyrillic ``i``)
becomes ``xn--test-temfinder-99l.example.com`` in Punycode.

Obviously, homographs can be used to spoof URLs.
Browsers generally present the Punycode form of an IDN
if it looks like suspicious homographs might be present in the address bar,
while presenting valid IDNs in Unicode; e.g., ``http://ουτοπία.δπθ.gr/``.

__ https://github.com/Netflix/SimianArmy/wiki/Chaos-Monkey
__ http://www.fileformat.info/info/unicode/char/0456/index.htm
__ http://www.fileformat.info/info/unicode/char/0069/index.htm
__ https://en.wikipedia.org/wiki/IDN_homograph_attack
__ https://www.punycoder.com/


.. _permalink:
    /blog/2016/08/26/HomographAttacks.html
