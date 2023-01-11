---
title: "Fog is my Copilot"
date: "2006-05-20"
permalink: "/blog/2006/05/20/FogIsMyCopilot.html"
tags: [tech]
---



.. image:: https://www.copilot.com/blog/Images/logo.jpg
    :alt: Fog Creek's Copilot
    :target: https://www.copilot.com/
    :class: right-float

I mentioned last week that `my parents have no aptitude for computers
</blog/2006/05/15/WritingClearly.html>`_.

My father emailed me with a list of computer woes; notably, he was getting
messages about no firewall. There was no way I was going to get to the
bottom of the issue just by email or talking to him on the phone. It's 
5,000 miles from Seattle to Dublin, so I can't drop by to take a look at
the computer in person--much as my parents would like to have me visit.

I had tried using the built-in Windows Remote Assistance to troubleshoot
issues on their laptop a couple of years ago, while they were on a
protracted stay in Cape Town. I had solved the problem, but that had been
fairly painful for me. The primary problem was the horrible sluggishness of
the connection: they were on a slow dialup connection and the latency is
something fierce. Another problem was the fragility of my control: if I
dismissed a dialog by hitting Escape, I stopped controlling the remote
desktop, and as a `longtime vi user
</blog/2005/12/30/20YearsOfVi.html>`_, I have certain
deeply ingrained reflexes that are hard to overcome.

I decided to try out `Joel Spolsky's Copilot
<http://www.joelonsoftware.com/articles/AardvarkMidtermReport.html>`_.
The Copilot service `builds on TightVNC <https://www.copilot.com/tech/>`_.
The helper and the person being helped both make outbound connections to a
Copilot server, which proxies the virtual session, neatly avoiding all
kinds of NAT issues that can arise when you try to make a direct connection
through a firewall. It's also supposedly easy to configure, requiring only
a visit to the `Copilot website <https://www.copilot.com/>`_ and typing in
an email address or a 12-digit number, before downloading a half-megabyte
executable.
It wasn't too painful to talk my father through making the connection,
though the first time that he did it, he "lost" the binary and had to
download it again. We initially tried the two-minute trial version, but
that wasn't nearly enough time to do anything, so I shelled out the $10 for
a day pass.

In Dublin, as in Cape Town, he dials up to the Internet on a 56K modem, and
that once again proved to be the primary source of pain for me. It seemed a
little less sluggish than I remembered Remote Assistance being, but I
wasn't about to subject myself to trying that out too. The experience
varied between tolerable and infuriating, but there's only so much that can
be done at a little over 3Kbps.

The second reason the experience was so painful was that I ended up needing
to repair the eTrust installation, and to download a full set of antivirus
signatures, and I simply couldn't do it. The eTrust FTP site kept dropping
the connection, and the full signature package takes over 20 minutes to
download. I blame the FTP server, as I was VPN'd in to his laptop the
whole time, so his Internet connection was obviously working. I eventually
gave up at 4AM PDT, in utter frustration.

*Verdict*. Copilot works fairly well, although it can be painful over a
dialup connection. I would have killed for a file-transfer facility so that
I could send files directly between his computer and mine. $10 for a day
pass isn't cheap, but he gets to pay it in future! I use Terminal Server
and Virtual PC regularly: both of them provide ways to press all of the
Windows keys
(`Terminal Server <http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/mstsc_use_shortcut_keys.mspx>`_,
`Virtual PC <http://www.techgalaxy.net/Docs/VirtualPC/Keyboard_shortcuts.htm>`_);
Copilot doesn't.

.. _permalink:
    /blog/2006/05/20/FogIsMyCopilot.html
