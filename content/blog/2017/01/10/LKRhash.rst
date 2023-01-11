---
title: "LKRhash: Scalable Hash Tables"
date: "2017-01-10"
permalink: "/blog/2017/01/10/LKRhashScalableHashTables.html"
tags: [hashtables, performance, til]
---



LKRhash is a hashtable that scales to multiple processors and to millions of items.
LKRhash was invented at Microsoft in 1997
by Per-Åke (Paul) Larson of Microsoft Research
and Murali Krishnan and George Reilly of Internet Information Services.
LKRhash has been used in many Microsoft products.
The techniques that give LKRhash its performance
include `linear hashing`__, cache-friendly data structures, and fine-grained locking.

* `Northwest C++ Users' Group talk`__, June 2012. `Speaker Deck Slides`__.
* `Unpublished paper`__ submitted to `Software: Practice & Experience`__ (Oct 1999).
* `US 6,578,131 patent`__. Associated PDF__ contains some of the SP&E paper.

If Microsoft had had `20% time`__,
LKRhash would have been my main 20% project.
I put a lot of effort into making it a polished, well-tuned library
that was used in multiple products across the company.
I even ported the C++ code to kernel mode,
though it never ended up in a production driver, as far as I know.
Several years ago, after I left Microsoft,
I attempted to get it open-sourced.
However, despite some help on the inside,
we were never able to surmount the legal barriers.

__ https://en.wikipedia.org/wiki/Linear_hashing
__ http://nwcpp.org/june-2012.html
__ https://speakerdeck.com/georgevreilly/lkrhash-the-design-of-a-scalable-hashtable
__ /content/LKRhash-for-SoftwarePE.pdf
__ http://www.wiley.com/WileyCDA/WileyTitle/productCd-SPE.html
__ https://patents.google.com/patent/US6578131B1/en
__ https://www.google.com/patents/US6578131.pdf
__ https://qz.com/115831/googles-20-time-which-brought-you-gmail-and-adsense-is-now-as-good-as-dead/

.. _permalink:
    /blog/2017/01/10/LKRhashScalableHashTables.html
