---
title: "Using Log4Net from a COM+ Application"
date: "2006-08-29"
permalink: "/blog/2006/08/29/UsingLog4NetFromACOMApplication.html"
tags: [.NET, til]
---



.. image:: https://logging.apache.org/log4net/images/ls-logo.jpg
    :alt: Log4Net
    :target: https://logging.apache.org/log4net/

I spent far too much time on Friday trying to make `log4net`__ work in a COM+ application.

Someone else had done part of the work necessary,
by creating an `application.config`__ for the COM+ application 
and setting a custom Application Root Directory. 
This was enough to ensure that most of the managed code in the application 
got their configuration settings;
log4net being the exception.

It took some additional work to realize that we needed to add two assembly attributes:

::

    [assembly: log4net.Config.Repository("unique-name")]
    [assembly: log4net.Config.XmlConfigurator(ConfigFile="application.config")]

The repository name just needs to be a unique string.
We used the name of the assembly.

__ https://logging.apache.org/log4net/
__ http://blogs.msdn.com/florinlazar/archive/2003/12/04/41369.aspx

.. _permalink:
    /blog/2006/08/29/UsingLog4NetFromACOMApplication.html
