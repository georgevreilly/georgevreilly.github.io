---
title: "Greasemonkey for demos and mockups"
date: "2007-10-11"
permalink: "/blog/2007/10/11/GreasemonkeyForDemosAndMockups.html"
tags: [programming, javascript, til]
---



.. image:: https://www.wired.com/wired/archive/13.09/images/ST_34_monkey1_f.jpg
    :alt: Greasemonkey
    :target: http://www.greasespot.net/

I've been meaning to play around with `Greasemonkey`_ for a couple of years.
Greasemonkey is a Firefox extension that allows users to install
scripts that make on-the-fly changes to the look and feel of third-party websites.
For example, adding price comparisons to Amazon
or thumbnail images to Google search results.
`UserScripts.org`_ has a large repository of Greasemonkey scripts.

I finally built my first script the other day.
We're putting together a new feature at `Cozi`_ that integrates
partner websites with our site.
Since the feature is not yet announced, I'll just say that partners
will add a link to Cozi on many of their database-driven pages.
That link has a complex, page-dependent querystring.
Until the partners do the work to add the link to their sites,
we were limited to testing and demoing with hand-modified pages.

I wrote a little Greasemonkey script that finds the right spot
on the partner pages to place the link,
scrapes some context to construct the querystring,
and inserts the link.
Now we can test against the real sites and show a compelling demo.
Of course, it only works on Firefox and it requires you to
install both Greasemonkey and this script.
Our partners will have to make minor changes to their sites
before ordinary users can take advantage of the feature.

Some gotchas with Greasemonkey.
Inserting, say, ``<b>Click here</b>`` is as simple as
``document.getElementById('spot').innerHTML = <b>Click here</b>``.
However, inserting a ``<script>`` node requires:

.. code-block:: javascript

    var scr = document.createElement('script');
    scr.type = 'text/javascript';
    scr.text = 'createLink(' + p1 + ', ' + p2 + ', ' + p3 + ');';
    document.getElementById('spot').appendChild(scr);

Greasemonkey will definitely become part of my repertoire.

.. _Greasemonkey:
    http://www.greasespot.net/
.. _UserScripts.org:
    http://userscripts.org/
.. _Cozi:
    http://www.cozi.com/

.. _permalink:
    /blog/2007/10/11/GreasemonkeyForDemosAndMockups.html
