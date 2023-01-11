---
title: "Max audio extractor"
date: "2009-05-04"
permalink: "/blog/2009/05/04/MaxAudioExtractor.html"
tags: [tech, music]
---



.. image:: https://sbooth.org/Max/images/logo.png
    :alt: Max
    :target: http://sbooth.org/Max/
    :class: right-float

I blogged before that I had used `Exact Audio Copy`_
to rip most of my CD collection to the lossless FLAC_ format.
I haven't ripped any more CDs since then,
as the old Windows laptop that I was using had severe problems.

We went to the `Columbia City Beatwalk`_ on Friday night.
I liked the `Correo Aereo`_ duo so much that I bought their CD.

It was time to figure out how to rip a CD to FLAC on the Mac.
I found some hints that it was possible to run Exact Audio Copy
in a virtual machine or under Wine,
but neither choice appealed to me.

One guide_ recommended xACT_ over Max_ on the grounds
that xACT will tell you exactly where an error occurs on a CD,
should one occur, while Max only gives a percent encoded successfully.
What you do if an error occurs was not described.

I tried xACT first.
It's a thin wrapper around various command-line utilities.
The guide_ details a clunky process to rip a CD to FLAC.

Then I tried Max and I was greatly impressed.
The UI is polished for an open-source app.
It rips to WAV, then encodes to multiple formats if you want.
It can also transcode over 20 audio formats.
Max is multithreaded:
it can be encoding a WAV from one track to FLAC and MP3 simultaneously,
while ripping the next track from the CD.
Exact Audio Copy rips a track to WAV, then encodes to FLAC, without overlapping.
Net result is that Max rips a CD about four times faster than EAC.
A lot has to do with the hardware.
My five-year-old Windows laptop was not high-end even when brand new.
My two-year-old Core 2 Duo MacBook Pro was top of the line.

I no longer have to run a Python script to convert all the FLACs to MP3s.
Max puts both sets of files in the same folder,
so I had to write a small script to split them into two separate trees.
Otherwise, I'm very happy with Max.


.. _Exact Audio Copy:
    /blog/2008/11/18/HardwareLazarus.html
.. _FLAC:
    http://en.wikipedia.org/wiki/Free_Lossless_Audio_Codec
.. _Max:
    http://sbooth.org/Max/
.. _Correo Aereo:
    http://www.correoaereo.com/
.. _Columbia City Beatwalk:
    http://www.columbiacitybeatwalk.org/
.. _guide:
    http://puddletowndesign.com/FLAC/macRipping
.. _xACT:
    http://sourceforge.net/projects/xact

.. _permalink:
    /blog/2009/05/04/MaxAudioExtractor.html
