---
title: "New Compression Formats"
date: "2016-08-31"
permalink: "/blog/2016/08/31/NewCompressionFormats.html"
tags: [tech, compression, til]
---



You might think that data compression is a solved problem, lossless or lossy.
But, no.
Gzip and related formats like zlib, Zip, and PNG that use the DEFLATE__ algorithm
were great 25 years ago, still do a decent job, and are completely ubiquitous and indispensable,
but there are better, smarter algorithms now.

Google has announced two new compression formats in the last couple of years,
Zopfli and Brotli.
Zopfli__ does a better job of generating Deflate-compatible data,
although it's very slow.
Brotli__ gives ~20% better compression than Deflate, but at about the same speed.
Then there's xz__, which grew out of 7-zip, and also works well.

Zstandard__ has just been announced by Facebook
and it sounds like it does a great all-round job
of achieving high compression ratios at high speed.
The announcement article is worth reading.

There are also several new lossless image compression algorithms:
FLIF__, BPG__, and WebP__, all of which outperform__ the venerable PNG.


__ https://en.wikipedia.org/wiki/DEFLATE
__ https://en.wikipedia.org/wiki/Zopfli
__ https://en.wikipedia.org/wiki/Brotli
__ https://en.wikipedia.org/wiki/Xz
__ https://code.facebook.com/posts/1658392934479273/smaller-and-faster-data-compression-with-zstandard/
__ http://flif.info/
__ https://en.wikipedia.org/wiki/Better_Portable_Graphics
__ https://en.wikipedia.org/wiki/WebP
__ http://cloudinary.com/blog/flif_the_new_lossless_image_format_that_outperforms_png_webp_and_bpg

.. _permalink:
    /blog/2016/08/31/NewCompressionFormats.html
