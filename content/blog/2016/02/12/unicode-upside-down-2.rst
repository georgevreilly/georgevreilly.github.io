---
title: "Unicode Upside-Down Mapping, Part 2"
date: "2016-02-12"
permalink: "/blog/2016/02/12/UnicodeUpsideDownMappingPart2.html"
tags: [font, unicode, til]
---



`Yesterday`_ I showed FileFormat's `ɹǝʇɹǝʌuoↃ uʍo◖-ǝpısd∩ ǝpoɔıu∩`_.
Although the lowercase letters generally looked good,
several of the uppercase letters and numerals were unsatisfactory.
Looking through the `Unicode Table`_ site,
I came across the `Fraser Lisu alphabet`_,
which is unfortunately not well supported in most fonts.
The following renders in Hack_ and `Source Code Pro`_ in MacVim,
but not in the `Source Code Pro webfont`_ from Google Fonts::

    B: ꓭ u+A4ED  Lisu Letter Gha
    D: ꓷ u+A4F7  Lisu Letter Oe
    J: ꓩ u+A4E9  Lisu Letter Fa
    K: ꓘ u+A4D8  Lisu Letter Kha
    L: ꓶ u+A4F6  Lisu Letter Uh
    R: ꓤ u+A4E4  Lisu Letter Za
    T: ꓕ u+A4D5  Lisu Letter Tha
    U: ꓵ u+A4F5  Lisu Letter Ue
    V: ꓥ u+A4E5  Lisu Letter Nga

In `Number Forms`_, I also found upside-down forms of ``2`` and ``3``,
as well as vulgar fractions and Roman numerals.
Unfortunately, Turned Digit Two and Turned Digit Three don't render in many fonts,
including Hack and Source Code Pro::

    2: ↊ u+218A  Turned Digit Two
    3: ↋ u+218B  Turned Digit Three

I also found this for ``2``, which does work in most fonts::

    2: ꯖ u+ABD6  Meetei Mayek Letter Jil

Looking at `UpsideDownText`_, I found some other digit forms,
which also work in most fonts::

    1: Ɩ u+0196  Latin Capital Letter Iota
    5: ϛ u+03DB  Greek Small Letter Stigma
    7: ㄥ u+3125  Bopomofo Letter Eng

.. _Yesterday:
    /blog/2016/02/11/UnicodeUpsideDownMapping.html
.. _ɹǝʇɹǝʌuoↃ uʍo◖-ǝpısd∩ ǝpoɔıu∩:
    http://www.fileformat.info/convert/text/upside-down.htm
.. _Unicode Table:
    http://unicode-table.com/en/
.. _Fraser Lisu alphabet:
    http://unicode-table.com/en/blocks/lisu/
.. _Hack:
    http://sourcefoundry.org/hack/
.. _Source Code Pro:
    https://en.wikipedia.org/wiki/Source_Code_Pro
.. _Source Code Pro webfont:
    https://www.google.com/fonts/specimen/Source+Code+Pro
.. _Number Forms:
    http://unicode-table.com/en/blocks/number-forms/
.. _UpsideDownText:
    http://www.upsidedowntext.com/unicode

.. _permalink:
    /blog/2016/02/12/UnicodeUpsideDownMappingPart2.html
