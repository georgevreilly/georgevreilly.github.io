---
title: "dasBlog 1.8 and w.bloggar"
date: "2005-11-12"
permalink: "/blog/2005/11/12/dasBlog18AndWbloggar.html"
tags: [dasblog]
---



I finally updated my blog to run on dasBlog 1.8.
Not too painful.
I unzipped the binary distribution,
downloaded the content folder from my server to my local drive,
ran the provided upgrade utility,
and used WinMerge to update the configuration files.

The most obvious change is that I'm using a new theme (skin),
which gives the site a very different look.
The previous default theme had problems if your browser window was too narrow,
due to some hardcoded table sizes (I think).

I also figured out how to post to dasBlog via w.bloggar.
I looked for info on configuring w.bloggar a few weeks ago, and couldn't find it then.

Followup: the multiword links in this post are mangled when they appear in a browser.
I think this is an issue in dasBlog's XML transforms.
Specifically, it only seems to happen when the multiword link contains "dasBlog":
ego-surfing, perhaps.
Reported as dasBlog bug 1354987.

Followup #2: the problem turned out to be
one of the out-of-the box rewriting rules in site.config.
Commenting out::

      <ContentFilter find="dasBlog" ...

fixed it.

These rules seem to be generally useful.
The default configuration allows you to convert several varieties of smilies to graphics:

========    =======
Code        Result
========    =======
``:-o``	    :-o
``:-S``	    :-S
``:-D``	    :-D
``:'(``	    :'(
``;-)``	    ;-)
``:-)``	    :-)
========    =======

as well as Google searches,
$g(bush sucks) → bush sucks,
and dictionary.com lookups,
$d(defenestration) → defenestration.
(The preceding examples were escaped by bracketing the first character
in the pattern with a ``<span>`` tag.)

[Note: the above examples no longer display correctly,
as this site is no longer hosted on dasBlog.]

More details on ContentFilter at the new dasBlog documentation site,
http://dasBlog.info.

.. _permalink:
    /blog/2005/11/12/dasBlog18AndWbloggar.html
