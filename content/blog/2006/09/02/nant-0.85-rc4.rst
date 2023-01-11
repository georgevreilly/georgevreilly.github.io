---
title: "Upgrade your installation of NAnt"
date: "2006-09-02"
permalink: "/blog/2006/09/02/UpgradeYourInstallationOfNAnt.html"
tags: [programming, .NET]
---



.. image:: https://nant.sourceforge.net/logo.gif
    :alt: NAnt
    :target: http://nant.sourceforge.net/release/0.85-rc4/releasenotes.html
    :class: right-float

My colleague, Greg, and I spent all day debugging a build break in
some unit tests that exercise a webservice interface in legacy .NET 1.1 code.
Last night, the tests stopped working on our
`CruiseControl.NET <http://ccnet.thoughtworks.com>`_
build server. We couldn't understand it. The tests had been working for
months. Now we were getting timeouts in SOAP. The tests essentially
`mock <http://en.wikipedia.org/wiki/Mock_object>`_
a SOAP service using the ``soap.inproc`` transport and a stub
implementation that signaled an event to acknowledge a method being called.

The only thing that had changed in the code tree was that another
colleague, Pavel, had discovered that two of our ``.csproj`` files somehow
shared the same GUID, and had repaired that. But that could hardly have any
effect on the WSE2 runtime. Could it?

Turns out that it was the cause of the break.
NAnt 0.85 rc2 and rc3 silently failed to build the
NUnit assembly because of the duplicated GUIDs. The assembly was not
getting propagated to the directory where all the other NUnit assemblies
are placed. The CC.NET task that ran the tests never noticed the missing
assembly because the test was couched in terms of ``*.NUnit.dll``. And we
never noticed that the test hadn't been run in months because we have ~20
such NUnit assemblies, and the NUnit summary output goes on for several
screens in CC.NET.

**Morals of the story**

#. Use `NAnt 0.85 rc4
   <http://nant.sourceforge.net/release/0.85-rc4/releasenotes.html>`_, which
   detects the GUID collision and treats it as a fatal error.
#. Create ``.csproj`` files through the IDE, not by taking an existing file
   and hacking on it. (At least, that's we assume happened.)
#. Assumptions can bite you. We assumed that the code was being run all
   along, so it took us several hours to draw the connection between
   Pavel's checkin and the failing NUnit assembly.
#. Don't mock a webservice by implementing a dummy ``SoapReceiver``,
   hauling in the WSE runtime and a boatload of non-determinism.
   (Instead, make fun of its dress sense.)
   For our newer code, we've been taking an approach
   `like this
   <http://blogs.msdn.com/davidwaddleton/archive/2006/08/03/687841.aspx>`_,
   using ``partial`` classes and `Rhino Mocks
   <http://www.ayende.com/projects/rhino-mocks.aspx>`_.
#. We have also taken to including our test fixtures in the same
   assemblies as the code they test. I have mixed feelings about this:
   it offends my sensibilities to have all this test code compiled into
   production code. But it would certainly have been hard to miss the
   build break in production code.

.. _permalink:
    /blog/2006/09/02/UpgradeYourInstallationOfNAnt.html
