---
title: "Northwest Python Day 2009"
date: "2009-02-01"
permalink: "/blog/2009/02/01/NorthwestPythonDay2009.html"
tags: [python]
---



.. figure:: /content/binary/Eric-on-BuildBot.jpg
    :alt: Eric on BuildBot
    :target: http://www.seapig.org/NorthwestPythonDay

    [Eric holding forth on BuildBot_]

Eric and I attended `Northwest Python Day 2009`_ today at the University of Washington.
There were about 50 people present, with a few out-of-town visitors from
Portland and Vancouver BC.

It was a mixed bag.
I found the afternoon sessions more interesting than the morning ones.

The morning talks started with a set of five-minute lightning talks, including:

* ctypes_ being used to crack open a raw binary file with arbitrary bit alignment.
* Werkzeug_: a set of WSGI utilities. Debugger sounds particularly useful.
* BuildBot_: Eric talked about using it for Continuous Integration and
  how easy it was to configure and extend, compared to `CruiseControl.NET`_.

.. _Northwest Python Day 2009:
    http://www.seapig.org/NorthwestPythonDay
.. _ctypes:
    http://docs.python.org/library/ctypes.html
.. _Werkzeug:
    http://werkzeug.pocoo.org/
.. _BuildBot:
    http://buildbot.net/trac
.. _CruiseControl.NET:
    http://ccnet.thoughtworks.com/

*Browser Interface, Local Server*: creating a desktop app
that contains, in one process, both a browser app and a local HTTP server,
running on separate threads.
The browser app can also be used to connect to a remote web server.
Used wxPython_ to host an HTML control for the browser part.

The afternoon lightning talks included:

* `Sphinx`_: a documentation generator built on top of `reStructuredText`_.
* `NodeBox`_: a Mac app for creating 2D visuals.
* vmshell: a not-yet-released toolkit for manipulating virtual machines using `libvirt`_.

.. _wxPython:
    http://www.wxpython.org/
.. _Sphinx:
    http://sphinx.pocoo.org/
.. _reStructuredText:
    /blog/2008/11/24/reStructuredText.html
.. _libvirt:
    http://libvirt.org/
.. _NodeBox:
    http://nodebox.net/code/index.php/Home

`Sage`_ is an impressive open-source package for doing mathematics,
and a potential alternative to expensive commercial products
like Mathematica and Matlab.
Browse the `Sage Notebook`_ to get a feel for what it can do.
Talk a look at today's `Sage talk`_.

`Google App Engine`_ is good for a narrow class of apps:
HTTP, request+response, time-limited, sandboxed.
There are many quotas, known and unknown.
The non-relational data store has restricted queries:
no joins, only complete entities, limited comparisons.

`Cython`_ is a Python-to-C compiler that seems promising.
It requires slight modifications to the classes and functions
that will be compiled to C: declare them with the ``cdef`` keyword.
It offers significant speedups for hotspot code
and it's heavily used in Sage.

.. _Sage:
    http://www.sagemath.org/
.. _Sage Notebook:
    http://www.sagenb.org/
.. _Sage talk:
    http://www.sagenb.org/home/pub/198/
.. _Google App Engine:
    http://en.wikipedia.org/wiki/Google_App_Engine
.. _Cython:
    http://www.cython.org/

`Ted Leung`_ closed the day by talking about Python at Sun.
All of the dynamic languages have been trending upwards
in the last few years, hence Sun's (and Microsoft's)
interest in dynamic languages.
`Jython`_, after years of struggling along, is alive and well.
I really have to check out `DTrace`_ on Mac or OpenSolaris soon.
One way to win mindshare for Python is better tools:
`NBPython`_ will provide Python support for the NetBeans IDE:
code completion, debugger, etc.

.. _Ted Leung:
    http://www.sauria.com/blog/
.. _Jython:
    http://www.jython.org/
.. _DTrace:
    http://www.valuedlessons.com/2008/10/how-to-dtrace-python-in-osx.html
.. _NBPython:
    https://nbpython.dev.java.net/

There were a handful of other talks that I didn't write up.

My thanks to the organizers for putting together a successful free conference.

.. _permalink:
    /blog/2009/02/01/NorthwestPythonDay2009.html
