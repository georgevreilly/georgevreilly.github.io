---
title: "Skype and SSL"
date: "2005-11-17"
permalink: "/blog/2005/11/17/SkypeAndSSL.html"
tags: [tech, til]
---



A year ago, I ran into a problem with `Skype squatting on port 80`__,
which I had long forgotten about.
Today, I ran into one with Skype squatting on port 443.

__ http://weblogs.asp.net/george_v_reilly/archive/2004/09/15/230281.aspx

I was trying to set up SSL on my Windows Server 2003 dev box.
My ultimate goal is to experiment with client certs and server certs for SOAP,
but that's a story for another time.
I was running into all kinds of strange problems,
exacerbated by the relatively strange IIS configuration on my machine.

I tried SslDiag__.
In hindsight, it pointed me towards the underlying problem,
but I couldn't see it at the time.
I did a lot of digging around on Google.
Eventually, a `newsgroup thread`__ on ListenOnlyList gave me CurrPorts__,
which showed me that Skype was listening on port 443.
I suppose ``netstat -anob``, TcpView__, or `Port Reporter`__
would have told me the same thing,
though CurrPorts had the friendliest view.
WFetch from the `IIS 6 Resource Kit Tools`__ was also useful
in looking at raw requests and responses.

__ https://www.iis.net/downloads/community/2009/09/ssl-diagnostics-tool-for-iis-7
__ http://www.issociate.de/board/goto/1018679/server2003_and_default_website.html%23msg_1018679
__ http://www.nirsoft.net/utils/cports.html
__ https://technet.microsoft.com/en-us/sysinternals/tcpview.aspx
__ http://blogs.msdn.com/brianjo/archive/2004/09/08/227133.aspx
__ http://www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/993a8a36-5761-448f-889e-9ae58d072c09.mspx

.. _permalink:
    /blog/2005/11/17/SkypeAndSSL.html
