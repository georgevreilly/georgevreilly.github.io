---
title: "Path Traversal Attacks"
date: "2021-10-05"
permalink: "/blog/2021/10/05/PathTraversalAttacks.html"
tags: [iis, security, unicode]
---



I was surprised to read this evening that the Apache Web Server
just fixed an actively exploited path traversal flaw.

__ https://github.com/apache/httpd/commit/4c79fd280dfa3eede5a6f3baebc7ef2e55b3eb6a

.. raw:: html

    <blockquote class="twitter-tweet">
    <p lang="en" dir="ltr">
    🚨 Apache has disclosed an *actively exploited* Path traversal flaw
    in the <a href="https://twitter.com/hashtag/opensource?src=hash&amp;ref_src=twsrc%5Etfw">#opensource</a>
    &quot;httpd&quot; server.
    Over 112,000 exposed Apache servers run version 2.4.49,
    and should be upgraded now!<br>
    New fix checks for encoded path traversal characters
    e.g. /../.%2E/<a href="https://t.co/1tLNc3LAul">https://t.co/1tLNc3LAul</a>
    <a href="https://t.co/mDHLEU3k9N">pic.twitter.com/mDHLEU3k9N</a>
    </p>&mdash; Ax Sharma (@Ax_Sharma)
    <a href="https://twitter.com/Ax_Sharma/status/1445391350053183500?ref_src=twsrc%5Etfw">October 5, 2021</a>
    </blockquote>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Apparently, it was `introduced over a year ago`__.

I'm gobsmacked that Apache didn't have a robust suite of tests for this.

Directory Traversal attacks have been a problem for web servers
since the beginning.
OWASP_, PortSwigger_, and Spanning_ all have explanations that you can read.
The essence is that you make a request to a URL that looks like
``http://example.com/cgi-bin/../../../../etc/passwd``
and, voilà, you get access to something that you shouldn't.
Each of the ``..`` path segments climbs up a level of the file system.
Even the simplest web server knows better than to blindly allow
a sequence of ``..`` path segments,
so you have to be a little clever about how you express them.

IIS Unicode Exploit
===================

I remember when I worked on the IIS development team at Microsoft in 1997–2004,
we got hit by `CVE-2000-0884`_ in 2000,
which made use of an `overlong UTF-8 encoding`_.

URLs allow `percent encoding`_ for characters that can't be sent literally.
For example, ``%3D`` encodes an ``=``
as the two-digit hexadecimal value of ``=``\ ’s ASCII code.
UTF-8 characters beyond U+007F require two or more bytes of storage,
each of which can be percent encoded;
e.g., U+00C1 (``Á``) is encoded as the ``C3 81`` byte pair in UTF-8,
and as ``%C3%81`` in percent encoding.

The slash character, ``/`` or U+002F, can be percent encoded as ``%2F``.
IIS 4 and 5 were smart enough to treat ``%2F`` as a slash
and to defend against sequences like ``..%2F..%2F``.
However, the attackers encoded a slash as ``%C0%AF``\ —\
a sequence that is burned into my brain.
This two-byte UTF-8 sequence can be decoded as U+002F,
though it should not be treated as valid
as it is overlong_:
the five payload bits in the leading byte are all zero.

The `GIAC paper`_ explains in some detail how this could be exploited.

Windows Security Push
=====================

Windows XP went on sale in late 2001,
touted as the most secure version of Windows ever.
(It was, at that time.)

Right around Christmas 2001,
the `UPnP vulnerabilty`_ was disclosed.
Brian Valentine, the Senior VP who ran Windows, threw a shitfit.
It was announced that *all* of Windows would spend the month of February 2002
undergoing security training,
so that we could `threat model`_ and review our code.

For IIS 6, which would be released in Windows Server 2003,
we had fundamentally rearchitected it with a new worker process model
(inspired by Apache's) and we had rewritten much of it.
There was a new kernel mode driver, http.sys,
that terminated all requests and routed them
to the appropriate handler in kernel or user mode.
I was part of the http.sys dev team at that point.

IIS had already gotten serious about security by then.
We had to, after `Code Red`_, Nimda_, the Unicode exploit, and others.
`Mike Howard`_ had been the IIS Security Program Manager
before he went on to bigger responsiblities.
A lot of the first edition of his `Writing Secure Code`_ book
was based on his experience with securing IIS,
and a lot of the second edition benefited from the Security Push experience.

Since http.sys was new and an obvious target,
our team actually spent two months carefully reviewing everything.
It turned out that we had done a good job over the previous couple of years
and we didn't find much to worry about.

We did identify that the URL canonicalization in http.sys
was overly complicated.
I rewrote that component and I created a ton of unit tests for it.
Developers writing unit tests was not common at Microsoft back in 2002:
we had a separate caste of testers to write tests.

I've been out of the loop since I left IIS in 2004,
but to my knowledge, there were no further vulnerabilities in URL handling.

I'm surprised and disappointed that Apache would mess up path traversal in the 2020s.

.. _OWASP:
    https://owasp.org/www-community/attacks/Path_Traversal
.. _PortSwigger:
    https://portswigger.net/web-security/file-path-traversal
.. _Spanning:
    https://spanning.com/blog/directory-traversal-web-based-application-security-part-8/
.. _CVE-2000-0884:
    https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0884
.. _overlong UTF-8 encoding:
.. _overlong:
    https://en.wikipedia.org/wiki/UTF-8#Overlong_encodings
.. _percent encoding:
    https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding
.. _GIAC paper:
    https://www.giac.org/paper/gcih/115/iis-unicode-exploit/101163
.. _UPnP vulnerabilty:
    https://www.giac.org/paper/gcih/274/windows-xp-upnp-exploits/102906
.. _threat model:
    https://owasp.org/www-community/Threat_Modeling
.. _Code Red:
    https://en.wikipedia.org/wiki/Code_Red_(computer_worm)
.. _Nimda:
    https://en.wikipedia.org/wiki/Nimda
.. _Mike Howard:
    https://www.linkedin.com/in/mikehow/
.. _Writing Secure Code:
    https://www.amazon.com/Writing-Secure-Second-Developer-Practices/dp/0735617228

.. _permalink:
    /blog/2021/10/05/PathTraversalAttacks.html
