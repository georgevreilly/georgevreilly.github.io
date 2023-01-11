---
title: "Third-Party Cookies"
date: "2009-10-16"
permalink: "/blog/2009/10/16/ThirdPartyCookies.html"
tags: [web]
---



.. image:: https://cache.gawker.com/assets/images/lifehacker/2009/08/C_is_for_Cookie.jpg
    :alt: C is for Cookie
    :target: http://lifehacker.com/5334984/web-sites-using-flash-instead-of-browser-cookies-to-track-your-activity
    :width: 200
    :class: right-float

Over the last few weeks,
I built a PHP application that `overlays Approve 71 banners on profile pictures`_.
The actual application is hosted in an iframe
and lives on a server in a different domain, ``eq.dm``,
than the main server at ``approvereferendum71.org``.

This works fine in most browsers.
Then we started getting reports that it wasn't working in IE8 on Win7 RC1.
The iframe content was blank.

Poking around, I found the problem with the `Fiddler proxy`_.
The landing page on ``eq.dm`` was supposed to stick some information into the PHP session,
then redirect to a second page at the same site.
The second page was in an endless loop, redirecting to itself.
In Fiddler, I saw a different PHPSESSID cookie on each response,
and no cookie in the requests.

After reading `IE 8 only has access to session cookies`_,
I told IE8 to Accept All Cookies and the iframe content appeared.
That fixed it for me, but we could hardly ask people to lower their security sessions.

I created a P3P file for the second domain, using the `IBM P3P Policy Editor`_.
(`KB 323752`_ has more background on P3P and third-party cookies.)

IE now worked at its default security level.
Problem solved!
Or so I thought.

A day later, we got reports of similar problems with Safari 4 on Mac OS X.

I sniffed the traffic with `Wireshark`_.
Same problem: the “third-party“ cookie wasn't being accepted by Safari.

Unfortunately, `Setting cross-domain cookies in Safari`_
indicated that there was no reasonable workaround.

We overcame the issue up playing some DNS games,
which was only possible because we control both servers.
The second server is now also acting as a subdomain of the first,
at ``dev.approvereferendum71.org``.
We used ``ini_set("session.cookie_domain",".approvereferendum71.org")``
to scope the iframe cookies.
I've tried it in a variety of Windows, Mac, and Linux browsers,
and it works in all of them.


.. _overlays Approve 71 banners on profile pictures:
    http://approvereferendum71.org/create-a-profile-picture
.. _Fiddler proxy:
    http://www.fiddler2.com/fiddler2/
.. _IE 8 only has access to session cookies:
    http://stackoverflow.com/questions/1003490/ie-8-only-has-access-to-session-cookies
.. _KB 323752:
    http://support.microsoft.com/default.aspx/kb/323752/EN-US/
.. _IBM P3P Policy Editor:
    http://www.alphaworks.ibm.com/tech/p3peditor
.. _Wireshark:
    http://www.wireshark.org/
.. _Setting cross-domain cookies in Safari:
    http://stackoverflow.com/questions/408582/setting-cross-domain-cookies-in-safari

.. _permalink:
    /blog/2009/10/16/ThirdPartyCookies.html
